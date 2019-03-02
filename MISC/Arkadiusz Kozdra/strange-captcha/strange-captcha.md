# Strange captcha (misc/web, 400 pkt)
Arkadiusz Kozdra

# Treść
> THIS IS SKYNET SPEAKING HERE. IN ORDER TO BECOME A PART OF US, YOU MUST PROVE THAT YOU ARE A [HUMANOID CAPABLE OF DOING ELECTRICAL COMPUTATIONS EASILY](https://strange-captcha.ecsc18.hack.cert.pl) (HCDECE).
>
> Format flagi: `ecsc{litery_cyfry_i_znaki_specjalne}`.

# Rozwiązanie
Oczywiście ręcznie nie da się tego policzyć szybko, zwłaszcza, że tutaj
pojawia się licznik punktów, który resetuje się przy każdej złej odpowiedzi.

Układy elektryczne można rozwiązywać inteligentnie, ale w tym wypadku działa
też podejście przybliżania wyniku a'la binary search, można na to wpaść
po przeczytaniu akceptowanej wartości błędu względnego.

Trzeba zrobić skrypt, który będzie ściągał obrazek, zbierał z niego
informacje, wyliczał odpowiedź i wpisywał do przeglądarki.  Można
naturalnie użyć czegokolwiek, co wyśle żądanie POST, ale skorzystamy do tego
z `xdotool`, narzędzia m.in. do emulowania działania klawiatury i myszy.

Obrazek na szczęście jest w formacie SVG, więc nie trzeba robić
skomplikowanego OCR (chociaż gocr dawał radę), tylko wystarczy dobrze
mu się przyjrzeć.

Tekst zapisany jest szesnastkowo w tagach, `#DejaVuSans-3a9` daje U+03A9,
czyli `Ω` itp.  Trochę trudniej rozpoznać kierunek ogniw, ponieważ są
zapisane tylko w ścieżkach SVG, ale da się zrobić, na przykład sortując
ich rzędne.

Po uruchomieniu skryptu i stu poprawnych odpowiedziach, strona daje
flagę: `ecsc{electrical_captcha_lol}`.

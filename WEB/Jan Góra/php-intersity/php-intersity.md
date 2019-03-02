PHP Intersity (web, 150 punktów)
===
*Eliminacje do European Cyber Security Challenge - Seniorzy*
***Jan Góra, 14.02.2019**

>I work for a train operator company. Yesterday we've got an anonymous email which stated that there are some security problems with our tickets.
>
>The attacker said that he forged a ticket by exploiting crypto. It's not my domain and I could not understand what's wrong.
>
>I've bought a train ticket from Moscov to Novosibirsk. I've also made a debug endpoint where you can paste the ticket content (base64-encoded QR code contents) in order to check validity. There are also some debug prints there.
>
>Is it possible to somehow forge a ticket with another departure date?
>
>Format flagi: ecsc{litery_cyfry_i_znaki_specjalne}.

Mamy dwie strony do dyspozycji
Szyfrującą dane: https://php-intersity.ecsc18.hack.cert.pl/ticket/  i deszyfrującą https://php-intersity.ecsc18.hack.cert.pl/validate/. Po zaszyfrowaniu nazwy podróżującego, dostajemy kod QR https://php-intersity.ecsc18.hack.cert.pl/ticket/make_ticket.php?sid=ec0ca2efd8033ca21169a5f729fd3f88, który następnie dekodujemy przy użyciu: https://zxing.org/w/decode?u=https://php-intersity.ecsc18.hack.cert.pl/ticket/make_ticket.php?sid=ec0ca2efd8033ca21169a5f729fd3f88. Otrzymujemy string `6XVmefbLQ75yg76aNFVi4BgeRNINZ/alwYmIudSHJrPW5foePzS6ZtzRicNruGSeDl1zpC/KERYYm6N5CfquThzBot+fgSacQSdU3yMrb0K9B6HK49uHuimW2qVfzWUq`, który po odszyfrowaniu daje:
```
Ticket owner: aaaa

Raw decrypted:
7b2264617465223a22323031382d3033
2d3130222c2266726f6d5f7374617469
6f6e223a224d6f73766f76222c22746f
5f73746174696f6e223a224e6f766f73
69626972736b222c226f776e6572223a
2261616161227d000000000000000000
```

Po odszyfrowaniu bajtów na ASCII otrzymujemy:

```
{
    "date":"2018-03-10",
    "from_station":"Mosvov",
    "to_station":"Novosibirsk",
    "owner":"aaaa"
}
```

Spróbujmy zrobić JSON injection poprzez wpisanie nazwy podróżującego jako `", "date": "1337-13-37`, a następnie odszyfrujmy kod QR. Otrzymujemy:

```
1337-13-37: Mosvov - Novosibirsk

Ticket owner:

You have managed to forge a ticket. Here is your reward: ecsc{i_LIKE_traInZ!!!11111111}

Raw decrypted:
7b2264617465223a22323031382d3033
2d3130222c2266726f6d5f7374617469
6f6e223a224d6f73766f76222c22746f
5f73746174696f6e223a224e6f766f73
69626972736b222c226f776e6572223a
22222c202264617465223a2022313333
372d31332d3337227d00000000000000
00000000000000000000000000000000
```

wraz z flagą **ecsc{i_LIKE_traInZ!!!11111111}**

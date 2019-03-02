# Xorxorxor   crypto  Punkty: 25
# Łukasz Dzwoniarek

# pwn{revenge-of-the-xor}



Mamy zaszyfrowane dane za pomocą funkcji xor i nie znamy długości maski.

Sprawdzanie wszystkich możliwości było by czasochłonne, dlatego skorzystamy z narzędzia xortool.
-c 20 podajemy numer najczęstszego znaku (spacja)
Program nie sprawdza wszystkich możliwości, a jedynie "zgaduje" klucz, o danej długości tak, aby w odszyfrowanych danych najczęstrzym znakiem była spacja.

```console
$ xortool -c 20 xorxorxor_15cbeeb0e90cb28937edecb9a214eef1 
The most probable key lengths:
   1:   13.4%
   3:   13.0%
   6:   11.9%
  14:   9.0%
  21:   6.9%
  23:   20.7%
  26:   5.6%
  28:   5.3%
  31:   4.8%
  46:   9.5%
Key-length can be 3*n
1 possible key(s) of length 23:
pwn{revenge-of-the-xor}
Found 1 plaintexts with 95.0%+ printable characters
See files filename-key.csv, filename-char_used-perc_printable.csv
```
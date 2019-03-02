# Xorxor   crypto  Punkty: 25
# Łukasz Dzwoniarek

# pwn{cyber-cyber-co-z-ciebie-wyrosnie}

Mamy zaszyfrowane dane za pomocą funkcji xor i maski o długości 4 bajtów.

Sprawdzanie wszystkich możliwości było by czasochłonne, dlatego skorzystamy z narzędzia xortool.
-l 4 podajemy długość szykanego klucza
-c 20 podajemy numer najczęstszego znaku (spacja)
Program nie sprawdza wszystkich możliwości, a jedynie "zgaduje" klucz, o danej długości tak, aby w odszyfrowanych danych najczęstrzym znakiem była spacja.

# key
## \x92\x81\xa7\xbf = 2457970623
## (2 457 970 623 / 256) / 256 = 37505.6552582

# Fast answer
```console
$ xortool -l 4 -c 20 xorxor_b8cf1bd02512e3294f069089803d3840 
1 possible key(s) of length 4:
\x92\x81\xa7\xbf
Found 1 plaintexts with 95.0%+ printable characters
See files filename-key.csv, filename-char_used-perc_printable.csv

$ cat './xortool_out/0.out' 
Cyber may refer to:
    Cyber-, a common prefix
    Cybernetics
    Cybernetic organism (Cyborg)
    Cyber-attack
    Cybercafe or Internet cafe, a business which provides internet access
    Cyber crime
    Cybercrime and countermeasures
    Cybercrime Convention
        Cyber Crime Investigation Cell
    Cybercrime Prevention Act of 2012
    Cyber Crime Unit (Hellenic Police)
    Cyberculture emergent culture based on the use of computer networks
    Cybergoth
    Cyber Party
    Cybersecurity or computer security
    Cyber hygiene
    Cyberspace
    Cybersex (colloquially)
    Cyberwarfare
    Cyberflags (see pwn{cyber-cyber-co-z-ciebie-wyrosnie})
    CDC Cyber, a range of mainframe computers
```
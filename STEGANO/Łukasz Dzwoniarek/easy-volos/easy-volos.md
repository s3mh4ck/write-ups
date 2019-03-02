# Easy Volos  stegano  Punkty: 100
# Łukasz Dzwoniarek

# Zgodnie z wykładem
# ecsc{inflat3_or_d3flate}

W pliku png można ukryć dodatkowe dane, które nie są w żadnen sposób interpretowane przez programy graficzne. Uzyskujemy ten efekt poprzed odpiowiednie ustawienie wskaźników w pliku png.

W tym zadaniu ukryte pliki to jakieś skompresowane dane, które zawierają flagę zapisaną w ASCII.

```bash
# pobieramy obrazek
$ wget https://hack.cert.pl/files/volos-38f67b00df2f42c5ebe570ea31ae968b09224737.png
# wyciągamy ukryte pliki z obrazka i rozpakowujemy je
$ binwalk -e volos-38f67b00df2f42c5ebe570ea31ae968b09224737.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 288 x 479, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, best compression
381077        0x5D095         Zlib compressed data, default compression
# odczytujemy flagę ukrytą w obrazku
$ cat _volos-38f67b00df2f42c5ebe570ea31ae968b09224737.png.extracted/5D095
####################################################
####################################################
####################################################
####################################################
####################################################
########     ecsc{inflat3_or_d3flate}      #########
####################################################
####################################################
####################################################
####################################################
####################################################
```

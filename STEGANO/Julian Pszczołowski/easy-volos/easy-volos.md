Easy Volos, stegano, 100
Julian Pszczołowski

Należy pobrać plik `volos.png` ze strony https://hack.cert.pl/challenge/easy-volos. Następnie uruchomić program `binwalk` w ten sposób:
```
$ binwalk -e volos.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 288 x 479, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, best compression
381077        0x5D095         Zlib compressed data, default compression
```
Utworzył się katalog `_volos.png.extracted`, w którym znajduje się flaga znaleziona przez `binwalk`:
```
$ cat _volos.png.extracted/5D095
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
Jak widzimy, flaga to `ecsc{inflat3_or_d3flate}`.

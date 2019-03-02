# Learn Some Basics stegano Punkty: 50
# Łukasz Dzwoniarek

# ecsc{wow_much_crypto_very_secure}

```bash
# Pobieramy i "instalujemy" program do wyświetlania obrazków z filtrami
wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar
chmod +x stegsolve.jar
mkdir bin
mv stegsolve.jar bin/
# Uruchamiamy program
java -jar ./bin/stegsolve.jar 
```
Wybieramy File/Open/
Klikamy na strzałki pod obrazkiem i odczytujemy kolejne fragmenty flagi
```
Red plane 0     # ecsc{wow_much
Green plane 0   _crypto_
Blue plane 0    very_secure}
```
Znaleźliśmy czarno biały obrazek/napis ukryty na najmniej znaczącym bicie określającym jasność każdego z trzech składowych kolorów (czarwony, niebieski i zielony) na danym piskelu.

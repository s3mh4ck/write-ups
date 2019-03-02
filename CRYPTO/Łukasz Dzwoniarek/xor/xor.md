# Xor   crypto  Punkty: 25
# Łukasz Dzwoniarek

# pwn{almost-like-mr-robot}

Mamy zaszyfrowane dane za pomocą funkcji xor i maski o długości 1 bajta.

Odszyfrowujemy przy pomocy prog.py, który sprawdza wszystkie możliwe maski,
a następnie wybiera tą przy, ktorwej w ciągu wynikowym pojawia się napis 'pwn', 
o którym wiemy, że jest fragmntem flagi. 


```bash
python prog.py
```

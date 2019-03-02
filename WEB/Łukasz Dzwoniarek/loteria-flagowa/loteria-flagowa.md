# Loteria flagowa  web  Punkty: 100
# Łukasz Dzwoniarek

# pwn{U5e_M0ar_53cuR3_4and0m}


1. Otwieramy stronę internetową
<https://lottery.pwning2016.p4.team/>

2. Kopiujemy "Your user ID:", np.:
> LTIwNTc2MDc2MDIsLTAuMg==

3. Dekodujemy 
```bash
$ echo `echo LTIwNTc2MDc2MDIsLTAuMg== | base64 --decode`
```
> -2057607602,-0.2

4. Na podstawie kodu dołączonego do zadania obliczamy szczęśliwe liczby:
```javascript
var seed = -2057607602;
var m = 25, a = 11, c = 17, z = seed || 3;
for (i = 0; i < 7; i++) {
    z=(a*z+c)%m
    if( i == 0 ) {
        print("Test number is: " + z/m);
    }
    else {
        print(i + " lucky number is " + Math.floor(z/m*89+10));
    }    
}
```
> Test number is: -0.2
> 1 lucky number is -37
> 2 lucky number is 6
> 3 lucky number is 31
> 4 lucky number is 38
> 5 lucky number is 27
> 6 lucky number is 88

5. Wyłączamy sprawdzanie zakresu liczb na stronie (wpisując w konsolę w przeglądarce):
```javascript
document.querySelectorAll('input').forEach(a=>a.removeAttribute('pattern'));
```

6. Wpisujemy wyliczone liczby i dostajemy:
> Success! Your flag is pwn{U5e_M0ar_53cuR3_4and0m}
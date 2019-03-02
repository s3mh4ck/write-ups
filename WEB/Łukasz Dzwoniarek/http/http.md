# HTTP  web Punkty: 100
# Łukasz Dzwoniarek

# ecsc{too_many_encoded_headers}

```console
$ curl -v https://web-http.ecsc18.hack.cert.pl/ > out 2>&1 
$ curl -v https://web-http.ecsc18.hack.cert.pl/ 2>&1 | grep X-Secret | awk '{print $3}' | tr -d '\r\n' | base64 --decode | tr '[\000-\011\013-\037\177-\377]' '\n' | grep ecsc
```





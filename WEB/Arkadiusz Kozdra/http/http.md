# HTTP (web, 100 pkt)
Arkadiusz Kozdra

# Treść
> The flag is [somewhere there](https://web-http.ecsc18.hack.cert.pl/). Can you find it?
>
> Format flagi: `ecsc{litery_cyfry_i_znaki_specjalne}`.

# Rozwiązanie
Strona jest niemal pusta:

```html
<h1>Hi there!</h1>
```

Za to przez HTTP wysyłane są podejrzane nagłówki `X-Secret-*`.
```
$ curl -sv https://web-http.ecsc18.hack.cert.pl/ 2>>http.md
*   Trying 195.164.49.185...
* TCP_NODELAY set
* Connected to web-http.ecsc18.hack.cert.pl (195.164.49.185) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* Cipher selection: ALL:!EXPORT:!EXPORT40:!EXPORT56:!aNULL:!LOW:!RC4:@STRENGTH
* successfully set certificate verify locations:
*   CAfile: /etc/pki/tls/certs/ca-bundle.crt
  CApath: none
* TLSv1.2 (OUT), TLS header, Certificate Status (22):
* TLSv1.2 (OUT), TLS handshake, Client hello (1):
* TLSv1.2 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS change cipher, Client hello (1):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS change cipher, Client hello (1):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-RSA-AES256-GCM-SHA384
* ALPN, server accepted to use http/1.1
* Server certificate:
*  subject: CN=ecsc18.hack.cert.pl
*  start date: Dec  3 14:39:33 2018 GMT
*  expire date: Mar  3 14:39:33 2019 GMT
*  subjectAltName: host "web-http.ecsc18.hack.cert.pl" matched cert's "*.ecsc18.hack.cert.pl"
*  issuer: C=US; O=Let's Encrypt; CN=Let's Encrypt Authority X3
*  SSL certificate verify ok.
> GET / HTTP/1.1
> Host: web-http.ecsc18.hack.cert.pl
> User-Agent: curl/7.54.1
> Accept: */*
> 
< HTTP/1.1 200 OK
< Server: nginx
< Date: Wed, 02 Jan 2019 11:49:46 GMT
< Content-Type: text/html; charset=UTF-8
< Content-Length: 18
< Connection: keep-alive
< X-Powered-By: PHP/7.0.30
< X-Secret0: tOAsS732fOkV63ai2PC+KNaSzL4h3Vr/kzULhs8b
< X-Secret1: +18Y7DBcuPIciR8/glMkDyxLQgxozrgXo/elT3v6
< X-Secret2: mzzlWyQ+5H9U2CBUm5CvwGOI6mFnWhdJlaomqJ4c
< X-Secret3: BoJnq6HnaWuB2bahxasSIfz3bsIQb/jumNO16ikS
< X-Secret4: m/dxwDZ/ocfi2qOWDbJiDB9UFOtN77opkdfWAA2D
< X-Secret5: mWabKwoibrZDNk2dblOCcLLqhIQq9mWM2aMmv21u
< X-Secret6: nGdomv9Izrss65Yo7GsYRmUzr8ca5Z89Atj21AZF
< X-Secret7: 7r4r5Nszkzxngn3QBio4goS8TxHnCgilVzfEQ9D3
< X-Secret8: 9+MQr/nmubOKRAlj4E8ebZsMlIxZTMOoVbqcxiNR
< X-Secret9: 7BQF3aCkEOQM/V7m8JdUTyUp4yPF9bCYbsn6umVN
< X-Secret10: cNPnPzCnHZ6cP96f5OL5bP/nERe7P2P3w9wXh8P8
< X-Secret11: nSNJxzbsD+8ZLeZ+yBqMla6xGff5c3z6wM0T/0ZQ
< X-Secret12: /B1UuYZCCchmOuhvxRHXLtqU+3VQapYszvTYGvCl
< X-Secret13: g1aSl3lqvZWAR78Nt+X9ah/xG+UStK7nWCt5JGWH
< X-Secret14: 3W5Mx5MfyJAkDrwexy2oYE5uBsXnSO3pFIn6S8dj
< X-Secret15: vqjS7EkDKFNqjd4DosmNYRJYWs7xGhL0R1z7eqs7
< X-Secret16: CU4UGcCArrLTlJfyh69/tvHAiiTdJNx05mXJLX2T
< X-Secret17: v/NiJrs+BVp+qt1/zfTFjlk/yh4moO2yjjF3iMr/
< X-Secret18: hvdfuv2NK1paXcr9LaS1pfqshjC/3WnjGc7nXUbm
< X-Secret19: 3h0AFYVtdYP74VTMPsniQV7H6Cd+Y9madV/9CouR
< X-Secret20: 0p+M/c1t8Jpa5ONsoEnswvVGeZOMfKWUV5GfW4cB
< X-Secret21: 9ZwipfUm5ZCUgp/haTywityMVCEohjCpFdmdxNrj
< X-Secret22: 9Xuk+WcI6MG2RspdnI1zqoaClH9jWoS3Dnbu0GeQ
< X-Secret23: s6lm51OSpVFtEG9UJxAOl3X4QFAnshRHX/NB6oqn
< X-Secret24: +HrwKhc6vUiRo7rhPg5OuNZKic1YdWjedkLzsjH7
< X-Secret25: 2WPE+9K/bWzFwz/7zR9cBH8akGOZq/aBki9QJEIy
< X-Secret26: VfC7g3Q4LxOwartk8lHJoBshBFmdQVbK5Xkb9zTl
< X-Secret27: kKgFzZPpUSJ2ker0iIe6ZtGS8zptLi0g6i20tLHL
< X-Secret28: R5Tp/5MFbyP22G2+6FX1AQYUnrTtZcSbaMMrJ6nZ
< X-Secret29: 7m92iLAhVN4rSdm5lVEE5MQWamtg8gh2wWFeupjT
< X-Secret30: 5dmEM37K7tgzIMMjmj99IKeR4fyJYyhTOAB3aBII
< X-Secret31: jS7y+q6W/7MVLoScmlNq0J4yM3yOFVzc9n8jkb4K
< X-Secret32: TAuVsh/fDgwP49KT5lgzSCYp1FbO3D2Qbz0Mx2yx
< X-Secret33: /x0yPXn0l/HsOi9k0qxxTJaG9x0/hP4W4vUDrvL6
< X-Secret34: XCQpYNcdxNQkvhcZceH0iVGJk1FuvKtJc7DRB9XQ
< X-Secret35: MP3TtGYhhmVpzK5Y4pXZQQZQYJSWwK4Xr/tWPoN+
< X-Secret36: 5Uo/c8S/3ffu8CxXRHoM0pvdJx5x0LdCMl/pueh0
< X-Secret37: ij0VSwX0b22vAv/e74AsNm2nY1r2HwD612INYQqd
< X-Secret38: SsiWiRtedWBE2BVZzkGmXZ3JFF5gn6V5XPyWQbRo
< X-Secret39: 1dhhfGAMW/w3A7NEMf88brbEIAfnFK69NAM3zc1a
< X-Secret40: cvwyt9mwbkP0jJMYv+QhFgPhxGUzStufhwI+0dCf
< X-Secret41: F2gmyUOoyB7FHAgOOy6uB1k4ylslhV0jRZwCLGo5
< X-Secret42: 1TrvL3oEXIJ4isyx7tMbghWX8bb0k1Dd6h3k3b4x
< X-Secret43: 7yrDhcK/zCqeort8fftiSYnyQqv4fjI0xYCGlJK5
< X-Secret44: 6XiIR3GHtbd/3ggsCZscu8mDfXIfnJBS8tkABJDN
< X-Secret45: FcmEDD3n3i62dovBPd89/b++i5xGuZl6pXB2JGj2
< X-Secret46: 5r4Z7RjZyXcXqAh8MnPIPlInMcXsiivl9XVC+UXL
< X-Secret47: DFKAvH9hnqzEnnAWCGBQKH8D8DOu7rRXDi48D+zH
< X-Secret48: Wm0J0RmYyt9Aeuca1houXSqURN6+iLR83gxEv5gL
< X-Secret49: TRktGWZWUbV7hbZ4DKOvkQfnJkY/9HDfvQTZ7lLf
< X-Secret50: EAf/Kd5ZJi2sREtdW2Fk1iJHQKa+GPzg+SrYHx8L
< X-Secret51: iP3DATn9w1bOyh5m5OU4BLNSUKp/JIoZm2FxfsZh
< X-Secret52: Jt2j8wO5zyV94Dg48Cia64lMXlldWadHJgPOLWDW
< X-Secret53: ULPPu/jRKbKLXQ5SCGfB/ZAcJzkeXjH7hA2famrq
< X-Secret54: 2kSFZanWtmgG2M7vLqgrxbE1L9vvh4DYOkQq74sM
< X-Secret55: VljqZ0tKCa8DGV5trc7xVmdxDU18xiF7wLExRHNI
< X-Secret56: njWJmhLmVYSj3Lazu/XWgDcKqUzWB7nm6oXyQYsw
< X-Secret57: s+ib+RHq6AELbweCCb6xgpCMIqK44/qxEkgu5bcO
< X-Secret58: 3SuYS98da2OHjtNIm38cXVxOS7uHkDHwhwhPxS3y
< X-Secret59: AK/gN0Nss25VhUpsDTFfKokheabxoiFNdCHbO/w6
< X-Secret60: 7VeQnZ03umm10ZK6tgwvREAwNGIcUsHr0lt8N/fF
< X-Secret61: yNS+HKRV724Hh5GCPq88u8nQ6QJ7CTyz3JfLadhK
< X-Secret62: TAARRR7pko40q4x+Nkpw+7RHVDk1KAfqEbUwihra
< X-Secret63: SguguJai8ORFAMBk2OkzrOJGbIlUxLtlVm0qKOSA
< X-Secret64: 8MSiSrRVfQZ+B2CAbZlRXS54u06dccuKErFls6xA
< X-Secret65: EcXAM6U/i6T6LyITnUG8pJ8kS64RRrYfhTBI4nSz
< X-Secret66: HgvGiXBPhQSn7KoZaWxFtgJk0NyGucl0OAWGN4Lp
< X-Secret67: DeAMrvo6fvDSTBvt39PO+2TgM/iXxUCiDKpw9Vul
< X-Secret68: EGeqc2oLvZesSSSNxHeRg2DdsMd6gz+ZGen5GxgL
< X-Secret69: HPz4t8+nYkGVtnTTPNEpDecRTB66jZKPKQvpDB+q
< X-Secret70: mbuBkX6Odrb6BfuISmBxQ9s4paDTX7Qcph2DgB69
< X-Secret71: Y+sJnlYBvzbRQ1+O1j7tJozXPLAYR5m1LIishBrL
< X-Secret72: Z4IckVVSdvrCus5Te82syoRZEW1IkpkEDWcSuGT6
< X-Secret73: iD0HzP/VmGZZY4elpmyDAIHwQzSRMWF0tnhBxQA4
< X-Secret74: 75pWeGpK38OJSNCCCA6JwuoJX7dxxqp1lFY0+Oor
< X-Secret75: dNE968xUToCky2G4S6L3NtQSFeFx64iAssTaZefo
< X-Secret76: FcTMaePBf+XOhctBoz6Nb8ia1EiBujVqX7uqeWZS
< X-Secret77: 1iK+UujuoPYq8KXZ+LHZKzuBvdgD2fWw4//Mjc3H
< X-Secret78: WJ7wVPffjR8Z5GlknnynaXqFaLYe2NKARjYfk73E
< X-Secret79: ypMR0OW5OPsjB+lFCUJYOvJN6BAdFfErRIgo+qzd
< X-Secret80: il9UH/v67KMl/E1PdFKkMsclPtue+Me+Giw4rAYR
< X-Secret81: sQgyYmJvvwrvXZI61qxkM4W8q6Dc8oaTAQQNuiyM
< X-Secret82: uSuoUgCwXoBnCw6PoeJoJ+XpcpKprKJLWmBc/kIt
< X-Secret83: 7OgABVX63gg08w9ms8vSJlTEZE8X/2EIyAQI7ADs
< X-Secret84: vUUBiR4SLa74TTHHEnAXiGJOe3fSFGK2q+AoVfZn
< X-Secret85: fCYZd9Hjf5QGkF5CJu2GsR0OqmhhBX71ZQhEkKy/
< X-Secret86: MwiJQAnDXTGMK6q/XcCs2Ts+lLAl14413EXaRRal
< X-Secret87: GJn3FdAsoPQ2bown3fMAszIbC+pbKwgogJLPjE7q
< X-Secret88: WiDD0ht9rIvuEk4q12DuB1qV7iqkuaaEIlmXXIrz
< X-Secret89: Fxv8hDarjKI1ZQeszQplmdMXpqak0vo8z7ZgkdDJ
< X-Secret90: tGy3aQiI5Syp1eTM3EIypqZJvGI4uWRqk56Gd4QT
< X-Secret91: Tv/UBFP2SflnVzan6kb31vgZRaapedKsQqjHo4VL
< X-Secret92: SQzN9chqEK2sxcTBFN3qxecfw2xto1+DqWA7obPY
< X-Secret93: qxRpmZx8zPNZ1zeAaHQPrDlBuXmeGWkMf8pECcYA
< X-Secret94: an3IiIwedvT9O67NgAKkYG4GhYxhUWD1a6xR6Ol9
< X-Secret95: MNR4fI1go/vgyjHmYyBq0yKDaFtyTcl37XKB5C3J
< X-Secret96: 2n2HFFHYjW7yinYwrbCjdmsdK0F7+J809cuh+1dK
< X-Secret97: bhTedi1QTlNQYGiyLn8svp3QT7/16fBi2W7b5IA4
< X-Secret98: TUWZTBm+YExw07ty5BUGNZ8ZCs3ObtVYZ+CQuY4m
< X-Secret99: fSzzturn+TF24VvVxbEoVJfe9s2PdmWAdRyIXvjk
< X-Secret100: a7885H13KHGULys9HkZQxPIRNnwNXWm7hToJODrL
< X-Secret101: MRhtpQEq7r8PR4om3SLI2LuygXu9KOHaG52hW8+T
< X-Secret102: PVfQfnop1VuNh2989ilgc+TWXjBTcCaqumofUgAO
< X-Secret103: jXfHwr+wvWP4wi493ziD+Xm6Yr/rL51wdmxSgnkl
< X-Secret104: 3XiSd1i+0Yf8yquTYTuj5GZfVesdWQ9PFyeSvw4P
< X-Secret105: RZxuAuTf4VZ2+sDcS+KFmSMmrH84oeFfVf+w3PQi
< X-Secret106: B2notZ1IwXUHtNoxiZiSugiNWBicoP2BSUuS7LoU
< X-Secret107: +PV06csoRoITE9jRMqxTfrwDFiJ1wR8wKoZf5ItQ
< X-Secret108: psrOGyinwsnd+OBDESEJEA6zmdSbZnBlbusHS6iD
< X-Secret109: MVjZNhwaX88+7RqrwYY/D9xgMbhc6fhc50wUsodo
< X-Secret110: +qxWmibkWN5St/JFxPH01jE1USYevCnc9T7slz78
< X-Secret111: wWZHPqqKx/M6n3TQkWAOOZFHSAxsjexJQLO7nmzC
< X-Secret112: WpxIxJX4xoWh9naNL6Mkz2M9cz6OL1JqqHFNRWUh
< X-Secret113: zxdppKYC4whhbVfhuCj6vjPaYUxesGgVa01i/par
< X-Secret114: XXc3/aIPbKUpTsa7jwGCycOoaBoAB95kaIMYiY/D
< X-Secret115: sNv4EjJIAtGFT5miMjuHvtRPm4H915QlNI7Xo+T0
< X-Secret116: N23DUHlI0BMuIwtDvCMpYzemXkx0m6VTYpPVheci
< X-Secret117: DFO6WwCWH0a0g1GRUqySb150BNbNkFL0xRD2MEB3
< X-Secret118: QuF6iOKpfa4r2rFeDXgs4W4hUmaJ/7e4vvvgG+I+
< X-Secret119: e5qKrngROzSvsIvTaSzXrqiH7dzwFu/LtTMW3DVt
< X-Secret120: /ueiSwLtiXnYRrdq39AKoAT/snwxju1q3BXdCryy
< X-Secret121: hhEJoK5MIm0pk8Hfb0w6fBWCv7LZ1zekxhzhYF5A
< X-Secret122: inBV6KALa/pbhdD2uARcQiBCj7OtWGhU7DCTIptH
< X-Secret123: jNhHwuTpkPK7n1MJ1Rci51FjAJex4gAzQOaFH5MO
< X-Secret124: LeGImat62ys3Ju9fXWk2xF41Nxv+P70qnnqi5zBS
< X-Secret125: pTx26S/fJ7LlaNj5hPosHIHzaETKQ54tCFPJCiEI
< X-Secret126: Tju9483bLLL4BvVZH94U+vrvcRtyzyibEtV9pWHI
< X-Secret127: FPr3l5lN18M9D1+5fnwZgWlCdWQlCpm8c0GYi2po
< X-Secret128: o+o+o2pt5wALcVMaTSFA2XYgiq8MQNPa8m3CSuuy
< X-Secret129: ysf3cFrRVQTqVwt4tVXG4OInX8uyv3OqFDUA3ieI
< X-Secret130: 8Nk2Gq2dpTD1URrRAeSaSnrDCZG9S0s3/5q+N29Q
< X-Secret131: xTh+HG3TcjSKlzgwJSxfakhLXIjIbxp/E9jOvj+W
< X-Secret132: kUELiTULfXoe6YtBzux0UHj6UeNUJbBcbXdM+XlY
< X-Secret133: TX6fDNGd6F5pGd/9r0z5FYYaOfbd5D5ek2C9Qfct
< X-Secret134: StMXE/X84zbhFanufDPCY4DDAwGmhHEvcoI+UDfa
< X-Secret135: dFayfxEERonrFuTNXVHvIi+jL2v57jDdFrkjxEEN
< X-Secret136: nhQF7DM28GfpynuadVv1PhdqKUS+bV5b6WpUUhDr
< X-Secret137: 3yFdYHu2Rut9DHSB7bBFTzGE8sbrdFrKCjvWCVjx
< X-Secret138: Q15hJ46BmpehlqqY29DdJXP4pTSaDn4dDUMEcpTp
< X-Secret139: kU9E4m/DJiyUFkAxfm6OZllRnSVLOAi7W0LefM/2
< X-Secret140: Ve2bq+EXRueMVazKE/KgozHw+P37+Xe/0RjHOam/
< X-Secret141: 9h+vDP9vkyX9kN0vZCOp9fe4NPICPV9z8ejOUXNP
< X-Secret142: ghCqeUqAeh+Cm7HT3ZL1DiXXCb0Z9BBWsxFm9t3A
< X-Secret143: KOpnoG+S6BKG7BrO1u1ofldgLwdO8CcjTvQYfd6b
< X-Secret144: 5oHUXBbCJ9OgEsM2tmwQWpAHcb9ZQD6fsWqI8OIv
< X-Secret145: iMXY7VV9VyU5iWtmVHrySLDuB4Y1O6qyAkWlcHz7
< X-Secret146: eX+URRMfJN3rmPXnraaYS69EU4sZk6XN8gexmZpk
< X-Secret147: FA8V27XdmCURIbBAr17BL1pomVznjo8VF6cKkGqi
< X-Secret148: 2Pp94MbURvhOFSgIuQVVLx/zs5sRFA6/ZGLoSPRo
< X-Secret149: 9+dERxZ5o9E34fOh0/HRD8GRmKDekNa5+kp0zSFw
< X-Secret150: XwIo2p+L7HR57bDksVwNMAP+h3bCDoW5NdGb96mB
< X-Secret151: AtoQVL4CPSLO2ZkvAjqmWOnVCNEUcAkMvwmpsKVV
< X-Secret152: F/8R85CVEXORtz+HEvHKVCW/8czD+UDXJx/Ekd3i
< X-Secret153: 1sRnRygXk54Dn9666IRI8RKngQ6lKfOZOeTHd3Hg
< X-Secret154: iLf/WT1dtum30J/puz1ir7x2Md50ORCiZBGreGmI
< X-Secret155: gIlLw6Mih3LcY+/4F9vECZC+vYVJcRC8V3jhh1AH
< X-Secret156: 6GFH1qu4XdHfh+PpR7n/pPC+YzByx2KrEZeik2WQ
< X-Secret157: cc5Ytx25dYhq1uC7qyWBnFZ84LKPCeklF9B+nzDs
< X-Secret158: w0F0MFfUzEIkqqpr1e6pve63bHrlQaZuyvGfJckt
< X-Secret159: NUWXhU9H56s4p45m+GEq5HHYbFMINlOc6/IzMxbR
< X-Secret160: b9rg8zjN3kyT+OO7UWN/EgkaTKGbD5v6dqN0pRqP
< X-Secret161: wf4nqQ4JT+3yFWOhfWtxYr0v2ZaVTXDKzRfFvyuX
< X-Secret162: kkDlYU2XwPNn+sjSwsLkPxHzQD79OBSbxhSVqlNc
< X-Secret163: UG6ZpGRYW9GR7ahbsQS0eTYp9YOVfeOjGn2ndNFt
< X-Secret164: sbiVQKMpjNZ//a5dRoXnN1vY4ssTbiBGzsx/lQA4
< X-Secret165: Ps2QCVAyK6C/VoatmXSZ6zUWWzxzwyoRVajy+GWt
< X-Secret166: NftL5NkjsyVTtdm5ctUdFQ+SHSAKxogXzZfbvmjJ
< X-Secret167: 5zx5RE1z3fwuJxNKGaP/T8dFUihsLLcZtwmwD9Fg
< X-Secret168: EBQR1WEafpkEfJhWePJXTIWX+PG7CXmHNTUFweoP
< X-Secret169: xsiD+beuzDGhwXpcrmfHrOFtgclnyRquqNNfpC+3
< X-Secret170: oCnILkD0WH8FiF4Mag3kpCpWTE3fb8Ok+GEwGc/0
< X-Secret171: wmXvQJFhIhipk+f8GW9LPrQNcFVVra04Y+aoNYGk
< X-Secret172: QuJq6VWzSulVUCSR78A7TtmLzBfo3m02K8bxWrR5
< X-Secret173: 6z2XsEtTVNoPKOccGreWBxH+WX5UYxKdyLDcuHYO
< X-Secret174: NvLmUm51KhKis/4PK/82IiI78+v5VmEeCNd7fooI
< X-Secret175: Y3vcOcWou/2dOyhfKUA6quFyzA3yJft5h+OwghD9
< X-Secret176: sQMlG755N6XhOhRsRJFy5Zlz/LMgWTnD8TzBRdNO
< X-Secret177: KuOxLviQasXuO0ICoovZVWEdhgxeoUo9SiIe5w+v
< X-Secret178: jWbf7sugVnrXnKIYU4JzljIhsht/vJHL/JswS2oy
< X-Secret179: x0RljdX5fn1febSMzmGa7sjvlM5tK6JmrLHVm9Eu
< X-Secret180: HYhH8cfFRf77yTez9OMzOQhk6wrfgXlJZz9zsibo
< X-Secret181: Bq4DVCEL4JYgTnSjLakE7NSo5+qAIrZmlf5WrpW2
< X-Secret182: jdq1oIxOHVHWQC1HGdkeYKcDapKs4ObuPwwXtJzU
< X-Secret183: V/Z+WgGytA+TGzZLVyreY6mEYnETnyQtLWTjLtuz
< X-Secret184: ZPKenOEOgLkQnkJXY91K2W4/SpPEVvXRRVzWbaiz
< X-Secret185: bUV3nn4zgxBWDOfUQxFap+Xb7TPUAnIhcmgH7IwS
< X-Secret186: yMzJ0VK8GSPK11PHiowLKhHo4SLfJqHWRaYvjNnB
< X-Secret187: PQJ04ajM2CQ/ZgwZiHlC85Qrj56LTy4AnM90liY5
< X-Secret188: tQgQFIRTkv09gfDu/EMswRpqne77yF1Y8nOsBoOn
< X-Secret189: dlwu4xS2/s17L5dxF/QE2nnTLxl5MraALKZ4h0hK
< X-Secret190: qgRoqGczne4i1ownu9oln7b3WUq2GcPGuJn/0msE
< X-Secret191: k4eV5XoznQkHo8Vdg5EEx8MakhYBYIIlhmHQBdRm
< X-Secret192: 8vYDeC20P31+i9+eVhkvpW8IfMj4Wwm+KULO2bO5
< X-Secret193: Q0wT6DI4GPHxRKAftgdFnQSno7wEZYLRbqWTxEJz
< X-Secret194: vSPsXXefk9JpSSRnTTVCDfONi61HIgaviisji632
< X-Secret195: jJnVmTUeoN2O3M4A6RbiXVHbC7MbmafWsMcqtXEt
< X-Secret196: ePT+autUWh17tHkuxcYn4unOk2VKjK3nZa6f9Gal
< X-Secret197: ShotXm0KZIcbkxNvD0umXO24LKWxmzfdpfsXC98p
< X-Secret198: USDCAy7OhAlgSU5qGQCWlOIpjET3d2HaR0CYLZe9
< X-Secret199: Lodojh6M37iNUOnaouyzjJFXJA07L/jXCvH7SGdJ
< X-Secret200: D0ia3wZkuHCT6zHxl2Q5ksSl/w0aC6ZXu7om0Idd
< X-Secret201: tIw5YTq7RlKi81i6xubJy5kkdCYi4b/SORz67Py5
< X-Secret202: URvB3OIx2r3aIDQGnRcZuEJoDg8UJHu5yVgT3jOp
< X-Secret203: 1S5TlWZt6wBQ8n22xIoxfkLqx/eBrc5ORf+aR8bC
< X-Secret204: ewvT7zyTXOzcHHUe0M9XM49EPyWWbCipxH0bmNmi
< X-Secret205: DXnBSViw8N5Ev0FYmO2NzGuv2lvTQT4VlZ7MMe2V
< X-Secret206: BHnKPxgDIhjToW/C2M/7XizkWr19YStMQrCYes3w
< X-Secret207: PJAFy07iKqfczE195kb992xT1m2bRnJbSz0mzgTN
< X-Secret208: qDYLd4QsOAwiH0M2TidSf9ILnl20vnAZ+CY0ezN0
< X-Secret209: g5mn/GagYJWnr3OpXQ1dzXKP4UtDRWg2iEblLoY3
< X-Secret210: NtdtsTSsipzuQxUqmoFkMICBfnIXpfPZfYplyBzk
< X-Secret211: CNZMgso1RuR9/SLfS9t0+TLaXHqyX8x8alx1u25i
< X-Secret212: A5/M4Q1A8J/tL9p7XOj49pucvTSHSoLRo7sXgun6
< X-Secret213: nA8X5xXjurx9C5AViNUpkq4Ac+Ym6qW7uBaMqI+c
< X-Secret214: iaLne7JQqzeGiT4m7K1+SzY+ctgzmUWLCu/l5elT
< X-Secret215: M7cGwJkQsxcA24KojhCIlgmC8vf4y/Sla2vDXCHQ
< X-Secret216: 9RwunVQml1XrN80Hiv91S/yMr5YpAkyV+JtzzP7g
< X-Secret217: 45KDd1tMArknfEJ5TbhW/c7OFcDIRQdIfBra9QZd
< X-Secret218: fQ42KK73O5EfrYy5q2KAqJBEdWzaTOaFepslXDaI
< X-Secret219: /pE5ExILOf4Sy8JeKzKz3QpiJE0gw9r9MDmNuUm4
< X-Secret220: AJLyGrwbfaeG3Rir+3xM4X+BpG+f2v6ZdEz+LxS8
< X-Secret221: W1PLjKmiPawWREtRxffIwhPPkLwE3ibA8M1g3Z+I
< X-Secret222: 7NyyLneulInDv74SuxVVMRtHVYPygYkWExaTEFHZ
< X-Secret223: 0y890gKcW+Y9vPM11PpF3n0zXZeIk4LrKMr/+Srx
< X-Secret224: a59MrI8eKdqiAjFrqP7bdOLnlYq7fmu01LR0i4He
< X-Secret225: wU2GqcoX80pKzmnRZflM31qHAImglBB3qgw8I0ji
< X-Secret226: U1yPqg6d4BS6yMrVyET/2iMg6qnt/t/5y50g7Anm
< X-Secret227: l5RBdB5QRzd97cgFfeKy4Y50lpC8hIH2PgzpDUXl
< X-Secret228: Q+ithO49eAkhdbGPQIFHi4eJjoTRl+K62sSIK8gR
< X-Secret229: MkVvfgi2JLc9pWsRAZVBKJdiDaHzgTvs2Tev6oIC
< X-Secret230: e15LrwMwGsyiQ22j//hGssV6kPsbrCniQlnLsyHy
< X-Secret231: 3voCvgtgCQmXq5zS7SLLCorAHMOo1tiePJFahG/3
< X-Secret232: PIEbPmejivgAlatCdGvmzi4bZbpVQ17R5Xq40pha
< X-Secret233: V4+IWpU/0aYXEntBP1nat6qNnF49d1DduVC1Ot9k
< X-Secret234: szfDDM4QB2yk8pU9+ZpNiJwI9aEplshijExbNuX1
< X-Secret235: UtNqNON+wsA2MCGSx+IwhyVeeKfWYFyCn+IlUo0d
< X-Secret236: 0uYUsHmYt3ZHiLAT4q6Lx2Jlrp5CCxjGT1sPZk4u
< X-Secret237: AMqL8D2ABqBstnayJWXyUQFfjwlKLcGJO/+/NttG
< X-Secret238: rySAHTc86ZUDN3xFwPFCf3IrSiOswxqC7CgIvFeW
< X-Secret239: Su31uJt9oCjQtrAdByimymlVFfIf94tqpND+DGXF
< X-Secret240: 4gsKL6Tie5VjvEfglg237AjjQEwWdbk3oqNf9FwG
< X-Secret241: tG6/sSuZcaG3qNH+xXBetIzkezX6jMj5jiVOIQCY
< X-Secret242: o4UOeEYR9wZotf3aaSDtefLGrzVrTd2qiSO4oPWE
< X-Secret243: nos8wZRgiqxpRb/W27XoXWfg5Kptdtb2tpPZJjfv
< X-Secret244: WNFUou7OPS/rQFaULCgEMhaaqPQZ3ZCa5ioDEGTg
< X-Secret245: TwQah8G1+8l+JG3bs1MHA2DELiARjUi9adtR8Mnt
< X-Secret246: V8yvS7WbmbLpCNuAQhm5CtmmW6HzjcJHxhj+CyTz
< X-Secret247: oGgB8pJp+jvgqR3TvLZLjtB7cNrcYnHZBNfPjCW5
< X-Secret248: x3KqqmkYg7xzdQlzfOVnOQPwj9Ov/wBdNaFTssLL
< X-Secret249: tpqmY7XsTtWaF/6nXN3M+SGJvAqUB1af9Ha/7NnX
< X-Secret250: fYe/02cyiKAH0/pawjbwWoQXTxDdWFwJFvwalSsm
< X-Secret251: HJkTXyF/26WnyaSv4o4BeQwtUKFMynJpHwQbAOTB
< X-Secret252: h5cfyizixfJIWouNfPALWtyge9gjLtGIEHxBdeEm
< X-Secret253: C7hJqhEVuwizTHM9koCG7b6SstWNFOEloHtkf2qJ
< X-Secret254: PriQ52IYGrFxWJRg5cVlAh605trB9/NMwAwP9qyp
< X-Secret255: ZjVpO/K/saI5bJ63/wlRidoxPmM+9SpzXvgwyhYF
< X-Secret256: 0obI+fXD6Y5b9NilsmRTIZPinhp4K05eUaLIvIlY
< X-Secret257: jYA8e/dOnxpImHnHJmftS8+SYLgx7uDl1Nq5x0jk
< X-Secret258: c4nX82s5BOKYyQFUohkrIGXksKOKtiufCzfJykGa
< X-Secret259: gnTqsxgcCOt5jp38KCmGW43Pk8ESU0wh0O4pp7Hm
< X-Secret260: xAZC/1jmOM8r+Emoi1zQFGZxImODq9go09RMKguJ
< X-Secret261: UOnEIDEowCmAFxRMan4A1b8mGCI9DI1KU11PKvoh
< X-Secret262: 5S6sFlB5PeohgVnCHwFDn/7FQcGoN37DJNMPQREF
< X-Secret263: 7J4KuyzvXyjd92tb1fQTOdW7qM2/3RiMvULAt5K0
< X-Secret264: miy+/72MDid/ENUx8pUyPQCizwLJ43+nNVTSVc7+
< X-Secret265: 5LgHRoWrZMq/DojgDPdf+10MZ+6nOkQDtzXiwDB4
< X-Secret266: LhUc0YaY+qSgTpHrenRnB79tfa6rbZPScLPhEUKF
< X-Secret267: JrD5RV+o+eZq3aohwOWCkimpkMTOJmaKwvELmFWb
< X-Secret268: EORgg/7WJK7PYYowVc5u5HHUAdQJKJ1xHDT9OWmR
< X-Secret269: eQu4wVRcwUJwyf+rn1CV+2sm0WmxysTFSku/0AM2
< X-Secret270: 3e1qaDAv5sQLUaUdJkbfkE7GCdOhWv0Oezb2TUEi
< X-Secret271: hFjtp2WsvxmCuo8HrAKe14T5viiQAU6tFF1EefIR
< X-Secret272: ZWNzY3t0b29fbWFueV9lbmNvZGVkX2hlYWRlcnN9
< X-Secret273: W/UxcHEEqHgf9tlDl4wOXWrVHU7tp5CMCTXzjNRy
< X-Secret274: jDQ6Lot1kdG9lSbvCLsZPh40SuoSTTCKevEsJJXF
< X-Secret275: i8LB4S6gL1zGRd0w4yKufUfMvV6Tzh55tweUfHfR
< X-Secret276: HgFCHm7MJA26lPPXLImH6ZObVHoKoR6NcXxHRAFl
< X-Secret277: oybvzyNa8Zj8Kf7h373SMj0L1V9vHOugns877kK7
< X-Secret278: atmGO/FEKir2lqLn0xErG2AnbADRnzt9prTqmJ6s
< X-Secret279: FvvDKRHUGoTF9ReA4XjyRwgqxfszNocvnYmXFAIk
< X-Secret280: ZxU2pFlvaoFpBPslndss/TNbMBtVEOY/64Hq/6LJ
< X-Secret281: r8gwX8NpBJr3R7XHyBfVMzG1Hf4ygGI2w/Jz6J+R
< X-Secret282: 7sGTQ5Ch9OUjNQxUu81+ind4xV4lWifj7pCwkuyp
< X-Secret283: XPBLITPyc7lrQKQ6RNQEO3tsj25hYIq8Zls7JqJg
< X-Secret284: 6tjPNiIgmGYUeqYlB3mF70LcsqdQCk8BWauksFfc
< X-Secret285: OfnGgqMI/Rh3Z6bBf7D/ROOwBzsUzmy1gDB1wN5y
< X-Secret286: 5r1e1iOsEpjlfU9/YEBOnOWBNHjF3FvtCRvJZykO
< X-Secret287: D6qDTDRvH7tX4o5UkIg67beIjECj394tKVNGoY5s
< X-Secret288: PZAvvdlfSRrGdBm31L0DijJWOkBRqDwdc3BjWlpa
< X-Secret289: 64Ut8xAOZ0pSNOWvea40om8sCdxEknMv4p06Zlkg
< X-Secret290: wf7BJilE2mALSdP6KNJ8usJvbPsD1fKm3ff89qqz
< X-Secret291: iJeq3z6m2Az8Wn9Gbu8Ua82Ue9QYe0ORXiX03Gmc
< X-Secret292: 9Rfgb4vqNWW4ZKz9luyxaA0V6/cuR6gffhVEl0ES
< X-Secret293: EihfDcm9eceu4FG1sNJJnGxRS2n+4snXVyxUrD6q
< X-Secret294: BJPMYGrvvhVd8R2zEU1e4yimwqG2f5rjaO/ej/ck
< X-Secret295: 1Js6IbZ73g3PW8Z4zI3mv7KcO0BPwQZWBewMCGew
< X-Secret296: 1zx0Mf7mS+xbol0dDyA0FBWa/94b1w4tZKHuRZUa
< X-Secret297: KFQ+BEonjJ24zWQ6WzNqHq5pukgMp+mRwtBrSkjF
< X-Secret298: YdZyaqZO9XNzZzTUMsZkiqbKVoiYjylt0aORuCsX
< X-Secret299: sBit1hT9vmndFbgTgRzK8uGzdXzICKqnLbw1YjEi
< 
* Connection #0 to host web-http.ecsc18.hack.cert.pl left intact
```

Ich treść wygląda na base64, więc próbujemy!
```
$ grep 'X-Secret[0-9]' http.md|cut -d: -f2|tr -d '[:space:]'|base64 -d|strings /dev/stdin|grep ecsc
ecsc{too_many_encoded_headers}[
```

Taka jest też flaga (bez końcowego `[`).


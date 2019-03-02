print(r"""
Input:
    /-------+-------+-------+----- A
    |       |       |       |
    1       2       3       |
    |       |       |       7
    6       5       4       |
    |       |       |       |
    \-------+-------+-------+----- B

Give current ↓ and voltage ±.

""")

class Obj:
    _o = _v = _a = typ = None
    def __init__(self, idx):
        self.idx = idx
    @property
    def o(self):
        if self._o is not None:
            return self._o
        if self._v is not None and self._a is not None:
            self._o = self._v/self._a
    @property
    def v(self):
        if self._v is not None:
            return self._v
        if self._o is not None and self._a is not None:
            self._v = self._o*self._a
        return self._v
    @property
    def a(self):
        if self._a is not None:
            return self._a
        if self._v is not None and self._o is not None:
            self._a = self._v/self._o
        return self._a

    @o.setter
    def o(self, x):
        self._o = x
    @v.setter
    def v(self, x):
        self._v = x
    @a.setter
    def a(self, x):
        if self.typ == 'a':
            return
        if self.a != x:
            self._a = x
            if self.idx in range(7):
                objs[7-self.idx].a = x
        self._a = x
objs = [Obj(i) for i in range(8)]

for i in range(1,8):
    print("Gimme %d (e.g. 1v, 2a, 5o, defaults to o)"%i, end=" ")
    while True:
        num = input().replace('Ω', 'o').replace('_', '').strip()
        if num: break
    if not num[-1:].isalpha():
        num += 'o'
    unit = num[-1:].lower()
    num = int(num[:-1])
    print("got %d %s"%(num, unit))
    setattr(objs[i], unit, num)
    objs[i].typ = unit

mi = -1e9
ma = 1e9

if objs[7].v is not None:
    mi = ma = ce = objs[7].v

print()

while ma-mi > 1e-5:
    ce = (ma+mi)/2
    objs[7].v = ce
    if objs[7].typ != 'a':
        objs[7].a = None
    s = objs[7].a
    for i in range(1,4):
        t1 = objs[i].typ
        t2 = objs[7-i].typ
        if t1 == 'o' and t2 == 'o':
            su = ce/(objs[i].o+objs[7-i].o)
            objs[i].a = objs[7-i].a = su
            objs[i].v = objs[7-i].v = None
        if t1 == 'v' or t2 == 'a':
            objs[7-i].v = ce-objs[i].v
            if t2 != 'o':
                objs[7-i].o = None
            if t2 != 'a':
                objs[7-i].a = None
            if t1 != 'a':
                objs[i].a = objs[7-i].a
        if t1 == 'a' or t2 == 'v':
            objs[i].v = ce-objs[7-i].v
            if t1 != 'o':
                objs[i].o = None
            if t1 != 'a':
                objs[i].a = None
            if t2 != 'a':
                objs[7-i].a = objs[i].a
        try:
            s += objs[i].a
        except TypeError:
            print("Err", t1, t2)
            raise
    if s > 0:
        ma = ce
    else:
        mi = ce

print(int(round(ce)))


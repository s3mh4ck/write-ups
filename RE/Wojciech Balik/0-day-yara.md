# 0-day Yara (https://hack.cert.pl/challenge/0day-yara)

Treść zadania:

```

    One of researchers notified us about very dangerous 0-day malware. Unfortunately, we can't look at the sample, because analyst refused to provide one. After a short talk, he gave us an Yara rule, but again... only a compiled version of it.

    Could you recover that rule to plaintext form? We've tried to do it on our own, but have been unsuccessful (the condition part looks very unusual).

    Compiled Yara rules are version-dependent. That one was generated using Yara 3.7.1.

    Hint: Yara rule conditions syntax allows to build very verbose and complicated rules. To evaluate them quickly, they're compiled to Yara bytecode (interpreter can be found here).

    Format flagi: ecsc{litery_cyfry_i_znaki_specjalne}.

```

Z treści zadania wynika że będzie ono miało związek z yarą, czyli narzędziem do identyfikacji wirusów.
Pozwala ono pisać własne reguły opisujące malware, a następnie skompilować je do bajtkodu. W zadaniu
otrzymujemy właśnie tego typu bajtkod, i jak wynika z treści, został on wygenerowany yarą w wersji 3.7.1.
Po jej ściągnięciu i skompilowaniu, możemy wykonać nasz bajtkod:

```bash
echo asdf > input
./yara 0day.yarac input
```

Można by teraz próbować zrozumieć jak działa maszyna wirtualna która interpretuje bajtkod, ale
można to zrobić prościej. Kod(libyara/exec.c) który odpowiada za interpretacje i wykonianie bajtkodu wygląda
mniej więcej tak:

```c
...
  while(!stop)
  {
    opcode = *ip;
    ip++;
    switch(opcode)
    {
      case OP_NOP:
        break;

      case OP_HALT:
        assert(sp == 0); // When HALT is reached the stack should be empty.
        stop = TRUE;
        break;

      case OP_PUSH:
        r1.i = *(uint64_t*)(ip);
        ip += sizeof(uint64_t);
        push(r1);

        break;

      case OP_POP:
        pop(r1);
        break;

      case OP_CLEAR_M:
        r1.i = *(uint64_t*)(ip);
        ip += sizeof(uint64_t);
        mem[r1.i] = 0;
        break;

      case OP_ADD_M:
        r1.i = *(uint64_t*)(ip);
        ip += sizeof(uint64_t);
...
```

czyli jest to jeden wielki switch, możemy więc np. za pomocą jakiegoś regexa dodać printf pod każdym
case. W vscode zmieniłem `case (OP_[^:]+):` na `case $1:\nprintf("$1\\n");`, i po wykonaniu
bajtkodu dla wejścia `asdf` otrzymałem taki output:

```
OP_INIT_RULE
OP_PUSH
OP_PUSH
OP_PUSH
OP_OF
OP_JFALSE
OP_JTRUE
OP_POP
OP_HALT
```

Nastomiast dla wejścia `ecsc{asdf}` otrzymałem:

```
OP_INIT_RULE
OP_PUSH
OP_PUSH
OP_PUSH
OP_OF
OP_JFALSE
OP_PUSH
OP_PUSH
OP_OFFSET
OP_PUSH
OP_INT_ADD
OP_UINT8
OP_PUSH
OP_INT_EQ
OP_AND
OP_JTRUE
OP_POP
OP_HALT
```

Warto by było dla takich opkodów jak `OP_INT_EQ` albo `OP_PUSH` wypisać jakie przyjmują argumenty, ale
to już niestety trzeba zrobić ręcznie, np tak:

```c
case OP_INT_EQ:
    pop(r2);
    pop(r1);
    ensure_defined(r2);
    ensure_defined(r1);
    printf("OP_INT_EQ %lx %lx\n", r1.i, r2.i);
    r1.i = r1.i == r2.i;
    push(r1);
    break;
```

Jeśli wykonamy kod jeszcze razm zobaczymy że `OP_INT_EQ` nie zostało wypisane, prawdopodobnie przez
`ensure_defined`. Jeśli podamy nieco dłuższy input, np. `ecsc{1234567890qwertyui}`, to zobaczymy
tam linijkę z `OP_INT_EQ 6f 7d`. `6f` i `7d` w ascii to odpowiednio `o`o i `}`, więc nasz flaga powinna kończyć się tam gdzie obecnie jest literka `o`, czyli wiemy że flaga ma 18 znaków. Jak podamy na
wejściu `ecsc{1234567890qwertyui}` to dostaniemy trochę większy output, ale można w nim zauważyć że co
jakiś czas pojawia się linijka typu `OP_INT_EQ 4f4c 142a`. Jak wykonamy `./yara 0day.yarac input | grep OP_INT_EQ`, to powinniśmy otrzymać:

```
OP_INT_EQ 7d 7d
OP_INT_EQ b870 b560
OP_INT_EQ 103d 516
OP_INT_EQ 9ef3 a9e6
OP_INT_EQ 291b 191c
OP_INT_EQ 98da f782
OP_INT_EQ 1829 4e63
OP_INT_EQ 4bc4 24ae
OP_INT_EQ 3d7f 622f
OP_INT_EQ 4f4c 142a
```

(pomijamy pierwszą linijkę, jest już nieistotna)
Zmieniając pierwszą literkę naszego inputu, tzn `1` -> `2`, zmieni się jedynie ostatnia linijka outputu,
na `OP_INT_EQ 4f4c 1429`. Po kilku minutach prób, można stwierdzić, że liczby po lewej to poprawne
wartości, a te po prawej to "hash", wygenerowany przez nasz input, oraz że wszystkie literki wejścia są od siebie niezależne, i zależność między wejściem a wyjściem jest taka:
```
...
9  8
6  7
5  4
2  3
1  0
```

Można więc znaleźć flagę bruteforcem, np w ten sposób:

```python
import sys
import os
from string import printable

def get_output(input_):
    assert len(input_) == 18
    with open('input', 'w') as f:
        f.write('ecsc{' + input_ + '}')
    
    os.system('./yara 0day.yarac input | grep OP_INT_EQ > output')
    with open('output') as f:
        output = [i.split()[2].rjust(4, '0').decode('hex') for i in f.read().split('\n')[1:-1][::-1]]
        for i in range(0, len(output), 2):
            output[i] = output[i][::-1]
        output = ''.join(output)

    return output

correct = '4c4f3d7fc44b1829da98291bf39e103d70b8'.decode('hex')
flag = ''


input_ = bytearray(18*'A')

al = printable

for idx in range(18):
    for c in al:
        c = ord(c)
        input_[idx] = c
        output = get_output(str(input_))
        if output[idx] == correct[idx]:
            flag += chr(c)
            break
    print(idx)
print(flag)
```
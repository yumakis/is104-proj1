from math import *

def rp(x,p):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    E = int(x)
    D = x - E
    e = str(E)
    d = str(D)
    res = 0
    if p < len(e):
        i = 0
        while i < p:
            res += int(e[i])*10**(len(e)-1-i)
            i += 1
        if 5 <= int(e[i]):
            res += 10**(len(e)-i)
        return res
    elif len(e) <= p:
        if len(e) == 1:
            if e[0] == 0
        res = E
        i = len(e)
        if 5 <= int(d[2]):
            res += 1
        return res
    return 0

print(rp(152.06,3))


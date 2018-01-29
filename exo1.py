from math import *

def rp(x,p):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    E = int(x)
    D = float(x - E)
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
        res = E
        if E == 0:
            i = 2
            print(d)
            while int(d[i]) == 0:
                i += 1
            count = 0
            while count < p:
                res += int(d[i])*10**(-(i-1))
                i += 1
                count += 1
            if i < len(d):
                if 5 <= int(d[i]):
                    res += 10**(-(i-2))
        else:
            count = len(e)
            i = 2
            while count < p:
                res += int(d[i])*10**(-(i-1))
                i += 1
                count += 1
            if i < len(d):
                if 5 <= int(d[i]):
                    res += 10**(-(i-2))
        return res
    return 0

print(rp(0.00015252,1))


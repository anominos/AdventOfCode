pin = 33100000

sm = pin//10

def sieve(n):
    pf = [True]*(n//2)
    pf[0] = False
    for i,x in enumerate(pf):
        if x:
            s = i*2+1
            for z in range(i+s, len(pf), s):
                pf[z] = False
            if s > n**0.5:
                yield 2
                for j,y in enumerate(pf):
                    if y:
                        yield j*2+1
                break
p = list(sieve(sm))
from functools import lru_cache

@lru_cache(maxsize=None)
def getFactSum(a):
    c=0
    for x in range(1,int(a**0.5)+1):
        if a%x==0:
            c+=x+a//x
            if x==a//x:c-=x
    return c



for x in range(2,sm):
    if getFactSum(x) >= sm:
        print(x)
        break



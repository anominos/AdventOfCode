dat = []
with open("d10in.txt") as f:
    for x in f:
        dat.append(int(x.strip()))
cpy = dat[:]
d = [0,0,1]
cur = 0
while dat:
    d[min(dat)-cur-1]+=1
    cur = min(dat)
    dat.remove(min(dat))
print(d[0]*d[-1])
dat = cpy[:]
from functools import lru_cache
dat.sort()
@lru_cache(maxsize=None)
def rec(i):
    ##starting joltage, index of final adap left
    if dat[i] in [1,2,3]:
        c = 1
    else:
        c=0
    if i < 0:
        return 0
    
    for ind in range(1,4):
        if i >= ind and  dat[i]-dat[i-ind] <= 3:
            # print(i-ind, dat[i-ind], i, dat[i])
            c+=rec(i-ind)
    return c
print(rec(len(dat)-1))
# print(dat[:5])
# for i in range(0, 5):
#     print(rec(i), dat[i])

## 165801105555456

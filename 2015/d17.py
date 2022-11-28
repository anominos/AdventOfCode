dat = []
with open("d17in.txt") as f:
    for x in f:
        dat.append(int(x.strip()))
dat = [43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38]
from functools import lru_cache    
@lru_cache(maxsize=None)
def numWays(left, i):
    if left==0:
        return 1
    if left < 0:
        return 0
    if i==len(dat):
        return 0
    
    return numWays(left, i+1) + numWays(left-dat[i], i+1)

print(numWays(150, 0))

@lru_cache(maxsize=None)
def numWays2(left, i, l):
    if l == 0 and left==0:
        return 1
    if l==0 or left<=0 or i==len(dat):
        return 0
    
    return numWays2(left, i+1, l) + numWays2(left-dat[i], i+1, l-1)

for x in range(len(dat)):
    if (y:=numWays2(150, 0, x))!=0:
        print(y)
        break

dd = []
with open("d21in.txt") as f:
    for x in f:
        dd.append(int(x.strip()[-1])-1)
# dd[0]= 3
# dd[1] = 7
dat = dd[:]
score = [0,0]
dice = 0
cur = False
c=0
while max(score) < 1000:
    dat[cur] += (dice*3+6)
    dat[cur]%= 10
    score[cur]+= dat[cur]+1
    dice += 3
    dice%=100
    cur = not(cur)
    c+=1
    # print(score,dat,dice)
    # input()
print(min(score)*c*3)

from collections import deque
from itertools import product
from functools import lru_cache

@lru_cache(maxsize=None)
def winsFrom(r):
    if r[0]>=21:
        return 1,0
    if r[1]>=21:
        return 0,1
    a,b = 0,0
    for dRoll in product(range(1,4),repeat=3):
        s1,s2,p1,p2,turn=r
        n = sum(dRoll)
        if turn:
            p1 += n
            if p1>10:p1-=10
            s1 += p1
        else:
            p2+=n
            if p2>10:p2-=10
            s2+=p2
        da,db = winsFrom((s1,s2,p1,p2,not(turn)))
        a+=da;b+=db
    return a,b

a,b = winsFrom((0,0,dd[0]+1,dd[1]+1,True))
print(max(a,b))
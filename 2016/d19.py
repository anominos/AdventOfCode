num = 3001330
n=1
while n < num:
    n*=2
n//=2
print((num-n) * 2 + 1)




from collections import deque
from math import ceil
def sim2(num):
    l = deque(range(1,num+1))
    while len(l)>1:
        prev = len(l)
        if len(l)%2==1:
            l = deque(j for i,j in enumerate(l) if i<len(l)//2 or (i-len(l)//2)%3==1)
        else:
            l = deque(j for i,j in enumerate(l) if i<len(l)//2 or (i-len(l)//2)%3==2)
        l.rotate(-prev+len(l))
    return l[0]
print(sim2(num))
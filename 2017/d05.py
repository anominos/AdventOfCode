o = []
with open("d05in.txt") as f:
    for x in f:
        o.append(int(x.strip()))
l = o[:]
i=0 
c=0
while i<len(l):
    l[i]+=1
    i+= l[i]-1
    c+=1
print(c)
from time import time
ttt = time()

l = o[:]
i=0 
c=0
while i<len(l):
    if l[i] >=3:
        l[i]-=1
        n=True
    else:
        l[i]+=1
        n=False
    i+= l[i]+(1 if n else -1)
    c+=1
print(c)
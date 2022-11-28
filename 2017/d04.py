l =[]
with open("d04in.txt") as f:
    for x in f:
        l.append(x.strip().split())
c=0
for x in l:
    c+= len(x)==len(set(x))
print(c)
c=0
from collections import Counter
for x in l:
    x = list(map(lambda a:tuple(sorted(a)), x))
    c+= len(x)==len(set(x))
print(c)
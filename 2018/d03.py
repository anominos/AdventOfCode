import re
d={}
pat = re.compile("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
with open("d03in.txt") as f:
    for x in f:
        mtch = re.match(pat,x).groups()
        idd, x,y,width,height = map(int,mtch)
        d[idd] = [x,y,width,height]
from collections import defaultdict
a = defaultdict(list)
b = []
for idd, dat in d.items():
    b.append(idd)
    for y in range(dat[1], dat[1]+dat[3]):
        for x in range(dat[0], dat[0]+dat[2]):
            a[(x,y)].append(idd)

c=0
for i in a.values():
    c+=len(i)>1
print(c)
b = set(b)
for y in a.values():
    if len(y)>1:
        b.difference_update(y)

print(b.pop())

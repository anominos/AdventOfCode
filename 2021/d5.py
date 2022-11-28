dat = []
with open("d5in.txt") as f:
    for x in f:
        dat.append((x.strip()))
from collections import defaultdict
dd = defaultdict(int)
import re
for x in dat:
    a,b,c,d = map(int, re.findall("(\d+)", x))
    if a==c:
        for y in range(min(b,d),max(b,d)+1):
            dd[(a,y)]+=1
    elif b==d:
        for n in range(min(a,c), max(a,c)+1):
            dd[(n,b)]+=1

c=0
for x in dd.values():
    if x>1:
        c+=1
print(c)


from collections import defaultdict
dd = defaultdict(int)
import re
for x in dat:
    a,b,c,d = map(int, re.findall("(\d+)", x))
    if a==c:
        for y in range(min(b,d),max(b,d)+1):
            dd[(a,y)]+=1
    elif b==d:
        for n in range(min(a,c), max(a,c)+1):
            dd[(n,b)]+=1
    else:
        dx = (a-c)//abs(a-c)
        dy = (b-d)//abs(b-d)
        start = (c,d)
        while start != (a,b):
            dd[start]+=1
            start = (start[0]+dx, start[1]+dy)
        dd[start]+=1

c=0
for x in dd.values():
    if x>1:
        c+=1
print(c)

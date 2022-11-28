dat = []
with open("d17in.txt") as f:
    for x in f.read().split("\n"):
        dat.append((x.strip()))
from collections import defaultdict
d = defaultdict(bool)
for x in range(len(dat)):
    for y in range(len(dat[x])):
        d[x,y,0,0] = dat[x][y] == "#"
for turn in range(6):
    # print(d)
    newd = defaultdict(bool)
    toVisit = {a for a,b in d.items() if b}
    Visited = set()
    while toVisit:
        (x, y, z, w) = toVisit.pop()
        Visited.add((x, y, z, w))
        c=0
        for (dx, dy, dz, dw) in [(i,j,k,l) for i in range(-1, 2)for j in range(-1, 2)for k in range(-1, 2) for l in range(-1, 2) if not(i==j==l==k==0)]:
            if d[x,y,z,w] and not((x+dx, y+dy, z+dz, w+dw) in Visited):toVisit.add((x+dx, dy+y, z+dz, w+dw))
            if d[x+dx, dy+y, z+dz, w+dw]:
                c+=1
        if d[x, y, z,w]:
            if not(c==2 or c==3):
                newd[x,y,z,w] = False
            else:
                newd[x,y,z,w] = True
        else:
            if c==3:
                newd[x,y,z,w] = True
            else:
                newd[x,y,z,w] = False
    d = newd.copy()
c=0
for y in d.values():
    if y:
        c+=1
print(c)
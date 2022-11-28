dat = []
with open("d24in.txt") as f:
    for x in f.read().split("\n"):
        dat.append((x.strip()))

from collections import defaultdict
d = defaultdict(bool)
aname = "e se sw w nw ne".split()
c=0
adjs = [[1, 0], [1, -1], [0, -1], [-1, 0], [-1, 1], [0,1]]
for x in dat:
    xx, yy = 0,0
    i=0
    ins = []
    while i < len(x):
        if x[i] in "ns":
            ins.append(x[i:i+2])
            i+=1
        else:
            ins.append(x[i])
        i+=1
    # print(ins, x)
    for x in ins:
        dx, dy = adjs[aname.index(x)]
        xx+=dx
        yy+=dy
    # print(xx, yy)
    if  d[xx,yy]:
        c+=1
    d[xx, yy] = not(d[xx, yy])

c=0
for x in d.values():
    if x:
        c+=1
print(c)

for turn in range(100):
    todo = set(d.keys())
    done = set()
    change = []
    while todo:
        x, y = todo.pop()
        done.add((x, y))
        c=0
        for dx, dy in adjs:
            if d[x+dx, y+dy]:
                c+=1
            if d[x, y] and (x+dx, y+dy) not in done:
                todo.add((x+dx, y+dy))
        if d[x, y]:
            if c==0 or c > 2:
                change.append((x, y))
        else:
            if c==2:
                change.append((x, y))
    for x,y in change:
        d[x, y] = not(d[x, y])
c=0
for x in d.values():
    if x:
        c+=1
        
print(c)
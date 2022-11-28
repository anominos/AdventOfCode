dat = []
with open("d9in.txt") as f:
    for x in f:
        dat.append(list(map(int, x.strip())))

adj = [[0,1],[0,-1],[1,0],[-1,0]]

c=0
l = []
for x in range(len(dat)):
    for y in range(len(dat[0])):
        f = True
        for dx,dy in adj:
            if 0<= x+dx<len(dat) and 0<=y+dy < len(dat[0]):
                if dat[x+dx][y+dy] <= dat[x][y]:
                    f=False
        if f:
            c+= dat[x][y]+1
            l.append((x,y))
print(c)
from collections import Counter
f = []

for start in l:
    q = [start]
    done = set()
    c=0
    while q:
        # print(q)
        x,y = q.pop()
        done.add((x,y))
        c+=1
        for dx, dy in adj:
            if 0<= x+dx<len(dat) and 0<=y+dy < len(dat[0]):
                if dat[x+dx][y+dy]!=9 and not((x+dx, y+dy) in done):
                    q.append((x+dx, y+dy))
                    done.add((x+dx,y+dy))
                    
        # print(q)
    f.append(c)
    # print()
r=(sorted(f, reverse=True)[:3])
print(r[0]*r[1]*r[2])
# print(r)
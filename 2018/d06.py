maxx = maxy = 500
grid = [[-1]*maxx for _ in range(maxy)]
c=0
d = []
from collections import defaultdict

with open("d06in.txt") as f:
    for x in f:
        a, b = map(int, x.strip().split(", "))
        d.append((a,b))
        grid[b][a] = c
        c+=1
alls = set(range(c))
edge = set()
for x in range(maxx):
    for y in range(maxy):
        minn = float("inf")
        c = -1
        for i,j in enumerate(d):
            comp = abs(j[0] - x) + abs(j[1]-y)
            if comp < minn:
                minn = comp
                c=i
            elif comp==minn:
                c=-1
        grid[y][x] = c
        if x==0 or y==0 or x==maxx-1 or y==maxy-1:edge.add(c)
    
d2 =defaultdict(int)
for x in grid:
    for y in alls-edge:
        d2[y]+=x.count(y)
print(max(d2.values()))

dis = 10000
done = set()
good = []
todo = {(250,250)}
adj = [[0,1],[1,0],[-1,0],[0,-1]]
while todo!=set():
    x, y = todo.pop()
    done.add((x,y))
    dd=0
    for i in d:
        ox, oy = i
        dd+= abs(ox-x)+abs(oy-y)
    if dd<dis:
        good.append((x,y))
        for i,j in adj:
            new = (x+i, y+j)
            if not new in done:
                todo.add(new)
print(len(good))

'''
'''
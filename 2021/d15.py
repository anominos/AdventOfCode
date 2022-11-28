dat = []
with open("d15in.txt") as f:
    for x in f:
        dat.append(list(map(int, x.strip())))
X = len(dat[0])
Y = len(dat)
def gdat(x,y):
    dx,mx = divmod(x,X)
    dy,my = divmod(y,Y)
    a = dat[my][mx]+dx+dy
    if a>9:
        a-=9
    return a
from collections import defaultdict
from heapq import *
d = defaultdict(lambda : float("inf"))
d[0,0] = gdat(0,0)
visited = set()
todo = [(gdat(0,0), gdat(0,0),0,0)]
adj = [[0,1],[0,-1],[1,0],[-1,0]]
while todo:
    heu,di,x,y = heappop(todo)
    if (x,y) == (5*X-1, 5*Y-1):
        break
    visited.add((x,y))
    if di==d[x,y]:
        for dx,dy in adj:
            if 0<=x+dx < 5*X and 0<= y+dy < 5*Y and not((x+dx,y+dy) in visited):
                tgs = di+gdat(x+dx,y+dy)
                if tgs < d[x+dx,y+dy]:
                    d[x+dx,y+dy] = tgs
                    heappush(todo, (di+gdat(x+dx, y+dy)+x+y,di+gdat(x+dx,y+dy), x+dx, y+dy))

print(d[X-1,Y-1]-gdat(0,0))
print(d[5*X-1,5*Y-1]-gdat(0,0))
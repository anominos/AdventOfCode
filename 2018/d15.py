from heapq import *
from collections import deque
l = []
with open("d15test.txt") as f:
    for x in f:
        l.append(list(x.strip()))

XSIZE = len(l[0])
YSIZE = len(l)
print(XSIZE, YSIZE)
walls = []
gob = []
elv = []
for x in l:
    walls.append([y=="#" for y in x])
    gob.append([y=="G" for y in x])
    elv.append([y=="E" for y in x])

# print(len(walls), len(walls[0]))

def empty(x,y):
    # print(x,y,len(walls[0]),len(gob[0]),len(elv[0]))
    return not(walls[y][x] or gob[y][x] or elv[y][x])

gpos, epos = [], []
for y in range(len(l)):
    for x in range(len(l[y])):
        if l[y][x] == "G":
            heappush(gpos, (y,x))
        elif l[y][x] == "E":
            heappush(epos, (y,x))

def nxt(g,e):
    if not(g):return heappop(e)
    if not(e):return heappop(g)
    if g[0] < e[0]:
        return heappop(g)
    else:
        return heappop(e)

ADJS = [[0,1],[1,0],[0,-1],[-1,0]]
def closestTargs(x,y,targs):
    q = deque([(x,y,0)])
    done = {(x,y)}
    stop = 1000000
    l = []
    while q:
        cx,cy,d = q.popleft()
        if d > stop:break
        for dx, dy in ADJS:
            ny, nx = cy+dy,cx+dx
            if 0<=nx<XSIZE and 0<=ny<YSIZE:
                if empty(nx,ny) and not((nx,ny) in done):
                    q.append((nx,ny,d+1))
                    done.add((nx,ny))
                if ((ny,nx) in targs):
                    l.append((nx,ny))
                    stop = d
        # print(q)
    return l


def move(x,y,isgob):
    l = closestTargs(x, y, (epos if isgob else gpos))
    print(l, x, y)

while gpos or epos:
    cury,curx = nxt(gpos, epos)
    isgob = gob[cury][curx]
    move(curx,cury,isgob)

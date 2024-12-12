# flake8: noqa

*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return list((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

from collections import *
import numpy as np
import math
from utils import *

DIAG_DIRS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # Clockwise from north for (i,j): l[di][dj]
ADJ_DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NWSE for (i, j): l[di][dj]


d = defaultdict(list)
done = set()
c=0
edges = defaultdict(set)

def floodfill(pos, c):
    sx, sy = pos
    q = deque([pos])
    targ = l[sx][sy]
    done.add(pos)
    while q:
        cx, cy = q.popleft()
        d[c].append((cx, cy))
        for dx, dy in ADJ_DIRS:
            if 0<=cx+dx<len(l) and 0<=cy+dy<len(l) and l[cx+dx][cy+dy] == targ:
                if (cx+dx, cy+dy) not in done:
                    q.append((cx+dx, cy+dy))
                    done.add((cx+dx, cy+dy))
            else:
                edges[c].add((cx, cy, dx, dy))

debug_c = {}

for x in range(len(l)):
    for y in range(len(l[x])):
        if (x, y) in done:
            continue

        start = (x, y)
        floodfill(start, c)
        debug_c[c] = l[x][y]
        c+=1
ans = 0
for x in range(c):
    ans += len(d[x]) * len(edges[x])
print(ans)

def calc(edg):
    dd = defaultdict(list)
    for cx, cy, dx, dy in edg:
        dd[dx, dy].append((cx, cy))
    g=0
    for a in dd:
        s = defaultdict(list)
        if a[0] != 0:
            for posx, posy in dd[a]:
                s[posx].append(posy)
        else:
            for posx, posy in dd[a]:
                s[posy].append(posx)
        for lst in s.values():
            r = 1
            lst = sorted(lst)
            for i in range(len(lst)-1):
                if lst[i]+1 != lst[i+1]:
                    r += 1
            g += r

    return g

ans = 0
for x in range(c):
    ans += len(d[x]) * calc(edges[x])
    # print(debug_c[x], len(d[x]) , calc(edges[x]))
print(ans)
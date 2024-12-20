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
ADJ_DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NESW for (i, j): l[di][dj]

for x in range(len(l)):
    for y in range(len(l[x])):
        if l[x][y] == "S":
            start = (x, y)
        if l[x][y] == "E":
            end = (x, y)

fromstart = {start:0}
visited = {start}
q = deque([(0, start)])
while q:
    d, (cx, cy) = q.popleft()
    fromstart[cx, cy] = d
    for dx, dy in ADJ_DIRS:
        if 0<=cx+dx<len(l) and 0<=cy+dy<len(l[x]):
            if l[cx][cy] != "#":
                if (cx+dx, cy+dy) not in visited:
                    visited.add((cx+dx, cy+dy))
                    q.append((d+1, (cx+dx, cy+dy)))

fromend = {end: 0}
visited = {end}
q = deque([(0, end)])
while q:
    d, (cx, cy) = q.popleft()
    fromend[cx, cy] = d
    for dx, dy in ADJ_DIRS:
        if 0<=cx+dx<len(l) and 0<=cy+dy<len(l[x]):
            if l[cx][cy] != "#":
                if (cx+dx, cy+dy) not in visited:
                    visited.add((cx+dx, cy+dy))
                    q.append((d+1, (cx+dx, cy+dy)))
base = fromstart[end]

c=0
for x in range(1, len(l)-1):
    for y in range(1, len(l[x])-1):
        # print(x, y)
        if l[x][y] == "#":
            score = []
            if (l[x+1][y] != "#" and l[x-1][y] != "#"):
                score.append(fromstart[x+1, y] + fromend[x-1, y] + 2)
                score.append(fromstart[x-1,y] + fromend[x+1, y] + 2)
            if l[x][y+1] != "#" and l[x][y-1] != "#":
                score.append(fromstart[x, y+1] + fromend[x, y-1] + 2)
                score.append(fromstart[x,y-1] + fromend[x, y+1] + 2)
            for s in score:
                if base - s >= 100:
                    c+=1
print(c)



c=0
for sx in range(1, len(l)-1):
    for sy in range(1, len(l[x])-1):
        if l[sx][sy] == "#":
            continue
        for ex in range(max(1, sx-20), min(len(l)-1, sx+21)):
            for ey in range(max(1, sy-20+abs(ex-sx)), min(len(l[x])-1, sy+21-abs(ex-sx))):
                if l[sx][sy] != "#" and l[ex][ey] != "#":
                    s = fromstart[sx, sy] + fromend[ex, ey] + abs(ex-sx) + abs(ey-sy)
                    if base-s >= 100:
                        c+=1

print(c)
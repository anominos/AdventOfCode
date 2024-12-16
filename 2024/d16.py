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

d = 1
for x in range(len(l)):
    for y in range(len(l[0])):
        if l[x][y] == "S":
            pos = (x, y)
from heapq import *
visited = set()
q = [(0, pos, d)]
minscore = defaultdict(lambda: float("inf"))
minscore[*pos, d] = 0
prev = defaultdict(list)
first = False
while q:
    score, (cx, cy), cd = heappop(q)
    if score > minscore[cx, cy, cd]:
        continue
    if l[cx][cy] == "E":
        if not first:
            print(score)
            end = cx, cy, cd
            first = True


    dx, dy = ADJ_DIRS[cd]
    if l[cx+dx][cy+dy] != "#":
        if minscore[cx+dx, cy+dy, cd] > score+1:
            prev[cx+dx, cy+dy, cd] = [(cx, cy, cd)]
            minscore[cx+dx, cy+dy, cd] = score+1
            heappush(q, (score+1, (cx+dx, cy+dy), cd))
        elif minscore[cx+dx, cy+dy, cd] == score+1:

            prev[cx+dx, cy+dy, cd].append((cx, cy, cd))
            # heappush(q, (score+1, (cx+dx, cy+dy), cd))

    for nd in [(cd+1)%4, (cd+3)%4]:
        ndx, ndy = ADJ_DIRS[nd]
        if l[cx+ndx][cy+ndy] != "#":
            if minscore[cx, cy, nd] > score+1000:
                prev[cx, cy, nd] = [(cx, cy, cd)]
                minscore[cx, cy, nd] = score+1000
                heappush(q, (score+1000, (cx, cy), nd))
            elif minscore[cx, cy, nd] == score+1000:
                prev[cx, cy, nd].append((cx, cy, cd))
                # heappush(q, (score+1000, (cx, cy), nd))

# for d in range(4):
#     print(prev[7, 5, d])

visited = set()
def recback(x, y, d):
    if (x, y, d) in visited:
        return set()
    visited.add((x, y, d))
    s = {(x, y)}
    for back in prev[x, y, d]:
        s |= recback(*back)
    return s

print(len(set(recback(*end))))
for x,y in recback(*end):
    l[x][y] = "O"

# flake8: noqa

*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return list(map(int, x))

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

def calc(sx, sy):
    q = deque([(sx, sy)])
    s = set()
    r = []
    while q:
        cx, cy = q.popleft()
        if l[cx][cy] == 9:
            s.add((cx, cy))
            r.append((cx, cy))
        for dx, dy in ADJ_DIRS:

            if 0<=cx+dx<len(l) and 0<=cy+dy<len(l[x]) and l[cx+dx][cy+dy] == l[cx][cy]+1:
                q.append((cx+dx, cy+dy))
    return len(s), len(r)

c2=0
c=0
for x in range(len(l)):
    for y in range(len(l[x])):
        if l[x][y] == 0:
            r1, r2 = calc(x, y)
            c+=r1
            c2+=r2
print(c)
print(c2)
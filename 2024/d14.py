# flake8: noqa

*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    return tuple([*map(int, re.findall(r"-?\d+",x)),])
    return str((x))

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

XMOD = 101
YMOD = 103

# XMOD = 11
# YMOD = 7

state = l[:]
for _ in range(100):

    nw = []
    for x, y, dx, dy in state:
        x += dx
        y += dy
        x = (x + XMOD) % XMOD
        y = (y + YMOD) % YMOD
        nw.append((x, y, dx, dy))
    state = nw

d = Counter()
for (x, y, _, _) in state:
    if x==XMOD//2 or y==YMOD//2:
        continue
    d[x<XMOD//2, y<YMOD//2] += 1



m = 1

for i in d.values():
    m*=i
print(m)

# done = set()

def printgrid(s, f=None):
    g = [[0] * 101 for _ in range(103)]
    for x, y, _, _ in s:
        g[y][x] += 1
    for a in g:
        print("".join(map(str, a)).replace("0", "."), file=f)

# def calc()

# with open("d14outless.txt", "w") as f:
state = l[:]
coh = (float("inf"), -1)
for t in range(1, 10403+1):
    # s = tuple(sorted(state))
    # if s in done:
    #     print(t)
    #     break
    # done.add(s)
    nw = []
    for x, y, dx, dy in state:
        x += dx
        y += dy
        x = (x + XMOD) % XMOD
        y = (y + YMOD) % YMOD
        nw.append((x, y, dx, dy))
    state = nw
    midx = XMOD//2
    midy=YMOD//2
    # midy=sum(y for _, y, _, _ in state)
    # midx=sum(x for x, _, _, _ in state)
    nc = sum((i-midx)**2+(j-midy)**2 for i, j, _, _ in state)
    # nc = sum(x for x, y, _, _ in state)
    # nc = calc(s)
    # if -nc < coh[0] or abs(t-5074) < 3:
    #     print(t)
    coh = min((nc, t), coh)
    # if t == 1328:
    #     printgrid(state)
    # if t == 10378:
    #     print(nc)
    if t == 7753:
        with open("2024/d14output.txt","w") as f:
            printgrid(state, f)
    # if nc > 27000:
    #     printgrid(state, f)
    #     print(str(t) + "\n\n", file=f)
print(coh[1])
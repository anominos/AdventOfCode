# flake8: noqa

*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    return [*map(int, re.findall(r"-?\d+",x)),]
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
ADJ_DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NESW for (i, j): l[di][dj]


# l1 = []
def step(x):
    if x==0:return 0
    if x<0:return -1
    return 1

horiz_ranges = []
vert_ranges = []

for i, (a, b) in enumerate(l):
    # l1.append((a, b))
    nxta,nxtb = l[(i+1)%len(l)]
    # ra,rb = (nxta-a, nxtb-b)
    # l1.append((a+step(ra), b+step(rb)))

    if a==nxta:
        vert_ranges.append((sorted([b, nxtb]), a))
    else:
        horiz_ranges.append((sorted([a, nxta]), b))

setl = set(map(tuple, l))

def inside(x, y):
    if (x, y) in setl:
        return True
    c=0
    for (l, h), yy in horiz_ranges:
        if l<= x <= h and y == yy:
            return True
        if l <= x < h and y < yy:
            c += 1
    if c%2==0:
        return False
    c=0
    for (l, h), xx in vert_ranges:
        if l <= y <= h and x == xx:
            return True
        if l <= y < h and x < xx:
            c += 1
    if c%2==0:
        return False
    return True

mx=0
mx1 = 0
for i, (a, b) in enumerate(l):
    for c, d in l[i:]:
        mx = max(mx, (abs(d-b)+1) * (abs(c-a)+1))
        if (abs(d-b)+1) * (abs(c-a)+1) < mx1:
            continue

        # f = True
        # poi =[]
        # for x, y in l:
        #     if (a<x<c or c<x<a) and (b<y<d or d<y<b):
        #         f = False
        #         break
        #     if (x==a or x==c) and (b<y<d or d<y<b):
        if a<c:
            na = a+1
        else:
            na  = a-1
        if b<d:
            nb = b+1
        else:
            nb = b-1

        if not inside(na, nb):
            continue
        good = True
        for ((lb, hb), yy) in horiz_ranges:
            if b<yy<d or d<yy<b:
                if not(hb <= min(a, c) or lb>=max(a, c)):
                    good = False
        for ((lb, hb), xx) in vert_ranges:
            if a<xx<c or c<xx<a:
                if not(hb <= min(b, d) or lb >= max(b, d)):
                    good = False
                    # if (a, b, c, d) == (1, 15, 6, 9):
                    #     print(lb, hb, xx)

        # if (a, b, c, d) == (1, 15, 6, 9):
        #     print(good)
        if good:
            mx1 = max(mx1, (abs(d-b)+1) * (abs(c-a)+1))
            # print(a, b, c, d, (abs(d-b)+1) * (abs(c-a)+1))

print(mx)
print(mx1)

# 1,1
# 1,15
# 7,15
# 7,4
# 6,4
# 6,9
# 3,9
# 3,1

# l = """
# .................
# .#.............#.
# .................
# .#.......#.......
# .................
# .................
# ....#....#.......
# ....#..........#.
# .................
# """
# for i, x in enumerate(l.splitlines()):
#     for j, y in enumerate(x):
#         if y == "#":
#             print(f"{i},{j}")
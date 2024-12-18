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
l = list(map(tuple, l))
block = set()

def do(block, dop = False):
    cp = (0, 0)
    targ = (70, 70)
    # targ = (6, 6)
    visited = set([cp])

    q = deque([(0, cp)])
    while q:
        d, (cx, cy) = q.popleft()
        if (cx, cy) == targ:
            if dop:print(d)
            return True

        for dx, dy in ADJ_DIRS:
            if 0<=cx+dx<=targ[0] and 0<=cy+dy<=targ[1]:
                if (cx+dx, cy+dy) not in block:
                    if (cx+dx, cy+dy) not in visited:
                        visited.add((cx+dx, cy+dy))
                        q.append((d+1, (cx+dx, cy+dy)))
    return False

do(l[:1024], True)

low = 1024
high =len(l)

while low < high:
    mid = (low+high)//2
    block = set(l[:mid])
    if do(block):
        low = mid+1
    else:
        high = mid

print(*l[low-1], sep=",")
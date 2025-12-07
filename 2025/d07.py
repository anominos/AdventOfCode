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

start = {l[0].index("S")}
d = Counter()
d[l[0].index("S")] += 1
c=0
for x in range(1, len(l)):
    nw = set()
    nd = Counter()
    for y in start:
        if l[x][y] == "^":
            nw.add(y+1)
            nd[y+1] += d[y]
            nw.add(y-1)
            nd[y-1] += d[y]
            c+=1
        else:
            nd[y] += d[y]
            nw.add(y)
    start = nw
    d = nd

print(c)
print(sum(d.values()))
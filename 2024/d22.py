# flake8: noqa

*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return int((x))

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
MOD = 16777216
c=0
diffs = []
prices = []
for d in l:
    a = [d]
    for _ in range(2000):
        d = ((d<<6)^d)%MOD
        d = ((d>>5)^d)%MOD
        d = ((d<<11)^d)%MOD
        a.append(d % 10)
    prices.append(a[1:])
    diffs.append([a[i+1]-a[i] for i in range(len(a)-1)])
    c += d
print(c)

seqtoprice = []
g = defaultdict(int)
for arr, dif in zip(prices, diffs):
    seqtoprice.append({})
    for i in range(len(arr)-4):
        seq = tuple(dif[i:i+4])
        if seq not in seqtoprice[-1]:
            seqtoprice[-1][seq] = arr[i+3]
            g[seq] += arr[i+3]

print(max(g.values()))
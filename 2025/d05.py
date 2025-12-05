# flake8: noqa

*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    return [[*map(int, re.findall(r"\d+",i)),] for i in x.split("\n")]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().strip().split("\n\n"):
        if x!="":
            l.append(func(x))

from collections import *
import numpy as np
import math
from utils import *

DIAG_DIRS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # Clockwise from north for (i,j): l[di][dj]
ADJ_DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NESW for (i, j): l[di][dj]
ranges, n = l

c=0
for [x] in n:
    for a, b in ranges:
        if a<=x<=b:
            c+=1
            break
print(c)

merge_ranges = []
for a, b in ranges:
    to_remove = []
    for c, d in merge_ranges:
        if c <= a <= d:
            a = d+1
        if c <= b and d >= b:
            b = c-1
        if a <= c <= d <= b:
            to_remove.append((c, d))
    if a <= b:
        merge_ranges.append((a, b))
    for x in to_remove:
        merge_ranges.remove(x)

cc = 0
for a, b in merge_ranges:
    cc += b-a + 1
print(cc)
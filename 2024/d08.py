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
for x in range(len(l)):
    for y in range(len(l[x])):
        d[l[x][y]].append((x, y))

s = set()
for letter in d.keys():
    if letter == ".":
        continue
    for a in d[letter]:
        for b in d[letter]:
            if a==b:continue
            dd = a[0] - b[0], a[1] - b[1]
            r1 = (a[0] + dd[0], a[1] + dd[1])
            r2 = (b[0] - dd[0], b[1] - dd[1])

            if 0<=r1[0]<len(l) and 0<=r1[1] < len(l[0]):
                # if l[r1[0]][r1[1]] == ".":
                    s.add(r1)

            if 0<=r2[0]<len(l) and 0<=r2[1] < len(l[0]):
                # if l[r2[0]][r2[1]] == ".":
                    s.add(r2)

print(len(s))

s = set()
for letter in d.keys():
    if letter == ".":
        continue
    for a in d[letter]:
        for b in d[letter]:
            if a==b:continue
            dd = a[0] - b[0], a[1] - b[1]

            r1 = a
            while 0<=r1[0]<len(l) and 0<=r1[1] < len(l[0]):
                # if l[r1[0]][r1[1]] == ".":
                s.add(r1)
                r1 = r1[0] + dd[0], r1[1] + dd[1]

            r1 = b
            while 0<=r1[0]<len(l) and 0<=r1[1] < len(l[0]):
                # if l[r1[0]][r1[1]] == ".":
                s.add(r1)
                r1 = r1[0] - dd[0], r1[1] - dd[1]


print(len(s))
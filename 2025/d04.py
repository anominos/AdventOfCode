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
cc=0
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] != "@":
            continue
        c=0
        for di, dj in DIAG_DIRS:
            if 0<=i+di < len(l) and 0 <= j+dj < len(l[i]):
                c += l[i+di][j+dj] == "@"
        if c < 4:
            cc += 1
print(cc)

cc=0
changed = True
while changed:
    changed = False
    s = []
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] != "@":
                continue
            c=0
            for di, dj in DIAG_DIRS:
                if 0<=i+di < len(l) and 0 <= j+dj < len(l[i]):
                    c += l[i+di][j+dj] == "@"
            if c < 4:
                cc += 1
                s.append((i, j))
    for i, j in s:
        l[i][j] = "."
        changed = True
print(cc)

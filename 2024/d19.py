# flake8: noqa

*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
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

patterns = l[0].split(", ")
tries = l[1:]

import functools
@functools.lru_cache(maxsize=None)
def ispossible(pattern:str):
    if pattern=="":return True
    for x in patterns:
        if pattern.startswith(x):
            if ispossible(pattern[len(x):]):
                return True
    return False

@functools.lru_cache(maxsize=None)
def count(pattern:str):
    if pattern=="":return 1
    c=0
    for x in patterns:
        if pattern.startswith(x):
            c += count(pattern[len(x):])
    return c


c=0
for x in tries:
    if ispossible(x):
        c+=1

print(c)
c=0
for x in tries:
    c+=count(x)

print(c)
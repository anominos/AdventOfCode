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

ns = "9876543210"
c=0
for x in l:
    for i in ns:
        if i in x:
            index = x.index(i)
            if index != len(x)-1:
                break
    mx = "0"
    for j in x[index+1:]:
        mx = max(mx, j)
    c += int(i+mx)
print(c)

from functools import lru_cache
import sys
sys.setrecursionlimit(8196)


def ss(a):
    if a  == 0:
        return ""
    return a
c2=0
for x in l:
    @lru_cache(maxsize=None)
    def dp(i, n):
        # dp(i, n) = max from x[i:] using n numbers
        if n==0:
            return 0
        if i==len(x):
            return None

        mx = -1
        if (a:=dp(i+1, n-1)) is not None:
            mx = int(f"{x[i]}{ss(a)}")
        if (b:=dp(i+1, n)) is not None:
            mx = max(mx, b)
        if mx == -1:
            return None
        return mx
    c2 += (dp(0, 12))
print(c2)
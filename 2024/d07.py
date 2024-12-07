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
ADJ_DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NWSE for (i, j): l[di][dj]
r = 0
def func(g, ans, part2=False):
    if g==[]:
        return ans == 0
    if ans%g[-1] == 0:
        if func(g[:-1], ans//g[-1], part2):
            return True
    if ans >= g[-1]:
        if func(g[:-1], ans-g[-1], part2):
            return True
    if part2:
        if str(ans).endswith(str(g[-1])):
            r = ans // 10**len(str(g[-1]))
            if func(g[:-1], r, part2):
                return True
    return False
c=0
for x in l:
    ans, *g = x
    if func(g, ans):
        c+=ans
print(c)
c=0
for x in l:
    ans, *g = x
    if func(g, ans, True):
        c+=ans
print(c)
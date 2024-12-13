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
    for x in f.read().split("\n\n"):
        if x!="":
            l.append(func(x))

from collections import *
import numpy as np
import math
from utils import *

import z3

DIAG_DIRS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # Clockwise from north for (i,j): l[di][dj]
ADJ_DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NWSE for (i, j): l[di][dj]

ans=0
for line in l:
    a, b, c, d, e, f = line
    A, B = [[a, c], [b, d]], [e, f]
    x = (np.linalg.solve(A, B))

    s = z3.Optimize()
    x1 = z3.Int("x1")
    y1 = z3.Int("y1")
    cost = z3.Int("cost")
    # ax + cy = e

    s.add(a * x1 + c * y1 == e, b*x1 + d*y1 == f)
    s.add(cost == x1 * 3 + y1)
    h = s.minimize(cost)
    if s.check() == z3.sat:
        s.lower(h)
        cst = (s.model()[cost].as_long())
        ans+= cst
        # print(s.model()[cost])

print(ans)

ans=0
for line in l:
    a, b, c, d, e, f = line
    e += 10000000000000
    f += 10000000000000
    s = z3.Optimize()
    x1 = z3.Int("x1")
    y1 = z3.Int("y1")
    cost = z3.Int("cost")
    # ax + cy = e

    s.add(a * x1 + c * y1 == e, b*x1 + d*y1 == f)
    s.add(cost == x1 * 3 + y1)
    h = s.minimize(cost)
    if s.check() == z3.sat:
        s.lower(h)
        ans+=(s.model()[cost].as_long())
        # print(s.model()[cost])
print(ans)

def eea(a, b):
    x = 1
    y = 0
    while b > 0:
        x, y = y, x-y*(a//b)
        a, b = b, a%b
    return x, y
from math import gcd
import numpy
ans = 0
for line in l:
    a, b, c, d, e, f = line
    det = a*d - b*c
    if det != 0:
        aa, bb = d*e - c*f, a*f - b*e
        if aa%det ==0 and bb%det == 0:
            aa //= det
            bb //= det
            if aa>=0 and bb>=0:
                ans += 3*aa+bb
print(ans)
ans = 0
for line in l:
    a, b, c, d, e, f = line
    e += 10000000000000
    f += 10000000000000
    det = a*d - b*c
    if det != 0:
        aa, bb = d*e - c*f, a*f - b*e
        if aa%det ==0 and bb%det == 0:
            aa //= det
            bb //= det
            if aa>=0 and bb>=0:
                ans += 3*aa+bb
print(ans)
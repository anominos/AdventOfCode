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

def intersect(a, b):
    pxa, pya, _, vxa, vya, _ = a
    pxb, pyb, _, vxb, vyb, _ = b

    M = np.array([
        [vxa, -vxb],
        [vya, -vyb],
    ])
    if np.linalg.det(M) == 0:
        return
    N = np.array([pxb-pxa, pyb-pya])
    ta, tb = (np.linalg.solve(M, N))
    if ta < 0 or tb < 0:
        return
    return (pxa + vxa * ta), (pya + vya * ta)

L, H = 200000000000000, 400000000000000
# L, H = 7, 27
c=0
for i, x in enumerate(l):
    for j, y in enumerate(l):
        if i<j:
            # print(x, y)
            # print(intersect(x, y))
            if (z:=intersect(x, y)) is not None:
                if (L <= z[0] <= H and
                    L <= z[1] <= H):
                    c += 1
print(c)

import z3
a, b, c, d, e, f = (z3.Real(i) for i in "abcdef")
ts = []
s = z3.Solver()
for i, x in enumerate(l):
    ti = z3.Real('t'+str(i))
    px, py, pz, vx, vy, vz = x
    s.add(a - px + (b-vx) * ti == 0, ti >= 0)
    s.add(c - py + (d-vy) * ti == 0, ti >= 0)
    s.add(e - pz + (f-vz) * ti == 0, ti >= 0)
    ts.append(ti)
s.check()
m = (s.model())
a, c, e = (str(m[a]), str(m[c]), str(m[e]))
# print(a, c, e)
print(int(a) + int(c) + int(e))
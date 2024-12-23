# flake8: noqa

*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return x.split("-")

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

d = defaultdict(set)
for a, b in l:
    d[a].add(b)
    d[b].add(a)
import itertools
s = set()
for x, y in d.items():
    if len(y)>1:
        for a in itertools.permutations(y, 2):
            if a[1] in d[a[0]]:
                s.add(tuple(sorted(a + (x, ))))
c=0
for x in s:
    if any(i[0] == "t" for i in x):
        c+=1
print(c)

def recurse(cur: set, avail: set, unavail: set):
    if not avail and not unavail:
        return cur
    m = set()
    while avail:
        v = avail.pop()
        m = max(m, recurse(cur|{v}, avail & d[v], unavail & d[v]), key=len)
        unavail.add(v)
    return m

print(*sorted(recurse(set(), set(d), set())), sep=",")

# # original attempt:
# f = True
# while f:
#     f = False
#     ns = set()
#     for x in s:
#         for y in d:
#             if all(y in d[i] for i in x):
#                 ns.add(tuple(sorted(x + (y,))))
#                 f = True
#     if not f:
#         print(",".join(s.pop()))
#     s = ns
#     print(len(s))
# print(s)
# flake8: noqa

*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
l2 = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return x.split()

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))
            l2.append(x)

from collections import *
import numpy as np
import math
from utils import *

DIAG_DIRS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # Clockwise from north for (i,j): l[di][dj]
ADJ_DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NESW for (i, j): l[di][dj]

c=0
for i in range(len(l[0])):
    r = []
    for j in l:
        r.append(j[i])

    x = list(map(int, r[:-1]))

    if r[-1] == "+":
        c += sum(x)
    else:
        g = 1
        for i in x:
            g*=i
        c+=g
print(c)

c2=0
cur=0
for i in range(len(l2[0])):
    chars = []
    for j in l2:
        if i >= len(j):
            chars.append(" ")
        else:
            chars.append(j[i])

    if chars[-1] != " ":
        c2 += cur
        op = chars[-1]
        cur = 0 if op=="+" else 1

    if all(i==" " for i in chars[:-1]):
        continue
    n = int("".join(chars[:-1]))
    if op=="+":
        cur += n
    else:
        cur *= n

c2 += cur
print(c2)
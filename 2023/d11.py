*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return list((i=="#" for i in x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

from collections import *
import numpy as np
import math

def expand(l):
    nw = []
    for i, x in enumerate(l):
        if not any(x):
            nw.append(x)
        nw.append(x)

    for _ in range(2):
        nw = list(zip(*nw[::-1]))

    nw2 = []
    for i, x in enumerate(zip(*nw[::-1])):
        if not any(x):
            nw2.append(x)
        nw2.append(x)

    return list(zip(*nw2[::-1]))

from copy import deepcopy
l2 = deepcopy(l)
l = expand(l)
gal = []
for x in range(len(l)):
    for y in range(len(l[x])):
        if l[x][y]:
            gal.append((x, y))

c=0
for i in gal:
    for j in gal:
        if i<j:
            c += abs(i[0] - j[0]) + abs(i[1] - j[1])
print(c)

row, col = [], []
for i in range(len(l2)):
    if not any(l2[i]):
        row.append(i)
    if not any(j[i] for j in l2):
        col.append(i)

gal=[]
for x in range(len(l2)):
    for y in range(len(l2[x])):
        if l2[x][y]:
            gal.append((
                x + 999_999 * sum(1 for i in row if i < x),
                y + 999_999 * sum(1 for i in col if i < y)
            ))

c=0
for i in gal:
    for j in gal:
        if i<j:
            c += abs(i[0] - j[0]) + abs(i[1] - j[1])
print(c)

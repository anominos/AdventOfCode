# flake8: noqa

*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

dep = []
l =[]
import re
def func(x):
    return [*map(int, re.findall(r"-?\d+",x)),]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    a,b = f.read().split("\n\n")
    for x in a.split("\n"):
        if x!="":
            dep.append(func(x))
    for x in b.split("\n"):
        if x!="":
            l.append(func(x))

from collections import *
import numpy as np
import math
from utils import GridFunc

DIAG_DIRS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # Clockwise from north for (i,j): l[di][dj]
ADJ_DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NWSE for (i, j): l[di][dj]

d = defaultdict(set)
for x,y in dep:
    d[y].add(x)

c=0
for update in l:
    f =True
    for x in range(len(update)):
        if d[update[x]] & set(update[x:]):
            f = False
    if f:
        c+=update[len(update)//2]
print(c)


c2=0
for update in l:
    f =True
    while f:
        f = False
        for x in range(len(update)):
            if d[update[x]] & set(update[x:]):
                f = True
                for y in d[update[x]] & set(update[x:]):
                    update.remove(y)
                    update.insert(0, y)
                break



for update in l:
    c2+=update[len(update)//2]
print(c2-c)
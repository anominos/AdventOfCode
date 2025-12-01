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

dial = 50
c=0
c2=0
for x in l:
    d, n = x[0], int(x[1:])
    if d=="L":
        for _ in range(n):
            dial -= 1
            dial = (dial+100)%100
            if dial ==0:
                c2+=1
        # dial -= n
    else:
        for _ in range(n):
            dial += 1
            dial = (dial+100)%100

            if dial ==0:
                c2+=1
        # dial += n
    dial = (dial+100)%100
    if dial==0:
        c+=1
print(c)
print(c2)
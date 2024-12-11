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

state = l[0]

def step_state(prev):
    nw = []
    for x in prev:
        if x==0:
            nw.append(1)
        elif len(str(x))%2==0:
            s = str(x)
            a, b = s[:len(s)//2], s[len(s)//2:]
            nw.append(int(a))
            nw.append(int(b))
        else:
            nw.append(x*2024)
    return nw

for _ in range(25):
    state = step_state(state)

print(len(state))


state = l[0]

import functools
@functools.lru_cache(maxsize=None)
def count_end(num: int, rem = 75):
    if rem==0:
        return 1

    if num==0:
        return count_end(1, rem-1)
    elif len(str(num))%2==0:
        s = str(num)
        a, b = s[:len(s)//2], s[len(s)//2:]
        a, b = int(a), int(b)
        return count_end(a, rem-1) + count_end(b, rem-1)
    else:
        return count_end(num*2024, rem-1)

c=0
for x in state:
    c += count_end(x)
print(c)

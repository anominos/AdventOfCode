# flake8: noqa

*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    return [*map(int, re.findall(r"\d+",x)),]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split(","):
        if x!="":
            l.append(func(x))

from collections import *
import numpy as np
import math
from utils import *

DIAG_DIRS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # Clockwise from north for (i,j): l[di][dj]
ADJ_DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NESW for (i, j): l[di][dj]

def get_next_front(base, repeats):
    if len(base) % repeats == 0:
        front = a[:len(a)//repeats]
    else:
        front = "1" + ("0" * (len(b)//repeats - 1))
    return front

c=0
for a, b in l:
    a = str(a)
    b = str(b)
    assert len(b) <= len(a)+1
    if len(a) % 2 == 0:
        front = a[:len(a)//2]
    elif len(b) %2 == 0:
        front = "1"  + ("0"*(len(b)//2 - 1))
    # print(a, b, front)

    n = int(front+front)
    while n <= int(b):
        if int(a) <= n:
            c += n
        front = str(int(front) + 1)
        # print(a, b, front, n)
        n = int(front+front)

print(c)
c2=0
for a, b in l:
    a, b = str(a), str(b)
    g = set()
    for rep in range(2, len(b)+1):
        front = get_next_front(a, rep)
        while (i:=int(front*rep)) <= int(b):
            if i >= int(a):
                g.add(i)
                # print(i)
            front = str(int(front) + 1)
    c2 += sum(g)
print(c2)
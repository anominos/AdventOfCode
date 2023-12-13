*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    a = []
    for y in x.split("\n"):
        if y!="":
            a.append([i=="#" for i in y])
    return a

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n\n"):
        if x!="":
            l.append(func(x))

from collections import *
import numpy as np
import math

def check_start(a, b):
    for x, y in zip(a, b):
        if x!=y:
            return False
    return True

def findmirr(grid, skip=-1):
    for i in range(1, len(grid)):
        if i==skip:
            continue
        if check_start(grid[:i][::-1], grid[i:]):
            return i
    return None

c=0
c2=0
for x in l:
    r = findmirr(x)
    if r is not None:
        d = r * 100
    else:
        d=findmirr(list(zip(*x[::-1])))
    c+=d
    stop = False
    for i in range(len(x)):
        for j in range(len(x[i])):
            x[i][j] = not x[i][j]

            if r is not None:
                s = findmirr(x, skip=r)
            else:
                s = findmirr(x)

            if s is not None:
                e = s * 100
            else:
                if r is None:
                    e=findmirr(list(zip(*x[::-1])), skip=d)
                else:
                    e=findmirr(list(zip(*x[::-1])))

            if e is not None and d != e:
                c2+=e
                stop = True
                break

            x[i][j] = not x[i][j]
        if stop:break
    if not stop:
        pass
        # print(x)


print(c)
print(c2)
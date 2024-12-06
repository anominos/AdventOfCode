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
ADJ_DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NWSE for (i, j): l[di][dj]
def do(l, do_print=False):
    for x in range(len(l)):
        for y in range(len(l[x])):
            if l[x][y] == "^":
                cur = (x, y)

    d = 0
    s = set()
    turn_points = []

    while cur not in s:
        s.add((cur, d))
        cd = ADJ_DIRS[d]
        nxt = cur[0] + cd[0], cur[1] + cd[1]
        if not(0<=nxt[0]<len(l) and 0<=nxt[1]<len(l[0])):
            break
        if l[nxt[0]][nxt[1]] == "#":
            turn_points.append(cur)

        while l[nxt[0]][nxt[1]] == "#":
            d += 1
            d %= 4
            cd = ADJ_DIRS[d]
            nxt = cur[0] + cd[0], cur[1] + cd[1]


        cur = nxt
        if (cur,d) in s:
            return True

    r = {i[0] for i in s}
    if do_print:
        print(len(r))
    return False

do(l, True)
c=0
l = [list(i) for i in l]
for i in range(len(l)):
    for j in range(len(l[0])):
        if l[i][j] == ".":
            l[i][j] = "#"

            if do(l):
                c+=1

            l[i][j] = "."
print(c)

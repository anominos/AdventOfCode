*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return list((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

from collections import *
import numpy as np
import math


def get_dirs(char, d):
    match char:
        case ".":
            nwdirs = [d]
        case "|":
            if d[0] == 0:
                nwdirs = [(1, 0), (-1, 0)]
            else:
                nwdirs = [d]
        case "-":
            if d[1] == 0:
                nwdirs = [(0, 1), (0, -1)]
            else:
                nwdirs = [d]
        case "/":
            nwdirs = [(-d[1], -d[0])]
        case "\\":
            nwdirs = [(d[1], d[0])]
    return nwdirs

def run_with(start, start_d):
    visiting = [(start, i) for i in get_dirs(l[start[0]][start[1]], start_d)]
    visited = set()

    while visiting:
        cur = visiting.pop()
        visited.add(cur)
        pos, d = cur
        nwpos = pos[0]+d[0], pos[1]+d[1]
        if 0<=nwpos[0]<len(l) and 0<=nwpos[1]<len(l[0]):
            for nwd in get_dirs(l[nwpos[0]][nwpos[1]], d):
                if (nwpos, nwd) not in visited:
                    visiting.append((nwpos, nwd))

    s = set()
    for x, _ in visited:
        s.add(x)
    return (len(s))

print(run_with((0, 0), (0, 1)))

m = 0
for x in range(len(l)):
    m = max(m, run_with((x, 0), (0, 1)))
    m = max(m, run_with((x, len(l[0])-1), (0, -1)))

for x in range(len(l[0])):
    m = max(m, run_with((0, x), (1, 0)))
    m = max(m, run_with((len(l)-1, x), (-1, 0)))

print(m)
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

def proc(l):
    return "".join(map("".join, l))

s = []
while proc(l) not in s:
    s.append(proc(l))
    for j in range(4):
        for x in range(len(l)):
            for y in range(len(l[x])):
                if l[x][y] == "O":
                    nx = x
                    while nx>0:
                        nx-=1
                        if l[nx][y] != ".":
                            nx+=1
                            break
                    l[x][y] = "."
                    l[nx][y] = "O"
        if len(s) == 1 and j==0:
            c=0
            for i, x in enumerate(l):
                c+=(x.count("O") * (len(l)-i))
            print(c)
        l = list(map(list, zip(*reversed(l))))

tot = int(1e9//4)
cycle_length = len(s) - s.index(proc(l))
use_index = (tot - len(s)) % cycle_length + s.index(proc(l)) + 1
def unproc(s):
    r = []
    for i in range(0, len(l) * len(l[0]), len(l)):
        r.append(s[i:i+len(l)])
    return r
l = (unproc(s[use_index]))

c=0
for i, x in enumerate(l):
    c+=(x.count("O") * (len(l)-i))
print(c)
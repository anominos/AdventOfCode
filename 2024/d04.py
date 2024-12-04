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
            l.append(x.strip())

from collections import *
import numpy as np
import math
c=0
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j:j+4] == "XMAS" or l[i][j:j+4] == "SAMX":
            c+=1
            print(i, j)

l = list(zip(*l[::-1]))
print(l)
for i in range(len(l)):
    for j in range(len(l[i])):
        if "".join(l[i][j:j+4]) == "XMAS" or "".join(l[i][j:j+4]) == "SAMX":
            c+=1
            print(i, j)

for i in range(len(l)):
    for j in range(len(l[i])):
        for di, dj in [(a, b) for a in [-1, 1] for b in [-1, 1]]:
            ci, cj = i, j
            s=""
            for _ in range(4):
                if 0<=ci < len(l) and 0<=cj<len(l[i]):
                    s += l[ci][cj]
                    ci+=di
                    cj+=dj
            if s=="XMAS":
                c+=1
                print("diag",ci,cj)
print(c)

c2=0
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] == "A":
            r = []
            for di, dj in [(a, b) for a in [-1, 1] for b in [-1, 1]]:
                if 0<=i+di < len(l) and 0<=j+dj<len(l[i]):
                    r.append(l[i+di][j+dj])
            if r.count("M") == 2 and r.count("S") ==2:
                if r[0] != r[-1]:
                    c2+=1
print(c2)
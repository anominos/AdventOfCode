# flake8: noqa

*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return (x.split(": "))

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

d = {}
for src, dst in l:
    d[src] = dst.split()

num_sols = {}
def recurse(node):
    if node in num_sols:
        return num_sols[node]
    if node == "out":
        return 1
    num_sols[node] = sum(recurse(i) for i in d[node])
    return num_sols[node]

print(recurse("you"))


num_sols2 = {}
def recurse2(node, fft, dac):
    if (node, fft, dac) in num_sols2:
        return num_sols2[node, fft, dac]
    if node == "out":
        return int(fft and dac)

    num_sols2[node, fft, dac] = sum(recurse2(i, fft or node == "fft", dac or node=="dac") for i in d[node])
    return num_sols2[node, fft, dac]


print(recurse2("svr", False, False))


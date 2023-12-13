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
from functools import lru_cache

@lru_cache(maxsize=None)
def do_count(s, n, prev_dot=True):
    if s=="":
        if len(n)==0 or (len(n) == 1 and n[0] == 0):
            return 1
        else:
            return 0
    if len(n)==0:
        n = (0, )
    if s[0] == "#":
        r = (n[0]-1, *n[1:])
        if r[0] < 0:
            return 0
        return do_count(s[1:], r, False)
    elif s[0] == ".":
        if n[0] == 0:
            return do_count(s[1:], n[1:])
        else:
            if n[0] < 0:
                return 0
            elif n[0] > 0 and not prev_dot:
                return 0
            else:
                return do_count(s[1:], n)
    else:
        return do_count("." + s[1:], n, prev_dot) + do_count("#" + s[1:], n, prev_dot)


c=0
c2=0
for i, x in enumerate(l):
    s, n = x.split(" ")
    n = tuple(map(int, n.split(",")))
    c+=do_count(s, n)
    c2+=do_count("?".join([s]*5), n*5)
print(c)
print(c2)
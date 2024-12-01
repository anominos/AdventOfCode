# flake8: noqa

*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    return [*map(int, re.findall(r"-?\d+",x)),]
    # return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

from collections import *
import numpy as np
import math
a = []
b = []
for x,y in l:
    a.append(x)
    b.append(y)
ans =0
for c, d  in zip(sorted(a), sorted(b)):
    ans += abs(c-d)
print(ans)


b = Counter(b)
a2 = 0
for x in a:
    a2 += b[x] * x
print(a2)
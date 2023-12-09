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

def predict(lst):
    if all(i == lst[0] for i in lst):
        return lst[0]
    else:
        return lst[-1] + predict(np.diff(lst))
def predict2(lst):
    if all(i == lst[0] for i in lst):
        return lst[0]
    else:
        return lst[0] - predict2(np.diff(lst))
c=0
c2=0
for x in l:
    c+=(predict(x))
    c2+=predict2(x)
print(c)
print(c2)
# flake8: noqa

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
c=0
for x in l:
    df = np.diff(x)
    if (np.all(df>0) or np.all(df<0)) and 1<=min(np.abs(df)) and max(np.abs(df))<=3:
        c+=1
print(c)

c=0
for x in l:
    df = np.diff(x)
    if (np.all(df>0) or np.all(df<0)) and 1<=min(np.abs(df)) and max(np.abs(df))<=3:
        c+=1
        continue
    for y in range(len(x)):
        z = x[:y] + x[y+1:]
        df = np.diff(z)
        if (np.all(df>0) or np.all(df<0)) and 1<=min(np.abs(df)) and max(np.abs(df))<=3:
            c+=1
            print(z)
            break
print(c)
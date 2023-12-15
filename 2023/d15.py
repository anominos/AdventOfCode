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

s = l[0].strip()
c=0

def HASH(x):
    cv = 0
    for i in x:
        cv += ord(i)
        cv *= 17
        cv %= 256
    return cv



boxes = defaultdict(dict)

for x in s.split(","):
    c+=HASH(x)
    ##
    if "=" in x:
        a, b = x.split("=")
        boxes[HASH(a)][a] = b
    else:
        a = x[:-1]
        if a in boxes[HASH(a)]:
            del boxes[HASH(a)][a]

print(c)
c2=0
for i, x in boxes.items():
    for j, v in enumerate(list(x.values()), start=1):
        c2 += j * int(v) * (1 + i)
print(c2)
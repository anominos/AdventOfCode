*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):

    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))
from collections import defaultdict

c=0
for x in l:
    g, x = x.split(": ")
    g = int(g[5:])
    x = x.split("; ")
    f = True
    for y in x:
        y = y.split(", ")
        d = defaultdict(int)
        for z in y:
            a, b = z.split()
            d[b] = int(a)
        if d["green"] <= 13 and d["red"] <= 12 and d["blue"] <= 14:
            pass
        else: f = False
    if f:
        c+=g
print(c)

c = 0
for x in l:
    g, x = x.split(": ")
    g = int(g[5:])
    x = x.split("; ")
    f = True
    d = defaultdict(int)
    for y in x:
        y = y.split(", ")
        for z in y:
            a, b = z.split()
            d[b] = max(d[b], int(a))
    m = 1
    for i in d.values():
        m*=i
    c+=m
print(c)
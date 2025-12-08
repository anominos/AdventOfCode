# flake8: noqa

*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    return (*map(int, re.findall(r"-?\d+",x)),)
    return str((x))

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

for x in l:
    for y in l:
        if x<y:
            d[(x, y)] = sum([(i-j)*(i-j) for i,j in zip(x, y)])

adj_lst = defaultdict(list)
g = list(sorted(d.items(), key=lambda a: a[1]))
print(g[0])
for i, ((a,b), d) in enumerate(g):
    if i==1000:
        break
    adj_lst[a].append(b)
    adj_lst[b].append(a)

ff = {}
def fill(node, num):
    ff[node] = num
    for x in adj_lst[node]:
        if x not in ff:
            fill(x, num)

for a in l:
    if a in ff:
        continue
    fill(a, a)

a, b, c, *h = sorted(Counter(ff.values()).values(), reverse=True)
print(a*b*c)

num_comps = 3 + len(h)

def get_root(a):
    if a == ff[a]:
        return a

    ff[a] = get_root(ff[a])
    return ff[a]


def merge(a, b):
    global num_comps
    if get_root(a) > get_root(b):
        a, b = b, a

    if ff[get_root(b)] != get_root(a):
        num_comps -= 1
        print(a, b)
        if num_comps == 1:
            print(a[0] * b[0])
            return True
    ff[get_root(b)] = get_root(a)
    return False

for i, ((a,b), d) in enumerate(g[1000:]):
    adj_lst[a].append(b)
    adj_lst[b].append(a)

    if merge(a, b):break
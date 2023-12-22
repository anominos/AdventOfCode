*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    # return list((x))
    # return str((x))
    return [*map(int, re.findall(r"-?\d+",x)),]

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

from collections import *
import numpy as np
import math

cur_points = set()
cur_bricks = []
for a, b, c, d, e, f in l:
    assert a<=d and b<=e and c<=f
    br = set()
    for x in range(a, d+1):
        for y in range(b, e+1):
            for z in range(c, f+1):
                br.add((x, y, z))
                cur_points.add((x, y, z))
    cur_bricks.append(br)

run = True
while run:
    run = False
    for i, br in enumerate(cur_bricks):
        nwb = []
        for x, y, z in br:
            if z-1 <= 0 or ((x, y, z-1) in cur_points and (x, y, z-1) not in br):
                break
            nwb.append((x, y, z-1))
        else:
            cur_points -= set(br)
            cur_points |= set(nwb)
            cur_bricks[i] = nwb
            run  = True

# print(cur_bricks)

supported_by = defaultdict(set)
b_map = {}
for i, x in enumerate(cur_bricks):
    for y in x:
        b_map[y] = i

for i, br in enumerate(cur_bricks):
    for x, y, z in br:
        if (x, y, z-1) in b_map and b_map[x, y, z-1] != i:
            supported_by[i].add(b_map[x, y, z-1])
ans = set(range(len(cur_bricks)))
for x in supported_by.values():
    if len(x) == 1:
        j = list(x)[0]
        ans -= {j}
print(len(ans))

c=0
for x in set(range(len(cur_bricks)))-ans:
    falling = {x}
    run = True
    while run:
        run = False
        for k, v in supported_by.items():
            if k not in falling and v.issubset(falling):
                falling.add(k)
                run = True
    c += len(falling)-1
print(c)
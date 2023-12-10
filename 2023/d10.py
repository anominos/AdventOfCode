*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return list((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

from collections import *
import numpy as np
import math

d = defaultdict(set)

start = tuple()

for x in range(len(l)):
    for y in range(len(l[x])):
        if l[x][y] == "|":
            a, b = (x-1, y), (x+1, y)
        elif l[x][y] == "-":
            a, b = (x, y-1), (x, y+1)
        elif l[x][y] == "L":
            a, b = (x-1, y), (x, y+1)
        elif l[x][y] == "J":
            a, b = (x-1, y), (x, y-1)
        elif l[x][y] == "7":
            a, b = (x+1, y), (x, y-1)
        elif l[x][y] == "F":
            a, b = (x+1, y), (x, y+1)
        elif l[x][y] == "S":
            start = (x, y)
            continue
        else:
            continue

        if len(l) > a[0] >= 0 and len(l[x]) > a[1] >= 0:
            d[x, y].add(a)
            d[a].add((x, y))
        if 0<=b[0] < len(l) and 0 <= b[1] < len(l[x]):
            d[x, y].add(b)
            d[b].add((x, y))

visited = set()
todo = {start}
c=0
while todo:
    nw = set()
    for nxt in todo:
        visited.add(nxt)
        x, y = nxt
        if l[x][y] == "|":
            a, b = (x-1, y), (x+1, y)
        elif l[x][y] == "-":
            a, b = (x, y-1), (x, y+1)
        elif l[x][y] == "L":
            a, b = (x-1, y), (x, y+1)
        elif l[x][y] == "J":
            a, b = (x-1, y), (x, y-1)
        elif l[x][y] == "7":
            a, b = (x+1, y), (x, y-1)
        elif l[x][y] == "F":
            a, b = (x+1, y), (x, y+1)
        elif l[x][y] == "S":
            a, b = list(d[nxt])
        for adj in (a, b):
            if adj not in visited:
                nw.add(adj)
    todo = nw
    # print(todo, c+1)
    c+=1
print(c-1)


# def get_adj(x, y):
#     def check(nx, ny):
#         return 0<=nx<len(l) and 0<=ny<len(l[nx])
#     for dx in [-1, 1]:
#         if check(x+dx, y):
#             yield x+dx, y
#     for dy in [-1, 1]:
#         if check(x, y+dy):
#             yield x, y+dy


# ff = [[None] * len(l[0]) for _ in range(len(l))]
# def floodfill(x, y, i):
#     if ff[x][y] is not None:
#         return x==0 or y==0 or x==len(l)-1 or y == len(l[0])-1
#     ff[x][y] = i
#     f = False
#     for nx, ny in get_adj(x, y):
#         if (nx, ny) not in visited:
#             f |= floodfill(nx, ny, i)
#     return x==0 or y==0 or x==len(l)-1 or y == len(l[0])-1 or f


# i=0
# good = []
# for x in range(len(l)):
#     for y in range(len(l[x])):
#         if ff[x][y] is None and (x, y) not in visited:
#             if not floodfill(x, y, i):
#                 good.append(i)
#             i+=1
# print(ff, good)
# c2=0
# for x in ff:
#     for i in good:
#         c2+=x.count(i)
# print(c2)

# loop = [start]
# while loop.count(start) == 1:
#     x, y = loop[-1]
#     if l[x][y] == "|":
#         a, b = (x-1, y), (x+1, y)
#     elif l[x][y] == "-":
#         a, b = (x, y-1), (x, y+1)
#     elif l[x][y] == "L":
#         a, b = (x-1, y), (x, y+1)
#     elif l[x][y] == "J":
#         a, b = (x-1, y), (x, y-1)
#     elif l[x][y] == "7":
#         a, b = (x+1, y), (x, y-1)
#     elif l[x][y] == "F":
#         a, b = (x+1, y), (x, y+1)
#     elif l[x][y] == "S":
#         a, b = list(d[x, y])

#     if len(loop) >= 2 and a == loop[-2]:
#         loop.append(b)
#     else:
#         loop.append(a)
# print(loop)
a,b = d[start]
x, y = start
if a[0] == b[0]:
    start_replace = "-"
elif a[1] == b[1]:
    start_replace = "|"
elif sorted([a, b]) == sorted([(x-1, y), (x, y+1)]):
    start_replace = "L"
elif sorted([a, b]) == sorted([(x-1, y), (x, y-1)]):
    start_replace = "J"
elif sorted([a, b]) == sorted([(x+1, y), (x, y-1)]):
    start_replace = "7"
elif sorted([a, b]) == sorted([(x+1, y), (x, y+1)]):
    start_replace = "F"

import re
c2=0
for x in range(len(l)):
    cur_len = 0
    closed = False
    y=0
    while y < (len(l[x])):
        if (x, y) in visited:
            cur = l[x][y]
            if cur == "S":
                cur = start_replace
            if cur in "|7J":
                closed = not closed
            elif cur in "FL":
                start = cur
                while True:
                    y+=1
                    cur = l[x][y]
                    if cur == "S":
                        cur = start_replace
                    if cur != "-":
                        break
                if (start == "F" and cur == "J") or (start == "L" and cur == "7"):
                    closed = not closed
        else:
            c2+=closed
        y+=1
print(c2)
# def get_dir(x, y):
#     cur_i = loop.index((x, y))
#     while loop[cur_i][0] == x:
#         cur_i += 1
#         cur_i %= len(loop)
#     return loop[cur_i][0] > x


# for x in range(len(l)):
#     st = None
#     cur_len = 0
#     for y in range(len(l[x])):
#         if (x, y) in visited:
#             if st is not None:
#                 if get_dir(*st) != get_dir(x, y):
#                     c2+=cur_len

#             cur_len = 0
#             st = (x, y)

#         else:
#             cur_len += 1
# print(c2)
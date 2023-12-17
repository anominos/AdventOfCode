*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return [int(i) for i in x]

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

from collections import *
import numpy as np
import math
# print(l)

# cache = {}


# def find_path(x, y, d, num_consec, path):
#     if (x, y) in path:
#         return 1e9
#     if num_consec >= 3:
#         return 1e9
#     if (x, y) == (len(l)-1, len(l[0])-1):
#         return 0
#     if (x, y, d, num_consec) in cache:
#         return cache[x, y, d, num_consec]

#     path.append((x, y))
#     best = 1e9
#     for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#         if 0<=x+dx<len(l) and 0<=y+dy<len(l[0]):
#             nw_cons = 0
#             if d == (dx, dy):
#                 nw_cons = num_consec+1
#             nw = find_path(x+dx, y+dy, (dx,dy), nw_cons, list(path))
#             best = min(best, nw + l[x+dx][y+dy])
#     # print(path)
#     for i in range(0, num_consec+1):
#         cache[x, y, d, i] = min(best, cache.get((x, y, d, i), 1e9))
#     return best

# print(find_path(0, 0, (0, 0), 0, []))
# d = defaultdict(list)
# for x in cache:
#     if cache[x] != 1e9:
#         d[x[0], x[1]].append(cache[x])

# path = [(0, 0)]
# cur = d[path[0]][0]
# while path[-1] not in [(11, 12), (12, 11)]:
#     cx, cy = path[-1]
#     m=0
#     for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#         if (cx+dx, cy+dy) in d:
#             if cur - l[cx+dx][cy+dy] in d[cx+dx, cy+dy]:
#                 path.append((cx+dx, cy+dy))
#                 cur -= l[cx+dx][cy+dy]
#                 m+=1
#     print(m)
# print(d)
# print(path)
# for i in range(len(l)):
#     for j in range(len(l[0])):
#         if (i, j) in path:
#             print(end="#")
#         else:
#             print(end=".")
#     print()
import heapq
visiting = [(0, 0, 0, 0, 0)]
visited = set()

while True:
    # print(visiting)
    distance, x, y, dx, dy = heapq.heappop(visiting)
    if (x, y) == (len(l)-1, len(l[0])-1):
        print(distance)
        break
    if (x, y, dx, dy) in visited:
        continue
    visited.add((x, y, dx, dy))
    for ndx, ndy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if (dx, dy) == (ndx, ndy) or (dx, dy) == (-ndx, -ndy):
            continue
        c=0
        for step in range(1, 4):
            nx, ny = x + (ndx*step), y+(ndy*step)
            if 0<=nx<len(l) and 0<=ny<len(l[0]):
                c+=l[nx][ny]
                heapq.heappush(visiting, (
                    distance + c,
                    nx, ny,
                    ndx, ndy,
                ))


## p2

visiting = [(0, 0, 0, 0, 0)]
visited = set()



while True:
    # print(visiting)
    distance, x, y, dx, dy = heapq.heappop(visiting)
    if (x, y) == (len(l)-1, len(l[0])-1):
        print(distance)
        break
    if (x, y, dx, dy) in visited:
        continue
    visited.add((x, y, dx, dy))
    for ndx, ndy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if (dx, dy) == (ndx, ndy) or (dx, dy) == (-ndx, -ndy):
            continue
        c=0
        for step in range(1, 4):
            nx, ny = x + (ndx*step), y+(ndy*step)
            if 0<=nx<len(l) and 0<=ny<len(l[0]):
                c+=l[nx][ny]

        for step in range(4, 11):
            nx, ny = x + (ndx*step), y+(ndy*step)
            if 0<=nx<len(l) and 0<=ny<len(l[0]):
                c+=l[nx][ny]
                heapq.heappush(visiting, (
                    distance + c,
                    nx, ny,
                    ndx, ndy,
                ))




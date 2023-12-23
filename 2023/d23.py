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

for i, x in enumerate(l[0]):
    if x==".":
        start = (0, i)


for i, x in enumerate(l[-1]):
    if x==".":
        end = (len(l)-1, i)

def get_adj(x, y):
    for dx in [-1, 1]:
        if 0<=x+dx<len(l):
            yield x+dx, y
    for dy in [-1, 1]:
        if 0<=y+dy<len(l[0]):
            yield x, y+dy

visiting = [(start, set([start]))]
lengths = [0]

mp = dict(zip("^v<>", [[-1, 0], [1, 0], [0, -1], [0, 1]]))

# print(mp)

while visiting:
    cur, visited = visiting.pop()
    if cur == end:
        lengths.append(len(visited)-1)
        # if len(visited) == 97:
        #     s = visited

    visited.add(cur)
    for nx, ny in get_adj(*cur):
        if (nx, ny) in visited:
            continue
        if l[nx][ny] == ".":
            visiting.append(((nx, ny), visited|{(nx, ny)}))
        elif l[nx][ny] in "<>v^":
            r = mp[l[nx][ny]]
            if (nx+r[0], ny+r[1]) not in visited:
                visiting.append((
                    (nx+r[0], ny+r[1]),
                    visited|{(nx, ny), (nx+r[0], ny+r[1])}
                ))
print(max(lengths))

# for x in range(len(l)):
#     for y in range(len(l[x])):
#         if (x, y) in s:
#             print(end="O")
#         else:
#             print(end=l[x][y])
#     print()

crosses = set()
for x in range(len(l)):
    for y in range(len(l[x])):
        if l[x][y] != "#":
            if sum(l[i][j]!="#" for i,j in get_adj(x, y)) != 2:
                crosses.add((x, y))
crosses.add(end)

edges = defaultdict(dict)

visiting = [(start, start, 0, None)]
visited = set()
while visiting:
    cur, prev, d, p1 = visiting.pop()
    nw = []
    if cur in crosses:
        edges[prev][cur] = d
        edges[cur][prev] = d
        prev = cur
        d=0
    if cur in visited:
        continue
    for nx, ny in get_adj(*cur):
        if l[nx][ny] != "#" and (nx, ny) != p1:
            nw.append((nx, ny))

    for i in nw:
        visiting.append(
            (i, prev, d+1, cur)
        )
    if cur in crosses:
        visited.add(cur)
# print(edges)
# print("Generated edges")
# print(len(edges))
ls = []
def search(cur, d, visited):
    if cur == end:
        ls.append(d)
        return
    visited.add(cur)
    for nei, nd in edges[cur].items():
        if nei not in visited:
            search(nei, d + nd, visited)
    visited.remove(cur)

search(start, 0, set())
print(max(ls))

# import networkx as nx
# G = nx.Graph({i: list(j.keys()) for i, j in edges.items()})
# nx.draw_planar(G, with_labels=True)

# def manhatten(a, b):
#     return abs(a[0]-b[0]) + abs(a[1]-b[1])

# openset = [(0, start)]
# gscore = defaultdict(lambda : float("inf"))
# gscore[start] = 0
# import heapq
# fscore = defaultdict(lambda : float("inf"))
# fscore[start] = -manhatten(end, start)
# visited = set()
# while openset:
#     _, cur = heapq.heappop(openset)
#     if cur in visited:
#         continue
#     visited.add(cur)
#     if cur == end:
#         break
#     for nei, d in edges[cur].items():
#         tent_gscore = gscore[cur] - d
#         if tent_gscore < gscore[nei]:
#             gscore[nei] = tent_gscore
#             fscore[nei] = tent_gscore - manhatten(nei, end)
#             heapq.heappush(openset, (fscore[nei], nei))
# print(gscore[end])


# dists = defaultdict(lambda : float("inf"))
# dists[start] = 0
# visiting = [(0, start)]
# visited = set()
# import heapq
# while visiting:
#     _, cur = heapq.heappop(visiting)
#     if cur in visited:
#         continue
#     visited.add(cur)
#     for n, d in edges[cur].items():
#         if dists[n] > dists[cur]-d:
#             dists[n] = dists[cur] - d
#             heapq.heappush(visiting, (dists[n], n))

# print(dists)


# visiting = [(start, 0, set())]
# ls = []
# while visiting:
#     cur, d, visited = visiting.pop()
#     if cur == end:
#         ls.append(d)
#         s = visited
#     for n, nd in edges[cur].items():
#         if n not in visited:
#             visiting.append((
#                 n, d+nd, visited|{cur}
#             ))
#     print(len(visiting))
# print(max(ls))
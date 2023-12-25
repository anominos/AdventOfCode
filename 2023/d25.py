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

import sys
sys.setrecursionlimit(4096)

edges = defaultdict(list)
for x in l:
    s, ds = x.split(": ")
    ds = ds.split(" ")
    for i in ds:
        edges[s].append(i)
        edges[i].append(s)

import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph(edges)
pairs = (nx.minimum_edge_cut(G))

# nx.draw(G, with_labels=True)
# plt.show()


# edges: hxq/txl zcj/rtt tpn/gxv
# pairs = "hxq,txl zcj,rtt tpn,gxv".split(" ")
# pairs = "hfx,pzl bvb,cmg nvd,jqt".split(" ")

for pair in pairs:
    a, b = pair
    edges[a].remove(b)
    edges[b].remove(a)


d = {}
def dfs(x, i):
    d[x] = i
    for j in edges[x]:
        if j not in d:
            dfs(j, i)

c=1
for n in edges.keys():
    if n not in d:
        dfs(n, c)
        c+=1
a, b = 0, 0
for i in d:
    if d[i] == 1:
        a+=1
    else:
        b+=1

print(a*b)


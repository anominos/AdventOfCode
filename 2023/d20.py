*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return re.match(r"([%&]?[a-z]+) -> (.+)", x).groups()

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

from collections import *
import numpy as np
import math

inps = defaultdict(list)
d = {}
for a, b in l:
    if a=="broadcaster":
        start = b.split(", ")
    else:
        d[a[1:]] = (a[0], b.split(", "))
        for x in b.split(", "):
            inps[x].append(a[1:])
r = sorted(set(d.keys()) | set(inps.keys()))

def do(mem, init=None, track=[]):
    track = {i: 0 for i in track}
    if init is None:
        q = deque((i, False) for i in start)
    else:
        q = deque(init)
    c1=0  # l
    c2=1  # h
    while q:
        # print(q[0])
        cur, rcv = q.popleft()
        if cur in track:
            track[cur] +=  not rcv
        if rcv:
            c1+=1
        else:
            c2+=1
        if cur not in d:
            continue
        t, nxt = d[cur]
        if t == "%":
            if not rcv:
                mem[cur] = not mem[cur]
                for x in nxt:
                    q.append((x, mem[cur]))
        elif t == "&":
            if all(mem[y] for y in inps[cur]):
                mem[cur] = False
            else:
                mem[cur] = True
            for x in nxt:
                q.append((x, mem[cur]))
    if len(track) > 0:
        return mem, c2, c1, track
    return mem, c2, c1

curm = defaultdict(bool)
alll = 0
allh = 0
c=0
ans = None
seen = []
prevseen = None
cc=0
while c < 1000:
    curm, low, high = do(curm)
    # print(curm, low, high)
    alll += low
    allh += high
    c += 1
    # if "rx" in curm and ans is None:
    #     ans = c
    if c==1000:
        print(alll * allh)

    # a = curm["zq"]
    # if prevseen is None or a != prevseen:
    #     l.append(cc)
    #     prevseen = a
    #     cc=0
    # else:
    #     cc+=1
# print(ans)

# adjl = {i: j for i, (_, j) in d.items()}
# adjl["broadcast"] = start
# print(adjl)
# labels = {i: t+i for i, (t, _) in d.items()}
# labels["rx"] = "rx"
# labels["broadcast"] = "broadcast"

# import networkx as nx
# import matplotlib.pyplot as plt
# G = nx.DiGraph(adjl)
# nx.draw_planar(G, labels=labels, with_labels = True)
# plt.show()

# for x in d:
#     if d[x][0] == "&":
#         nodes = inps[x]

#         if all(d[n][0] == "%" for n in nodes):
#             s1 = set(nodes)
#             s2 = set()
#             for n in nodes:
#                 s2 |= set(d[n][1])
#             print(sorted(nodes))
#             print(sorted(s2))
#             # print(s2, s1)

curm = defaultdict(bool)
r = defaultdict(list)
for n in range(20000):
    curm, _, _, tracked = do(curm, track=inps[inps["rx"][0]])
    for i, j in tracked.items():
        if j > 0:
            r[i].append(n)

s = {}
for x in r:
    s[x] = r[x][1] - r[x][0]

from math import lcm
print(lcm(*s.values()))

# from functools import reduce
# def crt(l):
#     l = list(l)
#     m, n = [], []
#     p = reduce(lambda a, b: a*b, l)
#     for x in l:
#         m.append(p//x)
#         n.append(pow(m[-1], -1, x))
#     c=0
#     for i in range(len(m)):
#         c += (l[i]-1) * m[i] * n[i]
#     return c % p

# print(crt(s.values()))

# 232605773145468
# 232605773145466
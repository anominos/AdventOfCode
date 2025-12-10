# flake8: noqa

*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
from functools import reduce
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    # return str((x))
    return x.split()

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

cc = 0
for x in l:
    targ, *b, r = x

    targ = [i=="#" for i in targ[1:-1]]
    b = [list(map(int, i[1:-1].split(","))) for i in b]
    targn=0
    for i, x in enumerate(targ):
        if x:
            targn |= 1<<i

    todo = [0]
    done = {0}
    c=0
    gg = False
    while todo and not gg:
        c+=1
        ttodo = []
        for cur in todo:
            for x in b:
                nw = cur
                for y in x:
                    nw ^= 1<<y
                if nw not in done:
                    ttodo.append(nw)
                    done.add(nw)
                    if nw == targn:
                        gg = True
                        cc += c
                        break
                if gg:break
            if gg:break
        todo = ttodo

print(cc)
import heapq, z3
cc=0

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

for x in l:
    targ, *b, r = x
    b = [list(map(int, i[1:-1].split(","))) for i in b]
    r = tuple(map(int, r[1:-1].split(",")))

    # def minus(l, bb):
    #     l = list(l)
    #     for i in bb:
    #         l[i] -= 1
    #     return tuple(l)
    # d = {}
    # def get_min(targ):
    #     if sum(targ) == 0:
    #         return 0
    #     if targ in d:
    #         return d[targ]
    #     mn = sum(targ) + 1
    #     for x in b:
    #         rr = minus(targ, x)
    #         if all(i>=0 for i in rr):
    #             mn = min(mn, get_min(rr) + 1)
    #     d[targ] = mn
    #     return mn


    # A*
    # print(get_min(tuple(r)))
    # mx_step = max(len(i) for i in b)
    # todo = [(sum(r), (0,)*len(r))]
    # done = {todo[0][-1]}
    # best = defaultdict(lambda : float("inf"))
    # best[todo[0][-1]] = 0
    # while True:
    #     f, cur = heapq.heappop(todo)
    #     if cur == r:
    #         print(best[cur])
    #         break
    #     done.add(cur)
    #     for y in b:
    #         nw = list(cur)
    #         bad = False
    #         for j in y:
    #             nw[j]+=1
    #             if nw[j] > r[j]:
    #                 bad = True
    #         nw = tuple(nw)
    #         if not bad:
    #             if best[nw] > best[cur] + 1:
    #                 best[nw] = best[cur] + 1
    #                 # best[cur] + diff
    #                 # best[nw] + (diff - len(y))
    #                 heapq.heappush(todo, (f - (len(y)-1), tuple(nw)))


    ## primes
    # targ = 1
    # for n, i in zip(primes, r):
    #     targ *= n**i

    # bs = []
    # for j in b:
    #     n=1
    #     for k in j:
    #         n *= primes[k]
    #     bs.append(n)

    opt = z3.Optimize()
    ints = []
    for i in range(len(b)):
        ints.append(z3.Int(f"a{i}"))
        opt.add(ints[-1] >= 0)

    for i in range(len(r)):
        f = []
        for j, bb in enumerate(b):
            if i in bb:
                f.append(ints[j])
        opt.add(sum(f) == r[i])

    cost = z3.Int("cost")
    opt.add(cost == sum(ints))

    m = opt.minimize(cost)
    assert (opt.check()) == z3.sat

    cc += (opt.lower(m).as_long())
    # print(type(opt.model()[cost]))
    # break
print(cc)
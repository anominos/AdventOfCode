# flake8: noqa

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
from utils import *

DIAG_DIRS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # Clockwise from north for (i,j): l[di][dj]
ADJ_DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NESW for (i, j): l[di][dj]


numgrid = [list(".0A"), list("123"), list("456"), list("789")][::-1]
dirgrid = [list("<v>"), list(".^A")][::-1]


dirgridmap = {}
numgridmap = {}
for x in range(len(numgrid)):
    for y in range(len(numgrid[0])):
        if numgrid[x][y] == "A":
            numgridstart = (x, y)
        if numgrid[x][y] != ".":
            numgridmap[numgrid[x][y]] = (x, y)

for x in range(len(dirgrid)):
    for y in range(len(dirgrid[0])):
        if dirgrid[x][y] == "A":
            dirgridstart = (x, y)
        if dirgrid[x][y] != ".":
            dirgridmap[dirgrid[x][y]] = (x, y)


from itertools import permutations
def dist_numgrid(sx, sy, ex, ey):
    s = ""
    if ex > sx:
        s += "v"*(ex-sx)
    else:
        s += "^"*(sx-ex)
    if ey > sy:
        s += ">"*(ey-sy)
    else:
        s += "<"*(sy-ey)

    for x in permutations(s):
        if not x:
            yield x
            continue
        if sx == len(numgrid)-1 and x[:sy] == ("<",)*(sy) and sy>0:
            continue
        if sy == 0 and x[:3-sx] == ("v",)*(3-sx) and 3-sx>0:
            continue
        yield x

poss_numgrid = {}

for x in range(len(numgrid)):
    for y in range(len(numgrid[x])):
        if numgrid[x][y] != ".":
            for ex in range(len(numgrid)):
                for ey in range(len(numgrid[x])):
                    if numgrid[ex][ey] != ".":
                        poss_numgrid[x, y, ex, ey] = set(dist_numgrid(x, y, ex, ey))

def dist_dirgrid(sx, sy, ex, ey):
    s = ""
    if ex > sx:
        s += "v"*(ex-sx)
    else:
        s += "^"*(sx-ex)
    if ey > sy:
        s += ">"*(ey-sy)
    else:
        s += "<"*(sy-ey)
    for x in permutations(s):
        # if (sx, sy, ex, ey) == (1, 0, 0, 2):
        #     print(sx, sy, x[:sy], x[:1-sx], s)
        if sx == 0 and x[:sy] == ("<",)*(sy) and sy>0:
            continue
        if sy==0 and x and x[0] == "^":
            continue
        yield x

poss_dirgrid = {}

for x in range(len(dirgrid)):
    for y in range(len(dirgrid[x])):
        if dirgrid[x][y] != ".":
            for ex in range(len(dirgrid)):
                for ey in range(len(dirgrid[x])):
                    if dirgrid[ex][ey] != ".":
                        poss_dirgrid[x, y, ex, ey] = set(dist_dirgrid(x, y, ex, ey))
# print(poss_dirgrid)

# shortest_to[output, robd1, robd2, robn] = shortest_to[prev, (any_comb)]

# shortest_to = {}
# shortest_to["", "A", "A", "A"] = 0
# for x in "<>^v":
#     d =


# def backtrack(targ: str, usedir):
#     if usedir:
#         start = dirgridstart
#         grid = dirgridmap
#     else:
#         start = numgridstart
#         grid = numgridmap
#     q = deque([("", "",start)])
#     ans = []
#     while q:
#         d, sofar, (posx, posy) = q.popleft()
#         if sofar == targ:
#             ans.append(d)
#         if ans and len(d) > len(ans[0]):
#             break
#         for ch, (dx, dy) in zip("^>v<", ADJ_DIRS):
#             if (posx+dx, posy+dy) in grid:
#                 q.append((d+ch, sofar, (posx+dx, posy+dy)))

#         if targ.startswith(sofar + grid[posx, posy]):
#             q.append((d+"A", sofar+grid[posx, posy], (posx, posy)))
#         print(d)
#     return ans

# # print(backtrack("^^>A", False))
# compl = 0
# for code in l:
#     p = "A"
#     ans = ""
#     for x in code:
#         t = (poss_numgrid[numgridmap[p] + numgridmap[x]])
#         m = None
#         for ss in (t):
#             pp = "A"
#             rr = ""
#             for xx in ss + ("A",):
#                 tt = (poss_dirgrid[dirgridmap[pp] + dirgridmap[xx]])
#                 pp = xx
#                 mm = None
#                 for sss in (tt):
#                     ppp = "A"
#                     rrr = ""
#                     for xxx in sss + ("A",):
#                         ttt = (poss_dirgrid[dirgridmap[ppp] + dirgridmap[xxx]])
#                         ppp = xxx
#                         rrr += "".join(min(ttt, key=len)) + "A"

#                     if mm == None:
#                         mm = rrr
#                     mm = min(mm, rrr, key=len)

#                 rr += mm
#             if m == None:
#                 m = rr
#             m = min(m, rr, key=len)
#             # print(ss, mm)
#         p = x
#         ans += m
#     print(int(code[:-1]), len(ans))
#     compl += len(ans) * int(code[:-1])
# print(compl)

"""
A -> (ss) -> A


"""

import functools

@functools.cache
def recurse(ss: str, d):
    if d==0:
        return len(ss)+1

    pp = "A"
    rr = 0
    for xx in ss + ("A",):
        tt = (poss_dirgrid[dirgridmap[pp] + dirgridmap[xx]])
        pp = xx
        rr += min((recurse(i, d-1) for i in tt))
    return rr


compl = 0
for code in l:
    p = "A"
    ans = 0
    for x in code:
        t = (poss_numgrid[numgridmap[p] + numgridmap[x]])
        mn = float("inf")
        for s in t:
            mn = min(mn, recurse(s, 2))
        p = x
        ans += mn
    compl += ans * int(code[:-1])
print(compl)



compl = 0
for code in l:
    p = "A"
    ans = 0
    for x in code:
        t = (poss_numgrid[numgridmap[p] + numgridmap[x]])
        mn = float("inf")
        for s in t:
            mn = min(mn, recurse(s, 25))
        p = x
        ans += mn
    compl += ans * int(code[:-1])
print(compl)



"""
<v<A
<A

"""
# flake8: noqa

*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    return [*map(int, re.findall(r"-?\d+",x)),]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    l = list(f.read().strip())
    # for x in f.read().split("\n"):
    #     if x!="":
    #         l.append(func(x))

from collections import *
import dataclasses
import numpy as np
import math
from utils import *

DIAG_DIRS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # Clockwise from north for (i,j): l[di][dj]
ADJ_DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NWSE for (i, j): l[di][dj]

l = list(map(int, l))
ar = [-1] * (sum(l[::2]))
j = []
s = 0
mem = [-1] * sum(l)
for i in range(0, len(l), 2):
    block = l[i]
    for _ in range(block):
        mem[s] = i//2
        if s < len(ar):
            ar[s] = i//2
        else:
            j.append(i//2)
        s+=1
    if i+1<len(l):
        free = l[i+1]
        s += free

i = 0
for x in j[::-1]:
    while ar[i] != -1:
        i+=1
    ar[i] = x
c=0
for i, x in enumerate(ar):
    c+= i*x
print(c)

from itertools import groupby
import sys
sys.setrecursionlimit(32768)

# frees = [i for i in arr if i[0] == -1]
# blocks = [i for i in arr if i[0] != -1]
arr = [[i, sum(1 for _ in j)] for i,j in groupby(mem)]
back = len(arr)-1
while back >= 0:
    while back >= 0 and arr[back][0] == -1:
        back -= 1
    front = -1
    for x in range(min(back, len(arr))):
        if arr[x][0] == -1 and arr[x][1] >= arr[back][1]:
            front = x
            break
    if front == -1:
        back -= 1
        continue

    arr[front][1] -= arr[back][1]
    if arr[front][1] == 0:
        arr[front] = arr[back][:]
    else:
        arr.insert(front, arr[back][:])
        back += 1
        front += 1
    arr[back][0] = -1
    back -= 1
s=0
c2=0
for a, b in arr:
    for _ in range(b):
        if a!=-1:
            c2 += a*s
        s+=1
print(c2)

# arr = deque(arr)


class linkedlist:
    def __init__(self, val, nxt=None, prev=None):
        self.val = val
        self.nxt: linkedlist | None = nxt
        self.prev: linkedlist | None = prev

    def __iter__(self):
        yield self
        if self.nxt:
            yield from iter(self.nxt)

    def __str__(self):
        s = []
        for x in self:
            s.append(repr(x.val))
        return "["+",".join(s) + "]"

    @classmethod
    def from_list(cls, l: deque, prev:"linkedlist"=None):
        if not l:
            return
        nw = cls(l.popleft())
        if prev:
            prev.nxt = nw
        nw.prev = prev
        linkedlist.from_list(l, nw)
        return nw

# lst: linkedlist = linkedlist.from_list(arr)


# frees: list[linkedlist] = []
# for i in lst:
#     if i.val[0] == -1:
#         frees.append(i)
#     back = i
# while back:
#     while back and back.val[0] == -1:
#         back = back.prev

#     nextback = back.prev

#     for x in frees:
#         if x.val[1] >= back.val[1]:

#             x.val[1] -= back.val[1]
#             if x.val[1] == back.val[1]:
#                 frees.remove(x)

#             if back.prev:
#                 back.prev.nxt = back.nxt
#             if back.nxt:
#                 back.nxt.prev = back.prev

#             pprev = x.prev
#             pprev.nxt = back
#             x.prev = back
#             back.prev = pprev
#             back.nxt = x
#             break

#     back = nextback
# print(lst)

# front = None
# free_size = defaultdict(list)
# cur = front
# i=0
# while cur is not None:
#     if cur.val[0] == -1:
#         free_size[cur.val[1]].append((i, cur))
#     cur = cur.nxt

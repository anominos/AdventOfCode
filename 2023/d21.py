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
import sys
# sys.setrecursionlimit(8196)

# class Tree:
#     class TNode:
#         def __init__(self, val):
#             self.val = val
#             self.lhs = None
#             self.rhs = None
#         # def traverse_add(self, a):
#         #     print(self.val, a)
#         #     if self.val == a:
#         #         return
#         #     elif a < self.val:
#         #         if self.lhs is None:
#         #             self.lhs = Tree.TNode(a)
#         #             return
#         #         self.lhs.traverse_add(a)
#         #     elif a > self.val:
#         #         if self.rhs is None:
#         #             self.rhs = Tree.TNode(a)
#         #             return
#         #         self.rhs.traverse_add(a)
#         def __iter__(self):
#             yield self.val
#             if self.lhs is not None:
#                 for x in self.lhs:
#                     yield x
#             if self.rhs is not None:
#                 for x in self.rhs:
#                     yield x

#     def __init__(self, iter=None):
#         self.size = 0
#         self.root = None
#         if iter is not None:
#             for x in iter:
#                 self.add(x)
#     def __len__(self):
#         return self.size

#     def add(self, a):
#         if self.root == None:
#             self.root = Tree.TNode(a)
#             self.size+=1
#         else:
#             cur = self.root
#             while True:
#                 if cur.val == a:
#                     return
#                 elif a < cur.val:
#                     if cur.lhs is None:
#                         cur.lhs = Tree.TNode(a)
#                         self.size+=1
#                         return
#                     cur = cur.lhs
#                 elif a > cur.val:
#                     if cur.rhs is None:
#                         cur.rhs = Tree.TNode(a)
#                         self.size+=1
#                         return
#                     cur = cur.rhs

#     def __iter__(self):
#         return iter(self.root)

# t = Tree()
# t.add((1, 1))
# t.add((2, 1))
# t.add((1, 2))
# t.add((1, 1))
# for x in t:
#     print(x)



def adj(x, y):
    for dx in [-1, 1]:
        if 0<=x+dx<len(l):
            yield x+dx, y
    for dy in [-1, 1]:
        if 0<=y+dy<len(l[0]):
            yield x, y+dy

def adj2(x, y):
    for dx in [-1, 1]:
        # if -len(l)<=x+dx<len(l)*2:
            yield (x+dx), y
    for dy in [-1, 1]:
        # if -len(l[0])<=y+dy<len(l[0])*2:
            yield x, (y+dy)


for x in range(len(l)):
    for y in range(len(l[x])):
        if l[x][y] == "S":
            start = x, y


def do_step(visiting, adj=adj):
    nwv = set()
    for cx, cy in visiting:
        for nx, ny in adj(cx, cy):
            if l[nx%len(l)][ny%len(l[0])] != "#":
                nwv.add((nx, ny))
    return nwv

visiting = set([start])
for _ in range(64):
    visiting = do_step(visiting)

print(len(visiting))

def get_expected(h):
    q, r = divmod(h+1, 2)
    if r==0:
        return 4*q*q
    return (2*q + 1)**2


a = 65
v = set([start])
for _ in range(a):
    v = do_step(v, adj2)

r = []
for _ in range(3):
    r.append(len(v))
    for _ in range(131):
        v = do_step(v, adj2)
    # print(r)
r.append(len(v))
# print(r)

# r = [3847, 34165, 94697, 185443]
a = (r[2] +r[0] - 2*r[1])//2
c = r[0] - ((r[1] - r[0]) - a*2)
b = r[0] - a - c

def g(n):
    return a * n * n + b * n + c

tot_steps = 26501365
r = (tot_steps - 65)/131 + 1
print(g(int(r)))


#>85412341372829
#618255320926843

#618261433219147



# blocked_odd = get_expected(a) - len(v)
# blocked_even = get_expected(a+1) - len(do_step(v, adj2))



# for _ in range(66):
#     v = do_step(v)
# b = a + 66
# r = b//2
# blocked_oddo = (r * (r+1) * 2) - len(v) - blocked_odd
# blocked_eveno = (r**2 + (r+1)**2) - len(do_step(v)) - blocked_even


# print(blocked_even, blocked_odd, blocked_eveno, blocked_oddo)

# tot_steps = 26501365

# h = tot_steps // 131 + 1

# a, b = get_expected(h), get_expected(h-1)

# ans = 0
# if h%2==1:
#     ans += a * blocked_even + b * blocked_odd
# else:
#     ans += b * blocked_even + a * blocked_odd

# ans += h * (h+1) * (2* blocked_oddo)
# print(ans)


# visiting = set([start])
# dists = defaultdict(dict)
# d = 0

# while visiting:
#     d+=1
#     nw = set()
#     for x, y in visiting:
#         for nx, ny in adj2(x, y):
#             if (nx, ny) not in dists and l[nx%len(l)][ny%(len(l[0]))] != "#":
#                 dists[nx, ny] = d
#                 nw.add((nx, ny))
#     del visiting
#     visiting = nw
    # print(len(nw))

# def manhatten(x, y):
#     return abs(x[0] - y[0]) + abs(x[1] - y[1])
# import heapq
# def get_dist(start, end):
#     gscore = defaultdict(lambda: float("inf"))
#     fscore = defaultdict(lambda: float("inf"))
#     gscore[start] = 0
#     fscore[start] = manhatten(start, end)
#     openset = [(fscore[start], start)]
#     visited = set()
#     while openset:
#         while True:
#             _fscore, cur = heapq.heappop(openset)
#             # print(cur, visited)
#             if cur not in visited:
#                 break
#         # print(cur, end)
#         if cur == end:
#             return gscore[cur]
#         visited.add(cur)
#         for nei in adj2(*cur):
#             nx, ny = nei
#             if l[nx%len(l)][ny%len(l[0])] != "#":
#                 tent_g = gscore[cur] + 1
#                 if tent_g < gscore[nei]:
#                     gscore[nei] = tent_g
#                     fscore[nei] = tent_g +  manhatten(nei, end)
#                     if nei not in visited:
#                         heapq.heappush(openset, (fscore[nei], nei))


# print(get_dist(start, (len(l)*2, len(l[0]))))
# assert len(l) == len(l[0])
# corner = (0, 0)
# d_a = get_dist(start, (len(l), len(l[0])))
# prev2 = [set(), set([corner])]
# c=0
# while True:
#     cur = do_step(prev2[1])
#     if cur == prev2[0]:
#         break
#     c+=1
#     prev2 = [prev2[1], cur]


# bs = [len(visiting)]
# for _ in range(10):
#     for _ in range(131):
#         visiting = do_step(visiting, adj=adj2)
#     bs.append(len(visiting))

# step_dist = len(l) + len(l[0])

# tot_blocks, rem_steps = divmod(tot_steps - d_a, len(l))
# print(tot_blocks, rem_steps)
# quadrants = tot_blocks * (tot_blocks + 1) * (len(prev2[0]) + len(prev2[1]))  ######

# curs = [set([corner]) for corner in [
#     (0, 0),
#     (0, len(l[0])-1),
#     (len(l)-1, 0),
#     (len(l)-1, len(l[0])-1),
# ]]
# for _ in range(rem_steps):
#     for i in range(4):
#         curs[i] = do_step(curs[i])
# quadrants += (tot_blocks + 1) * sum(map(len, curs))   #######

# # print(quadrants)

# ### lines

# tot_line, rem = divmod(tot_steps, len(l))
# assert rem >= len(l)//2
# curs = [set([corner]) for corner in [
#     (start[0], 0),
#     (start[0], len(l[0])-1),
#     (0, start[1]),
#     (len(l)-1, start[1]),
# ]]
# for _ in range(rem):
#     for i in range(4):
#         curs[i] = do_step(curs[i])

# # double count middle one, and remove later

# if start in prev2[0]:
#     r = len(prev2[1])
# else:
#     r = len(prev2[0])




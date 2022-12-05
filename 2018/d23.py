import re
import networkx
from itertools import combinations

l = []
with open("d23in.txt") as f:
    for x in f.readlines():
        a,b,c,d = re.findall(r"-?\d+", x)
        l.append([*map(int, [a,b,c,d])])

m = max(l, key=lambda a:a[-1])
c=0

def dist(x,y):
    return sum(map(lambda a,b: abs(a-b), x[:-1], y[:-1]))

def mid(x, y):
    return (*map(lambda a: a/2, map(int.__add__, x[:-1], y[:-1])),)

for x in range(len(l)):
    if dist(l[x], m) <= m[-1]:
        c+=1
print(c)

edges = [set() for i in range(len(l))]
degrees = [0 for _ in range(len(l))]
intersections = []
for x in range(len(l)):
    for y in range(x+1, len(l)):
        if not (dist(l[x], l[y]) <= l[x][-1]+l[y][-1]):
            edges[x].add(y)
            edges[y].add(x)
            degrees[x] += 1
            degrees[y] += 1

# remove the least number of nodes such that there are 0 edges left
# greedily remove edge with largest degree on every iteration

def max_index(l):
    mx,i = -1,0
    for x in range(len(l)):
        if l[x] > mx:
            mx = l[x]
            i = x
    return i

while max(degrees) > 0:
    i = max_index(degrees)
    for y in edges[i]:
        degrees[y] -= 1
        edges[y].remove(i)
    edges[i] = []
    degrees[i] = -1

a = []
for x in range(len(degrees)):
    if degrees[x] != -1:
        a.append(x)

mn = (99999999999,)
for x in range(len(a)):
    for y in range(x+1, len(a)):
        if l[x][-1] + l[y][-1] - dist(l[x], l[y]) >= 0:
            mn = min((l[x][-1] + l[y][-1] - dist(l[x], l[y]),l[x],l[y]), mn)
assert mn[0] == 0
_, a, b = mn
print(a,b)


"""

  #
 ###
##x##
 ###
  ##
  #x#
   #


"""

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
    return (*map(lambda a: a/2, map(int.__add__, x, y)),)

for x in range(len(l)):
    if dist(l[x], m) <= m[-1]:
        c+=1
print(c)

edges = [set() for i in range(len(l))]
intersections = []
for x in range(len(l)):
    for y in range(x+1, len(l)):
        if not (dist(l[x], l[y]) <= l[x][-1]+l[y][-1]):
            edges[x].add(y)

# remove the least number of nodes such that there are 0 edges left

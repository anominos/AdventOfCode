dat = []
with open("d13in.txt") as f:
    for x in f.read().split("\n\n"):
        dat.append(x)
points, folds = dat
from collections import defaultdict
import re

g = set()
for x in points.splitlines():
    a,b = x.split(",")
    g.add((int(a),int(b)))
folds = folds.splitlines()
for f in folds:
    d,n = re.search("([xy])=(\d+)",f).groups()
    n = int(n)
    cpy = set()
    for x,y in g:
        if d=="x":
            if n<x:
                cpy.add((2*n-x, y))
            else:
                cpy.add((x,y))
        else:
            if y>n:
                cpy.add((x,2*n-y))
            else:
                cpy.add((x,y))
    if f==folds[0]:print(len(cpy))
    g = cpy

a = [[None]*100 for _ in range(100)]
for x in g:
    a[x[1]][x[0]] = "#"

for x in a:
    if any(x):
        for y in x:
            if y==None:
                print(end=" ")
            else:
                print(end=y)
        print()
#ARHZPCUH
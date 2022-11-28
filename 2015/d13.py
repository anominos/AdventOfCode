import re
dat = []
with open("d13in.txt") as f:
    for x in f.read().strip().split("\n"):
        dat.append(re.findall(r"(-?\d+|[A-Z])", x.replace("lose ", "-")))
names = list(set([i[0] for i in dat]))

mat = [[float("inf")]*len(names) for _ in range(len(names))]

for x in dat:
    mat[names.index(x[0])][names.index(x[2])] = int(x[1])
from itertools import permutations
mx = 0
mx2 = 0
for i in permutations(range(len(names)), len(names)):
    c=0
    for x in range(len(i)):
        if x == len(i)-1:
            mx2 = max(c, mx2)
        c+=mat[i[x]][i[(x+1)%len(i)]]
        c+=mat[i[(x+1)%len(i)]][i[x]]
    mx = max(c, mx)
print(mx)
print(mx2)
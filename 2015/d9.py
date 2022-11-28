from collections import defaultdict
d = defaultdict(dict)
with open("d9in.txt") as f:
    for x in f:
        a, _, c, _, e = x.split()
        d[a][c]=int(e)
        d[c][a] = int(e)

from itertools import permutations as perm
mn = float("inf")
mx=0
for x in perm(d.keys(), len(d)):
    dis = 0
    for y in range(len(x)-1):
        dis+= d[x[y]][x[y+1]]
    mn = min(dis, mn)
    mx = max(dis, mx)
print(mn)
print(mx)
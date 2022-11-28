import re
from copy import deepcopy
pos = {}
lookup = {}
c=0
with open("d10in.txt") as f:
    for x in f:
        x, y, dx, dy = map(int, re.findall("-?\d+", x.strip()))
        c+=1
        lookup[c] = (dx, dy)
        pos[c] = [x, y]
prev = [float("inf")]*2
c=0
while True:
    c+=1
    for i, j in pos.items():
        for k in [0,1]:
            pos[i][k] += lookup[i][k]
    az, bz = min(pos.values())[0], max(pos.values())[0]
    if prev[0] > az and prev[1] < bz:
        break
    prev = (az, bz, list(map(list,pos.values())))
coords = prev[-1]
maxx = max(coords)[0]
maxy = max(coords, key=lambda a:a[1])[1]
minx = min(coords)[0]
miny = min(coords, key=lambda a:a[1])[1]
l = [[" "]*(maxx-minx+1) for _ in range(maxy-miny+1)]
for x,y in coords:
    l[y-miny][x-minx] = "#"
print("\n".join(map("".join, filter(lambda a:len(set(a))!=1, l))))
print(c-1)
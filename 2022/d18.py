*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []
import re
def func(x):
    return [*map(int, re.findall(r"-?\d+",x)),]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

overlap=0
for i in range(len(l)):
    for j in range(len(l)):
        if sum([abs(a-b)for a,b in zip(l[i],l[j])])==1:
            overlap+=1
w = (len(l)*6-overlap)
print(w)
n=[]
l = set(map(tuple, l))
processing = set()
done = {}
import sys
sys.setrecursionlimit(1_000_000)

ds = []
for d in [-1, 1]:
    ds.extend([[0,0,d],[0,d,0],[d,0,0]])
def floodfill(x,y,z, i):
    if not(-1<=x<=20 and -1<=y<=20 and -1<=z<=20):
        return
    if (x,y,z) in l:
        return
    if grid[x][y][z] != 0:
        return
    grid[x][y][z] = i
    for dx,dy,dz in ds:
        floodfill(x+dx, y+dy, z+dz, i)

grid = [[[0]*22 for _ in range(22)] for _ in range(22)]
floodfill(-1,-1,-1, 1)
for x in range(-1, 21):
    for y in range(-1, 21):
        for z in range(-1, 21):
            if grid[x][y][z] == 0 and (x,y,z) not in l:
                n.append((x,y,z))

overlap=0
for i in range(len(n)):
    for j in range(len(n)):
        if sum([abs(a-b)for a,b in zip(n[i],n[j])])==1:
            overlap+=1


r = (len(n)*6-overlap)
print(w-r)

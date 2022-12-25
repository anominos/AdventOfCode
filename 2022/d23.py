*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))


dirs = [
 [[-1, -1], [0, -1], [1, -1]],
 [[1, 1], [0, 1], [-1, 1]],
 [[-1, 1], [-1, 0], [-1, -1]],
 [[1, 1], [1, 0], [1, -1]],
]
elves = []
for y, p in enumerate(l):
    for x, q in enumerate(p):
        if q == "#":
            elves.append((x, y))

def printg(lst):
    last = lambda a: a[1]
    a,b,c,d = min(lst)[0], min(lst, key=last)[1], max(lst)[0], max(lst, key=last)[1]
    gr = [["."]*(c-a+1) for _ in range(d-b+1)]
    for x,y in lst:
        gr[y-b][x-a] = "#"
    for x in gr:
        print("".join(x))
    print()

from collections import Counter

for rd in range(100_000):
    # printg(elves)
    nw = []
    s = set(elves)
    c = Counter()
    change = False
    for ex, ey in elves:
        haself = False
        nx, ny = None, None
        for i in dirs:
            chaself = False
            for dx, dy in i:
                if (ex+dx, ey+dy) in s:
                    chaself = True
            if not chaself:
                if (nx,ny) == (None, None):
                    nx,ny = ex+i[1][0], ey+i[1][1]
            if chaself:
                haself=True
        if haself and nx is not None:
            nw.append((nx, ny))
        else:
            nw.append((ex, ey))
        c[nw[-1]] += 1
    for i in range(len(nw)):
        if c[nw[i]] == 1:
            if elves[i] != nw[i]:
                change=True
                elves[i] = nw[i]
    if not change:
        print(rd+1)
        break
    dirs = dirs[1:] + [dirs[0]]
    if rd==9:
        last = lambda a: a[1]
        a,b,c,d = min(elves)[0], min(elves, key=last)[1], max(elves)[0], max(elves, key=last)[1]
        print((d-b+1)*(c-a+1) - len(elves))
        # printg(elves)
# printg(elves)

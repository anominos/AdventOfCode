*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []
import re
def func(x):
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

def get_rocks():
    while True:
        yield [(i, 0) for i in range(4)]
        yield [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)]
        yield [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
        yield [(0, i) for i in range(4)]
        yield [(0, 0), (0, 1), (1, 0), (1, 1)]
from itertools import cycle

def fmt(x):
    gr = [["."]*7 for _ in range(2+max(x, key=lambda a:a[1])[1])]
    for (i, j) in x:
        if j>=0:
            gr[j][i] = "#"
    for x in gr[::-1]:
        print("".join(x))
    print()
seen = []
zz=0
r = 1000000000000
mul, output = divmod(r,(len(l[0])*5))
pushes: list[str] = cycle(l[0])
chamber = set([(i, -1) for i in range(7)])
y = 0
py=0
n=0
ll = get_rocks()
xx=0
ys = []
offset=0
for cr in ll:
    cur_rock = {(i+2, y+3+j) for (i,j) in cr}
    while len(cur_rock & chamber) == 0:
        cur_push = next(pushes)
        if cur_push == ">":
            if max(cur_rock)[0] < 6:
                nr = {(i+1, j) for (i,j) in cur_rock}
                if not nr&chamber:
                    cur_rock = nr
        else:
            if min(cur_rock)[0] > 0:
                nr = {(i-1, j) for (i,j) in cur_rock}
                if not nr&chamber:
                    cur_rock = nr
        xx+=1
        cur_rock = {(i, j-1) for (i,j) in cur_rock}
    cur_rock = {(i, j+1) for (i,j) in cur_rock}
    y = max(y, max(cur_rock, key=lambda a: a[1])[1]+1)
    chamber |= cur_rock
    n+=1
    if n==2022:
        print(y)
    if n==60_000:
        break
    ys.append(y)
    seen.append((n%5, xx%len(l[0]), [i for i in range(7) if (i, y-1) in chamber]))

    if len(seen[-1][-1]) == 7 and y<30000:
        spl = n-offset
        offset=n

diff = ys[offset+spl] - ys[offset]
assert diff == ys[offset+spl+spl] - ys[offset+spl]
mul, mod = divmod(r-offset, spl)
print(mul*diff + ys[offset+mod-1])

# fmt(chamber)
# not 1540634005752
"""

.......
.......
.......
.##....
.##....
..#....
..#....
..##.#.
..#####
.###.#.
..####.
..##...
..##...
...#...
...#...
...#..#
...#..#
...####
..###..
...#...
.####..
....##.
....##.
"""

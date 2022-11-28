import re
from collections import defaultdict
import sys
from time import sleep
sys.setrecursionlimit(16_556)
d = defaultdict(int)
with open("d17in.txt") as f:
#     f = """x=495, y=2..7
# y=7, x=495..501
# x=501, y=3..7
# x=498, y=3..4
# x=506, y=1..2
# x=498, y=10..13
# x=504, y=10..13
# y=3, x=502..506
# y=9, x=494..498
# y=13, x=498..504""".split("\n")
    for n in f:
        x = re.search("x=([0-9\.]+)", n).group(1)
        y = re.search("y=([0-9\.]+)", n).group(1)
        x = x.split("..")
        y = y.split("..")
        if len(x)==1:
            x.append(x[0])
        if len(y)==1:
            y.append(y[0])
        for i in range(int(x[0]), int(x[1])+1):
            for j in range(int(y[0]), int(y[1])+1):
                d[(i, j)] = 2
maxy = max(d.keys(), key=lambda a:a[1])[1]
miny = min(d.keys(), key=lambda a:a[1])[1]

curx, cury = 500,0
c=0

def draw(grid, pos):
    print(pos)
    grid = [["."]*(45) for _ in range(15)]
    d2  = {0:".", 1:"|", 2:"#", 3:"~"}
    for x in range(-22,23):
        for y in range(-7,8):
            grid[y+7][x+22] = d2[d[(x+pos[0], y+pos[1])]]
    for x in grid:
        print("".join(x))
    input()
    # sleep(0.05)

def doLevel(posx, posy):
    # draw(d, (posx, posy))
    left = 0
    while True:
        if d[(posx-left, posy+1)] in [0,1]:
            d[(posx-left, posy)] = 1
            doVertical(posx-left, posy+1)
            leftWall = False
            break
        if d[(posx-left, posy)] in [2,3]:
            leftWall = True
            break
        d[(posx-left, posy)] = 1
        left+=1

    right = 1
    while True:
        if d[(posx+right, posy+1)]in [0,1]:
            d[(posx+right, posy)] = 1
            doVertical(posx+right, posy+1)
            rightWall = False
            break
        if d[(posx+right, posy)] in [2,3]:
            rightWall = True
            break
        d[(posx+right, posy)] = 1
        right+=1
    if leftWall and rightWall:
        for index in range(posx-left+1, posx+right):
            d[(index, posy)] = 3
        doLevel(posx, posy-1)
    return True
def doVertical(posx, posy):
    # draw(d, (posx, posy))
    while True:
        if posy > maxy or d[(posx, posy)]==1:
            return
        d[(posx, posy)] = 1
        down = (posx, posy+1)
        if d[down] != 0 and d[down]!=1:
            if doLevel(posx, posy):
                return 
        posy+=1




doVertical(curx, cury)
# draw(d, (500, 5))
c=0
c2 = 0
for x, y in d.items():
    if miny<=x[1]<=maxy:
        c+= y in [1, 3]
        c2+=y == 3
print(c)
print(c2)
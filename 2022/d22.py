*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

grid: list[str] = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    a,b = f.read().split("\n\n")
    for x in a.split("\n"):
        grid.append(func(x))

row_wrap = []
column_wrap = [[5000, -5000] for _ in range(len(grid[0]))]
for x in grid:
    try:
        w = x.rindex(" ")
    except ValueError:
        w = -1
    row_wrap.append((w, len(x)))

for y in range(len(grid)):
    for x in range(len(grid[y])):
        try:
            if grid[y][x] in ".#":
                column_wrap[x][0] = min(column_wrap[x][0], y-1)
                column_wrap[x][1] = max(column_wrap[x][1], y+1)
        except:pass

def next1(cx, cy, dx, dy):
    if dy != 0:
        if row_wrap[cx][0] == cy+dy:
            nx, ny = cx, row_wrap[cx][1]-1
        elif row_wrap[cx][1] == cy+dy:
            nx, ny = cx, row_wrap[cx][0]+1
        else:
            nx, ny = cx, cy+dy
        if grid[nx][ny] == ".":
            cx = nx
            cy = ny
    if dx != 0:
        if column_wrap[cy][0] == cx+dx:
            nx, ny = column_wrap[cy][1]-1, cy
        elif column_wrap[cy][1] == cx+dx:
            nx, ny = column_wrap[cy][0]+1, cy
        else:
            nx, ny = cx+dx, cy
        if grid[nx][ny] == ".":
            cx = nx
            cy = ny
    return cx, cy, dx, dy


show = []
def do(next, log=False, f=None):
    if log:
        s = [[" "]*150 for _ in range(200)]
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                s[y][x] = grid[y][x]
    cx, cy = 0, 50

    dx, dy = 0, 1
    i = 0

    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    while i<len(b):
        nxt = 10000
        try:
            nxt = b.index("R", i)
        except ValueError:
            pass
        try:
            nxt = min(nxt, b.index("L", i))
        except ValueError:
            nxt = len(b)
        # print(b, i, nxt)
        n = int(b[i:nxt])
        for _ in range(n):
            # print(cx, cy)
            if log:
                s[cx][cy] = "m"
            cx, cy, dx, dy = next(cx, cy, dx, dy)
            if log:
                s[cx][cy] = ">v<^"[dirs.index([dx,dy])]
                showstuff(s)
        try:
            if b[nxt] == "R":
                dx, dy = dirs[(dirs.index([dx,dy])+1)%4]
            else:
                dx, dy = dirs[(dirs.index([dx,dy])-1)%4]
        except:
            break
        i = nxt+1
        if f is not None:
            print(cx, cy, file=f)
    print((cx+1)*1000 + (cy+1)*4 + dirs.index([dx,dy]))


def next2(cx, cy, dx, dy):
    if cx+dx >= 0 and cy+dy >= 0:
        try:
            if grid[cx+dx][cy+dy]==".":
                return (cx+dx, cy+dy, dx, dy)
            elif grid[cx+dx][cy+dy] == "#":
                return cx,cy,dx,dy
        except IndexError:
            pass
    if dx == 1:
        if 0<=cy<50:
            ret =  0, cy+100, dx, dy
        elif 50<=cy<100:
            ret =  cy+100, 49, 0, -1
        elif 100<=cy<150:
            ret =  cy-50, 99, 0, -1
    if dx == -1:
        if 0<=cy<50:
            ret =  cy+50, 50, 0, 1
        elif 50<=cy<100:
            ret =  cy+100, 0, 0, 1
        elif 100<=cy<150:
            ret =  199, cy-100, dx, dy
    if dy==1:
        if 0<=cx<50:
            ret =  149-cx, 99, -dx, -dy
        elif 50<=cx<100:
            ret =  49, cx+50, -1, 0
        elif 100<=cx<150:
            ret =  149-cx, 149, -dx, -dy
        elif 150<=cx<200:
            ret =  149, cx-100, -1, 0
    if dy == -1:
        if 0<=cx<50:
            ret =  149-cx, 0, -dx, -dy
        elif 50<=cx<100:
            ret =  100, cx-50, 1,0
        elif 100<=cx<150:
            ret =  149-cx, 50, -dx, -dy
        elif 150<=cx<200:
            ret =  0, cx-100, 1, 0

    if grid[ret[0]][ret[1]] == "#":
        return cx, cy, dx, dy
    return ret



def showstuff(l):
    import matplotlib.pyplot as plt
    each = [i.copy() for i in l]
    for y in range(len(each)):
        for x in range(len(each[y])):
            if each[y][x] == "." or each[y][x] == " ":
                each[y][x] = [255,255,255]
            elif each[y][x] == "#":
                each[y][x] = [0, 0, 0]
            elif each[y][x] == "m":
                each[y][x] = [255, 0, 0]
            else:
                each[y][x] = [0, 255, 0]
    plt.imshow(each, interpolation="nearest")
    plt.pause(0.1)


do(next1)
with open("debug2", "w") as f:
    do(next2, f=f)

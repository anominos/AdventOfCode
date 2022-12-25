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

bz = set()
chars = "^v><"
d = "NSEW"
dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

mapp = dict(zip(chars, d))
map2 = dict(zip(d, dirs))
for x in range(len(l)):
    for y in range(len(l[x])):
        if l[x][y] in mapp:
            bz.add((x, y, mapp[l[x][y]]))

states = {(0, 1, "")}
c=0
r = True
goal =  (len(l)-1, len(l[0])-2)
goals = [goal, (0, 1), goal]
while True:
    # step bz
    nbz = set()
    for x,y,q in bz:
        dx,dy = map2[q]
        nx, ny = x+dx, y+dy
        if nx == 0:
            nx = len(l)-2
        if nx == len(l)-1:
            nx = 1
        if ny == 0:
            ny = len(l[0])-2
        if ny == len(l[0])-1:
            ny = 1

        nbz.add((nx, ny, q))
    bz = nbz

    nw = set()
    for curx,cury,curp in states:
        for dx,dy in dirs + [[0,0]]:
            if 0<curx+dx<len(l)-1 and 0<cury+dy<len(l[0])-1:
                if not any((curx+dx, cury+dy, w) in bz for w in d):
                    nw.add((curx+dx, cury+dy, curp))
            if (curx+dx, cury+dy) == goal and r:
                print(c+1)
                r = False
                goal = (0, 1)
            if (curx+dx, cury+dy) == goals[len(curp)]:
                nw.add((curx+dx, cury+dy, curp+"1"))
                if len(curp) == 2:
                    print(c+1)
                    exit()
    states = nw
    c+=1

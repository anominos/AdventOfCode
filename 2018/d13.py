import sys
from copy import deepcopy

def printGrid(grid, carts):
    debug = deepcopy(grid)
    for y in range(len(debug)):
        for x in range(len(debug[y])):
            if debug[y][x] in "<>":
                debug[y][x] = "-"
            if debug[y][x] in "^v":
                debug[y][x] = "|" 
    for x in carts:
        debug[x[0]][x[1]] = "^<v>"[dirs.index(x[-1])]
    for x in debug:
        print("".join(x))

grid = []
with open("d13in.txt") as f:
    for x in f:
        grid.append(list(x.strip("\n")))

## cart: (x, y, nxtTurn, dir)
dirs = [[0,-1], [-1,0],[0,1],[1,0]]
carts = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] in "^v<>":
            carts.append([y, x, 1, dirs["^<v>".index(grid[y][x])]])

p1 = True
carts.sort()

while len(carts)>1:
    i=0
    while i < len(carts):
        car = carts[i]
        dx, dy = car[-1]
        car[1]+=dx
        car[0]+=dy
        if (nxt:=grid[car[0]][car[1]]) == "/":
            car[-1] = [-i for i in car[-1][::-1]]
        elif nxt=="\\":
            car[-1] = car[-1][::-1]
        elif nxt == "+":
            car[-1] = dirs[(dirs.index(car[-1])+car[2])%4]
            car[2] -=1
            if car[2] < -1:
                car[2] = 1
        for n in range(len(carts)):
            x = carts[n]
            if car[:2] == x[:2] and id(car)!=id(x):
                ##COLLISION
                if p1:
                    print(*car[:2][::-1])
                    p1=False
                carts.remove(car)
                carts.remove(x)
                i-=1
                if n <= i:
                    i-=1
                break
        i+=1
        #printGrid(grid, carts)

    carts.sort()
print(*carts[0][:2][::-1])
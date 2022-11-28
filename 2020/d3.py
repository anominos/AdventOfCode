import sys
with open("d3in.txt")as f:
    dat = []
    for x in f:
        dat.append((x.strip()))

grid = []
for x in dat:
    grid.append([])
    for y in x:
        grid[-1].append(y=="#")

mul=1
for dx in [1,3,5,7,10]:
    pos=0
    dy=1
    if dx==10:
        dx=1
        dy=2
    tree = 0
    print(dy, dx)
    for y in range(0,len(grid),dy):
        if grid[y][pos%len(grid[y])]:
            print(end="#")
        else:
            print(end=".")
        tree+=grid[y][pos%len(grid[y])]
        pos+=dx
    mul*=tree
    # if dx==3 and dy==1:
    #     print(tree)
print(mul)
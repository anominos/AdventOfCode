instruc  =[]
with open("d08in.txt","r") as f:
    for x in f:
        instruc.append(x.strip())
import re,time,os
h = 6
grid = [[False for i in range(50)]for _ in range(h)]
for x in instruc:
    x = x.split()
    if x[0]=="rect":
        a, b = map(int,x[1].split("x"))
        for i in range(b):
            for j in range(a):
                grid[i][j]=True
    else:
        a = int(x[2][2:])
        b = int(x[-1])
        if x[1]=="row":
            grid[a] = grid[a][-b:]+grid[a][:-b]
        else:
            col= []
            for y in range(h):
                col.append(grid[y][a])
            col = col[-b:]+col[:-b]
            for y in range(h):
                grid[y][a] = col[y]
    #os.system("cls")
    #for x in grid:
    #    print("".join("#" if i else " " for i in x))

print("silver:",sum(sum(grid,[])))
print("gold:")
for x in grid:
    print("".join("#" if i else " " for i in x))

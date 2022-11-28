with open("d18in.txt") as f:
    dat = []
    for x in f.read().split("\n"):
        dat.append([i=="#" for i in x])

# grid = """.#.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####..""".splitlines()
# grid = [list(map(lambda a:a=="#", i)) for i in grid]

def getAdj(x,y):
    c=0
    for dx in range(-1,2):
        for dy in range(-1,2):
            if not dx==dy==0:
                if 0<=x+dx<len(grid) and 0<=y+dy<len(grid):
                    c+=grid[x+dx][y+dy]
    return c


for c in range(2):
    grid = [list(i) for i in dat]
    for _ in range(100):
        if c==1:
            grid[0][0] = True
            grid[0][-1] = True
            grid[-1][0] = True
            grid[-1][-1]=True
        ng = []
        for y in range(len(grid)):
            ng.append([])
            for x in range(len(grid[y])):
                a = getAdj(x,y)
                ng[-1].append((grid[x][y] and a==2) or a==3)
        grid = [list(i) for i in ng]
    if c==1:
        grid[0][0] = True
        grid[0][-1] = True
        grid[-1][0] = True
        grid[-1][-1]=True
    print(sum(map(sum, grid)))
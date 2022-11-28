grid = []
with open("d19in.txt") as f:
    for x in f:
        grid.append(x.replace("\n", ""))

dr = [0,1]
start = [grid[0].index("|"), 0]
l=""
c=0
while 0<=start[0]<len(grid[0]) and 0<=start[1]<len(grid):
    if not (y:=grid[start[1]][start[0]]) in "|-+ ":
        l+=y
    new = start[:]
    new[0]+=dr[0]
    new[1]+=dr[1]
    if not 0<=new[0]<len(grid[0]) or not 0<=new[1]<len(grid) or grid[new[1]][new[0]]== " ":
        dr = dr[::-1]
        new = start[:]
        new[0]+=dr[0]
        new[1]+=dr[1]
        if not 0<=new[0]<len(grid[0]) or not 0<=new[1]<len(grid) or grid[new[1]][new[0]]== " ":
            dr = list(map(lambda a:-a, dr))
            new = start[:]
            new[0]+=dr[0]
            new[1]+=dr[1]
            if not 0<=new[0]<len(grid[0]) or not 0<=new[1]<len(grid) or grid[new[1]][new[0]]== " ":
                break
    start = new[:]
    c+=1
print(l)
print(c+1)

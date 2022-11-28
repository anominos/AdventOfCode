from collections import defaultdict
gsn = 6548
grid = []
for y in range(1,301):
    grid.append([])
    for x in range(1,301):
        rid = x+10
        power = rid*y
        power += gsn
        power*=rid
        power = (power//100)%10
        power-=5
        grid[-1].append(power)

ps = defaultdict(int)
for y in range(300):
    for x in range(300):
        ps[x, y] = grid[y][x] + ps[x-1, y] + ps[x, y-1] - ps[x-1, y-1]

mx = [0,0,0]
for size in range(1,300):
    for y in range(size-1, 300):
        for x in range(size-1, 300):
            score = ps[x, y]-ps[x-size, y]-ps[x, y-size]+ps[x-size,y-size]
            mx = max(mx, [score,x+2-size, y+2-size, size] )
    if size==3:
        print(*mx[1:3],sep=",")
print(*mx[1:],sep=",")
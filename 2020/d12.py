dat = []
with open("d12in.txt") as f:
    for x in f:
        dat.append((x.strip()))

adj = [[0,1],[1,0],[0,-1],[-1,0]]

x, y = 0,0
facing = 1
for l in dat:
    if l[0]  in "NESW":
        dx, dy = adj["NESW".index(l[0])]
        x+=dx*int(l[1:])
        y+=dy*int(l[1:])
    if l[0] == "R":
        facing += int(l[1:])//90
        facing %=4
    if l[0]=="L":
        facing -= int(l[1:])//90
        facing %=4
    if l[0]=="F":
        dx, dy = adj[facing]
        x+=dx*int(l[1:])
        y+=dy*int(l[1:])
print(sum(map(abs, [x,y])))


x, y = 10,1
sx, sy = 0,0
for l in dat:
    if l[0]  in "NESW":
        dx, dy = adj["NESW".index(l[0])]
        x+=dx*int(l[1:])
        y+=dy*int(l[1:])
    if l[0] == "R":
        for _ in range(int(l[1:])//90):
            x, y = y,-x
    if l[0]=="L":
        for _ in range(int(l[1:])//90):
            x, y= -y, x
        
    if l[0]=="F":
        sx+=x*int(l[1:])
        sy+=y*int(l[1:])
    # print(x, y, sx, sy)
print(abs(sx)+abs(sy))
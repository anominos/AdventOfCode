f = open("d22in.txt")
f = f.readlines()
f = f[2:]
##f = """/dev/grid/node-x0-y0   10T    8T     2T   80%
##/dev/grid/node-x0-y1   11T    6T     5T   54%
##/dev/grid/node-x0-y2   32T   28T     4T   87%
##/dev/grid/node-x1-y0    9T    7T     2T   77%
##/dev/grid/node-x1-y1    8T    0T     8T    0%
##/dev/grid/node-x1-y2   11T    7T     4T   63%
##/dev/grid/node-x2-y0   10T    6T     4T   60%
##/dev/grid/node-x2-y1    9T    8T     1T   88%
##/dev/grid/node-x2-y2    9T    6T     3T   66%""".split("\n")
dat = {}
for x in f:
    s = (x.strip().replace("T", "").replace("%", "").replace("/dev/grid/node-x", "").split())
    dat[tuple(map(int,s[0].split("-y")))] = list(map(int,s[1:]))
maxx = max(dat.keys())[0]
maxy = max(dat.keys())[1]

c=0
for x in range(maxx+1):
    for y in range(maxy+1):
        A = dat[(x, y)]
        if A[1]==0:
            continue
        for a in range(maxx+1):
            for b in range(maxy+1):
                if a==x and b==y:
                    continue
                B = dat[(a, b)]
                if A[1] <= B[2]:
                    c+=1
print(c)
boundl, boundh = 50, 100
#boundl, boundh = 5, 15
grid = ""
for y in range(maxy+1):
    for x in range(maxx+1):
        used = dat[(x, y)][1]
        if used ==0:
            grid+="_"
            startx, starty = x, y
        elif 50<used<100:
            grid+="."
        else:
            grid+="#"
    grid+="\n"


adj = [[0,1],[1,0],[-1,0],[0,-1]]
todo = {(startx, starty)}
done = set()
c=0
while True:
    new = []
    for x in todo:
        if x==(maxx, 0):
            break
        done.add(x)
        for y in adj:
            if 0<=x[0]+y[0] <= maxx and 0<=x[1]+y[1] <= maxy and boundl<dat[(x[0]+y[0],x[1]+y[1])][1]<boundh and not (x[0]+y[0],x[1]+y[1]) in done:
                new.append((x[0]+y[0],x[1]+y[1]))
    else:
        todo = set(new)
        c+=1
        continue
    break
print(c+(5*(maxx-1)))
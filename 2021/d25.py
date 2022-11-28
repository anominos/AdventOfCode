dat = []
with open("d25in.txt") as f:
    for x in f:
        dat.append((x.strip()))


d = dict(zip(">v.", range(3)))
coords = dict()
cur = ">"
c=0
change = {">":[0,1], "v":[1,0]}
r = {}
X,Y = len(dat),len(dat[0])
for x in range(X):
    for y in range(Y):
        r[x,y] = dat[x][y]
dat = r
pg = True
g = True

def printGrid():
    s = ""
    print(c)
    for x in range(X):
        for y in range(Y):
            s+= dat[x,y]
        s+="\n"
    print(s)

while True:
    pg = g
    g=False
    nw = dict()
    for x in range(X):
        for y in range(Y):
            if dat[x,y] == cur:
                dx, dy = change[cur]
                if dat[(x+dx)%X, (y+dy)%Y]==".":
                    nw[(x+dx)%X, (y+dy)%Y] = cur
                    nw[x,y]="."
                    g=True
            if not ((x,y) in nw):
                nw[x,y] = dat[x,y]
    dat = nw.copy()
    if cur==">":
        cur = "v"
    else:
        c+=1
        cur = ">"
        if not(pg or g):break
        # printGrid()
print(c)
n= 312051
c=1
while c**2 < n:
    c+=2
d = c**2
while d > c:
    d-=n
print("silver:",abs(c//2 - d) + c//2)
from collections import deque
posx, posy = 0,0
d = [[1,0],[0,1],[-1,0],[0,-1]]
i = 0
r = deque([deque([0,0,0]), deque([0,1,0]), deque([0,0,0])])
g=4

def getsum(grid, x, y):
    c=0
    l = len(grid)//2
    for dx in range(-1,2):
        for dy in range(-1,2):
            if not(x==y==0):
                if -l <= x+dx <= l and -l <= y+dy <= l:
                    c+= grid[y+dy+l][x+dx+l]
    return c
while True:
    curd = d[i]
    posx += curd[0]
    posy += curd[1]
    nxt = d[(i+1)%4]
    if r[posy+nxt[1]+len(r)//2][posx+nxt[0]+len(r)//2]==0:
        i+=1
        i%=4
        g-=1
        if g==0:
            r.appendleft(deque([0]*len(r[0])))
            r.append(deque([0]*len(r[0])))
            for x in r:
                x.append(0)
                x.appendleft(0)
            g=4
    a = getsum(r, posx, posy)
    r[posy+len(r)//2][posx+len(r)//2]=a
    if a>n:
        break

print("gold:",a)

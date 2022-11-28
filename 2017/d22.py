d = {}
with open("d22in.txt") as f:
    '''f = """..#
#..
...""".split("\n")'''
    x=0
    for n in f:
        for y in range(len(n.strip())):
            d[(x,y)] = n[y]=="#"
        x+=1
x-=1
cur = (x//2, y//2)
def p1(cur, d):
    dr = [[1,0],[0,1],[-1,0],[0,-1]] # left to right = anticlockwise
    dc = 2
    c=0
    for _ in range(10000):
        if d.get(cur, False):
            dc-=1
        else:
            dc+=1
            c+=1
        dc%=len(dr)
        d[cur] = not(d.get(cur, False))
        cur = (cur[0]+dr[dc][0], cur[1]+dr[dc][1])
    print(c)
p1(cur[:], d.copy())

def p2(cur, d):
    for x, y in d.items():
        if d[x]:
            d[x] = 2
        else:
            d[x]=0
    dr = [[1,0],[0,1],[-1,0],[0,-1]] # left to right = anticlockwise
    dc = 2
    c=0
    for _ in range(10_000_000):
        if _%100000==0:
            print(_)
        if (y:=d.get(cur,0))==2:
            dc-=1
        elif y==0:
            dc+=1
        elif y==3:
            dc+=2
        else:
            c+=1
        dc%=len(dr)
        d[cur] = (y+1)%4
        cur = (cur[0]+dr[dc][0], cur[1]+dr[dc][1])
    print(c)
p2(cur, d)
*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []
import re
def func(x):
    return [*map(int, re.findall(r"-?\d+",x)),]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

def dist(a,b,c,d):
    return abs(c-a) + abs(b-d)

r = 2_000_000
s = set()
q = set()
for a,b,c,d in l:
    if d==r:
        q.add(c)
    if abs(r-b) <= dist(a,b,c,d):
        sidew = dist(a,b,c,d) - abs(r-b)
        for i in range(a - sidew, a+sidew+1):
            s.add(i)
print(len(s-q))
ww = 4_000_000
def check(sx, sy):
    if not(0<=sx<=ww and 0<=sy<=ww):
        return
    for a,b,c,d in l:
        if dist(a,b,c,d) >= dist(a,b,sx,sy):
            return
    print(sx*ww+sy)
    exit()

def do(i,j):
    d1 = dist(*l[i])
    d2 = dist(*l[j])
    a,b,*_ = l[i]
    c,d,*_ = l[j]
    for dx,dy in [[1,1],[1,-1],[-1,-1],[-1,1]]:
        sx, sy = a + (d1+1)*-dx, b
        check(sx, sy)
        while sx != a:
            # break
            if sx > ww:
                sy += dy*(sx-ww)
                sx = ww
            sx+=dx
            sy+=dy
            check(sx, sy)


for i in range(len(l)):
    (a,b,c,d) = l[i]
    d1 = dist(a,b,c,d)
    for j in range(i+1, len(l)):
        (e,f,g,h) = l[j]
        d2 = dist(e,f,g,h)
        if dist(a,b,e,f) - (d1+d2) == 2:
            do(i, j)

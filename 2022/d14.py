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

blocked = set()
mxy = 0
for x in l:
    p,q = x[:2]
    mxy = max(mxy, q)
    for y in range(2, len(x), 2):
        a, b = x[y:y+2]
        mxy = max(mxy, b)
        dx, dy = a-p, b-q
        if dx!=0:
            dx = dx/abs(dx)
        if dy!=0:
            dy = dy/abs(dy)
        while (p, q) != (a, b):
            blocked.add((p, q))
            p+=dx
            q+=dy
        blocked.add((p,q))
mxy+=2
c=0
start = (500, 0)
for r in range(2):
    f = True
    while f:
        f = False
        sandx,sandy = start
        while (not r and sandy < 515) or (r and (500,0) not in blocked):
            # print(sandx, sandy)
            sandy += 1
            if (sandx, sandy) in blocked:
                if (sandx-1, sandy) in blocked:
                    if (sandx+1, sandy) in blocked:
                        blocked.add((sandx, sandy-1))
                        c+=1
                        f = True
                        break
                    else:
                        sandx+=1
                else:
                    sandx-=1
    print(c)
    for n in range(0, 1000):
        blocked.add((n, mxy))

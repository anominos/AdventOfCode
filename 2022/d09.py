*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []
import re
def func(x):
    return [x[0], *map(int, re.findall(r"-?\d+",x)),]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))
for ii in [2,10]:
    knots = [[0,0] for _ in range(ii)]
    s = set([tuple([0,0])])
    dd = [[0,1],[1,0],[0,-1],[-1,0]]
    ins = "URDL"
    for a,b in l:
        dx, dy = dd[ins.index(a)]
        for _ in range(b):
            knots[0][0] += dx
            knots[0][1] += dy
            for i in range(1, ii):
                t = knots[i]
                h = knots[i-1]
                if max(abs(t[1] - h[1]), abs(t[0]-h[0])) > 1:
                    if t[1] > h[1]:
                        t[1]-=1
                    elif t[1] < h[1]:
                        t[1] += 1
                    if t[0] > h[0]:
                        t[0] -= 1
                    elif t[0] < h[0]:
                        t[0] += 1
            s.add(tuple(knots[-1]))
    print(len(s))

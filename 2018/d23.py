import re
from itertools import combinations
from z3 import z3


l = []
with open("d23in.txt") as f:
    for x in f.readlines():
        a,b,c,d = re.findall(r"-?\d+", x)
        l.append([*map(int, [a,b,c,d])])

m = max(l, key=lambda a:a[-1])
c=0

def dist(x,y):
    return sum(map(lambda a,b: abs(a-b), x[:-1], y[:-1]))

def mid(x, y):
    return (*map(lambda a: a/2, map(int.__add__, x[:-1], y[:-1])),)

for x in range(len(l)):
    if dist(l[x], m) <= m[-1]:
        c+=1
print(c)


x = z3.Int("x")
y = z3.Int("y")
z = z3.Int("z")

opt = z3.Optimize()
for (px, py, pz, r) in l:
    opt.add_soft(z3.Abs(px-x) + z3.Abs(py-y) + z3.Abs(pz-z) <= r)

opt.minimize(x + y + z)

opt.check()
m = opt.model()
print(m.eval(x + y + z))
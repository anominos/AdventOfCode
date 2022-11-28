from collections import defaultdict, deque
from typing import DefaultDict

d = defaultdict(bool)
with open("d12in.txt")as f:
    g= f.readlines()
    init, sc = g[0], g[2:]
    init = init.split(": ")[1][:-1]
    for x in sc:
        a, b = x.strip().split(" => ")
        d[a] = b=="#"

pots = defaultdict(bool)
for i, x in enumerate(init):
    pots[i] = x=="#"
gen = 1
p5 = deque([-1,-1,-1,-1,-1])
while True:
    newP = defaultdict(bool)
    for index in range(min(pots.keys())-2, max(pots.keys())+3):
        c = ""
        for g in range(index-2, index+3):
            c+=".#"[pots[g]]
        newP[index] = d[c]
    pots = newP.copy()
    c=0
    for i,x in pots.items():
        if x:
            c+=i
    p5.popleft()
    p5.append(c)
    dif = p5[1]-p5[0]
    for x in range(len(p5)-1):
        if p5[x+1]-p5[x]!=dif:
            break
    else:
        break
    if gen==20:
        print(c)
    gen+=1

mxGen = 50_000_000_001
mxGen -= gen
print(c + (mxGen-1)*dif)
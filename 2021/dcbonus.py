dat = []
with open("dcbonusin.txt") as f:
    for x in f:
        dat.append((x.strip()))

d = dict(zip("1#0.", "aa ab da db".split()))
from collections import deque
alive = []
ant = []
for x in range(len(dat)):
    alive.append([])
    ant.append([])
    for y in range(len(dat[0])):
        alive[-1].append(d[dat[x][y]][0]=="a")
        ant[-1].append(d[dat[x][y]][1]=="a")
        
n = int(1e10)
ant = ant[n%len(ant):] + ant[:n%len(ant)]
alive = [i[n%len(alive):]+i[:n%len(alive)] for i in alive]

c=0
for x in range(len(dat)):
    for y in range(len(dat[0])):
        if alive[x][y]:
            if ant[x][y]:
                c+=1
            else:
                c-=1
print(abs(c))

o = ""
for x in range(len(dat)):
    for y in range(len(dat[0])):
        # print(alive[x][y], ant[x][y], alive[x][y]<<1, (alive[x][y]<<1) | ant[x][y])
        o+=".0#1"[(alive[x][y]<<1) | ant[x][y]]
    o+="\n"

with open("dcbonusout.txt","w") as f:
    f.write(o.replace("#", "").replace(".", ""))
# o = ""
# for x in range(len(dat)):
#     for y in range(len(dat[0])):
#         if ant[x][y]:
#             o+="01"[alive[x][y]]
#     o+="\n"
# with open("dcbonusout.txt","w") as f:
#     f.write(o)
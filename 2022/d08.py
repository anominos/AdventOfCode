*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []
import re
import numpy as np
def func(x):
    return [*map(int, re.findall(r"\d",x)),]
    return str((x))
with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))
l = np.array(l)

s = set()
c=0
for x in range(len(l)):
    for y in range(len(l[x])):
        try:
            if min(l[:x,y].max(),
                l[x+1:,y].max(),
                l[x,:y].max(),
                l[x,y+1:].max()) < l[x][y]:
                s.add((x,y))
        except ValueError:
            s.add((x,y))
        # r=1
        # for forward in [l[x+1:,y],l[x,y+1:]]:
        #     # if forward.size==0:
        #     #     r=0
        #     try:
        #         whr = np.where(forward < l[x,y], -1, l[x,y])
        #         whr=np.append(whr, l[x,y])
        #         amx = np.argmax(whr)+1
        #         r*=amx
        #         print(forward,x,y,whr,amx)
        #     except ValueError:
        #         pass
        # for b in [l[:x,y],l[x,:y]]:
        #     # if b.size==0:
        #     #     r=0
        #     try:
        #         whr = np.where(b[::-1] < l[x,y], -1, l[x,y])
        #         whr=np.append(whr, l[x,y])
        #         amx = len(b) - np.argmax(whr)
        #         r*=amx
        #         print(b,x,y,whr,amx)
        #     except ValueError:
        #         pass
        # print()
        # c = max(r,c)
c=0
for x in range(len(l)):
    for y in range(len(l[x])):
        r=1
        for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
            cx,cy = x,y
            n=0
            while True:
                try:
                    cx+=dx
                    cy+=dy
                    if not(0<=cx<len(l) and 0<=cy<len(l[0])):
                        break

                    n+=1
                    if not l[cx,cy] < l[x,y]:
                        break
                except:
                    break
            r*=n
        c = max(c,r)


print(len(s))
print(c)

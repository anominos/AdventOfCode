*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []
import re
def func(x):
    return [*map(lambda a:ord(a)-ord("a"), x),]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

adj = [[0,1],[1,0],[0,-1],[-1,0]]
q = set()
for i,x in enumerate(l):
    for j,y in enumerate(x):
        if chr(y+ord("a"))=="S":
            start=((i,j))
            l[i][j] = 0
        if y==0:
            q.add((i,j))
            l[i][j] = 0
        if chr(y+ord("a")) == "E":
            end = i,j
            l[i][j] = 25

def doq(q):
    c=0
    while end not in q:
        newq = set()
        for curx,cury in q:
            for dx,dy in adj:
                if 0<=curx+dx<len(l) and 0<=cury+dy<len(l[0]):
                    if l[curx+dx][cury+dy] <= l[curx][cury]+1:
                        newq.add((curx+dx, cury+dy))
        c+=1
        q = newq
    print(c)
doq({start})
doq(q)

d = {".":0, "|":1, "#":2}
d1 = dict(zip(d.values(), d.keys()))
l =[]
with open("d18in.txt") as f:
    for x in f:
        l.append(list(map(lambda a:d[a], x.strip())))
from copy import deepcopy
def getAdj(l, x, y):
    for i in range(-1,2):
        for j in range(-1, 2):
            if not i==j==0:
                try:
                    if y+j >=0 and x+i >=0:
                        yield l[y+j][x+i]
                except IndexError:
                    continue
s=[]
check  = set()
c=0
while True:
    n = deepcopy(l)
    for y in range(len(l)):
        for x in range(len(l[0])):
            a=[i for i in getAdj(l, x, y)]
            if l[y][x] == 0:
                if a.count(1)>=3:
                    n[y][x] = 1
            elif l[y][x] == 1:
                if a.count(2)>=3:
                    n[y][x] = 2
            else:
                if not(a.count(2) >= 1 and a.count(1) >= 1):
                    n[y][x] = 0
    l = deepcopy(n)
    if c==9:
        lum, tre = 0,0
        for x in l:
            lum+=x.count(2)
            tre += x.count(1)
        print(lum*tre)
    string = "".join(["".join(map(lambda a:d1[a], i)) for i in l])
    hsh = (string)
    if hsh in check:
        end = hsh
        break
    s.append(hsh)
    check.add(hsh)
    c+=1

n = s[(1000000000 - c)%(c-s.index(end))+ s.index(end) - 1]

print(n.count("|")*n.count("#"))
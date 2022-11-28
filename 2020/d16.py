dat = []
with open("d16test.txt") as f:
    for x in f.read().split("\n\n"):
        dat.append((x.strip()))

bounds = []
for x in dat[0].splitlines():
    a, b = x.split(": ")[1].split(" or ")
    n = []
    for i in [a,b]:
        n.append(tuple(map(int, i.split("-"))))
    bounds.append(n)

c=0
val =[]
for x in dat[-1].splitlines()[1:]:
    f=True
    for y in x.split(","):
        y = int(y)
        if not any([i<=y<=j for z in bounds for i,j in z]):
            c+=y
            f = False
    if f:
        val.append(x)
print(c)


from collections import defaultdict

poss = defaultdict(lambda:list(range(len(bounds))))
for x in val:
    for j,y in enumerate(x.split(",")):
        y = int(y)
        for i, z in enumerate(bounds):
            if not any(n<=y<=m for n, m in z):
                # print(y, z, i, j)
                if i in poss[j]:
                    poss[j].remove(i)
d = dict(zip(range(len(bounds)), [-1]*len(bounds)))
for x in range(len(bounds)):
    poss[x]
while -1 in d.values():
    for k,v in poss.items():
        if len(v)==1:
            v = v[0]
            d[k] = v
            for j in poss.values():
                if v in j:
                    j.remove(v)
            del poss[k]
            break

my = list(map(int, dat[1].splitlines()[1:][0].split(",")))
m=1
for k, v in d.items():
    if v<6:
        m*=my[k]
print(m)
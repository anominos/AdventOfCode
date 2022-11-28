dat = []
with open("d21in.txt") as f:
    for x in f.read().split("\n"):
        dat.append((x.strip()))

all = []
d = {}
for x in dat:
    a = x.split(" (contains ")
    if len(a)==2:
        stuff, aller = a
    else:
        all.extend(a[0].split())
        continue
    aller = aller[:-1]
    all.extend(stuff.split())
    for y in aller.split(", "):
        if y in d.keys():
            d[y] &= set(stuff.split())
        else:
            d[y] = set(stuff.split())

while len(max(d.values(), key=len))>1:
    for x, y in d.items():
        if len(y)==1:
            for i in y:
                break
            for w,z in d.items():
                if w != x and i in z:
                    z.remove(i)
s = set()
for v in d.values():
    s|=v
c=0
for x in all:
    if not x in s:
        c+=1
print(c)

print(*(j.pop()for i, j in sorted(d.items())),sep=",")

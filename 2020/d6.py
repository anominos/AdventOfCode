dat = []
dat2=[]
with open("d6in.txt") as f:
    for x in f.read().split("\n\n"):
        dat2.append(x.split())
        dat.append(x.replace("\n", ""))
c=0
for x in dat:
    c+=len(set(x))
print(c)
c=0
for x in dat2:
    s = set(x[0])
    for y in x:
        s&=set(y)
    c+=len(s)
print(c)
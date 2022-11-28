dat = []
with open("d13in.txt") as f:
    for x in f:
        dat.append((x.strip()))

est = int(dat[0])
times = dat[1].split(",")
mn = (float("inf"),)
for x in times:
    if x!="x":
        x = int(x)
        mn = min(mn,(x-(est%x), x))
print(mn[0]*mn[1])
d = {}
for i, x in enumerate(times):
    if x!="x":
        x= int(x)
        d[x] = i

cur = 0
mul = 1
for x,i in d.items():
    while cur%x!=(x-i)%x:
        cur+=mul
    mul*=x
print(cur)

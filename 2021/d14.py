dat = []
with open("d14in.txt") as f:
    for x in f.read().split("\n\n"):
        dat.append((x.strip()))
start = dat[0]
first,last = start[0], start[-1]
d = {}
for x in dat[1].splitlines():
    a,b = x.split(" -> ")
    d[a] = b
from collections import Counter

# for _ in range(10):
#     add = ""
#     for x in range(len(start)-1):
#         add += d[start[x:x+2]]
#     start = "".join(sum(zip(start, add), tuple()))+start[-1]
# c = Counter(start)
c = Counter()
for x in range(len(start)-1):
    c[start[x:x+2]] +=1

for _ in range(40):
    cpy = Counter()
    for a,b in c.items():
        cpy[a[0] + d[a]]+=b
        cpy[d[a]+a[1]] += b
    c = cpy
    # print(c)
    if _ == 9:
        f = Counter()
        for i,x in c.items():
            f[i[0]]+=x
            f[i[1]]+=x
        f[first]+=1
        f[last]+=1
        for i,x in f.items():
            if x == max(f.values()):
                a = x
            if x == min(f.values()):
                b = x
        print((a-b)//2)


f = Counter()
for i,x in c.items():
    f[i[0]]+=x
    f[i[1]]+=x
f[first]+=1
f[last]+=1
for i,x in f.items():
    if x == max(f.values()):
        a = x
    if x == min(f.values()):
        b = x
print((a-b)//2)
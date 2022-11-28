import re
dat = []
with open("d14in.txt") as f:
    for x in f.read().strip().splitlines():
        dat.append(list(map(int, re.findall(r"\d+", x))))


d =[]
for x in dat:
    t,m = divmod(2503, (x[2]+x[1]))
    t = t*(x[0]*x[1])
    t+= min(x[1], m)*x[0]
    d.append(t)
print(max(d))
rd = [0]*len(dat)
p = [0] * len(dat)
for t in range(2503):
    for i,x in enumerate(rd):
        if t%(dat[i][1]+dat[i][2]) < dat[i][1]:
            rd[i] += dat[i][0]
    for i,x in enumerate(rd):
        if x==max(rd):
            p[i]+=1
print(max(p))

import re
dat = []
with open("d15in.txt") as f:
    for x in f:
        dat.append(list(map(int, re.findall("-?\d+", x))))
mx=0
mx2=0
for a in range(100):
    for b in range(100-a):
        for c in range(100-a-b):
            d = 100-a-b-c
            if d<=0:break
            n = 1
            for x in range(len(dat[0])-1):
                j = (dat[0][x]*a + dat[1][x]*b+dat[2][x]*c+dat[3][x]*d)
                j = max(0, j)
                n*=j
            mx = max(mx, n)
            if dat[0][-1]*a + dat[1][-1]*b+dat[2][-1]*c+dat[3][-1]*d == 500:
                mx2 = max(mx2, n)
print(mx)
print(mx2)
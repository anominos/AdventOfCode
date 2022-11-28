import sys
dat = []
with open("d9in.txt") as f:
    for x in f:
        dat.append(int(x.strip()))

for i in range(25, len(dat)):
    pre = dat[i-25:i]
    pre = set(pre)
    for x in pre:
        if dat[i]-x in pre:
            break
    else:
        n = dat[i]
        print(dat[i])

for l in range(2,len(dat)):
    for start in range(len(dat)-l):
        r = dat[start:start+l]
        if sum(r)==n:
            print(max(r)+min(r))
            sys.exit()
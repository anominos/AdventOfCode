import re, sys
sys.setrecursionlimit(8196)
dat = []
with open("d23in.txt") as f:
    for x in f:
        dat.append(list(map(int, re.findall(r"(-?\d+)",x))))
loc = max(dat, key=lambda a:a[-1])
c=0
for x in dat:
    if sum([abs(a-b) for a,b in zip(x[:-1], loc[:-1])]) <= loc[-1]:
        c+=1
print(c)


def isPoss(ind, left, bounds):
    # print(ind, left, bounds)
    if left==0:
        for x in range(0,6,2):
            if bounds[x] > bounds[x+1]:
                return False
        return True
    if ind >= len(dat):
        return False
    nb = list(bounds)
    for x in range(3):
        nb[x*2] = max(nb[x*2], (dat[ind][x] - dat[ind][-1]))
        nb[x*2+1] = min(nb[x*2+1], (dat[ind][x] + dat[ind][-1]))
    return isPoss(ind+1, left, bounds) or isPoss(ind+1, left-1, tuple(nb))

start = (-float("inf"), float("inf"))*3

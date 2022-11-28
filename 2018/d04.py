import datetime, re

def getSecs(a):
    d = datetime.datetime.fromisoformat(a)
    td = d - datetime.datetime(1500, 1, 1)
    return td.total_seconds()
d = {}
with open("d04in.txt")as f:
    for x in f:
        a, b= re.match(r"\[(.*)\] (.*)", x).groups()
        n = getSecs(a)
        d[n] = [int(re.search(r":(\d+)",x).group(1)),b]

from collections import defaultdict
dSleep = defaultdict(list)
cur  = -1
curSl = 0
for x in sorted(d.keys()):
    mins = d[x][0]
    dat = d[x][1].split()
    if dat[0]=="Guard":
        cur = int(dat[1][1:])
    elif dat[0] == "falls":
        curSl = mins
    elif dat[0] == "wakes":
        dSleep[cur].extend(range(curSl, mins))
mm = (0,0,0)
n = 0
for x, y in dSleep.items():
    if sum(y) > mm[0]:
        mm = (sum(y),x)
        n = y
print(max(n, key=n.count)*mm[1])
mm = 0
n = 0
for x, y in dSleep.items(): 
    if mm < y.count(max(y, key=y.count)):
        mm = y.count(max(y, key=y.count))
        n = [x, max(y, key=y.count)]
print(n[0]*n[1])
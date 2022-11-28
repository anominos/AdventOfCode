dat = []
from itertools import product
from collections import deque
with open("d11in.txt") as f:
    for x in f:
        dat.append(list(map(int, x.strip())))
o=0
step = 0
while True:
    step+=1
    # print(step)
    # for x in (dat):
    #     print(x)
    a = deque()
    for x in range(len(dat)):
        for y in range(len(dat[x])):
            dat[x][y] += 1
            if dat[x][y] > 9:
                a.append((x,y))
    done = set()
    while a:
        cx,cy = a.popleft()
        if (cx,cy) in done:
            continue
        
        done.add((cx,cy))
        if step<=100:
            o+=1
        for dx,dy in product(range(-1,2),repeat=2):
            if not(dx==dy==0) and 0<=cx+dx<len(dat) and 0<=cy+dy<len(dat[x]):
                dat[cx+dx][cy+dy]+=1
                if dat[cx+dx][cy+dy] > 9:
                    a.append((cx+dx,cy+dy))
    n=0

    for x in range(len(dat)):
        for y in range(len(dat[x])):
            if dat[x][y]>9:
                dat[x][y] = 0
                n+=1
    if n== len(dat)*len(dat[0]):
        break
    # input()
print(o)
print(step)

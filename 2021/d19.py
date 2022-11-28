dat = []
with open("d19testin.txt") as f:
    for x in f.read().split("\n\n"):
        dat.append((x.strip().splitlines()[1:]))

for x in range(len(dat)):
    dat[x] = [tuple(map(int, i.split(","))) for i in dat[x]]
from itertools import permutations, product
from collections import Counter, defaultdict, deque

def allDiff(a,b,c,f):
    b = list(b)
    for x in product(range(2),repeat=3):
        for rs in range(3):
            g = []
            for i,y in enumerate(x):
                if y:
                    g.append(abs(a[i]-b[i]))
                else:
                    g.append(abs(a[i]+b[i]))
            if sum(x)%2:
                g.reverse()
            c[tuple(g)]+=1
            f[tuple(g)].append((a,b,x,rs))
            b.append(b.pop(0))
def diff(a,b):
    return (abs(a[0]-b[0]),abs(a[1]-b[1]), abs(a[2]-b[2]))
def findPair(lst):
    oo = []
    for x in range(len(lst)):
        for y in range(x+1, len(lst)):
            print(x,y)
            a,b = lst[x],lst[y]
            c=Counter()
            f = defaultdict(list)
            for start in a:
                for end in b:
                    allDiff(start,end,c,f)
            # print(c.most_common(3))
            for i,z in c.most_common(1):
                if z>=12:
                    return (x,y,i,z,f[i])

def trueDiff(a,b):
    return a[0]-b[0], a[1]-b[1], a[2]-b[2]

def combine(lst,a,b,offs,h):
    m = deque([x if h[0][2][i] else -x for i,x in enumerate(h[0][1])])
    if sum(h[0][2])%2:m.reverse()
    m.rotate(h[0][3])
    r = trueDiff(h[0][0],m)
    
    n = set(map(tuple,lst[a]))
    for j in lst[b]:
        j = deque([y if h[0][2][i] else -y for i,y in enumerate(j)])
        if sum(h[0][2])%2:m.reverse()
        m.rotate(h[0][3])
        j = tuple(y+r[i] for i,y in enumerate(j))
        n.add(j)
    lst[a] = list(n)
    del lst[b]

# for x in dat:print(x)

while len(dat)>1:
    # print(findPair(dat))
    x,y,i,z,h = findPair(dat)
    print(x,y,i)
    combine(dat, x,y,i,h)
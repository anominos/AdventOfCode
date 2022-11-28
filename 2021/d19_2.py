dat = []
with open("d19in.txt") as f:
    for x in f.read().split("\n\n"):
        dat.append((x.strip().splitlines()[1:]))

for x in range(len(dat)):
    dat[x] = [tuple(map(int, i.split(","))) for i in dat[x]]


transformations = []
from itertools import product
for x in product(range(2),repeat=3):
    if sum(x)%2:
        r = "lambda a:({}a[1],{}a[0],{}a[2])".format(*(" -"[i] for i in x))
        transformations.append(eval(r))
        r = "lambda a:({}a[2],{}a[1],{}a[0])".format(*(" -"[i] for i in x))
        transformations.append(eval(r))
        r = "lambda a:({}a[0],{}a[2],{}a[1])".format(*(" -"[i] for i in x))
        transformations.append(eval(r))
    else:
        r = "lambda a:({}a[0],{}a[1],{}a[2])".format(*(" -"[i] for i in x))
        transformations.append(eval(r))
        r = "lambda a:({}a[2],{}a[0],{}a[1])".format(*(" -"[i] for i in x))
        transformations.append(eval(r))
        r = "lambda a:({}a[1],{}a[2],{}a[0])".format(*(" -"[i] for i in x))
        transformations.append(eval(r))

from collections import Counter, defaultdict
def diff(a,b):
    return a[0]-b[0], a[1]-b[1], a[2]-b[2]
def add(a,b):
    return a[0]+b[0], a[1]+b[1], a[2]+b[2]

# d = defaultdict(list)
done = {0}
oo = []
while done != set(range(len(dat))):
    for cur in range(len(dat)):
        print(cur)
        for x in range(len(dat)):
            if not(cur in done):
                continue

            if x==cur:continue
            for t in transformations:
                possPoints = Counter()
                a = list(map(t, dat[x]))
                for n in dat[cur]:
                    for m in a:
                        possPoints[diff(n,m)]+=1
                if possPoints.most_common(1)[0][1] >= 12:
                    oo.append(possPoints.most_common(1)[0][0])
                    # print(cur,x,t((0,1,2)))
                    o = []
                    # print(possPoints.most_common(1)[0][0], cur,x)
                    for m in a:
                        o.append(add(possPoints.most_common(1)[0][0], m))
                        # if o[-1] == (-889,563,-600):
                        #     print(possPoints.most_common(1)[0][0],m,cur,x)
                    # print(x)
                    dat[x] = o
                    done.add(x)
                    break
          
points = set(sum(dat,[]))
# for x in sorted(points):
#     print(",".join(map(str,x)))
print(len(points))
# print(tOff)
mx = 0
for x in oo:
    for y in oo:
        mx = max(mx,abs(x[0]-y[0])+abs(x[1]-y[1])+abs(x[2]-y[2]))
print(mx)
#<456
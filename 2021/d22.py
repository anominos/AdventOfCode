dat = []
with open("d22in.txt") as f:
    for x in f:
        dat.append((x.strip()))


from collections import defaultdict
from itertools import product
import re


l = []
for x in dat:
    a = x.split()
    change = a[0]=="on"
    b = re.findall("-?\d+", x)
    b = list(map(int,b))
    for n in [1,3,5]:
        b[n]+=1
    l.append((change,b))

def do(lx,hx,ly,hy,lz,hz):
    d = defaultdict(bool)
    for change,b in l:
        for x in range(max(lx,b[0]),min(b[1],hx)):
            for y in range(max(ly,b[2]),min(b[3],hy)):
                for z in range(max(lz,b[4]),min(b[5],hz)):
                    d[x,y,z] = change
    return (sum(d.values()))
print(do(-50,50,-50,50,-50,50))


# def intVol(a,b):
#     x = sorted([a[0],a[1],b[0],b[1]])
#     if x!= a[:2]+b[:2] and x!= b[:2]+a[:2]:
#         x = x[2]-x[1]
#     else:x=-1
#     y = sorted([a[2],a[3],b[2],b[3]])
#     if y!= a[2:4]+b[2:4] and y!= b[2:4]+a[2:4]:
#         y = y[2]-y[1]
#     else:y=-1
#     z = sorted([a[4],a[5],b[4],b[5]])
#     if z!= a[4:]+b[4:] and z!= b[4:]+a[4:]:
#         z = z[2]-z[1]
#     else:z=-1
#     if x<0 or y<0 or z<0:return 0
#     return (x+1)*(y+1)*(z+1)

# d = defaultdict(list)
# s=0
# for x in range(len(l)):
#     if l[x][0]:
#         q,w,e,r,t,y = l[x][1]
#         s+= (w-q+1)*(r-e+1)*(y-t+1)
#     for y in range(x+1,len(l)):
#         if intVol(l[x][1], l[y][1])>0 and not(l[x][0]==l[y][0]==True):
#             d[x].append(y)
#             d[y].append(x)
#             # s-= intVol(l[x][1],l[y][1])
# print(d)
# print(s)
# print(2758514936282235)

# g = [0,0,0,0,0,0]
# for change,b in l:
#     for i in range(len(g)):
#         g[i] = (max if i&1 else min)(g[i], b[i])
# print(g)



# dx,dy,dz = [defaultdict(bool) for _ in range(3)]
# for change,b in l:
#     for x in range(b[0],b[1]+1):
#         dx[x] = change
#     for y in range(b[2],b[3]+1):
#         dy[y] = change
#     for z in range(b[4],b[5]+1):
#         dz[z] = change

def getInt(a,b):
    c = []
    for i in [0,2,4]:
        xs = sorted(a[i:i+2]+b[i:i+2])
        if (xs==a[i:i+2]+b[i:i+2] or xs==b[i:i+2]+a[i:i+2]):
            return [0]*6
        c.extend(xs[1:3])
    return c


cuboids = []

for change,b in l:
    nc = []
    for x in cuboids:
        r = getInt(b,x)
        # print(r)
        if r != [0]*6:  
            pairs = []
            for i in [0,2,4]:
                go=False
                l = []
                for n in sorted(b[i:i+2] + x[i:i+2]):
                    if n==x[i]:
                        go=True
                    if go:
                        l.append(n)
                    if n==x[i+1]:go=False
                pairs.append([l[j:j+2] for j in range(len(l)-1)])
            # print(x,b,r, pairs)
            for cube in product(*pairs):
                cube = sum(cube,[])
                # print(cube)
                if getInt(cube,b) == [0]*6:
                    # print("HI")
                    nc.append(cube)
            # print()
        else:
            nc.append(x)
    if change:
        nc.append(b)
        # print(b)
    cuboids = nc[:]
c=0
for x in cuboids:
    c+= (x[1]-x[0])*(x[3]-x[2])*(x[5]-x[4])
print(c)
            


l=[]
with open("d20in.txt") as f:
    '''f = """p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>    
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>""".split("\n")'''
    for x in f:
        n = x.strip().split(", ")
        for y in range(len(n)):
            n[y] = list(map(int,n[y][3:-1].split(",")))
        l.append(n)
func = lambda a:(sum(map(abs, a[-1])))
print("silver:", l.index(min(l, key=func)))
'''
objs = len(l)
from math import sqrt
def qform(a, b, c):
    if a==0:
        if b==0:
            return 0 if c==0 else False
        t = (-c/b)
        return t if t >=0 else False
    discr = b**2 - 4*a*c
    if discr < 0:
        return False
    p, n = (-b+sqrt(discr))/(a*2), (-b-sqrt(discr))/(a*2)
    return max(0, min(p*(p==int(p)), n*(n==int(n))))

n = [[False]*len(l) for _ in range(len(l))]

for x in range(objs):
    for y in range(x+1, objs):
        a = l[x]
        b = l[y]
        for z in range(3):
            col = qform(a[2][z]-b[2][z], a[1][z]-b[1][z],a[0][z]-b[0][z])
            if col != False and col == int(col):
                n[x][y] = col
                n[y][x] = col

while True:
    print(len(n), end=" ")
    ans = float("inf")
    for x in n:
        if (c:=list(filter(None, x)))!=[]:
            ans = min(ans, min(c))
    print(ans)
    if ans==float("inf"):
        break
    p=[]
    for x in range(len(n)):
        if ans in n[x]:
            p.append(x)
    p.reverse()
    for x in p:
        for y in n:
            del y[x]
        del n[x]


print(len(n))
#maths ^
'''
from collections import Counter
from time import time
tt = time()
for _ in range(50):
    for y in range(len(l)):
        for z in range(3):
            l[y][1][z] += l[y][2][z]
            l[y][0][z] += l[y][1][z]
    l.sort()
    i=0
    while i<len(l)-1:
        f = False
        while l[i][0]==l[i+1][0]:
            del l[i]
            f=True
        if f:
            del l[i]
        else:
            i+=1
print("gold:",len(l))

'''
s = (init s)+ut+(a*t**2)/2
s1 = s2
(init s1)+u1t+(a1*t**2)/2 = (init s2)+u2t+(a2*t**2)/2

(a1/2)*t**2-(a2/2)*t**2+u1t-u2t+s1-s2 = 0
((a1-a2)/2)t**2 + (u1-u2)t + (s1-s2) = 0


if a == 0:
    s = u*t+(init s)
    s==s:
    u1t + s1 = u2t+s2
    (u1-u2)t=s2-s1
    t=(s2-s1)/(u1-u2)

160< x < 586


'''
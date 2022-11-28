dat = []
with open("d22in.txt") as f:
    for x in f.read().split("\n\n"):
        dat.append(map(int, x.strip().split("\n")[1:]))
dat = [list(i) for i in dat]
o = [list(i) for i in dat]
while len(dat[0])>0 and len(dat[1])>0:
    one = dat[0].pop(0)
    two = dat[1].pop(0)
    if one>two:
        dat[0].append(one)
        dat[0].append(two)
    else:
        dat[1].append(two)
        dat[1].append(one)

dat.remove([])
d =dat.pop()
c=0
for i, x in enumerate(d[::-1], 1):
    c+=i*x
print(c)

dat = o

prev = [set(), set()]

def rec(a, b, pr=None):
    # print(a, b)
    if len(a)==0:
        return 1
    if len(b)==0:
        return 0
    if pr==None:
        pr = prev
    if tuple(a) in pr[0] or tuple(b) in pr[1]:
        return 0
    pr[0].add(tuple(a))
    pr[1].add(tuple(b))
    o = a.pop(0)
    t = b.pop(0)
    if o > len(a) or t > len(b):
        if o > t:
            a.extend([o,t])
            return False
        else:
            b.extend([t,o])
            return True
    else:
        x = a[:o]
        y = b[:t]
        p = [set(), set()]
        while type(z:=rec(x,y, p))!=int:
            pass
        if z:
            b.extend([t,o])
            return True
        else:
            a.extend([o,t])
            return False

c=0
while True:
    c+=1
    # print(c,dat)
    if type(y:=rec(dat[0], dat[1]))==int:
        d = dat[y]
        break
# print(dat)



c=0
for i, x in enumerate(d[::-1], 1):
    c+=i*x
print(c)
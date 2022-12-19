*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []
import re
def func(x):
    return [*map(int, re.findall(r"-?\d+",x)),]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

def update(x):
    for i in range(4):
        x[i+4] += x[i]



cc=0
for prices in l:
    done = {}
    idn, a, b, c,d, e,f = prices
    lprices = [a, b, (c, d), (e, f)]
    q = [[1, 0, 0, 0, 0, 0, 0, 0]]
    for _ in range(24):
        nq = []
        for r in q:
            if r[4] >= lprices[3][0] and r[6] >= lprices[3][1]:
                n = [i for i in r]
                n[4] -= lprices[3][0]
                n[6] -= lprices[3][1]
                update(n)
                n[3]+=1
                nq.append(n)
            else:
                n = [i for i in r]
                update(n)
                nq.append(n)
            if r[4] >= lprices[2][0] and r[5] >= lprices[2][1]:
                n = [i for i in r]
                n[4] -= lprices[2][0]
                n[5] -= lprices[2][1]
                update(n)
                n[2]+=1
                nq.append(n)
            if r[4] >= lprices[1]:
                n = [i for i in r]
                n[4] -= lprices[1]
                update(n)
                n[1] +=1
                nq.append(n)
            if r[4] >= lprices[0]:
                n = [i for i in r]
                n[4] -= lprices[0]
                update(n)
                n[0] += 1
                nq.append(n)
        nq.sort(key=lambda a: [a[-1], a[3], a[-2], a[2], a[1], a[0]], reverse=True)
        q = [nq[0]]
        for x in nq[1:20000]:
            if x != q[-1]:
                q.append(x)
        # if _ == 13:
        # print(q)
        # input()
        # print(len(q), _)
    cc+=(max(q, key=lambda a:a[-1])[-1] * idn)
print(cc)


cc=1
for prices in l[:3]:
    done = {}
    idn, a, b, c,d, e,f = prices
    lprices = [a, b, (c, d), (e, f)]
    q = [[1, 0, 0, 0, 0, 0, 0, 0]]
    for _ in range(32):
        nq = []
        for r in q:
            if r[4] >= lprices[3][0] and r[6] >= lprices[3][1]:
                n = [i for i in r]
                n[4] -= lprices[3][0]
                n[6] -= lprices[3][1]
                update(n)
                n[3]+=1
                nq.append(n)
            else:
                n = [i for i in r]
                update(n)
                nq.append(n)
            if r[4] >= lprices[2][0] and r[5] >= lprices[2][1]:
                n = [i for i in r]
                n[4] -= lprices[2][0]
                n[5] -= lprices[2][1]
                update(n)
                n[2]+=1
                nq.append(n)
            if r[4] >= lprices[1]:
                n = [i for i in r]
                n[4] -= lprices[1]
                update(n)
                n[1] +=1
                nq.append(n)
            if r[4] >= lprices[0]:
                n = [i for i in r]
                n[4] -= lprices[0]
                update(n)
                n[0] += 1
                nq.append(n)
        nq.sort(key=lambda a: [a[-1], a[3], a[-2], a[2], a[1], a[0]], reverse=True)
        q = [nq[0]]
        for x in nq[1:20000]:
            if x != q[-1]:
                q.append(x)
        # if _ == 13:
        # print(q)
        # input()
        # print(len(q), _)
    cc*=max(q, key=lambda a:a[-1])[-1]
print(cc)
""">1143"""

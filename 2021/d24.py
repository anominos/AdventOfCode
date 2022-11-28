dat = []
with open("d24in.txt") as f:
    for x in f:
        dat.append((x.strip()))
l = []
for x in dat:
    if x.split()[0]=="inp":
        l.append([])
    l[-1].append(x)
r,s,t = [],[],[]
for x in range(len(l[0])):
    o = ""
    for g in l:
        o+= g[x] + " "*(10-len(g[x]))
        if x==5:r.append(int(g[x].split()[-1]))
        if x==15:s.append(int(g[x].split()[-1]))
        if x==4:t.append(int(g[x].split()[-1]))

def interp(b,d):
    try:
        return int(b)
    except ValueError:
        return d[b]

def run(a, inps):
    d = {}
    for i in "wxyz":
        d[i] = 0

    for x in dat:
        a = x.split()
        if a[0]=="inp":
            # print(d)
            d[a[1]] = int(inps.pop())
        elif a[0] == "add":
            d[a[1]] += interp(a[2],d)
        elif a[0] == "mul":
            d[a[1]] *= interp(a[2],d)
        elif a[0] == "div":
            d[a[1]] //= interp(a[2],d)
        elif a[0] == "mod":
            d[a[1]] %= interp(a[2],d)
        elif a[0] == "eql":
            d[a[1]] = int(d[a[1]] == interp(a[2],d))
    return d

def run2(inps,df="9"):
    z=0
    l = ""
    for x in range(len(r)):
        n = z%26
        z//= t[x]
        if t[x] == 1:
            w =int(inps.pop())
            l+=str(w)
            if (n + r[x])!=w:
                z*= 26
                z+=w+s[x]
        else:
            if 1<= n+r[x] <= 9:
                l+= str(n+r[x])
            else:
                l+=df
                z*=26
                z+= 9+s[x]
    return z,l


for x in range(100_000_000, 10000000, -1):

    if "0" in str(x):continue
    a,b = run2(list(str(x)))
    if a==0:
        print(b)
        break

for x in range(10_000_000, 100000000):
    # if x%1_00_000==0:print(x)

    if "0" in str(x):continue
    a,b = run2(list(str(x)),"1")
    if a==0:
        print(b)
        break
# for x in range(int("9"*14), int("1"+"0"*13),-1):
#     d = run(dat, [int(i) for i in str(x)])
#     print(x,d["z"])
#     if d["z"]==0:
#         print(x)
#         break

'''
r = z%26
z//= __

if (r + __)!=w:
    z*= 26 +w+__
'''
dat = []
with open("d14in.txt") as f:
    for x in f:
        dat.append((x.strip()))

from collections import defaultdict

def getAll(a):
    if len(a)==1:
        a = list(a.replace("f", "01"))
        return a
    b = getAll(a[1:])
    for x in range(len(b)):
        if a[0]=="f":
            b.append("0"+b[x])
            b[x] = "1"+b[x]
        else:
            b[x] = a[0]+b[x] 
    return b      

mem = defaultdict(lambda :"0"*36)
msk=""
for x in dat:
    c, r = x.split(" = ")
    if c=="mask":
        msk = r
    else:
        curAdd = bin(int(c.split("[")[1][:-1]))[2:]
        curAdd = "0"*(36-len(curAdd))+curAdd
        newAdd = ""
        for x in range(len(msk)):
            if msk[x]=="0":
                newAdd+=curAdd[x]
            elif msk[x]=="1":
                newAdd+="1"
            else:
                newAdd+="f"
        for x in getAll(newAdd):
            mem[int(x, 2)] = int(r)


c=0
for k,v in mem.items():
    c+=v
print(c)
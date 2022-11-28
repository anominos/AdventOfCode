dat = []
with open("d5in.txt") as f:
    for x in f:
        dat.append((x.strip()))

mx = 0
a=[]
for x in dat:
    lx, hx = 0,128
    ly, hy = 0,8
    for y in x:
        if y=="F":
            hx=(hx+lx)//2
        elif y=="B":
            lx=(hx+lx)//2
        elif y=="L":
            hy=(hy+ly)//2
        else:
            ly=(hy+ly)//2
    mx = max(mx, lx*8+ly)
    a.append(lx*8+ly)
print(mx)
print(max(set(range(mx))-set(a)))
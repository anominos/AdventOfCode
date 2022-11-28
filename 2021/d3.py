dat = []
with open("d3in.txt") as f:
    for x in f:
        dat.append((x.strip()))

# dat = """00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010""".splitlines()
def mx(dat, g):
    a=""
    b=""
    c=0
    for x in dat:
        c+=x[g]=="1"
    if c*2 >= len(dat):
        a+="1"
        b+="0"
    elif c*2 < len(dat):
        a+="0"
        b+="1"
    return a,b

i,j = "", ""
for x in range(len(dat[0])):
    t,y=(mx(dat,x))
    i+=t
    j+=y
print(int(i,2)*int(j,2))
g = list(dat)
h = list(dat)
for x in range(len(dat[0])):
    r = (mx(g,x))[0]

    for y in range(len(g)):
        if g[y][x]!=r:
            g[y] = -1
    r = (mx(h,x))[1]
    for y in range(len(h)):
        if h[y][x]!=r:
            h[y] = -1
    g = list(filter(lambda a:a!=-1, g))
    h = list(filter(lambda a:a!=-1, h))

    if len(g)==1:
        n=(g[0])
    if len(h)==1:m=(h[0])
print(int(n,2)*int(m,2))
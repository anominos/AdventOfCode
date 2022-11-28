def a(lengths, ss, lst, shifted):

    for x in lengths:
        x = int(x)
        lst = lst[:x][::-1]+lst[x:]
        #lst.rotate(-x-ss)
        lst = lst[(x+ss)%len(lst):]+lst[:(x+ss)%len(lst)]
        shifted += x+ss
        ss+=1

    #shifted -= x+ss-1
    shifted%=len(lst)
    return ss, lst, shifted
def knthash(dat):
    lengths = list(map(ord, dat))
    lengths+=[17, 31, 73, 47, 23]
    s=0
    sh=0
    l = list(range(256))
    for _ in range(64):
        s, l, sh = a(lengths, s, l, sh)
    sh = len(l)-sh
    l = l[sh:]+l[:sh]
    from functools import reduce
    s=[]
    def pad(s):
        if len(s)==1:
            return "0"+s
        return s
    for x in range(0,256,16):
        s.append(reduce(lambda a, b:a^b, l[x:x+16]))
    s = map(lambda a:pad(hex(a)[2:]), s)
    return ("".join(s))

kstring = "hfdlxzhv"
c=0
po = []
for x in range(128):
    hx = knthash(kstring+"-"+str(x))

    hx = f"{int(hx, 16):0128b}"

    c+=hx.count("1")
    po.extend([(i,x) for i,j in enumerate(hx) if j=="1"])
print(c)

'''grid = [["."]*128 for _ in range(128)]
for y in po:
# for i, x in enumerate(c):
    # for y in x:

        grid[y[1]][y[0]] = "#"
f = open("d14d.txt","w")
for x in grid:
    print("".join(x), file=f)
f.close()
'''



pos = set(po)
c = []
n=0
while pos != set():
    todo = {pos.pop()}
    done = set()
    while todo!=set():
        cur = todo.pop()
        done.add(cur)
        for d in [[0,1],[1,0],[0,-1],[-1,0]]:
            y=(d[0]+cur[0], d[1]+cur[1])
            if  y in pos and not y in done:
                todo.add(y)
    pos-=done
    n+=1
print(n)
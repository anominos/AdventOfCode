from collections import defaultdict
def parse(d, n, t):
    if t=="r":
        return d[n]
    else:
        return n

def dofunc(func, args):
    return func(args[0], args[1])

def doLine(l, d):
    op, a, b, c = l
    if op[:3]=="add":
        d[c] = dofunc(lambda a, b: a+b, [parse(d, a, "r"), parse(d, b, op[-1])])
    elif op[:3] == "mul":
        d[c] = dofunc(lambda a, b:a*b, [parse(d, a, "r"), parse(d, b, op[-1])])
    elif op[:3]=="ban":
        d[c] = dofunc(lambda a, b: a&b, [parse(d, a, "r"), parse(d, b, op[-1])])
    elif op[:3]=="bor":
        d[c] = dofunc(lambda a, b: a|b, [parse(d, a, "r"), parse(d, b, op[-1])])
    elif op[:3]=="set":
        d[c] = dofunc(lambda a, b:a, [parse(d, a, op[-1]), b])
    elif op[:2]=="gt":
        d[c] = dofunc(lambda a, b:int(a>b), [parse(d, a, op[-2]), parse(d, b, op[-1])])
    elif op[:2]=="eq":
        d[c] = dofunc(lambda a, b:int(a==b), [parse(d, a, op[-2]), parse(d, b, op[-1])])
    return d
d = defaultdict(int)
opcodes = "addr addi mulr muli banr bani borr bori setr seti gtir gtri gtrr eqir eqri eqrr".split()
if __name__=="__main__":
    with open("d16in.txt") as f:
        p1, p2 = f.read().split("\n\n\n\n")
    p1 = p1.split("\n\n")
    p2 = p2.split("\n")
    codes = [list(opcodes) for _ in range(16)]
    g=0
    for x in p1:
        a, b, c = x.split("\n")
        a, c = a.split(": ")[1][1:-1], c.split(":  ")[1][1:-1]
        a = a.split(", ")
        b = b.split()
        c = c.split(", ")
        a = list(map(int, a))
        b = list(map(int, b))
        c = list(map(int, c))
        d = dict(enumerate(a))
        e = dict(d)
        orig = b[0]
        f=0
        for x in opcodes:
            b[0] = x
            d = doLine(b, d)
            if list(d.values()) != c:
                if x in codes[orig]:codes[orig].remove(x)
            else:
                f+=1
            d = dict(e)
        if f>=3:
            g+=1
    print(g)

    dcode = {}
    # for x in codes:print(x)
    while list(filter(lambda a:a!=[], codes)):
        a = min(filter(lambda a:a!=[], codes), key=len)
        if len(a)!=1:
            print(a)
            break
        a = a[0]
        dcode[codes.index([a])] = a
        for x in codes:
            if a in x:
                x.remove(a)
    print(dcode)
    d = dict(enumerate([0]*4))
    for x in p2:
        a = list(map(int, x.split()))
        a[0] = dcode[a[0]]
        d = doLine(a, d)
    print(d[0])
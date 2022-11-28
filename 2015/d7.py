from functools import lru_cache


def parse(n,bd):
    if n.isdigit():
        return int(n)
    return getVal(n,bd)

    

ops = [lambda a,b:a&b, lambda a,b:a|b, lambda a,b:a<<b, lambda a,b:a>>b]
codes = "AND OR LSHIFT RSHIFT".split()

instr = {}

with open("d7in.txt") as f:
    for x in f:
        x = x.strip()
        a, b = x.split(" -> ")
        instr[b] = a

# print(d)

@lru_cache(maxsize=None)
def getVal(gate,bd=False):
    if bd:
        if gate=="b":
            return getVal("a")
    lhs = instr[gate]
    dat = lhs.split()
    if len(dat)==1:
        return parse(dat[0],bd)
    elif len(dat)==2:
        a = parse(dat[-1],bd)
        return 0xffff - a
    else:
        a, op, b = dat
        a, b= parse(a,bd), parse(b,bd)
        return ops[codes.index(op)](a, b)

print(getVal("a"))
print(getVal("a", True))

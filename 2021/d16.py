from functools import reduce


with open("d16in.txt") as f:
    dat= f.read().strip()

a = bin(int(dat, 16))[2:]
a = "0"*(len(dat)*4 - len(a))+a
def dec(i=0):
    s = a[i:]
    # print(i,s)
    version = int(s[:3],2)
    typ = int(s[3:6],2)
    s = s[6:]
    oi = 6+i
    count = version
    if typ == 4:
        # print("lit")
        d = []
        for x in range(0,len(s),5):
            d.append(s[x+1:x+5])
            if s[x] == "0":
                break
        oi+=x+5
        out = int("".join(d), 2)
    else:
        lty = s[0]
        s = s[1:]
        l = []
        if lty == "0":
            # print("while")
            length = int(s[:15],2)
            # print(length)
            oi+=16
            length+= oi
            while oi < length:
                # print(oi,length)
                c,oi, o = dec(oi)
                l.append(o)
                count+=c
        else:
            # print("for")
            number = int(s[:11],2)            
            oi+=12
            # print(oi)
            for _ in range(number):
                c,oi,o = dec(oi)
                l.append(o)
                count+=c
        r = [sum, lambda c:reduce(lambda a,b:a*b, c), min, max, None, lambda a:int(a[0]>a[1]), lambda a:int(a[0]<a[1]), lambda a:int(a[0]==a[1])]
        out = r[typ](l)
    return count, oi, out


a,b,c = dec()
print(a)
print(c)
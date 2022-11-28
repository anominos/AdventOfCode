'''import re
l=[]
with open("d25in.txt") as f:
    for x in f:
        l.append(x.strip())

def run(start, inst):
    def parse(a):
        if a in "abcd":
            return reg['abcd'.index(a)]
        return int(a)

    instruc = inst
    reg = [start,0,0,0]
    pat1 = re.compile("^(\w+) (.*)$")
    i=0
    while i<len(instruc):

        func, args = re.match(pat1, instruc[i]).groups()
        if func=="cpy":
            x,y = args.split()
            if y in "abcd":
                reg["abcd".index(y)] = parse(x)
        elif func=="inc":
            x = args
            if x in "abcd":
                reg["abcd".index(x)]+=1
        elif func=="dec":
            x = args
            if x in "abcd":
                reg["abcd".index(x)]-=1
        elif func=="jnz":
            x,y = args.split()
            if parse(y)==-2:
                if {instruc[i-1][:3],instruc[i-2][:3]} == {"inc", "dec"}:
                    b, a = map(lambda a:a[4], sorted(instruc[i-2:i]))
                    reg["abcd".index(a)] += reg["abcd".index(b)]
                    reg["abcd".index(b)]=0
            elif parse(x)!=0:
                i+=int(parse(y))-1
        elif func=="tgl":
            x = args
            x = parse(x)
            if i+x <len(instruc):
                before = instruc[i+x][:3]
                args = instruc[i+x][3:]
                if before == "jnz":
                    instruc[i+x]="cpy"+args
                elif before == "cpy":
                    instruc[i+x] = "jnz"+args
                elif before == "inc":
                    instruc[i+x] = "dec"+args
                elif before == "dec" or before == "tgl":
                    instruc[i+x] = "inc"+args
        elif func=="out":
            yield parse(args)
        i+=1
x=0
while True:
    n = run(x,l)
    z=[]
    for y in n:
        z.append(y)
        print(y, end=" ")
        if len(z)>100:
            break
    print()
    if z==[0,1,0,1]:
        break
    x+=1
print(x)'''

'''
cpy a d
cpy 14 c
cpy 182 b
inc d
dec b
jnz b -2

dec c
jnz c -5

d = 14*182 + a
while True:
    cpy d a

    a = d
    while a !=0:

        jnz 0 0
        cpy a b
        cpy 0 a
        cpy 2 c

        b = a
        a = 0
        c = 2

        #int div
            jnz b 2
            jnz 1 6
            dec b
            dec c
            jnz c -4
            inc a
            jnz 1 -7
        ##
        cpy 2 b

        a = b//2
        b=2

        jnz c 2
        jnz 1 4
        dec b
        dec c
        jnz 1 -4

        b-=2



        jnz 0 0

        print(b)
        out b
    jnz a -19
jnz 1 -21
#######################
d = 14*182 + a
while True:
    a = d
    while a !=0:
        b = a
        a = 0
        c = 2
        a = b//2
        b=2
        b-=c
        print(b)
'''
x=-1
f=False
while not f:
    x+=1
    s = bin(x+14*182)[2:]
    f=True
    for y in range(len(s)-1):
        if s[y]==s[y+1]:
            f=False
print(x, s)
import re
ins=[]
with open("d23in.txt","r") as f:
    for x in f:
        ins.append(x.strip())


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
            elif parse(y)==-5:
                string = """cpy b c
inc a
dec c
jnz c -2
dec d"""
                if "\n".join(instruc[i-5:i])==string:
                    reg[0]+=reg[1]*reg[-1]
                    reg[-1]= 0
                else:
                    if parse(x)!=0:
                        i+=int(parse(y))-1
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
        i+=1
    print(reg[0])
run(7, list(ins))
run(12, list(ins))

'''
cpy a b
-
a = input() #7 or 12
b = a


-
dec b
cpy a d
cpy 0 a
cpy b c
inc a
dec c
jnz c -2
dec d
jnz d -5
dec b
cpy b c
cpy c d
dec d
inc c
jnz d -2
-
b-=1
d = a
a=0
a = b*d
b-=1
c = b*2
-


tgl c # toggle every 4th instruction
cpy -16 c
jnz 1 c
cpy 73 c
jnz 91 d
inc a
inc d
jnz d -2
inc c
jnz c -5
'''


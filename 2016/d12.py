import re
instruc=[]
with open("d12in.txt","r") as f:
    for x in f:
        instruc.append(x.strip())

def parse(a):
    if a in "abcd":
        return reg['abcd'.index(a)]
    return int(a)

reg = [0,0,0,0]
pat1 = re.compile("^(\w+) (.*)$")
i=0
while i<len(instruc):
    func, args = re.match(pat1, instruc[i]).groups()
    if func=="cpy":
        x,y = args.split()
        reg["abcd".index(y)] = parse(x)
    elif func=="inc":
        x = args
        reg["abcd".index(x)]+=1
    elif func=="dec":
        x = args
        reg["abcd".index(x)]-=1
    elif func=="jnz":
        x,y = args.split()
        if parse(x)!=0:
            i+=int(y)-1
    i+=1
print(reg[0])

reg = [0,0,1,0]
pat1 = re.compile("^(\w+) (.*)$")
i=0
while i<len(instruc):
    func, args = re.match(pat1, instruc[i]).groups()
    if func=="cpy":
        x,y = args.split()
        reg["abcd".index(y)] = parse(x)
    elif func=="inc":
        x = args
        reg["abcd".index(x)]+=1
    elif func=="dec":
        x = args
        reg["abcd".index(x)]-=1
    elif func=="jnz":
        x,y = args.split()
        if parse(x)!=0:
            i+=int(y)-1
    i+=1
print(reg[0])
'''
cpy 1 a # a = 1
cpy 1 b # b = 1
cpy 26 d #d = 26
jnz c 2 #nothing for silver
jnz 1 5 #skip
cpy 7 c 
inc d
dec c
jnz c -2 #d+=7
##
cpy a c #endskip, c=a
inc a #  --|
dec b #  --| - a+=b, b=0
jnz b -2#--|
cpy c b # b = c 
dec d #d-=1
jnz d -6 #
##
    for x in range(d):
        a+=b
        b=c
        c=a

##
##
cpy 17 c #c=17
cpy 18 d #d=18
inc a  #   |
dec d  #   |-a+=d
jnz d -2 # |
dec c  
jnz c -5#
##
a+=18*17

decomp:
a=b=c=1
for x in range(26): #33 for gold
    a+=b
    b=c
    c=a
a+=18*17


'''
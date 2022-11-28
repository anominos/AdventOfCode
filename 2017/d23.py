n = "abcdefgh"
regs = [0]*8
def isint(a):
    if a[0]=="-":
        return a[1:].isdigit()
    return a.isdigit()
def parse(i):
    if isint(i):
        return int(i)
    return regs[ord(i)-ord("a")]
l=[]
with open("d23in.txt") as f:
    for x in f:
        l.append(x.strip().split())
i=0
c=0
while i < len(l):
    op, args = l[i][0], l[i][1:]
    if op=="set":
        x, y = args
        regs[ord(x)-ord("a")] = parse(y)
    elif op=="sub":
        x, y= args
        regs[ord(x)-ord("a")] -= parse(y)
    elif op=="mul":
        c+=1
        x,y = args
        regs[ord(x)-ord("a")] *= parse(y)
    elif op=="jnz":
        x, y=  args
        if parse(x)!=0:
            i+=parse(y)-1
    i+=1
print(c)

'''
set b 84
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
    
if part==silver:
    b = 84
    c = 84
else:
    b = 108400
    c = 125400

while True:
    set f 1
    set d 2
    f=1
        set e 2
        set g d
        mul g e
        sub g b
        jnz g 2
        set f 0
        sub e -1
        set g e
        sub g b
        jnz g -8
        sub d -1
        set g d
        sub g b
        jnz g -13
    ## if b is prime, f=1?
    for d in range(2, b):
        for e in range(2, b):    
            if d*e==b:
                f=0
    jnz f 2
    sub h -1
    if f==0:
        h+=1
    
    set g b
    sub g c
    g = b-c
    if b==c:
        break
    jnz g 2
    jnz 1 3 #break
    sub b -17
    b+=17

jnz 1 -23


if part==silver:
    b = 84
    c = 84
else:
    b = 108400
    c = 125400

for b in range(b, c+1, 17):
    f=1
    ## if b is prime, f=1?
    for d in range(2, b):
        for e in range(2, b):    
            if d*e==b:
                f=0
    if f==0:
        h+=1



number of primes between 108400 and 125400 (step 17)
'''
def sieve(n):
    pf = [True]*(n//2)
    pf[0]=False
    p = [2]
    for i,x in enumerate(pf):
        if x:
            s = i*2+1
            p.append(s)
            for y in range(i+s, len(pf), s):
                pf[y] = False
            if s > (n**0.5):
                for z in range(i+1, len(pf)):
                    if pf[z]==True:
                        p.append(z*2+1)
                break
    return p

primes = set(sieve(200_000))
c=0
for x in range(108400, 125401, 17):
    if not x in primes:
        c+=1
print(c)

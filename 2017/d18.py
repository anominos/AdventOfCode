l = []
with open("d18in.txt") as f:
    for x in f:
        l.append(x.strip())

def isNum(n):
    if n[0]=="-":
        return n[1:].isdigit()
    return n.isdigit()
def parse(a,d):
    if isNum(a):
        return int(a)
    return d[a]
from collections import defaultdict
def part1():
    d = defaultdict(int)
    i=0
    f = []
    while i < len(l):
        cir = l[i]
        instr, args = cir[:3], cir[3:].split()
        if instr == "snd":
            f.append(parse(args[0],d))
        elif instr == "set":
            a, b = args
            d[a]=parse(b,d)
        elif instr == "add":
            a, b = args
            d[a] +=parse(b,d)
        elif instr=="mul":
            a, b = args
            d[a]*=parse(b,d)
        elif instr=="mod":
            a,b = args
            d[a]%=parse(b,d)
        elif instr=="rcv":
            if parse(args[0])!=0:
                print(f[-1])
                break
        elif instr=="jgz":
            a,b = args
            if parse(a,d)>0:
                i+=parse(b,d)-1
        i+=1
def thread(link,init):
    d = defaultdict(int)
    d["p"]=init
    i=0
    f = []
    while i < len(l):
        cir = l[i]
        instr, args = cir[:3], cir[3:].split()
        if instr == "snd":
            f.append(parse(args[0], d))
        elif instr == "set":
            a, b = args
            d[a]=parse(b, d)
        elif instr == "add":
            a, b = args
            d[a] +=parse(b, d)
        elif instr=="mul":
            a, b = args
            d[a]*=parse(b, d)
        elif instr=="mod":
            a,b = args
            d[a]%=parse(b, d)
        elif instr=="rcv":
            if link==[]:
                yield f
                f=[]
            d[args[0]] = link.pop(0)

        elif instr=="jgz":
            a,b = args
            if parse(a,d)>0:
                i+=parse(b,d)-1
        i+=1

l1, l2 = [], []
t1 = thread(l1,0)
t2 = thread(l2,1)
c=0
while True:
    l2[:] = next(t1)
    l1[:]=[]
    if l1==[] and l2==[]:break
    l1[:] = next(t2)
    c+=len(l1)
    l2[:]=[]
    if l1==[] and l2==[]:break
print(c)


'''
import random
def thread(a):
    l=[]
    while True:
        if a==[]:
            l.append(random.randint(1,10))
            yield l
        print(a)
        l.append(random.randint(1,10))
    
'''
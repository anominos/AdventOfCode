import re,copy,sys,os
floors = []
with open("d11in.txt") as f:
    for x in f:
        floors.append(x.strip())

'''floors = """The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.""".split("\n")'''

for i, s in enumerate(floors):
    s = re.match("The \w+ floor contains (.+).",s).group(1)
    floors[i] = re.split(r"(?:and |, and |, )",s)
    if floors[i][0]=="nothing relevant":
        floors[i]=[]

gld=False
'''gld=True
gldin = """An elerium generator.
An elerium-compatible microchip.
A dilithium generator.
A dilithium-compatible microchip.""".lower()
for x in gldin.split("\n"):
    floors[0].append(x.strip("."))'''

for x in floors:
    for i,y in enumerate(x):
        f=y[2:].replace("-compatible", "")
        f = f.split()
        f[1]=f[1]=="microchip"
        x[i]=tuple(f)
floors = tuple(map(tuple,floors))
startFlr = copy.deepcopy(floors)

def getState(floor):
    t = sorted(floor)
    i=0
    paired = []
    chips = []
    gens = []
    while i<len(t):
        if i+1<len(t) and t[i][0]==t[i+1][0]:
            paired.append(t[i][0])
            i+=1
        else:
            if t[i][1]:
                chips.append(t[i][0])
            else:
                gens.append(t[i][0])
        i+=1
    return paired,chips,gens


def posGood(floors):
    for x in floors:
        a,b,c = getState(x)
        if b!=[] and (a!=[] or c!=[]):
            return False
    return True

def move(floors, curfloor,newfloor, items):
    items = list(map(floors[curfloor].index, items))
    items.sort(reverse=True)
    floors = list(list(i) for i in floors)
    for x in items:
        floors[newfloor].append(floors[curfloor].pop(x))
    return tuple(tuple(sorted(i)) for i in floors)
def getMoves(floors, elv,d):
    if d==-1 and all(i==() for i in floors[:elv]):
        return []
    moves = []
    p, c, g = getState(floors[elv])
    #moving a pair - doesnt matter which pair
    if p!=[]:
        moves.append((p[0],True))
        moves.append((p[0],False))
    for x in c:
        moves.append((x,True))
    for x in g:
        moves.append((x,False))
    for x in moves:
        yield (x,)
        for y in moves:
            if x<y:
                yield (x,y)
def formatted(s):
    c=0
    outt=""
    for elv,floors in s:
        outt+=str(c)+":\n"
        out=""
        for x in range(3,-1,-1):
            out += f"F{x}" if x!=elv else "E "
            out+=" "
            out += " ".join(map(lambda a:a[0][:2]+("m" if a[1] else "g"),floors[x]))
            out+="\n"
        outt+=out+"\n"
        c+=1
    return outt
def hash(elv, floors):
    h=""
    h+=str(elv)+"|"
    n=0
    d={}
    for floor in floors:
        p,c,g = getState(floor)
        l=[str(p)]
        for x in c:
            if x in d.keys():
                l.append(d[x]+"c")
            else:
                l.append(str(n)+"c")
                d[x]=str(n)
        for x in g:
            if x in d.keys():
                l.append(d[x]+"g")
            else:
                l.append(str(n)+"g")
                d[x]=str(n)
        h+=",".join(l)
        h+=";"
    return h
poss = [(0,tuple(tuple(sorted(i)) for i in floors))]
done = set()
c=0
loop=True
slvr = False
while loop:
    newPoss = []
    c+=1
    for elv,floors in poss:
        for dirr in [-1,1]:
            if 0<=(newfloor:=elv+dirr)<4:
                for x in getMoves(floors, elv,dirr):
                    newPos = move(floors, elv, newfloor, x)
                    if posGood(newPos) and not hash(newfloor,newPos) in done:
                        newPoss.append((newfloor,newPos))
                        done.add(hash(newfloor,newPos))
                        if newPos[0]==newPos[1]==newPos[2]==():
                            print("gold:" if gld else "silver:", c)
                            loop=False
                            break
                if loop==False:break
        if loop==False:break
    poss = tuple(set(newPoss))
    print(len(poss), c)

#print(formatted(poss))

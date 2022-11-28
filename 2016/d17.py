pcode = "gdjjyniy"
from hashlib import md5
def hsh(a):
    return md5(a.encode()).hexdigest()[:4]

states = [("", 0, 0)]# path, posx, posy

dirs = [[0,-1], [0,1],[-1,0],[1,0]]
dl = "UDLR"
p = True

while states!=[]:
    newStates = []
    for state in states:
        path, x, y = state
        if x==3 and y==3:
            if p:
                print(path)
                p=False
            l = len(path)
        else:
            doors = hsh(pcode+path)
            for i in range(4):
                if doors[i] in "bcdef":
                    newx, newy = x+dirs[i][0], y+dirs[i][1]
                    if 0<=newx < 4 and 0<= newy < 4:
                        newStates.append((path+dl[i], newx, newy))
    states = newStates[:]
print(l)
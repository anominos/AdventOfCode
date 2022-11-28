instruc = []
with open("d21in.txt") as f:
    for x in f:
        instruc.append(x.strip())

def rotate(l, i):
    if i < 0:
        i = len(l)+i
    return l[i:] + l[:i]

def run(a):
    a = list(a)
    for x in instruc:
        b = x.split()
        if b[0] == "swap":
            if b[1] == "position":
                i,j = map(int, (b[2], b[5]))
            else:
                i,j = map(a.index, (b[2], b[5]))
            a[i], a[j] = a[j], a[i]
        elif b[0]=="rotate":
            if b[1]=="based":
                i=a.index(b[-1])
                i+= i>=4
                i+=1
                a = rotate(a, -i)
            else:
                i=int(b[2])
                if b[1]=="right":
                    i = -i
                a = rotate(a, i)
        elif b[0] == "reverse":
            x, y = int(b[2]), int(b[4])
            a = [a[:x], a[x:y+1], a[y+1:]]
            a[1] = a[1][::-1]
            a = sum(a, [])
        else:
            x, y=  map(int, (b[2], b[-1]))
            a.insert(y, a.pop(x))
    return "".join(a)
def rev(a):
    a = list(a)
    for x in instruc[::-1]:
        b = x.split()
        if b[0] == "swap":
            if b[1] == "position":
                i,j = map(int, (b[2], b[5]))
            else:
                i,j = map(a.index, (b[2], b[5]))
            a[i], a[j] = a[j], a[i]
        elif b[0]=="rotate":
            if b[1]=="based":
                i =-1
                while a.index(b[-1]) !=i:
                    a = rotate(a, 1)
                    if a.index(b[-1])==i >=4:
                        break
                    i+=1
            else:
                i=int(b[2])
                if b[1]=="left":
                    i = -i
                a = rotate(a, i)
        elif b[0] == "reverse":
            x, y = int(b[2]), int(b[4])
            a = [a[:x], a[x:y+1], a[y+1:]]
            a[1] = a[1][::-1]
            a = sum(a, [])
        else:
            y, x=  map(int, (b[2], b[-1]))
            a.insert(y, a.pop(x))
    return "".join(a)
print("silver:",run("abcdefgh"))
print("gold:",rev("fbgdceah"))
dat = []
with open("d23in.txt") as f:
    for x in f:
        dat.append(x.strip())
import re

a = re.findall("[A-D]", "".join(dat[2:4]))
row = [None]*11
cols = list(zip(a[:4],a[4:]))
from collections import defaultdict, deque
q = deque([(row,cols,0)])
mn = 1e9
done = defaultdict(lambda:1e9)
done[tuple(row), tuple(cols)]=0
while q:
    r,c,e = q.popleft()
    if sum(c,tuple()) == tuple("AABBCCDD"):
        mn = min(mn, e)
    ff=True
    for x in range(4):
        char = "ABCD"[x]
        if c[x] == tuple() or c[x] == (char, ):
            y = (x+1)*2
            z = (x+1)*2
            f=True
            while f:
                f=False
                if y < len(r) and r[y] == None:
                    y+=1
                    f=True
                if z >= 0 and r[z] == None:
                    z-=1
                    f=True
            c[x] += (char, )
            if y < len(r) and r[y] == char:
                r[y] = None
                nwe = e+(abs((x+1)*2-y)+3-len(c[x]))*pow(10,ord(char)-ord("A"))
                if done[tuple(r),tuple(c)]>nwe:
                    q.append((r[:],c[:],nwe))
                    done[tuple(r),tuple(c)] = nwe
                r[y] = char
                ff=False
            if z >= 0 and r[z] == char:
                r[z] = None
                nwe = e+(abs((x+1)*2-z)+3-len(c[x]))*pow(10,ord(char)-ord("A"))
                if done[tuple(r),tuple(c)]>nwe:
                    q.append((r[:],c[:],nwe))
                    done[tuple(r),tuple(c)] = nwe
                r[z] = char
                ff=False
            c[x] = c[x][:-1]
    if ff:
        for i in range(len(c)):
            if c[i] != tuple() and not(c[i] == ("ABCD"[i],) or c[i] == ("ABCD"[i], "ABCD"[i])):
                a = c[i][0]
                c[i] = c[i][1:]
                s=set([2,4,6,8])
                y = (i+1)*2
                z = (i+1)*2
                f=True
                while f:
                    f=False
                    if y < len(r) and r[y] == None:
                        y+=1
                        f=True
                    if z >= 0 and r[z] == None:
                        z-=1
                        f=True
                for n in range(z+1,y):
                    if not(n in s):
                        r[n] = a
                        nwe = e+(abs((i+1)*2-n)+2-len(c[i]))*pow(10,ord(a)-ord("A"))
                        if done[tuple(r),tuple(c)]>nwe:
                            q.append((r[:],c[:],nwe))
                            done[tuple(r),tuple(c)] = nwe
                        r[n] = None
                c[i] = (a,)+c[i]
print(mn)







a = re.findall("[A-D]", "".join(dat[2:4]))
row = [None]*11
cols = list(zip(a[:4],"DCBA", "DBAC", a[4:]))
# from collections import defaultdict, deque
q = deque([(row,cols,0)])
mn = 1e9
done = defaultdict(lambda:1e9)
done[tuple(row), tuple(cols)]=0
while q:
    r,c,e = q.popleft()
    # print(sum(c,tuple()))
    if sum(c,tuple()) == tuple("AAAABBBBCCCCDDDD"):
        mn = min(mn, e)
    ff=True
    for x in range(4):
        char = "ABCD"[x]
        if c[x] == tuple() or any(c[x]==tuple(char*i) for i in range(1,5)):
            y = (x+1)*2
            z = (x+1)*2
            f=True
            while f:
                f=False
                if y < len(r) and r[y] == None:
                    y+=1
                    f=True
                if z >= 0 and r[z] == None:
                    z-=1
                    f=True
            c[x] += (char, )
            if y < len(r) and r[y] == char:
                r[y] = None
                nwe = e+(abs((x+1)*2-y)+5-len(c[x]))*pow(10,ord(char)-ord("A"))
                if done[tuple(r),tuple(c)]>nwe:
                    q.append((r[:],c[:],nwe))
                    done[tuple(r),tuple(c)] = nwe
                r[y] = char
                ff=False
            if z >= 0 and r[z] == char:
                r[z] = None
                nwe = e+(abs((x+1)*2-z)+5-len(c[x]))*pow(10,ord(char)-ord("A"))
                if done[tuple(r),tuple(c)]>nwe:
                    q.append((r[:],c[:],nwe))
                    done[tuple(r),tuple(c)] = nwe
                r[z] = char
                ff=False
            c[x] = c[x][:-1]
    if ff:
        for i in range(len(c)):
            rwe = set(c[i])
            if len(rwe)==1 and rwe.pop() == "ABCD"[i]:
                continue
            if c[i] != tuple():
                a = c[i][0]
                c[i] = c[i][1:]
                s=set([2,4,6,8])
                y = (i+1)*2
                z = (i+1)*2
                f=True
                while f:
                    f=False
                    if y < len(r) and r[y] == None:
                        y+=1
                        f=True
                    if z >= 0 and r[z] == None:
                        z-=1
                        f=True
                for n in range(z+1,y):
                    if not(n in s):
                        r[n] = a
                        nwe = e+(abs((i+1)*2-n)+4-len(c[i]))*pow(10,ord(a)-ord("A"))
                        if done[tuple(r),tuple(c)]>nwe:
                            q.append((r[:],c[:],nwe))
                            done[tuple(r),tuple(c)] = nwe
                        r[n] = None
                c[i] = (a,)+c[i]
    # print(len(q))
print(mn)
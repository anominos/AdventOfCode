from string import ascii_lowercase as alph
start = "hxbxwxba"
a = []
for x in start:
    a.append(alph.index(x))

ban = list(map(alph.index, "iol"))
c=0

while c < 2:
    for x in range(len(a)):
        if a[x] in ban:
            a[x]+=1
    t1=False
    for x in range(len(a)-3):
        if a[x]==a[x+1]-1 == a[x+2]-2:
            t1=True

    t2=0
    i=0
    while i < len(a)-1:
        if a[i] == a[i+1]:
            t2+=1
            i+=1
        i+=1
    t2 = t2 >= 2

    if t1 and t2:
        print(*map(alph.__getitem__, a), sep="")
        c+=1


    a[-1]+=1
    start = -1
    while a[start] == 26:
        a[start] = 0
        start-=1
        a[start]+=1



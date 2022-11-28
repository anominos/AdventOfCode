from hashlib import md5

dp2 = {}
dp1 = {}
def dohash2(a):
    if a in dp2.keys():
        return dp2[a]
    c = md5(a.encode()).hexdigest()
    for _ in range(2016):
        c = md5(c.encode()).hexdigest()
    dp2[a] = c
    return c
def dohash1(a):
    if a in dp1.keys():
        return dp1[a]
    c = md5(a.encode()).hexdigest()
    dp1[a] = c
    return c

def solve(dohash):
    salt = "qzyelonm"
    #salt = "abc"
    table = []
    for i in range(1,1001):
        b=[]
        h = dohash(salt+str(i))
        for y in "0123456789abcdef":
            if h.find(str(y*5))!=-1:
                b.append(y)
        table.append(b)

    i=0
    keys =[]
    while len(keys)<64:
        h = dohash(salt+str(i))
        for y in range(len(h)-2):
            if h[y:y+3]==h[y]*3:
                if h[y] in sum(table, []):
                    keys.append(i)
                break
        i+=1
        b=[]
        for y in "0123456789abcdef":
            if dohash(salt+str(1000+i)).find(str(y*5))!=-1:
                b.append(y)
        table.append(b)
        table = table[1:]
    return (keys[-1])
print("silver:", solve(dohash1))
print("gold:", solve(dohash2))
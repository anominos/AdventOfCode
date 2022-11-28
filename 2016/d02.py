d ={}
direction = [0,1]
for x in "URDL":
    d[x]=direction
    direction = direction[::-1]
    if direction[0]==0:
        direction[1]= -direction[1]

silver = ""
with open("d02in.txt", "r") as f:
    inp = f.readlines()
inp = map(lambda a:a.strip(), inp)

a = """789
456
123""".split("\n")
pos = [0,0]
b = """  1  
 234 
56789
 ABC
  D  """.split("\n")[::-1]
posg = [0,-2]
gold=""
for x in inp:
    for y in x:
        pos[0]+=d[y][0]
        pos[1]+=d[y][1]
        if not (-1<=pos[0]<=1 and -1<=pos[1]<=1):
            pos[0]-=d[y][0]
            pos[1]-=d[y][1]
        posg[0]+=d[y][0]
        posg[1]+=d[y][1]
        if not(-2<=posg[0]<=2 and -2<=posg[1]<=2 and sum(map(abs,posg))<=2):
            posg[0]-=d[y][0]
            posg[1]-=d[y][1]
    gold+=b[posg[1]+2][posg[0]+2]
    silver+=(a[pos[1]+1][pos[0]+1])
print("silver:",silver)
print("gold:",gold)
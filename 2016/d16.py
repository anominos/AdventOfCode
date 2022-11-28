def nextDat(a):
    b = a
    b = b[::-1]
    b = "".join(map(lambda a:'1' if a == '0' else '0', b))
    return a+ '0'+b

def checksum(a):
    b=""
    for x in range(0,len(a),2):
        b+=str(int(a[x]==a[x+1]))
    return b

init = "11110010111001001"
size = 272
'''
init = "10000"
size = 200
'''
while len(init)<size:
    init=nextDat(init)
dat = init[:size]
while len(dat)%2==0:
    dat = checksum(dat)
print("silver:", dat)
'''
bruteforce, works reasonable time
init = "11110010111001001"
size = 35651584//2

while len(init)<size:
    init=nextDat(init)
dat = init

cs = checksum(dat+"0")+checksum(dat[::-1][:-1])
cs = cs[:size]

while len(cs)%2==0:
    cs = checksum(cs)

print("gold:",dat)
'''
init = "11110010111001001"
initOnes = init.count("1")
iiOnes = len(init)-initOnes

size = 35651584

ii = "".join(map(lambda a:'1' if a == '0' else '0', init[::-1]))

n=0
l = len(init)
while l<size:
    l=l*2+1
    n+=1

joins = ""
for x in range(n):
    joins = nextDat(joins)
joins = list(map(int, joins))
print(len(joins))
chunk = 2**n

ans="1"
for x in range(chunk,size+1,chunk):
    i=0
    totOnes = 0
    paired, rem = divmod(x,36)
    totOnes+=sum(joins[i:i+(paired*2)])
    totOnes+=paired*17
    i+=paired*2
    remNum = init
    if rem>17:
        remNum+=str(joins[i])
        i+=1
    if rem>18:
        remNum+=ii
    remNum = remNum[:rem]
    totOnes+=remNum.count("1")
    ans+= str(int(1 - (totOnes%2)!=ans.count("0")%2))


print("gold:", ans[1:])
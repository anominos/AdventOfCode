dtot={}
d = {}
with open("d13in.txt") as f:
    for x in f:
        a, b = x.strip().split(": ")
        dtot[int(a)] = int(b)
        d[int(a)] = [0,1]
sev = 0
for n in range(max(dtot.keys())+1):
    if n in d.keys():
        if d[n][0]==0:
            sev+=n*dtot[n]
    for num, state in d.items():
        state[0]+=state[1]
        if dtot[num]==state[0]+1 or state[0]==0:
            state[1] = -state[1]
print(sev)

'''
find number n where:
for all x,y in dtot.items():
    (n+x)%((y-1)*2) != 0
'''

n=0
while True:
    for x, y in dtot.items():
        if (n+x)%((y-1)*2)==0:
            break
    else:
        break
    n+=1
print(n)
#bruteforce 3.3 secs


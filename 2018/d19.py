# dat =[]
# with open("d19in.txt") as f:
#     for x in f:
#         dat.append(x.strip().split())

# ip = int(dat[0][1])
# dat = dat[1:]
# from d16 import *
# d = [0]*6
# c=0
# d[0] = 1
# while d[ip] < len(dat):
#     line = dat[d[ip]]
#     line = [int(i) if i.isdigit() else i for i in line]
#     d = doLine(line, d)
#     d[ip]+=1
#     c+=1
#     print(line, d)
#     if c>50:break


n=954
s=0
for x in range(1,n+1):
    if n%x==0:
        s+=x
print(s)


## < 10494


r2 = 27
r2*=28
r2+=29
r2*=30
r2*=14
r2*=32

n+=r2
s=0
for x in range(1,int(n**0.5)+1):
    if n%x==0:
        s+=x
        s+=n//x
print(s)
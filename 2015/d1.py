with open("d1in.txt")as f:
    for x in f:
        s = x
print(s.count("(")-s.count(")"))
c=0
for i,x in enumerate(s):
    if x=="(":
        c+=1
    else:c-=1
    if c==-1:
        print(i+1)
        break
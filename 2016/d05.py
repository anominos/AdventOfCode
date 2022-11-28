import hashlib

ID ="wtnhxymk"
ind = 0
svr = ""
gld = list("________")
while "_" in gld:
    if (i:=str(hashlib.md5((ID+str(ind)).encode()).hexdigest()))[:5]=="00000":
        if len(svr)<8:svr+=i[5]
        if i[5].isdigit() and (j:=int(i[5]))<8:
            if gld[j]=="_":
                gld[j]=i[6]
        print(ind,i)
    ind+=1

print("silver:", svr)
print("gold:", "".join(gld))
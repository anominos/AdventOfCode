import re
ips=[]
with open("d07in.txt") as f:
    for x in f:
        ips.append(x.strip())

cs=0
cg = 0
pat = re.compile(r"(\[[^\]]*\])")
pat2 = re.compile(r"(.)(?!\1)(.)\2\1")
pat3 = re.compile(r"(?=((.)(?!\2)([^ ])\2))")
for x in ips:
    ins = re.findall(pat, x)
    good = True
    aba = []
    for y in ins:
        y = y[1:-1]
        if re.search(pat2, y):
            good = False
        aba+=re.findall(pat3,y)
    x = re.sub(pat, " ", x)
    for _,a,b in aba:
        if re.search(rf"{b}{a}{b}",x):
            cg+=1
            break

    if re.search(pat2, x) and good:
        cs+=1

print("silver:",cs)
print("gold:",cg)
pword = []
with open("d4in.txt") as f:
    for x in f.read().split("\n\n"):
        pword.append(x)

c=0
c2=0
valid = []
import re
for x in pword:
    x = x.replace("\n", " ")
    f=[False]
    f2=True
    for y in "byr iyr eyr hgt hcl ecl pid".split():
        if not y+":" in x:
            f2=False
    if f2:
        dat = re.findall(r"(...):(\S+)", x)
        f=[]
        for k,v in dat:
            if k=="cid":
                f.append(True)
            elif (k=="byr" and len(v)==4 and 1920<=int(v)<=2002):
                f.append(True)
            elif (k=="iyr" and len(v)==4 and 2010<=int(v)<=2020):
                f.append(True)
            elif (k=="eyr" and len(v)==4 and 2020<=int(v)<=2030):
                f.append(True)
            elif (k=="hgt"):
                if v[-2:]=="cm" and 150<=int(v[:-2])<=193:
                    f.append(True)
                elif v[-2:]=="in" and 59<=int(v[:-2])<=76:
                    f.append(True)
                else:
                    f.append(False)
            elif (k=="hcl" and re.match(r"#[0-9a-f]{6}$",v)):
                f.append(True)
            elif (k=="ecl" and v in "amb blu brn gry grn hzl oth".split()):
                f.append(True)
            elif (k=="pid" and re.match(r"[0-9]{9}$", v)):
                f.append(True)
            else:
                f.append(False)

    if f2:
        c+=1
    if all(f):
        c2+=1
        valid.append({})
        for y in x.split():
            valid[-1][y.split(":")[0]]=y.split(":")[1]
            

print(c)
print(c2)
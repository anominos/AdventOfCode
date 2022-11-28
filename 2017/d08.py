names = set()
instr = []
with open("d08in.txt") as f:
    for x in f:
        instr.append(x.strip().replace("inc", "+=").replace("dec", "-=")+" else 0")
        names.add(x.split()[0])
code = ", ".join(names) + "=" + ", ".join(["0"]*len(names))+"\n"
code+="\n".join(instr)
code+= "\nprint(max("+", ".join(names)+"))"
exec(code)

join = "maxx = max(maxx, "+", ".join(names)+")\n"
code = "maxx=0\n"+", ".join(names) + "=" + ", ".join(["0"]*len(names))+"\n"
code+=f"\n{join}".join(instr)
code+= "\nprint(maxx)"
exec(code)
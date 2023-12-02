import dataclasses, re

@dataclasses.dataclass
class Group:
    group_id: int
    group_name: str
    units: int
    hp: int
    weakness: list
    immune: list
    dmg: int
    dmg_type: str
    initiative: int

    def effective_power(self):
        return self.units * self.dmg

    def calc_dmg(self, other: "Group"):
        if self.dmg_type in other.immune:
            return 0
        elif self.dmg_type in other.weakness:
            return self.effective_power() * 2
        return self.effective_power()

    def deal_dmg_from(self, other: "Group"):
        raw_dmg = other.effective_power()
        if other.dmg_type in self.immune:
            return
        elif other.dmg_type in self.weakness:
            raw_dmg *= 2

        units_lost = raw_dmg // self.hp
        self.units -= units_lost
        self.units = max(0, self.units)
        return units_lost

    def __repr__(self):
        return f"Group({self.group_name} {self.group_id}: {self.units} units)"


with open("d24in.txt") as f:
    reindeer, infection = f.read().split("\n\n")

reindeer = reindeer.strip().split("\n")[1:]
infection = infection.strip().split("\n")[1:]

def process(s: list[str], name: str, boost=0) -> list[Group]:
    l = []
    for i, x in enumerate(s):
        m = re.match(r"(\d+) units each with (\d+) hit points (\([^\)]*\) )?with an attack that does (\d+) ([a-z]+) damage at initiative (\d+)", x)
        unit_num, hitpoints, defense_types, dmg,  dmg_type, initiative = m.groups()
        weaks = []
        immunes = []
        if defense_types is not None:
            weaks = re.findall("weak to ((?:[a-z]+, )*[a-z]+)[;\)]", defense_types)
            if weaks != []:
                weaks = weaks[0].split(", ")
            immunes = re.findall("immune to ((?:[a-z]+, )*[a-z]+)[;\)]", defense_types)
            if immunes != []:
                immunes = immunes[0].split(", ")

        l.append(Group(
            i, name, int(unit_num), int(hitpoints), weaks, immunes, int(dmg) + boost, dmg_type, int(initiative)
        ))
    return l

reindeer_groups = process(reindeer, "reindeer")
infection_groups = process(infection, "infection")

def turn(reindeer_groups, infection_groups, return_killed = False):
    ## target select
    attacks: list[tuple[Group, Group]] = []
    reindeers = sorted(reindeer_groups, key=lambda a: (a.effective_power(), a.initiative), reverse=True)
    targets = infection_groups[:]
    for source in reindeers:
        current_best = (-1, -1, -1, None)
        for consider in targets:
            dmg = source.calc_dmg(consider)
            if dmg > 0:
                current_best = max(current_best, (dmg, consider.effective_power(), consider.initiative, consider))
        if current_best[-1] is not None:
            attacks.append((source, current_best[-1]))
            targets.remove(current_best[-1])

    infections = sorted(infection_groups, key=lambda a: (a.effective_power(), a.initiative), reverse=True)
    targets = reindeer_groups[:]
    for source in infections:
        current_best = (-1, -1, -1, None)
        for consider in targets:
            dmg = source.calc_dmg(consider)
            if dmg > 0:
                current_best = max(current_best, (dmg, consider.effective_power(), consider.initiative, consider))
        if current_best[-1] is not None:
            attacks.append((source, current_best[-1]))
            targets.remove(current_best[-1])

    # attacks
    killed = 0
    for a, b in sorted(attacks, key=lambda a: a[0].initiative, reverse=True):
        killed += b.deal_dmg_from(a)

    reindeer_groups = [i for i in reindeer_groups if i.units > 0]
    infection_groups = [i for i in infection_groups if i.units > 0]
    if return_killed:
        return reindeer_groups, infection_groups, killed
    return reindeer_groups, infection_groups


while reindeer_groups != [] and infection_groups != []:
    reindeer_groups, infection_groups = turn(reindeer_groups, infection_groups)
bst = (sum(i.units for i in reindeer_groups + infection_groups))
print(bst)

def check(rg, ig):
    while rg != [] and ig != []:
        rg, ig, ks = turn(rg, ig, True)
        if ks == 0:
            return False
    if ig == []:
        return True
    return False

low = 0
high = bst

mn = bst
while low <= high:
    x = (low+high) // 2
    if check(process(reindeer, "reindeer", x), process(infection, "infection")):
        mn = min(mn, x)
        high = x - 1
    else:
        low = x + 1

rg, ig = process(reindeer, "reindeer", mn), process(infection, "infection")
while rg != [] and ig != []:
    rg, ig = turn(rg, ig)
bst = (sum(i.units for i in rg + ig))
print(bst)
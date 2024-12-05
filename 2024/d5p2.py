t=0
test = "C:/Users/tyler/Documents/advent of code/2024/test.txt"
inp = "C:/Users/tyler/Documents/advent of code/2024/inp.txt"
with open(inp, "r") as f:
    f = f.readlines()

ordering_rules = []
update_pg_numbers = []
for line in f:
    line = line.strip()
    if "|" in line:
        ordering_rules.append(line)
    else:
        update_pg_numbers.append(line.split(","))
update_pg_numbers.pop(0)

order = []
i = 0
for rule in ordering_rules:
    rule = rule.split("|")
    ordering_rules[i] = rule
    i+=1

correctly_ordered = []
for update in update_pg_numbers:
    visited = []
    correctly_ordered_bool = True
    for page in update:
        for rule in ordering_rules:
            if rule[0] not in update: continue
            if rule[0] not in visited and rule[1] in visited:
                correctly_ordered_bool = False 
                break
        visited.append(page)
        if correctly_ordered_bool == False: break

    if correctly_ordered_bool:
        correctly_ordered.append(update)

incorrectly_ordered = []
for update in update_pg_numbers:
    if update in correctly_ordered: continue
    incorrectly_ordered.append(update)

befores = []
afters = []
for rule in ordering_rules:
    befores.append(rule[0])
    afters.append(rule[1])

counts = {}
for x in befores:
    counts[x] = befores.count(x)

for x in afters:
    if x not in counts.keys():
        counts[x] = 0

counts = dict(sorted(counts.items(),key=lambda x: x[1], reverse=True))
ordered = []
print(counts)
for x in incorrectly_ordered:
    new = []
    for key in list(counts.keys()):
        for y in x:
            if y == key:
                new.append(y)
    ordered.append(new)

for x in ordered:
    t+=int(x[len(x)//2])
print(t)
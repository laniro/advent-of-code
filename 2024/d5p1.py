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

print(correctly_ordered)

for update in correctly_ordered:
    middle = len(update)//2
    t+=int(update[middle])
print(t)
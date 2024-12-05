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


rules = []
for i in range(100):
    rules.append([])
for i in ordering_rules:
    rules[int(i[1])].append(i[0])

# rules is a list of numbers. At index x is stored the list of numbers that must be printed before x.

#for x in range(len(rules)):
 #   print(x, rules[x])

correcteds = []
for update in incorrectly_ordered:
    ordered = []
    pages = update
    while len(pages) != 0:
        page = pages[0]
        # if everything from the rules list in our new list, then we add the current page to the new list
        # however, we cannot do this now as the current rules would require numbers that may not be in the update
        # Example: The ruleset for '61' requires ['97','47','75']. For the update ['61', '13', '29'], these numbers will never
        # be in the ordered list no matter how many times we iterate. Therefore, 61 never gets added.
        # To solve this, we must find the intersection of the ruleset for the current page, and the update.
        # In the case of '61', the intersection is [ ], so '61' would be added
        rules_intersect = list(set(update).intersection(rules[int(page)]))
        for rule in rules_intersect:
            # if all befores in list: add current page to list
            # if not, add current page back to pages, break out of loop to go to next page
            # finally, remove the current page from the queue (pages)
            if rule in ordered:
                continue
                # great, continue checking
            elif rule not in ordered: # should be an else, but using a elif for now to make code comprehensible
                pages.append(page)
                break
        else:
            ordered.append(page)
        pages.pop(0)
    correcteds.append(ordered)

for update in correcteds:
    t+=int(update[len(update)//2])
print(t)
with open("2023/in.txt","r") as f:
    f = f.readlines()

f = [x.strip().split() for x in f]
f = [list(map(int,x)) for x in f]

def findNextNum(depth, lst):
    depth += 1
    differences = []
    for i in range(len(lst)-1):
        differences.append(lst[i+1]-lst[i])
    for i in range(len(differences)-1):
        if differences[i] != differences[i+1]:
            break
    else: # Deepest depth, all differences are the same so no break in for loop
        return lst[len(lst)-1] + differences[0]
    # Differences are different, so for loop breaks. Can go further
    return lst[len(lst)-1] + findNextNum(depth, differences)

t = 0
for line in f:
    t+=findNextNum(0,line)
print(t)
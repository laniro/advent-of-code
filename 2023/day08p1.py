with open("2023/in.txt","r") as f:
    f = [x.strip() for x in f.readlines() if x != '\n']

directions = f[0]
f = [tuple(x.split(" = ")) for x in f[1:]]
f = {i: tuple(l[1:-1].split(", ")) for i, l in f}
location = 'AAA'

c=1
while True:
    for i in directions:
        if i == 'L':
            location = f[location][0]
        else:
            location = f[location][1]
        if location == 'ZZZ':
            break
        else:
            c += 1
    else: continue
    break

print(c)
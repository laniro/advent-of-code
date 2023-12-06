with open("2023/in.txt","r") as f:
    f = f.readlines()

times = [int(x.strip()) for x in f[0].split(":")[1].split()]
records = [int(x.strip()) for x in f[1].split(":")[1].split()]

rbs = []

for i, t in enumerate(times):
    rb = 0
    dists = []
    for heldtime in range(t):
        dists.append((t-heldtime)*heldtime)
    for dist in dists:
        if dist > records[i]:
            rb+=1
    rbs.append(rb)

i = 1
for x in rbs:
    i*=x
print(i)
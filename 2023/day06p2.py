with open("2023/in.txt","r") as f: 
    f = f.readlines()
time = int(''.join([x.strip() for x in f[0].split(":")[1]]))
record = int(''.join([x.strip() for x in f[1].split(":")[1]]))

rb = 0
for heldtime in range((time//2)+1):
    if (time-heldtime)*heldtime > record:
        rb+=2

print(rb)
with open("2023/in.txt","r") as f:
    f = f.readlines()

seeds = [int(x.strip()) for x in f[0].split(": ")[1].split(" ")]
maps = [i.strip() for i in f if 'map' in i] 
md = {}
gg = 0
import threading
import time
run = True
def tt():
    global run
    global gg
    t=0
    while run:
        print("Working for",t,"seconds\n",gg)
        time.sleep(0.5)
        t+=0.5

threading.Thread(target=tt).start()

for i in maps:
    md[i[:-1]] = []

currentMap = ''
for line in f[2:]:
    line = line.strip()
    if 'map' in line:
        currentMap = line[:-1]
    else:
        if line != '': 
            md[currentMap].append(line.split(" "))

print(md)

for mk in md:
    gg+=1
    mg = md[mk]
    map = []
    newSeeds = []
    for m in mg:
        ds = int(m[0])
        ss = int(m[1])
        r = int(m[2])
        for i in range(r):
            if ss+i in seeds:
                map.append((ss+i,ds+i))
    
    for seed in seeds:
        for item in map:
            if seed == item[0]:
                break
        else:
            map.append((seed,seed))
    
    for item in map:
        gg = item
        newSeeds.append(item[1])
    seeds = newSeeds
    print(seeds)

print(min(seeds))
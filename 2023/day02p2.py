power = 0
t = 0
with open("2023/in.txt","r") as f:
    for line in f.readlines():
        line = line.strip()

        total = {
            "red":0,
            "green":0,
            "blue":0
        }

        colonIndex = line.find(":")
        gameNum = int(line[5:colonIndex])
        line = line[colonIndex+2:].split("; ")
        
        for set in line:
            set = set.split(", ")
            for cubes in set:
                for colour in total:
                    try: colourIndex = cubes.index(str(colour))
                    except: pass
                    else:
                        total[colour] = max(total[colour], int(cubes[:colourIndex-1]))
        
        power = total["red"]*total["green"]*total["blue"]
        t += power

print(t)
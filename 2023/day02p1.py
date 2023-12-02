possibleGames = []

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
        
        if total["red"] > 12:
            continue
        elif total["green"] > 13:
            continue
        elif total["blue"] > 14:
            continue
        else:
            possibleGames.append(gameNum)

t = 0
print(possibleGames)
for item in possibleGames:
    t += item
print(t)
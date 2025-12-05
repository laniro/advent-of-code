def one():
    with open(0) as f:
        f = f.readlines()
    ranges = []
    for line in f:
        line = line.strip()
        if line == "":
            break
        line = line.split("-")
        ranges.append((int(line[0]),int(line[1])))

    ingredients = []
    t=0
    for line in f:
        line = line.strip()
        if "-" in line or line == "": continue
        for tup in ranges:
            if int(line) >= tup[0] and int(line) <= tup[1] and int(line) not in ingredients:
                ingredients.append(int(line))
                t+=1

    return t


def two():
    with open(0) as f:
        f = f.readlines()
    ranges = []
    for line in f:
        line = line.strip()
        if line == "":
            break
        line = line.split("-")
        ranges.append([int(line[0]),int(line[1])])
    ranges = sorted(ranges, key=lambda x : x[0])

    for i in range(len(ranges)): # removing duplicates
        try:
            if ranges[i][0] == ranges[i+1][0]: # lower bound the same
                if ranges[i][1] >= ranges[i+1][1]: # removing tuple with lower upper bound
                    ranges.pop(i+1)
                else:
                    ranges.pop(i)
        except:
            pass

    for i in range(len(ranges)): 
        try:
            if ranges[i][1] > ranges[i+1][1]: # upper > next upper -> swap uppers
                temp = ranges[i][1]
                ranges[i][1] = ranges[i+1][1]
                ranges[i+1][1] = temp
            
            if ranges[i][1] >= ranges[i+1][0]: # upper >= next lower -> upper = next lower - 1
                ranges[i][1] = ranges[i+1][0]-1
        except:
            pass

    t=0
    for r in ranges:
        t += r[1] - r[0] + 1
    return t

print(two())
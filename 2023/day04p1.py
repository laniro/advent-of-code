import math
t=0
with open("2023/in.txt","r") as f:
    for line in f.readlines():
        n = 0
        line = line[line.index(":")+2:].strip()
        line = line.split(" | ")
        for item in range(len(line)):
            line[item] = line[item].split(" ")
            line[item].sort()
            for i in range(line[item].count('')):
                line[item].pop(0)
        for item in line[0]:
            if item in line[1]:
                n += 1
        t += math.floor(2**(n-1))
print(t)
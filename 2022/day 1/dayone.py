file = open("day 1\dayone.txt", "r")
temp = 0
max1 = 0
max2 = 0
max3 = 0

for line in file:
    if line == '\n':
        if temp > max1:
            max3 = max2
            max2 = max1
            max1 = temp
            temp = 0
        elif temp > max2:
            max3 = max2
            max2 = temp
            temp = 0
        elif temp > max3:
            max3 = temp
            temp = 0
        else:
            temp = 0
    else:
        temp += int(line)
file.close()

print(max1+max2+max3)
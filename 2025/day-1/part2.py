dial = 50
zeroes = 0

with open("input.txt") as f:
    for line in f.readlines():
        instruction = line.strip()
        dire = 1
        match instruction[0]:
            case 'L':
                dire = -1
            case 'R':
                dire = 1

        for i in range(int(instruction[1::])):
            dial += dire
            dial %= 100

            if dial == 0:
                zeroes += 1
        
print(zeroes)
dial = 50
zeroes = 0

with open("input.txt") as f:
    for line in f.readlines():
        instruction = line.strip()
        match instruction[0]:
            case 'L':
                dial = dial - int(instruction[1:])
                dial = dial % 100
            case 'R':
                dial = dial + int(instruction[1:])
                dial = dial % 100

        if dial == 0:
            zeroes += 1

print(zeroes)
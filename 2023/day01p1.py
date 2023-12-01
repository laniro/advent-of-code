total = 0
with open("2023/in.txt","r") as f:
    for line in f.readlines():
        for char in line.strip():
            if ord(char) < 58:
                firstDigit = char
                break
        for char in line.strip()[-1::-1]:
            if ord(char) < 58:
                lastDigit = char
                break
        total += int(firstDigit+lastDigit)
print(total)
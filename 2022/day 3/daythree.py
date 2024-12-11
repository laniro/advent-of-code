f = open("day 3\daythree.txt","r").read().split()

sp = 0
n = 0
for i in range(len(f)//3):
    for i in range(3):
        try:
            x = f[0+n]
            y = f[1+n]
            z = f[2+n]
        except:
            break
    n += 3
    for char in x:
            if char in y and char in z:
                if ord(char) > 90:
                    sp += ord(char)-96
                else:
                    sp += ord(char)-38
                break

print(sp)
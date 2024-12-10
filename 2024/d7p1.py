import math
test = "C:/Users/tyler/Documents/advent of code/2024/test.txt"
inp = "C:/Users/tyler/Documents/advent of code/2024/inp.txt"
file_path = inp
with open(file_path, "r") as f:
    f = f.readlines()
f = [x.split() for x in f]
for x in f:
    x[0] = x[0].strip(":")
for i in range(len(f)):
    f[i] = (f[i][0], list(f[i][1:]))

t = 0
for tup in f:
    print(tup)
    test_value = int(tup[0])
    operands = [int(x) for x in tup[1]]
    gaps = len(operands)-1
    for i in range(gaps):
        operands.insert(2*i+1, '')
    
    for i in range(2**gaps): # permutations
        binary = list(f'{i:32b}')[::-1]
        operators = ['' for x in binary]
        for x in range(len(binary)):
            if binary[x] == '1':
                operators[x] = '*'
            else:
                operators[x] = '+'
        
        operator = 0
        for j in range(len(operands)):
            if operands[j] == '' or operands[j] == '+' or operands[j] == '*':
                operands[j] = operators[operator]
                operator +=1
        mode = '+'
        acc = 0
        for x in operands:
            if type(x) == int:
                match mode:
                    case '+':
                        acc += x
                    case '*':
                        acc *= x
            else:
                match x:
                    case '+':
                        mode = '+'
                    case '*':
                        mode = '*'
        if acc == test_value:
            t += test_value
            break
print(t)
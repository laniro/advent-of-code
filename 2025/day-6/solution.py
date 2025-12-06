def one():
    with open(0) as f:
        f = f.readlines()
    f = [line.split() for line in f]
    f = [list(x) for x in zip(*f)]

    r=0
    for eq in f:
        match eq[-1]:
            case "*":
                t=1
                for x in eq[:-1]:
                    t*=int(x)
            case "+":
                t = sum(map(int,eq[:-1]))
        r+=t
    return r

def two():
    with open(0) as f:
        f = f.readlines()
    f = [x.strip("\n") for x in f] # removes newline characters
    f = [[y for y in x] for x in f] # splits into 2d list of characters
    f = [x[::-1] for x in f] # reverses nested lists
    f = [list(x) for x in zip(*f)] # transposes 2d list
    f = [''.join(x) for x in f] # flattens 2d list into list of strings

    operands = []
    r=0
    for num in f:
        if "*" in num or "+" in num:
            operands.append(num[:-1])
            r += do_equation(operands, num[-1])
            operands = []
        else:
            operands.append(num)
    return r

def do_equation(operands, operator):
    operands = [int(x) for x in operands if x.strip() != ''] # removing whitespace
    match operator:
        case "*":
            t=1
            for x in operands: 
                t *= x
        case "+":
            t = sum(operands)
    return t

print(two())
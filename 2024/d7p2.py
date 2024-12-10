import numpy as np
import multiprocessing as mp

def test_all_perms(test_value, operands, gaps,index,file_len):
    print(f"Starting {index}")
    for i in range(3**gaps): # permutations
        ternary = list(np.base_repr(i,base=3,padding=32))[::-1] # need this in ternary
        operators = ['' for x in ternary]
        for x in range(len(ternary)):
            if ternary[x] == '2':
                operators[x] = '*'
            elif ternary[x] == '1':
                operators[x] = '+'
            else:
                operators[x] = '||'
        
        operator = 0
        for j in range(len(operands)):
            if operands[j] == '' or operands[j] == '+' or operands[j] == '*' or operands[j] == '||':
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
                    case '||':
                        acc = int(str(acc) + str(x))
            else:
                match x:
                    case '+':
                        mode = '+'
                    case '*':
                        mode = '*'
                    case '||':
                        mode = '||'
        if acc == test_value:
            print(f"{index} out of {file_len}... MATCH")
            return test_value
    print(f"{index} out of {file_len}... No Match")
    return 0

if __name__ == "__main__":
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
    p = mp.Pool()
    args = []
    for tup in f:
        test_value = int(tup[0])
        operands = [int(x) for x in tup[1]]
        gaps = len(operands)-1
        for i in range(gaps):
            operands.insert(2*i+1, '')
        
        args.append([test_value, operands, gaps,f.index(tup)+1,len(f)])

    res = p.starmap(test_all_perms,args)
    for r in res:
        t+=r
    print(t)
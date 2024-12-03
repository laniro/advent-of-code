import os
t=0
file_path = "C:/Users/tyler/Documents/advent of code/2024/inp.txt"

def check_safe(list):
    increasing = None
    for i in range(1,len(list)):
        diff = int(list[i-1]) - int(list[i])
        if diff > 0 and increasing == None:
            increasing = True
        elif diff < 0 and increasing == None:
            increasing = False
        
        if increasing == True and diff < 0:
            print("Unsafe", list)
            return False
        elif increasing == False and diff > 0:
            print("Unsafe", list)
            return False

        if abs(diff) not in [1,2,3]:
            print("Unsafe", list)
            return False
    else:
        print("Safe", list)
        return True
    

if os.path.exists(file_path):
    print('The file exists')
    with open(file_path, 'r', encoding='utf-8') as f:
        f = f.readlines()
    for line in f:
        line = line.split()
       
        if check_safe(line):
            t+=1
        else:
            for i in range(len(line)):
                new_line = []
                for x in range(len(line)):
                    if x != i:
                        new_line.append(line[x])
                if check_safe(new_line) == True:
                    t+=1
                    break
    print(t)
else:
    print('The specified file does NOT exist')


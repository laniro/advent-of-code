import os
t=0
file_path = "C:/Users/tyler/Documents/advent of code/2024/inp.txt"
if os.path.exists(file_path):
    print('The file exists')
    with open(file_path, 'r', encoding='utf-8') as f:
        f = f.readlines()
    for line in f:
        line = line.split()
        increasing = None
        for i in range(1,len(line)):
            diff = int(line[i-1]) - int(line[i])
            if diff > 0 and increasing == None:
                increasing = True
            elif diff < 0 and increasing == None:
                increasing = False
            
            if increasing == True and diff < 0:
                print("Unsafe", line)
                break
            elif increasing == False and diff > 0:
                print("Unsafe", line)
                break

            if abs(diff) not in [1,2,3]:
                print("Unsafe", line)
                break
        else:
            t+=1
    print(t)
else:
    print('The specified file does NOT exist')
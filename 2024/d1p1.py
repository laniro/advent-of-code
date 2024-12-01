import os
t=0
file_path = input("File Path: ")
if os.path.exists(file_path):
    print('The file exists')
    list1 = []
    list2 = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        line = line.split()
        list1.append(int(line[0]))
        list2.append(int(line[1]))
    
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        distance = abs(list1[i] - list2[i])
        t+= distance

    print(t)
else:
    print('The specified file does NOT exist')

input()
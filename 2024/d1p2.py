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
    for i in list1:
        count_in_second_list = list2.count(i)
        t += i * count_in_second_list

    print(t)
else:
    print('The specified file does NOT exist')

input()
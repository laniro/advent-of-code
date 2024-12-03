import os
import re
t=0
file_path = "C:/Users/tyler/Documents/advent of code/2024/inp.txt"
if os.path.exists(file_path):
    print('The file exists')
    with open(file_path, 'r', encoding='utf-8') as f:
        f = f.readlines()
        f = ''.join(f)
        i_hate_regex = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)',f)
        for instruction in i_hate_regex:
            operators = re.findall('[0-9]{1,3}', instruction)
            t += int(operators[0]) * int(operators[1])
    print(t)

else:
    print('The specified file does NOT exist')
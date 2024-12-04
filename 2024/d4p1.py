import os
import re
t=0
file_path = "C:/Users/tyler/Documents/advent of code/2024/inp.txt"
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        f = f.readlines()
    rows = f
    columns = list(zip(*f))
    rows = [''.join(row.strip()) for row in rows]
    columns = [''.join(''.join(column).strip()) for column in columns]
    for row in rows:
        t += len(re.findall('XMAS', row, re.IGNORECASE))
        t += len(re.findall('SAMX', row, re.IGNORECASE))
    for column in columns:
        t += len(re.findall('XMAS', column, re.IGNORECASE))
        t += len(re.findall('SAMX', column, re.IGNORECASE))
    for i in range(len(rows)):
        for j in range(len(columns)):
            if rows[i][j] != 'X': continue
            if i+3 < len(rows[i]) and j+3 < len(columns[i]):
                if rows[i+1][j+1] == 'M' and rows[i+2][j+2] == 'A' and rows[i+3][j+3] == 'S':
                    t+=1
            if i-3 >= 0 and j+3 < len(columns[i]):
                if rows[i-1][j+1] == 'M' and rows[i-2][j+2] == 'A' and rows[i-3][j+3] == 'S':
                    t+=1
            if i-3 >= 0 and j-3 >= 0:
                if rows[i-1][j-1] == 'M' and rows[i-2][j-2] == 'A' and rows[i-3][j-3] == 'S':
                    t+=1
            if i+3 < len(rows[i]) and j-3 >= 0:
                if rows[i+1][j-1] == 'M' and rows[i+2][j-2] == 'A' and rows[i+3][j-3] == 'S':
                    t+=1

    print(t)
else:
    print('The specified file does NOT exist')
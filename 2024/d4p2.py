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
    for i in range(len(rows)):
        for j in range(len(columns)):
            if i+2 < len(rows[i]) and j+2 < len(columns[i]):
                if rows[i][j] == 'M' and rows[i+1][j+1] == 'A' and rows[i+2][j+2] == 'S':
                    # M.x
                    # .A.
                    # x.S
                    if rows[i+2][j] == 'M' and rows[i][j+2] == 'S':
                        # M.M
                        # .A.
                        # S.S
                        t+=1
                    if rows[i][j+2] == 'M' and rows[i+2][j] == 'S':
                        # M.S
                        # .A.
                        # M.S
                        t+=1

                if rows[i][j] == 'S' and rows[i+1][j+1] == 'A' and rows[i+2][j+2] == 'M':
                    # S.x
                    # .A.
                    # x.M
                    if rows[i+2][j] == 'M' and rows[i][j+2] == 'S':
                        # S.M
                        # .A.
                        # S.M
                        t+=1
                    if rows[i][j+2] == 'M' and rows[i+2][j] == 'S':
                        # S.S
                        # .A.
                        # M.M
                        t+=1

    print(t)
else:
    print('The specified file does NOT exist')
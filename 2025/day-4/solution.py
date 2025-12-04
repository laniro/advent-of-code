def add(char):
    if char == '@': 
        return 1
    else: 
        return 0

def get_adjacent_rolls(x,y,g):
    r = 0
    if x-1 != -1 and y-1 != -1:
        r += add(g[y-1][x-1])

    if y-1 != -1:
        r += add(g[y-1][x])

    try:
        if y-1 != -1:
            r += add(g[y-1][x+1])
    except: pass
    
    if x-1 != -1:
        r += add(g[y][x-1])

    try:
        r += add(g[y][x+1])
    except: pass

    try:
        if x-1 != -1:
            r += add(g[y+1][x-1])
    except: pass

    try:
        r += add(g[y+1][x])
    except: pass
    
    try:
        r += add(g[y+1][x+1])
    except: pass
    
    return r

SHOW_GRID = False

import copy
def one():
    with open(0) as f:
        rolls = 0
        grid = [[y for y in x.strip()] for x in f.readlines()]
        new = [line[:] for line in grid]
        for i, line in enumerate(grid):
            for j,char in enumerate(line):
                if char == '@' and get_adjacent_rolls(j,i,grid) < 4:
                    rolls += 1
                    new[i][j]= 'x'

        if SHOW_GRID:
            for line in new:
                for char in line:
                    print(char,end='')
                print('')
    return rolls


def remove_rolls(grid):
    rolls = 0
    new = [line[:] for line in grid]
    for i, line in enumerate(grid):
        for j,char in enumerate(line):
            if char == '@' and get_adjacent_rolls(j,i,grid) < 4:
                rolls += 1
                new[i][j] = 'x'
    
    if SHOW_GRID:
        for y, line in enumerate(new):
            for x, char in enumerate(line):
                print(char,end='')
                if char == 'x':
                    new[y][x] = '.'
            print('')

    if rolls == 0: return 0
    else: return remove_rolls(new) + rolls

def two():
    with open(0) as f:
        grid = [[y for y in x.strip()] for x in f.readlines()]
        return remove_rolls(grid)

print(two())
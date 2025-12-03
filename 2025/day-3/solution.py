def best_char_one(string, start_index):
    for char in range(9,0,-1):
        index = string.find(str(char), start_index)
        if index != -1:
            return index

def one():
    t=0 
    with open(0) as f:
        for line in f.readlines():
            line = line.strip()
            i = best_char_one(line[:len(line)-1], 0)
            j = best_char_one(line, i+1)
            t+=int(line[i]+line[j])
    return t


def best_char(string, start_index, end_index):
    for char in range(9,0,-1):
        index = string.find(str(char), start_index, end_index+1)
        if index != -1:
            return index

def two():
    t=0
    with open(0) as f:
        for line in f.readlines():
            line = line.strip()
            s = ""
            index = 0
            for i in range(12,0,-1):
                index = best_char(line, index, len(line)-i)
                s += line[index]
                index += 1
            t+=int(s)
    return t

print(two())
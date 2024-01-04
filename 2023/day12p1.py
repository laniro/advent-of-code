with open("2023/test.txt","r") as f:
    f = [x.strip() for x in f.readlines()]

def compress(lst):
    clst = []
    p = None
    t=1
    for c in lst:
        if p == c:
            t+=1
        else:
            if p != None:
                clst.append((p*t))
                t=1
        p = c
    clst.append(p*t)
    return clst
            


for line in f:
    r,l = line.split()
    l = [int(x) for x in l.split(",")]
    r = [x for x in r]

    while True:
        if r[0] == '.' or r[-1] == '.':
            if r[0] == '.':
                r.pop(0)
            if r[-1] == '.':
                r.pop(-1)
        else:
            break
        
    cr = compress(r)
    
    if cr[0] == '#'*l[0]:
        print(cr,"0",l)
    if cr[-1] == '#'*l[-1]:
        if r[-l[-1]-1] == '.':
            cr.pop(-1)
            cr.pop(-1)
    print(cr)
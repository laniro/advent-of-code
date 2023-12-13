with open("2023/in.txt","r") as f:
    f = [x.strip() for x in f.readlines()]
rows = []
columns = []
for i, row in enumerate(f):
    if "#" not in row:
        rows.append(i)

cs = [''.join(x) for x in list(zip(*f))]

for i, column in enumerate(cs):
    if "#" not in column:
        columns.append(i)

t = 1
d = {}
for i,r in enumerate(f):
    for j,x in enumerate(r):
        if x == "#":
            d[t] = (j+1,i+1)
            t+=1

exC = 1000000 # How much the universe is expanding by
for k in d:
    v = d[k]
    nx, ny = 0, 0
    for c in columns:
        if v[0] > c:
            ny += exC-1
    for r in rows:
        if v[1] > r:
            nx += exC-1
    d[k] = (v[0]+ny, v[1]+nx)

def tupSub(tup1, tup2): # tuple subtraction
    return tuple(abs(x-y) for x, y in zip(tup1, tup2))

tl = 0
for g in d:
    for galaxy in d:
        if g >= galaxy:
            continue
        ts = tupSub(d[g],d[galaxy])
        tl += ts[0] + ts[1]
print(tl)
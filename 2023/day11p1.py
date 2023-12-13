with open("2023/in.txt","r") as f:
    f = [x.strip() for x in f.readlines()]
dots = ["." for i in range(len(f[0]))]
rows = []
columns = []

for i, row in enumerate(f):
    if "#" not in row:
        rows.append(i)

cs = [''.join(x) for x in list(zip(*f))]

for i, column in enumerate(cs):
    if "#" not in column:
        columns.append(i)

eu = [list(x) for x in f]

for i,x in enumerate(rows):
    eu.insert(i+x,dots)

for i,row in enumerate(eu):
    for j, x in enumerate(row):
        if j in columns:
            eu[i][j] = ".."


eu = [''.join(x) for x in eu]
eu = [list(x) for x in eu]
t = 1
d = {}
for i,r in enumerate(eu):
    for j,x in enumerate(r):
        if x == "#":
            eu[i][j] = str(t)
            d[t] = (j,i)
            t+=1

def tupSub(tup1, tup2):
    return tuple(abs(x-y) for x, y in zip(tup1, tup2))

tl = 0

for g in d:
    for galaxy in d:
        if g >= galaxy:
            continue
        ts = tupSub(d[g],d[galaxy])
        tl += ts[0] + ts[1]
print(tl)
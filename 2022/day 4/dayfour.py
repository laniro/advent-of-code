t = 0
f = open("day 4\dayfour.txt","r").read().split()
for item in f:
    x,y = item.split(",")
    x,y = x.split("-"), y.split("-")

    a, b = set(range(int(x[0]), int(x[1])+1)), set(range(int(y[0]), int(y[1])+1))
    if a.isdisjoint(b) == False or b.isdisjoint(a) == False:
        t+=1
print(t)

# Done in 15;3/15;2

# Rewritten; Original below
"""t = 0
f = open("day 4\dayfour.txt","r").read().split()
for item in f:
    xz, yz = [], []
    x,y = item.split(",")
    x,y = x.split("-"), y.split("-")
    for i in range(int(x[0]), int(x[1])+1):
        xz.append(i)
    for i in range(int(y[0]), int(y[1])+1):
        yz.append(i)
    
    a, b = set(xz), set(yz)
    if a.isdisjoint(b) == False or b.isdisjoint(a) == False:
        t+=1
print(t)

# Done in 15;3/15;2"""
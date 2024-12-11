f = open("day 5\dayfive.txt")

mydict = {1: ['P','Z','M','T','R','C','N'],
          2: ['Z','B','S','T','N','D'], 
          3: ['G','T','C','F','R','Q','H','M'],
          4: ['Z','R','G'],
          5: ['H','R','N','Z'],
          6: ['D','L','Z','P','W','S','H','F'],
          7: ['M','G','C','R','Z','D','W'],
          8: ['Q','Z','W','H','L','F','J','S'],
          9: ['N','W','P','Q','S']}

for item in f:
    x = []
    l = item.split()
    count, orig, target = int(l[1]), int(l[3]), int(l[5])
    
    for i in range(count):
        x.append(mydict[orig][0])
        mydict[orig].remove(mydict[orig][0])

    x.reverse()

    for item in x: mydict[target].insert(0,item)

aaa,s = [], ''
for item in mydict:
    n = mydict[item][0]
    aaa.append(n)
for i in aaa: s += i

print(s)
f = open("day 6\daysix.txt", "r").read()
import re

n = 14
x = []

p = set(range(2,n+1))

for i in f:
    x.append(i)
    if len(x) == 15:
        x.pop(0)
        n+=1
        s = ''
        for item in x:
            s+=item
        a = []
        for item in s:
            a.append(len(re.findall(item,s)))
            if len(re.findall(item,s)) > 1:
                break
        if p.isdisjoint(a):
            print(n)
            exit()
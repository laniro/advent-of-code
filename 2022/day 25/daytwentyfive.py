t = 0

for item in open("day 25\daytwentyfive.txt","r"):
    n=0
    SNAFUnum=0
    SNAFUnumlist = list(item.strip())
    l = len(SNAFUnumlist)
    for i in SNAFUnumlist[::-1]:
        if i == '=':
            SNAFUnum -= 2*(5**n)
        elif i == '-':
            SNAFUnum -=5**n
        else:
            SNAFUnum += int(i)*(5**n)
        n+=1
        if n > l:
            break
    t+=SNAFUnum

f = ''

while t:
    r = t%5
    t //= 5
    f = "012=-"[r] + f
    if r > 2:
        t+=1
        
        

print(f)
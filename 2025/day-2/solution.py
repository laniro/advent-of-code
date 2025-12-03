def one():
    t=0
    with open("input.txt") as f:
        f = f.readline().split(",")
        for r in f:
            start = int(r.split("-")[0])
            end = int(r.split("-")[1])
            for i in range(start,end):
                i = str(i)
                if len(i) % 2 == 1: continue
                if i[len(i)//2:] == i[:len(i)//2]:
                    t += int(i)
    return t

def two():
    t=0
    with open("input.txt") as f:
        f = f.readline().split(",")
        for r in f:
            start = int(r.split("-")[0])
            end = int(r.split("-")[1])+1

            for i in range(start,end):
                s = str(i)
                
                repeats = set(map(lambda x : x+1 if len(s)%(x+1) == 0 else 1, range(len(s)//2)))
                for j in repeats:
                    res = [s[k:k + j] for k in range(0, len(s), j)]
                    if all(x == res[0] for x in res):
                        t+=i
                        break
    return t


t = two()
print(t)
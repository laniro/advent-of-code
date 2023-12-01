total = 0
indices = ["1","2","3","4","5","6","7","8","9","one","two","three","four","five","six","seven","eight","nine"]
presentList = []
indexList = []

def word2num(word):
    match word:
        case "one": return 1
        case "two": return 2
        case "three": return 3
        case "four": return 4
        case "five": return 5
        case "six": return 6
        case "seven": return 7
        case "eight": return 8
        case "nine": return 9
        case _: return word

with open("2023/in.txt","r") as f:
    for line in f.readlines():
        indexList = []
        lineList = []
        
        line = line.replace("one","onee")
        line = line.replace("two", "twoo")
        line = line.replace("three","threee")
        line = line.replace("five","fivee")
        line = line.replace("seven","sevenn")
        line = line.replace("eight","eightt")
        line = line.replace("nine","ninee")

        for item in indices[9:]:
            line = line.replace(item,str(word2num(item)))
        

        for item in line:
            if item in indices:
                lineList.append(item)


        line = ''.join(lineList)

        for item in indices:
            try: 
                indexList.append(line.index(item))
            except: pass

        finalNum = int(line[0]+line[-1])
        print(finalNum)
        

        # add to total
        total+= finalNum

print(total)


# 58ninehxcsnzfxbf6xvgcrfznrldqntsbsjmr5
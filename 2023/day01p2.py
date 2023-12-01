total = 0
indices = ["1","2","3","4","5","6","7","8","9","one","two","three","four","five","six","seven","eight","nine"]

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
        # adding extra letters to end of lines: 6two6threeeightwott -> 6twoo6threeeeighttwoott
        for item in indices[9:]:
            if item != "four" and item != "six":
                line = line.replace(item,item+item[-1])
        # replacing words with numbers: 6twoo6threeeeighttwoott -> 62o63e82ott
        for item in indices[9:]:
            line = line.replace(item,str(word2num(item)))
        # adds numbers to new list: 62o63e82ott -> [6,2,6,3,8,2]
        for item in line:
            if item in indices:
                lineList.append(item)
        # concats first item in list to last item and adds it to total.
        total +=  int(lineList[0]+lineList[-1])
print(total)
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
        presentList = []
        indexList = []
        for item in indices:
            if str(item) in line:
                presentList.append(item)

        # iterate through presence presentList and find indices
        for number in presentList:
            index = line.find(str(number))
            indexList.append(index)

        # generate new list with indices. both lists match ie present numbers [1,2,9] matches to indices [3,0,4]
        # done in above step

        # get index in presence presentList of lowest and highest indices ie lowest = 0 --> 2, highest = 4 --> 9
        lowIndex = presentList[indexList.index(min(indexList))]
        highIndex = presentList[indexList.index(max(indexList))]

        # convert words to numbers
        lowIndex = str(word2num(lowIndex))
        highIndex = str(word2num(highIndex))

        # concatenate lowest + highest number
        finalNum = int(lowIndex+highIndex)

        # add to total
        total+= finalNum

print(total)


# 58ninehxcsnzfxbf6xvgcrfznrldqntsbsjmr5
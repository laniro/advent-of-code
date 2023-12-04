cards = []
with open("2023/in.txt","r") as f:
    for line in f.readlines():
        matches = 0
        countCopies = 0
        colonIndex = line.index(":")
        cardNum = int(line[4:colonIndex].strip())
        cards.append(cardNum) # Adds current card number to 'pile'
        # Counts how many of the card cardNum are in the pile
        for card in cards:
            if cardNum == card:
                countCopies +=1
        # Splitting line into 2d list of winning numbers and numbers
        line = line[colonIndex+2:].strip()
        line = line.split(" | ")
        # Removing cases of ''
        for item in range(len(line)):
            line[item] = line[item].split(" ")
            line[item].sort()
            for i in range(line[item].count('')):
                line[item].pop(0)
        # Calculating matches
        for item in line[0]:
            if item in line[1]:
                matches += 1
        # For each copy of card cardNum in pile, add new copies of cards to pile of cards. This bit takes a while.
        for i in range(countCopies): 
            for i in range(matches):
                cards.append(int(cardNum)+i+1)
print(len(cards))
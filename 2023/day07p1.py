with open("2023/in.txt","r") as f:
    f = list(enumerate(f.readlines()))

cardVals = {'T': '10',
            'J': '11',
            'Q': '12',
            'K': '13',
            'A': '14'}
for i in range(1,10):
    cardVals.setdefault(str(i),str(i))

def handType(hand):
    hand = [int(cardVals[x]) for x in hand]
    hand = list(enumerate(hand))
    hand = sorted(hand, key=lambda x:x[1])
    cardPairs = {}

    for c in hand:
        c = c[1]
        if c in cardPairs:
            cardPairs[c] = cardPairs[c]+1
        else:
            cardPairs.setdefault(c,1)
    
    cardPairs = list({k: v for k, v in sorted(cardPairs.items(), key=lambda item: item[1], reverse=True)}.values())
    match cardPairs[0]:
        case 5: return 7 # Five of kind
        case 4: return 6 # Four of kind
        case 3:
            match cardPairs[1]:
                case 2: return 5 # Full house
                case _: return 4 # Three of kind
        case 2:
            match cardPairs[1]:
                case 2: return 3 # Two pair
                case _: return 2 # One pair
        case 1: return 1 # High card
    
returnCases = {7: "Five of a kind",
               6: "Four of a kind",
               5: "Full house",
               4: "Three of a kind",
               3: "Two pair",
               2: "One pair",
               1: "High card"}

l = []

for line in f:
    cardNum = line[0]
    line = line[1].strip()
    cards = line.split()[0]
    a = handType(cards)
    l.append((cardNum,a,[int(cardVals[x]) for x in cards]))


l = sorted(l, key=lambda x: (x[1],x[2]))

tw = 0
for player in enumerate(l):
    rank = player[0]+1
    id = player[1][0]
    bid = int(f[id][1].split()[1])
    tw+=bid*rank
print(tw)
with open("2023/in.txt","r") as f:
    f = list(enumerate(f.readlines()))

cardVals = {'T': '10', 'J': 'J', 'Q': '12', 'K': '13', 'A': '14'}
for i in range(1,10):
    cardVals[str(i)] = str(i)

def getMode(arr):
        if arr==[]:
            return 1
        else:
            return max(set(arr), key=arr.count)

def getPairs(hand):
    cardPairs = {}
    for c in hand:
        c = c[1]
        if c in cardPairs:
            cardPairs[c] = cardPairs[c]+1
        else:
            cardPairs[c] = 1
    cardPairs = list({k: v for k, v in sorted(cardPairs.items(), key=lambda item: item[1], reverse=True)}.values())
    return cardPairs

def handType(hand):
    hand = [cardVals[x] for x in hand]
    hand = list(enumerate(hand))
    JCount = 0
    for c in enumerate(hand):
        if c[1][1] == 'J':
            JCount +=1
    hand = list(enumerate([x[1] for x in hand]))
    hand = sorted(hand, key=lambda x:x[1])
    cardPairs = getPairs(hand)
    cardPairs[0] = min(5,cardPairs[0] + JCount)
    match cardPairs[0]:
        case 5: return 7 # Five of kind
        case 4: return 6 # Four of kind
        case 3:
            match cardPairs[1]:
                case 2: return 5 # Full house
                case 1: return 4 # Three of kind
        case 2:
            match cardPairs[1]:
                case 2: return 3 # Two pair
                case 1: return 2 # One pair
        case 1: return 1 # High card

l = []

for line in f:
    cardNum = line[0]
    line = line[1].strip()
    cards = line.split()[0]
    a = handType(cards)
    cc = []
    jc = 0
    for card in cards:
        if card == 'J':
            jc += 1
        else:
            cc.append(int(cardVals[card]))
    if 'J' in cards:
        for i, x in enumerate(cards):
            if x == 'J':
                cc.insert(i,0)
    
    l.append((cardNum,a,cc))
l = sorted(l, key=lambda x: (x[1],x[2]))

tw = 0

for player in enumerate(l):
    print(player)
    rank = player[0]
    id = player[1][0]
    bid = int(f[id][1].split()[1])
    ct = returnCases[player[1][1]]
    tw+=bid*rank
print(tw)
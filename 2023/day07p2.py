with open("2023/in.txt","r") as f:
    f = list(enumerate(f.readlines()))

cardVals = {'J': '0', 'T': '10', 'Q': '11', 'K': '12', 'A': '13'}
for i in range(1,10): # Adds standard numbers 2-9 inclusive to cardVals
    cardVals[str(i)] = str(i)
joker = cardVals['J']

def getPairs(hand): # Returns how many groups of cards are in a hand
    cardPairs = {}
    for c in hand:
        c = c[1]
        if c == joker: continue # Prevents J being added to cardPairs dict
        if c in cardPairs:
            cardPairs[c] = cardPairs[c]+1
        else:
            cardPairs[c] = 1
    cardPairs = sorted(cardPairs.items(), key=lambda item: item[1], reverse=True) # Sorts cardPairs, largest -> smallest card group
    cardPairs = list({k: v for k, v in cardPairs}.values()) # Makes dict of card: count into a list consisting only of the counts of cards
    if cardPairs == []: return [0] # When all cards are jokers
    else: return cardPairs

def handType(hand): # Goes through every card in hand, accounting for jokers, returning what kind of hand the player has.
    hand = [cardVals[x] for x in hand]
    hand = list(enumerate(hand))
    JCount = 0
    for c in enumerate(hand):
        if c[1][1] == joker:
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
        if card == joker:
            jc += 1
        else:
            cc.append(int(cardVals[card]))
    if joker in cards:
        for i, x in enumerate(cards):
            if x == joker:
                cc.insert(i,joker) # Adds the joker's value to the final hand, used for sorting in the same type
    l.append((cardNum,a,cc))
l = sorted(l, key=lambda x: (x[1],x[2])) # Sorts the hand, based of hand type, then the hand itself, from the first card in the hand

winnings = 0
for player in enumerate(l):
    rank = player[0]+1 # Add one because of 0-Indexing resulting in everything being worth one rank less
    id = player[1][0]
    bid = int(f[id][1].split()[1])
    winnings += bid*rank
print(winnings)
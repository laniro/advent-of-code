f = open("day 2\daytwo.txt", "r")

score = 0

for line in f:
    temp = line.split() # makes line into a list e.g. A Y becomes ['A', 'Y']
    match temp[1]:
        case 'X': # LOSS
            match temp[0]:
                case 'A': # They chose Rock, to lose need to choose scissors
                    score += 3
                case 'B': # They chose Paper, to lose need to choose rock
                    score += 1
                case 'C': # They chose Scissors, to lose need to choose paper
                    score += 2
        case 'Y': # DRAW
            match temp[0]:
                case 'A': # Rock, draw, rock
                    score += 1 + 3
                case 'B': # Paper, draw, paper
                    score += 2 + 3
                case 'C': # Scissors, draw, scissors
                    score += 3 + 3
        case 'Z': # WIN
            match temp[0]:
                case 'A': # Rock, win, paper
                    score += 2 + 6
                case 'B': # Paper, win, scissors
                    score += 3 + 6
                case 'C': # Scissors, win, rock
                    score += 1 + 6
print(score)
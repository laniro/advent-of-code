t=0
test = "C:/Users/tyler/Documents/advent of code/2024/test.txt"
inp = "C:/Users/tyler/Documents/advent of code/2024/inp.txt"
with open(inp, "r") as f:
    f = f.readlines()

def print_grid(list):
    for line in list:
        print((line))

class Guard:
    def __init__(this, x, y, facing):
        this.row = x
        this.column = y
        this.facing = facing
    def __str__(this):
        return f"({this.row},{this.column}) facing {this.facing}"
    
    def moveForward(this, step = 1):
        match this.facing:
            case "North":
                this.row -= 1 * step
            case "East":
                this.column += 1 * step
            case "South":
                this.row += 1 * step
            case "West":
                this.column -= 1 * step
    
    def rotate(this):
        match this.facing:
            case "North":
                this.facing = "East"
            case "East":
                this.facing = "South"
            case "South":
                this.facing = "West"
            case "West":
                this.facing = "North"



f = [list(y) for y in (x.strip() for x in f)]

for r in range(len(f)):
    for c in range(len(f[r])):
        if f[c][r] == '^':
            guard = Guard(c,r,"North")

visited = []
grid_size = (len(f)-1, len(f[guard.row])-1)
while (guard.row,guard.column,guard.facing) not in visited:
    visited.append((guard.row,guard.column,guard.facing))
    f[guard.row][guard.column] = 'X'
    guard.moveForward()

    if guard.row < 0 or guard.row > grid_size[0] or guard.column < 0 or guard.column > grid_size[1]: break

    while f[guard.row][guard.column] == '#':
        guard.moveForward(-1)
        guard.rotate()
        guard.moveForward
    
    match guard.facing:
            case "North":
                f[guard.row][guard.column] = '^'
            case "East":
                f[guard.row][guard.column] = '>'
            case "South":
                f[guard.row][guard.column] = 'v'
            case "West":
                f[guard.row][guard.column] = '<'

just_positions = []
for x in visited:
    just_positions.append((x[0],x[1]))

print(len(set(just_positions)))
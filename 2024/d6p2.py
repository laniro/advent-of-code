import multiprocessing as mp
def print_grid(list):
    for line in list:
        print(''.join(line))

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

def run_sim(guard, f, grid_size,cycle = (0,0)):
    visited = []
    while (guard.row,guard.column,guard.facing) not in visited:
        visited.append((guard.row,guard.column,guard.facing))
        f[guard.row][guard.column] = 'X'
        guard.moveForward()
        if guard.row < 0 or guard.row > grid_size[0] or guard.column < 0 or guard.column > grid_size[1]: 
            return visited

        while f[guard.row][guard.column] == '#':
            guard.moveForward(-1)
            guard.rotate()
            guard.moveForward()
    print(cycle)
    return True


if __name__ == "__main__":
    t=0
    test = "C:/Users/tyler/Documents/advent of code/2024/test.txt"
    inp = "C:/Users/tyler/Documents/advent of code/2024/inp.txt"
    file_path = inp
    with open(file_path, "r") as f:
        f = f.readlines()

    f = [list(y) for y in (x.strip() for x in f)]

    for r in range(len(f)):
        for c in range(len(f[r])):
            if f[c][r] == '^':
                guard = Guard(c,r,"North")

    grid_size = (len(f)-1, len(f[guard.row])-1)
    og_guard = Guard(guard.column, guard.row, "North")

    just_positions = []
    visited = run_sim(guard,f,grid_size)
    for x in visited:
        just_positions.append((x[0],x[1]))
    
    p = mp.Pool()
    args = []
    for i in range(grid_size[0]+1):
        for j in range(grid_size[1]+1):
            if (i,j) not in just_positions: continue
            # reset everything
            guard = Guard(og_guard.column, og_guard.row, "North")
            with open(file_path, "r") as f:
                f = f.readlines()
            f = [list(y) for y in (x.strip() for x in f)]
            f[i][j] = '#'
            
            # main loop
            args.append([guard,f,grid_size,(i,j)])

    res = p.starmap(run_sim,args)

    for r in res:
        if r == True:
            t+=1

    print(t)
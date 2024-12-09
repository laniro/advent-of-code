import multiprocessing as mp
def print_grid(list):
    for line in list:
        print(''.join(line))

class Guard:
    def __init__(this, x, y, facing = (-1,0)):
        this.row = x
        this.column = y
        this.facing = facing
    
    def __str__(this):
        return f"({this.row},{this.column}) facing {this.facing}"

    def moveForward(this, step = 1):
        this.row += this.facing[0] * step
        this.column += this.facing[1] * step
    
    def rotate(this):
        this.facing = (this.facing[1], -this.facing[0])

def run_sim(guard, f, grid_size,cycle = (0,0)):
    visited = []
    print(cycle)
    while (guard.row,guard.column,guard.facing) not in visited:
        visited.append((guard.row,guard.column,guard.facing))
        guard.moveForward()
        if guard.row < 0 or guard.row > grid_size[0] or guard.column < 0 or guard.column > grid_size[1]: 
            return visited

        while f[guard.row][guard.column] == '#':
            guard.moveForward(-1)
            guard.rotate()
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
                guard = Guard(c,r)

    grid_size = (len(f)-1, len(f[guard.row])-1)
    original_position = (guard.column, guard.row)

    just_positions = []
    visited = run_sim(guard,f,grid_size)
    for x in visited:
        just_positions.append((x[0],x[1]))
    
    p = mp.Pool()
    args = []
    for i in range(grid_size[0]+1):
        for j in range(grid_size[1]+1):
            if (i,j) not in just_positions: continue

            # reset guard and grid
            guard = Guard(original_position[1], original_position[0])
            with open(file_path, "r") as f:
                f = f.readlines()
            f = [list(y) for y in (x.strip() for x in f)]
            
            # add obstacle at (i,j)
            f[i][j] = '#'
            
            # main loop
            args.append([guard,f,grid_size,(i,j)])

    res = p.starmap(run_sim,args)

    for r in res:
        if r == True:
            t+=1

    print(t)
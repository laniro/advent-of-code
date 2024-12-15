from timeit import default_timer as timer
import multiprocessing as mp

def checkStone(stone, depth=0):
    if depth == 75:
        return 1

    if stone == 0:
        if depth >= 70:
            stone = 1
            return checkStone(stone, depth+1)
        else:
            stone = 2024
            return checkStone(stone, depth+2)
    
    elif len(str(stone)) % 2 == 0:
        return checkStone(int(str(stone)[0:len(str(stone))//2]), depth+1) + checkStone(int(str(stone)[len(str(stone))//2:]), depth+1)
    
    else:
        stone *= 2024
        return checkStone(stone, depth+1)

if __name__ == "__main__":
    start = timer()
    test = "C:/Users/tyler/Documents/advent of code/2024/test.txt"
    inp = "C:/Users/tyler/Documents/advent of code/2024/inp.txt"
    file_path = inp
    with open(file_path, "r") as f:
        f = f.readline().split()
    f = [int(x) for x in f]
    
    t=0
    for stone in f:
        print(f"Starting stone {stone}.")
        start_stone = timer()
        t += checkStone(stone)
        print(f"Stone {stone} completed. Running total: {t}. Took {timer()-start_stone} seconds.")

    print("Complete.")
    print(t)
    print(f"Took {timer() - start} seconds.")
    input()
from timeit import default_timer as timer
from aoclib import Vector2
from aoclib import Queue

if __name__ == "__main__":
    start = timer()
    test = "C:/Users/tyler/Documents/advent of code/2024/test.txt"
    inp = "C:/Users/tyler/Documents/advent of code/2024/inp.txt"
    file_path = inp
    with open(file_path, "r") as f:
        f = f.readline().split()
    f = [int(x) for x in f]

    for blink in range(25):
        print(f"Blink {blink} length: {len(f)}")
        for i, stone in enumerate(f):
            if isinstance(stone, str): 
                f[i] = int(f[i])
                continue
            if stone == 0:
                f[i] = 1
            elif len(str(stone)) % 2 == 0:
                f[i] = int(str(stone)[0:len(str(stone))//2])
                f.insert(i+1, str(stone)[len(str(stone))//2:])
                pass
            else:
                f[i] = f[i]*2024
                pass

    print(len(f))
    print(f"Took {timer() - start} seconds.")

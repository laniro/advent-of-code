from timeit import default_timer as timer
from aoclib import Vector2
from aoclib import Queue

if __name__ == "__main__":
    start = timer()
    test = "C:/Users/tyler/Documents/advent of code/2024/test.txt"
    inp = "C:/Users/tyler/Documents/advent of code/2024/inp.txt"
    file_path = inp
    with open(file_path, "r") as f:
        f = f.readlines()
    f = [list(y.strip()) for y in f]
    
    trailheads = []

    for x, r in enumerate(f):
        for y, c in enumerate(r):
            if c == '0':
                trailheads.append(Vector2(x,y))
    
    t=0
    directions = [Vector2(1,0),Vector2(0,1),Vector2(-1,0),Vector2(0,-1)]
    for th in trailheads:
        q = Queue(th)
        while not q.is_empty():
            pos = q.dequeue()
            height = int(f[pos.x][pos.y])
            if height== 9:
                t+=1
                continue
            for direction in directions:
                move = pos + direction
                if move.x < 0 or move.y < 0 or move.x >= len(f) or move.y >= len(f[0]): continue
                if height + 1 != int(f[move.x][move.y]): continue
                if move in q.queue: continue
                q.enqueue(move)

    print(t)
    print(f"Took {timer() - start} seconds.")
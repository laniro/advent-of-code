from timeit import default_timer as timer
from aoclib import Vector2
from aoclib import Queue

if __name__ == "__main__":
    start = timer()
    test = "2024/test.txt"
    inp = "2024/inp.txt"
    file_path = inp

    with open(file_path, "r") as f:
        f = f.readlines()
    f = [x.strip() for x in f]

    total_perimeter = []
    directions = [Vector2(1,0),Vector2(0,1),Vector2(-1,0),Vector2(0,-1)]
    for i, r in enumerate(f):
        total_perimeter.append([])
        for j, c in enumerate(f[i]):
            perimeter = 4
            pos = Vector2(i,j)
            for d in directions:
                move = pos + d
                if move.x < 0 or move.y < 0 or move.x >= len(f) or move.y >= len(f[i]): continue
                if f[move.x][move.y] != c: continue
                perimeter -= 1

            total_perimeter[i].append((c,perimeter))

    q = Queue()
    visited = []
    areas = {}
    perimeters = {}
    for i, r in enumerate(total_perimeter):
        for j,c in enumerate(r):
            if Vector2(i,j) in visited: continue
            print(i,j)
            area = 1
            perimeter = 0
            q.enqueue(Vector2(i,j))
            while not q.is_empty():
                pos = q.dequeue()
                visited.append(pos)
                perimeter += total_perimeter[pos.x][pos.y][1]
                for d in directions:
                    move = pos + d
                    if move.x < 0 or move.y < 0 or move.x >= len(f) or move.y >= len(f[i]): continue
                    if f[move.x][move.y] != c[0]: continue
                    if move in q.queue: continue
                    if move in visited: continue
                    q.enqueue(move)
                    area+=1
            if c[0] in areas.keys(): 
                areas[c[0]].append(area)
                perimeters[c[0]].append(perimeter)
            else: 
                areas.update({c[0]: [area]})
                perimeters.update({c[0]: [perimeter]})
            
    t=0
    visited = {}
    final = []
    for i,x in enumerate(areas.values()):
        for j, y in enumerate(x):
            t += y * list(perimeters.values())[i][j]
    print(t)
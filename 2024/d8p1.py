from aoclib import Vector2
def print_grid(list):
    for line in list:
        print(''.join(line))
if __name__ == "__main__":
    test = "C:/Users/tyler/Documents/advent of code/2024/test.txt"
    inp = "C:/Users/tyler/Documents/advent of code/2024/inp.txt"
    file_path = inp
    with open(file_path, "r") as f:
        f = f.readlines()
    f = [list(y) for y in (x.strip() for x in f)]
    locations = {}
    for r in range(len(f)):
        for c in range(len(f[r])):
            if f[r][c] != '.':
                if f[r][c] in locations.keys():
                    locations[f[r][c]].append(Vector2(r,c))
                else:
                    locations.update({f[r][c]:[Vector2(r,c)]})

    antennae = []
    for antenna in locations:
        for p1 in locations[antenna]:
            for p2 in locations[antenna]:
                if p1 == p2: continue
                print(p1,p2)
                vec = p2 - p1
                pos = p1 + 2 * vec
                if pos.x < 0 or pos.x >= len(f[0]) or pos.y < 0 or pos.y >= len(f) or pos in antennae: continue
                antennae.append(pos)

    print(len(antennae))
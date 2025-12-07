def next_layer(grid, layer, beam_positions):
    next_positions = []
    splits = 0
    for x in beam_positions:
        if grid[layer][x] == '^':
            next_positions.append(x-1)
            next_positions.append(x+1)
            splits += 1
        else:
            next_positions.append(x)
    next_positions = list(set(next_positions))
    if layer+1 == len(grid):
        return splits
    else:
        return next_layer(grid, layer+1, next_positions) + splits

def one():
    with open(0) as f:
        f = f.readlines()
    f = [x.strip() for x in f]
    beam_positions = []
    beam_positions.append(f[0].index("S"))
    print(next_layer(f, 0, beam_positions))

def simulate_timeline(grid, layer, x):
    global past_positions
    if (layer,x) in past_positions.keys():
        return past_positions[(layer,x)]
    
    next_positions = []
    if grid[layer][x] == '^':
        next_positions.append(x-1)
        next_positions.append(x+1)
    else:
        next_positions.append(x)
    
    if layer + 1 == len(grid): 
        return 1
    else:
        t = 0
        for timeline in next_positions:
            t += simulate_timeline(grid, layer+1, timeline)
        past_positions.update({(layer,x):t})
        return t

past_positions = {} # dict {(layer, xpos): branches}. caches number of branches from a position

def two():
    with open(0) as f:
        f = f.readlines()
    f = [[y for y in x.strip()] for x in f]
    print(simulate_timeline(f, 0, f[0].index("S")))

two()
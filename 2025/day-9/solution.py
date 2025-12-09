with open(0) as f:
    f = f.readlines()
f = [line.strip().split(",") for line in f]
red_tiles = [(int(x),int(y)) for x,y in f]

def one():
    m = 0
    for coord1 in red_tiles:
        x1,y1 = coord1
        for coord2 in red_tiles:
            x2,y2 = coord2
            x = abs(x1-x2)+1
            y = abs(y1-y2)+1
            area = x*y
            if area > m:
                m = area
    return m


import shapely.geometry
import numpy as np
import matplotlib.pyplot as plt
def plot(hollow_shapes, filled_shapes):
    for shape in hollow_shapes:
        x,y = shape.exterior.xy
        plt.plot(x,y)
    for shape in filled_shapes:
        x,y = shape.exterior.xy
        plt.fill(x,y)
    plt.show()

def two():
    floor = shapely.geometry.Polygon(red_tiles)
    max_area = 0
    for corner1 in red_tiles:
        x1,y1 = corner1
        for corner2 in red_tiles:
            x2,y2 = corner2
            corner3 = (x1,y2)
            corner4 = (x2,y1)
            rectangle = shapely.geometry.Polygon([corner1, corner3, corner2, corner4])
            if rectangle.within(floor):
                #plot([floor], [rectangle])
                max_area = max(max_area, (abs(x1-x2)+1) * (abs(y1-y2)+1))
    return max_area

print(two())

# note: the following are not used anywhere (hence they are commented out)
# but i decided to keep them to show some of the thought process behind today's part 2

"""
def display_grid(red, green, width, height):
    grid = []
    for r in range(height):
        grid.append([])
        for c in range(width):
            grid[r].append(".")

    for x,y in green:
        grid[y][x] = 'X'
    
    for x,y in red:
        grid[y][x] = '#'
        
    for x in grid:
        print(''.join(x))

def connect(tiles_to_connect):
    connecting_tiles = []
    for tile1 in tiles_to_connect:
        for tile2 in tiles_to_connect:
            if tile1 == tile2: continue
            if tile1[0] != tile2[0] and tile1[1] != tile2[1]: continue
            # same x, add all between to green tiles
            high_x = max(tile1[0],tile2[0])
            low_x = min(tile1[0],tile2[0])
            high_y = max(tile1[1],tile2[1])
            low_y = min(tile1[1],tile2[1])
            if tile1[0] == tile2[0]:
                for y in range(low_y, high_y):
                    connecting_tiles.append((tile1[0],y))
            elif tile1[1] == tile2[1]:
                for x in range(low_x, high_x):
                    connecting_tiles.append((x,tile1[1]))
    return connecting_tiles

def get_big_area(red_tiles):
    greatest_area = 0
    for tile1 in red_tiles:
        x1,y1 = tile1
        for tile2 in red_tiles:
            x2,y2 = tile2
            area = (abs(x1-x2)+1)*(abs(y1-y2)+1)
            if area > greatest_area:
                for x in range(min(x1,x2),max(x1,x2)):
                    for y in range(min(y1,y2),max(y1,y2)):
                        if (x,y) not in green_tiles: break
                    else: continue
                    break
                else:
                    greatest_area = area
    return greatest_area

def test_tile(point, corners):
    for tile1 in corners:
        for tile2 in corners:
            if tile1 == tile2: continue
            if tile1[0] != tile2[0] and tile1[1] != tile2[1]: continue
            if tile1[0] == tile2[0] == point[0]:
                if point[1] in range(min(tile1[1],tile2[1]),max(tile1[1],tile2[1])): return True
                else: return False
            if tile1[1] == tile2[1] == point[1]:
                if point[0] in range(min(tile1[0],tile2[0]),max(tile1[0],tile2[0])): return True
                else: return False
"""

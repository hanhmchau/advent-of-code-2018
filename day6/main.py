import operator

def read(file):
    f = open(file, 'r')
    contents = f.read()
    lines = contents.split('\n')
    return lines

def parse_coord(line):
    parts = line.split(',')
    x = int(parts[0].strip())
    y = int(parts[1].strip())
    return y, x

def parse_coords(lines):
    return [ parse_coord(line) for line in lines ]

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def closest_coord(point, coords):
    distances = [ (coord, distance(point, coord)) for coord in coords ]
    minDist = distances[0][1]
    minCoord = coords[0]
    freq = 0
    
    for dist in distances[1:]:
        if dist[1] < minDist:
            minDist = dist[1]
            minCoord = dist[0]
            freq = 0
        else:
            if dist[1] == minDist:
                freq += 1
    if freq == 0:
        return minCoord

def to_letter(coord, coords):
    if coord is None:
        return '.'
    ind = coords.index(coord)
    return chr(97 + ind)

def process_grid(coords):
    grid = [[ None for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            if (i, j) in coords:
                grid[i][j] = (i, j)
            else:
                grid[i][j] = closest_coord((i, j), coords)
    
    return grid

def find_lands(grid, coords):
    infinites = set()
    length = len(grid) - 1

    for i in range(size):
        if grid[0][i] is not None:
            infinites.add(grid[0][i])
        if grid[i][0] is not None:
            infinites.add(grid[i][0])
        if grid[i][length] is not None:
            infinites.add(grid[i][length])
        if grid[length][i] is not None:
            infinites.add(grid[length][i])

    finites = [ x for x in coords if x not in infinites ]
    masses = [ count_land(grid, x) for x in finites ]
    return max(masses)

def count_land(grid, coord):
    count = 0
    for i in range(size):
        for j in range(size):
            if grid[i][j] == coord:
                count += 1
    return count

lines = read('day6/main.txt')
size = 400
grid = [[ 0 for x in range(size)] for y in range(size)]
coords = parse_coords(lines)
grid = process_grid(coords)
# for i in range(size):
#         print(''.join(grid[i]))
print(find_lands(grid, coords))
# print(closest_coord((0, 0), coords))

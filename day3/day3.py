class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def area():
        return width * height

def read(file):
    f = open(file, 'r')
    contents = f.read()
    lines = contents.split('\n')
    return lines

def toRectangles(lines):
    return [ toRectangle(line) for line in lines ]

def toRectangle(line):
    parts = line.split()
    id = parts[0][1:]
    coords = parts[2][:-1].split(',')
    sides = parts[3].split('x')
    left = int(coords[0])
    top = int(coords[1])
    width = int(sides[0])
    height = int(sides[1])
    return Rectangle(left, top, width, height)

size = 1000
grid = [[ 0 for x in range(size)] for y in range(size)]

def processRectangles(rects):
    for rect in rects:
        processRectangle(rect)

def processRectangle(rect):
    for i in range(rect.left, rect.left + rect.width):
        for j in range(rect.top, rect.top + rect.height):
            grid[i][j] += 1

def countOverlaps(grid):
    overlap = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if (grid[i][j] > 1):
                overlap += 1
    return overlap


lines = read('day3.txt')
rectangles = toRectangles(lines)
processRectangles(rectangles)
print(countOverlaps(grid))
def read(file):
    f = open(file, 'r')
    contents = f.read()
    offsets = contents.split()
    return offsets

def process(offsets):
    total = 0
    for offset in offsets:
        total = total + int(offset)
    return total

def find_repeat(offsets):
    sums = set()
    i = 0
    total = 0
    while total not in sums:
        sums.add(total)
        total = total + int(offsets[i])
        i = (i + 1) % len(offsets)
    return total

offsets = read('day1/main.txt')
print(find_repeat(offsets))
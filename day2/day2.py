def read(file):
    f = open(file, 'r')
    contents = f.read()
    ids = contents.split()
    return ids

def contains(str, times):
    map = {}
    for char in list(str):
        occ = map.get(char, 0)
        map[char] = occ + 1
    for key, value in map.items():
        if value == times:
            return True
    return False

def contains_two(str):
    return contains(str, 2)

def contains_three(str):
    return contains(str, 3)

def checksum(ids):
    sumTwo = 0;
    sumThree = 0
    for id in ids:
        if contains_two(id):
            sumTwo += 1
        if contains_three(id):
            sumThree += 1
    return sumTwo * sumThree

def is_close(a, b):
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
    return diff == 1

def extract(a, b):
    same = ''.join([ a[i] for i in range(len(a)) if a[i] == b[i]])

    # Less weird way to write things:
    # same = ''
    # for x, y in zip(a, b):
    #     if x == y:
    #         same += x
    return same

def findCommon(ids):
    for x in ids:
        for y in ids:
            if x != y:
                if is_close(x, y):
                    return extract(x, y)

ids = read('day2.txt')
print(findCommon(ids))
import operator
import queue

def read(file):
    f = open(file, 'r')
    contents = f.read()
    lines = contents.split('\n')
    return lines

def parse_prerequisite(line):
    parts = line.split(' ')
    pre = ord(parts[1].strip()) - 65
    post = ord(parts[7].strip()) - 65
    return pre, post

def parse_prerequisites(lines):
    return [ parse_prerequisite(line) for line in lines ]

def to_char(num):
    return chr(num + 65)

def build_steps(prerequisites):
    steps = [ [] for x in range(size) ]
    for pre, post in prerequisites:
        steps[post] .append(pre)
    return steps

def size_of_task(num):
    return num + 1 + 60
    
def dig(steps):
    workers = [ (-1, 0) ] * worker_count
    remnants = [ x for x in range(size) ]
    seconds = 0
    while len(remnants):
        for i, prereqs in enumerate(steps):
            if len(prereqs) == 0 and i in remnants:
                min_rem = workers[0][1]
                min_index = 0
                for ind, rem in enumerate(workers):
                    if rem[1] < min_rem:
                        min_rem = rem[1]
                        min_index = ind
                if min_rem == 0:
                    remnants.remove(i)
                    workers[min_index] = (i, size_of_task(i))
        
        min_rem = 100000
        for rem in workers:
            if rem[1] < min_rem and rem[1] > 0:
                min_rem = rem[1]
        if (min_rem == 100000):
            min_rem = 0
        for ind, rem in enumerate(workers):
            if workers[ind][1] > 0:
                workers[ind] = (workers[ind][0], workers[ind][1] - min_rem)
                if workers[ind][1] == 0:
                    for ps in steps:
                        try:
                            ps.remove(workers[ind][0])
                        except:
                            pass
        seconds += min_rem
    return seconds
            

worker_count = 5
size = 26
lines = read('day7/main.txt')
prereqs = parse_prerequisites(lines)
steps = build_steps(prereqs)
print(dig(steps))
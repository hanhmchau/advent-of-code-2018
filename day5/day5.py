import operator

def read(file):
    f = open(file, 'r')
    return f.read().strip()

def is_pair(a, b):
    return a.swapcase() == b

def count_reaction_remainder(str):
    stack = []
    count = 0
    for c in list(str):
        if len(stack) and is_pair(stack[len(stack) - 1], c):
            stack.pop()
            count += 2
        else:
            stack.append(c)
    return len(str) - count

def eliminate_char(str, char):
    return str.replace(char, '').replace(char.upper(), '')

def produce_short_polymer(str):
    chars = set(list(str.lower()))
    remainders = []
    for c in chars:
        cleaned_string = eliminate_char(str, c)
        remainder = count_reaction_remainder(cleaned_string)
        remainders.append(remainder)
    return min(remainders)


content = read('day5/day5.txt')
# print(count_reaction_remainder(content))

print(produce_short_polymer(content))
import operator
import queue

def read(file):
    f = open(file, 'r')
    contents = f.read()
    nums = [int(x) for x in contents.split()]
    return nums

def solve(nums, index):
    children_count = nums[index]
    meta_count = nums[index + 1]

    children_values = [ 0 ] * children_count
    next_index = index + 2
    meta_total = 0
    for i in range(children_count):
        value, next_index = solve(nums, next_index)
        children_values[i] = value
    
    for i in range(meta_count):
        meta = nums[next_index + i]
        if children_count == 0:
            meta_total += meta
        else:
            if meta <= children_count:
                meta_total += children_values[meta - 1]
    return meta_total, next_index + meta_count

nums = read('day8/main.txt')
meta_total, ind = solve(nums, 0)
print(meta_total)
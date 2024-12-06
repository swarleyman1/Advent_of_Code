# Advent of Code: Day 3

# Read data from file
data = open("2020/Input/Day3.txt", "r").read().splitlines()
data = [list(i) for i in data]

# Part 1 (slope: right 3, down 1)
trees = 0
x = 0
for i in data:
    if i[x % len(i)] == "#":
        trees += 1
    x += 3

print(trees)


# Part 2
def count_trees(right, down):
    trees = 0
    x = 0
    for i in range(0, len(data), down):
        if data[i][x % len(data[i])] == "#":
            trees += 1
        x += right
    return trees

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

product = 1
for i in slopes:
    product *= count_trees(i[0], i[1])

print(product)

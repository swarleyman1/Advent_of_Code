# Advent of Code: Day 1
# Read data from file and find the two entries that sum to 2020 and then multiply those two numbers together.

# Read data from file
data = open("2020/Input/Day1.txt", "r").read().splitlines()
data = [int(i) for i in data]

# Part 1
for i in data:
    for j in data:
        if i + j == 2020:
            print(i * j)
            
# Part 2
for i in data:
    for j in data:
        for k in data:
            if i + j + k == 2020:
                print(i * j * k)

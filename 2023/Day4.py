# Advent of Code: Day 4

# Read data from file
data = open("2023/Input/Day4.txt", "r").read().splitlines()
data = [i[10:] for i in data]
data = [i.split(" | ") for i in data]
data = [[j.split() for j in i] for i in data]
data = [[[int(k) for k in j] for j in i] for i in data]

# Part 1
# For every scrather, find the number of winning numbers.
# Find which numbers in first list are valid, given the correct numbers in the second list.
# The points for a scratcher are 2^(number of correct numbers - 1).	

# Part 2
# Find the total number of scrathcers if each scratcher gives a copy of the (number of correct numbers) following scratchers.
# This means if scratcher 1 has 3 correct numbers, it gives copies of scratchers 2, 3 and 4.
# Then the copies and the original scratcher 2 are evaluated and the process repeats.
num_valid = []
total_points = 0
scratchers = dict()
for i in range(len(data)):
    scratchers[i] = 0

for i, line in enumerate(data):
    num_valid.append(0)
    scratchers[i] += 1
    for j in line[0]:
        if j in line[1]:
            num_valid[-1] += 1
    if num_valid[-1] > 0:
        total_points += 2**(num_valid[-1] - 1)
    for j in range(num_valid[-1]):
        scratchers[i+1+j] += scratchers[i]

print(int(total_points))
print(sum(scratchers.values()))

# Advent of Code: Day 9

# Read data from file
data = open("2023/Input/Day9.txt", "r").read().splitlines()
data = [[int(x) for x in line.split()] for line in data]

# print(data)

# Part 1
# For each line find the difference between all pairs of numbers.
# If the difference is not all 0, continue with calculating
# the difference between all pairs in the difference list. 
# Continue recursively until the difference is all 0. 
# Then extrapolate the next number in each difference list using 
# the difference of the lower level difference list.

def recursive_diff_forward(line):
    if all([x == 0 for x in line]):
        return 0
    diffs = []
    for i in range(len(line)-1):
        diffs.append(line[i+1] - line[i])
    else:
        return line[-1] + recursive_diff_forward(diffs)
    
ans = 0
for line in data:
    ans += recursive_diff_forward(line)
print(ans)

# Part 2

def recursive_diff_backward(line):
    if all([x == 0 for x in line]):
        return 0
    diffs = []
    for i in range(len(line)-1):
        diffs.append(line[i+1] - line[i])
    else:
        return line[0] - recursive_diff_backward(diffs)

ans = 0
for line in data:
    ans += recursive_diff_backward(line)
print(ans)
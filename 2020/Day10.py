# Advent of Code: Day 10

# Read data from file
data = open("2020/Input/Day10.txt", "r").read().splitlines()
data = [int(i) for i in data]

# Part 1
data.sort()
max_joltage = data[-1] + 3
data.append(max_joltage)
current_joltage = 0
one_jolt_diff = 0
three_jolt_diff = 0
for i in data:
    if i - current_joltage == 1:
        one_jolt_diff += 1
    elif i - current_joltage == 3:
        three_jolt_diff += 1
    current_joltage = i

print(one_jolt_diff * three_jolt_diff)


# Part 2

# This is a dynamic programming problem. We can use the fact that the number of ways
# to get to a certain adapter is equal to the sum of the number of ways to get to 
# the adapters that can reach it. We can start at the end of the list and work backwards,
# and we know that there is only one way to get to the last adapter (the device itself).
# We can then work backwards and calculate the number of ways to get to each adapter.

for i in range(len(data)):
    data[i] = [data[i], 0]

data.append([0, 0])
data.append([max_joltage+3, 1])
data.sort(reverse=True)

for i in range(len(data)):
    for j in range(1, 4):
        if i + j < len(data) and data[i][0] - data[i+j][0] <= 3:
            # print(data[i][0] - data[i+j][0])
            data[i+j][1] += data[i][1]

print(data[-1][1])
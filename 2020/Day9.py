# Advent of Code: Day 9

# Read data from file
data = open("2020/Input/Day9.txt", "r").read().splitlines()
data = [int(i) for i in data]


# Part 1
for i in range(25, len(data)):
    found = False
    for j in range(i-25, i):
        for k in range(i-25, i):
            if data[j] + data[k] == data[i]:
                found = True
    if found == False:
        print(data[i])
        break


# Part 2
max_index = i
target = data[i]
for i in range(max_index):
    for j in range(i, max_index):
        if sum(data[i:j]) == target:
            print(min(data[i:j]) + max(data[i:j]))
            break

    

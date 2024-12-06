# Advent of Code: Day 8

import copy

# Read data from file
data = open("2020/Input/Day8.txt", "r").read().splitlines()
data = [i.replace("+", "") for i in data]

""" Example data: 
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

# Part 1

accumulator = 0
data = [i.split(" ") for i in data]
data = [[i[0], int(i[1]), False] for i in data]
data2 = copy.deepcopy(data)

current_line = 0
while data[current_line][2] == False:
    data[current_line][2] = True
    if data[current_line][0] == "acc":
        accumulator += data[current_line][1]
        current_line += 1
    elif data[current_line][0] == "jmp":
        current_line += data[current_line][1]
    else:
        current_line += 1

print(accumulator)

# Part 2

def check_loop(data):
    accumulator = 0
    current_line = 0
    while current_line < len(data):
        if data[current_line][2] == True:
            return False
        data[current_line][2] = True
        if data[current_line][0] == "acc":
            accumulator += data[current_line][1]
            current_line += 1
        elif data[current_line][0] == "jmp":
            current_line += data[current_line][1]
        else:
            current_line += 1
    return accumulator

for i in range(len(data2)):
    data = copy.deepcopy(data2)
    if data[i][0] == "jmp":
        data[i][0] = "nop"
    elif data[i][0] == "nop":
        data[i][0] = "jmp"
    else:
        continue
    result = check_loop(data)
    if result is not False:
        print(result)
        break

    
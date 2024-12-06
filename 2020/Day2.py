# Advent of code: Day 2


# Read data from file
data = open("2020/Input/Day2.txt", "r").read().splitlines()
data = [i.split() for i in data]


# Part 1
valid = 0
for i in data:
    min, max = i[0].split("-")
    min = int(min)
    max = int(max)
    letter = i[1][0]
    password = i[2]
    if min <= password.count(letter) <= max:
        valid += 1

print(valid)


# Part 2
valid = 0
for i in data:
    idx1, idx2 = i[0].split("-")
    idx1 = int(idx1)
    idx2 = int(idx2)
    letter = i[1][0]
    password = i[2]
    if (password[idx1 - 1] == letter) ^ (password[idx2 - 1] == letter):
        valid += 1

print(valid)
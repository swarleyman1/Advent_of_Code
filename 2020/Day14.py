# Advent of Code: Day 14


# Read data from file
data = open("2020/Input/Day14.txt", "r").read().splitlines()
data = [i.split(" = ") for i in data]

# Part 1
mask = ""
mem = {}

for i in data:
    if i[0] == "mask":
        mask = i[1]
    else:
        mem[i[0]] = int(i[1])
        for j in range(len(mask)):
            if mask[j] == "X":
                continue
            else:
                mem[i[0]] = mem[i[0]] & ~(1 << (35 - j)) | (int(mask[j]) << (35 - j))

print(sum(mem.values()))

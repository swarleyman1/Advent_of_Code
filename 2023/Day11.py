# Advent of Code: Day 11
import numpy as np
# Read data from file
data = open("2023/Input/Day11.txt", "r").read().splitlines()
data = [[x for x in line] for line in data]

convert = {"#": 1, ".": 0}
data = [[convert[x] for x in line] for line in data]
data = np.array(data)

# Part 1 & 2
# Find all indices of the "#" in the data
indices = np.argwhere(data == 1)
# indices = [tuple(x) for x in indices]

# Find all column and row indexes without any "#" in them
empty_columns = []
empty_rows = []
for i in range(data.shape[1]):
    if not any([x[1] == i for x in indices]):
        empty_columns.append(i)

for i in range(data.shape[0]):
    if not any([x[0] == i for x in indices]):
        empty_rows.append(i)

# If there is an empty column before an index of "#", then add to the index of "#" 
# If there is an empty row before an index of "#", then add to the index of "#"
# For part 1 add 1 to the index of "#" for each empty column/row
# For part 2, add 999999

for i, point in enumerate(indices):
    temp_point = point.copy()
    for j in empty_columns:
        if point[1] > j:
            temp_point[1] += 999999 # 
    for j in empty_rows:
        if point[0] > j:
            temp_point[0] += 999999
    indices[i] = temp_point

    

# Find the L1 distance between each pair of indices
distances = []
for i in range(len(indices)):
    for j in range(i+1, len(indices)):
        distances.append(abs(indices[i][0] - indices[j][0]) + abs(indices[i][1] - indices[j][1]))

print(sum(distances))

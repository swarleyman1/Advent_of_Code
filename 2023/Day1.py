# Advent of Code: Day 1

import re
import copy
# Read data from file
data = open("2023/Input/Day1.txt", "r").read().splitlines()
data2 = copy.deepcopy(data)



# Part 1
cumulative_sum = 0
data = [re.sub("[^0-9]", "", i) for i in data]
for i in data:
    # Add to cumulative sum
    if i == "":
        continue
    cumulative_sum += int(i[0]+i[-1])

print(cumulative_sum)

# Part 2
data = data2
cumulative_sum = 0
list_of_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# Find occurences of the values in list_of_numbers and replace them.
# For example: "one" becomes "one1one", "two" becomes "two2two", etc.
# (the extra letters are to account for potential overlap and will be removed later anyway)
for i in list_of_numbers:
    data = [re.sub(i, i+str(list_of_numbers.index(i)+1)+i, j) for j in data]

data = [re.sub("[^0-9]", "", i) for i in data]
for i in data:
    # Add to cumulative sum
    if i == "":
        continue
    cumulative_sum += int(i[0]+i[-1])

print(cumulative_sum)


# Advent of Code 2024: Day 3

data = open("2024/Input/Day3.txt", "r").read()

# Part 1
# Check the input string for "mul(x,y)" and return the product of x and y
# The input string can contain errors and should be ignored
# x and y are integers with up to 3 digits

import re
# Find all matches of the pattern
matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
# Multiply the two numbers in each match and sum the results
result = sum(int(x) * int(y) for x, y in matches)

print(result)

# Part 2
# Same as part 1 but we should now also search for "do()" and "don't()"
# If "do()" is found, all following "mul(x,y)" should be included in the sum
# If "don't()" is found, all following "mul(x,y)" should be excluded
# from the sum, until the next "do()" is found
# The first piece of data before the first "do()" or "don't()" should be included in the sum

# Find index of first "don't()"
index = data.find("don't()")
multiplications = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data[:index])

# Save text between "do()" and "don't()" or "do()" and end of string

matches = re.findall(r"(do\(\)(.*?)don't\(\))|(do\(\)(.*?)$)", data[index:])
for match in matches:
    if match[1] != "":
        multiplications += re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", match[1])
    elif match[3] != "":
        multiplications += re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", match[3])

result = sum(int(x) * int(y) for x, y in multiplications)

print(result)






# Advent of Code 2024: Day 7

# Read input data from file and split into lines
data = open("2024/Input/Day7.txt", "r").read().splitlines()

# For each line, split the line into value and components
data = [line.split(": ") for line in data]

values = [int(data[i][0]) for i in range(0, len(data))]
components = [list(map(int, data[i][1].split(" "))) for i in range(0, len(data))]
# Part 1
# Check if the components can be assembled into the corresponding value 
# The values can either be added or multiplied together (only left to right, no order of operations)

# Recursive function to add or multiply the components together
def check_components(components, value, cum_value):
    # If length of components is 0, return True if cum_value is equal to value, else False
    if len(components) == 0:
        return cum_value == value
    # If cum_value is larger than value, return False
    if cum_value > value:
        return False
    # Else, check if the first component can be added or multiplied to the cum_value
    return check_components(components[1:], value, cum_value + components[0]) or check_components(components[1:], value, cum_value * components[0])

# For each value, check if the components can be assembled into the value
# If True, add the current value to the counter
counter = 0
for i in range(0, len(values)):
    if check_components(components[i], values[i], 0):
        counter += values[i]

print(counter)

# Part 2
# Same as part 1 but the components can also be concatenated together
# Recursive function to add, multiply, or concatenate the components together
def check_components2(components, value, cum_value):
    # If length of components is 0, return True if cum_value is equal to value, else False
    if len(components) == 0:
        return cum_value == value
    # If cum_value is larger than value, return False
    if cum_value > value:
        return False
    # Else, check if the first component can be added, multiplied, or concatenated to the cum_value
    return check_components2(components[1:], value, cum_value + components[0]) or check_components2(components[1:], value, cum_value * components[0]) or check_components2(components[1:], value, int(str(cum_value) + str(components[0])))

# For each value, check if the components can be assembled into the value
# If True, add the current value to the counter
counter = 0
for i in range(0, len(values)):
    if check_components2(components[i][1:], values[i], components[i][0]):
        counter += values[i]

print(counter)
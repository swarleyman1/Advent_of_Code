# Advent of Code: Day 3

# Read data from file
data = open("2023/Input/Day3.txt", "r").read().splitlines()
data = [list(i) for i in data]

# Part 1 (find which numbers are close to a symbol)
# symbols are any charachters not numeric or "."

# Check if a number is next to a symbol (horizontally, vertically or diagonally)
def check_if_close_to_symbol(x, y, symbol_indexes):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if [x+i, y+j] in symbol_indexes:
                return True
    return False
    

# Get indexes of all numbers and save indexes as list of lists
number_indexes = []
symbol_indexes = []
gear_indexes = []
for i, row in enumerate(data):
    number_indexes.append([])
    for j, char in enumerate(row):
        if char.isnumeric():
            if j > 0 and row[j-1].isnumeric():
                number_indexes[i][-1].append(j)
            else:
                number_indexes[i].append([j])
        elif char == "*":
            gear_indexes.append([i, j])
            symbol_indexes.append([i, j])
        elif char == ".":
            continue
        else:
            symbol_indexes.append([i, j])
        
list_of_valid_numbers = [] # list of numbers that are close to a symbol
for i, row in enumerate(number_indexes):
    for j, number in enumerate(row):
        part_number = []
        # check if any digit in number is close to a symbol, if so, add the whole number to list_of_valid_numbers
        for k in number:
            if check_if_close_to_symbol(i, k, symbol_indexes):
                part_number = data[i][number[0]:number[-1]+1]
        if part_number != []:
            part_number = "".join(part_number)
            list_of_valid_numbers.append(int(part_number))

print(sum(list_of_valid_numbers))

# Part 2 (find which numbers are close to a gear and if exactly 2 numbers are close to a gear, multiply them.
# Gears are represented by "*")

def get_numbers_close_to_gear(x, y, number_indexes):
    numbers_close_to_gear = []
    for i, row in enumerate(number_indexes):
        for j, number in enumerate(row):
            for k in number:
                if abs(i-x) <= 1 and abs(k-y) <= 1:
                    numbers_close_to_gear.append(data[i][number[0]:number[-1]+1])
                    break
    if numbers_close_to_gear != []:
        numbers_close_to_gear = [int("".join(i)) for i in numbers_close_to_gear]
    return numbers_close_to_gear

def get_gear_ratio(x, y, number_indexes):
    numbers_close_to_gear = get_numbers_close_to_gear(x, y, number_indexes)
    if len(numbers_close_to_gear) == 2:
        return int(numbers_close_to_gear[0]) * int(numbers_close_to_gear[1])
    else:
        return 0
    
gear_ratios = []
for i in gear_indexes:
    gear_ratios.append(get_gear_ratio(i[0], i[1], number_indexes))

print(sum(gear_ratios))
            
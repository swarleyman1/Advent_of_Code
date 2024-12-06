# Advent of Code 2024: Day 4

data = open("2024/Input/Day4.txt", "r").read().splitlines()

# Part 1
# Check the input array for the word "XMAS" and return the number of times it appears
# The word "XMAS" can be written left to right, right to left, up to down, down to up, or diagonally
# One instance can overlap with another instance
# The input array is a 2D array of characters

def overlapping_count(string, substring):
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count

# Find the word "XMAS" in the input array
count = 0
# Check rows
for row in data:
    count += overlapping_count(row, "XMAS")
    count += overlapping_count(row, "SAMX")

# Check columns
for i in range(len(data[0])):
    column = "".join(row[i] for row in data)
    count += overlapping_count(column, "XMAS")
    count += overlapping_count(column, "SAMX")

# Check diagonal from top left to bottom right
for i in range(len(data) + len(data[0]) - 1):
    diagonal = "".join(data[j][i-j] for j in range(max(0, i-len(data)+1), min(i+1, len(data))))
    count += overlapping_count(diagonal, "XMAS")
    count += overlapping_count(diagonal, "SAMX")

# Check the other diagonal
for i in range(len(data) + len(data[0]) - 1):
    diagonal = "".join(data[j][len(data[0])-1-i+j] for j in range(max(0, i-len(data)+1), min(i+1, len(data))))
    count += overlapping_count(diagonal, "XMAS")
    count += overlapping_count(diagonal, "SAMX")

print(count)


# Part 2
# Instead of the word "XMAS", we should now search for the word "MAS" in the shape of an "X"
# We will do this by sliding a window of size 3x3 over the input array

# Since the word "MAS" can be written in any direction, we will need 4 windows
window1 = [["M", "", "S"],
            ["", "A", ""],
            ["M", "", "S"]]

window2 = [["S", "", "M"],
            ["", "A", ""],
            ["S", "", "M"]]

window3 = [["M", "", "M"],
            ["", "A", ""],
            ["S", "", "S"]]

window4 = [["S", "", "S"],
            ["", "A", ""],
            ["M", "", "M"]]

def window_count(window, data):
    """Count the number of times the window appears in the data
    Args:
        window (2D list): The window to search for, a 3x3 list of characters where empty strings represent any character
        data (2D list): The data to search in, a 2D list of characters
    """
    count = 0
    for i in range(len(data) - 2):
        for j in range(len(data[0]) - 2):
            found = True
            for x in range(3):
                for y in range(3):
                    if window[x][y] != "" and window[x][y] != data[i+x][j+y]:
                        found = False
                        break
                if not found:
                    break
            if found:
                count += 1
    return count

count = window_count(window1, data) + window_count(window2, data) + window_count(window3, data) + window_count(window4, data)
print(count)
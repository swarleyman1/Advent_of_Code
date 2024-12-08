# Advent of Code 2024: Day 8

# Read input data from file
data = open("2024/Input/Day8.txt", "r").read().splitlines()

grid = [list(row) for row in data]

# Part 1:
# Check how many antinodes exist within the bounds of the grid
# For two antennas, an antinode is a position along the line defined by the two antennas 
# exactly the same distance away from the antenna as the two antennas are from each other
# Each antenna is represented by a letter or number in the grid (a-z, A-Z, 0-9)

symbol_positions = {}
antinodes = set()
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y].isalnum():
            # Add position of antenna to symbol_positions
            if grid[x][y] in symbol_positions:
                symbol_positions[grid[x][y]].append((x, y))
            else:
                symbol_positions[grid[x][y]] = [(x, y)]

# Check for antinodes
for symbol in symbol_positions:
    for i in range(len(symbol_positions[symbol])):
        for j in range(i + 1, len(symbol_positions[symbol])):
            x1, y1 = symbol_positions[symbol][i]
            x2, y2 = symbol_positions[symbol][j]
            x_diff = x2 - x1
            y_diff = y2 - y1
            node_pos1 = (x1 - x_diff, y1 - y_diff)
            node_pos2 = (x2 + x_diff, y2 + y_diff)
            if node_pos1[0] in range(len(grid)) and node_pos1[1] in range(len(grid[0])):
                antinodes.add(node_pos1)
            if node_pos2[0] in range(len(grid)) and node_pos2[1] in range(len(grid[0])):
                antinodes.add(node_pos2)

print(len(antinodes))


# Part 2:
# Check how many antinodes exist within the bounds of the grid
# Now, an antinode is a position along the line defined by the two antennas anywhere 
# the distance is a multiple of the distance between the two antennas

antinodes = set()
for symbol in symbol_positions:
    for i in range(len(symbol_positions[symbol])):
        for j in range(i + 1, len(symbol_positions[symbol])):
            x1, y1 = symbol_positions[symbol][i]
            x2, y2 = symbol_positions[symbol][j]
            x_diff = x2 - x1
            y_diff = y2 - y1
            x, y = x1, y1
            while x in range(len(grid)) and y in range(len(grid[0])):
                antinodes.add((x, y))
                x += x_diff
                y += y_diff
            x, y = x1, y1
            while x in range(len(grid)) and y in range(len(grid[0])):
                antinodes.add((x, y))
                x -= x_diff
                y -= y_diff


print(len(antinodes))
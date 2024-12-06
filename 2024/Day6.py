# Advent of Code 2024: Day 6

# Read input data from file and split into lines
data = open("2024/Input/Day6.txt", "r").read().splitlines()

# Convert each line into a list of characters to form the grid
grid = [list(row) for row in data]

# Part 1: 
# Count the number of distinct positions the guard visits before it leaves the grid.
# Guard start position is marked with "^" and guard start direction is up.
# While guard has space in front of it, move guard forward.
# If guard encounters an obstacle (i.e., "#"), turn right 90 degrees and continue moving forward.

# Find starting coordinates (guard can start anywhere on the map)
x0 = next(i for i, row in enumerate(grid) if "^" in row)
y0 = grid[x0].index("^")

# Set to keep track of visited positions
seen = set()

def part1(grid, x, y):
    # Initial direction is up
    dx, dy = -1, 0
    seen.add((x, y))

    # Move the guard until it leaves the grid
    while x + dx in range(len(grid)) and y + dy in range(len(grid[0])):
        # Turn right if an obstacle is encountered
        while grid[x + dx][y + dy] == "#":
            dx, dy = dy, -dx
        
        # Move forward
        x += dx
        y += dy
        seen.add((x, y))

    # Return the number of distinct positions visited
    return len(seen)

# Print the result of part 1
print(part1(grid, x0, y0))

# Part 2: 
# Count the number of infinite loops that can be created by adding a single obstacle to the grid.
# An infinite loop is created when the guard visits a position it has already visited before with the same direction.

def part2(grid, x, y):
    # Set to keep track of visited positions with directions
    seen_directions = set()
    # Initial direction is up
    dx, dy = -1, 0
    seen_directions.add((x, y, dx, dy))

    # Move the guard until it leaves the grid
    while x + dx in range(len(grid)) and y + dy in range(len(grid[0])):
        # Turn right if an obstacle is encountered
        while grid[x + dx][y + dy] == "#":
            dx, dy = dy, -dx
        
        # Move forward
        x += dx
        y += dy
        # Check if the current position and direction have been seen before
        if (x, y, dx, dy) in seen_directions:
            return 1
        seen_directions.add((x, y, dx, dy))

    # No infinite loop found
    return 0

# Remove the starting position from the seen set
seen.remove((x0, y0))

# Count the number of infinite loops
inf_loops = 0
for pos in seen:
    x, y = pos
    # Add an obstacle at the current position
    grid[x][y] = "#"
    # Check if an infinite loop is created
    if part2(grid, x0, y0):
        inf_loops += 1
    # Remove the obstacle
    grid[x][y] = "."

# Print the result of part 2
print(inf_loops)
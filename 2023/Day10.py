# Advent of Code: Day 10

# Read data from file
data = open("2023/Input/Day10.txt", "r").read().splitlines()
data = [[x for x in line] for line in data]

# print dimensions of data
print(len(data), len(data[0]))

# Part 1 
# Maze of pipes
# Find the longest continuous path of pipes that both start and end at 'S'
# '|' is vertical pipe, '-' is horizontal pipe and '.' is no pipe
# Pipes are connected to each other in the following way:
# 'L' connects north and east
# 'J' connects north and west
# '7' connects south and west
# 'F' connects south and east

# Find the starting point
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "S":
            start = (i, j)
            
# Find the longest path
def find_path(start):
    path = []
    i = start[0]+1
    j = start[1]
    direction = "down"
    directions = []
    while True:
        path.append((i, j))
        directions.append(direction)
        if data[i][j] == "S":
            break
        if data[i][j] == "L":
            if direction == "down":
                direction = "right"
                #i += 1
                j += 1
            elif direction == "left":
                direction = "up"
                i -= 1
                #j -= 1
            else:
                # Throw error with message "Invalid direction"
                ValueError("Invalid direction")
        elif data[i][j] == "J":
            if direction == "down":
                direction = "left"
                #i += 1
                j -= 1
            elif direction == "right":
                direction = "up"
                i -= 1
                #j += 1
            else:
                # Throw error with message "Invalid direction"
                ValueError("Invalid direction")
        elif data[i][j] == "7":
            if direction == "up":
                direction = "left"
                #i -= 1
                j -= 1
            elif direction == "right":
                direction = "down"
                i += 1
                #j += 1
            else:
                # Throw error with message "Invalid direction"
                ValueError("Invalid direction")
        elif data[i][j] == "F":
            if direction == "up":
                direction = "right"
                #i -= 1
                j += 1
            elif direction == "left":
                direction = "down"
                i += 1
                #j -= 1
            else:
                # Throw error with message "Invalid direction"
                ValueError("Invalid direction")
        elif data[i][j] == "|":
            if direction == "down":
                i += 1
            elif direction == "up":
                i -= 1
            else:
                # Throw error with message "Invalid direction"
                ValueError("Invalid direction")
        elif data[i][j] == "-":
            if direction == "left":
                j -= 1
            elif direction == "right":
                j += 1
            else:
                # Throw error with message "Invalid direction"
                ValueError("Invalid direction")
        elif data[i][j] == ".":
            # Throw error with message "Invalid direction"
            ValueError("Invalid direction")
        else:
            # Throw error with message "Invalid character"
            ValueError("Invalid character")
    return path, directions

print(start)
path, directions = find_path(start)
print(len(path)/2)

# Part 2 Find the number of elements enclosed by the path

# Find area using the shoelace formula
def area(path):
    area = 0
    for i in range(len(path)-1):
        area += path[i][0]*path[i+1][1] - path[i][1]*path[i+1][0]
    return abs(area)/2

interior_points = area(path) - len(path)/2 + 1
print(interior_points)

# Advent of Code: Day 12


# Read data from file
data = open("2020/Input/Day12.txt", "r").read().splitlines()
data = [[i[0], int(i[1:])] for i in data]


# Part 1
start_direction = "E"
directions = ["N", "E", "S", "W"]
current_direction = start_direction
current_position = [0, 0]
for i in data:
    if i[0] == "N":
        current_position[0] += i[1]
    elif i[0] == "S":
        current_position[0] -= i[1]
    elif i[0] == "E":
        current_position[1] += i[1]
    elif i[0] == "W":
        current_position[1] -= i[1]
    elif i[0] == "L":
        current_direction = directions[(directions.index(current_direction) - i[1]//90) % 4]
    elif i[0] == "R":
        current_direction = directions[(directions.index(current_direction) + i[1]//90) % 4]
    elif i[0] == "F":
        if current_direction == "N":
            current_position[0] += i[1]
        elif current_direction == "S":
            current_position[0] -= i[1]
        elif current_direction == "E":
            current_position[1] += i[1]
        elif current_direction == "W":
            current_position[1] -= i[1]

print(abs(current_position[0]) + abs(current_position[1]))


# Part 2
waypoint_position = [1, 10]
current_position = [0, 0]

for i in data:
    if i[0] == "N":
        waypoint_position[0] += i[1]
    elif i[0] == "S":
        waypoint_position[0] -= i[1]
    elif i[0] == "E":
        waypoint_position[1] += i[1]
    elif i[0] == "W":
        waypoint_position[1] -= i[1]
    elif i[0] == "L":
        for j in range(i[1]//90):
            waypoint_position = [waypoint_position[1], -waypoint_position[0]]
    elif i[0] == "R":
        for j in range(i[1]//90):
            waypoint_position = [-waypoint_position[1], waypoint_position[0]]
    elif i[0] == "F":
        current_position[0] += waypoint_position[0] * i[1]
        current_position[1] += waypoint_position[1] * i[1]

print(abs(current_position[0]) + abs(current_position[1]))


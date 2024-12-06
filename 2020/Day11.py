# Advent of Code: Day 11

import copy

# Read data from file
data = open("2020/Input/Day11.txt", "r").read().splitlines()
data = [list(i) for i in data]
data2 = copy.deepcopy(data)

# Part 1
def get_adjacent_seats(data, x, y):
    adjacent_seats = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < len(data) and 0 <= y + j < len(data[0]) and (i != 0 or j != 0):
                adjacent_seats.append(data[x+i][y+j])
    return adjacent_seats

def get_new_seat_state(data, x, y):
    adjacent_seats = get_adjacent_seats(data, x, y)
    if data[x][y] == "L" and "#" not in adjacent_seats:
        return "#"
    elif data[x][y] == "#" and adjacent_seats.count("#") >= 4:
        return "L"
    else:
        return data[x][y]
    
def get_new_data(data):
    new_data = []
    for i in range(len(data)):
        new_data.append([])
        for j in range(len(data[i])):
            new_data[i].append(get_new_seat_state(data, i, j))
    return new_data

def get_num_occupied_seats(data):
    num_occupied_seats = 0
    for i in data:
        num_occupied_seats += i.count("#")
    return num_occupied_seats

while True:
    new_data = get_new_data(data)
    if new_data == data:
        break
    data = new_data

print(get_num_occupied_seats(data))


# Part 2

def get_visible_seats(data, x, y):
    visible_seats = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                a = x + i
                b = y + j
                while 0 <= a < len(data) and 0 <= b < len(data[0]):
                    if data[a][b] != ".":
                        visible_seats.append(data[a][b])
                        break
                    a += i
                    b += j
    return visible_seats

def get_new_seat_state2(data, x, y):
    visible_seats = get_visible_seats(data, x, y)
    if data[x][y] == "L" and "#" not in visible_seats:
        return "#"
    elif data[x][y] == "#" and visible_seats.count("#") >= 5:
        return "L"
    else:
        return data[x][y]
    
def get_new_data2(data):
    new_data = []
    for i in range(len(data)):
        new_data.append([])
        for j in range(len(data[i])):
            new_data[i].append(get_new_seat_state2(data, i, j))
    return new_data

data = data2
while True:
    new_data = get_new_data2(data)
    if new_data == data:
        break
    data = new_data

print(get_num_occupied_seats(data))
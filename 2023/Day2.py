# Advent of Code: Day 2

# Example data:
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green


# Read data from file
data = open("2023/Input/Day2.txt", "r").read().splitlines()
data = [i.split(": ") for i in data]
data = [[i[0][5:], i[1]] for i in data]
data = [[i[0], i[1].split("; ")] for i in data]
data = [[i[0], [j.split(", ") for j in i[1]]] for i in data]
data = [[i[0], [[k.split(" ") for k in j] for j in i[1]]] for i in data]

game_indexes = [int(i[0]) for i in data[:]]
list_of_games = [i[1] for i in data[:]]

# Part 1
# Find the sum of the indexes of the games that are valid, given at most 12 red cubes,
# 13 green cubes and 14 blue cubes.
max_red = 12
max_green = 13
max_blue = 14

wrong_games = []

for i, game in enumerate(list_of_games):
    for draw in game:
        for color in draw:
            if color[1] == "red":
                if int(color[0]) > max_red:
                    wrong_games.append(i)

            elif color[1] == "green":
                if int(color[0]) > max_green:
                    wrong_games.append(i)

            elif color[1] == "blue":
                if int(color[0]) > max_blue:
                    wrong_games.append(i)

# Remove duplicates
wrong_games = list(dict.fromkeys(wrong_games))

# Sum idxs of correct games
print(sum([i for i in game_indexes if game_indexes.index(i) not in wrong_games]))

# Part 2
# Find the lowest number of red, green and blue cubes that can be used
# in each game to make the game valid.

sum_of_powers = 0
for i, game in enumerate(list_of_games):
    min_red = 0
    min_green = 0
    min_blue = 0
    for draw in game:
        for color in draw:
            if color[1] == "red":
                if int(color[0]) > min_red:
                    min_red = int(color[0])
                    
            elif color[1] == "green":
                if int(color[0]) > min_green:
                    min_green = int(color[0])
                    
            elif color[1] == "blue":
                if int(color[0]) > min_blue:
                    min_blue = int(color[0])

    power = min_red * min_green * min_blue
    sum_of_powers += power

print(sum_of_powers)
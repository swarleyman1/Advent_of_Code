# Advent of Code: Day 5

# Read data from file
data = open("2020/Input/Day5.txt", "r").read().splitlines()

# Part 1
def get_seat_id(seat):
    row = int(seat[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(seat[-3:].replace("L", "0").replace("R", "1"), 2)
    return row * 8 + col

seat_ids = [get_seat_id(i) for i in data]
print(max(seat_ids))


# Part 2
seat_ids.sort()
for i in range(min(seat_ids), max(seat_ids)):
    if i not in seat_ids:
        print(i)
        break



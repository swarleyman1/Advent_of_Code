# Advent of Code: Day 6

# Read data from file
data = open("2020/Input/Day6.txt", "r").read().split("\n\n")
data = [i.replace("\n", " ") for i in data]

# Part 1

sum_of_counts = 0

for i in data:
    # Remove blanks
    i = i.replace(" ", "")

    # Sort out duplicates
    i = list(set(i))
    sum_of_counts += len(i)

print(sum_of_counts)


# Part 2
sum_of_counts = 0
for i in data:
    persons = i.split(" ")
    persons = [set(i) for i in persons]
    common_answers = set.intersection(*persons)
    sum_of_counts += len(common_answers)

print(sum_of_counts)
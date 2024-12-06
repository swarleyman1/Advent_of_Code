# Advent of code 2024: Day 1

data = open("2024/Input/Day1.txt", "r").read().splitlines()
ID_list = [[int(x) for x in line.split("   ")] for line in data]

list1 = [i[0] for i in ID_list]
list2 = [i[1] for i in ID_list]

# Part 1
# sort both lists
list1.sort()
list2.sort()

# Find the distance between the elements of the two lists
diff = [abs(a - b) for a, b in zip(list1, list2)]
print(sum(diff))

# Part 2
# Find the similarity score for the two lists
# The similarity score is the element in the left list multiplied by 
# how many times it appears in the right list
# Part 2
similarity = sum(i * list2.count(i) for i in list1)
print(similarity)

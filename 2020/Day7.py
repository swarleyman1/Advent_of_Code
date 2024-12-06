# Advent of Code: Day 7


# Read data from file
data = open("2020/Input/Day7.txt", "r").read().splitlines()
data = [i.replace("bags", "bag") for i in data]

# Part 1
# Create a dictionary of all bags and their contents
bags = {}

for i in data:
    # Remove all blank spaces
    i = i.replace(" ", "")

    # Remove all periods
    i = i.replace(".", "")

    # Split into bag and contents
    i = i.split("contain")
    bag = i[0]
    contents = i[1]

    # Remove the "bag" from the end of the bag name
    bag = bag[:-3]

    # Split the contents into a list
    contents = contents.split(",")

    # Remove the "bag" from the end of the contents
    contents = [i[:-3] for i in contents]
    
    # Remove the number from the contents
    contents = [i[1:] for i in contents]

    # Add the bag and contents to the dictionary
    bags[bag] = contents

bags['oother'] = []

def check_bag(bag):
    # Check if the bag contains a shiny gold bag
    if "shinygold" in bags[bag]:
        return True
    else:
        # Check if the bags inside the bag contain a shiny gold bag
        for i in bags[bag]:
            if check_bag(i):
                return True
        return False


# Count the number of bags that contain a shiny gold bag
count = 0
for i in bags:
    if check_bag(i):
        count += 1

print(count)

# Part 2
# Create a dictionary of all bags and their contents
bags = {}

for i in data:
    # Remove all blank spaces
    i = i.replace(" ", "")

    # Remove all periods
    i = i.replace(".", "")

    # Split into bag and contents
    i = i.split("contain")
    bag = i[0]
    contents = i[1]

    # Remove the "bag" from the end of the bag name
    bag = bag[:-3]

    # Split the contents into a list
    contents = contents.split(",")

    # Remove the "bag" from the end of the contents
    contents = [i[:-3] for i in contents]

    bag_contents = []
    if contents[0] == "noother":
        bag_contents = []
    else:
        for j in contents:
            nr = j[0]
            name = j[1:]
            for k in range(int(nr)):
                bag_contents.append(name)
    contents = bag_contents

    # Add the bag and contents to the dictionary
    bags[bag] = contents

bags["oother"] = []

def count_bags(bag):
    # Count the number of bags inside the bag
    count = 0
    for i in bags[bag]:
        count += 1
        count += count_bags(i)
    return count

print(count_bags("shinygold"))

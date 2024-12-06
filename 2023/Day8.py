# Advent of Code: Day 8
import math

# Read data from file
data = open("2023/Input/Day8.txt", "r").read().split("\n\n")
instructions = data[0]
nodes = [x.split(" = ") for x in data[1].splitlines()]

# Part 1
node_dict = {}
for node in nodes:
    node_dict[node[0]] = node[1][1:-1].split(", ")

current_node = "AAA"
num_steps = 0
i = 0
while current_node != "ZZZ":
    num_steps += 1
    if i >= len(instructions):
        i = 0
    if instructions[i] == "L":
        current_node = node_dict[current_node][0]
    elif instructions[i] == "R":
        current_node = node_dict[current_node][1]
    i += 1

print(num_steps)

# Part 2

# Add all nodes that end with the letter "A" to a list
current_nodes = []
for node in node_dict:
    if node[-1] == "A":
        current_nodes.append(node)

num_steps = 0
i = 0

def get_num_steps(node):
    num_steps = 0
    i = 0
    while node[-1] != "Z":
        num_steps += 1
        if i >= len(instructions):
            i = 0
        if instructions[i] == "L":
            node = node_dict[node][0]
        elif instructions[i] == "R":
            node = node_dict[node][1]
        i += 1
    return num_steps

steps = 1
for node in current_nodes:
    steps = math.lcm(steps, get_num_steps(node))
    
print(steps)
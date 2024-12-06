# Advent of Code 2024: Day 5

data = open("2024/Input/Day5.txt", "r").read()

# Split the input string on "\n\n" to get the list of rules and the list of updates
rules, updates = data.split("\n\n")
rules = rules.splitlines()
updates = updates.splitlines()

# Parse rules into a dictionary where the key is the key and the value is a list of values
rule_dict = {}
for rule in rules:
    key, value = map(int, rule.split("|"))
    if key not in rule_dict:
        rule_dict[key] = []
    rule_dict[key].append(value)

# Parse updates into lists of integers
updates = [[int(x) for x in update.split(",")] for update in updates]

# Part 1: Check if the update is valid and calculate the sum of the middle integers of valid updates
update_sum = 0
wrong_updates = []
for update in updates:
    valid = True
    for i in range(len(update)):
        current_number = update[i]
        for j in range(i):
            if update[j] in rule_dict.get(current_number, []):
                valid = False
                break
        if not valid:
            wrong_updates.append(update)
            break
    if valid:
        update_sum += update[len(update) // 2]

print(update_sum)

# Part 2: Reorder the numbers in wrong updates to satisfy all rules and calculate the sum of the middle integers
def reorder_update(update):
    for i in range(len(update)):
        current_number = update[i]
        for j in range(i):
            if update[j] in rule_dict.get(current_number, []):
                update[j], update[i] = update[i], update[j]
    return update

for i in range(len(wrong_updates)):
    wrong_updates[i] = reorder_update(wrong_updates[i])

update_sum = sum(update[len(update) // 2] for update in wrong_updates)
print(update_sum)
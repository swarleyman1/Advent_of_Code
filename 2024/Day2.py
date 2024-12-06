# Advent of Code 2024: Day 2

data = open("2024/Input/Day2.txt", "r").read().splitlines()
# convert each line to a list of integers
reports = [[int(x) for x in line.split(" ")] for line in data]

# Part 1
# Check for monotonical increase/decrease in each report
# Also check that the difference between two numbers is less than or equal to 3
valid_reports = 0
for report in reports:
    # Check increasing
    if all(report[i] < report[i+1] for i in range(len(report)-1)) and all(report[i+1] - report[i] <= 3 for i in range(len(report)-1)):
        valid_reports += 1
    # Check decreasing
    elif all(report[i] > report[i+1] for i in range(len(report)-1)) and all(report[i] - report[i+1] <= 3 for i in range(len(report)-1)):
        valid_reports += 1

print(valid_reports)

# Part 2
# Same as part 1 but one element from each report can be removed to make the report valid
valid_reports = 0
for report in reports:
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if all(new_report[i] < new_report[i+1] for i in range(len(new_report)-1)) and all(new_report[i+1] - new_report[i] <= 3 for i in range(len(new_report)-1)):
            valid_reports += 1
            break
        elif all(new_report[i] > new_report[i+1] for i in range(len(new_report)-1)) and all(new_report[i] - new_report[i+1] <= 3 for i in range(len(new_report)-1)):
            valid_reports += 1
            break

print(valid_reports)
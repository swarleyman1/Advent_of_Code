# Advent of Code: Day 6

# Input
# Time:        54     70     82     75
# Distance:   239   1142   1295   1253


times = [54, 70, 82, 75] # Race times
distances = [239, 1142, 1295, 1253] # Race record distances
total = 1
# Part 1
for race in range(len(times)):
    race_distances = []
    for time_held in range(times[race]):
        race_distances.append((times[race] - time_held) * time_held)
    # Count how many distances are larger than the current record for this race
    count = 0
    for distance in race_distances:
        if distance > distances[race]:
            count += 1
    total *= count
print(total)

# Part 2 
#
# Can also be solved by checking how long you have to press the button to get the record distance
# and then subtracting that from the total time
# After this you can check the other way (what the maximum time is to press the button to get the record time)
# and subtract the remaining ways to press the button to in the end get the number of ways you can press the button
# and still beat the record distance
# 
# You are basically solving the equation x^2 - t x + d <= 0 
# where x is the time you press the button, t is the total time and d is the record distance
# Counting the integer solutions to this equation would give the same result as the brute force solution
time = 54708275
distance = 239114212951253
race_distances = []
total = 1

# (Brute force solution)
for time_held in range(time):
    race_distances.append((time - time_held) * time_held)
# Count how many distances are larger than the current record for this race
count = 0
for dist in race_distances:
    if dist > distance:
        count += 1
print(count)
# Advent of Code: Day 5

# Read data from file
data = open("2023/Input/Day5.txt", "r").read().split("\n\n")
data = [block.split("\n") for block in data]

# Part 1
seeds = list(map(int, data[0][0].split(": ")[1].split()))

def parse_map(map_input):
    map_data = []
    map_input = map_input[1:]
    for i in map_input:
        (destination_start, source_start, range_length) = list(map(int, i.split()))
        map_data.append((destination_start, source_start, range_length))
    return map_data

def apply_map(map_rules, x):
    for (destination_start, source_start, range_length) in map_rules:
        if source_start <= x < source_start + range_length:
            return destination_start + x - source_start
    return x

seed2soil = parse_map(data[1])
soil2fertilizer = parse_map(data[2])
fertilizer2water = parse_map(data[3])
water2light = parse_map(data[4])
light2temperature = parse_map(data[5])
temperature2humidity = parse_map(data[6])
humidity2location = parse_map(data[7])

def get_final_destination(seed):
    soil = apply_map(seed2soil, seed)
    fertilizer = apply_map(soil2fertilizer, soil)
    water = apply_map(fertilizer2water, fertilizer)
    light = apply_map(water2light, water)
    temperature = apply_map(light2temperature, light)
    humidity = apply_map(temperature2humidity, temperature)
    location = apply_map(humidity2location, humidity)
    return location

locations = []
for i in seeds:
    locations.append(get_final_destination(i))

print(min(locations))
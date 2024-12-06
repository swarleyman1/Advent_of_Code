# Advent of Code: Day 13

import copy

# Read data from file
data = open("2020/Input/Day13.txt", "r").read().splitlines()
data[1] = data[1].split(",")
data2 = copy.deepcopy(data)
data[1] = [int(i) for i in data[1] if i != "x"]

print(data)

# Part 1
departure_time = int(data[0])
buses = data[1]
# initiate min_wait_time to be larger than any possible wait time
min_wait_time = departure_time

for i in buses:
    wait_time = i - (departure_time % i)
    if wait_time < min_wait_time:
        min_wait_time = wait_time
        bus_id = i

print(bus_id * min_wait_time)


# Part 2
def chinese_remainder_theorem(n, a):
    # https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
    sum = 0
    prod = 1
    for i in n:
        prod *= i
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    # https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q*x0, x0
    if x1 < 0:
        x1 += b0
    return x1


buses = data2[1]
buses = [int(i) if i != "x" else i for i in buses]
n = []
a = []
for i in range(len(buses)):
    if buses[i] != "x":
        n.append(buses[i])
        a.append(buses[i] - i)

print(chinese_remainder_theorem(n, a))
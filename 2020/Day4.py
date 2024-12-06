# Advent of Code: Day 4

# Read data from file
data = open("2020/Input/Day4.txt", "r").read().split("\n\n")
data = [i.replace("\n", " ") for i in data]

# Part 1
list_of_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] # cid is optional
valid_passports = 0
for i in data:
    if all(field in i for field in list_of_fields):
        valid_passports += 1

print(valid_passports)


# Part 2
import re

def validate_passport(passport):
    passport = passport.split(" ")
    passport = [i.split(":") for i in passport]
    passport = {i[0]: i[1] for i in passport}

    # byr
    if not 1920 <= int(passport["byr"]) <= 2002:
        return False

    # iyr
    if not 2010 <= int(passport["iyr"]) <= 2020:
        return False

    # eyr
    if not 2020 <= int(passport["eyr"]) <= 2030:
        return False

    # hgt
    if passport["hgt"][-2:] == "cm":
        if not 150 <= int(passport["hgt"][:-2]) <= 193:
            return False
    elif passport["hgt"][-2:] == "in":
        if not 59 <= int(passport["hgt"][:-2]) <= 76:
            return False
    else:
        return False

    # hcl
    if not re.match(r"^#[0-9a-f]{6}$", passport["hcl"]):
        return False

    # ecl
    if not passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    # pid
    if not re.match(r"^[0-9]{9}$", passport["pid"]):
        return False

    return True


valid_passports = 0
for i in data:
    if all(field in i for field in list_of_fields):
        if validate_passport(i):
            valid_passports += 1

print(valid_passports)

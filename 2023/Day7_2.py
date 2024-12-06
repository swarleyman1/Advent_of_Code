# Advent of Code: Day 7

# Sorting poker hands
# Example input: (hand) (bid)
# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483

# Read data from file
data = open("2023/Input/Day7.txt", "r").read().splitlines()
data = [line.split() for line in data]
data = [[[line[0][j] for j in range(len(line[0]))], line[1:]] for line in data]
data = [[line[0], int(line[1][0])] for line in data]


# Convert cards to numbers
card_values = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}
for line in data:
    for i in range(len(line[0])):
        if line[0][i] in card_values:
            line[0][i] = card_values[line[0][i]]
        else:
            line[0][i] = int(line[0][i])

# Add a column for the hand type according to the following list:
# 0: High card
# 1: Pair
# 2: Two pair
# 3: Three of a kind
# 4: Full house
# 5: Four of a kind
# 6: Five of a kind
# A joker (1) can represent wichever card is needed to make the best hand

def check_type_w_jokers(hand):
    hand = sorted(hand)
    # Check for number of jokers
    jokers = 0
    for card in hand:
        if card == 1:
            jokers += 1
    if jokers == 5:
        return 6
    elif jokers == 4:
        return 6
    elif jokers == 3:
        if hand[3] == hand[4]:
            return 6
        else:
            return 5
    elif jokers == 2:
        if hand[2] == hand[4]:
            return 6
        elif hand[2] == hand[3] or hand[3] == hand[4]:
            return 5
        else:
            return 3
    elif jokers == 1:
        if hand[1] == hand[4]:
            return 6
        elif hand[1] == hand[3] or hand[2] == hand[4]:
            return 5
        elif hand[1] == hand[2] and hand[3] == hand[4]:
            return 4
        elif hand[1] == hand[2] or hand[2] == hand[3] or hand[3] == hand[4]:
            return 3
        else:
            return 1
    else:
        return check_type(hand)


def check_type(hand):
    hand = sorted(hand)
    # Check for five of a kind
    if hand[0] == hand[4]:
        return 6
    # Check for four of a kind
    if hand[0] == hand[3] or hand[1] == hand[4]:
        return 5
    # Check for full house
    if hand[0] == hand[2] and hand[3] == hand[4]:
        return 4
    if hand[0] == hand[1] and hand[2] == hand[4]:
        return 4
    # Check for three of a kind
    if hand[0] == hand[2] or hand[1] == hand[3] or hand[2] == hand[4]:
        return 3
    # Check for two pair
    if hand[0] == hand[1] and hand[2] == hand[3]:
        return 2
    if hand[0] == hand[1] and hand[3] == hand[4]:
        return 2
    if hand[1] == hand[2] and hand[3] == hand[4]:
        return 2
    # Check for pair
    if hand[0] == hand[1] or hand[1] == hand[2] or hand[2] == hand[3] or hand[3] == hand[4]:
        return 1
    # High card
    return 0


for line in data:
    line.append(check_type_w_jokers(line[0]))

# If the hand type is the same, sort according to the first card in the hand, then the second, etc.
# This is done by first sorting the data by type and then sorting them 
# according to the first card, then the second, etc.
data = sorted(data, key=lambda x: (x[2], x[0][0], x[0][1], x[0][2], x[0][3], x[0][4]))

# Multiply the rank of the hand (place in the sorted list) with the bid of the hand (second column) and sum it up
total = 0
for i in range(len(data)):
    total += (i+1) * data[i][1]

print(total)

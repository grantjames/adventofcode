# That means card 1 is worth 8 points (1 for the first match, then doubled three times for each of the three matches after the first).

# Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
# Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
# Card 4 has one winning number (84), so it is worth 1 point.
# Card 5 has no winning numbers, so it is worth no points.
# Card 6 has no winning numbers, so it is worth no points.
# So, in this example, the Elf's pile of scratchcards is worth 13 points.
import time

start_time = time.time()

f = open("input.txt", "r")
input = [ line.strip() for line in f ]
f.close()

scores = []
cards = []

# Faster version - takes 0.65 secs to run with pypy3 (1.63 secs with python3)
# Parse and calculate matches first
for line in input:
    first_half, card_numbers = line.split(" | ")
    card_number = int(first_half.split()[1][:-1])
    winning_numbers = first_half.split()[2:]
    card_numbers = card_numbers.split()
    matches = sum(x in card_numbers for x in winning_numbers)

    cards.append((card_number, matches))

for card in cards:
    for x in range(0, card[1]):
        cards.append(cards[card[0] + x])

print(len(cards))



# Slow version - repeats line parsing and calculating matches
# Takes 10.3 secs to run with pypy3 (36 secs with python3!!!)
# scores = []

# for line in input:
#     first_half, card_numbers = line.split(" | ")
#     card_number = int(first_half.split()[1][:-1])
#     winning_numbers = first_half.split()[2:]
#     card_numbers = card_numbers.split()

#     matches = sum(x in card_numbers for x in winning_numbers)
#     for x in range(0, matches):
#         input.append(input[card_number + x])

# print(len(input))

end_time = time.time()

print(f"Execution took {end_time - start_time} secs")
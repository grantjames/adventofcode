# That means card 1 is worth 8 points (1 for the first match, then doubled three times for each of the three matches after the first).

# Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
# Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
# Card 4 has one winning number (84), so it is worth 1 point.
# Card 5 has no winning numbers, so it is worth no points.
# Card 6 has no winning numbers, so it is worth no points.
# So, in this example, the Elf's pile of scratchcards is worth 13 points.

f = open("input.txt", "r")
input = [ line.strip() for line in f ]
f.close()

scores = []

for line in input:
    winning_numbers, card_numbers = line.split(" | ")
    winning_numbers = winning_numbers.split()[2:]
    card_numbers = card_numbers.split()

    matches = sum(x in card_numbers for x in winning_numbers)
    if matches > 0:
        scores.append(pow(2, (matches-1)))

print(sum(scores))
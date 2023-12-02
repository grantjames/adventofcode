# Determine which games would have been possible if the 
# bag had been loaded with only
# 12 red cubes, 13 green cubes, and 14 blue cubes.
# What is the sum of the IDs of those games?

# Test input answer = 8

import re

f = open("input.txt", "r")
input = f.readlines()
f.close()

cubes = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

round_pattern = r"(\d+) (red|green|blue)"
total = 0
game_number = 0

for line in input:
    game_number += 1
    rounds = line.split(';')
    valid_game = True
    for round in rounds:
        results = re.findall(round_pattern, round)
        for result in results:
            # print(f"Is {result[0]} > {cubes[result[1]]}?")
            if int(result[0]) > cubes[result[1]]:
                # print("Yes")
                valid_game = False
                break
        if not valid_game:
            break
    if valid_game:
        total += game_number

print(total)
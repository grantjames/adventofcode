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
            if int(result[0]) > cubes[result[1]]:
                valid_game = False
                break
        if not valid_game:
            break
    if valid_game:
        total += game_number

print(total)
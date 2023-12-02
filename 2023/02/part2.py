import re
import math

f = open("input.txt", "r")
input = f.readlines()
f.close()

round_pattern = r"(\d+) (red|green|blue)"
totals = []

for line in input:
    rounds = line.split(';')
    max_counts = {
        'red': 0,
        'blue': 0,
        'green': 0
    }
    for round in rounds:
        results = re.findall(round_pattern, round)
        for result in results:
            if int(result[0]) > max_counts[result[1]]:
                max_counts[result[1]] = int(result[0])
    result = math.prod([v for _, v in max_counts.items()])
    totals.append(result)

print(sum(totals))
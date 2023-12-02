f = open("input.txt", "r")
input = f.readlines()
f.close()

total_score = 0
for i, x in enumerate(input):
    score = 0
    opponent, mine = x.split()

    # A = Rock, B = Paper, C = Scissors
    # X = Rock, Y = Paper, Z = Scissors

    # Scoring 1 Rock, 2 Paper, 3 scissors
    # 6 win, 3 draw, 0 loss
    # 15 for sample input

    if mine == "X":
        score += 1

        if opponent == "A":
            score += 3
        if opponent == "B":
            score += 0
        if opponent == "C":
            score += 6
    
    if mine == "Y":
        score += 2

        if opponent == "A":
            score += 6
        if opponent == "B":
            score += 3
        if opponent == "C":
            score += 0
    
    if mine == "Z":
        score += 3

        if opponent == "A":
            score += 0
        if opponent == "B":
            score += 6
        if opponent == "C":
            score += 3
    
    total_score += score

print(total_score)
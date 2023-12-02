f = open("input.txt", "r")
input = f.readlines()
f.close()

total_score = 0
for i, x in enumerate(input):
    score = 0
    opponent, mine = x.split()

    # A = Rock, B = Paper, C = Scissors
    # X = lose, Y = draw, Z = win

    # Scoring 1 Rock, 2 Paper, 3 scissors
    # 6 win, 3 draw, 0 loss
    # 12 for sample input

    if mine == "X": # need to lose
        score += 0

        if opponent == "A":
            # play scissors
            score += 3
        if opponent == "B":
            # play rock
            score += 1
        if opponent == "C":
            # play paper
            score += 2
    
    if mine == "Y": # need to draw
        score += 3

        if opponent == "A":
            # play rock
            score += 1
        if opponent == "B":
            # play paper
            score += 2
        if opponent == "C":
            # play scissors
            score += 3
    
    if mine == "Z": # need to win
        score += 6

        if opponent == "A":
            # play paper
            score += 2
        if opponent == "B":
            # play scissors
            score += 3
        if opponent == "C":
            # play rock
            score += 1
    
    total_score += score

print(total_score)
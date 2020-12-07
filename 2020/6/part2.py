f = open("input.txt", "r")
input = f.read()
f.close()

group_answers = input.split("\n\n")

yes_total = 0

for group in group_answers:
    person_answers = map(set, group.split("\n"))

    answers = len(set.intersection(*person_answers))

    yes_total += answers
    
print(yes_total)
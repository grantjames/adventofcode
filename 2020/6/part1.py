f = open("test_input.txt", "r")
input = f.read()
f.close()

group_answers = input.split("\n\n")

yes_total = 0

for group in group_answers:
    answers = len(set(group.replace("\n", "")))

    yes_total += answers
    
print(yes_total)
import re

f = open("input.txt", "r")
input = f.readlines()
f.close()

# convert lines to ints
input = list(map(int, input))

lookback = 25
# result = 0
invalid_number = 0

for index, n in enumerate(input):
    if index < lookback:
        continue

    # check if any 2 of the previous "lookback" numbers multiplied together give n
    lookback_list = list(set(input[index - lookback:index])) # use set() to make sure they're all different

    valid = False
    for x in lookback_list:
        for y in lookback_list[1:]:
            # print("does", x, "+", y, "=", n, "?")
            if x + y == n:
                valid = True
                break
        if valid:
            break
    
    if not valid:
        invalid_number = n
        break

print("Target value:", invalid_number)

contiguous_list = []
for i, x in enumerate(input):
    contiguous_list = [x]
    total = x
    for y in input[i+1:]:
        total += y

        contiguous_list.append(y)

        if total == invalid_number:
            print(contiguous_list)
            print("Result:", min(contiguous_list) + max(contiguous_list))
            exit()
import re

f = open("test_input.txt", "r")
input = f.readlines()
f.close()

# convert lines to ints
input = list(map(int, input))

lookback = 5
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

print(invalid_number)
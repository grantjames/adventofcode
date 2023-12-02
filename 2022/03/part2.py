f = open("input.txt", "r")
input = f.readlines()
f.close()

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

sum = 0
group_index = 0


while group_index < len(input):
    bag1 = set(input[group_index][:-1]) # :-1 to remove newline char
    bag2 = set(input[group_index+1][:-1])
    bag3 = set(input[group_index+2][:-1])

    common = bag1 & bag2 & bag3

    sum += characters.index(next(iter(common))) + 1
    group_index += 3

print(sum)
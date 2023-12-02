f = open("sample_input.txt", "r")
input = f.readlines()
f.close()

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

sum = 0

for bag in input:
    # split into halves
    first = bag[:len(bag)//2]
    second = bag[len(bag)//2:]

    # Find common characters in both halves
    common = [value for value in first if value in second]
    sum += characters.index(common[0]) + 1

print(sum)
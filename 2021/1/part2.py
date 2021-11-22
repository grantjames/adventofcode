f = open("input.txt", "r")
input = f.readlines()
input = list(map(int, input))  # convert the list of strings to a list of ints
f.close()

for x in input:
    for y in input:
        for z in input:
            if x + y + z == 2020:
                print(x * y * z)
                exit()
        
print("No result found")
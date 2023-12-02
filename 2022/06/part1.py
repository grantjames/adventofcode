f = open("input.txt", "r")
input = f.readline()
f.close()

buffer = []

for index, char in enumerate(input):
    buffer.append(char)
    
    if len(buffer) > 14:
        buffer = buffer[1:]

    if len(set(buffer)) == 14:
        print(index + 1)
        break
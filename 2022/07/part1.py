f = open("input.txt", "r")
input = f.readlines()
f.close()

dir_sizes = {}
pwd = []

for line in input:
    if line.startswith("$ cd .."):
        pwd.pop()

    elif line.startswith("$ cd "):
        # Get the name of the directory we're changing to
        directory = line[5:-1]
        pwd.append(directory)
        # if directory not in dir_sizes.keys():
        dir_sizes["/".join(pwd)] = 0
    
    # Do this for files
    elif not line.startswith("dir ") and not line.startswith("$"):
        size, name = line.split()
        for i, dir in enumerate(pwd):
            print(pwd[:i+1])
            dir_sizes["/".join(pwd[:i+1])] += int(size)

total = 0
for key, size in dir_sizes.items():
    print(key, size)
    if size <= 100000:
        total += size

print(total)

# Answer is not 1151021 (too low)
# also wrong: 312437 (too low)

# total = 0
# for dir, files in file_system.items():
#     current_dir_size = 0
#     for file in files:
#         current_dir_size += file[0]
#     if current_dir_size <= 100000:
#         total += current_dir_size
#     print(dir, current_dir_size)

# print(total)
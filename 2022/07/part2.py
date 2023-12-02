f = open("input.txt", "r")
input = f.readlines()
f.close()

fs_size = 70000000
space_needed_to_update = 30000000

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
            dir_sizes["/".join(pwd[:i+1])] += int(size)

free_space = fs_size - dir_sizes["/"]

to_free = space_needed_to_update - free_space
print("need to free up:", to_free)

suitable_sizes = []
for key, size in dir_sizes.items():
    if int(size) >= to_free:
        suitable_sizes.append(int(size))

suitable_sizes.sort()
print(suitable_sizes[0])
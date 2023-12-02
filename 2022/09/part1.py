from collections import namedtuple

f = open("input.txt", "r")
input = f.readlines()
f.close()

Point = namedtuple("Point", ["x", "y"])
Instruction = namedtuple("Instruction", ["dir", "times"])

instructions = []
t_visited = [Point(0, 0)]
h_pos = Point(0, 0)
t_pos = Point(0, 0)

for line in input:
    instructions.append(Instruction(line[0], int(line[2:-1])))

for instruction in instructions:
    for i in range(0, instruction.times):
        if instruction.dir == "R":
            h_pos = Point(h_pos.x + 1, h_pos.y)
        elif instruction.dir == "L":
            h_pos = Point(h_pos.x - 1, h_pos.y)
        elif instruction.dir == "U":
            h_pos = Point(h_pos.x, h_pos.y + 1)
        elif instruction.dir == "D":
            h_pos = Point(h_pos.x, h_pos.y - 1)
        
        # continue if T and H are adjacent
        if (t_pos.x >= h_pos.x - 1 and t_pos.x <= h_pos.x + 1) and t_pos.y >= h_pos.y - 1 and t_pos.y <= h_pos.y + 1:
            # print("skipping T move when H is at", h_pos, "because T is at", t_pos)
            continue
        
        # calculate new t_pos based off h_pos
        # Both are on the same column, so just change y
        if h_pos.x == t_pos.x:
            if h_pos.y > t_pos.y:
                t_pos = Point(t_pos.x, t_pos.y + 1)
            elif h_pos.y < t_pos.y:
                t_pos = Point(t_pos.x, t_pos.y - 1)
        
        # Both are on the same row, so just change x
        elif h_pos.y == t_pos.y:
            if h_pos.x > t_pos.x:
                t_pos = Point(t_pos.x + 1, t_pos.y)
            elif h_pos.x < t_pos.x:
                t_pos = Point(t_pos.x - 1, t_pos.y)

        # both cases above are fine if the two points are on top of each other
        
        # tail needs to move diagonally
        if h_pos.y != t_pos.y and h_pos.x != t_pos.x:
            new_x, new_y = t_pos.x, t_pos.y
            if h_pos.x > t_pos.x:
                new_x += 1
            elif h_pos.x < t_pos.x:
                new_x -= 1
            if h_pos.y > t_pos.y:
                new_y += 1
            elif h_pos.y < t_pos.y:
                new_y -= 1
            
            t_pos = Point(new_x, new_y)
        
        t_visited.append(t_pos)

t_visited_unique = set(t_visited)

# for y in range(4,-1, -1):
#     for x in range(0,6):
#         if Point(x, y) in t_visited_unique:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print("\n")

# for v in t_visited_unique:
#     print(v)
print(len(set(t_visited)))
from collections import namedtuple

f = open("input.txt", "r")
input = f.readlines()
f.close()

Point = namedtuple("Point", ["x", "y"])
Instruction = namedtuple("Instruction", ["dir", "times"])

instructions = []
knots = [
    Point(11, 5), Point(11, 5), Point(11, 5), Point(11, 5), Point(11, 5),
    Point(11, 5), Point(11, 5), Point(11, 5), Point(11, 5), Point(11, 5)
]

t_visited = [knots[len(knots) - 1]]

for line in input:
    instructions.append(Instruction(line[0], int(line[2:-1])))

def move_points(head, tail):
    
    # continue if T and H are adjacent
    if (tail.x >= head.x - 1 and tail.x <= head.x + 1) and tail.y >= head.y - 1 and tail.y <= head.y + 1:
        # print("skipping T move when H is at", h_pos, "because T is at", t_pos)
        return tail
    
    # calculate new t_pos based off h_pos
    # Both are on the same column, so just change y
    if head.x == tail.x:
        if head.y > tail.y:
            tail = Point(tail.x, tail.y + 1)
        elif head.y < tail.y:
            tail = Point(tail.x, tail.y - 1)
    
    # Both are on the same row, so just change x
    elif head.y == tail.y:
        if head.x > tail.x:
            tail = Point(tail.x + 1, tail.y)
        elif head.x < tail.x:
            tail = Point(tail.x - 1, tail.y)

    # tail needs to move diagonally
    if head.y != tail.y and head.x != tail.x:
        new_x, new_y = tail.x, tail.y
        if head.x > tail.x:
            new_x += 1
        elif head.x < tail.x:
            new_x -= 1
        if head.y > tail.y:
            new_y += 1
        elif head.y < tail.y:
            new_y -= 1
        
        tail = Point(new_x, new_y)
    
    return tail

for instruction in instructions:
    for i in range(0, instruction.times):
        # first move the head
        if instruction.dir == "R":
            knots[0] = Point(knots[0].x + 1, knots[0].y)
        elif instruction.dir == "L":
            knots[0] = Point(knots[0].x - 1, knots[0].y)
        elif instruction.dir == "U":
            knots[0] = Point(knots[0].x, knots[0].y + 1)
        elif instruction.dir == "D":
            knots[0] = Point(knots[0].x, knots[0].y - 1)
        
        # now move the other knots

        for n, knot in enumerate(knots[:-1]):
            # print(knots[9])
            knots[n+1] = move_points(knots[n], knots[n + 1])

            if n + 1 == len(knots) - 1:
                # print("tail is at:", knots[n+1])
                t_visited.append(knots[n+1])

t_visited_unique = set(t_visited)

for y in range(22,-1, -1):
    for x in range(0,22):
        if Point(x, y) in t_visited_unique:
            print("#", end="")
        else:
            print(".", end="")
    print("\n")

print(len(t_visited_unique))
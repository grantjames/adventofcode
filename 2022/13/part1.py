f = open("sinput.txt", "r")
input = f.readlines()
f.close()

pairs = []
for x in range(0, len(input), 3):
    # use eval
    pairs.append((eval(input[x].strip("\n")), eval(input[x + 1].strip("\n"))))

# Return None if no decision is made about the comparison
# Return True if in correct order (a is less than b)
# Return False if in wrong order
def compare(a, b):
    if type(a) is int and type(b) is int:
        if a == b:
            return None
        else:
            return a < b
    
    if type(a) is int and type(b) is list:
        return compare([a], b)
    if type(a) is list and type(b) is int:
        return compare(a, [b])

    if type(a) is list and type(b) is list and len(a) == 0 and len(b) == 0:
        return None

    if type(a) is list and len(a) == 0:
        return True
    if type(b) is list and len(b) == 0:
        return False
    
    result = compare(a[0], b[0])

    if result == None:
        if len(a) == 1 and len(b) == 1:
            return None
        elif len(a) == 1:
            return True
        elif len(b) == 1:
            return False
        else:
            return compare(a[1:], b[1:])
    else:
        return result
 
# print(compare([1,1,3,1,1], [1,1,5,1,1]))
# print(compare([[1],[2,3,4]], [[1],4]))
# print(compare([9], [[8,7,6]]))
# print(compare([[4,4],4,4], [[4,4],4,4,4]))
# print(compare([7,7,7,7], [7,7,7]))
# print(compare([], [3]))
# print(compare([[[]]], [[]]))
# print(compare([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]))

correct_order_indexes = []
for p, pair in enumerate(pairs):
    if compare(pair[0], pair[1]):
        correct_order_indexes.append(p + 1)
    
print(correct_order_indexes)
print(sum(correct_order_indexes))

# 6061 is too high
# 5994 is too high

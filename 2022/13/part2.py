import functools

f = open("input.txt", "r")
input = f.readlines()
f.close()

packets = []
for line in input:
    if not line.isspace():
        packets.append(eval(line.strip()))

# Add on the divider packets
packets.append([[2]])
packets.append([[6]])

def compare(a, b):
    if type(a) is int and type(b) is int:
        if a == b:
            return 0
        else:
            if a < b:
                return -1
            else:
                return 1
    
    if type(a) is int and type(b) is list:
        return compare([a], b)
    if type(a) is list and type(b) is int:
        return compare(a, [b])

    if type(a) is list and type(b) is list and len(a) == 0 and len(b) == 0:
        return 0

    if type(a) is list and len(a) == 0:
        return -1
    if type(b) is list and len(b) == 0:
        return 1
    
    result = compare(a[0], b[0])

    if result == 0:
        if len(a) == 1 and len(b) == 1:
            return 0
        elif len(a) == 1:
            return -1
        elif len(b) == 1:
            return 1
        else:
            return compare(a[1:], b[1:])
    else:
        return result

sorted = sorted(packets, key=functools.cmp_to_key(compare))
 
div1 = sorted.index([[2]]) + 1
div2 = sorted.index([[6]]) + 1

print(div1 * div2)
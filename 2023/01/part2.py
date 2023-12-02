f = open("input.txt", "r")
input = f.readlines()
f.close()

replace = {
    'nine': '9',
    'eight': '8',
    'seven': '7',
    'six': '6',
    'five': '5',
    'four': '4',
    'three': '3',
    'two': '2',
    'one': '1',
}

def get_first_digit(input):
    # Get index of first integer
    integer_index = 10000
    for _, v in replace.items():
        i = input.find(v)
        if i != -1 and i < integer_index:
            integer_index = i

    # Get index of first alpha
    alpha_index = 10000
    alpha = ""
    for k, v in replace.items():
        i = input.find(k)
        if i != -1 and i < alpha_index:
            alpha_index = i
            alpha = k
    
    # Return value which has earliest index
    if integer_index < alpha_index:
        return input[integer_index]
    else:
        return replace[alpha]
    
def get_last_digit(input):
    # Get index of last integer
    integer_index = -1
    for _, v in replace.items():
        i = input.rfind(v)
        if i != -1 and i > integer_index:
            integer_index = i

    # Get index of last alpha
    alpha_index = -1
    alpha = ""
    for k, v in replace.items():
        i = input.rfind(k)
        if i != -1 and i > alpha_index:
            alpha_index = i
            alpha = k
    
    # Return value which has latest index
    # print(f"integer_index = {integer_index}, alpha_index = {alpha_index}")
    if integer_index < alpha_index:
        return replace[alpha]
    else:
        return input[integer_index]

values = []
for line in input:
    v = int(get_first_digit(line) + get_last_digit(line))
    print(v)
    values.append(v)

print(sum(values))
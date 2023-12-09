"""
Day 9 Code
----------

Part 1
-------
    Extrapolate the next value in the sequence
    What is the sum of the extrapolated values?
"""

file_path = "./day_9/"
file_name = "day_9_input.txt"

with open(f"{file_path}{file_name}") as open_file:
    lines = open_file.read().splitlines()
    lines = [list(map(int, line.split(" ")))for line in lines]

def get_differences(sequence):
    difference_list = []
    for index, digit in enumerate(sequence):
        if index < len(sequence)-1:
            difference_list.append(sequence[index +1] - digit)
    return difference_list

def make_difference_dictionary(sequence):
    difference_dict = {0:sequence}
    for x in range(999):
        difference_dict[x + 1] = get_differences(difference_dict[x])
        if all(v == 0 for v in get_differences(difference_dict[x])):
            return difference_dict

def predict_next(sequence):
    difference = make_difference_dictionary(sequence)
    lasts = [value[-1] for value in list(difference.values())][::-1]
    return(sum(lasts))

# We can also do this by working out f(n) from the difference dictionary


"""
Part 2
-------
    Extrapolate backwards and sum

"""

def predict_first(sequence):
    difference = make_difference_dictionary(sequence)
    firsts = [value[0] for value in list(difference.values())][::-1]
    working_num = firsts[0]
    for first in firsts[1:]:
        working_num = first - working_num
    return working_num

        

print(sum(predict_first(line) for line in lines))

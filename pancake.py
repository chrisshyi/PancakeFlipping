import sys


def flip_bits(bit_array, start, end):
    """
    Flips all the boolean values in bit_array, from start to end inclusive
    :param bit_array: an array of booleans
    :param start: the starting index to begin the flipping
    :param end: the ending index
    :return: None
    """
    for x in range(start, end + 1):
        bit_array[x] = not bit_array[x]


def check_if_all_same(bit_array, start, end):
    """
    Checks if the values from start to end(inclusive) are all the same in bit_array
    :param bit_array: an array of booleans
    :param start: the starting index to begin the checking
    :param end: the ending index
    :return: True if all values are the same from start to end, False if otherwise
    """
    for x in range(start, end + 1):
        if bit_array[x] != bit_array[start]:
            return False
    return True


def solve_pancake(pancake_array, flipper_size, start, end, total_flips):
    """
    Finds the minimum number of flips to turn all values in pancake_array to True. The algorithm operates
    on a portion of the pancake array at a time, hence the start and end
    :param pancake_array: the pancakes represented as an array of boolean values
    :param flipper_size: the size of the pancake flipper
    :param total_flips: the total number of flips
    :param start: the starting index
    :param end: the ending index
    :return: (minimum flips, True/False depending on whether the array can be flipped to all True)
    """
    if end - start + 1 < flipper_size:
        # if remaining length is less than flipper size, all elements must be True for there
        # to be a solution
        for x in range(start, end + 1):
            if not pancake_array[x]:
                return 0, False
        return total_flips, True

    if end - start + 1 == flipper_size:
        if check_if_all_same(pancake_array, start, end):
            if pancake_array[start]:
                return total_flips, True
            else:
                return total_flips + 1, True
        else:
            return 0, False
    # Always keep the leftmost bit True, and then consider the rest of the array recursively
    if not pancake_array[start]:  # if the element at the start index is False, do a flip
        flip_bits(pancake_array, start, start + flipper_size - 1)
        total_flips += 1
    return solve_pancake(pancake_array, flipper_size, start + 1, end, total_flips)


def main(input_file):
    with open(input_file, 'r') as file:
        with open('pancake_results.txt', 'w') as out_file:
            num_lines = int(file.readline())
            for x in range(num_lines):
                line = file.readline()
                split_line = line.split(' ')
                pancake_array = []
                for char in split_line[0]:
                    if char == '-':
                        pancake_array.append(False)
                    else:
                        pancake_array.append(True)
                flipper_size = int(split_line[1])
                result = solve_pancake(pancake_array, flipper_size, 0, len(pancake_array) - 1, 0)
                out_file.write("Case #{}: ".format(x + 1))
                if not result[1]:
                    out_file.write("IMPOSSIBLE\n")
                else:
                    out_file.write("{}\n".format(result[0]))


if __name__ == '__main__':
    # Max recursion depth will be exceeded on the large input file if using original limit
    # Can rewrite algorithm in iterative way
    sys.setrecursionlimit(1500)
    main(sys.argv[1])
    # main("small_test")
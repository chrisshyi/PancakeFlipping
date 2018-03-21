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


def solve_pancake(pancake_array, flipper_size, start, end):
    """
    Finds the minimum number of flips to turn all values in pancake_array to True. The algorithm operates
    on a portion of the pancake array at a time, hence the start and end
    :param pancake_array: the pancakes represented as an array of boolean values
    :param flipper_size: the size of the pancake flipper
    :param start: the starting index
    :param end: the ending index
    :return: the minimum number of flips needed to flip all values in pancake_array to True
    """
    pass





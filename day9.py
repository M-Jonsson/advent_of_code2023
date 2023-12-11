from aoc_common import read_file
from time import perf_counter


def parse_data(data: list):
    """Re-formats the puzzle input to a list of lists, where each line
    in the input is a list of the numbers on the line as integers. 

    Args:
        data (list): Puzzle input as a list of each line as a str

    Returns:
        list: Re-formatted data
    """
    new_data = [[int(i) for i in line.split()] for line in data]
    return new_data


def reduce(line: list):
    """Reduces a line to one fewer elements by
    generating new elements m_i = n_i+1 - n_i 
    from the elements in the input. 

    Args:
        line (list): list of values to reduce  

    Returns:
        list: reduced value
    """
    reduced_line = [line[i+1]-line[i] for i in range(len(line)-1)]
    return reduced_line


def solution1(data: list) -> int:
    """Solution to part 1. Extrapolates new lines in which each element is the
    difference between the two elements above it, 
    until reaching a line with identical values.
    Then extends the line with identical values to the right by 1 element and
    extrapolates the extended value on each line until reaching the initial line.
    This corresponds to alternating between adding and subtracting the first 
    value on non-extended line to the first value of the initial line.
    Returns the sum of the extrapolated value on the initial line for
    all lines in the input.

    Args:
        data (list): Puzzle input as a list with each line as a list of int values.

    Returns:
        int: Sum of all extrapolated.
    """
    sum_extrapolated = 0
    for line in data:
        new_val = line[-1]
        while len(set(line)) > 1:
            line = reduce(line)
            new_val += line[-1]
        sum_extrapolated = new_val + sum_extrapolated

    return sum_extrapolated


def solution2(data: list) -> int:
    """Solution to part 2. Extrapolates new lines in which each element is the
    difference between the two elements above it, 
    until reaching a line with identical values.
    Then extends the line left with identical values to the left by 1 element and
    extrapolates the extended value on each line until reaching the initial line. 
    This corresponds to taking the sum of the last value for 
    all non-extended lines. 
    Returns the sum of the extrapolated value on the initial line for
    all lines in the input.

    Args:
        data (list): Puzzle input as a list with each line as a list of int values.

    Returns:
        int: Sum of all extrapolated.
    """
    sum_extrapolated = 0
    for line in data:
        new_val = line[0]
        while len(set(line)) > 1:
            line = reduce(line)
            # Alternate between subtracting and adding the first value on each line
            if (NUM_PER_LINE-len(line)) % 2 == 1:
                new_val -= line[0]
            else:
                new_val += line[0]
        sum_extrapolated = new_val + sum_extrapolated

    return sum_extrapolated


if __name__ == "__main__":
    data = read_file(9)
    data = parse_data(data)
    NUM_PER_LINE = len(data[0])

    print(f'Solution to part 1: {solution1(data)}')
    print(f'Solution to part 1: {solution2(data)}')

import regex as re
from aoc_common import read_file


def first_last(line, pattern):
    """Finds the first and last occurance of digits in a string and 
    returns the number gotten from combining them (7 and 2 --> 72).

    Args:
        line (str): The string to search
        pattern (re.Pattern): Pattern to serach with

    Returns:
        int: Output number as a combination of the first and last digits.
    """
    # Must handle overlaps. 'twone' should be treated as "two, one"
    # but results in only "two" using the standard re module.
    matches = re.findall(pattern, line, overlapped=True)
    digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4,
              'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
              '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    first_num = digits[matches[0]]
    last_num = digits[matches[-1]]

    return first_num*10 + last_num


def calibration_number(data, re_pattern):
    """Finds the number made from the first and last digit on each line in data, as identified by the provided regex pattern.
    Returns the sum of the numbers from all lines.

    Args:
        data (list): A list of lines of text to parse.
        re_pattern (re.Pattern): Compiled regex pattern for identifying digits.

    Returns:
        int: Sum of numbers from all lines.
    """
    calibration_sum = 0
    for line in data:
        calibration_sum += first_last(line, re_pattern)

    return calibration_sum


if __name__ == "__main__":
    data = read_file(1)

    # Part 1
    # Find the calibration value on each line using the first and last number on the line
    # 1abc3 -> 13
    # Return the sum of all calibration values in the file
    pattern_1 = re.compile(r'1|2|3|4|5|6|7|8|9')
    solution_part_1 = calibration_number(data, pattern_1)
    print(solution_part_1)

    # Part 2
    # The calibration value can also be spelled out
    # 1abc3five -> 15
    pattern_2 = re.compile(
        r'1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine')
    solution_part_2 = calibration_number(data, pattern_2)
    print(solution_part_2)

from aoc_common import read_file
import regex as re


def get_numbers_symbols(data):
    """Finds all numbers and symbols and stores their positions (row, col_0-col_n).
    Returns a list of numbers with positions and a list of symbols with positions.

    Args:
        data (list): List of strings to parse.

    Returns:
        list: List of numbers with positions and list of symbols with positions.
    """
    numbers = []
    symbols = []
    for row, line in enumerate(data):
       # Find numbers
        for nmatch in re.finditer(r'\d+', line):
            if nmatch:
                col = nmatch.span()
                num = int(nmatch.group())
                numbers.append([num, row, col])
        # Find all symbols (anything non-numberic except ".")
        for smatch in re.finditer(r'[^0-9.]{1}', line):
            if smatch:
                col = smatch.span()
                symb = smatch.group()
                symbols.append([symb, row, col])

    return numbers, symbols


def compare_positions(number_info, symbol_info):
    """Finds numbers with a symbol within 1 row and 1 column of each other.
    Returns "numfarabove" if the number row is too low (num_row < sym_row-1),
    "numfarbelow" if the number row is too high (num_row > sym_row+1),
    and "adjacent" if the symbol and number are adjacent on both rows and columns.

    Args:
        number_info (list): List of number value, row, and columns
        symbol_info (list): List of symbol, row, and columns

    Returns:
        str: String describing relative positions.
    """
    num_row = number_info[1]
    sym_row = symbol_info[1]
    if num_row < sym_row-1:
        return 'numfarabove'
    if num_row > sym_row+1:
        return 'numfarbelow'
    # Symbol within 1 row of the number (all remaining)
    # Symbol within 1 column of the number
    num_col = (number_info[2][0], number_info[2][1])
    symbol_col = symbol_info[2][0]
    if symbol_col in range(num_col[0]-1, num_col[1]+1):
        return 'adjacent'


def get_adjacent(numbers_list, symbols_list):
    """Finds all numbers with an adjacent symbol and 
    returns a list with their values and positions.

    Args:
        numbers_list (list): List of numbers with values and positions.
        symbols_list (list): List of symbols with values and positions.

    Returns:
        int: Sum of all numbers with adjacent symbols.
        list: List of value and position for numbers with adjacent symbols.
    """    
    # Make sure lists are sorted by row number for optimizations to work
    numbers_list.sort(key=lambda x: x[1])
    symbols_list.sort(key=lambda x: x[1])

    matches = []
    # Loop in reversed order to efficiently pop orphaned numbers
    for symbol_info in reversed(symbols_list):
        for number_info in reversed(numbers_list):
            number_position = compare_positions(number_info, symbol_info)
            if number_position == 'adjacent':
                matches.insert(0, number_info)
            # Reached numbers outside symbol reach (rows) - move to next symbol.
            elif number_position == 'numfarabove':
                break
            # "Orphaned" number below the furthest down symbol.
            # Discard to avoid repeatedly checking against symbols. 
            elif number_position == 'numfarbelow':
                numbers.pop()

    return matches


def solution1(numbers_list):
    """Returns the sum of all number values in the provided list of numbers.

    Args:
        numbers_list (list): List of numbers with values and positions.

    Returns:
        int: Sum of number values
    """    
    sum_of_valid = 0
    for number_info in numbers_list:
        sum_of_valid += number_info[0]
    
    return sum_of_valid
    


def solution2(numbers_list, symbols_list):
    """Finds all "*" symbols with more than 1 adjacent number, 
    calculates the product (gear ratio) of numbers sharing the same "*".
    Returns the sum of all gear ratio products.

    Args:
        numbers_list (list): List of number values and positions
        symbols_list (list): List of symbols and their positions

    Returns:
        int: Sum of gear ratios.
    """    
    # Make sure lists are sorted by row number for optimizations to work
    numbers_list.sort(key=lambda x: x[1])
    symbols_list.sort(key=lambda x: x[1])

    sum_gear_ratio = 0
    for symbol_info in reversed(symbols_list):
        if symbol_info[0] == '*':
            current_symbol_matches = []
            for number_info in reversed(numbers_list):
                position = compare_positions(number_info, symbol_info)
                # Reached numbers outside symbol reach (rows) - move to next symbol.
                if position == 'numfarabove':
                    break
                elif position == 'adjacent':
                    current_symbol_matches.append(number_info[0])
            
            # Calculate gear ratio when multiple numbers are adjacent
            if len(current_symbol_matches) > 1:
                gear_ratio = 1
                for num in current_symbol_matches:
                    gear_ratio *= num
                sum_gear_ratio += gear_ratio

    return sum_gear_ratio


if __name__ == "__main__":
    # Extract position of all numbers and symbols
    data = read_file(day_number=3)
    numbers, symbols = get_numbers_symbols(data)

    # List of numbers with an any adjacent symbol
    parts = get_adjacent(numbers, symbols)

    print(f'Solution to part 1: {solution1(parts)}')
    print(f'Solution to part 2: {solution2(parts, symbols)}')

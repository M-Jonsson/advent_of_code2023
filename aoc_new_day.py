import sys
from os.path import exists


def new_file(day_num: int):
    """Generates new files for a day of Advent of Code. 
    Generates a .py for the code and a .txt in /data to store the puzzle input
    on the format day{day_num}.py and day{day_num}_input.txt as long as the 
    files do not already exist.

    Args:
        day_num (int): Day number to use in the file names.
    """    
    if not exists(f'day{day_num}.py'):
        # Python file
        lines = ['from aoc_common import read_file',
                 'def solution1(data):', '\tpass',
                 'def solution2(data):', '\tpass',
                 'if __name__ == "__main__":',
                 f'\tdata = read_file({day_num})',
                 '\tprint(f"Solution to part 1: {solution1(data)}")',
                 '\tprint(f"Solution to part 2: {solution2(data)}")']
        with open(f'day{day_num}.py', 'w') as file:
            file.write('\n'.join(str(line) for line in lines))
        # Input txt file
        with open(f'data/day{day_num}_input.txt', 'a'):
            pass
    else:
        print('Python file already exists.')

if __name__=='__main__':
    try:
        day_num = int(sys.argv[1])
    except IndexError:
        exit()
    except ValueError:
        exit()

    new_file(day_num)
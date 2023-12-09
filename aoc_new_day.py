import sys


def new_file(day_num: int):
    """Generates files for a day of Advent of Code.
    Generates a .py for the code and a .txt in /data to store the puzzle input
    on the format day{day_num}.py and day{day_num}_input.txt.

    Args:
        day_num (int): Day number to use in the file names.
    """    
    # Python file
    with open(f'day{day_num}.py', 'a'):
        pass

    # Input txt file
    with open(f'data/day{day_num}_input.txt', 'a'):
        pass

if __name__=='__main__':
    try:
        day_num = int(sys.argv[1])
    except IndexError:
        exit()
    except ValueError:
        exit()

    new_file(day_num)
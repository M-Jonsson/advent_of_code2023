from time import perf_counter

def read_file(day_number: int):
    '''Read data from file for a given day, with the day number given as an int.
    Returns a list of lines, with each line stripped from white-spaces.'''
    file_data = []
    file_name = f'data/day{day_number}_input.txt'
    with open(file_name, 'r') as file:
        for line in file:
            file_data.append(line.strip())
    return file_data
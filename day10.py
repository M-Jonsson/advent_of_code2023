from aoc_common import read_file



def find_start(data: list):
    """Finds the position of the starting tile marked by 'S'.

    Args:
        data (list): List of str to search in.

    Returns:
        tuple: Coordinate position.
    """    
    for row, line in enumerate(data):
        for col, pipe in enumerate(line):
            if pipe == 'S':
                return (row, col)


def get_pipe(position: tuple):
    """Returns the pipe type at the specified position.

    Args:
        position (tuple): Position coordinates.

    Returns:
        str: Pipe type at the new position.
    """    
    return data[position[0]][position[1]]


def valid_move(new_position: tuple, direction: str):
    """Check if a move is valid by checking if the pipe at the new position allows
    for entry from the movement direction.

    Args:
        new_position (tuple): Coordinates for the position you are moving to.
        direction (str): Movement direction.

    Returns:
        bool: Move is valid or not.
    """    
    new_pipe = get_pipe(new_position)
    if direction in VALID_MOVES[new_pipe].keys():
        return True
    else:
        return False


def move(position: tuple, direction: str):
    """Moves 1 step along the pipe loop.
    Finds the new position and movement direction 
    based on the current position and movement direction.

    Args:
        position (tuple): Coordinate position of starting tile.
        direction (str): Direction of movement.

    Returns:
        tuple: Coordinate position of the new tile.
        str: Updated direction of movement based on pipe type on the new tile.
    """    
    # New coordinates
    if direction == 'N':
        next_pos = (position[0]-1, position[1])
    elif direction == 'W':
        next_pos = (position[0], position[1]-1)
    elif direction == 'S':
        next_pos = (position[0]+1, position[1])
    elif direction == 'E':
        next_pos = (position[0], position[1]+1)

    # Check move validity and get new direction base on pipe type
    if valid_move(next_pos, direction):
        dir_choices = VALID_MOVES[get_pipe(next_pos)]
        next_dir = dir_choices[direction]
        return next_pos, next_dir
    else:
        return None, None


def solution1(data: list):
    """Solution to part 1. Checks all 4 cardinal directions and finds the 
    longest possible path that connects back to the starting tile. Returns
    the number of steps to the tile furthest from the start, which is 
    half the distance of the longest loop.

    Args:
        data (list): Puzzle input as a list of str.

    Returns:
        int: Steps to the tile furthest from the start.
    """
    start_pos = find_start(data)
    longest_path = 0

    for dir in DIRECTIONS:
        position, dir = move(start_pos, dir)
        moves = 1

        # Follow pipe until back at start or no valid moves (pipe blocked)
        while position and position != start_pos:
            position, dir = move(position, dir)
            moves += 1
        
        # Track longest path based on starting direction
        if moves > longest_path:
            longest_path = moves
    
    return longest_path/2


if __name__ == "__main__":
    data = read_file(10)
    VALID_MOVES = {'|': {'N': 'N', 'S': 'S'},
                   '-': {'E': 'E', 'W': 'W'},
                   'L': {'S': 'E', 'W': 'N'},
                   'J': {'S': 'W', 'E': 'N'},
                   '7': {'N': 'W', 'E': 'S'},
                   'F': {'N': 'E', 'W': 'S'},
                   'S': {}}
    DIRECTIONS = ['N', 'W', 'S', 'E']
    print(f'Solution to part 1: {solution1(data)}')
    # print(f'Solution to part 2: {solution2(data)}')

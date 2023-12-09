from aoc_common import read_file
import regex as re


def max_rgb(data_input):
    """Extracts game id and maximum number of cubes drawn for each game, 
    considering all rounds. Works on the format 
    "Game xx: aa colour1, bb colour2; cc colour1, dd colour3", 
    where ; separates rounds within a single game.
    Returns a list with id and the maximum number of 
    red, green, and blue cubes drawn over all rounds in each game.

    Args:
        data_input (list): List of strings with game information.

    Returns:
        list: List of lists with game id and maximum of each cube drawn over all rounds in each game.
    """
    def max_int(text, colour):
        """Extracts the number of cubes of a specified colour drawn in all rounds of a game and returns the maximum.

        Args:
            text (str): String to search in.
            colour (str): Colour to search for

        Returns:
            int: Maximum number found.
        """
        # Finds n in all occurances of "n colour"
        matches = re.findall(fr'\d+\s{colour}', text)
        num = [int(match.split()[0])
               for match in matches]
        return max(num)

    rgb_by_id = []
    for line in data_input:
        # id is the first number found
        game_id = int(re.search(r'\d+', line).group())
        red_max = max_int(line, 'red')
        green_max = max_int(line, 'green')
        blue_max = max_int(line, 'blue')
        rgb_by_id.append([game_id, red_max, green_max, blue_max])

    return rgb_by_id


def solution1(data):
    """Finds the id of games where at most 12 red, 13 green, and 14 blue cubes
    were drawn over all rounds of the game. 
    Returns the sum of the id of all such games.

    Args:
        data (list): List of game id and maximum of each cube for each game.

    Returns:
        int: Sum of winning game ids.
    """
    sum_of_valid = 0
    for game in data:
        game_id = game[0]
        red_max = game[1]
        green_max = game[2]
        blue_max = game[3]

        if red_max <= 12 and green_max <= 13 and blue_max <= 14:
            sum_of_valid += game_id

    return sum_of_valid


def solution2(data):
    """Calculates the product of the maximum number of 
    red, green, and blue cubes drawn in each game and 
    returns the sum of the product from all games.

    Args:
        data (list): List of game id and maximum of each cube for each game.

    Returns:
        int: Sum of products of maximum cubes per game.
    """
    sum_power = 0
    for game in data:
        red_max = game[1]
        green_max = game[2]
        blue_max = game[3]
        sum_power += red_max * green_max * blue_max
    return sum_power


if __name__ == "__main__":
    data = read_file(2)
    max_rgb_by_id = max_rgb(data)

    print(f'Solution to part 1: {solution1(max_rgb_by_id)}')
    print(f'Solution to part 1: {solution2(max_rgb_by_id)}')

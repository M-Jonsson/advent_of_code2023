from aoc_common import read_file
import regex as re
from math import sqrt, ceil, floor


def convert_input(data):
    '''Extracts the race times and distances.
    Returns a list with (time, distance) tuples for each race.
    '''
    times = re.findall(r'\d+', data[0])
    distances = re.findall(r'\d+', data[1])
    new_data = []
    for i in range(len(times)):
        new_data.append((int(times[i]), int(distances[i])))

    return new_data


def solve_polynomial(time, max_distance):
    '''Calculates roots to
    max_distance=x(time-x) w.r.t. x.
    Returns a tuple of the roots with the larger root first.
    '''
    x_1 = ceil(time/2 - sqrt((time/2)**2-max_distance))
    x_2 = floor(time/2 + sqrt((time/2)**2-max_distance))

    return (x_1, x_2)


def solution1(data):
    '''Solves the number of winning possibilites as a 2nd order polynomial.
    Returns the product of the number of wins for all races.
    '''
    all_races = convert_input(data)
    total_margin = 1
    for race in all_races:
        # Roots are the button hold time that ties the record
        roots = solve_polynomial(race[0], race[1])
        # Margin - number of integers between the roots
        margin = roots[1]-roots[0]+1
        total_margin *= margin

    return total_margin


def solution2(data):
    '''Finds the number of ways to win a race
    by solving distance=holding_time*(total_time-holding_time).
    
    Returns the number of possible winning outcomes.
    '''
    time = int(''.join(re.findall(r'\d+', data[0])))
    max_distance = int(''.join(re.findall(r'\d+', data[1])))
    roots = solve_polynomial(time, max_distance)

    return roots[1]-roots[0]+1



if __name__ == '__main__':
    data = read_file(6)
    print(solution1(data))
    print(solution2(data))

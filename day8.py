from aoc_common import read_file
import regex as re
from math import lcm


def parse_data(data: list) -> dict:
    """Converts the list of lines (str) puzzle input to a dict that maps 
    nodes and their destinations.

    Args:
        data (list): List of lines (str) from the puzzle input.

    Returns:
        dict: Dict mapping nodes to their destinations.
    """
    nodes = {}
    node_pattern = re.compile(r'[A-Z]{3}')
    for line in data:
        nodes_raw = re.findall(node_pattern, line)
        if nodes_raw:
            nodes[nodes_raw[0]] = (nodes_raw[1], nodes_raw[2])

    return nodes


def calculate_steps(instructions: str, nodes: dict, start: str, stop: callable) -> int:
    """Finds the number of steps required to go from 
    the start node to the stop node when walking according to the
    provided instructions.

    Args:
        instructions (str): String of walking directions with 0 or 1 for left or right.
        nodes (dict): Dictionary of nodes and their destinations.
        start (str): Starting node.
        stop (function): Function to determine if at a stop node.

    Returns:
        int: Number of steps.
    """
    steps = 0
    node = start
    while True:
        for direction in instructions:
            steps += 1
            alternatives = nodes[node]
            node = alternatives[int(direction)]
            if stop(node):
                return steps


def solution1(instructions: str, nodes: dict) -> int:
    """Solution to part 1. Finds to number of steps to go from node 'AAA' to
    node 'ZZZ' when walking according to the provided instructions.

    Args:
        instructions (str): String of walking directions with 0 or 1 for left or right.
        nodes (dict): Dictionary of nodes and their destinations.

    Returns:
        int: Number of steps.
    """
    start = 'AAA'
    def stop(x): return x == 'ZZZ'
    steps = calculate_steps(instructions, nodes, start, stop)

    return steps


def solution2(instructions: str, nodes: dict) -> int:
    """Solution to part 2. Calculates the number of steps when
    simultaneously walking from all starting node (ends with A) according to
    the provided instructions until all paths have reached an end node
    (ends with Z) at the same time.

    Args:
        instructions (str): String of walking directions with 0 or 1 for left or right.
        nodes (dict): Dictionary of nodes and their destinations.

    Returns:
        int: Number of steps.
    """
    starting_nodes = [node for node in nodes.keys() if node[2] == 'A']
    def stop(x): return x[2] == "Z"

    # Steps to goal for each individual path
    steps_from_start = []
    for start in starting_nodes:
        steps_from_start.append(calculate_steps(
            instructions, nodes, start, stop))

    # Steps until all paths are simultaneouls at an end node is the
    # least common multiple of number of steps in the individual paths.
    return lcm(*steps_from_start)


if __name__ == "__main__":
    data = read_file(8)
    instructions = data[0].replace('L', '0').replace('R', '1')
    nodes = parse_data(data[1:])

    print(
        f'Solution to part 1: {solution1(instructions, nodes)}')
    print(f'Solution to part 1: {solution2(instructions, nodes)}')

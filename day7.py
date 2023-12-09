from aoc_common import read_file
from collections import Counter


def get_type(counts):
    """Determines the hand type from the card counts.

    Args:
        counts (list): Pre-sorted list of counts for each unique card in the hand.

    Returns:
        str: Hand type
    """
    if counts == [1, 1, 1, 1, 1]:
        return 'high card'
    elif counts == [1, 1, 1, 2]:
        return 'one pair'
    elif counts == [1, 2, 2]:
        return 'two pair'
    elif counts == [1, 1, 3]:
        return 'three of a kind'
    elif counts == [2, 3]:
        return 'full house'
    elif counts == [1, 4]:
        return 'four of a kind'
    elif counts == [5]:
        return 'five of a kind'
    else:
        return ''


def calculate_score(hands_dict):
    """Calculates the score from all hands by the bet and relative rank of each hand.

    Args:
        hands_dict (dict): A pre-sorted dictionary with hands, separated by hand type.

    Returns:
        int: Final score
    """
    rank = 1
    winnings = 0
    for ty in hands_dict.keys():
        for hand in hands_dict[ty]:
            winnings += hand[1]*rank
            rank += 1

    return winnings


def sort_hands(dict, rule):
    """Internally sort each dict value (a list) according to the provided sorting rule.
    Starts by sorting on the first character and breaks ties by looking at subsequent characters.

    Args:
        dict (dict): Dictionary to sort
        rule (dict): Dicitonary with sorting rules
    """
    for d in dict.values():
        d.sort(key=lambda x: (rule[x[0][0]], rule[x[0][1]],
                              rule[x[0][2]], rule[x[0][3]], rule[x[0][4]]))


def solution1(data_input):
    """Solution to part 1. Determines the type of each hand in the input,
    ranks hands relative to each other and calculates the final score
    based on the rank and initial bet of each hand.

    Args:
        data_input (list): List of (str(hand), int(bet)) tuples

    Returns:
        int: Score from all hands in the input.
    """
    hands_by_type = {'high card': [],
                     'one pair': [],
                     'two pair': [],
                     'three of a kind': [],
                     'full house': [],
                     'four of a kind': [],
                     'five of a kind': []}
    for hand in data_input:
        counts = sorted(Counter(hand[0]).values())
        hand_type = get_type(counts)
        hands_by_type[hand_type].append(hand)

    sort_hands(hands_by_type, SORT_RULE_STANDARD)
    score = calculate_score(hands_by_type)

    return score


def solution2(data_input):
    """Solution to part 2. Determines the best possible type of each hand, 
    allowing for jokers to become any other card. Ranks hands relative to
    each other and calculates the final score based on the rank and initial
    bet of each hand. 

    Args:
        data_input (list): List of (str(hand), int(bet)) tuples

    Returns:
        int: Score from all hands in the input.
    """
    hands_by_type = {'high card': [],
                     'one pair': [],
                     'two pair': [],
                     'three of a kind': [],
                     'full house': [],
                     'four of a kind': [],
                     'five of a kind': []}
    for hand in data_input:
        # Get counts for hand except joker cards
        hand_no_jokers = hand[0].replace('J', '')
        counts = sorted(Counter(hand_no_jokers).values())

        # Emulate counts with jokers added back as best possible hand
        # and handle special case of 5 jokers
        if counts:
            counts[-1] = counts[-1]+hand[0].count('J')
        else:
            counts = [5]

        hand_type = get_type(counts)
        hands_by_type[hand_type].append(hand)

    sort_hands(hands_by_type, SORT_RULE_JOKER)
    score = calculate_score(hands_by_type)

    return score


if __name__ == "__main__":
    SORT_RULE_STANDARD = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                          '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    SORT_RULE_JOKER = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                       '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 12, 'K': 13, 'A': 14}
    data = read_file(7)
    # Format data as a list of ('hand', bet) tuples
    data = [(line.split()[0], int(line.split()[1]))
            for line in data]

    print(f'Solution to part 1: {solution1(data)}')
    print(f'Solution to part 2: {solution2(data)}')

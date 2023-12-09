from aoc_common import read_file
from collections import Counter


def get_type(hand):
    # Quick identificatin of simple hands
    uniques = set(hand)
    if len(uniques) == 5:  # High card
        return 'high card'
    elif len(uniques) == 4:  # One pair
        return 'one pair'
    elif len(uniques) == 1:  # Five of a kind
        return 'five of a kind'

    # Differentiate more complex hands
    counts = sorted(Counter(hand).values())
    if counts == [1, 2, 2]:  # Two pair
        return 'two pair'
    elif counts == [1, 1, 3]:  # Three of a kind
        return 'three of a kind'
    elif counts == [2, 3]:  # Full house
        return 'full house'
    elif counts == [1, 4]:  # Four of a kind
        return 'four of a kind'


def sort_internal(ties):
    sort_order = {'2': 2, '3': 3, '4': 4, '5': 5, 
                  '6': 6, '7': 7, '8': 8, '9': 9, 
                  'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    ties.sort(key=lambda x: (sort_order[x[0]], sort_order[x[1]], sort_order[x[2]], sort_order[x[3]], sort_order[x[4]]))


def solution1(data_dict):
    hands_by_type = {'high card': [],
                     'one pair': [],
                     'two pair': [],
                     'three of a kind': [],
                     'full house': [],
                     'four of a kind': [],
                     'five of a kind': []}
    for hand in data_dict.keys():
        hand_type = get_type(hand)
        hands_by_type[hand_type].append(hand)
        
    rank = 1
    winnings = 0
    for ty in hands_by_type.keys():
        sort_internal(hands_by_type[ty])
        for hand in hands_by_type[ty]:
            winnings += data_dict[hand]*rank
            rank += 1




    return winnings


if __name__ == "__main__":
    data = read_file(7)
    data_as_dict = {}
    for hand in data:
        h = hand.split()
        data_as_dict[h[0]] = int(h[1])
    # data = [hand.split()[0], int(hand.split()[1]))
    #         for hand in data]
    from time import perf_counter
    s = perf_counter()
    print(f'Solution to part 1: {solution1(data_as_dict)}')
    print(perf_counter()-s)

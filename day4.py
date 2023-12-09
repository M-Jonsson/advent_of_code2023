from aoc_common import read_file
import regex as re


def get_overlap(card):
    """Finds overlap between the winning numbers and the "numbers you have", 
    separated by a vertical bar. 
    Returns a list of all overlaps.

    Args:
        card (str): String to extract numbers from.

    Returns:
        set: Set of overlapping numbers.
    """
    numbers = re.findall(r'[|\d]+', card)
    # Index of the vertical bar separates winning numbers and numbers you have
    bar = numbers.index('|')
    winning = {int(num) for num in numbers[1:bar]}
    numbers_have = {int(num) for num in numbers[bar+1:]}
    # Set union to find overlap
    matches = winning & numbers_have

    return matches


def solution1(cards):
    """Scores each card based on the number of overlapping numbers (n) between
    the winning numbers and the "numbers you have" according to 2^(n-1),
    or 0 when there are no matches. 
    Returns the sum of the scores from all cards.

    Args:
        cards (list): List of strings describing the cards in the deck.

    Returns:
        int: Sum of score of each card.
    """
    sum_of_scores = 0
    for card in cards:
        overlap = get_overlap(card)
        if overlap:
            score = 2**(len(overlap)-1)
            sum_of_scores += score

    return sum_of_scores


def solution2(cards):
    """Calculates the number of overlaps (n) between winning numbers and
    'numbers you have' on the current card and adds 
    another copy of the next n cards to deck.
    Returns the total number of cards in the deck 
    when all cards have been scored.

    Args:
        cards (list): List of strings describing the cards in the deck.

    Returns:
        int: The number of cards in the deck after scoring all cards.
    """
    # Start with 1 copy of each card
    copies_per_card = [1]*len(cards)

    for i, card in enumerate(cards):
        matches = get_overlap(card)
        if matches:
            score = len(matches)
            # Increase the n=score next elements
            # by the number of copies of the current card
            copies_per_card[i+1:i+1+score] = [copy_num+copies_per_card[i]
                                              for copy_num in copies_per_card[i+1:i+1+score]]

    return sum(copies_per_card)


if __name__ == "__main__":
    data = read_file(4)

    print(f'Solution to part 1: {solution1(data)}')
    print(f'Solution to part 2: {solution2(data)}')

# hand_evaluator.py

from treys import Evaluator, Card as TreysCard

def evaluate_hand(hole_cards, community_cards):
    evaluator = Evaluator()
    hole_cards_converted = [convert_card(card) for card in hole_cards]
    community_cards_converted = [convert_card(card) for card in community_cards]
    score = evaluator.evaluate(community_cards_converted, hole_cards_converted)
    return score

def convert_card(card):
    rank_conversion = {
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': 'T',
        'Jack': 'J',
        'Queen': 'Q',
        'King': 'K',
        'Ace': 'A'
    }

    suit_conversion = {
        'Hearts': 'h',
        'Diamonds': 'd',
        'Clubs': 'c',
        'Spades': 's'
    }

    rank = rank_conversion.get(card.rank)
    suit = suit_conversion.get(card.suit)

    if rank is None or suit is None:
        raise ValueError(f"Invalid card: {card.rank} of {card.suit}")

    treys_card_str = rank + suit
    return TreysCard.new(treys_card_str)

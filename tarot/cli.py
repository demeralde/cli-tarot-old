import random
from typing import List

from art import text2art

from tarot.cards import DEFAULT_DECK
from tarot.card import Card


class CLI:
    used_cards: List[int] = []

    def __init__(self):
        self._print_intro()
        card = Card(**self._get_card())
        card.get()
        # self._get_spread(1)

    def _print_intro(self):
        print(text2art("CLI   TAROT", font="big"))

    def _get_card_index(self):
        return random.randint(0, len(DEFAULT_DECK) - 1)

    def _get_card(self):
        index = self._get_card_index()
        card = DEFAULT_DECK[index]
        self.used_cards.append(index)
        return card

    def _get_spread(self, count=1):
        for card_no in range(count):
            card = self._get_card()
            self._print_card(card)
        print(self.used_cards)

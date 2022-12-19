import random
from typing import List

from tarot.card import Card
from tarot.cards import DEFAULT_DECK
from tarot.types import CardList


class Deck:
    cards: List[Card]
    name: str

    def __init__(self) -> None:
        self.name = "Rider Waite"
        self.cards = self._load_cards(DEFAULT_DECK)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Deck({self.name})"

    def _load_cards(self, cards: CardList) -> List[Card]:
        self.cards = []

        for card in cards:
            self.cards.append(Card(**card))

        return self.cards

    def _exclude_cards(self, cards: List[Card], exclude: List[int]) -> None:
        for index in exclude:
            cards.pop(index)

    def get_card(self, **kwargs) -> Card:
        available_cards = self.cards.copy()
        excluded_cards = kwargs.get("exclude", None)

        if excluded_cards:
            self._exclude_cards(available_cards, excluded_cards)

        return random.choice(available_cards)

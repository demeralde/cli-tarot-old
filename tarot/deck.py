import random
from typing import List

from tarot.card import Card
from tarot.types import CardTuple


class Deck:
    cards: List[Card]
    name: str

    def __init__(self, **kwargs) -> None:
        self.name = kwargs["name"]
        self.cards = self._load_cards(kwargs["cards"])

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Deck({self.name})"

    def _load_cards(self, cards: CardTuple) -> List[Card]:
        self.cards = []

        for card in cards:
            self.cards.append(Card(card))

        return self.cards

    def _exclude_cards(self, cards: List[Card], exclude: List[int]) -> None:
        for index in exclude:
            cards.pop(index)

    def get_card(self, exclude: List[int]) -> Card:
        available_cards = self.cards.copy()

        if exclude:
            self._exclude_cards(available_cards, exclude)

        return random.choice(available_cards)

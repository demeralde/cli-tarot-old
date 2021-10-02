from tarot.deck import Deck
from tarot.types import SpreadItems, SpreadItem, SpreadUsedCards


class Spread:
    deck: Deck
    used_cards: SpreadUsedCards
    name: str
    items: SpreadItems

    def __init__(self, **kwargs) -> None:
        self.name = kwargs["name"]
        self.deck = kwargs["deck"]
        self.items = kwargs["items"]

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Spread({self.name})"

    def _print_item(self, item: SpreadItem):
        if "name" in item:
            print(item["name"])

    def _get_cards(self):
        for index, item in enumerate(self.items):
            self._print_item(item)
            card = self._get_card()
            self._print_card(card)

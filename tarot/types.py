from typing import Dict, Union, Tuple, List, Callable

TemplateSpecs = Dict[str, int]
TemplateGraphics = Dict[str, str]

Col = str
Row = List[str]
GridSpecsItem = Dict[str, bool]
GridSpecs = Dict[str, GridSpecsItem]
Grid = List[Row]

CardGraphicsSpecs = Dict[str, int]
Card = Dict[str, Union[str, CardGraphicsSpecs]]
CardTuple = Tuple[Card]
Deck = Dict[str, Union[CardTuple, str]]

EnumerateRowAction = Callable[[Row, int, Col], None]

SpreadUsedCards = List[Card]
SpreadItem = Dict[str, str]
SpreadItems = List[SpreadItem]
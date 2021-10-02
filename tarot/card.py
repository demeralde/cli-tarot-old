import math

from tarot.template import TEMPLATE_SPECS, TEMPLATE_GRAPHICS
from tarot.types import (
    Row,
    Grid,
    Col,
    GridSpecsItem,
    GridSpecs,
    CardGraphicsSpecs,
    EnumerateRowAction,
    TemplateGraphics,
    TemplateSpecs,
)


class Card:
    template_specs: TemplateSpecs
    template_graphics: TemplateGraphics
    title: str
    subtitle: str
    description: str
    graphics: str
    graphics_specs: CardGraphicsSpecs

    def __init__(self, **kwargs) -> None:
        self.title = kwargs["title"]
        self.subtitle = kwargs["subtitle"]
        self.description = kwargs["description"]
        self.graphics = kwargs["graphics"]
        self.graphics_specs = kwargs["graphics_specs"]

        self.template_specs = TEMPLATE_SPECS
        self.template_graphics = TEMPLATE_GRAPHICS

    def __str__(self) -> str:
        return f"{self.title} - {self.subtitle}"

    def __repr__(self) -> str:
        return f"Card({self.title})"

    def _get_col_specs(self, col: int) -> GridSpecsItem:
        last_col = self.template_specs["width"] - 1
        is_first: bool = col == 0
        is_last: bool = col == last_col

        return {
            "is_first": is_first,
            "is_last": is_last,
            "is_edge": is_first or is_last,
        }

    def _get_row_specs(self, row: int) -> GridSpecsItem:
        last_row = self.template_specs["height"] - 1
        is_first: bool = row == 0
        is_last: bool = row == last_row

        return {
            "is_first": is_first,
            "is_last": is_last,
            "is_edge": is_first or is_last,
        }

    def _get_misc_specs(
        self, row_specs: GridSpecsItem, col_specs: GridSpecsItem
    ) -> GridSpecsItem:
        is_corner: bool = col_specs["is_edge"] and row_specs["is_edge"]
        is_side_x: bool = not is_corner and row_specs["is_edge"]
        is_side_y: bool = col_specs["is_edge"] and not is_corner

        return {
            "is_corner": is_corner,
            "is_side_x": is_side_x,
            "is_side_y": is_side_y,
            "is_middle": not is_corner and not is_side_x and not is_side_y,
        }

    def _get_footer_specs(self, row: int, col_specs: GridSpecsItem) -> GridSpecsItem:
        footer_start: int = (
            self.template_specs["height"] - self.template_specs["footer_height"]
        )
        is_start: bool = row == footer_start

        return {
            "is_start": is_start,
            "is_border": is_start and not col_specs["is_edge"],
            "is_corner": col_specs["is_edge"] and is_start,
        }

    def _get_graphics_specs(self, row: int, col: int, misc_specs: GridSpecsItem):
        misc_specs["is_middle"]
        margin: int = 1
        padding_total: int = (
            self.template_specs["width"] - self.graphics_specs["width"] - (margin * 2)
        )
        padding: int = math.floor(padding_total / 2)

    def _get_specs(self, row: int, col: int) -> GridSpecs:
        col_specs = self._get_col_specs(col)
        row_specs = self._get_row_specs(row)
        misc_specs = self._get_misc_specs(row_specs, col_specs)
        return {
            "col": col_specs,
            "row": row_specs,
            "misc": misc_specs,
            "footer": self._get_footer_specs(row, col_specs),
        }

    def _generate_row(self, index: int) -> Row:
        row = []

        for col in range(self.template_specs["width"]):
            specs = self._get_specs(index, col)
            self._get_graphics_specs(index, col, specs["misc"])
            is_corner = specs["misc"]["is_corner"] or specs["footer"]["is_corner"]
            is_side_x = specs["misc"]["is_side_x"] or specs["footer"]["is_border"]

            if is_corner:
                row.append(self.template_graphics["corner"])
            elif is_side_x:
                row.append(self.template_graphics["side_x"])
            elif specs["misc"]["is_side_y"]:
                row.append(self.template_graphics["side_y"])
            elif specs["misc"]["is_middle"]:
                row.append(" ")

        return row

    def _generate_rows(self) -> Grid:
        rows = []
        height = self.template_specs["height"]

        for row in range(height):
            rows.append(self._generate_row(row))

        return rows

    def _enumerate_row(self, row: Row, action: EnumerateRowAction) -> None:
        for index, col in enumerate(row):
            action(row, index, col)

    def _print_col(self, row: Row, index: int, value: Col) -> None:
        is_last_col = index == len(row) - 1
        print(value, end="\n" if is_last_col else "")

    def _print_cols(self, row) -> None:
        self._enumerate_row(row, self._print_col)

    def _print_description(self) -> None:
        print(self.description)

    def render(self) -> None:
        cols = self._generate_rows()

        for row in cols:
            self._print_cols(row)

        self._print_description()
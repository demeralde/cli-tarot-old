import random

from art import text2art
from prompt_toolkit import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import VSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.key_binding import KeyBindings

from tarot.deck import Deck


class CLI:

    def __init__(self):
        self._print_intro()
        self._init_app()

    def _print_intro(self):
        print(text2art("CLI   TAROT", font="big"))

    def _init_app(self):
        buffer1 = Buffer()
        root_container = VSplit([
            Window(content=BufferControl(buffer=buffer1)),
            Window(width=1, char='|'),
            Window(content=FormattedTextControl(text="Hello world")),
        ])
        layout = Layout(root_container)
        key_bindings = KeyBindings()

        # Exit user interface with Ctrl-Q
        @key_bindings.add("c-q")
        def exit_interface(event):
            event.app.exit()

        # Render a new card
        @key_bindings.add("space")
        def new_card(event):
            deck = Deck()
            deck.get_card().render()

        app = Application(layout=layout, key_bindings=key_bindings, full_screen=True)
        app.run()

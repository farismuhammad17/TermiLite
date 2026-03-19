from . import globals
from . import color

from .core.terminal      import init, restore
from .core.input_handler import update_input, get_kbd_buffer_left
from .core.mouse         import parse_mouse, handle_mouse
from .core.engine        import run

from .ui.page      import Page
from .ui.window    import Window
from .ui.panel     import Panel
from .ui.label     import Label
from .ui.inputbox  import InputBox
from .ui.button    import Button
from .ui.separator import Separator

size = globals.screen_width, globals.screen_height

__author__      = "Faris Muhammad"
__version__     = "0.1.2"
__license__     = "MIT"
__description__ = "A very lightweight TUI engine"

__all__ = [
    "run",
    "Page",
    "Window",
    "Label",
    "InputBox",
    "Button"
]

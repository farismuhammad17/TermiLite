from . import globals

from .core.terminal      import init, restore
from .core.input_handler import update_input, get_kbd_buffer_left
from .core.mouse         import parse_mouse, handle_mouse
from .core.engine        import run

from .ui.window import Window
from .ui.label  import Label
from .ui.input  import InputBox
from .ui.button import Button

__author__      = "Faris Muhammad"
__version__     = "0.1.0"
__license__     = "MIT"
__description__ = "A very lightweight TUI engine"

__all__ = [
    "run",
    "Window",
    "Label",
    "InputBox",
    "Button"
]

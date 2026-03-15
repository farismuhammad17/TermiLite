"""
Color variables are stored here for cleaner code.

RESET

Foreground (prefix: FG_):
    BLACK
    RED
    GREEN
    YELLOW
    BLUE
    MAGENTA
    CYAN
    WHITE

Background (prefix: BG_):
    BLACK
    RED
    BLUE
    WHITE
"""

RESET = "\x1b[0m"

FG_BLACK = "\x1b[30m"
FG_RED = "\x1b[31m"
FG_GREEN = "\x1b[32m"
FG_YELLOW = "\x1b[33m"
FG_BLUE = "\x1b[34m"
FG_MAGENTA = "\x1b[35m"
FG_CYAN = "\x1b[36m"
FG_WHITE = "\x1b[37m"

BG_BLACK = "\x1b[40m"
BG_RED = "\x1b[41m"
BG_BLUE = "\x1b[44m"
BG_WHITE = "\x1b[47m"

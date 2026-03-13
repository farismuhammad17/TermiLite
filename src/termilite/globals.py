"""
Stores variables for every program file here to use.
"""

from collections import deque

COLOR_RESET = "\x1b[0m"
COLOR_FG_BLACK = "\x1b[30m"
COLOR_FG_RED = "\x1b[31m"
COLOR_FG_GREEN = "\x1b[32m"
COLOR_FG_YELLOW = "\x1b[33m"
COLOR_FG_BLUE = "\x1b[34m"
COLOR_FG_MAGENTA = "\x1b[35m"
COLOR_FG_CYAN = "\x1b[36m"
COLOR_FG_WHITE = "\x1b[37m"
COLOR_BG_BLACK = "\x1b[40m"
COLOR_BG_RED = "\x1b[41m"
COLOR_BG_BLUE = "\x1b[44m"
COLOR_BG_WHITE = "\x1b[47m"

CORNER_TOP_LEFT     = "┌" # Unicode U+250C
CORNER_TOP_RIGHT    = "┐" # Unicode U+2510
CORNER_BOTTOM_LEFT  = "└" # Unicode U+2514
CORNER_BOTTOM_RIGHT = "┘" # Unicode U+2518
HLINE               = "─" # Unicode U+2500
VLINE               = "│" # Unicode U+2502

screen = []
color_buffer = []

screen_width  = 0 # Terminal width
screen_height = 0 # Terminal height

original_termios = None

windows = []      # List of all Window objects
total_windows = 0 # Total number of windows, is len(windows), but this feels nicer to use

active_window = None # Currently focussed window
is_running    = True # If the program is running

focussed_obj = None # Current focussed on object

is_dragging = False
drag_target = None
drag_offset_x = 0
drag_offset_y = 0

kbd_buffer = deque() # Keyboard buffer

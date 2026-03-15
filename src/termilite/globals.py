"""
Stores variables for every program file here to use.
"""

import shutil

from collections import deque

CORNER_TOP_LEFT     = "+" # Unicode U+002B
CORNER_TOP_RIGHT    = "┐" # Unicode U+2510
CORNER_BOTTOM_LEFT  = "└" # Unicode U+2514
CORNER_BOTTOM_RIGHT = "┘" # Unicode U+2518
HLINE               = "─" # Unicode U+2500
VLINE               = "│" # Unicode U+2502
DOUBLE_HLINE        = "=" # Unicode U+003D
DOUBLE_VLINE        = "‖" # Unicode U+2016

MIN_WINDOW_Z = 0          # Windows can have Z-index values from 0 to 9,999
MIN_PANEL_Z  = 10_000     # Panels get 9,999 to inf. This also acts as a maximum window limit.

MAX_WINDOW_Z = MIN_PANEL_Z

screen = []
color_buffer = []

size = shutil.get_terminal_size()

screen_width  = size.columns # Terminal width
screen_height = size.lines # Terminal height

original_termios = None

windows = []      # List of all Window objects
total_windows = 0 # Total number of windows, is len(windows), but this feels nicer to use
current_page = None

page_changed = False

active_window = None # Currently focussed window
is_running    = True # If the program is running

focussed_obj = None # Current focussed on object

is_dragging = False
drag_target = None
drag_offset_x = 0
drag_offset_y = 0

resize_target = None
resize_offset = 0

kbd_buffer = deque() # Keyboard buffer

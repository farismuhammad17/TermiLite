import termilite

import sys
import os
import shutil
import atexit

if os.name == 'nt':
    import msvcrt
    import ctypes
    from ctypes import wintypes
else:
    import termios
    import tty

def init():
    size = shutil.get_terminal_size()
    termilite.globals.screen_width = size.columns
    termilite.globals.screen_height = size.lines

    if os.name == 'nt':
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)
        mode = wintypes.DWORD()
        kernel32.GetConsoleMode(handle, ctypes.byref(mode))
        kernel32.SetConsoleMode(handle, mode.value | 0x0004)
    else:
        fd = sys.stdin.fileno()
        termilite.original_termios = termios.tcgetattr(fd)
        new_settings    = termios.tcgetattr(fd)
        new_settings[3] = new_settings[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSADRAIN, new_settings)

    # \x1b[?1049h -> Switch to Alternate Screen Buffer
    # \x1b[?25l   -> Hide Cursor
    # \x1b[?1000h -> Enable mouse click tracking
    # \x1b[?1006h -> Enable SGR extended mode (handles large screens)
    # \x1b[?1002h -> Cell motion tracking
    sys.stdout.write("\x1b[?1049h\x1b[?25l\x1b[?1000h\x1b[?1006h\x1b[?1002h")
    sys.stdout.flush()

    atexit.register(restore)

def restore():
    if termilite.original_termios:
        fd = sys.stdin.fileno()
        termios.tcsetattr(fd, termios.TCSADRAIN, termilite.original_termios)

        # Undoes init
        sys.stdout.write("\x1b[?1002l\x1b[?1000l\x1b[?1006l\x1b[?1049l\x1b[?25h")
        sys.stdout.flush()

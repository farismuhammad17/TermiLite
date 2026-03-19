import termilite

import os
import sys

if os.name == 'nt':
    import msvcrt
else:
    import select

def _update_input_windows(): # For Windows systems
    if not msvcrt.kbhit():
        return

    char = msvcrt.getch().decode('utf-8', errors='ignore')

    if char == '\x1b':
        seq = char
        while msvcrt.kbhit():
            seq += msvcrt.getch().decode('utf-8', errors='ignore')
            if seq[-1].isalpha() or seq[-1] == '~':
                break
        _process_sequence(seq)
    else:
        key = '\n' if char == '\r' else char
        _process_sequence(key)

def _update_input_unix(): # For Linux/Mac systems
    dr, _, _ = select.select([sys.stdin], [], [], 0)
    if not dr:
        return

    char = sys.stdin.read(1)
    if char == '\x1b':
        seq = char
        while True:
            c = sys.stdin.read(1)
            seq += c
            if c.isalpha() or c == '~':
                break
        _process_sequence(seq)
    else:
        _process_sequence(char)

def _process_sequence(seq):
    if seq.startswith("\x1b[<"): # Mouse codes
        termilite.handle_mouse(seq)
        return

    if seq in termilite.kbd_actions:
        termilite.kbd_actions[seq]()

    termilite.globals.kbd_buffer.append(seq)

def update_input():
    if os.name == 'nt':
        _update_input_windows()
    else:
        _update_input_unix()

def get_kbd_buffer_left():
    if termilite.globals.kbd_buffer:
        return termilite.globals.kbd_buffer.popleft()

    return None

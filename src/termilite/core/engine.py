import termilite

import sys
import time
import traceback

def set_cell(x, y, char, color = termilite.globals.COLOR_RESET):
    if 0 <= x < termilite.globals.screen_width and 0 <= y < termilite.globals.screen_height:
        termilite.globals.screen[y][x] = char
        termilite.globals.color_buffer[y][x] = color

def render():
    sorted_windows = sorted(termilite.globals.windows, key=lambda w: w.z)

    for win in sorted_windows: # Going up the sorted list ensures that higher ones overwrite the lower windows
        for comp in win.components:
            comp.update()

        for x_ in range(win.x, win.x + win.width): # To overlap, just clear off everything below us
            for y_ in range(win.y, win.y + win.height):
                set_cell(x_, y_, ' ')
        for i in range(win.x, win.x + win.width): # Borders
            set_cell(i, win.y - 1, termilite.globals.HLINE if not win == termilite.globals.active_window else '=') # Top
            set_cell(i, win.y + win.height, termilite.globals.HLINE if not win == termilite.globals.active_window else '=') # Bottom
        for i in range(win.y, win.y + win.height):
            set_cell(win.x - 1, i, termilite.globals.VLINE) # Left
            set_cell(win.x + win.width, i, termilite.globals.VLINE) # Right

        set_cell(win.x - 1, win.y - 1, termilite.globals.CORNER_TOP_LEFT)
        set_cell(win.x + win.width, win.y - 1, termilite.globals.CORNER_TOP_RIGHT)
        set_cell(win.x - 1, win.y + win.height, termilite.globals.CORNER_BOTTOM_LEFT)
        set_cell(win.x + win.width, win.y + win.height, termilite.globals.CORNER_BOTTOM_RIGHT)

        win.render()

    output = ["\x1b[H"] # Start with Move Cursor to 0,0

    for y in range(termilite.globals.screen_height):
        current_row_color = termilite.globals.COLOR_RESET
        row_str = ""

        for x in range(termilite.globals.screen_width):
            char  = termilite.globals.screen[y][x]
            color = termilite.globals.color_buffer[y][x]

            # If the color changes, inject the ANSI code into the string
            if color != current_row_color:
                row_str += color
                current_row_color = color

            row_str += char

        line_end = "\n" if y < termilite.globals.screen_height - 1 else ""
        output.append(row_str + termilite.globals.COLOR_RESET + line_end)

    # Make sure buffer won't suddently load in next time we focus on something
    # termilite.globals.kbd_buffer.clear()

    # Move cursor to 0,0 and write the whole frame at once
    sys.stdout.write("".join(output))
    sys.stdout.flush()

def run(fps=30):
    termilite.init()
    termilite.globals.is_running = True

    termilite.globals.screen = [[' ' for _ in range(termilite.globals.screen_width)] for _ in range(termilite.globals.screen_height)]
    termilite.globals.color_buffer = [[termilite.globals.COLOR_RESET for _ in range(termilite.globals.screen_width)] for _ in range(termilite.globals.screen_height)]

    # Focus on highest Z-valued window
    if termilite.globals.windows:
        sorted(termilite.globals.windows, key=lambda w: w.z, reverse=True)[0].focus()

    error_msg = None

    try:
        while termilite.globals.is_running:
            start_time = time.time()

            termilite.update_input()
            render()

            # Cap the frame rate
            time.sleep(max(0, (1/fps) - (time.time() - start_time)))

    except Exception:
        termilite.globals.is_running = False
        error_msg = traceback.format_exc()
    finally:
        termilite.restore()

        if error_msg:
            print("\x1b[31m[TermiLite Crash]\x1b[0m")
            print(error_msg)

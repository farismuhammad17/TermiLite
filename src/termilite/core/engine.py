import termilite

import sys
import time
import traceback

def set_cell(x, y, char, color = termilite.color.RESET):
    if 0 <= x < termilite.globals.screen_width and 0 <= y < termilite.globals.screen_height:
        termilite.globals.screen[y][x] = char
        termilite.globals.color_buffer[y][x] = color

def render():
    if termilite.globals.page_changed:
        termilite.globals.screen = [row[:] for row in termilite.globals.current_page.screen_buffer]
        termilite.globals.color_buffer = [row[:] for row in termilite.globals.current_page.color_buffer]
        termilite.globals.page_changed = False

    sorted_windows = sorted(termilite.globals.windows, key=lambda w: w.z)

    for win in sorted_windows: # Going up the sorted list ensures that higher ones overwrite the lower windows
        win.update()

        for x_ in range(win.x - win.margin_left, win.x + win.width + win.margin_right): # To overlap, just clear off everything below us
            for y_ in range(win.y - win.margin_top, win.y + win.height + win.margin_bottom):
                set_cell(x_, y_, ' ', win.color)

        border_up_char = win.border_top
        border_bottom_char = win.border_bottom
        border_left_char = win.border_left
        border_right_char = win.border_right

        if win == termilite.globals.active_window:
            border_up_char = win.focussed_top
            border_bottom_char = win.focussed_bottom
            border_left_char = win.focussed_left
            border_right_char = win.focussed_right

        name       = win.name[:win.width - 2]
        name_len   = len(name)
        name_start = (win.width - name_len) // 2

        for i in range(win.x, win.x + win.width): # Top and Bottom
            local_idx = i - win.x

            if name_len < win.width and name_start <= local_idx < name_start + name_len:
                set_cell(i, win.y - 1, name[local_idx - name_start])
            else:
                set_cell(i, win.y - 1, border_up_char)

            set_cell(i, win.y + win.height, border_bottom_char)
        for i in range(win.y, win.y + win.height): # Left and Right
            set_cell(win.x - 1, i, border_left_char)
            set_cell(win.x + win.width, i, border_right_char)

        set_cell(win.x - 1, win.y - 1, win.top_left_corner)
        set_cell(win.x + win.width, win.y - 1, win.top_right_corner)
        set_cell(win.x - 1, win.y + win.height, win.bottom_left_corner)
        set_cell(win.x + win.width, win.y + win.height, win.bottom_right_corner)

        win.render()

    output = ["\x1b[H"] # Start with Move Cursor to 0,0

    for y in range(termilite.globals.screen_height):
        current_row_color = termilite.color.RESET
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
        output.append(row_str + termilite.color.RESET + line_end)

    # Make sure buffer won't suddently load in next time we focus on something
    termilite.globals.kbd_buffer.clear()

    # Move cursor to 0,0 and write the whole frame at once
    sys.stdout.write("".join(output))
    sys.stdout.flush()

def run(fps=60):
    termilite.init()
    termilite.globals.is_running = True

    termilite.globals.screen = [[' ' for _ in range(termilite.globals.screen_width)] for _ in range(termilite.globals.screen_height)]
    termilite.globals.color_buffer = [[termilite.color.RESET for _ in range(termilite.globals.screen_width)] for _ in range(termilite.globals.screen_height)]

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
            print("\x1b[31m[Runtime Error]\x1b[0m")
            print(error_msg)

import termilite

def parse_mouse(sequence: str):
    try:
        parts = sequence[3:-1].split(';')

        # We subtract 1 because terminal coordinates are 1-indexed
        x = int(parts[1]) - 1
        y = int(parts[2]) - 1

        return (x, y)
    except (IndexError, ValueError):
        # If the sequence is malformed, return None
        return None

def handle_mouse(sequence: str):
    data = parse_mouse(sequence)
    if not data: return
    mx, my = data

    # State 'M' = Pressed/Moving, 'm' = Released
    if sequence.endswith('m'):
        termilite.globals.drag_target = None
        return

    if termilite.globals.drag_target:
        win = termilite.globals.drag_target

        for y_ in range(win.y - 1, win.y + win.height + 1):
            for x_ in range(win.x - 1, win.x + win.width + 1):
                if 0 <= y_ < termilite.globals.screen_height and 0 <= x_ < termilite.globals.screen_width:
                    termilite.globals.screen[y_][x_] = ' '
                    termilite.globals.color_buffer[y_][x_] = termilite.globals.COLOR_RESET

        win.x = mx - termilite.globals.drag_offset_x
        win.y = my - termilite.globals.drag_offset_y

        return

    for win in sorted(termilite.globals.windows, key=lambda w: w.z, reverse=True):
        if (win.x <= mx < win.x + win.width and
            win.y <= my < win.y + win.height):

            win.focus()
            was_widget_hit = win.handle_click(mx, my)

            if win.draggable and my == win.y and not was_widget_hit:
                termilite.globals.drag_target = win
                termilite.globals.drag_offset_x = mx - win.x
                termilite.globals.drag_offset_y = my - win.y
            break

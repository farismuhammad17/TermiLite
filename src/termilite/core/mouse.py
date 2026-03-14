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
        termilite.globals.resize_target = None

        return

    if termilite.globals.resize_target:
        win = termilite.globals.resize_target

        for r_y in range(win.y - 1, win.y + win.height + 1):
            for r_x in range(win.x - 1, win.x + win.width + 1):
                if 0 <= r_y < termilite.globals.screen_height and 0 <= r_x < termilite.globals.screen_width:
                    termilite.globals.screen[r_y][r_x] = ' '
                    termilite.globals.color_buffer[r_y][r_x] = termilite.globals.COLOR_RESET

        match termilite.globals.resize_mode:
            case 'T':
                new_y = my - termilite.globals.resize_offset
                diff = win.y - new_y
                if win.height + diff > 3:
                    win.y = new_y
                    win.height += diff

            case 'B':
                win.height = max(3, my - win.y - termilite.globals.resize_offset)

            case 'L':
                new_x = mx - termilite.globals.resize_offset
                diff = win.x - new_x
                if win.width + diff > 3:
                    win.x = new_x
                    win.width += diff

            case 'R':
                win.width = max(3, mx - win.x - termilite.globals.resize_offset)
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
        if (win.x <= mx + 1 <= win.x + win.width and
            win.y <= my + 1 <= win.y + win.height):

            win.focus()

            if win.handle_click(mx, my): break

            if win.draggable and mx == win.x - 1 and my == win.y - 1:
                termilite.globals.drag_target = win
                termilite.globals.drag_offset_x = mx - win.x
                termilite.globals.drag_offset_y = my - win.y

            elif win.resizable_top and my == win.y - 1 and win.x <= mx <= win.x + win.width:
                termilite.globals.resize_mode = 'T'
                termilite.globals.resize_target = win
                termilite.globals.resize_offset = my - win.y

            elif win.resizable_bottom and my == win.y + win.height - 1 and win.x <= mx <= win.x + win.width:
                termilite.globals.resize_mode = 'B'
                termilite.globals.resize_target = win
                termilite.globals.resize_offset = my - win.y - win.height

            elif win.resizable_left and mx == win.x - 1 and win.y <= my <= win.y + win.height:
                termilite.globals.resize_mode = 'L'
                termilite.globals.resize_target = win
                termilite.globals.resize_offset = mx - win.x

            elif win.resizable_right and mx == win.x + win.width - 1 and win.y < my <= win.y + win.height:
                termilite.globals.resize_mode = 'R'
                termilite.globals.resize_target = win
                termilite.globals.resize_offset = mx - win.x - win.width

            break

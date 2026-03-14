import termilite

class Window:
    def __init__(self, x: int, y: int, z: int, width: int, height: int, name: str = ""):
        self.x = x
        self.y = y
        self.z = z
        self.width  = width
        self.height = height
        self.name = name

        self.components = []

        self.draggable = True

        self.resizable_top    = True
        self.resizable_bottom = True
        self.resizable_left   = True
        self.resizable_right  = True

        self.border_top      = termilite.globals.HLINE
        self.border_bottom   = termilite.globals.HLINE
        self.border_left     = termilite.globals.VLINE
        self.border_right    = termilite.globals.VLINE
        self.focussed_top    = '='
        self.focussed_bottom = '='

        self.top_left_corner     = termilite.globals.CORNER_TOP_LEFT
        self.top_right_corner    = termilite.globals.CORNER_TOP_RIGHT
        self.bottom_left_corner  = termilite.globals.CORNER_BOTTOM_LEFT
        self.bottom_right_corner = termilite.globals.CORNER_BOTTOM_RIGHT

        termilite.globals.windows.append(self)
        termilite.globals.total_windows += 1

    def set_cell(self, x: int, y: int, char: str, color: str = termilite.globals.COLOR_RESET):
        pos_x = x + self.x
        pos_y = y + self.y

        if 0 <= x < self.width and 0 <= y < self.height:
            termilite.globals.screen[pos_y][pos_x] = char
            termilite.globals.color_buffer[pos_y][pos_x] = color

    def render(self):
        for comp in self.components:
            comp.render()

    def focus(self):
        if termilite.globals.active_window == self:
            return

        max_z = 0
        if termilite.globals.windows:
            max_z = max(w.z for w in termilite.globals.windows)

        self.z = max_z + 1

        termilite.globals.active_window = self

    def handle_click(self, mx, my):
        local_x = mx - self.x
        local_y = my - self.y

        for comp in self.components:
            if (comp.x <= local_x < comp.x + comp.width and
                comp.y <= local_y < comp.y + comp.height):

                termilite.globals.focussed_obj = comp
                return True
        return False

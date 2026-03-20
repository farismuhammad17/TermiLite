import termilite

class TermiliteMaximumWindowsReached(Exception):
    def __init__(self):
        super().__init__(f"Maximum number of windows reached: {termilite.globals.MIN_PANEL_Z} (configure value at termilite.globals if required)")

class Window:
    """
    Window object that can hold contents.

    Attributes:
        x, y (int): Position of top-left point.
        z (int): Z-index of the window, higher windows appear above lower.
        width, height (int): Window width and height.
        name (str): Window title that appears above it.
        color (str): Background color (use termilite.color)
        margin_top, margin_bottom, margin_left, margin_right (int):
            Amount of extra space taken by window beyond the border

    Movement and sizing:
        draggable (bool): Whether the window can be dragged by the top-left corner or not.
        resizable_top, resizable_bottom, resizable_left, resizable_right (bool):
            Whether the window is resizable.

    Display:
        border_top, border_bottom, border_left, border_right (str)
            Character used to display border.
        focussed_top, focussed_bottom, focussed_left, focussed_right (str):
            Character used to display border if focussed.
        top_left_corner, top_right_corner, bottom_left_corner, bottom_right_corner (str):
            Character used to display window corner.

    Methods:
        set_cell: Writes char to (x, y), relative to the window.
        focus: Set UI focus to window by setting highest Z-index.
    """

    def __init__(self, x: int, y: int, z: int, width: int, height: int, name: str = "", color: str = termilite.color.BG_BLACK, margin_top: int = 0, margin_bottom: int = 0, margin_left: int = 0, margin_right: int = 0):
        self._x = x
        self._y = y
        self._z = z + termilite.globals.MIN_WINDOW_Z
        self._width  = width
        self._height = height
        self._name = name
        self._color = color

        self.margin_top = margin_top
        self.margin_bottom = margin_bottom
        self.margin_left = margin_left
        self.margin_right = margin_right

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
        self.focussed_top    = termilite.globals.DOUBLE_HLINE
        self.focussed_bottom = termilite.globals.DOUBLE_HLINE
        self.focussed_left   = termilite.globals.DOUBLE_VLINE
        self.focussed_right  = termilite.globals.DOUBLE_VLINE

        self.top_left_corner     = termilite.globals.CORNER_TOP_LEFT
        self.top_right_corner    = termilite.globals.CORNER_TOP_RIGHT
        self.bottom_left_corner  = termilite.globals.CORNER_BOTTOM_LEFT
        self.bottom_right_corner = termilite.globals.CORNER_BOTTOM_RIGHT

        self.focussable = True

        termilite.globals.windows.append(self)
        termilite.globals.total_windows += 1

        if termilite.globals.total_windows >= 10_000:
            raise TermiliteMaximumWindowsReached()

    @property
    def x(self):
        return self._x() if callable(self._x) else self._x
    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y() if callable(self._y) else self._y
    @y.setter
    def y(self, value):
        self._y = value

    @property
    def z(self):
        return self._z() if callable(self._z) else self._z
    @z.setter
    def z(self, value):
        self._z = value

    @property
    def width(self):
        return self._width() if callable(self._width) else self._width
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height() if callable(self._height) else self._height
    @height.setter
    def height(self, value):
        self._height = value

    @property
    def name(self):
        return self._name() if callable(self._name) else self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def color(self):
        return self._color() if callable(self._color) else self._color
    @color.setter
    def color(self, value):
        self._color = value

    def set_cell(self, x: int, y: int, char: str, color: str = termilite.color.RESET):
        """
        Writes char to (x, y), relative to the window. Color can be set as well (Refer termilite.color)

        Attributes:
            x: int, y: int,
            char: str,
            color: str
        """

        pos_x = x + self.x
        pos_y = y + self.y

        if (0 <= pos_x < termilite.globals.screen_width and
            0 <= pos_y < termilite.globals.screen_height and
            0 <= x < self.width and 0 <= y < self.height
        ):
            termilite.globals.screen[pos_y][pos_x] = char
            termilite.globals.color_buffer[pos_y][pos_x] = color

    def render(self):
        """
        NOTE: Function is called by engine, not required to call.

        Renders the contents of the window.
        """

        for comp in self.components:
            comp.render()

    def update(self):
        """
        NOTE: Function is called by engine, not required to call.

        Updates all the contents of the window.
        """

        for comp in self.components:
            comp.update()

    def focus(self):
        """
        Set UI focus to window by setting highest Z-index
        """

        if termilite.globals.active_window == self or not self.focussable:
            return

        max_z = 0
        if termilite.globals.windows:
            max_z = max(w.z for w in termilite.globals.windows)

        self.z = (max_z + 1) % termilite.globals.MAX_WINDOW_Z

        termilite.globals.active_window = self

    def handle_click(self, mx, my):
        """
        NOTE: Function is called by engine, not required to call.

        Handles mouse clicks
        """

        local_x = mx - self.x
        local_y = my - self.y

        for comp in self.components:
            if (comp.x <= local_x < comp.x + comp.width and
                comp.y <= local_y < comp.y + comp.height):

                termilite.globals.focussed_obj = comp
                return True
        return False

    @staticmethod
    def create_desktop():
        """
        Creates a window that takes up the entire screen
        size, with the border styling going out of the
        screen.
        """

        win = Window(
            x=0, y=0, z=0,
            width=termilite.globals.screen_width,
            height=termilite.globals.screen_height
        )

        win.draggable = False

        win.resizable_top    = False
        win.resizable_bottom = False
        win.resizable_left   = False
        win.resizable_right  = False

        return win

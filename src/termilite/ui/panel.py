import termilite

class PanelInvalidSideException(Exception):
    def __init__(self, side: str):
        super().__init__(f"Invalid side provided to Panel: {side} (not 't', 'b', 'l', 'r')")
        self.invalid_side = side

class Panel(termilite.Window):
    """
    Creates a sidebar sort of window

    Attributes:
        side (str): t(op), b(ottom), l(eft), r(ight)
        size (int): Size from side
        z (int): Z-index of panel to other panels
        resizable (bool): If size can be adjusted
        name (str): Name to appear above

    Movement and sizing:
        [Same as Window]

        draggable (bool): Whether the window can be dragged by the top-left corner or not.
        resizable_top, resizable_bottom, resizable_left, resizable_right (bool):
            Whether the window is resizable.

    Display:
        [Same as Window]

        border_top, border_bottom, border_left, border_right (str)
            Character used to display border.
        focussed_top, focussed_bottom, focussed_left, focussed_right (str):
            Character used to display border if focussed.
        top_left_corner, top_right_corner, bottom_left_corner, bottom_right_corner (str):
            Character used to display window corner.

    Methods:
        update_panel: Only to be called if self.side was changed during runtime.

        [Same as Window]

        set_cell: Writes char to (x, y), relative to the window.
        focus: Set UI focus to window by setting highest Z-index.
    """

    def __init__(self, side: str, size: int, z: int, resizable: bool = True, name: str = ""):
        if side not in ('t', 'b', 'l', 'r'):
            raise PanelInvalidSideException(side)

        self.side = side
        self.size = size
        self.z = z + termilite.globals.MIN_PANEL_Z
        self.resizable = resizable
        self.name = name

        # Everything is set to negative, and is enabled later.

        self.draggable = False

        self.resizable_top    = False
        self.resizable_bottom = False
        self.resizable_left   = False
        self.resizable_right  = False

        self.border_top      = ''
        self.border_bottom   = ''
        self.border_left     = ''
        self.border_right    = ''
        self.focussed_top    = ''
        self.focussed_bottom = ''
        self.focussed_left   = ''
        self.focussed_right  = ''

        self.top_left_corner     = ''
        self.top_right_corner    = ''
        self.bottom_left_corner  = ''
        self.bottom_right_corner = ''

        self.update_panel()

        super().__init__(
            self.x, self.y, self.z,
            self.width, self.height,
            self.name
        )

    def focus(self):
        termilite.globals.active_window = self

    def update_panel(self):
        """
        NOTE: Only to be called if self.side was changed during runtime.

        Update the bounds, resizable side, and border of the Panel.
        """

        match self.side:
            case 't':
                self.x = 0
                self.y = 0
                self.width = termilite.globals.screen_width
                self.height = self.size

                self.resizable_bottom = self.resizable

                self.border_bottom   = termilite.globals.HLINE
                self.focussed_bottom = termilite.globals.DOUBLE_HLINE

            case 'b':
                self.x = 0
                self.y = termilite.globals.screen_height - self.size
                self.width = termilite.globals.screen_width
                self.height = self.size

                self.resizable_top = self.resizable

                self.focussed_right  = termilite.globals.DOUBLE_VLINE
                self.focussed_top    = termilite.globals.DOUBLE_HLINE

            case 'l':
                self.x = 0
                self.y = 0
                self.width = self.size
                self.height = termilite.globals.screen_height

                self.resizable_right = self.resizable

                self.border_right    = termilite.globals.VLINE
                self.focussed_right  = termilite.globals.DOUBLE_VLINE

            case 'r':
                self.x = termilite.globals.screen_width - self.size
                self.y = 0
                self.width = self.size
                self.height = termilite.globals.screen_height

                self.resizable_left = self.resizable

                self.border_left     = termilite.globals.VLINE
                self.focussed_left   = termilite.globals.DOUBLE_VLINE

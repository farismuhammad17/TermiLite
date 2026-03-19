import termilite

class Button:
    """
    Simple button.

    Attributes:
        window (Window): Parent window
        x, y (int): Relative position
        text (str): Content
        width, height (int): Dimensions
        onclick: Function to execute upon clicking.
    """

    def __init__(self, window: termilite.Window, x: int, y: int, text: str, width: int = None, height: int = None, color: str = termilite.color.RESET, onclick = lambda: None):
        self.window = window
        self._x = x
        self._y = y
        self._color = color

        self.onclick = onclick

        self.label = termilite.Label(window, x, y, text)
        window.components.remove(self.label)

        self._width = width or len(text)
        if height:
            self._height = height
        else:
            explicit_lines = text.count('\n') + 1
            wrap_lines = -(-len(text) // self.width)
            self._height = max(explicit_lines, wrap_lines)

        self.label.width = self._width
        self.label.height = self._height

        window.components.append(self)

    @property
    def x(self):
        return self._x() if callable(self._x) else self._x
    @x.setter
    def x(self, value):
        self._x = value
        self.label.x = value

    @property
    def y(self):
        return self._y() if callable(self._y) else self._y
    @y.setter
    def y(self, value):
        self._y = value
        self.label.y = value

    @property
    def text(self):
        return self.label.text() if callable(self.label.text) else self.label.text
    @text.setter
    def text(self, value):
        self.label.text = value

    @property
    def width(self):
        return self._width() if callable(self._width) else self._width
    @width.setter
    def width(self, value):
        self._width = value
        self.label.width = value

    @property
    def height(self):
        return self._height() if callable(self._height) else self._height
    @height.setter
    def height(self, value):
        self._height = value
        self.label.height = value

    @property
    def color(self):
        return self._color() if callable(self._color) else self._color
    @color.setter
    def color(self, value):
        self._color = value
        self.label.color = value

    def update(self):
        """
        NOTE: Function is called by engine, not required to call.

        Checks if the button is clicked
        """

        if termilite.globals.focussed_obj == self:
            self.onclick()
            termilite.globals.focussed_obj = None

    def render(self):
        """
        NOTE: Function is called by engine, not required to call.

        Renders the contents of the button.
        """

        for i in range(self.x, self.x + self.width):
            for j in range(self.y, self.y + self.height):
                self.window.set_cell(i, j, ' ', self.color)

        self.label.render()

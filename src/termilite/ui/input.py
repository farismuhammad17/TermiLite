import termilite

class InputBox:
    """
    Text entry widget

    Attributes:
        window (Window): Parent window
        x, y (int): Relative position
        width, height (int): Dimensions
        maxlen (int): Maximum input length

    Display:
        value (str): Text inputted
        underline (str): Default underline for empty region
        cursor (str): Default cursor for current mouse position
    """

    def __init__(self, window: termilite.Window, x: int, y: int, width: int = None, height: int = None, maxlen: int = 10):
        self.window = window
        self._x = x
        self._y = y

        self.label = termilite.Label(window, x, y, "")
        window.components.remove(self.label)

        self._width  = width or window.width
        self._height = height or window.height
        self._maxlen = maxlen

        self._underline = '_' # Can be set to empty strings if unpreferred
        self._cursor    = '|'

        window.components.append(self)

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
    def value(self):
        return self.label.text() if callable(self.label.text) else self.label.text
    @value.setter
    def value(self, value):
        self.label.text = value

    @property
    def color(self):
        return self.label.color() if callable(self.label.color) else self.label.color
    @color.setter
    def color(self, value):
        self.label.color = value

    @property
    def underline(self):
        return self._underline() if callable(self._underline) else self._underline
    @underline.setter
    def underline(self, value):
        self._underline = value

    @property
    def cursor(self):
        return self._cursor() if callable(self._cursor) else self._cursor
    @cursor.setter
    def cursor(self, value):
        self._cursor = value

    @property
    def maxlen(self):
        return self._maxlen() if callable(self._maxlen) else self._maxlen
    @maxlen.setter
    def maxlen(self, value):
        self._maxlen = value

    def update(self):
        """
        NOTE: Function is called by engine, not required to call.

        Checks whether keyboard buffer has values for input
        """

        if self != termilite.globals.focussed_obj or not termilite.globals.kbd_buffer or len(self.value) == self.maxlen:
            return

        char = termilite.get_kbd_buffer_left()

        if char in ("\x7f", "\x08"): # Backspace
            self.value = self.value[:-1]
        elif len(char) == 1 and char.isprintable():
            self.value += char

    def render(self):
        """
        NOTE: Function is called by engine, not required to call.

        Renders the contents of the input box.
        """

        self.label.render()

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
        cursor_x (int): X position of cursor
        cursor_y (int): Y position of cursor
        cursor_char (str): Character used to display cursor
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

        self._cursor_x = 0
        self._cursor_y = 0
        self._cursor_char = '|'

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
    def maxlen(self):
        return self._maxlen() if callable(self._maxlen) else self._maxlen
    @maxlen.setter
    def maxlen(self, value):
        self._maxlen = value

    @property
    def cursor_x(self):
        return self._cursor_x() if callable(self._cursor_x) else self._cursor_x
    @cursor_x.setter
    def cursor_x(self, value):
        self._cursor_x = value

    @property
    def cursor_y(self):
        return self._cursor_y() if callable(self._cursor_y) else self._cursor_y
    @cursor_y.setter
    def cursor_y(self, value):
        self._cursor_y = value

    @property
    def cursor_char(self):
        return self._cursor_char() if callable(self._cursor_char) else self._cursor_char
    @cursor_char.setter
    def cursor_char(self, value):
        self._cursor_char = value

    def update(self):
        """
        NOTE: Function is called by engine, not required to call.

        Checks whether keyboard buffer has values for input
        """

        if self != termilite.globals.focussed_obj or not termilite.globals.kbd_buffer or len(self.value) == self.maxlen:
            return

        char = termilite.get_kbd_buffer_left()

        if char in ('\x7f', '\x08'): # Backspace
            self.value = self.value[:-1]

        elif (len(char) == 1 and char.isprintable()) or char == '\n':
            lines = self.value.split('\n')
            current_line_count = len(lines)

            is_manual_wrap = char == '\n'
            is_auto_wrap   = len(lines[-1]) >= self.width

            if current_line_count + (1 if (is_manual_wrap or is_auto_wrap) else 0) <= self.height:
                if len(self.value) < self.maxlen:
                    self.value += char

    def render(self):
        """
        NOTE: Function is called by engine, not required to call.

        Renders the contents of the input box.
        """

        self.label.render()

        if termilite.globals.focussed_obj != self:
            return

        curr_x, curr_y = 0, 0
        for char in self.value:
            if char == '\n':
                curr_x = 0
                curr_y += 1
            else:
                curr_x += 1
                if curr_x >= self.width:
                    curr_x = 0
                    curr_y += 1

        if curr_y < self.height:
            self.cursor_x = curr_x
            self.cursor_y = curr_y

            self.window.set_cell(self.x + curr_x, self.y + curr_y, self.cursor_char, self.color)

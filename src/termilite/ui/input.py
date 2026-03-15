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
        self.x = x
        self.y = y

        self.width  = width or window.width
        self.height = height or window.height
        self.maxlen = maxlen

        self.value = ""

        self.underline = '_' # Can be set to empty strings if unpreferred
        self.cursor    = '|'

        window.components.append(self)

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

        if self == termilite.globals.focussed_obj:
            text = self.value + self.cursor + self.underline * (self.maxlen - len(self.value) - len(self.cursor))
        else:
            text = self.value + self.underline * (self.maxlen - len(self.value))

        x = self.x
        y = self.y
        for char in text:
            self.window.set_cell(x, y, char)
            x += 1
            if x > self.x + self.width - 2:
                x = self.x
                y += 1

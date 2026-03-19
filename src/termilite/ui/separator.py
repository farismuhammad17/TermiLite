import termilite

class Separator:
    def __init__(self, window: termilite.Window, position: int, horizontal: bool = True, color: str = termilite.color.RESET, char: str = None):
        self.window = window
        self._position = position
        self._horizontal = horizontal
        self._color = color

        self.x, self.y, self.width, self.height = 0, 0, 0, 0 # Clicking would crash it, because these variables are expected, but these don't matter here

        self._char = char or (termilite.globals.HLINE if horizontal else termilite.globals.VLINE)

        if horizontal:
            self.render = self.render_horizontal
        else:
            self.render = self.render_vertical

        window.components.append(self)

    @property
    def position(self):
        return self._position() if callable(self._position) else self._position
    @position.setter
    def position(self, value):
        self._position = value

    @property
    def horizontal(self):
        return self._horizontal() if callable(self._horizontal) else self._horizontal
    @horizontal.setter
    def horizontal(self, value):
        self._horizontal = value

    @property
    def color(self):
        return self._color() if callable(self._color) else self._color
    @color.setter
    def color(self, value):
        self._color = value

    @property
    def char(self):
        return self._char() if callable(self._char) else self._char
    @char.setter
    def char(self, value):
        self._char = value

    def update(self): pass

    def render_vertical(self):
        for y in range(self.window.height):
            self.window.set_cell(self.position, y, self.char, self.color)

    def render_horizontal(self):
        for x in range(self.window.width):
            self.window.set_cell(x, self.position, self.char, self.color)

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

    def __init__(self, window: termilite.Window, x: int, y: int, text: str, width: int = None, height: int = None, onclick = lambda: None):
        self.window = window
        self.x = x
        self.y = y
        self.text = text
        self.onclick = onclick

        self.width  = width or (window.width - x)
        if height:
            self.height = height
        else:
            explicit_lines = text.count('\n') + 1
            wrap_lines = -(-len(text) // self.width)
            self.height = max(explicit_lines, wrap_lines)

        window.components.append(self)

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

        x = self.x
        y = self.y

        for char in self.text:
            self.window.set_cell(x, y, char)
            x += 1
            if x > self.x + self.width - 2:
                x = self.x
                y += 1

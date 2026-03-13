import termilite

class Button:
    def __init__(self, window: termilite.Window, x: int, y: int, text: str, width: int, height: int, onclick = lambda: None):
        self.window = window
        self.x = x
        self.y = y
        self.text = text
        self.onclick = onclick

        self.width = width or window.width
        self.height = height or window.height

        window.components.append(self)

    def update(self):
        if termilite.globals.focussed_obj == self:
            self.onclick()
            termilite.globals.focussed_obj = None

    def render(self):
        x = self.x
        y = self.y

        for char in self.text:
            self.window.set_cell(x, y, char)
            x += 1
            if x > self.x + self.width - 2:
                x = self.x
                y += 1

import termilite

class Label:
    def __init__(self, window: termilite.Window, x: int, y: int, text: str, width: int = None, height: int = None):
        self.window = window
        self.x = x
        self.y = y
        self.text = text

        self.width = width or window.width
        self.height = height or window.height

        window.components.append(self)

    def update(self): pass

    def render(self):
        x = self.x
        y = self.y
        color = termilite.globals.COLOR_RESET

        special = False
        special_buffer = ""

        for char in self.text:
            if char == '\x1b':
                special = True
                continue

            if special:
                if char == '[': continue
                elif char == 'm':
                    special = False

                    match int(special_buffer):
                        case 0:  color = termilite.globals.COLOR_RESET
                        case 30: color = termilite.globals.COLOR_FG_BLACK
                        case 31: color = termilite.globals.COLOR_FG_RED
                        case 32: color = termilite.globals.COLOR_FG_GREEN
                        case 33: color = termilite.globals.COLOR_FG_YELLOW
                        case 34: color = termilite.globals.COLOR_FG_BLUE
                        case 35: color = termilite.globals.COLOR_FG_MAGENTA
                        case 36: color = termilite.globals.COLOR_FG_CYAN
                        case 37: color = termilite.globals.COLOR_FG_WHITE
                        case 40: color = termilite.globals.COLOR_BG_BLACK
                        case 41: color = termilite.globals.COLOR_BG_RED
                        case 44: color = termilite.globals.COLOR_BG_BLUE
                        case 47: color = termilite.globals.COLOR_BG_WHITE

                    continue
                special_buffer += char

                continue

            self.window.set_cell(x, y, char, color)
            x += 1
            if x > self.x + self.width - 1:
                x = self.x
                y += 1

    def set_text(self, text: str):
        self.text = str(text)

    def append_text(self, text: str):
        self.text += str(text)

    def get_text(self):
        return self.text

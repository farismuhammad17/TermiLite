import termilite

class Label:
    """
    Text widget

    Attributes:
        window (Window): Parent window
        x, y (int): Relative position
        text (str): Content
        width, height (int): Dimensions
    """

    def __init__(self, window: termilite.Window, x: int, y: int, text: str, width: int = None, height: int = None, color: str = termilite.color.RESET):
        self.window = window
        self.x = x
        self.y = y
        self.text = text
        self.color = color

        self.width  = width or (window.width - x)
        if height:
            self.height = height
        else:
            explicit_lines = text.count('\n') + 1
            wrap_lines = -(-len(text) // self.width)
            self.height = max(explicit_lines, wrap_lines)

        window.components.append(self)

    def update(self): pass

    def render(self):
        x = self.x
        y = self.y
        color = self.color

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

                    try:
                        code = int(special_buffer) if special_buffer else 0

                        match code:
                            case 0:  color = termilite.color.RESET
                            case 30: color = termilite.color.FG_BLACK
                            case 31: color = termilite.color.FG_RED
                            case 32: color = termilite.color.FG_GREEN
                            case 33: color = termilite.color.FG_YELLOW
                            case 34: color = termilite.color.FG_BLUE
                            case 35: color = termilite.color.FG_MAGENTA
                            case 36: color = termilite.color.FG_CYAN
                            case 37: color = termilite.color.FG_WHITE
                            case 40: color = termilite.color.BG_BLACK
                            case 41: color = termilite.color.BG_RED
                            case 44: color = termilite.color.BG_BLUE
                            case 47: color = termilite.color.BG_WHITE

                        special_buffer = ""
                    except ValueError:
                        special_buffer = ""
                    continue
                special_buffer += char
                continue

            if char == '\n':
                x = self.x
                y += 1
                continue # Skip drawing the newline character itself

            # Draw the character
            self.window.set_cell(x, y, char, color)

            x += 1
            # Auto-wrap logic: only wrap if we exceed the window width
            if x >= self.width:
                x = self.x
                y += 1

    def set_text(self, text: str):
        """
        Text setter function
        """

        self.text = str(text)

    def append_text(self, text: str):
        """
        Append value to end of text
        """

        self.text += str(text)

    def get_text(self):
        """
        Text getter function
        """

        return self.text

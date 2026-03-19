import termilite

class Page:
    """
    Holds a list of windows, making it easier to have different pages,
    and to switch from one to another.

    Attributes:
        windows (list): List of all the windows in the page

    Methods:
        load: Load page into the screen
        add: Add a window to the page
        extend: Add a list of windows to the page
        remove: Remove window from page
    """

    def __init__(self, windows: list):
        self.windows = windows

        self.screen_buffer = None
        self.color_buffer  = None

    def load(self):
        """
        Set current page to this
        """

        if termilite.globals.current_page:
            termilite.globals.current_page.screen_buffer = [row[:] for row in termilite.globals.screen]
            termilite.globals.current_page.color_buffer  = [row[:] for row in termilite.globals.color_buffer]

        if self.screen_buffer is None:
            self.screen_buffer = [[' ' for _ in range(termilite.globals.screen_width)] for _ in range(termilite.globals.screen_height)]
            self.color_buffer  = [[termilite.color.RESET for _ in range(termilite.globals.screen_width)] for _ in range(termilite.globals.screen_height)]

        termilite.globals.windows = self.windows
        termilite.globals.current_page = self
        termilite.globals.page_changed = True

        if self.windows:
            sorted(self.windows, key=lambda w: w.z)[-1].focus()

    def add(self, window):
        """
        Adds a window to the page.

        Arguments:
            window (Window): Window to add to the page
        """

        if window not in self.windows:
            self.windows.append(window)

        if termilite.globals.current_page == self:
            termilite.globals.windows = self.windows

    def extend(self, windows):
        """
        Adds a list of windows to the page.

        Arguments:
            windows (list[Window]): List of windows to add
        """

        for window in windows:
            self.add(window)

    def remove(self, window):
        """
        Removes a window from the page

        Arguments:
            window (Window): Window to remove
        """

        if window in self.windows:
            self.windows.remove(window)

        if termilite.globals.current_page == self:
            termilite.globals.windows = self.windows

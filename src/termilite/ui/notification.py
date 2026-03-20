import time

import termilite

class Notification(termilite.Window):
    """
    Notification widget that slides in from the bottom right

    Attributes:
        title (str): Notification title
        message (str): Content of the notification
        width (int): Width of notification window
        height (int): Height of notification window
        duration (int): How long the notification stays for (after sliding in -> before sliding out)

        target_x (int): The X value the notification will slide to
        state (str): IN (sliding in) / STAY (stationary) / OUT (sliding out)
        speed (int): Cells moved in X direction per tick

    Helper functions:
        create_notification(
            title: str,
            message: str,
            width: int,
            height: int,
            duration: int = 5
        )
    """

    def __init__(self, title: str, message: str, width: int, height: int, duration: int):
        start_x = termilite.globals.screen_width - 1
        start_y = termilite.globals.screen_height - height - 2

        super().__init__(x=start_x, y=start_y, z=100, width=width, height=height, name=title)

        termilite.Label(self, 1, 1, message)

        self.target_x = termilite.globals.screen_width - width
        self.duration = duration
        self.start_time = 0
        self.state = "IN" # IN, STAY, OUT
        self.speed = 1    # Characters per frame

    def update(self):
        """
        NOTE: Function is called by engine, not required to call.

        Updates position of notification for animation
        """

        if self.state == "IN":
            if self.x > self.target_x:
                self.x -= self.speed
            else:
                self.x = self.target_x
                self.state = "STAY"
                self.start_time = time.time()

        elif self.state == "STAY":
            if time.time() - self.start_time >= self.duration:
                self.state = "OUT"

        elif self.state == "OUT":
            if self.x <= termilite.globals.screen_width:
                self.clear_ghost_buffer(self.x - self.speed)
                self.x += self.speed
            else:
                termilite.globals.windows.remove(self)
                return

        super().update()

    def clear_ghost_buffer(self, old_x: str):
        """
        NOTE: Function is called by engine, not required to call.

        Clears ghost buffers formed when moving around
        """

        for y in range(self.y - 1, termilite.globals.screen_height - 1):
            termilite.globals.screen[y][old_x] = ' '

def create_notification(title: str, message: str, width: int, height: int, duration: int = 5):
    return Notification(title, message, width, height, duration)

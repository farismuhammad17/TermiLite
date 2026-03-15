import termilite
import random

random.seed(sum([ord(c) for c in termilite.__author__]))

width, height = termilite.size

background = termilite.Window(x=0, y=0, width=width, height=height, z=0)
background.focussable = False

random_text = ""
for i in range(width * height):
    random_text += chr(random.randint(33, 126))

termilite.Label(background, 0, 0, random_text, color=termilite.color.FG_GREEN)

win_width = 65
win_height = 15

win = termilite.Window(
    x=(width - win_width) // 2, y=(height - win_height) // 2,
    width=win_width, height=win_height, z=1,
    margin_top = 2, margin_bottom = 2, margin_left = 4, margin_right = 4)

title = """_______                   _ _      _ _
|__   __|                (_) |    (_) |
   | | ___ _ __ _ __ ___  _| |     _| |_ ___
   | |/ _ \ '__| '_ ` _ \| | |    | | __/ _ \\
   | |  __/ |  | | | | | | | |____| | ||  __/
   |_|\___|_|  |_| |_| |_|_|______|_|\__\___|"""
subtitle = "- Light TUI Engine -"

title_width = 46 # Counted
title_height = 6 # Also counted

termilite.Label(win, (win_width - title_width) // 2, (win_height - title_height) // 2, title)
termilite.Label(win, (win_width - len(subtitle)) // 2, (win_height - title_height) // 2 + title_height + 1, "- Light TUI Engine -")

termilite.run(fps=60)

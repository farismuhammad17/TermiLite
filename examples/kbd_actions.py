import termilite

win = termilite.Window(x=5, y=5, width=60, height=30, z=0)

def change_window_clr(color: str):
    win.color = color

termilite.kbd_actions["0"] = lambda: change_window_clr(termilite.color.RESET)
termilite.kbd_actions["1"] = lambda: change_window_clr(termilite.color.BG_RED)
termilite.kbd_actions["2"] = lambda: change_window_clr(termilite.color.BG_BLUE)
termilite.kbd_actions["3"] = lambda: change_window_clr(termilite.color.BG_GREEN)
termilite.kbd_actions["4"] = lambda: change_window_clr(termilite.color.BG_YELLOW)

termilite.run(fps=60)

import termilite

win = termilite.Window(x=5, y=5, width=60, height=30, z=0)
label = termilite.Label(win, win.width // 2 - 3, win.height // 2, "Center") # 3 since len("Center") / 2 = 3

label.x = lambda: win.width // 2 - 3
label.y = lambda: win.height // 2
label.width = lambda: win.width

termilite.run(fps=60)

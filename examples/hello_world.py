import termilite

win1 = termilite.Window(x=5, y=5, width=60, height=30, z=0)
termilite.Label(win1, 10, 10, "Hello, World!")

termilite.run(fps=60)

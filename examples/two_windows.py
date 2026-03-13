import termilite

win1 = termilite.Window(x=5, y=5, width=60, height=30, z=0)
termilite.Label(win1, 10, 10, "Hello")

win2 = termilite.Window(x=40, y=10, width=30, height=20, z=1)
termilite.Label(win2, 5, 10, "Hello \x1b[31mRed\x1b[0m World")

termilite.run(fps=60)
import termilite

win1 = termilite.Window(x=20, y=5, width=60, height=30, z=0)

panel1 = termilite.Panel('l', 10, 1)
button = termilite.Button(panel1, 2, 2, "Button!", 10, 5)

panel2 = termilite.Panel('b', 10, 0)

termilite.run(fps=60)

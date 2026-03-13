import termilite

win1 = termilite.Window(x=5, y=5, width=60, height=30, z=0)
inp_box = termilite.InputBox(win1, 0, 0, maxlen=1500)
inp_box.underline = ''

termilite.run(fps=60)

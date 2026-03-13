import termilite

WIDTH=30
HEIGHT=23

win = termilite.Window(x=5, y=5, width=WIDTH, height=HEIGHT, z=0)

# If you don't set the height to 1, it takes up the entire window space, and the buttons won't work
inp     = termilite.Label(win, 2, 1, "", height=1)
hr      = termilite.Label(win, 0, 3, "-" * WIDTH, height=1)

btn1    = termilite.Button(win, 5, 5, "1", 1, 1, onclick=lambda: inp.append_text('1'))
btn2    = termilite.Button(win, 15, 5, "2", 1, 1, onclick=lambda: inp.append_text('2'))
btn3    = termilite.Button(win, 25, 5, "3", 1, 1, onclick=lambda: inp.append_text('3'))
btn4    = termilite.Button(win, 5, 8, "4", 1, 1, onclick=lambda: inp.append_text('4'))
btn5    = termilite.Button(win, 15, 8, "5", 1, 1, onclick=lambda: inp.append_text('5'))
btn6    = termilite.Button(win, 25, 8, "6", 1, 1, onclick=lambda: inp.append_text('6'))
btn7    = termilite.Button(win, 5, 11, "7", 1, 1, onclick=lambda: inp.append_text('7'))
btn8    = termilite.Button(win, 15, 11, "8", 1, 1, onclick=lambda: inp.append_text('8'))
btn9    = termilite.Button(win, 25, 11, "9", 1, 1, onclick=lambda: inp.append_text('9'))
btn0    = termilite.Button(win, 5, 14, "0", 1, 1, onclick=lambda: inp.append_text('0'))
btn_eq  = termilite.Button(win, 15, 14, "=", 1, 1, onclick=lambda: inp.set_text(eval(inp.get_text())))
btn_add = termilite.Button(win, 25, 14, "+", 1, 1, onclick=lambda: inp.append_text('+'))
btn_sub = termilite.Button(win, 5, 17, "-", 1, 1, onclick=lambda: inp.append_text('-'))
btn_mul = termilite.Button(win, 15, 17, "*", 1, 1, onclick=lambda: inp.append_text('*'))
btn_div = termilite.Button(win, 25, 17, "/", 1, 1, onclick=lambda: inp.append_text('/'))
btn_bac = termilite.Button(win, 5, 20, "<", 1, 1, onclick=lambda: inp.set_text(inp.get_text()[:-1]))

termilite.run(fps=60)

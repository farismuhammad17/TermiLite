from termilite import *

page1 = Page([])
page2 = Page([])

window1_page1 = Window(10, 10, 0, 40, 30, "Window 1")
window1_page2 = Window(5, 20, 0, 20, 30, "Window 2")

Button(window1_page1, 2, 2, "Switch", onclick=lambda: page2.load())
Button(window1_page2, 2, 2, "Swatch", onclick=lambda: page1.load())

page1.extend([window1_page1]) # Both does the same, its for demonstration purpose
page2.add(window1_page2)      # that I am doing this atrocity

page1.load()

run()

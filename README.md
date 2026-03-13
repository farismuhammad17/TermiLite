# TermiLite

A lightweight TUI engine designed in Python. Obviously, it isn't exactly done, but I plan to use it on various projects. So as time goes, future projects may require more stuff from this small library, and, overtime, the library will grow.

As of now, it has no dependencies, and works in any system. There is proper Z-indexing, windows, labels, buttons, input boxes, ANSI escape sequence parsing, and I plan to add the 'etc.' part later.

# Syntax

> [!IMPORTANT]  
> Program must start with `init` and end with `restore`

```py
Window(
    x: int,
    y: int,
    z: int,
    width: int,
    height: int
)

Window.is_draggable: bool
```

```py
Label(
    window: Window,
    x: int,
    y: int,
    text: str,
    width: int = None, # Assumes parent window size
    height: int = None
)
```

```py
InputBox(
    window: Window,
    x: int,
    y: int,
    width: int = None, # Assumes parent window size
    height: int = None,
    maxlen: int = 10
)

InputBox.value: str
InputBox.underline: str
InputBox.cursor: str
```

```py
Button(
    window: Window,
    x: int,
    y: int,
    text: str,
    width: int,
    height: int,
    onclick: lambda: None
)
```

# Examples

*All example codes can be found in the [examples](examples) folder*

## 1. Hello, World!

```py
import termilite

win1 = termilite.Window(x=5, y=5, width=60, height=30, z=0)
termilite.Label(win1, 10, 10, "Hello, World!")

termilite.run(fps=60)
```

The `Window` object creates a window on the screen, to which we create a `Label`, where we write down the text we want.

## 2. Two windows

```py
import termilite

win1 = termilite.Window(x=5, y=5, width=60, height=30, z=0)
termilite.Label(win1, 10, 10, "Hello")

win2 = termilite.Window(x=40, y=10, width=30, height=20, z=1)
termilite.Label(win2, 5, 10, "Hello \x1b[31mRed\x1b[0m World")

termilite.run(fps=60)
```

Creates two `Window` objects, each with a `Label`.

## 3. Input box

```py
import termilite

win1 = termilite.Window(x=5, y=5, width=60, height=30, z=0)
inp_box = termilite.InputBox(win1, 0, 0, maxlen=1500)
inp_box.underline = ''

termilite.run(fps=60)
```

Underline's charcater is changed to nothing to make a clean notepad like window.

## 4. Calculator

```py
import termilite

WIDTH=30
HEIGHT=23

win = termilite.Window(x=5, y=5, width=WIDTH, height=HEIGHT, z=0)

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
```

It is crucial that the two `Label` objects must have specified height, or else they take up the whole window, and the buttons won't be clickable.

---

*Distributed under the MIT License. See [LICENSE](LICENSE) for more information.*

import tkinter as tk

BUTTON_WIDTH = 40
BUTTON_HEIGHT = 10

def copy_to_clipboard(text):
    window.clipboard_clear()
    window.clipboard_append(text)

window = tk.Tk()

button = tk.Button(
    text="button",
    width=BUTTON_WIDTH,
    bg="white",
    fg="black",
    command=copy_to_clipboard("dsdfadf")
)
button.pack()

window.mainloop()
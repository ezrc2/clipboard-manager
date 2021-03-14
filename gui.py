from database import Database
import tkinter as tk
from datetime import datetime as dt

BUTTON_WIDTH = 50

def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)

def update_clipboard_history():
    text = root.clipboard_get()
    date_time = dt.today().strftime("%m-%d-%Y, %H:%M:%S")
    db.store_clip(date_time, text)

if __name__ == "__main__":
    root = tk.Tk()
    db = Database()
    db.store_clip("2", "aaaaa")
    db.store_clip(3, "dadfasdf")

    rows = db.get_clips()
    for datetime, text in rows:
        button_text = f"{datetime}: {text}"
        b = tk.Button(root, width=BUTTON_WIDTH, text=button_text, command=lambda text=text: copy_to_clipboard(text))
        b.pack(fill=tk.X, side=tk.BOTTOM)

    root.mainloop()
    #update_clipboard_history()
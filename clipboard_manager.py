from database import Database
import tkinter as tk
from datetime import datetime as dt

class ClipboardManager:

    def __init__(self):
        self.width = 50
        self.truncate_length = self.width + 10
        self.delay = 100

        self.root = tk.Tk()
        self.root.title("Clipboard Manager")

        self.db = Database()
        self.prev_clip = self.root.clipboard_get()

    def copy_to_clipboard(self, text):
        self.root.clipboard_clear()
        self.root.clipboard_append(text)

    def read_from_clipboard(self):
        text = self.root.clipboard_get()

        # Only copy if clipboard content changes, or else it will constantly copy
        if text != self.prev_clip: 
            self.prev_clip = text
            print("copied")
            date_time = dt.today().strftime("(%m/%d %I:%M %p)")
            self.db.store_clip(date_time, text)
        
        self.root.after(self.delay, self.read_from_clipboard)
    
    def run(self):
        rows = self.db.get_clips()
        for datetime, text in rows:
            button_text = f"{datetime}: {text}"

            if len(button_text) > self.truncate_length:
                button_text = button_text[:self.truncate_length] + " ..."

            button = tk.Button(self.root, width=self.width, text=button_text, command=lambda text=text: self.copy_to_clipboard(text))
            button.pack(fill=tk.X, side=tk.BOTTOM)

        clear_button = tk.Button(self.root, width=self.width // 5, background="red", 
            text="Clear History", fg="red", command=lambda: self.db.clear_clips())
        clear_button.pack()
        
        self.read_from_clipboard()
        self.root.mainloop()

if __name__ == "__main__":
    ClipboardManager().run()
    
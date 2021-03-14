from database import Database
import tkinter as tk
from datetime import datetime as dt

class ClipboardManager:

    def __init__(self):
        self.width = 50
        self.truncate_length = 75
        self.delay = 100

        self.root = tk.Tk()
        self.root.title("Clipboard Manager")

        self.db = Database()
        self.db.create_table()
        self.prev_clip = self.root.clipboard_get()
        if self.prev_clip is None:
            self.prev_clip = ""

    def copy_to_clipboard(self, text):
        """Copies the selected text to the clipboard and removes previous entries 
        with the same text from the database
        """
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.db.delete_clip(text)

    def read_from_clipboard(self):
        """Checks the clipboard for a newly copied item. If there is, insert into database"""
        text = self.root.clipboard_get()

        # Only insert if clipboard content changes, or else it will constantly copy
        if text != self.prev_clip: 
            self.prev_clip = text
            date_time = dt.today().strftime("(%m/%d %I:%M %p)")
            self.db.insert_clip(date_time, text)
        
        self.root.after(self.delay, self.read_from_clipboard)
    
    def update(self):
        """Rebuilds the root window to show any changes made"""
        if (self.root.winfo_children() is not None):
            for widget in self.root.winfo_children():
                widget.destroy()
            self.add_buttons()

        self.root.after(self.delay, self.update)

    def add_buttons(self):
        """Adds a button for each row in the database in a date, time, text format
        to the root window
        """
        rows = self.db.get_clips()
        for datetime, text in rows:
            button_text = f"{datetime}: {text}"

            if len(button_text) > self.truncate_length:
                button_text = button_text[:self.truncate_length] + " ..."

            # Use default parameter in lambda function to avoid late-binding issue
            button = tk.Button(self.root, width=self.width, text=button_text, anchor="w",
                command=lambda text=text: self.copy_to_clipboard(text))

            button.pack(fill=tk.X, side=tk.BOTTOM)

        clear_button = tk.Button(self.root, width=self.width, background="red", 
            text="Clear History", fg="red", command=lambda: self.db.clear_clips())
        clear_button.pack()

    def main(self):
        self.read_from_clipboard()
        self.update()
        self.root.mainloop()

if __name__ == "__main__":
    ClipboardManager().main()
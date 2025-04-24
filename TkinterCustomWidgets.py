import tkinter as tk
from tkinter import ttk

class LabeledEntry(ttk.Frame):
    def __init__(self, master, label_text, **kwargs):
        super().__init__(master, **kwargs)
        self.label = ttk.Label(self, text=label_text)
        self.entry = ttk.Entry(self)
        self.label.pack(side=tk.LEFT, padx=(0, 5))
        self.entry.pack(side=tk.LEFT, expand=True, fill=tk.X)

    def get(self):
        return self.entry.get()

    def set(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)

class ColorPicker(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.r = ttk.Scale(self, from_=0, to=255, command=self.update_color)
        self.g = ttk.Scale(self, from_=0, to=255, command=self.update_color)
        self.b = ttk.Scale(self, from_=0, to=255, command=self.update_color)
        self.color_display = tk.Canvas(self, width=50, height=50)

        self.r.pack(fill=tk.X)
        self.g.pack(fill=tk.X)
        self.b.pack(fill=tk.X)
        self.color_display.pack(pady=10)

        self.update_color()

    def update_color(self, *args):
        r = int(self.r.get())
        g = int(self.g.get())
        b = int(self.b.get())
        color = f'#{r:02x}{g:02x}{b:02x}'
        self.color_display.config(bg=color)

    def get_color(self):
        return f'#{int(self.r.get()):02x}{int(self.g.get()):02x}{int(self.b.get()):02x}'

class CustomWidgetDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Custom Widget Demo")
        self.geometry("300x400")

        self.labeled_entry = LabeledEntry(self, "Name:")
        self.labeled_entry.pack(padx=10, pady=10, fill=tk.X)

        self.color_picker = ColorPicker(self)
        self.color_picker.pack(padx=10, pady=10, fill=tk.X)

        self.submit_button = ttk.Button(self, text="Submit", command=self.on_submit)
        self.submit_button.pack(pady=10)

    def on_submit(self):
        name = self.labeled_entry.get()
        color = self.color_picker.get_color()
        print(f"Name: {name}, Color: {color}")

if __name__ == "__main__":
    app = CustomWidgetDemo()
    app.mainloop()

"""
This script demonstrates creating custom widgets in Tkinter:
1. LabeledEntry: A combination of Label and Entry
2. ColorPicker: A custom widget for picking colors

Key points:
- Custom widgets can be created by subclassing ttk.Frame or tk.Frame
- Composition of existing widgets to create more complex ones
- Custom methods can be added to enhance widget functionality

Applications:
1. Creating reusable UI components
2. Implementing complex input methods
3. Building domain-specific interface elements
4. Enhancing user experience with tailored widgets
"""
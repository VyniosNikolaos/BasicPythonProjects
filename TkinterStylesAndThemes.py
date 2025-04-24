import tkinter as tk
from tkinter import ttk

class StyleDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Style Demo")
        self.geometry("400x300")

        self.style = ttk.Style()
        self.create_widgets()
        self.create_custom_style()

    def create_widgets(self):
        frame = ttk.Frame(self, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Default Button:").pack(pady=5)
        ttk.Button(frame, text="Click Me").pack()

        ttk.Label(frame, text="Custom Style Button:").pack(pady=5)
        ttk.Button(frame, text="Styled Button", style="Custom.TButton").pack()

        ttk.Label(frame, text="Themes:").pack(pady=5)
        themes = ttk.Combobox(frame, values=self.style.theme_names())
        themes.pack()
        themes.set(self.style.theme_use())
        themes.bind("<<ComboboxSelected>>", self.change_theme)

    def create_custom_style(self):
        self.style.configure("Custom.TButton",
                             foreground="white",
                             background="#007bff",
                             font=("Helvetica", 12, "bold"),
                             padding=10)
        
        self.style.map("Custom.TButton",
                       foreground=[('pressed', 'white'), ('active', 'black')],
                       background=[('pressed', '!disabled', '#0056b3'), ('active', '#0056b3')])

    def change_theme(self, event):
        theme = event.widget.get()
        self.style.theme_use(theme)

if __name__ == "__main__":
    app = StyleDemo()
    app.mainloop()

"""
This script demonstrates styling and theming in Tkinter:
1. Creating and applying custom styles to widgets
2. Using built-in themes
3. Dynamically changing themes

Key points:
- ttk.Style() is used to create and modify styles
- Styles can be applied to ttk widgets
- Tkinter supports multiple themes which can be switched at runtime

Applications:
1. Creating consistent look and feel across an application
2. Implementing dark mode or multiple color schemes
3. Customizing widget appearance for branding
4. Improving accessibility with high-contrast themes
"""
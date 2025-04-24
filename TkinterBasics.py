import tkinter as tk

def button_click():
    label.config(text="Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Tkinter Basics")
root.geometry("300x200")

# Create and pack a label
label = tk.Label(root, text="Welcome to Tkinter!")
label.pack(pady=20)

# Create and pack a button
button = tk.Button(root, text="Click me!", command=button_click)
button.pack()

# Start the Tkinter event loop
root.mainloop()

"""
This script demonstrates the basics of creating a GUI with Tkinter:
1. Importing the tkinter module
2. Creating a main window
3. Adding widgets (Label and Button)
4. Defining a callback function for button click
5. Starting the Tkinter event loop

To run: Simply execute this script with Python.

Applications:
1. Creating simple desktop applications
2. Prototyping user interfaces
3. Building tools with graphical interfaces for non-technical users
4. Creating custom dialogs and forms
"""
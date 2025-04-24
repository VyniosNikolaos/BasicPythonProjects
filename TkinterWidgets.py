import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def show_message():
    name = name_entry.get()
    age = age_spinbox.get()
    country = country_combobox.get()
    message = f"Name: {name}\nAge: {age}\nCountry: {country}"
    messagebox.showinfo("User Info", message)

# Create the main window
root = tk.Tk()
root.title("Tkinter Widgets Demo")
root.geometry("300x250")

# Label and Entry for Name
tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Label and Spinbox for Age
tk.Label(root, text="Age:").grid(row=1, column=0, padx=5, pady=5)
age_spinbox = tk.Spinbox(root, from_=1, to=120)
age_spinbox.grid(row=1, column=1, padx=5, pady=5)

# Label and Combobox for Country
tk.Label(root, text="Country:").grid(row=2, column=0, padx=5, pady=5)
country_combobox = ttk.Combobox(root, values=["USA", "UK", "Canada", "Australia"])
country_combobox.grid(row=2, column=1, padx=5, pady=5)

# Button to submit
submit_button = tk.Button(root, text="Submit", command=show_message)
submit_button.grid(row=3, column=0, columnspan=2, pady=20)

# Start the Tkinter event loop
root.mainloop()

"""
This script showcases various Tkinter widgets:
1. Label: For displaying text
2. Entry: For text input
3. Spinbox: For numeric input within a range
4. Combobox: For selecting from a list of options
5. Button: For triggering actions
6. MessageBox: For displaying information in a popup

To run: Execute this script with Python.

Applications:
1. Creating forms for data entry
2. Building configuration interfaces
3. Developing custom dialog boxes
4. Creating interactive dashboards
"""
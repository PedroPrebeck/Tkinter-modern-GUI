import tkinter as tk
import ttkbootstrap as ttk

def get_input():
    entry_text = entry.get()
    label['text'] = entry_text
    entry['state'] = 'disabled'

def restore_input():
    label['text'] = "Hello World"
    entry['state'] = 'enabled'

# Create a window
window = ttk.Window(themename = "superhero")
window.title("Getting and Setting Widgets")

# Label
label = ttk.Label(window, text = "Hello World")

# Entry
entry = ttk.Entry(window,  width = 50)

# Button
button = ttk.Button(window, text = "Click Me", command = get_input)

# Exercise button
exercise_button = ttk.Button(window, text = "Exercise", command = restore_input)

# Packing
label.pack()
entry.pack()
button.pack()
exercise_button.pack()

# Run
window.mainloop()
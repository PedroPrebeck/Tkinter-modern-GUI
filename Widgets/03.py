import tkinter as tk
import ttkbootstrap as ttk

def button_clicked():
    string_var.set("Button clicked")

# Create a window
window = ttk.Window(themename = "superhero")
window.title("Tkinter Variables")

# Tkinter Variables
string_var = tk.StringVar()

# Label
label = ttk.Label(master=window, text = "Hello World", textvariable=string_var)

# Entry
entry = ttk.Entry(master=window, textvariable=string_var)

# Button
button = ttk.Button(master=window, text = "Click Me", command=button_clicked)


# Exercise
exercise_var = tk.StringVar(value = "Test")

entry1 = ttk.Entry(master=window, textvariable = exercise_var)
entry2 = ttk.Entry(master=window, textvariable = exercise_var)
exercise_label = ttk.Label(master=window, textvariable=exercise_var)

# Packing
label.pack()
entry.pack()
button.pack()

entry1.pack()
entry2.pack()
exercise_label.pack()

# Run
window.mainloop()
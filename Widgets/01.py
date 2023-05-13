import tkinter as tk
import ttkbootstrap as ttk

def button_func():
    print("Button pressed")

# Create a window
window = ttk.Window(themename = "superhero")
window.title("Window and Widgets")
window.geometry("800x500")

# Ttk label
label = ttk.Label(master = window, text = "This is a test")
label.pack()

# Tk text
text = tk.Text(master = window)
text.pack()

# Ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# Exercise label
exercise_label = ttk.Label(master = window, text = "My label")
exercise_label.pack()

# Ttk button
button = ttk.Button(master = window, text = "A button", command = button_func)
button.pack()

# Exercise button
exercise_button = ttk.Button(master = window,
                            text = "Exercise button",
                            command = lambda: print("hello"))
exercise_button.pack()

# Run
window.mainloop()
import tkinter as tk
import ttkbootstrap as ttk

def convert_miles_to_km():
    miles_input = float(entry_float.get())
    km_output = miles_input * 1.609
    output_string.set(f"{km_output:.2f}")

# Window
window = ttk.Window(themename = "cosmo")
window.title("Demo")
window.geometry("300x150")

# Title
title_label = ttk.Label(master = window,
                        text = "Miles to Kilometers",
                        font = "Calibri 24 bold")
title_label.pack()

# Input field
input_frame = ttk.Frame(master = window)
entry_float = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_float)
button = ttk.Button(master = input_frame, text = "Convert", command = convert_miles_to_km)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack(pady = 10)

# Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window,
                        text = "0",
                        font = "Calibri 24",
                        textvariable = output_string)
output_label.pack(pady = 5)

# Run
window.mainloop()
import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title("Quote Estimate")

app.geometry("800x200")

entries = []
labels = ["Base Rate", "Length", "Implementation"]
buttons = []

frame_column = ttk.Frame(app)
frame_column.columnconfigure(0, weight=1)
frame_column.columnconfigure(1, weight=1)
frame_column.columnconfigure(2, weight=1)

frame_row = ttk.Frame(app)
frame_row.rowconfigure(0, weight=1)
frame_row.rowconfigure(1, weight=1)

# TODO: Align Label above each Entry widget

for index, label in enumerate(labels):
    # tk.Label requires a parent widget (app in this case) and a text argument, with optinal font parameters
    label = tk.Label(frame_column, text=label)
    label.grid(row=0, column=index, padx=5, pady=5, stick="we")
   
    entry = tk.Entry(frame_column)
    #  Pack prints the widget in the parent widget (app) and allows for padding and side alignment
    entry.grid(row=1, column=index, padx=5, pady=5, sticky="we")

    entries.append(entry)

frame_column.pack(padx=10, pady=10, fill=tk.X)

# button = tk.Button(app, text="Calculate", command=lambda: print("Calculating..."))
# button.pack(padx=5, pady=5, side=tk.LEFT)

app.mainloop()

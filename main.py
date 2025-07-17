import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title("Quote Estimate")

entries = []

labels = ["Base Rate", "Length", "Implementation"]

# TODO: Manage placement via grid

for label in labels:
    label = tk.Label(app, text=label)
    label.pack(padx=5, pady=5, side=tk.LEFT)

    entry = tk.Entry(app)
    entry.pack(padx=5, pady=5, side=tk.BOTTOM)

    entries.append(entry)

app.mainloop()

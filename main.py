import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title("Quote Estimate")

app.geometry("800x200")
labels = [{"type": "entry", "name": "Base Rate"}, {"type": "entry", "name": "Length"}, {"type": "combo", "name": "Complexity"}, {"type": "entry", "name": "Variations"}, {"type": "combo", "name": "Implementation"}, {"type": "entry", "name": "Buffer"}, {"type": "label", "name": "Total"}]

frame_column = ttk.Frame(app)

for i, label in enumerate(labels):
    frame_column.columnconfigure(i, weight=1)

for index, label in enumerate(labels):
    label_iteration = tk.Label(frame_column, text=label["name"])
    label_iteration.grid(row=0, column=index, padx=5, pady=5)
   
    if label["type"] == "entry":
        entry = tk.Entry(frame_column)
        entry.grid(row=1, column=index, padx=5, pady=5)
    if label["type"] == "combo":
        combo = ttk.Combobox(frame_column)
        combo.grid(row=1, column=index, padx=5, pady=5)
    if label["type"] == "label":
        text = tk.Label(frame_column, text="Calculate Total Hours")
        text.grid(row=1, column=index, padx=5, pady=5)

frame_column.pack(padx=5, pady=5, fill=tk.X)

# button = tk.Button(app, text="Calculate", command=lambda: print("Calculating..."))
# button.pack(padx=5, pady=5, side=tk.LEFT)

app.mainloop()

import tkinter as tk
from tkinter import ttk

# TODO: Convert to a class-based structure for better organization

app = tk.Tk()
app.title("Quote Estimate")
app.geometry("1080x720")

labels = [{"type": "entry", "name": "Base Rate"}, {"type": "entry", "name": "Length"}, {"type": "combo", "name": "Complexity"}, {"type": "entry", "name": "Variations"}, {"type": "combo", "name": "Implementation"}, {"type": "entry", "name": "Buffer"}, {"type": "label", "name": "Estimated Hours"}, {"type": "label", "name": "Total Cost"}]
fields = []
est_hours = None
total_cost = None

frame_column = ttk.Frame(app)

#  TODO: Dynamically adjust non-combo widgets to be smaller
def setup_grid():
    for i, label in enumerate(labels):
        if label["type"] != "combo":
            frame_column.columnconfigure(i, weight=1)
        else:
            frame_column.columnconfigure(i, weight=1)

def pack_widgets():
    for index, label in enumerate(labels):
        label_iteration = tk.Label(frame_column, text=label["name"])
        label_iteration.grid(row=0, column=index, padx=5, pady=5)
    
        if label["type"] == "entry":
            entry = tk.Entry(frame_column)
            entry.grid(row=1, column=index, padx=5, pady=5)
            fields.append(entry)
        if label["type"] == "combo":
            combo = ttk.Combobox(frame_column)
            combo.grid(row=1, column=index, padx=5, pady=5)
            fields.append(combo)
            if label["name"] == "Complexity":
                combo["values"] = ["Low", "Medium", "High"]
                combo.current(0)
            if label["name"] == "Implementation":
                combo["values"] = ["Basic", "Moderate", "Extensive"]
                combo.current(0)
        if label["type"] == "label":
            text = tk.Label(frame_column)
            text.grid(row=1, column=index, padx=5, pady=5)
            fields.append(text)

    frame_column.pack(padx=5, pady=5, fill=tk.X)
    calc_btn = tk.Button(app, text="Calculate", command=calculate_estimated_hours)
    calc_btn.pack(pady=10)

# TODO: Add error handling for empty or invalid inputs
def calculate_estimated_hours():
    try:
        base_rate = float(fields[0].get())
        length = float(fields[1].get())

        complexity = None

        if fields[2].get() == "Low":
            complexity = 4.0
        elif fields[2].get() == "Medium":
            complexity = 5.0
        elif fields[2].get() == "High":
            complexity = 6.0

        variations = float(fields[3].get())

        implementation = None

        if fields[4].get() == "Basic":
            implementation = 1.0
        elif fields[4].get() == "Moderate":
            implementation = 2.0
        elif fields[4].get() == "Extensive":
            implementation = 3.0

        buffer = float(fields[5].get())
        result = (length * complexity) + variations + implementation + buffer

        fields[6].config(text=str(result))
        fields[7].config(text=str(result * base_rate))
    except ValueError:
        fields[6].config(text="Error")
        fields[7].config(text="Error")

setup_grid()
pack_widgets()

app.mainloop()

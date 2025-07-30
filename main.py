from os import error
import tkinter as tk
from tkinter import ttk, messagebox


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.labels = [
            {"type": "entry", "name": "Base Rate", "mandatory": True, "field": ""},
            {"type": "entry", "name": "Length", "mandatory": True, "field": ""},
            {"type": "combo", "name": "Complexity", "mandatory": True, "field": ""},
            {"type": "entry", "name": "Variations", "mandatory": True, "field": ""},
            {"type": "combo", "name": "Implementation", "mandatory": True, "field": ""},
            {"type": "entry", "name": "Buffer", "mandatory": False, "field": ""},
            {"type": "label", "name": "Estimated Hours", "mandatory": False, "field": ""},
            {"type": "label", "name": "Total Cost", "mandatory": False, "field": ""},
        ]

        self.title("Quote Estimate")
        self.geometry("1080x720")

        self.fields = []
        self.entry_fields = []
        self.mandatory_fields = []
        self.frame_column = ttk.Frame(self)

        # TODO: Develop a more efficient way to handle labels and fields.

        self.setup_grid()
        self.pack_widgets()

    def setup_grid(self):
        """Set up the grid configuration for the frame.
        Args:           None
        Returns:        None
        """
        for i, label in enumerate(self.labels):
            self.frame_column.columnconfigure(i, weight=1)

    def pack_widgets(self):
        """Creates and packs the widgets in the frame. The calculate button calls the calculate_estimated_hours
        method to calculate the results.
        Args:           None
        Returns:        None
        """
        for index, label in enumerate(self.labels):
            if label["type"] == "entry":
                entry = tk.Entry(self.frame_column)
                entry.grid(row=1, column=index, padx=5, pady=5)
                label["field"] = entry
            elif label["type"] == "combo":
                combo = ttk.Combobox(self.frame_column)
                combo.grid(row=1, column=index, padx=5, pady=5)
                label["field"] = combo
                if label["name"] == "Complexity":
                    combo["values"] = [1, 2, 3]
                    combo.current(0)
                if label["name"] == "Implementation":
                    combo["values"] = [1, 2, 3]
                    combo.current(0)
            elif label["type"] == "label":
                text = tk.Label(self.frame_column, bg="grey", width=20)
                text.grid(row=1, column=index, padx=5, pady=5)
                label["value"] = text

            if label["mandatory"]:
                label["name"] += " *"

            label_iteration = tk.Label(self.frame_column, text=label["name"])
            label_iteration.grid(row=0, column=index, padx=5, pady=5)

        self.frame_column.pack(padx=5, pady=5, fill=tk.X)
        calc_btn = tk.Button(
            self, text="Calculate", command=self.calculate_estimated_hours
        )
        calc_btn.pack(pady=10)

    def calculate_estimated_hours(self):
        """Adds calculation logic to the calculate button, checks for mandatory fields, and validates numeric entries.
        Args:           None
        Raises:         ValueError if any mandatory field is empty or if numeric fields contain non-numeric values.
        Displays:       Error messages for missing fields or invalid numeric entries.
        Calculates:     Estimated hours and total cost based on the provided inputs.
        Returns:        None
        """
        # TODO: Display all errors in a single message box instead of multiple pop-ups.
        # TODO: Apply colour change to entry fields only to avoid crashing when reaching combo fields. 
        
        values = []

        for label in self.labels:
            if label["type"] == "entry" and not label["field"].get():
                label["field"].config(highlightbackground="red")
                messagebox.showerror(
                    "Missing Field", f"Please fill in the {label['name']} field."
                )
                return
            if label["type"] == "combo" and not label["field"].get():
                messagebox.showerror(
                    "Missing Field", f"Please select a value for {label['name']}."
                )
                return
            
        # TODO: get() returns an attribute error.
        try:
            for label in self.labels:
                values.append(float(label["field"].get()))

            print(values)
                    
            result = (values[1] * values[2]) + values[3] + values[4] + values[5]

            self.fields[6].config(text=str(result))
            self.fields[7].config(text=str(result * values[0]))
        except ValueError:
            self.fields[6].config(text="Error")
            self.fields[7].config(text="Error")


if __name__ == "__main__":
    app = App()
    app.mainloop()

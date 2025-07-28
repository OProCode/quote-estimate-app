import tkinter as tk
from tkinter import ttk, messagebox


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.labels = [
            {"type": "entry", "name": "Base Rate"},
            {"type": "entry", "name": "Length"},
            {"type": "combo", "name": "Complexity"},
            {"type": "entry", "name": "Variations"},
            {"type": "combo", "name": "Implementation"},
            {"type": "entry", "name": "Buffer"},
            {"type": "label", "name": "Estimated Hours"},
            {"type": "label", "name": "Total Cost"},
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
            label_iteration = tk.Label(self.frame_column, text=label["name"])
            label_iteration.grid(row=0, column=index, padx=5, pady=5)

            if label["type"] == "entry":
                entry = tk.Entry(self.frame_column)
                entry.grid(row=1, column=index, padx=5, pady=5)
                self.fields.append(entry)
                self.mandatory_fields.append(entry)
                self.entry_fields.append(entry)
            elif label["type"] == "combo":
                combo = ttk.Combobox(self.frame_column)
                combo.grid(row=1, column=index, padx=5, pady=5)
                self.fields.append(combo)
                self.mandatory_fields.append(combo)
                if label["name"] == "Complexity":
                    combo["values"] = ["Low", "Medium", "High"]
                    combo.current(0)
                if label["name"] == "Implementation":
                    combo["values"] = ["Basic", "Moderate", "Extensive"]
                    combo.current(0)
            elif label["type"] == "label":
                text = tk.Label(self.frame_column, bg="grey", width=20)
                text.grid(row=1, column=index, padx=5, pady=5)
                self.fields.append(text)

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
        for field in self.mandatory_fields:
            if not field.get():
                messagebox.showerror(
                    "Missing Field", "Please fill in all mandatory fields."
                )
                return

        for field in self.entry_fields:
                try:
                    float(field.get())
                except ValueError:
                    messagebox.showerror(
                        "Invalid Value", "Entry fields must contain numeric values."
                    )
                    return

        try:
            base_rate = float(self.fields[0].get())
            length = float(self.fields[1].get())

            complexity = {"Low": 4.0, "Medium": 5.0, "High": 6.0}.get(
                self.fields[2].get(), 4.0
            )
            variations = float(self.fields[3].get())
            implementation = {"Basic": 1.0, "Moderate": 2.0, "Extensive": 3.0}.get(
                self.fields[4].get(), 1.0
            )
            buffer = float(self.fields[5].get())

            result = (length * complexity) + variations + implementation + buffer

            self.fields[6].config(text=str(result))
            self.fields[7].config(text=str(result * base_rate))
        except ValueError:
            self.fields[6].config(text="Error")
            self.fields[7].config(text="Error")


if __name__ == "__main__":
    app = App()
    app.mainloop()

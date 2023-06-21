import tkinter as tk
from MeteoWidget.MeteoWidget import MeteoWidget

class MeteoWidgetGUI():
    def __init__(self, root):
        self.root = root
        self.root.title("MeteoWidget")

        # Checkbox variables
        self.checkbox_var1 = tk.BooleanVar()
        self.checkbox_var2 = tk.BooleanVar()
        self.checkbox_var3 = tk.BooleanVar()

        # Latitude and longitude variables
        self.latitude_var = tk.StringVar()
        self.longitude_var = tk.StringVar()

        # Create checkbox
        self.checkbox_frame = tk.Frame(root)
        self.checkbox_frame.pack(pady=10)
        self.checkbox_label = tk.Label(self.checkbox_frame, text="Select items:")
        self.checkbox_label.pack()
        self.checkbox_item1 = tk.Checkbutton(self.checkbox_frame, text="Item 1", variable=self.checkbox_var1)
        self.checkbox_item1.pack()
        self.checkbox_item2 = tk.Checkbutton(self.checkbox_frame, text="Item 2", variable=self.checkbox_var2)
        self.checkbox_item2.pack()
        self.checkbox_item3 = tk.Checkbutton(self.checkbox_frame, text="Item 3", variable=self.checkbox_var3)
        self.checkbox_item3.pack()

        # Create latitude and longitude entry fields
        self.location_frame = tk.Frame(root)
        self.location_frame.pack(pady=10)
        self.latitude_label = tk.Label(self.location_frame, text="Latitude:")
        self.latitude_label.grid(row=0, column=0, padx=5)
        self.latitude_entry = tk.Entry(self.location_frame, textvariable=self.latitude_var)
        self.latitude_entry.grid(row=0, column=1, padx=5)
        self.longitude_label = tk.Label(self.location_frame, text="Longitude:")
        self.longitude_label.grid(row=1, column=0, padx=5)
        self.longitude_entry = tk.Entry(self.location_frame, textvariable=self.longitude_var)
        self.longitude_entry.grid(row=1, column=1, padx=5)

        # Create Run MeteoWidget button
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)
        self.run_button = tk.Button(self.button_frame, text="Run MeteoWidget", command=self.run_meteo_widget)
        self.run_button.pack()

    def run_meteo_widget(self):
        latitude = float(self.latitude_var.get())
        longitude = float(self.longitude_var.get())

        # Perform actions based on checkbox selections
        if self.checkbox_var1.get():
            print("Item 1 selected.")
            # Perform item 1 action

        if self.checkbox_var2.get():
            print("Item 2 selected.")
            # Perform item 2 action

        if self.checkbox_var3.get():
            print("Item 3 selected.")
            # Perform item 3 action

        # Create MeteoWidget and retrieve forecast
        meteo_widget = MeteoWidget(latitude, longitude)
        forecast = meteo_widget.get_forecast()
        print(forecast)
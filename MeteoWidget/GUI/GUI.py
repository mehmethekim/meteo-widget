import tkinter as tk
from MeteoWidget.MeteoWidget import MeteoWidget

class MeteoWidgetGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MeteoWidget")
        
        # Checkbox variables
        self.hourly_temperature_2m = tk.BooleanVar()
        self.hourly_relative_humidity_2m = tk.BooleanVar()
        self.hourly_rain = tk.BooleanVar()

        self.daily_maximum_temperature_2m = tk.BooleanVar()
        self.daily_minimum_temperature_2m = tk.BooleanVar()

        # Latitude and longitude variables
        self.latitude_var = tk.StringVar()
        self.longitude_var = tk.StringVar()

        # Create Hourly section
        self.hourly_frame = tk.Frame(root)
        self.hourly_frame.pack(pady=10)

        self.hourly_label = tk.Label(self.hourly_frame, text="Hourly Weather Variables:")
        self.hourly_label.pack()

        self.hourly_temperature_2m_checkbox = tk.Checkbutton(self.hourly_frame, text="Temperature (2m)", variable=self.hourly_temperature_2m)
        self.hourly_temperature_2m_checkbox.pack()

        self.hourly_relative_humidity_2m_checkbox = tk.Checkbutton(self.hourly_frame, text="Relative Humidity (2 m)", variable=self.hourly_relative_humidity_2m)
        self.hourly_relative_humidity_2m_checkbox.pack()

        self.hourly_rain_checkbox = tk.Checkbutton(self.hourly_frame, text="Rain", variable=self.hourly_rain)
        self.hourly_rain_checkbox.pack()


        # Create Daily section
        self.daily_frame = tk.Frame(root)
        self.daily_frame.pack(pady=10)

        self.daily_label = tk.Label(self.daily_frame, text="Daily Weather Variables:")
        self.daily_label.pack()
        self.daily_maximum_temperature_2m_checkbox = tk.Checkbutton(self.daily_frame, text="Maximum Temperature (2m)", variable=self.daily_maximum_temperature_2m)
        self.daily_maximum_temperature_2m_checkbox.pack()
        self.daily_minimum_temperature_2m_checkbox = tk.Checkbutton(self.daily_frame, text="Minimum Temperature (2m)", variable=self.daily_minimum_temperature_2m)
        self.daily_minimum_temperature_2m_checkbox.pack()

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


        #Set window dimensions and center it on the screen
        window_width = 400
        window_height = 300
        screen_width =  self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
    

    def run_meteo_widget(self):
        latitude = float(self.latitude_var.get())
        longitude = float(self.longitude_var.get())

        # Perform actions based on Hourly checkbox selections
        if self.hourly_temperature_2m.get():
            print("Hourly Option 1 selected.")
            # Perform Hourly Option 1 action

        if self.hourly_relative_humidity_2m.get():
            print("Hourly Option 2 selected.")
            # Perform Hourly Option 2 action

        # Perform actions based on Daily checkbox selections
        if self.daily_maximum_temperature_2m.get():
            print("Daily Option 1 selected.")
            # Perform Daily Option 1 action

        if self.daily_minimum_temperature_2m.get():
            print("Daily Option 2 selected.")
            # Perform Daily Option 2 action

        # Create MeteoWidget and retrieve forecast
        meteo_widget = MeteoWidget(latitude, longitude)
        forecast = meteo_widget.get_forecast()
        print(forecast)
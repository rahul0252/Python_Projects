import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import ttk as tk_tt

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("450x700")
        self.root.resizable(True, True)

        self.api_key = "91539538b13ebf225a14a5385e741ad8"
 
        # Variables to store current state
        self.current_city = None
        self.current_country = None
        self.current_description = None
        self.current_icon_url = None
        self.current_temperature = None
        self.current_humidity = None
        self.current_unit = tk.StringVar(value="metric")

        # Configure grid layout
        self.root.columnconfigure(0, weight=1)

        # City entry
        self.city_entry = ttk.Entry(root, font=("Helvetica", 16), justify='center')
        self.city_entry.grid(row=0, column=0, pady=(20, 10), padx=20, sticky="ew")

        # Search button
        self.search_btn = ttk.Button(root, text="Search", command=self.search_weather, bootstyle=PRIMARY)
        self.search_btn.grid(row=1, column=0, pady=10, padx=20, sticky="ew")

        # Temperature unit selection
        unit_frame = ttk.LabelFrame(root, text="Select Unit", bootstyle=INFO)
        unit_frame.grid(row=2, column=0, pady=10, padx=20, sticky="ew")

        self.unit_celsius = ttk.Radiobutton(unit_frame, text="Celsius", variable=self.current_unit,
                                            value="metric", command=self.update_unit)
        self.unit_celsius.pack(side="left", expand=True, fill="x", padx=10, pady=5)

        self.unit_fahrenheit = ttk.Radiobutton(unit_frame, text="Fahrenheit", variable=self.current_unit,
                                               value="imperial", command=self.update_unit)
        self.unit_fahrenheit.pack(side="left", expand=True, fill="x", padx=10, pady=5)

        # Location label
        self.location_label = ttk.Label(root, text="", font=("Helvetica", 20), anchor="center")
        self.location_label.grid(row=3, column=0, pady=(10, 5), padx=20)

        # Weather icon
        self.icon_label = ttk.Label(root)
        self.icon_label.grid(row=4, column=0, pady=5)

        # Temperature label
        self.temperature_label = ttk.Label(root, text="", font=("Helvetica", 24), anchor="center")
        self.temperature_label.grid(row=5, column=0, pady=5, padx=20)

        # Description label
        self.description_label = ttk.Label(root, text="", font=("Helvetica", 16), anchor="center")
        self.description_label.grid(row=6, column=0, pady=5, padx=20)

        # Humidity label
        self.humidity_label = ttk.Label(root, text="", font=("Helvetica", 16), anchor="center")
        self.humidity_label.grid(row=7, column=0, pady=5, padx=20)

        # Weather type selection
        self.data_type_var = tk.StringVar(value="current")
        data_type_frame = ttk.LabelFrame(root, text="Weather Type", bootstyle=INFO)
        data_type_frame.grid(row=8, column=0, pady=10, padx=20, sticky="ew")

        data_types = [("Current", "current"), ("Hourly", "hourly"), ("Daily", "daily")]
        for text, mode in data_types:
            button = ttk.Radiobutton(data_type_frame, text=text, variable=self.data_type_var,
                                     value=mode, command=self.search_weather)
            button.pack(side="left", expand=True, fill="x", padx=10, pady=5)

        # Data Treeview for hourly and daily data
        self.data_tree = tk_tt.Treeview(root, columns=("Time/Date", "Temp", "Humidity"), show='headings')
        self.data_tree.heading("Time/Date", text="Time/Date")
        self.data_tree.heading("Temp", text="Temp")
        self.data_tree.heading("Humidity", text="Humidity")
        self.data_tree.grid(row=9, column=0, pady=10, padx=20, sticky="nsew")

        # Configure grid weights for better resizing behavior
        self.root.rowconfigure(9, weight=1)

    def search_weather(self):
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return

        data_type = self.data_type_var.get()
        unit = self.current_unit.get()
        url = f"http://api.openweathermap.org/data/2.5/{'weather' if data_type == 'current' else 'forecast'}?q={city}&appid={self.api_key}&units={unit}"

        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code != 200:
                message = data.get("message", "Error fetching data.")
                messagebox.showerror("Error", message.capitalize())
                return

            # Handle different data types
            if data_type == "current":
                self.process_current_weather(data)
            elif data_type in ["hourly", "daily"]:
                self.process_forecast_data(data, data_type)

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def process_current_weather(self, data):
        self.current_city = data.get("name")
        self.current_country = data.get("sys", {}).get("country")
        self.current_temperature = data.get("main", {}).get("temp")
        self.current_humidity = data.get("main", {}).get("humidity")
        self.current_description = data.get("weather", [{}])[0].get("description", "").capitalize()
        icon_id = data.get("weather", [{}])[0].get("icon")
        self.current_icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png" if icon_id else None

        self.update_ui()

    def process_forecast_data(self, data, data_type):
        self.data_tree.delete(*self.data_tree.get_children())  # Clear previous data
        forecast_list = data.get("list", [])
        unit_symbol = "°C" if self.current_unit.get() == "metric" else "°F"

        if data_type == "hourly":
            for hour in forecast_list[:8]:  # Limit to next 8 entries (3-hour intervals)
                time = hour["dt_txt"]
                temp = f"{hour['main']['temp']:.1f}{unit_symbol}"
                humidity = f"{hour['main']['humidity']}%"
                self.data_tree.insert("", "end", values=(time, temp, humidity))

        elif data_type == "daily":
            for day in forecast_list[::8]:  # Limit to daily data (24-hour intervals)
                date = day["dt_txt"].split(" ")[0]
                temp = f"{day['main']['temp']:.1f}{unit_symbol}"
                humidity = f"{day['main']['humidity']}%"
                self.data_tree.insert("", "end", values=(date, temp, humidity))

    def update_unit(self):
        if self.current_city:
            self.search_weather()

    def update_ui(self):
        # Update location
        self.location_label.config(text=f"{self.current_city}, {self.current_country}")

        # Update icon
        if self.current_icon_url:
            try:
                image_data = requests.get(self.current_icon_url, stream=True).raw
                image = Image.open(image_data)
                photo = ImageTk.PhotoImage(image)
                self.icon_label.config(image=photo)
                self.icon_label.image = photo  # Keep a reference
            except Exception:
                self.icon_label.config(image='', text="No Image Available")
        else:
            self.icon_label.config(image='', text="No Image Available")

        # Update temperature and humidity
        unit_symbol = "°C" if self.current_unit.get() == "metric" else "°F"
        self.temperature_label.config(text=f"{self.current_temperature:.1f}{unit_symbol}")
        self.humidity_label.config(text=f"Humidity: {self.current_humidity}%")

        # Update description
        self.description_label.config(text=self.current_description)


# Initialize and run the application
if __name__ == "__main__":
    root = ttk.Window(themename="morph")
    app = WeatherApp(root)
    root.mainloop()

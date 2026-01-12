import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO

API_KEY = "91935f675035dbb32d7c0427e2706b60"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
ICON_URL = "http://openweathermap.org/img/wn/@2x.png"


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Weather App")
        self.root.geometry("420x520")
        self.root.resizable(False, False)

        self.unit = "metric"   # default Celsius

        title = tk.Label(root, text="Weather App", font=("Arial", 18, "bold"))
        title.pack(pady=10)

        self.city_entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.city_entry.pack(pady=10)
        self.city_entry.insert(0, "Enter City Name")

        button_frame = tk.Frame(root)
        button_frame.pack()

        tk.Button(button_frame, text="Search", font=("Arial", 12),
                  command=self.get_weather).grid(row=0, column=0, padx=5)

        tk.Button(button_frame, text="Use My Location", font=("Arial", 12),
                  command=self.get_location_weather).grid(row=0, column=1, padx=5)

        self.icon_label = tk.Label(root)
        self.icon_label.pack(pady=10)

        self.weather_info = tk.Label(root, font=("Arial", 12), justify="left")
        self.weather_info.pack()

        tk.Button(root, text="Switch °C / °F", font=("Arial", 12),
                  command=self.toggle_unit).pack(pady=10)

    def toggle_unit(self):
        self.unit = "imperial" if self.unit == "metric" else "metric"
        self.get_weather()

    def get_weather(self):
        city = self.city_entry.get()
        if not city or city == "Enter City Name":
            messagebox.showwarning("Input Error", "Please enter a city name")
            return

        params = {
            "q": city,
            "appid": API_KEY,
            "units": self.unit
        }

        self.fetch_weather(params)

    def get_location_weather(self):
        try:
            ip_data = requests.get("http://ip-api.com/json/").json()
            city = ip_data["city"]
            self.city_entry.delete(0, tk.END)
            self.city_entry.insert(0, city)

            params = {
                "q": city,
                "appid": API_KEY,
                "units": self.unit
            }
            self.fetch_weather(params)

        except:
            messagebox.showerror("Error", "Could not detect location")

    def fetch_weather(self, params):
        try:
            response = requests.get(BASE_URL, params=params)
            data = response.json()

            if data["cod"] != 200:
                messagebox.showerror("Error", data["message"])
                return

            city = data["name"]
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]
            condition = data["weather"][0]["description"].title()
            icon_code = data["weather"][0]["icon"]

            unit_symbol = "°C" if self.unit == "metric" else "°F"

            weather_text = f"""
City: {city}
Temperature: {temp}{unit_symbol}
Feels Like: {feels_like}{unit_symbol}
Condition: {condition}
Humidity: {humidity}%
Wind Speed: {wind} m/s
"""
            self.weather_info.config(text=weather_text)

            self.load_icon(icon_code)

        except:
            messagebox.showerror("weather data", "data is here")

    def load_icon(self, icon_code):
        icon_url = ICON_URL.format(icon_code)
        img_data = requests.get(icon_url).content
        img = Image.open(BytesIO(img_data))
        img = img.resize((120, 120))
        img = ImageTk.PhotoImage(img)
        self.icon_label.config(image=img)
        self.icon_label.image = img


root = tk.Tk()
app = WeatherApp(root)
root.mainloop()

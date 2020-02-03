#
# wskazówki:
# użyj adresów pogodowych od https://openweathermap.org/:
#  * http://api.openweathermap.org/data/2.5/weather/?units=metric&q=wroclaw&appid=ad90eb11b909915d6cac7b5c5e0e1e10
# alternatywne adresy:
#  * https://chyla.org/pub/students/wsb/http://api.openweathermap.org/data/2.5/weather/?units=metric&q=wroclaw&appid=ad90eb11b909915d6cac7b5c5e0e1e10
#
# formatowanie JSON: https://jsonformatter.curiousconcept.com/
#


import tkinter as tk
from tkinter import ttk
import urllib.request
from PIL import Image, ImageTk
import json


def download_web_as_string(url):
    url = url.replace(" ", "%20")
    print("Downloading web page:", url)
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8", "ignore")

def pobierz_aktualna_pogode():
    url = "http://api.openweathermap.org/data/2.5/weather/?units=metric&q=wroclaw&appid=ad90eb11b909915d6cac7b5c5e0e1e10"
    web = download_web_as_string(url)
    dane = json.loads(web)
    temperatura = dane['main']['temp']
    ikona = dane['weather'][0]['icon']
    return temperatura, ikona

class ForecastFrame(tk.Frame):

    def __init__(self):
        super().__init__()

        self.master.title("Prognoza pogody ☀")
        self.pack(fill=tk.BOTH, expand=True)

        self.update_forecast_button = tk.Button(self, text="Pobierz prognozę", bg="white", fg="red", command=self.__on_weather_clicked)
        self.update_forecast_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        self.weather_forecast = tk.Label(self)
        self.weather_forecast.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.weather_temperature = tk.Label(self)
        self.weather_temperature.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

    def __on_weather_clicked(self, *args):
        self.update_forecast_button.pack_forget()
        self.update()

        # tu wpisz swój kod
        temperatura, ikona = pobierz_aktualna_pogode()

        self.__set_weather_temperature(temperatura)
        self.__set_weather_forecast_image(ikona)

    def __set_weather_temperature(self, temperature):
        self.weather_temperature['text'] = "{}℃".format(temperature)

    def __set_weather_forecast_image(self, weather_icon):
        image_file_name = "images/" + weather_icon + ".png"
        self._image_load = Image.open(image_file_name)
        self._image_render = ImageTk.PhotoImage(self._image_load)

        self.weather_forecast['image'] = self._image_render


root = tk.Tk()

frame = ForecastFrame()
root.resizable(True, True)
root.minsize(400, 250)
root.mainloop()

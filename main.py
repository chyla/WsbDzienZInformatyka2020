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
from tkinter import ttk, messagebox
import urllib.request
from PIL import Image, ImageTk
import json


def pobierz_jako_tekst(url):
    url = url.replace(" ", "%20")
    print("Pobieram url: ", url)
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8", "ignore")


class Okno(tk.Frame):

    def __init__(self):
        super().__init__()

        self.master.title("Prognoza pogody ☀")
        self.pack(fill=tk.BOTH, expand=True)

        self.przycisk = tk.Button(self, text="Pobierz prognozę", bg="white", fg="red", command=self.__obsluz_nacisniecie_przycisku)
        self.przycisk.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        self.prognoza_obrazek = tk.Label(self)
        self.prognoza_obrazek.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.prognoza_temperatura = tk.Label(self)
        self.prognoza_temperatura.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

    def __obsluz_nacisniecie_przycisku(self, *args):
        self.przycisk.pack_forget()
        self.update()

        # tu wpisz swój kod

    def __wyswietl_temperature(self, temperature):
        self.prognoza_temperatura['text'] = "{}℃".format(temperature)

    def __wyswietl_obrazek_prognozy(self, weather_icon):
        image_file_name = "images/" + weather_icon + ".png"
        self._image_load = Image.open(image_file_name)
        self._image_render = ImageTk.PhotoImage(self._image_load)

        self.prognoza_obrazek['image'] = self._image_render


root = tk.Tk()

okno = Okno()
root.resizable(True, True)
root.minsize(400, 250)
root.mainloop()

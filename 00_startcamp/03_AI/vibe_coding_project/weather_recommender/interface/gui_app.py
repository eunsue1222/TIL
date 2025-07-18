import tkinter as tk
from tkinter import messagebox
from recommender.clothes_recommender import ClothesRecommender
import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/clothes_rules.csv')

class WeatherApp:
    def __init__(self, master):
        self.master = master
        master.title("날씨 기반 옷차림 추천")
        self.recommender = ClothesRecommender(DATA_PATH)

        self.label = tk.Label(master, text="기온(℃) 입력:")
        self.label.pack()
        self.temp_entry = tk.Entry(master)
        self.temp_entry.pack()

        self.rain_var = tk.IntVar()
        self.rain_check = tk.Checkbutton(master, text="비/눈이 오나요?", variable=self.rain_var)
        self.rain_check.pack()

        self.button = tk.Button(master, text="추천 받기", command=self.recommend)
        self.button.pack()

        self.result = tk.Label(master, text="")
        self.result.pack()

    def recommend(self):
        try:
            temp = float(self.temp_entry.get())
            rain = bool(self.rain_var.get())
            weather_data = {'main': {'temp': temp}, 'rain': {} if rain else None}
            rec = self.recommender.recommend(weather_data)
            result_text = f"상의: {rec['상의']}\n하의: {rec['하의']}\n아우터: {rec['아우터']}\n액세서리: {rec['액세서리']}"
            self.result.config(text=result_text)
        except Exception as e:
            messagebox.showerror("오류", str(e))

def run_gui():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()

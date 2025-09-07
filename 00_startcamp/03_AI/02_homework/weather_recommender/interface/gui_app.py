
import tkinter as tk
from tkinter import messagebox
from recommender.clothes_recommender import ClothesRecommender
import json
import os
import requests
from bs4 import BeautifulSoup

DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/clothes_rules.csv')

class WeatherApp:
    def __init__(self, master):
        self.master = master
        master.title("날씨 기반 옷차림 추천")
        self.recommender = ClothesRecommender(DATA_PATH)

        # 도시명 입력
        self.city_label = tk.Label(master, text="도시명(예: 서울) 입력:")
        self.city_label.pack()
        self.city_entry = tk.Entry(master)
        self.city_entry.pack()

        self.fetch_btn = tk.Button(master, text="네이버에서 날씨 불러오기", command=self.fetch_weather)
        self.fetch_btn.pack()

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

    def fetch_weather(self):
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showerror("입력 오류", "도시명을 입력하세요.")
            return
        try:
            # 네이버 날씨 검색 결과 크롤링
            url = f"https://search.naver.com/search.naver?query={city}+날씨"
            headers = {'User-Agent': 'Mozilla/5.0'}
            resp = requests.get(url, headers=headers, timeout=5)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, 'html.parser')
            # 기온
            temp_tag = soup.select_one('.temperature_text strong')
            if not temp_tag:
                temp_tag = soup.select_one('.temperature')
            temp = None
            if temp_tag:
                temp_str = temp_tag.get_text().replace('°', '').replace('현재 온도', '').strip()
                try:
                    temp = float(temp_str)
                except Exception:
                    temp = None
            # 강수(비/눈)
            rain = False
            weather_tag = soup.select_one('.weather')
            if weather_tag and ('비' in weather_tag.text or '눈' in weather_tag.text):
                rain = True
            # 일부 네이버 구조 대응
            desc_tag = soup.select_one('.weather before_slash')
            if desc_tag and ('비' in desc_tag.text or '눈' in desc_tag.text):
                rain = True
            if temp is not None:
                self.temp_entry.delete(0, tk.END)
                self.temp_entry.insert(0, str(temp))
            self.rain_var.set(1 if rain else 0)
            if temp is None:
                messagebox.showwarning("알림", "기온 정보를 찾을 수 없습니다. 네이버 날씨 페이지 구조가 변경되었을 수 있습니다.")
        except Exception as e:
            messagebox.showerror("크롤링 오류", f"날씨 정보를 불러오지 못했습니다: {e}")

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

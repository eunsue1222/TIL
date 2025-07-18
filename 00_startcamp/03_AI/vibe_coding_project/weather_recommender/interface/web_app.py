from fastapi import FastAPI, Query
from pydantic import BaseModel
from recommender.clothes_recommender import ClothesRecommender
import os

app = FastAPI(title="Weather Clothes Recommender API")
DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/clothes_rules.csv')
recommender = ClothesRecommender(DATA_PATH)

class WeatherInput(BaseModel):
    temp: float
    rain: bool = False

@app.post("/recommend")
def recommend_clothes(input: WeatherInput):
    weather_data = {'main': {'temp': input.temp}, 'rain': {} if input.rain else None}
    rec = recommender.recommend(weather_data)
    return {"상의": rec['상의'], "하의": rec['하의'], "아우터": rec['아우터'], "액세서리": rec['액세서리']}

@app.get("/")
def root():
    return {"message": "Weather Clothes Recommender API. POST /recommend with temp, rain."}

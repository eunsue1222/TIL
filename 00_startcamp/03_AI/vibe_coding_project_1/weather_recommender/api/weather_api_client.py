import os
import requests
from .exceptions import WeatherAPIError

class WeatherAPIClient:
    """
    외부 날씨 API(OpenWeatherMap 등)와 통신하는 클라이언트
    """
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("OPENWEATHER_API_KEY")
        if not self.api_key:
            raise WeatherAPIError("API 키가 설정되어 있지 않습니다.")

    def get_current_weather(self, location):
        """
        location: 도시명(str) 또는 (위도, 경도) 튜플
        return: dict (날씨 정보)
        """
        params = {
            "appid": self.api_key,
            "units": "metric",
        }
        if isinstance(location, str):
            params["q"] = location
        elif isinstance(location, (tuple, list)) and len(location) == 2:
            params["lat"], params["lon"] = location
        else:
            raise ValueError("location은 도시명(str) 또는 (위도, 경도) 튜플이어야 합니다.")

        try:
            resp = requests.get(self.BASE_URL, params=params, timeout=5)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            raise WeatherAPIError(f"날씨 API 요청 실패: {e}")

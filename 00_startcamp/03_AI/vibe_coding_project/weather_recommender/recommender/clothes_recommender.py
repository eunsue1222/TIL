from .utils import load_clothes_rules

class ClothesRecommender:
    """
    날씨 데이터와 의상 룰을 바탕으로 추천을 수행하는 엔진
    """
    def __init__(self, rules_path):
        self.rules = load_clothes_rules(rules_path)

    def recommend(self, weather_data):
        temp = weather_data['main']['temp']
        rain = bool(weather_data.get('rain'))
        # 룰 중 조건에 맞는 첫 번째 추천 반환
        for rule in self.rules:
            if rule['min_temp'] <= temp <= rule['max_temp']:
                if rule['rain'] == 'any' or rule['rain'] == rain:
                    return {
                        '상의': rule['top'],
                        '하의': rule['bottom'],
                        '아우터': rule['outer'],
                        '액세서리': rule['accessory']
                    }
        return {'상의': '추천 없음', '하의': '추천 없음', '아우터': '추천 없음', '액세서리': '추천 없음'}

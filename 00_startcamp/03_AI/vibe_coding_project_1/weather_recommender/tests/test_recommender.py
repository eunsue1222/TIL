
import os
import json
import unittest
from typing import Dict, Any
from recommender.clothes_recommender import ClothesRecommender

DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/clothes_rules.csv')
SAMPLE_WEATHER_PATH = os.path.join(os.path.dirname(__file__), '../data/sample_weather.json')

class TestClothesRecommender(unittest.TestCase):
    """
    ClothesRecommender 엔진의 동작을 검증하는 단위 테스트
    """
    def setUp(self) -> None:
        self.recommender = ClothesRecommender(DATA_PATH)
        with open(SAMPLE_WEATHER_PATH, encoding='utf-8') as f:
            self.weather_data: Dict[str, Any] = json.load(f)

    def test_recommend(self) -> None:
        """예시 날씨 데이터에 대해 추천 결과가 올바른지 검증"""
        rec = self.recommender.recommend(self.weather_data)
        self.assertIn('상의', rec, "추천 결과에 '상의' 키가 없습니다.")
        self.assertIn('하의', rec, "추천 결과에 '하의' 키가 없습니다.")
        self.assertIn('아우터', rec, "추천 결과에 '아우터' 키가 없습니다.")
        self.assertIn('액세서리', rec, "추천 결과에 '액세서리' 키가 없습니다.")
        self.assertNotEqual(rec['상의'], '추천 없음', "추천 결과가 비어 있습니다.")

if __name__ == "__main__":
    unittest.main()

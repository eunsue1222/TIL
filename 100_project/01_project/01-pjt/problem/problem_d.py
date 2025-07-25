import requests
import csv

# TMDB API 키 설정
API_KEY = '41ad3f4a63c674f10f1b1a9ada311144'
BASE_URL = 'https://api.themoviedb.org/3'

# 문제 a에서 생성된 movies.csv 파일을 기반으로 영화 ID 목록 가져오기
# API 호출 함수
# 배우 데이터 처리 함수
cast_data = []
with open('movies.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        movie_id = row['id']
        url = f'{BASE_URL}/movie/{movie_id}/credits?api_key={API_KEY}&language=en-US&page=1'
        response = requests.get(url).json()
        
        cast_list = response.get('cast', [])
        for cast in cast_list:
            if cast.get('order') <= 10:
                name = cast.get('name', '').replace('\n', ' ').replace('\r', ' ').strip()
                character = cast.get('character', '').replace('\n', ' ').replace('\r', ' ').strip()
                
                cast_data.append({
                    'cast_id': cast.get('cast_id'),
                    'movie_id': movie_id,
                    'name': cast.get('name'),
                    'character': cast.get('character'),
                    'order': cast.get('order')
                })

# 데이터 수집 및 CSV 파일로 저장
with open('movie_cast.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['cast_id', 'movie_id', 'name', 'character', 'order']
    writer = csv.DictWriter(file, fieldnames=['cast_id', 'movie_id', 'name', 'character', 'order'])
    writer.writeheader()
    writer.writerows(cast_data)
import requests
import csv

# TMDB API 키 설정
API_KEY = '41ad3f4a63c674f10f1b1a9ada311144'
BASE_URL = 'https://api.themoviedb.org/3'

# CSV 파일에서 영화 ID 읽기
# # API 호출 함수
# 영화 데이터 처리 함수
movies = []
with open('movies.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        movie_id = row['id']
        url = f'{BASE_URL}/movie/{movie_id}?api_key={API_KEY}&language=en-US&page=1'
        response = requests.get(url).json()
        
        genres = ', '.join([r['name'] for r in response.get('genres')])
        movies.append({
            'movie_id': response.get('id'),
            'budget': response.get('budget'),
            'revenue': response.get('revenue'),
            'runtime': response.get('runtime'),
            'genres': genres
        })

# 데이터 수집 및 CSV 파일로 저장
with open('movie_details.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['movie_id', 'budget', 'revenue', 'runtime', 'genres'])
    writer.writeheader()
    writer.writerows(movies)
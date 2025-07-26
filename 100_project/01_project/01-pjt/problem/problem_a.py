import requests 
import csv

# TMDB API 키 설정
API_KEY = '41ad3f4a63c674f10f1b1a9ada311144'
BASE_URL = 'https://api.themoviedb.org/3'

# API 호출 함수
url = f'{BASE_URL}/movie/popular?api_key={API_KEY}&language=en-US&page=1'
response = requests.get(url).json()

# 영화 데이터 처리 함수
movies = []
for movie in response['results']:
    movies.append({
        'id': movie['id'],
        'title': movie['title'],
        'release_date': movie['release_date'],
        'popularity': movie['popularity']
})

# 데이터 수집 및 CSV 파일로 저장
with open('movies.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['id', 'title', 'release_date', 'popularity'])
    writer.writeheader()
    writer.writerows(movies)
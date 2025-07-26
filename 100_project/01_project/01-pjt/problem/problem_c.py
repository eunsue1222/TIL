import requests
import csv

# TMDB API 키 설정
API_KEY = '7394faef83b673f55d39ca81be6ecd61'
BASE_URL = 'https://api.themoviedb.org/3/movie/{movie_id}/reviews'

# 영화 ID 리스트를 movies.csv 파일에서 읽어옴
movie_ids = []

with open('movies.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movie_ids.append(row['id'])
        
# API 호출 함수
def get_reviews(movie_id):
    url= f"https://api.themoviedb.org/3/movie/{movie_id}/reviews"
    params = {
        'api_key': API_KEY,
        'language': 'en'
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json().get('results', [])
    else: 
        return []

# 리뷰 데이터 처리 함수
def process_review(movie_id, reviews):
    result = []
    for review in reviews:
        content = review.get('content') or '내용 없음'
        rating = review.get('author_details', {}).get('rating', 0)
        if rating is not None and rating >= 5:
            result.append({
                'review_id': review['id'],
                'movie_id': movie_id,
                'author': review['author'],
                'content': content,
                'rating': rating
            })
    return result
    
# 데이터 수집 및 CSV 파일로 저장
all_reviews = []

for movie_id in movie_ids:
    reviews = get_reviews(movie_id)
    filtered = process_review(movie_id, reviews)
    all_reviews.extend(filtered)

with open('movie_reviews.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['review_id', 'movie_id', 'author', 'content', 'rating', ])
    writer.writeheader()
    writer.writerows(all_reviews)
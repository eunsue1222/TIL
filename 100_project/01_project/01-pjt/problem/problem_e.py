import csv
import requests
from collections import defaultdict

# TMDB API 키
API_KEY = '7394faef83b673f55d39ca81be6ecd61'

# 1. 영화 ID 리스트 불러오기
movie_ids = []
with open('movies.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movie_ids.append(row['id'])

# 2. 리뷰 파일에서 평점 분포 계산
rating_distributions = defaultdict(lambda: {str(i): 0 for i in range(1, 11)})

with open('movie_reviews.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movie_id = row['movie_id']
        try:
            rating = int(float(row['rating']))
            if 1 <= rating <= 10:
                rating_distributions[movie_id][str(rating)] += 1
        except:
            continue  # 유효하지 않은 평점 무시

# 3. TMDB API로부터 평균 평점과 투표 수 가져오기
movie_ratings = []

for movie_id in movie_ids:
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        'api_key': API_KEY,
        'language': 'en-US'
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        average_rating = data.get('vote_average', 0)
        vote_count = data.get('vote_count', 0)
    else:
        average_rating = 0
        vote_count = 0

    # 평점 분포 문자열 생성 (예: "1:0,2:1,3:5,...,10:2")
    distribution_dict = rating_distributions.get(movie_id, {str(i): 0 for i in range(1, 11)})
    distribution_str = ','.join([f"{k}:{v}" for k, v in distribution_dict.items()])

    movie_ratings.append({
        'movie_id': movie_id,
        'average_rating': average_rating,
        'vote_count': vote_count,
        'rating_distribution': distribution_str
    })

# 4. 결과 CSV로 저장
with open('movie_ratings.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['movie_id', 'average_rating', 'vote_count', 'rating_distribution']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(movie_ratings)
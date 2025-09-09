-- 1. 개봉 연도가 2000년부터 2010년 사이인 영화 목록을 조회하시오.
SELECT * FROM movie_list
WHERE release_year BETWEEN 2000 AND 2010;

-- 2. 영화 제목이 'A'부터 'M' 사이의 문자로 시작하는 영화 목록을 조회하시오.
SELECT * FROM movie_list
WHERE title BETWEEN 'A%' AND 'M%';

-- 3. 장르가 'Drama'이고 개봉 연도가 1990년부터 2000년 사이인 영화 목록을 조회하시오.
SELECT * FROM movie_list
WHERE genre = 'Drama' AND release_year BETWEEN 1990 AND 2000;

-- 4. 개봉 연도가 2015년부터 2020년 사이인 영화 중 Sci-Fi 또는 Action 장르의 영화 목록을 조회하시오.
SELECT * FROM movie_list
WHERE release_year BETWEEN 2015 AND 2020
AND genre IN ('Sci-Fi', 'Action');

-- 5. 개봉 연도가 2005년 이후이지만 2015년 이전인 영화를 조회하시오.
SELECT * FROM movie_list
WHERE release_year BETWEEN 2006 AND 2014;
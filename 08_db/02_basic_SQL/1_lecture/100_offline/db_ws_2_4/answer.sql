SELECT * FROM movie_list;

INSERT INTO movie_list VALUES (DEFAULT, 'SOME_MOVIE', 'Drama', '1994')

-- 1. 'Drama' 장르의 영화 중 개봉 연도가 가장 빠른 영화의 제목을 조회하시오.
SELECT title, release_year
FROM movie_list
WHERE genre = 'Drama' AND release_year IS NOT NULL
ORDER BY release_year
LIMIT 2;

-- 개봉년도가 최솟값이 몇인지 보고 싶어. 장르가 드라마인...
SELECT MIN(release_year) FROM movie_list WHERE genre = 'Drama'
-- 1994

SELECT title, release_year
FROM movie_list
WHERE genre = 'Drama'
  AND release_year = (
    SELECT MIN(release_year) FROM movie_list WHERE genre = 'Drama'
  );


-- 2. 2000년 이후에 개봉된 영화들 중 개봉 연도가 가장 늦은 
-- 'Action' 장르 영화의 제목과 개봉년도를 조회하시오.
SELECT title, release_year
FROM movie_list
WHERE genre = 'Action' AND release_year > 2000
ORDER BY release_year DESC
LIMIT 1;

SELECT title, release_year
FROM movie_list
WHERE genre = 'Action' 
AND release_year = (
  SELECT MAX(release_year) 
  FROM movie_list 
  WHERE genre = 'Action'
    AND release_year > 2000
);

-- 3. 'Drama' 장르의 영화와 개봉 연도가 같은 
-- 'Sci-Fi' 또는 'Action' 장르의 영화 목록을 조회하시오.
SELECT release_year
FROM movie_list
WHERE genre = 'Drama';

SELECT * 
FROM movie_list
WHERE release_year IN (NULL, 1994, 1999)
  AND genre IN ('Sci-Fi', 'Action');



SELECT * 
FROM movie_list
WHERE release_year IN (
  SELECT release_year
  FROM movie_list
  WHERE genre = 'Drama'
)
  AND genre IN ('Sci-Fi', 'Action');

SELECT m2.*
FROM movie_list m1
JOIN movie_list m2
  ON m1.release_year = m2.release_year
WHERE m1.genre = 'Drama'
  AND m2.genre IN ('Sci-Fi', 'Action');



-- 4. 모든 'Action' 장르의 영화 개봉 연도의 평균보다 
-- 더 늦게 개봉한 'Sci-Fi' 장르의 영화 목록을 조회하시오.

SELECT *
FROM movie_list
WHERE genre = 'Sci-Fi'
  AND release_year > (
    SELECT AVG(release_year) FROM movie_list WHERE genre = 'Action'
  );


-- 5. 개봉 연도가 'Action' 장르 영화의 최소 개봉 연도와 
-- 같은 다른 장르의 영화를 조회하시오.
SELECT *
FROM movie_list
WHERE release_year = (
  SELECT MIN(release_year)
  FROM movie_list
  WHERE genre = 'Action'
) AND genre <> 'Action';

-- 가장 많은 영화를 보유한 장르를 조회하시오.
SELECT genre, COUNT(*)
FROM movie_list
GROUP BY genre;

SELECT genre, movie_count, max_count
FROM (
  SELECT 
    genre, 
    COUNT(*) AS movie_count,
    MAX(COUNT(*)) OVER () as max_count
  FROM movie_list
  GROUP BY genre
) as movie_count_table
WHERE movie_count = max_count;



-- 장르별 영화의 개수와 평균 개봉 연도를 조회하시오.
SELECT 
  genre, 
  COUNT(*) AS movie_count,
  AVG(release_year) AS avg_release_year
FROM movie_list
GROUP BY genre;


-- 장르별로 가장 최근에 개봉한 영화의 
-- 제목과 개봉 연도를 조회하시오.
-- 장르, 개봉년도 -> 가장 최근에 개봉한 것들만 뽑아서 추출
SELECT m1.genre, m1.title, m1.release_year
FROM movie_list m1
LEFT JOIN movie_list m2
  ON m1.genre = m2.genre 
     AND IFNULL(m1.release_year, 0) < IFNULL(m2.release_year, 0)
WHERE m2.id IS NULL;


SELECT 
  genre, title, release_year
FROM
  movie_list main
WHERE
  main.release_year = (
    SELECT
      MAX(release_year)
    FROM
      movie_list sub
    WHERE
      main.genre = sub.genre
  )
;



-- 개봉 연도가 
-- 'Action' 장르 영화의 최소 개봉 연도와 
-- 같은 다른 장르의 영화를 개봉 연도와 제목으로 정렬하여 조회하시오.
SELECT DISTINCT m2.id, m2.release_year, m2.title, m2.genre
FROM movie_list m1
LEFT JOIN movie_list m1b 
  ON m1.genre = 'Action' 
     AND m1b.genre = 'Action' 
     AND m1.release_year > m1b.release_year
JOIN movie_list m2 
  ON m1.release_year = m2.release_year
WHERE m1.genre = 'Action'
  AND m1b.id IS NULL
  AND m2.genre <> 'Action'
ORDER BY m2.release_year, m2.title;


SELECT id, release_year, title, genre
FROM movie_list
WHERE genre <> 'Action'
  AND release_year = (
      SELECT MIN(release_year)
      FROM movie_list
      WHERE genre = 'Action'
  )
ORDER BY release_year, title;



-- 모든 'Drama' 장르의 영화와 같은 개봉 연도를 가진 
-- 'Sci-Fi' 또는 'Action' 장르의 영화를 개봉 연도 순으로 정렬하여 조회하시오.
SELECT DISTINCT m2.id, m2.release_year, m2.title, m2.genre
FROM movie_list m1
JOIN movie_list m2 
  ON m1.release_year = m2.release_year
WHERE m1.genre = 'Drama'
  AND m2.genre IN ('Sci-Fi', 'Action')
ORDER BY m2.release_year;

SELECT id, release_year, title, genre
FROM movie_list
WHERE genre IN ('Sci-Fi', 'Action')
  AND release_year IN (
      SELECT release_year
      FROM movie_list
      WHERE genre = 'Drama'
  )
ORDER BY release_year;

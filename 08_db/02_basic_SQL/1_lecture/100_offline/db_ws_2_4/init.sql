DROP DATABASE IF EXISTS movies;

CREATE DATABASE movies;

USE movies;
-- 2. movies 데이터베이스 내에 movie_list라는 이름의 테이블을 생성하되, 다음 필드를 포함하시오:
-- id (INT, PRIMARY KEY, AUTO_INCREMENT)
-- title (VARCHAR(255))
-- genre (VARCHAR(100))
-- release_year (YEAR)
CREATE TABLE movie_list (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    genre VARCHAR(100),
    release_year YEAR
);

-- 3. movie_list 테이블에 다음 데이터를 삽입하시오:
-- (title: 'Inception', genre: 'Sci-Fi', release_year: 2010)
-- (title: 'The Dark Knight', genre: 'Action', release_year: 2008)
-- (title: 'Interstellar', genre: 'Sci-Fi', release_year: 2014)
INSERT INTO movie_list (title, genre, release_year) VALUES
('Inception', 'Sci-Fi', 2010),
('The Dark Knight', 'Action', 2008),
('Interstellar', 'Sci-Fi', 2014),
('Unknown', 'Drama', Null),
('The Shawshank Redemption', 'Drama', 1994),
('Fight Club', 'Drama', 1999),
('Mad Max: Fury Road', 'Action', 2015),
('Star Wars: The Force Awakens', 'Sci-Fi', 2015),
('The Matrix', 'Sci-Fi', 1999),
('Gladiator', 'Action', 2000),
('Jurassic Park', 'Sci-Fi', 1993),
('The Fugitive', 'Action', 1993);
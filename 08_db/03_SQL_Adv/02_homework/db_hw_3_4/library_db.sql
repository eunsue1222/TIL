SELECT 
    b.title,
    a.name AS author_name,
    g.genre_name
FROM books b
INNER JOIN authors a ON b.author_id = a.id
INNER JOIN genres g ON b.genre_id = g.id;

-- 작가 이름 인덱스
CREATE INDEX idx_authors_name ON authors(name);

-- 장르 이름 인덱스
CREATE INDEX idx_genres_genre_name ON genres(genre_name);

SELECT 
    b.title,
    a.name AS author_name,
    g.genre_name
FROM books b
INNER JOIN authors a ON b.author_id = a.id
INNER JOIN genres g ON b.genre_id = g.id
WHERE a.name = 'J.K. Rowling'
  AND g.genre_name = 'Fantasy';

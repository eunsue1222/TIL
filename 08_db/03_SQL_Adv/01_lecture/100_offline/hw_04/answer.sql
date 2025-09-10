-- authors 테이블의 name 컬럼에 인덱스 생성
CREATE INDEX idx_authors_name ON authors(name);

-- genres 테이블의 genre_name 컬럼에 인덱스 생성
CREATE INDEX idx_genres_genre_name ON genres(genre_name);

-- INNER JOIN을 사용하여 책의 제목, 저자 이름, 장르 이름을 모두 포함하는 조회문을 작성하시오.
SELECT
    b.title AS BookTitle,
    a.name AS AuthorName,
    g.genre_name AS GenreName
FROM
    books b
INNER JOIN authors a ON b.author_id = a.id
INNER JOIN genres g ON b.genre_id = g.id;


-- name 및 genre_name 기반 조회
SELECT b.title AS book_title, a.name AS author_name, g.genre_name AS genre_name
FROM books b
INNER JOIN authors a ON b.author_id = a.id
INNER JOIN genres g ON b.genre_id = g.id
WHERE a.name = 'J.K. Rowling' AND g.genre_name = 'Fantasy';

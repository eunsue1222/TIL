-- Active: 1752635264960@@127.0.0.1@3306@sns_db
-- sns_db라는 이름의 데이터베이스를 생성하시오

CREATE DATABASE sns_db
    DEFAULT CHARACTER SET utf8mb4;

-- users 와 posts 라는 이름의 두 개의 테이블을 생성하시오.
USE sns_db;
-- users 테이블의 필드:
-- id (INT, PRIMARY KEY, AUTO_INCREMENT)
-- username (VARCHAR(255))
-- email (VARCHAR(255))
-- created_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255),
    email VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DESCRIBE users;

INSERT INTO users (username, email, crea) VALUES ('alice', 'alice@example.com');

-- created_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)

-- posts 테이블의 필드:
-- id (INT, PRIMARY KEY, AUTO_INCREMENT)
-- user_id (INT, FOREIGN KEY)
-- content (TEXT)
-- created_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)

CREATE TABLE posts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO posts (user_id, content) VALUES (1, 'Hello, world!');
DELETE FROM posts WHERE id = 14;
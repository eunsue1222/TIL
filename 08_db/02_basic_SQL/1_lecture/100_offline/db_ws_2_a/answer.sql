-- 데이터베이스 생성
CREATE DATABASE IF NOT EXISTS restaurant_db;

-- 데이터베이스 사용
USE restaurant_db;

-- restaurants 테이블 생성
CREATE TABLE IF NOT EXISTS restaurants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    cuisine_type VARCHAR(100)
);

-- menus 테이블 생성
CREATE TABLE IF NOT EXISTS menus (
    id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_id INT,
    item_name VARCHAR(255),
    price DECIMAL(10, 2),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
);

-- restaurants 테이블에 데이터 삽입
INSERT INTO restaurants (name, location, cuisine_type) VALUES
('Sushi Place', 'Tokyo', 'Japanese'),
('Pasta Paradise', 'Rome', 'Italian'),
('Curry Corner', 'Mumbai', 'Indian');

-- menus 테이블에 데이터 삽입
INSERT INTO menus (restaurant_id, item_name, price) VALUES
(1, 'Salmon Nigiri', 5.50),
(1, 'Tuna Sashimi', 6.00),
(2, 'Spaghetti Carbonara', 7.50),
(2, 'Margherita Pizza', 8.00),
(3, 'Chicken Curry', 6.50),
(3, 'Vegetable Biryani', 5.00);

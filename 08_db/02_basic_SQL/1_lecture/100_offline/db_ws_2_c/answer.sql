-- 데이터베이스 사용
USE restaurant_db;

-- menus 테이블에서 'Salmon Nigiri' 항목 삭제
DELETE FROM menus WHERE item_name = 'Salmon Nigiri';

-- restaurants 테이블에서 'Pasta Paradise' 레스토랑을 삭제하고 관련된 menus 항목도 삭제
DELETE FROM menus WHERE restaurant_id = (SELECT id FROM restaurants WHERE name = 'Pasta Paradise');
DELETE FROM restaurants WHERE name = 'Pasta Paradise';
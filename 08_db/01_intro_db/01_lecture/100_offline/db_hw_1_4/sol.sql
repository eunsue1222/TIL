-- SNS 관리 시스템의 데이터베이스에 대한 다양한 변경 사항을 적용하려고 한다. 요구 사항을 참고하여 적절한 SQL 문을 작성하시오. 단, DB는 2단계에서 생성한 sns_db를 사용한다
USE sns_db;

-- 요구사항
-- users 테이블에 profile_picture (VARCHAR(255)) 필드를 추가하시오.
ALTER TABLE users ADD profile_picture VARCHAR(255);
-- users 테이블에서 email 필드의 크기를 255에서 320으로 변경하시오.
ALTER TABLE users MODIFY email VARCHAR(320);

-- posts 테이블에 title (VARCHAR(255)) 필드를 추가하시오.
ALTER TABLE posts ADD title VARCHAR(255);

-- posts 테이블에서 content 필드의 자료형을 TEXT에서 LONGTEXT로 변경하시오.
ALTER TABLE posts MODIFY content LONGTEXT;


-- CHAR(255)
-- VARCHAR(0 ~ 65,535문자)
-- LONGTEXT
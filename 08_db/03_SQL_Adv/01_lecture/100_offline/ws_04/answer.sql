-- 1. 병원 데이터베이스 생성
CREATE DATABASE hospital;
USE hospital;

-- 8. 각 환자의 이름, 전화번호, 모든 방문 날짜, 
-- 각 방문별 담당 의사의 이름, 그리고 전문 분야를 조회
-- 방문 정보 -> visits table 
SELECT
  -- 환자 이름을 가져오고 싶다.
  -- 내 vsitis 테이블에서 patient_id == patient.id
  (SELECT first_name FROM patient WHERE patient_id = v.patient_id) AS first_name,
  v.visit_date,
  (SELECT first_name FROM doctor WHERE doctor_id = v.doctor_id) as  doctor_first_name,
  (SELECT specialty FROM doctor WHERE doctor_id = v.doctor_id) as  specialty
FROM
  visits v;

SELECT * FROM visits;
-- INNER JOIN -> 교집합 -> left right table 구분 의미 있다? 없다.
SELECT
  p.first_name, p.last_name, p.phone_number,
  v.visit_date,
  d.first_name, d.last_name, d.specialty
FROM
  patient p
JOIN visits v ON p.patient_id = v.patient_id
JOIN doctor d ON d.doctor_id = v.doctor_id;

-- 목적이, 모든 doctor (방문 정보가 없는 닥터 포함 .환자가 없었던거임) 테이블 기준으로,
-- 환자랑, 닥터의 방문 정보를 포함한 정보를 얻고싶어.


-- 9. 지난 1년 동안(2024년 한 해) 방문한 환자들 중에서 의사별로 방문 횟수를 조회



SELECT 
  first_name, last_name, specialty,
  (
    SELECT
      COUNT(*)
    FROM
      visits v
    WHERE
      v.doctor_id = d.doctor_id 
      AND visit_date BETWEEN '2024-01-01' AND '2024-12-31'
  )
FROM
  doctor d;


SELECT
  d.first_name,
  COUNT(*)
FROM 
  visits v
JOIN doctor d ON d.doctor_id = v.doctor_id
WHERE visit_date BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY d.doctor_id;


-- 10. 특정 의사에게 방문한 환자 목록을 조회하되, 
-- 방문 횟수가 두 번 이상인 환자만 조회



-- SELECT
--   p.first_name,
--   (
--     SELECT
--       COUNT(*)
--     FROM
--       visits v
--     JOIN patient p ON v.patient_id = p.patient_id
--     WHERE v.doctor_id = 2
--   )
-- FROM
--   patient p
-- WHERE
--   (
--     SELECT
--       COUNT(*)
--     FROM
--       visits v
--     JOIN patient p ON v.patient_id = p.patient_id
--     WHERE v.doctor_id = 2
--   ) >= 2;


SELECT
  p.first_name,
  COUNT(*)
FROM
  visits v
JOIN patient p ON p.patient_id = v.patient_id
WHERE v.doctor_id = 1
GROUP BY p.patient_id
  HAVING COUNT(*) >= 2;


-- FROM에 서브 쿼리 써서, 조회 대상 테이블 만들기
-- vs
-- VIEW로 만들어서 쓰기

SELECT  3 = NULL;

-- A == FALSE
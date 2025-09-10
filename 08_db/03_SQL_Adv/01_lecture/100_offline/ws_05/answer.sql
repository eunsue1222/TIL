-- 특정 전문 분야(specialty)를 가진 의사의 목록 조회
SELECT d.first_name, d.last_name, d.specialty
FROM doctor d
JOIN visits ON d.doctor_id = visits.doctor_id
WHERE d.specialty IN ('Neurology', 'Dermatology')
GROUP BY d.specialty, d.doctor_id

-- 1. 각 환자의 이름, 전화번호, 모든 방문 날짜, 각 방문별 담당 의사의 이름, 그리고 전문 분야를 포함하는 View 생성
CREATE VIEW patient_visit_details AS
SELECT p.first_name AS patient_first_name, p.last_name AS patient_last_name, p.phone_number, v.visit_date, 
       d.first_name AS doctor_first_name, d.last_name AS doctor_last_name, d.specialty
FROM patient p
JOIN visits v ON p.patient_id = v.patient_id
JOIN doctor d ON v.doctor_id = d.doctor_id;

-- 2. 특정 의사에게 방문한 환자 목록을 조회하는 View 생성
CREATE VIEW doctor_patient_list AS
SELECT d.first_name AS doctor_first_name, d.last_name AS doctor_last_name, p.first_name AS patient_first_name, p.last_name AS patient_last_name, p.phone_number
FROM doctor d
JOIN visits v ON d.doctor_id = v.doctor_id
JOIN patient p ON v.patient_id = p.patient_id;

-- 3. 생성한 View를 사용하여 각 환자의 이름, 전화번호, 모든 방문 날짜, 각 방문별 담당 의사의 이름, 그리고 전문 분야를 조회
SELECT * FROM patient_visit_details;

-- 4. 생성한 View를 사용하여 특정 의사에게 방문한 환자 목록을 조회 (예: doctor_id = 1인 경우)
SELECT * FROM doctor_patient_list
WHERE doctor_first_name = 'Alice' AND doctor_last_name = 'Brown';
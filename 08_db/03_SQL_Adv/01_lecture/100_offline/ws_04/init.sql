-- 1. 병원 데이터베이스 생성
CREATE DATABASE hospital;
USE hospital;

-- 2. 환자(patient) 테이블 생성
CREATE TABLE patient (
  patient_id INT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  phone_number VARCHAR(15),
  birth_date DATE
);

-- 3. 의사(doctor) 테이블 생성
CREATE TABLE doctor (
  doctor_id INT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  specialty VARCHAR(100)
);

-- 4. 환자 테이블에 데이터 삽입
INSERT INTO patient (patient_id, first_name, last_name, birth_date, phone_number)
VALUES (1, 'John', 'Doe', '1990-01-01', '123-456-7890'),
       (2, 'Jane', 'Smith', '1985-02-02', '098-765-4321'),
       (3, 'Alice', 'White', '1970-03-15', '111-222-3333');

-- 5. 의사 테이블에 데이터 삽입
INSERT INTO doctor (doctor_id, first_name, last_name, specialty)
VALUES (1, 'Alice', 'Brown', 'Cardiology'),
       (2, 'Bob', 'Johnson', 'Neurology'),
       (3, 'Charlie', 'Davis', 'Dermatology');

-- 6. 환자와 의사 간의 진료 기록을 저장하는 visits 테이블 생성
CREATE TABLE visits (
  visit_id INT PRIMARY KEY,
  patient_id INT,
  doctor_id INT,
  visit_date DATE,
  FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
  FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id)
);

-- 7. visits 테이블에 데이터 삽입
INSERT INTO visits (visit_id, patient_id, doctor_id, visit_date)
VALUES (1, 1, 1, '2024-01-01'),
       (2, 2, 2, '2024-02-01'),
       (3, 1, 2, '2024-03-01'),
       (4, 3, 3, '2024-04-01'),
       (5, 1, 2, '2024-05-01'),
       (6, 2, 3, '2024-06-01'),
       (7, 3, 1, '2024-07-01');
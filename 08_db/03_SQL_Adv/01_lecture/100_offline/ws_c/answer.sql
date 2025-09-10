
-- applicants 테이블의 username 열에 인덱스 생성
CREATE INDEX idx_applicants_username ON applicants(username);

-- jobs 테이블의 department 열에 인덱스 생성
CREATE INDEX idx_jobs_department ON jobs(department);

-- applications 테이블의 application_date 열에 인덱스 생성
CREATE INDEX idx_applications_application_date ON applications(application_date);

-- applications 테이블의 status 열에 인덱스 생성
CREATE INDEX idx_applications_status ON applications(status);

-- 특정 지원자가 작성한 모든 지원 내역과 지원한 직무의 위치를 조회 (인덱스 활용)
SELECT a.username, j.title, j.location, app.application_date, app.status
FROM applicants a
INNER JOIN applications app ON a.id = app.applicant_id
INNER JOIN jobs j ON app.job_id = j.id
WHERE a.username = 'john_doe';

-- 각 부서별로 'Pending' 상태의 지원 건수를 조회 (인덱스 활용)
SELECT j.department, COUNT(app.id) AS pending_count
FROM jobs j
INNER JOIN applications app ON j.id = app.job_id
WHERE app.status = 'Pending'
GROUP BY j.department;

-- 특정 일자 이후의 'Reviewed' 상태 지원 내역과 지원자의 이메일, 전화번호, 지원한 직무의 위치를 조회 (복잡한 방식, 인덱스 활용)
SELECT a.username, a.email, a.phone, j.title, j.location, app.application_date, app.status
FROM applicants a
INNER JOIN applications app ON a.id = app.applicant_id
INNER JOIN jobs j ON app.job_id = j.id
WHERE app.status = 'Reviewed'
  AND app.application_date > '2023-08-01';

-- 모든 지원자들의 지원 내역과 해당 직무 정보를 포함하는 뷰 생성
CREATE VIEW applicant_job_applications AS
SELECT 
    a.username,
    j.title AS job_title,
    j.department,
    j.location,
    app.application_date,
    app.status
FROM 
    applicants a
    INNER JOIN applications app ON a.id = app.applicant_id
    INNER JOIN jobs j ON app.job_id = j.id;

-- 특정 지원자가 작성한 모든 지원 내역을 뷰를 통해 조회
SELECT * 
FROM applicant_job_applications 
WHERE username = 'john_doe';


-- 특정 지원자의 모든 지원 내역과 지원한 직무의 위치를 조회하시오.
SELECT a.username, j.title, j.location, app.application_date, app.status
FROM applicants a
INNER JOIN applications app ON a.id = app.applicant_id
INNER JOIN jobs j ON app.job_id = j.id
WHERE a.username = 'john_doe';

-- 모든 'Accepted' 상태의 지원 내역과 해당 지원자의 이메일, 전화번호를 조회하시오.
SELECT a.username, a.email, a.phone, j.title, app.application_date
FROM applicants a
INNER JOIN applications app ON a.id = app.applicant_id
INNER JOIN jobs j ON app.job_id = j.id
WHERE app.status = 'Accepted';

-- 특정 직무에 지원한 지원자 수와 그 직무의 부서명을 조회하시오.
SELECT j.title, j.department, COUNT(app.id) AS applicant_count
FROM jobs j
INNER JOIN applications app ON j.id = app.job_id
WHERE j.title = 'Software Engineer'
GROUP BY j.id;

-- 각 부서별로 'Pending' 상태의 지원 건수를 조회하시오.
SELECT j.department, COUNT(app.id) AS pending_count
FROM jobs j
INNER JOIN applications app ON j.id = app.job_id
WHERE app.status = 'Pending'
GROUP BY j.department;
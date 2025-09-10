-- 특정 학생이 작성한 가장 오래된 피드백의 내용을 검색
SELECT comment
FROM feedback
WHERE (student_id, created_at) = (
  SELECT student_id, MIN(created_at)
  FROM feedback
  WHERE student_id = (SELECT id FROM students WHERE username = 'john_doe')
  GROUP BY student_id
);


-- 특정 학생이 작성한 모든 피드백과 해당 코스의 제목을 포함하는 뷰 생성
CREATE VIEW student_feedback_with_courses AS
SELECT 
    s.username,
    c.title AS course_title,
    f.comment,
    f.created_at
FROM 
    students s
    INNER JOIN feedback f ON s.id = f.student_id
    INNER JOIN courses c ON f.course_id = c.id;

-- 뷰를 사용하여 특정 학생이 작성한 모든 피드백과 해당 코스의 제목 조회
SELECT * 
FROM student_feedback_with_courses 
WHERE username = 'john_doe';

-- 특정 학생이 작성한 코스 피드백과 해당 코스의 제목 검색 (INNER JOIN 활용)
SELECT 
    s.username,
    c.title AS course_title,
    f.comment
FROM 
    students s
    INNER JOIN feedback f ON s.id = f.student_id
    INNER JOIN courses c ON f.course_id = c.id
WHERE 
    s.username = 'john_doe';

-- 특정 학생이 작성한 코스 피드백과 해당 코스의 제목 검색 (LEFT JOIN 활용)
SELECT 
    s.username,
    c.title AS course_title,
    f.comment
FROM 
    students s
    LEFT JOIN feedback f ON s.id = f.student_id
    LEFT JOIN courses c ON f.course_id = c.id
WHERE 
    s.username = 'jane_smith';

-- 특정 학생이 작성한 가장 최근 피드백의 내용을 검색
SELECT comment
FROM feedback
WHERE id = (
  SELECT id
  FROM feedback
  WHERE student_id = (SELECT id FROM students WHERE username = 'mary_jones')
  ORDER BY created_at DESC
  LIMIT 1
);

SELECT
    d.departmentName          AS Department,
    MAX(s.salary)             AS "Top salary",
    SUM(s.salary)             AS "Total salary",
    ROUND(AVG(s.salary), 0)   AS "Average salary"
FROM STAFF s
JOIN DEPARTMENT d
    ON s.departmentId = d.departmentId
GROUP BY d.departmentId, d.departmentName
ORDER BY d.departmentId;
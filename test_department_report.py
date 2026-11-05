import sqlite3
import unittest

REPORT_SQL = """
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
"""


class TestDepartmentReport(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.conn.executescript("""
            CREATE TABLE DEPARTMENT (
                departmentId   TEXT PRIMARY KEY,
                departmentName TEXT
            );
            CREATE TABLE STAFF (
                staffId      TEXT PRIMARY KEY,
                staffName    TEXT,
                salary       INTEGER,
                managerId    TEXT,
                departmentId TEXT
            );
            INSERT INTO DEPARTMENT VALUES ('D01', 'Commercial'), ('D02', 'Tech');
            INSERT INTO STAFF VALUES
                ('S0001', 'Susan', 55000, NULL,    'D01'),
                ('S0002', 'John',  30000, 'S0001', 'D01'),
                ('S0003', 'Mike',  28000, 'S0001', 'D01'),
                ('S0004', 'Andy',  45000, NULL,    'D02'),
                ('S0005', 'Tom',   27000, 'S0004', 'D02');
        """)

    def tearDown(self):
        self.conn.close()

    def test_report_matches_expected_output(self):
        rows = self.conn.execute(REPORT_SQL).fetchall()
        expected = [
            ("Commercial", 55000, 113000, 37667),
            ("Tech", 45000, 72000, 36000),
        ]
        self.assertEqual(rows, expected)

    def test_column_names(self):
        cursor = self.conn.execute(REPORT_SQL)
        columns = [col[0] for col in cursor.description]
        self.assertEqual(
            columns,
            ["Department", "Top salary", "Total salary", "Average salary"],
        )

    def test_department_without_staff_is_not_listed(self):
        # JOIN ปกติจะไม่แสดงแผนกที่ไม่มีพนักงาน
        self.conn.execute("INSERT INTO DEPARTMENT VALUES ('D03', 'HR')")
        rows = self.conn.execute(REPORT_SQL).fetchall()
        self.assertEqual(len(rows), 2)


if __name__ == "__main__":
    unittest.main()
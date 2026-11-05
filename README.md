# homework-test-software-intern
Homework test for Software Engineer Intern
## ไฟล์ในโปรเจกต์
- `solution.py` : ข้อ 1 ฟังก์ชัน `sum_positive` หาผลรวมของตัวเลขที่มากกว่า 0
- `solution.sql` : ข้อ 2 SQL รายงานของแต่ละแผนก (Top / Total / Average salary)
- `test_sum_positive.py` : unit test ข้อ 1
- `test_department_report.py` : unit test ข้อ 2 (ใช้ SQLite in-memory)
- 
## วิธีรัน test
```
python -m unittest discover -v
```

## ผลลัพธ์
- ข้อ 1: `sum_positive([-3,-2,-1,0,1,2,3,4,5,6,7,8,9,-10])` = 45
- ข้อ 2:

| Department | Top salary | Total salary | Average salary |
|---|---|---|---|
| Commercial | 55000 | 113000 | 37667 |
| Tech | 45000 | 72000 | 36000 |

## หมายเหตุ
ทดสอบ SQL ด้วย SQLite ไวยากรณ์ใช้ได้กับ MySQL และ PostgreSQL ด้วย

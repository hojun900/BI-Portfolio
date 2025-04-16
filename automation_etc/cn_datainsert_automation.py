import pyodbc
from datetime import datetime

# DB 연결 설정
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=your_server_name;"
    "DATABASE=your_db_name;"
    "UID=your_username;"
    "PWD=your_password"
)
cursor = conn.cursor()

# 자동 인서트할 데이터 예시 (반복 리스트)
data_list = [
    (1001, '아이템A', 500, datetime(2025, 4, 1)),
    (1002, '아이템B', 800, datetime(2025, 4, 2)),
    (1003, '아이템C', 300, datetime(2025, 4, 3)),
]

# 쿼리 작성
insert_sql = """
INSERT INTO YourTableName (itemNo, itemName, price, insertDate)
VALUES (?, ?, ?, ?)
"""

# 반복 인서트
for row in data_list:
    cursor.execute(insert_sql, row)

conn.commit()
cursor.close()
conn.close()

print("데이터 인서트 완료.")

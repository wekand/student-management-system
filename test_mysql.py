import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="0109",
    database="student_db"
)
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

result = cursor.fetchall()

print(result)
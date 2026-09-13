
from app.database.connection import get_connection
from app.models.student import Student
def insert_student(student):
    conn = get_connection()
    cursor = conn.cursor()
    sql="INSERT INTO students (id, name, score) VALUES (%s, %s, %s)"
    cursor.execute(sql, (student.id, student.name, student.score))
    conn.commit()
    cursor.close()
    conn.close()




def get_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT id, name, score FROM students WHERE id = %s"
    cursor.execute(sql, (student_id,))
    result = cursor.fetchone()

    if result:
        student=Student(result[0],result[1],result[2])
    else:
        student=None
    cursor.close()
    conn.close()
    return student


def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM students WHERE id = %s"
        cursor.execute(sql, (student_id,))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()




def update_student(student_id, name, score):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        sql = """
        UPDATE students
        SET name = %s, score = %s
        WHERE id = %s
        """
        cursor.execute(sql, (name, score, student_id))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()








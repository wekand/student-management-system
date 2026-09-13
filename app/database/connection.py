import pymysql

def get_connection():
    return pymysql.connect(
    host="localhost",
    user="root",
    password="0109",
    database="student_db")
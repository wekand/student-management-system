from pymysql import IntegrityError
from app.repositories.student_repository import insert_student, get_student, delete_student, update_student
class StudentAlreadyExistsError(Exception):
    pass

#查询
def lookup_student(student_id):
    return get_student(student_id)


#删除学生
def remove_student(student_id):
    result = delete_student(student_id)
    if result == 0:
        raise StudentNotFoundError("学生未找到")

#修改学生
class StudentNotFoundError(Exception):
    pass


def modify_student(student_id, name, score):
    result=update_student(student_id, name, score)
    if result==0:
        raise StudentNotFoundError("学生未找到")

#添加学生
def add_student(student):
    try:
        insert_student(student)
    except IntegrityError:
        raise StudentAlreadyExistsError("学生已存在")




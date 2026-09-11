from app.repositories.student_repository import insert_student, get_student, delete_student, update_student
from app.service.operation import execute_with_save

#查询
def lookup_student(id):
    result=get_student(id)
    return result



#删除学生
def remove_student(id):
    result = execute_with_save(lambda:delete_student(id))
    return result



#修改学生
def modify_student(id, name, score):
    result=execute_with_save(lambda:update_student(id, name, score))
    return result

#添加学生
def add_student(student):
    result = execute_with_save(lambda: insert_student(student))
    return result
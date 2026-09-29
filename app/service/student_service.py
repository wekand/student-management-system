from sqlalchemy.exc import IntegrityError

from app.models.student import Student
from app.repositories.student_repository import insert_student, get_student, delete_student, update_student

class StudentNotFoundError(Exception):
    pass

class StudentAlreadyExistsError(Exception):
    pass

#查询
def lookup_student(db,student_id):
    return get_student(db,student_id)


#删除学生
def remove_student(db,student_id):
    try:
        result = delete_student(db,student_id)
        if result is None:
            raise StudentNotFoundError("学生未找到")
        db.commit()
    except Exception:
        db.rollback()
        raise


#修改学生
def modify_student(db,student_id, name, score):
    try:
        result=update_student(db,student_id, name, score)
        if result is None:
            raise StudentNotFoundError("学生未找到")
        db.commit()
    except Exception:
        db.rollback()
        raise



#添加学生
def add_student(db,student):
    try:
        student=Student(student.id,student.name,student.score)
        insert_student(db,student)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise StudentAlreadyExistsError("学生已存在")
    except Exception:
        db.rollback()
        raise






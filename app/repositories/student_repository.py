

from app.models.student import Student
def insert_student(db,student):
    db.add(student)





def get_student(db,student_id):
    student=db.get(Student,student_id)
    return student



def delete_student(db,student_id):
    student=db.get(Student,student_id)
    if student is not None:
        db.delete(student)
    return student




def update_student(db,student_id, name, score):
   student=db.get(Student,student_id)
   if student is not None:
       student.name = name
       student.score = score
   return student









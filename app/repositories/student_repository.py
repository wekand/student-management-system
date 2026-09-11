from app.storage import storage
def insert_student(student):
    for orl_student in storage.students:
        if orl_student.id== student.id:
            return False
    storage.students.append(student)
    return True

def get_student(id):
    for student in storage.students:
        if student.id == id:
            return student
    return None

def delete_student(id):
    for student in storage.students:
        if student.id == id:
            storage.students.remove(student)
            return True
    return False

def update_student(id,name,score):
    for student in storage.students:
        if student.id == id:
            student.score = score
            student.name = name
            return True
    return False


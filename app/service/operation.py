from copy import deepcopy
from app.storage import storage

def save_with_rollback(old_students):

    try:
        storage.save_students(storage.students)
        return True
    except PermissionError:
        storage.students.clear()
        storage.students.extend(old_students)
        raise



def execute_with_save(operation):
    old_students=deepcopy(storage.students)
    result=operation()
    if result:
       return save_with_rollback( old_students)
    else:
        return False
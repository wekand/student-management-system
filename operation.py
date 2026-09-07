from copy import deepcopy
from storage import save_students

def save_with_rollback(students, old_students):

    try:
        save_students(students)
        return 0
    except PermissionError:
        students.clear()
        students.extend(old_students)
        return 2



def execute_with_save(students, operation):
    old_students=deepcopy(students)
    result=operation(students)
    if result:
       return save_with_rollback(students, old_students)
    else:
        return 1
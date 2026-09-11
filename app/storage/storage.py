import json
from student import Student

def student_to_dict(student):
    student={"id":student.id,"name":student.name,"score":student.score}
    return student

def students_to_dict(students):
    result = []
    for student in students:
        result.append(student_to_dict(student))
    return result

def dict_to_student(data):
    # dict → Student
    student = Student(data["id"], data["name"], data["score"])
    return student

def dict_to_students(data):
    result = []
    for student in data:
        result.append(dict_to_student(student))
    return result

def load_students():
    try:
        with open('students.json','r',encoding='utf-8') as f:
            students = json.load(f)
            students = dict_to_students(students)
            return students
    except FileNotFoundError:
        students = [
            Student(101, "张三", 80),
            Student(102, "李四", 90),
            Student(103, "王五", 75)
        ]
        save_students(students)
        return students
    except json.JSONDecodeError:
        print("json文件解析失败")
        return None
# def save_students(students):
#     raise PermissionError("模拟保存失败")

def save_students(students):
    students=students_to_dict(students)
    with open('students.json','w',encoding='utf-8') as f:
        json.dump(students,f,ensure_ascii=False,indent=4)

students = load_students()


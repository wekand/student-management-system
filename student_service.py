from utils import get_integer, get_score
from student import Student
#查询
def lookup_student(students):
    id_look=get_integer("请输入要查询的学号：")
    #设置标志
    flag= False
    for student in students:
        if student.id == id_look:
            print(student.name, student.score)
            flag= True
    if not flag:
        print(f"没有找到学号为{id_look}的学生")



#添加
def insert_student(students):
    id_insert=get_integer("请输入要添加的学号：")
    for student in students:
        if student.id == id_insert:
            print("学号已经存在，不能重复添加")
            return False
    name_insert = input("请输入名字：")
    score_insert =get_score("请输入分数：")
    students.append(Student(id_insert,name_insert, score_insert))
    return True


#删除学生
def delete_student(students):
    id_delete=get_integer("请输入要删除的学号：")

    for student in students:
        if student.id == id_delete:
            students.remove(student)
            return True

    print("没有找到该学生，删除失败")
    return False


#修改学生
def update_student(students):
    id_update=get_integer("请输入要更新的学号：")

    for student in students:
        if student.id == id_update:

            name_update=input("请输入新的姓名：")
            score_update=get_score("请输入新的成绩：")
            student.score=score_update
            student.name=name_update
            return True

    print("没有找到该学生")
    return False

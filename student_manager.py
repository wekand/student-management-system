from storage import load_students, save_students

from student_service import (
    insert_student,
    lookup_student,
    delete_student,
    update_student
)



#显示所有学生
def show_students(students):
    for student in students:
        print(student["id"], student["name"], student["score"])


#显示菜单
def show_menu():
    print('='*50)
    print("学生管理系统")
    print('='*50)
    print("1. 添加学生")
    print("2. 查询学生")
    print("3. 删除学生")
    print("4. 修改学生")
    print("5. 显示所有学生")
    print("6. 退出")

def main():
    students= load_students()
    if students is None:
        return
    while True:
        show_menu()
        num_chose=input("请选择：")
        if num_chose == "1":
            result=insert_student(students)
            if result:
                save_students(students)
        elif num_chose == "2":
            lookup_student(students)
        elif num_chose == "3":
            result=delete_student(students)
            if result:
                save_students(students)
        elif num_chose == "4":
            result=update_student(students)
            if result:
                save_students(students)
        elif num_chose == "5":
            show_students(students)
        elif num_chose == "6":
            break


if __name__ == "__main__":
            main()
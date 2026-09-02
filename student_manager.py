
#学生的数据结构设计(创建 students 列表)
students = [
    {"id": 101, "name": "张三", "score": 80},
    {"id": 102, "name": "李四", "score": 90},
    {"id": 103, "name": "王五", "score": 75}
]

#查询
def lookup_student():
    #类型转换
    id_look=int(input("请输入要查询的学号："))
    #设置标志
    flag= False
    for student in students:
        if student["id"] == id_look:
            print(student["name"], student["score"])
            flag= True
    if not flag:
            print(f"没有找到学号为{id_look}的学生")

#添加
def insert_student():
    id_insert = int(input("请输入学号："))
    flag= False
    for student in students:
        if student["id"] == id_insert:
            print("学号已经存在，不能重复添加")
            flag= True
    if not flag:
        name_insert = input("请输入名字：")
        score_insert = int(input("请输入分数："))
        students.append( {"id": id_insert, "name":name_insert , "score": score_insert})


#删除学生
def delete_student():
    id_delete=int(input("请输入要删除的学号："))
    flag= False
    for student in students:
        if student["id"] == id_delete:
            students.remove(student)
            flag= True
    if not flag:
        print("没有找到该学生，删除失败")

#显示所有学生
def show_students():
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
    print("4. 显示所有学生")
    print("5. 退出")

def main():
    while True:
        show_menu()
        num_chose=input("请选择：")
        if num_chose == "1":
            insert_student()
        elif num_chose == "2":
            lookup_student()
        elif num_chose == "3":
            delete_student()
        elif num_chose == "4":
            show_students()
        elif num_chose == "5":
            break



if __name__ == "__main__":
            main()
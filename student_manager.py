
#学生的数据结构设计(创建 students 列表)
students = [
    {"id": 101, "name": "张三", "score": 80},
    {"id": 102, "name": "李四", "score": 90},
    {"id": 103, "name": "王五", "score": 75}
]

#查询
def lookup_student():
    id_look=get_integer("请输入要查询的学号：")
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
    id_insert=get_integer("请输入要添加的学号：")
    flag= False
    for student in students:
        if student["id"] == id_insert:
            print("学号已经存在，不能重复添加")
            flag= True
    if not flag:
        name_insert = input("请输入名字：")
        score_insert =get_score("请输入分数：")
        students.append( {"id": id_insert, "name":name_insert , "score": score_insert})



#删除学生
def delete_student():
    id_delete=get_integer("请输入要删除的学号：")
    flag= False
    for student in students:
        if student["id"] == id_delete:
            students.remove(student)
            flag= True
    if not flag:
        print("没有找到该学生，删除失败")


#修改学生
def update_student():
    id_update=get_integer("请输入要更新的学号：")
    flag= False
    for student in students:
        if student["id"] == id_update:
            flag= True
            name_update=input("请输入新的姓名：")
            score_update=get_score("请输入新的成绩：")
            student['score']=score_update
            student['name']=name_update
    if not flag:
        print("没有找到该学生")

def get_score(message):
    while True:
        score=get_integer(message)
        if 0<=score<=100:
            return score
        else:
            print("成绩必须在0~100之间")


#显示所有学生
def show_students():
    for student in students:
        print(student["id"], student["name"], student["score"])

def get_integer(message):
    while True:
        try:
            integer= int(input(message))
        except ValueError:
            print("请输入数字")
        else:
            return integer

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
            update_student()
        elif num_chose == "5":
            show_students()
        elif num_chose == "6":
            break



if __name__ == "__main__":
            main()
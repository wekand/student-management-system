import json
def load_students():
    try:
        with open('students.json','r',encoding='utf-8') as f:
            students = json.load(f)
            return students
    except FileNotFoundError:
        students = [
            {"id": 101, "name": "张三", "score": 80},
            {"id": 102, "name": "李四", "score": 90},
            {"id": 103, "name": "王五", "score": 75}
        ]
        save_students(students)
        return students
    except json.JSONDecodeError:
        print("json文件解析失败")
        return None

def save_students(students):
    with open('students.json','w',encoding='utf-8') as f:
        json.dump(students,f,ensure_ascii=False,indent=4)
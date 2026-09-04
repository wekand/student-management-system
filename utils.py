
def get_integer(message):
    while True:
        try:
            integer= int(input(message))
        except ValueError:
            print("请输入数字")
        else:
            return integer

def get_score(message):
    while True:
        score=get_integer(message)
        if 0<=score<=100:
            return score
        else:
            print("成绩必须在0~100之间")
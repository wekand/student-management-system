class Student:
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score
    def add_score(self, amount):
        if  amount >0 and self.score+amount <= 100:
            self.score += amount
            return True
        else:
            return False

    def is_passed(self):
        return self.score >= 60



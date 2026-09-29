from sqlalchemy import Column, Integer, String
from app.database.session import Base
# 定义model
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)

    def is_passed(self):
        return self.score >= 60

    def add_score(self, amount):
        if amount < 0:
            return False
        if self.score + amount > 100:
            return False
        self.score += amount
        return True
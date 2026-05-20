# 7
class University:
    def __init__(self, name, students):
        self.name = name
        self.__students = students


    @property
    def students(self):
        return self.__students

    @password.setter
    def students(self, toza):
        self.__students = toza


s = University('Ali', 12212)

res = s.students
print(res)

s.students = 1
print(s.students)

class Student:
    def __init__(self, name, age, average_grade):
        self._name = name
        self._age = age
        self._average_grade = average_grade
        self._grades = []

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def average_grade(self):
        return self._average_grade

    @name.setter
    def name(self, value):
        self._name = value

    @age.setter
    def age(self, value):
        self._age = value

    @average_grade.setter
    def average_grade(self, value):
        self._average_grade = value

    def add_grade(self, grade):
        self._grades.append(grade)
        self._average_grade = round(sum(self._grades) / len(self._grades), 2)

    def get_info(self):
        return f"Студент: {self._name} | Возраст: {self._age} | Средний балл: {self._average_grade}"

    def evaluate(self):
        if self._average_grade > 8:
            return "Отлично"
        elif 6 <= self._average_grade <= 8:
            return "Хорошо"
        elif 4 <= self._average_grade < 6:
            return "Удовлетворительно"
        else:
            return "Неудовлетворительно"

    def is_excellent(self):
        return self._average_grade > 8

    def __str__(self):
        return self.get_info()
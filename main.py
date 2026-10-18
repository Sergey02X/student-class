from student import Student

s1 = Student("Иван Петров", 20, 9.2)
s2 = Student("Мария Иванова", 19, 7.5)
s3 = Student("Алексей Сидоров", 21, 5.4)
s4 = Student("Ольга Кузнецова", 18, 3.1)

students = [s1, s2, s3, s4]

for st in students:
    print(f"{st.get_info()} -> {st.evaluate()}")

print("\nИзменение свойств:")
s3.age = 22
s3.average_grade = 8.7
print(f"{s3.get_info()} -> {s3.evaluate()}")

print("\nДобавление оценок:")
s4.add_grade(9.0)
s4.add_grade(10.0)
s4.add_grade(8.5)
print(f"{s4.get_info()} -> {s4.evaluate()}")

print("\nОтличники:")
for st in students:
    print(f"{st.name}: {'да' if st.is_excellent() else 'нет'}")
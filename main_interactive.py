from student import Student

def main():
    print("=" * 40)
    print(" ИНТЕРАКТИВНЫЙ РЕЖИМ: Создание студента")
    print("=" * 40)
    
    try:
        name = input("Введите имя студента: ")
        age = int(input("Введите возраст: "))
        avg_grade = float(input("Введите начальный средний балл (0-10): "))
        
        # Создаем студента
        student = Student(name, age, avg_grade)
        
        print("\nСтудент успешно создан!")
        print(student.get_info())
        print(f"Оценка: {student.evaluate()}")
        
        # Добавление оценок
        while True:
            print("\nХотите добавить новую оценку?")
            choice = input("Введите 'да' для добавления или 'нет' для выхода: ").strip().lower()
            
            if choice == 'да':
                new_grade = float(input("Введите оценку (0-10): "))
                student.add_grade(new_grade)
                print(f"Оценка добавлена! Новый средний балл: {student.average_grade}")
                print(f"Текущий статус: {student.evaluate()}")
            elif choice == 'нет':
                break
            else:
                print("Пожалуйста, введите 'да' или 'нет'.")
                
        print("\n" + "=" * 40)
        print(" ИТОГОВАЯ ИНФОРМАЦИЯ")
        print("=" * 40)
        print(student.get_info())
        print(f"Итоговая оценка: {student.evaluate()}")
        print(f"Отличник: {'Да' if student.is_excellent() else 'Нет'}")
        
    except ValueError as e:
        print(f"\nОшибка ввода данных: {e}")
        print("Пожалуйста, запустите программу заново и введите корректные числа.")

if __name__ == "__main__":
    main()
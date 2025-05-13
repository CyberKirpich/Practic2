class Student:
    def __init__(self, surname, birth, group, grades):
        self.surname = surname
        self.birth = birth
        self.group = group
        self.grades = grades

    def change_surname(self, new_surname):
        self.surname = new_surname

    def change_birth(self, new_birth):
        self.birth = new_birth

    def change_group(self, new_group):
        self.group = new_group

    def show_info(self):
        print("Фамилия: ", self.surname)
        print("Дата рождения: ", self.birth)
        print("Группа: ", self.group)
        print("Оценки: ", self.grades)
students = [
    Student("Иванов", "01.01.2000", "101", [4, 5, 4, 3, 5]),
    Student("Петров", "15.03.2001", "102", [5, 4, 5, 4, 5]),
    Student("Сидоров", "28.07.1999", "103", [3, 4, 4, 5, 4]),
    Student("Кузнецов", "12.10.2002", "104", [4, 3, 5, 5, 3])
]
def find_student():
    surname = input("Введите фамилию: ")
    birth = input("Введите дату рождения: ")
    for s in students:
        if s.surname == surname and s.birth == birth:
            print("Найден студент: ")
            s.show_info()

def list_students():
    for i, s in enumerate(students):
        print('Студент #',i + 1)
        s.show_info()
    print()

def add_student():
    surname = input("Фамилия: ")
    birth = input("Дата рождения (дд.мм.гггг): ")
    group = input("Номер группы: ")
    grades = input("Введите 5 оценок через пробел: ").split()
    grades = list(map(int, grades))
    student = Student(surname, birth, group, grades)
    students.append(student)
    print("Студент добавлен")

def edit_student():
    num = int(input("Введите номер студента для изменения: ")) - 1
    if 0 <= num < len(students):
        s = students[num]
        print("1. Изменить фамилию")
        print("2. Изменить дату рождения")
        print("3. Изменить номер группы")
        changes = input("Выбор: ")
        if changes == "1":
            s.change_surname(input("Новая фамилия: "))
        elif changes == "2":
            s.change_birth(input("Новая дата рождения: "))
        elif changes == "3":
            s.change_group(input("Новый номер группы: "))
        else:
            print("Неверный выбор")
    else:
        print("Нет такого студента")
def programm():
    while True:
        print("\n1. Добавить студента")
        print("2. Список студентов")
        print("3. Изменить данные")
        print("4. Найти")
        action = input("Выберите действие: ")
        if action == "1":
            add_student()
        elif action == "2":
            list_students()
        elif action == "3":
            edit_student()
        elif action == "4":
            find_student()
programm()



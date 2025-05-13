class Numbers:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def show_numbers(self):
        print("Числа: ",self.num1, self.num2)

    def change_numbers(self, new_num1, new_num2):
        self.num1 = new_num1
        self.num2 = new_num2

    def sum_numbers(self):
        return self.num1 + self.num2

    def find_max(self):
        return max(self.num1, self.num2)

def calc():
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    numbers = Numbers(num1, num2)
    while True:
        print("\n1. Вывести числа")
        print("2. Изменить числа")
        print("3. Вычислить сумму")
        print("4. Найти наибольшее")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            numbers.show_numbers()
        elif choice == "2":
            new_num1 = int(input("Введите новое первое число: "))
            new_num2 = int(input("Введите новое второе число: "))
            numbers.change_numbers(new_num1, new_num2)
        elif choice == "3":
            print("Сумма чисел:", numbers.sum_numbers())
        elif choice == "4":
            print("Наибольшее число:", numbers.find_max())
        elif choice == "0":
            print("Выход из программы")
            break
        else:
            print("Неверный выбор")
calc()
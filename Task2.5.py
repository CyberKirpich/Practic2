class MyClass:
    def __init__(self, value1=0, value2=0):
        self.value1 = value1
        self.value2 = value2
        print(f"Создан объект с value1={self.value1}, value2={self.value2}")

    def __del__(self):
        print(f"Объект с value1={self.value1}, value2={self.value2} удален")
def main():
    while True:
        print("\n1. Создать объект с параметрами по умолчанию")
        print("2. Создать объект с заданными параметрами")
        print("0. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            obj = MyClass()
        elif choice == "2":
            value11 = int(input("Введите значение value1: "))
            value22 = int(input("Введите значение value2: "))
            obj = MyClass(value11, value22)
        elif choice == "0":
            print("Выход из программы")
            break
        else:
            print("Неверный выбор")
main()
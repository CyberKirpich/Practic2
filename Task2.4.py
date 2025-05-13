class Counter:
    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def get_value(self):
        return self.value

def main():
    value = int(input("Введите начальное значение счетчика, 0 - по умолчанию: "))
    counter = Counter(value)
    while True:
        print("\n1. Увеличить счетчик")
        print("2. Уменьшить счетчик")
        print("3. Вывести значение")
        print("0. Выход")
        choice = input("Выберите действие: \n")
        if choice == "1":
            counter.increment()
            print("Счетчик увеличен")
        elif choice == "2":
            counter.decrement()
            print("Счетчик уменьшен")
        elif choice == "3":
            print("Текущее значение счетчика: ",counter.get_value())
        elif choice == "0":
            print("Выход из программы")
            break
        else:
            print("Неверный выбор")
main()
class Worker:
    def __init__(self, name, surname, rate, days):
        self._name = name
        self._surname = surname
        self._rate = rate
        self._days = days

    def GetSalary(self):
        salary = self._rate * self._days
        print(f"Зарплата {self.get_name()} {self.get_surname()}: {salary}")

    def show_info(self):
        print("Имя: ", self.get_name())
        print("Фамилия: ", self.get_surname())
        print("Ставка: ", self.get_rate())
        print("Отработанные дни: ", self.get_days())

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_rate(self):
        return self._rate

    def get_days(self):
        return self._days
def main():
    workers = [
        Worker("Иван", "Иванов", 1000, 20),
        Worker("Мария", "Петрова", 1500, 15),
        Worker("Алексей", "Сидоров", 1200, 18)
    ]
    while True:
        print("\n1. Вывести зарплату всех работников")
        print("2. Вывести информацию о всех работниках")
        print("0. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            if workers:
                for worker in workers:
                    worker.GetSalary()
            else:
                print("Список работников пуст")
        elif choice == "2":
            if workers:
                for worker in workers:
                    worker.show_info()
            else:
                print("Список работников пуст")
        elif choice == "0":
            print("Выход из программы")
            break
        else:
            print("Неверный выбор")
main()
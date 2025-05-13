class Train:
    def __init__(self, destination, train_number, departure_time):
        self.destination = destination
        self.train_number = train_number
        self.departure_time = departure_time

    def show_info(self):
        print("Пункт назначения: ",self.destination)
        print("Номер поезда: ",self.train_number)
        print("Время отправления: ",self.departure_time)
trains = [
    Train("Москва", "123", "10:00"),
    Train("Санкт-Петербург", "456", "12:30"),
    Train("Екатеринбург", "789", "15:15"),
]

def find_train():
    train_number = input("Введите номер поезда: ")
    found = False
    for train in trains:
        if train.train_number == train_number:
            print("\nИнформация о поезде:")
            train.show_info()
            found = True
    if not found:
        print("Поезд с таким номером не найден")
def main():
    while True:
        print("\n1. Найти поезд")
        print("0. Выход")
        action = input("Выберите действие: ")
        if action == "1":
            find_train()
        elif action == "0":
            print("Выход из программы")
            break
        else:
            print("Неверная команда")
main()
class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def GetSalary(self):
        salary = self.rate * self.days
        print(f"Зарплата {self.name} {self.surname}: {salary}")

def main():
    workers = [
        Worker("Иван", "Иванов", 1000, 20),
        Worker("Мария", "Петрова", 1500, 15),
        Worker("Алексей", "Сидоров", 1200, 18)
    ]
    if workers:
            for worker in workers:
                worker.GetSalary()
main()
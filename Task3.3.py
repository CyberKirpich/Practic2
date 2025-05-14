class Calculation:
    def __init__(self):
        self.calculationLine = ""

    def SetCalculationLine(self, new_calculationLine):
        self.calculationLine = new_calculationLine

    def SetLastSymbolCalculationLine(self, symbol):
        self.calculationLine += symbol

    def GetCalculationLine(self):
        print(self.calculationLine)

    def GetLastSymbol(self):
        if self.calculationLine:
            return self.calculationLine[-1]
        else:
            return None

    def DeleteLastSymbol(self):
        if self.calculationLine:
            self.calculationLine = self.calculationLine[:-1]
        else:
            print("Строка пуста")
def main():
    calc = Calculation()
    while True:
        print("\n1. Установить строку вычисления")
        print("2. Добавить символ в конец строки")
        print("3. Вывести строку вычисления")
        print("4. Получить последний символ")
        print("5. Удалить последний символ")
        print("0. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            new_calculationLine = input("Введите новую строку вычисления: ")
            calc.SetCalculationLine(new_calculationLine)
        elif choice == "2":
            symbol = input("Введите символ для добавления: ")
            calc.SetLastSymbolCalculationLine(symbol)
        elif choice == "3":
            calc.GetCalculationLine()
        elif choice == "4":
            last_symbol = calc.GetLastSymbol()
            print(f"Последний символ: {last_symbol}")
        elif choice == "5":
            calc.DeleteLastSymbol()
        elif choice == "0":
            print("Выход из программы")
            break
        else:
            print("Неверный выбор")
main()
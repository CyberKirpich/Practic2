def calculate(num1, num2, operation):
    result = None
    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            return (num1, num2 ,operation, "\nНеизветсная операция")
    except ZeroDivisionError:
        result = "На 0 делить нельзя!"
    return (f"Первое число: '{num1}' Второе число:  '{num2}' Операция: '{operation}' Ответ: {result}")
print(calculate(1,3,'+'))
print(calculate(1,0,'/'))
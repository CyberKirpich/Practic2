import locale
from datetime import datetime
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
def format_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%d.%m.%Y')
        formatted_date = date_obj.strftime('%A, %d %B, %Y')
        formatted_date = formatted_date[0].upper() + formatted_date[1:]
        return formatted_date
    except ValueError:
        return ("Ошибка неверного формата даты")
print(format_date("31.05.2025"))

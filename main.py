def add_everything_up(a, b):
    # Проверяем, являются ли a и b разными типами
    if isinstance(a, str) and isinstance(b, (int, float)) or isinstance(b, str) and isinstance(a, (int, float)):
        # Если да, возвращаем их строковое представление
        return str(a) + str(b)

    # Иначе, складываем числа или используем конкатенацию для строк
    return a + b


# Примеры использования
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))  # Вывод: яблоко4215
print(add_everything_up(123.456, 7))  # Вывод: 130.456

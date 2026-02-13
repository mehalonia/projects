numbers = [1, 2, 3, 4, 5, 0]

for number in numbers:
    try:
        result = 10 / number
        print(f"Результат деления 10 на {number}: {result}")
    except ZeroDivisionError:
        print(f"Ошибка: Деление на ноль при попытке разделить 10 на {number}.")
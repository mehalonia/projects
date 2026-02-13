# Создаем словарь data
data = {'name': 'Ivan', 'age': 25}

# Пытаемся получить значение по ключу 'city'
try:
    city_value = data['city']
except KeyError:
    print("Ключ 'city' не найден в словаре.")
else:
    # Прибавляем 10 к значению
    city_value += 10
    print(f"Значение по ключу 'city': {city_value}")
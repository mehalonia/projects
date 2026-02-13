import requests

# URL с параметром запроса
url = 'https://www.google.com/search?q=google.com'

# Отправляем GET-запрос
response = requests.get(url)

# Проверяем статус ответа
if response.status_code == 200:
    # Получаем содержимое страницы
    content = response.text
    
    # Выводим размер контента (количество байт)
    print(f"Размер страницы: {len(content)} байт")
else:
    print(f"Не удалось загрузить страницу. Статус код: {response.status_code}")
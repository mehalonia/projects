# Импортируем библиотеку random для генерации случайных чисел
import random

def main():
    # Генерируем список из 10 случайных целых чисел от 1 до 50
    items = [random.randint(1, 50) for _ in range(10)]
    
    # Печатаем каждый элемент списка
    for item in items:
        print(item)

# Вызываем функцию main()
if __name__ == "__main__":
    main()
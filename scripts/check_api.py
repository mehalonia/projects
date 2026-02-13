import pandas as pd

# Импорт библиотеки pandas
try:
    # Проверка наличия библиотеки pandas
    import pandas
    
    # Вывод версии pandas
    print(f"Версия pandas: {pandas.__version__}")
except ImportError as e:
    # Если библиотека pandas не найдена, вывести ошибку
    print("Ошибка: Библиотека pandas не установлена")
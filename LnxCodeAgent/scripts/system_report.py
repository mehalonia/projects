import os
from datetime import datetime
import getpass

def get_user():
    """Получить имя текущего пользователя (безопасный метод)."""
    return getpass.getuser()

def get_uptime():
    """Получить аптайм системы."""
    # Для Linux используем чтение /proc/uptime
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    
    days = int(uptime_seconds // 86400)
    hours = int((uptime_seconds % 86400) // 3600)
    minutes = int((uptime_seconds % 3600) // 60)
    return f"{days} дн {hours} ч {minutes} мин"

def list_files():
    """Собрать список файлов."""
    return [f for f in os.listdir('.') if os.path.isfile(f)]

def main():
    user = get_user()
    uptime = get_uptime()
    files = list_files()

    # Сохраняем информацию
    with open('report.txt', 'w') as f_out:
        f_out.write(f"Имя пользователя: {user}\n")
        f_out.write(f"Аптайм системы: {uptime}\n")
        f_out.write("Список всех файлов:\n")
        for file_name in files:
            f_out.write(file_name + '\n')

    # Выводим содержимое на экран
    with open('report.txt', 'r') as f_in:
        print(f_in.read())

if __name__ == "__main__":
    main()

import os

def write_to_file(filename, content):
    """Создает файл и записывает в него код."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content.strip())
        return f"✅ Файл '{filename}' успешно сохранен!"
    except Exception as e:
        return f"❌ Ошибка при записи файла: {e}"

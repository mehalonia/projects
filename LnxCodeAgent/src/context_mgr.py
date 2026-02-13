import os

def get_project_context():
    """Собирает список всех файлов в проекте."""
    files_list = []
    exclude = {'venv', '.git', '__pycache__'}
    
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in exclude]
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), ".")
            files_list.append(rel_path)
            
    return "\n".join(files_list)

def read_file_content(path):
    """Читает содержимое файла."""
    if os.path.exists(path) and os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    return "Файл не найден."

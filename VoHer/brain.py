def process_command(text):
    if not text:
        return None
    
    # 1. Приветствие
    if "привет" in text or "здравствуй" in text:
        return "Привет! Я на связи."
    
    # 2. Время
    elif "время" in text:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M")
        return f"Сейчас {now}."
    
    # 3. Выход
    elif "пока" in text or "выключись" in text or "стоп" in text:
        return "Завершаю работу"
    
    # ВАЖНО: Если команда не узнана, возвращаем None (молчим)
    # Это предотвратит бесконечный диалог робота с самим собой
    return None

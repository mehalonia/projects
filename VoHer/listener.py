import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    
    # Настройка под твой сверхчувствительный микрофон
    # Поднимаем порог: 300-500 — норма, 1000+ — для очень громких микрофонов
    recognizer.energy_threshold = 1500 
    recognizer.dynamic_energy_threshold = False # Выключаем автоподстройку
    
    with sr.Microphone() as source:
        # Убираем долгую подготовку
        try:
            # Слушаем максимум 3 секунды, если тишина — выходим
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=4)
            text = recognizer.recognize_google(audio, language="ru-RU")
            return text.lower()
        except:
            return None

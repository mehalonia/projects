import listener
import brain
import speaker
import time
from pynput import keyboard

# Новая кнопка: Правый Option
WAKE_KEY = keyboard.Key.alt_r
# Поддержка обеих раскладок для подтверждения
CONFIRM_KEYS = ['y', 'н'] 

class VoHerController:
    def __init__(self):
        self.is_recording = False
        self.press_time = 0
        self.current_text = None

    def on_press(self, key):
        if key == WAKE_KEY and not self.is_recording:
            self.press_time = time.time()
            self.is_recording = True
            if self.current_text:
                print("\n[СБРОС] Предыдущая команда отменена.")
                self.current_text = None
            
    def on_release(self, key):
        if key == WAKE_KEY:
            self.is_recording = False
            duration = time.time() - self.press_time
            
            if duration < 0.3:
                print("[READY] Система очищена.")
                self.current_text = None
            else:
                print("[ОБРАБОТКА] Запись завершена...")
                self.process_voice()
        
        # Проверка подтверждения с учетом раскладки
        if hasattr(key, 'char') and key.char is not None:
            if key.char.lower() in CONFIRM_KEYS and self.current_text:
                self.execute_command()

    def process_voice(self):
        text = listener.listen() 
        if text:
            print(f"Распознано: {text}")
            print(f"Нажми 'Y' (или 'Н') для подтверждения или кликни Option для отмены.")
            self.current_text = text
        else:
            print("Тишина. Попробуй еще раз.")

    def execute_command(self):
        response = brain.process_command(self.current_text)
        if response:
            speaker.say(response)
        self.current_text = None
        print("--- Готов к работе ---")

controller = VoHerController()

def start_voher():
    print(f"Запущено. Зажми ПРАВЫЙ OPTION для записи.")
    with keyboard.Listener(on_press=controller.on_press, on_release=controller.on_release) as k_listener:
        k_listener.join()

if __name__ == "__main__":
    start_voher()

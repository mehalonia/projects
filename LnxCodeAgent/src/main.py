import os
import subprocess
import sys
import re

# Импортируем наши модули, которые теперь лежат в той же папке src
from brain import CodeBrain
from context_mgr import get_project_context
from tools.writer import write_to_file

def git_sync(filename):
    """Автоматически пушит изменения в GitHub для контроля"""
    try:
        # Проверяем, инициализирован ли гит
        if not os.path.exists(".git") and not os.path.exists("../.git"):
            return # Гит не настроен, пропускаем
            
        subprocess.run(["git", "add", "."], capture_output=True)
        subprocess.run(["git", "commit", "-m", f"Auto-sync: updated {filename}"], capture_output=True)
        # В фоне пробуем отправить, чтобы не тормозить работу
        subprocess.Popen(["git", "push"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("🌐 Состояние синхронизировано с облаком (GitHub).")
    except Exception:
        pass # Если гита нет, просто работаем дальше

def main():
    brain = CodeBrain()
    last_filename = None
    print("🚀 LnxCodeAgent v2.3: Структура 'src' активна")

    while True:
        query = input("\n👤 Вы: ")
        if query.lower() in ['exit', 'выход', 'quit']:
            break

        context = get_project_context()
        print("🤖 Ответ:\n" + "—"*20)

        full_response = ""
        for chunk in brain.send_request(query, context):
            print(chunk, end="", flush=True)
            full_response += chunk
        print("\n" + "—"*20)

        current_code_context = full_response
        
        while "```" in current_code_context:
            if last_filename:
                prompt = f"💾 Сохранить код в '{last_filename}'? (y/n/новое_имя): "
            else:
                prompt = "💾 Сохранить код в файл? (имя.py / n): "
            
            save_input = input(prompt).strip()
            if save_input.lower() == 'n': break
            
            if last_filename and (save_input.lower() == 'y' or save_input == ""):
                filename = last_filename
            elif save_input.lower() != 'y':
                filename = save_input
                last_filename = filename
            else: continue

            try:
                # Очистка и сохранение
                raw_code = current_code_context.split("```")[1]
                if raw_code.startswith("python"): raw_code = raw_code[6:]
                clean_code = raw_code.strip()
                
                print(write_to_file(filename, clean_code))

                # --- ТВОЕ ПРАВИЛО ПОДТВЕРЖДЕНИЯ ---
                confirm = input(f"📝 Вы подтверждаете, что код в {filename} изменен? (y/n): ")
                if confirm.lower() == 'y':
                    # СИНХРОНИЗАЦИЯ ДЛЯ МОЕГО КОНТРОЛЯ
                    git_sync(filename)
                    
                    run_it = input(f"🛠 Запустить {filename}? (y/n): ")
                    if run_it.lower() == 'y':
                        print(f"⌛ Запуск {filename}...")
                        result = subprocess.run([sys.executable, filename], capture_output=True, text=True)

                        if result.returncode != 0:
                            print(f"❌ Ошибка:\n{result.stderr}")
                            if input("🤔 Исправить автоматически? (y/n): ").lower() == 'y':
                                auto_query = f"Скрипт {filename} упал с ошибкой:\n{result.stderr}\nИсправь его."
                                print("🔄 Перегенерация...")
                                current_code_context = ""
                                for chunk in brain.send_request(auto_query, context):
                                    print(chunk, end="", flush=True)
                                    current_code_context += chunk
                                print("\n" + "—"*20)
                                continue 
                        else:
                            print(f"✅ Успех!\nВывод:\n{result.stdout}")
                break
            except Exception as e:
                print(f"❌ Ошибка: {e}")
                break

if __name__ == "__main__":
    main()

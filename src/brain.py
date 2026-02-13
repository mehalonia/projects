import requests
import json

class CodeBrain:
    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.model = "qwen2.5-coder:3b" 

    def send_request(self, prompt, context):
        full_prompt = f"""Ты — LnxCodeAgent. Пиши только чистый и рабочий код.
        Контекст: {context}
        Запрос: {prompt}
        """
        
        data = {
            "model": self.model,
            "prompt": full_prompt,
            "stream": True  # ВКЛЮЧАЕМ СТРИМИНГ
        }
        
        try:
            # Используем stream=True в самом запросе requests
            response = requests.post(self.url, json=data, stream=True)
            for line in response.iter_lines():
                if line:
                    # Декодируем каждую порцию текста из JSON
                    chunk = json.loads(line.decode('utf-8'))
                    yield chunk.get("response", "")
                    if chunk.get("done"):
                        break
        except Exception as e:
            yield f"Ошибка связи: {e}"

import os
from gtts import gTTS

def say(text):
    print(f"VoHer: {text}")
    tts = gTTS(text=text, lang='ru')
    tts.save("reply.mp3")
    # afplay — стандартный плеер macOS для терминала
    os.system("afplay reply.mp3")
    os.remove("reply.mp3")

if __name__ == "__main__":
    say("Система запущена. Я тебя слышу.")

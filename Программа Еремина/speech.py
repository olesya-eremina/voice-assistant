import pyttsx3
from time import sleep
from threading import *

mic_blocked = False #глобальная переменная-флаг для блокировки микрофона
engine = pyttsx3.init() #инициализируем голосовой движок
engine.setProperty('rate', 180)

def block_mic(): #блокировка микрофона
    global mic_blocked
    mic_blocked = True

def unblock_mic(): #разблокировка микрофона
    global mic_blocked
    mic_blocked = False

def sleep_print(str, label, text):
    for char in text:
        str+=char
        label.setText(str)
        label.adjustSize()
        sleep(0.05)

def speaker(self, text): #озвучка текста
    t = Thread(target=sleep_print, args=("", self.output_label, text))
    t.start()
    block_mic()
    engine.say(text)
    engine.runAndWait()
    unblock_mic()
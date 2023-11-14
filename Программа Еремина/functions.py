import sys #модуль, который обеспечивает доступ
            #к некоторым переменным и функциям,
            # #взаимодействующим с интерпретатором python.
import requests #модуль для языка Python, который используют
                #для упрощения работы с HTTP-запросами. 
from translate import Translator #модуль для перевода
import webbrowser #модуль для просмотра веб-документов
import os #модуль для работы с операционной системой
import datetime #модуль для работы с датами и временем

import editing_settings
import speech


def offBot(self): #функция отключения бота
    self.launch_Button.setText("Пуск")
    self.launch_Button.setStyleSheet("QPushButton\n"
                                    "{\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "    background-color: rgb(85, 34, 51);\n"
                                    "    font: 14pt \"Comic Sans MS\";\n"
                                    "    border-radius: 10;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover\n"
                                    "{\n"
                                    "    background-color: rgb(177, 149, 158);\n"
                                    "}")
    sys.exit()

def get_weather(self):
    open_weather_token = "a5635055be9774223fa602e7993d17de"
    
    translator = Translator(from_lang="russian",to_lang="english")
    try:
        city = translator.translate(editing_settings.SETTINGS['city'])
    except:
        speech.speaker(self, "Проверьте название города")
        return

    weather = {
        "Clear": "Ясно",
        "Clouds": "Облачно",
        "Rain": "Дождь",
        "Drizzle": "Дождь",
        "Thunderstorm": "Гроза",
        "Snow": "Снег",
        "Mist": "Туман"
    }
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["main"]
        if weather_description in weather:
            wd = weather[weather_description]
        else:
            wd = "не найдена"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]

        result=(f"Погода в городе {editing_settings.SETTINGS['city']} сегодня: {wd} \nТемпература {cur_weather} градусов Цельсия\n"
              f"Влажность {humidity}%\nДавление {pressure} миллиметров ртутного столба\nВетер: {wind} метров в секунду"
              )
        speech.speaker(self, result)

    except Exception as ex:
        speech.speaker(self,"Проверьте название города")

def time(self):
    now = datetime.datetime.now()
    res = f" время: {now.hour}:{now.minute}"
    speech.speaker(self, res)

def open_app(self, app_name):
    ex=os.system(editing_settings.APP_PATHS[app_name])
    if ex != 0:
        speech.speaker(self, "Исполняемый файл не найден")

def open_website(ws_name):
    webbrowser.open_new_tab(editing_settings.WEB_PATHS[ws_name])

def offpc():
    os.system('shutdown -s')


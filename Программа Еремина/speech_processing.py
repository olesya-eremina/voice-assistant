from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
import sounddevice as sd
import vosk
import random
import json
import queue
from pymystem3 import Mystem
from threading import *

import words
from functions import *
import speech


q = queue.Queue() #инициализируем очередь
model = vosk.Model('model_small') #подгружаем модель распознования речи
device = sd.default.device # выбираем девайсы по умолчанию
#получаем частоту микрофона
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])

myst = Mystem() #инициализация программы для лемматизации

def diction_form(text): #лемматизация
    text = ''.join(myst.lemmatize(text)).rstrip('\n')
    return text

def callback(indata, frames, time, status): #добавление в очередь семплов из потока
    if not speech.mic_blocked:
        q.put(bytes(indata))

def check(rec, temp1, self):
        temp2=rec.PartialResult()
        if temp2 != '{"text": ""}' and temp2 != '{\n  "partial" : ""\n}':
                temp2 = temp2.replace('{\n  "partial" : "', "")
                temp2 = temp2.replace('"\n}', "")
                str= temp2[len(temp1):]
                if temp2 != temp1:
                        speech.sleep_print(temp1, self.input_label, str)
                return temp2
        return ""
        

def main(self):
        x = []
        y = []
        
        try:
                with open('json/x.json', 'r') as filehandle:
                        x=json.load(filehandle)
                
                with open('json/y.json', 'r') as filehandle:
                        y=json.load(filehandle)
        except:
                speech.speaker(self, "Не получается загрузить данные")
                function.offBot(self);



        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(x) #изучение словарного запаса и idf; преобразование документов в матрицу

        try:
                clf = KNeighborsClassifier(n_neighbors=1, p=1, weights='distance')
                clf.fit(vectors, y)
        except:
               speech.speaker(self, "Загружены неверные данные")
               offBot(self)


        #постоянная прослушка микрофона
        with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16',
                                channels=1, callback=callback):
                rec = vosk.KaldiRecognizer(model, samplerate)
                temp1=""
                while self.flag:
                        data = q.get()
                        temp2=rec.PartialResult()
                        if temp2 != '{"text": ""}':
                                temp1=check(rec, temp1, self)
                        if rec.AcceptWaveform(data):
                                data = json.loads(rec.Result())['text']
                                temp1=""
                                self.input_label.setText(data)
                                self.input_label.adjustSize()
                                if data:
                                    self.output_label.setText("")
                                    self.output_label.adjustSize()
                                    recognize(self, diction_form(data), vectorizer, clf) #обработка
        self.flag = True
        offBot(self)

def recognize(self, data, vectorizer, clf): #анализ распознанной речи
        trg = words.TRIGGERS.intersection(data.split()) #поиск слов-триггеров
        if not trg:
                return
        if trg: #удаление слов-триггеров
                data.replace(list(trg)[0], '')

        text_vector = vectorizer.transform([data]).toarray()[0] #векторизация
        intent = clf.predict([text_vector])[0] #предсказание намерения

        if intent not in words.SPEAKERS:
                try:
                        out = random.choice(words.INTENTS[intent]["responses"]) #выбор рандомного ответа на предсказанное намерение
                        speech.speaker(self, out) #озвучка ответа
                except:
                       speech.speaker(self, "Команда не распознана")

        if intent in words.FUNCS: #выполнение функций
                exec(intent + '(self)')
        
        if intent in words.APPS:
                open_app(self, intent)

        if intent in words.WEB_SITES:
                open_website(intent)
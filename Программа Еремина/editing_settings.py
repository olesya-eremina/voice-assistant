import json

try:
    with open ('json/app_paths.json', 'r') as filehandle:
        APP_PATHS = json.load(filehandle)
except:
    APP_PATHS = {
    'telegram': '',
    'calc': '',
    'game': '',
    'excel': '',
    'paint': '',
    'powerpoint': '',
    'terminal': '',
    'word': '',
    'settings': '',
    'calendar': '',
    'notebook': '',
    'photo': '',
    'camera': '',
    'watch': ''
}

try:
    with open ('json/web_paths.json', 'r') as filehandle:
        WEB_PATHS = json.load(filehandle)
except:
    WEB_PATHS = {
    'browser': 'http://',
    'mail': 'https://mail.google.com/',
    'youtube': 'https://www.youtube.com/',
    'vk': 'https://vk.com/',
    'kinopoisk': 'https://www.kinopoisk.ru/',
    'yandexmusic': 'https://music.yandex.ru/',
    'wikipedia': 'https://ru.wikipedia.org/',
    'ok': 'https://ok.ru/',
    'google': 'https://www.google.ru/',
    'rambler': 'https://www.rambler.ru/',
    'avito': 'https://www.avito.ru/',
    'gismeteo': 'https://www.gismeteo.ru/',
    'ozon': 'https://www.ozon.ru/',
    'rbc': 'https://rt.rbc.ru/',
    'yandexmarket': 'https://market.yandex.ru/',
    'gosuslugi': 'https://www.gosuslugi.ru/',
    'yandexeda': 'https://eda.yandex.ru/',
    'googletranslate': 'https://translate.google.com/'
}

try:
    with open ('json/settings.json', 'r') as filehandle:
        SETTINGS = json.load(filehandle)
except:
    SETTINGS={'city': ''}

def save_apps(self):
        APP_PATHS['telegram'] = self.telegram_lineEdit.text();
        APP_PATHS['calc'] = self.calc_lineEdit.text();
        APP_PATHS['game'] = self.game_lineEdit.text();
        APP_PATHS['excel'] = self.excel_lineEdit.text();
        APP_PATHS['paint'] = self.paint_lineEdit.text();
        APP_PATHS['powerpoint'] = self.powerpoint_lineEdit.text();
        APP_PATHS['terminal'] = self.terminal_lineEdit.text();
        APP_PATHS['word'] = self.word_lineEdit.text();
        APP_PATHS['settings'] = self.settings_lineEdit.text();
        APP_PATHS['calendar'] = self.calendar_lineEdit.text();
        APP_PATHS['notebook'] = self.notebook_lineEdit.text();
        APP_PATHS['photo'] = self.photo_lineEdit.text();
        APP_PATHS['camera'] = self.camera_lineEdit.text();
        APP_PATHS['watch'] = self.watch_lineEdit.text();
        with open('json/app_paths.json', 'w') as filehandle:
                json.dump(APP_PATHS, filehandle)

def save_webs(self):
        WEB_PATHS['browser'] = self.browser_lineEdit.text()
        WEB_PATHS['mail'] = self.mail_lineEdit.text()
        WEB_PATHS['youtube'] = self.youtube_lineEdit.text()
        WEB_PATHS['vk'] = self.vk_lineEdit.text()
        WEB_PATHS['kinopoisk'] = self.kinopoisk_lineEdit.text()
        WEB_PATHS['yandexmusic'] = self.yandexmusic_lineEdit.text()
        WEB_PATHS['wikipedia'] = self.wikipedia_lineEdit.text()
        WEB_PATHS['ok'] = self.ok_lineEdit.text()
        WEB_PATHS['google'] = self.google_lineEdit.text()
        WEB_PATHS['rambler'] = self.rambler_lineEdit.text()
        WEB_PATHS['avito'] = self.avito_lineEdit.text()
        WEB_PATHS['gismeteo'] = self.gismeteo_lineEdit.text()
        WEB_PATHS['ozon'] = self.ozon_lineEdit.text()
        WEB_PATHS['rbc'] = self.rbc_lineEdit.text()
        WEB_PATHS['yandexmarket'] = self.yandexmarket_lineEdit.text()
        WEB_PATHS['gosuslugi'] = self.gosuslugi_lineEdit.text()
        WEB_PATHS['yandexeda'] = self.yandexeda_lineEdit.text()
        WEB_PATHS['googletranslate'] = self.googletranslate_lineEdit.text()
        with open('json/web_paths.json', 'w') as filehandle:
                json.dump(WEB_PATHS, filehandle)

def save_settings(self):
        SETTINGS['city'] = self.city_lineEdit.text()
        with open('json/settings.json', 'w') as filehandle:
                json.dump(SETTINGS, filehandle)
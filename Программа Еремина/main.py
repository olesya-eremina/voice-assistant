from PyQt5 import QtCore, QtGui, QtWidgets
from threading import *

import speech_processing
from editing_settings import APP_PATHS, WEB_PATHS, SETTINGS, save_apps, save_webs, save_settings

class Ui_MainWindow(object):
    flag = True
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 670)
        font = QtGui.QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow\n"
"{\n"
"    background-color: rgb(168, 193, 240)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 830, 630))
        font = QtGui.QFont()
        font.setKerning(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane\n"
"{\n"
"    border: 1px;\n"
"    margin: 0px;\n"
"    background-color: rgb(239, 217, 206);\n"
"    border-radius: 10;\n"
"    border-top-left-radius: 0;\n"
"}\n"
"\n"
"QTabBar::tab\n"
"{\n"
"    background-color: rgb(160, 126, 136);\n"
"    min-width: 30ex;\n"
"    min-height: 8ex;\n"
"    margin-left: 1px;\n"
"    left: -1px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"Comic Sans MS\";\n"
"    border-top-left-radius: 10;\n"
"    border-top-right-radius: 10;\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    background-color: rgb(239, 217, 206);\n"
"    color: rgb(85, 34, 51);\n"
"}\n"
"\n"
"QTabBar::tab:hover\n"
"{\n"
"    background-color: rgb(177, 149, 158);\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    color: rgb(0, 0, 127);\n"
"    font: 10pt \"Comic Sans MS\";\n"
"    border-radius: 10;\n"
"    padding-left: 5px;\n"
"    color: rgb(35, 99, 209)\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"    color: rgb(85, 34, 51);\n"
"}\n"
"\n"
"QScrollArea\n"
"{\n"
"    padding: 5px;\n"
"    border: 2px solid white;\n"
"    border-radius: 10;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 252, 90, 90))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./icons/bot.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(720, 40, 90, 90))
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./icons/man.png"))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.output_label = QtWidgets.QLabel(self.tab)
        self.output_label.setGeometry(QtCore.QRect(140, 260, 460, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_label.sizePolicy().hasHeightForWidth())
        self.output_label.setSizePolicy(sizePolicy)
        self.output_label.setMinimumSize(QtCore.QSize(460, 90))
        self.output_label.setMaximumSize(QtCore.QSize(460, 200))
        self.output_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10;\n"
"    font: 10pt \"Comic Sans MS\";\n"
"    padding: 10px;\n"
"    color: rgb(85, 34, 51);\n"
"}")
        self.output_label.setWordWrap(True)
        self.output_label.setObjectName("output_label")
        self.output_label.setAlignment(QtCore.Qt.AlignCenter)
        self.input_label = QtWidgets.QLabel(self.tab)
        self.input_label.setGeometry(QtCore.QRect(240, 40, 460, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_label.sizePolicy().hasHeightForWidth())
        self.input_label.setSizePolicy(sizePolicy)
        self.input_label.setMinimumSize(QtCore.QSize(460, 90))
        self.input_label.setMaximumSize(QtCore.QSize(460, 200))
        self.input_label.setStyleSheet("QLabel\n"
"{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10;\n"
"    font: 10pt \"Comic Sans MS\";\n"
"    padding: 10px;\n"
"    color: rgb(85, 34, 51);\n"
"}")
        self.input_label.setWordWrap(True)
        self.input_label.setObjectName("input_label")
        self.input_label.setAlignment(QtCore.Qt.AlignCenter)
        self.launch_Button = QtWidgets.QPushButton(self.tab)
        self.launch_Button.setGeometry(QtCore.QRect(305, 500, 220, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.launch_Button.setFont(font)
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
        self.launch_Button.setObjectName("launch_Button")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(700, 65, 40, 40))
        self.label_3.setStyleSheet("width: 0;\n"
"height: 0;\n"
"border: 20px solid rgb(239, 217, 206);\n"
"border-left-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(100, 285, 40, 40))
        self.label_4.setStyleSheet("width: 0;\n"
"height: 0;\n"
"border: 20px solid rgb(239, 217, 206);\n"
"border-right-color:  rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.output_label.raise_()
        self.input_label.raise_()
        self.launch_Button.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("")
        self.tab_2.setObjectName("tab_2")
        self.save_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.save_pushButton.setGeometry(QtCore.QRect(305, 500, 220, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.save_pushButton.setFont(font)
        self.save_pushButton.setStyleSheet("QPushButton\n"
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
        self.save_pushButton.setObjectName("save_pushButton")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea.setGeometry(QtCore.QRect(20, 20, 790, 460))
        self.scrollArea.setStyleSheet("QWidget\n"
"{\n"
"    background-color: rgb(239, 217, 206);\n"
"}\n"
"QLineEdit\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -31, 755, 477))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout_2 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout_2.setObjectName("formLayout_2")
        self.telegram_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.telegram_label.setFont(font)
        self.telegram_label.setStyleSheet("")
        self.telegram_label.setObjectName("telegram_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.telegram_label)
        self.word_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setKerning(False)
        self.word_label.setFont(font)
        self.word_label.setStyleSheet("")
        self.word_label.setObjectName("word_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.word_label)
        self.powerpoint_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.powerpoint_label.setFont(font)
        self.powerpoint_label.setStyleSheet("")
        self.powerpoint_label.setObjectName("powerpoint_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.powerpoint_label)
        self.excel_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.excel_label.setFont(font)
        self.excel_label.setStyleSheet("")
        self.excel_label.setObjectName("excel_label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.excel_label)
        self.paint_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.paint_label.setStyleSheet("")
        self.paint_label.setObjectName("paint_label")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.paint_label)
        self.game_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.game_label.setStyleSheet("")
        self.game_label.setObjectName("game_label")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.game_label)
        self.terminal_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.terminal_label.setStyleSheet("")
        self.terminal_label.setObjectName("terminal_label")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.terminal_label)
        self.calc_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.calc_label.setStyleSheet("")
        self.calc_label.setObjectName("calc_label")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.calc_label)
        self.settings_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.settings_label.setStyleSheet("")
        self.settings_label.setObjectName("settings_label")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.settings_label)
        self.calendar_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.calendar_label.setStyleSheet("")
        self.calendar_label.setObjectName("calendar_label")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.calendar_label)
        self.notebook_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.notebook_label.setStyleSheet("")
        self.notebook_label.setObjectName("notebook_label")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.notebook_label)
        self.photo_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.photo_label.setStyleSheet("")
        self.photo_label.setObjectName("photo_label")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.photo_label)
        self.camera_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.camera_label.setStyleSheet("")
        self.camera_label.setObjectName("camera_label")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.camera_label)
        self.watch_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.watch_label.setStyleSheet("")
        self.watch_label.setObjectName("watch_label")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.watch_label)
        self.telegram_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.telegram_lineEdit.setFont(font)
        self.telegram_lineEdit.setStyleSheet("")
        self.telegram_lineEdit.setObjectName("telegram_lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.telegram_lineEdit)
        self.word_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.word_lineEdit.setObjectName("word_lineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.word_lineEdit)
        self.powerpoint_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.powerpoint_lineEdit.setObjectName("powerpoint_lineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.powerpoint_lineEdit)
        self.excel_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.excel_lineEdit.setObjectName("excel_lineEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.excel_lineEdit)
        self.paint_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.paint_lineEdit.setObjectName("paint_lineEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.paint_lineEdit)
        self.game_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.game_lineEdit.setObjectName("game_lineEdit")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.game_lineEdit)
        self.terminal_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.terminal_lineEdit.setObjectName("terminal_lineEdit")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.terminal_lineEdit)
        self.calc_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.calc_lineEdit.setObjectName("calc_lineEdit")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.calc_lineEdit)
        self.settings_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.settings_lineEdit.setObjectName("settings_lineEdit")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.settings_lineEdit)
        self.calendar_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.calendar_lineEdit.setObjectName("calendar_lineEdit")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.calendar_lineEdit)
        self.notebook_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.notebook_lineEdit.setObjectName("notebook_lineEdit")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.notebook_lineEdit)
        self.photo_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.photo_lineEdit.setObjectName("photo_lineEdit")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.photo_lineEdit)
        self.camera_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.camera_lineEdit.setObjectName("camera_lineEdit")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.camera_lineEdit)
        self.watch_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.watch_lineEdit.setObjectName("watch_lineEdit")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.watch_lineEdit)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_2.setGeometry(QtCore.QRect(20, 20, 790, 460))
        self.scrollArea_2.setStyleSheet("QWidget\n"
"{\n"
"    background-color: rgb(239, 217, 206);\n"
"}\n"
"QLineEdit\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 755, 609))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents_3)
        self.formLayout_4.setObjectName("formLayout_4")
        self.browser_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.browser_label.setObjectName("browser_label")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.browser_label)
        self.mail_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.mail_label.setObjectName("mail_label")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.mail_label)
        self.youtube_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.youtube_label.setObjectName("youtube_label")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.youtube_label)
        self.vk_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.vk_label.setObjectName("vk_label")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.vk_label)
        self.kinopoisk_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.kinopoisk_label.setObjectName("kinopoisk_label")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.kinopoisk_label)
        self.yandexmusic_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.yandexmusic_label.setObjectName("yandexmusic_label")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.yandexmusic_label)
        self.wikipedia_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.wikipedia_label.setObjectName("wikipedia_label")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.wikipedia_label)
        self.ok_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ok_label.setObjectName("ok_label")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.ok_label)
        self.google_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.google_label.setObjectName("google_label")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.google_label)
        self.rambler_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.rambler_label.setObjectName("rambler_label")
        self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.rambler_label)
        self.avito_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.avito_label.setObjectName("avito_label")
        self.formLayout_4.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.avito_label)
        self.gismeteo_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.gismeteo_label.setObjectName("gismeteo_label")
        self.formLayout_4.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.gismeteo_label)
        self.ozon_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ozon_label.setObjectName("ozon_label")
        self.formLayout_4.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.ozon_label)
        self.rbc_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.rbc_label.setObjectName("rbc_label")
        self.formLayout_4.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.rbc_label)
        self.yandexmarket_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.yandexmarket_label.setObjectName("yandexmarket_label")
        self.formLayout_4.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.yandexmarket_label)
        self.gosuslugi_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.gosuslugi_label.setObjectName("gosuslugi_label")
        self.formLayout_4.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.gosuslugi_label)
        self.yandexeda_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.yandexeda_label.setObjectName("yandexeda_label")
        self.formLayout_4.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.yandexeda_label)
        self.googletranslate_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.googletranslate_label.setObjectName("googletranslate_label")
        self.formLayout_4.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.googletranslate_label)
        self.browser_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.browser_lineEdit.setObjectName("browser_lineEdit")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.browser_lineEdit)
        self.mail_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.mail_lineEdit.setObjectName("mail_lineEdit")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.mail_lineEdit)
        self.youtube_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.youtube_lineEdit.setObjectName("youtube_lineEdit")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.youtube_lineEdit)
        self.vk_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.vk_lineEdit.setObjectName("vk_lineEdit")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.vk_lineEdit)
        self.kinopoisk_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.kinopoisk_lineEdit.setObjectName("kinopoisk_lineEdit")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.kinopoisk_lineEdit)
        self.yandexmusic_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.yandexmusic_lineEdit.setObjectName("yandexmusic_lineEdit")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.yandexmusic_lineEdit)
        self.wikipedia_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.wikipedia_lineEdit.setObjectName("wikipedia_lineEdit")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.wikipedia_lineEdit)
        self.ok_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.ok_lineEdit.setObjectName("ok_lineEdit")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.ok_lineEdit)
        self.google_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.google_lineEdit.setObjectName("google_lineEdit")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.google_lineEdit)
        self.rambler_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.rambler_lineEdit.setObjectName("rambler_lineEdit")
        self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.rambler_lineEdit)
        self.avito_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.avito_lineEdit.setObjectName("avito_lineEdit")
        self.formLayout_4.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.avito_lineEdit)
        self.gismeteo_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.gismeteo_lineEdit.setObjectName("gismeteo_lineEdit")
        self.formLayout_4.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.gismeteo_lineEdit)
        self.ozon_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.ozon_lineEdit.setObjectName("ozon_lineEdit")
        self.formLayout_4.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.ozon_lineEdit)
        self.rbc_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.rbc_lineEdit.setObjectName("rbc_lineEdit")
        self.formLayout_4.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.rbc_lineEdit)
        self.yandexmarket_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.yandexmarket_lineEdit.setObjectName("yandexmarket_lineEdit")
        self.formLayout_4.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.yandexmarket_lineEdit)
        self.gosuslugi_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.gosuslugi_lineEdit.setObjectName("gosuslugi_lineEdit")
        self.formLayout_4.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.gosuslugi_lineEdit)
        self.yandexeda_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.yandexeda_lineEdit.setObjectName("yandexeda_lineEdit")
        self.formLayout_4.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.yandexeda_lineEdit)
        self.googletranslate_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.googletranslate_lineEdit.setObjectName("googletranslate_lineEdit")
        self.formLayout_4.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.googletranslate_lineEdit)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.save2_pushButton = QtWidgets.QPushButton(self.tab_3)
        self.save2_pushButton.setGeometry(QtCore.QRect(305, 500, 220, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.save2_pushButton.setFont(font)
        self.save2_pushButton.setStyleSheet("QPushButton\n"
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
        self.save2_pushButton.setObjectName("save2_pushButton")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.save3_pushButton = QtWidgets.QPushButton(self.tab_4)
        self.save3_pushButton.setGeometry(QtCore.QRect(305, 500, 220, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.save3_pushButton.setFont(font)
        self.save3_pushButton.setStyleSheet("QPushButton\n"
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
        self.save3_pushButton.setObjectName("save3_pushButton")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea_3.setGeometry(QtCore.QRect(20, 20, 790, 460))
        self.scrollArea_3.setStyleSheet("QWidget\n"
"{\n"
"    background-color: rgb(239, 217, 206);\n"
"}\n"
"QLineEdit\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 776, 446))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents_4)
        self.formLayout.setObjectName("formLayout")
        self.city_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.city_label.setObjectName("city_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.city_label)
        self.city_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.city_lineEdit.setObjectName("city_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.city_lineEdit)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()
        self.add_paths()
        self.add_websites()
        self.add_set()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Голосовой помощник «Зефир»"))
        self.output_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Привет! Меня зовут Зефир!</p><p align=\"center\">Произнеси команду с моим именем.</p></body></html>"))
        self.input_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.launch_Button.setText(_translate("MainWindow", "Пуск"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Запуск"))
        self.save_pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.telegram_label.setText(_translate("MainWindow", "Телеграм"))
        self.word_label.setText(_translate("MainWindow", "Word"))
        self.powerpoint_label.setText(_translate("MainWindow", "PowerPoint"))
        self.excel_label.setText(_translate("MainWindow", "Excel"))
        self.paint_label.setText(_translate("MainWindow", "Paint"))
        self.game_label.setText(_translate("MainWindow", "Игра"))
        self.terminal_label.setText(_translate("MainWindow", "Терминал"))
        self.calc_label.setText(_translate("MainWindow", "Калькулятор"))
        self.settings_label.setText(_translate("MainWindow", "Настройки"))
        self.calendar_label.setText(_translate("MainWindow", "Календарь"))
        self.notebook_label.setText(_translate("MainWindow", "Блокнот"))
        self.photo_label.setText(_translate("MainWindow", "Фото"))
        self.camera_label.setText(_translate("MainWindow", "Камера"))
        self.watch_label.setText(_translate("MainWindow", "Часы"))
        self.telegram_lineEdit.setText(_translate("MainWindow", "http///cvghbjnkml,kmjnhbgvfcdxc"))
        self.word_lineEdit.setText(_translate("MainWindow", "http///cvghbjnkml,kmjnhbgvfcdxc"))
        self.powerpoint_lineEdit.setText(_translate("MainWindow", "http///cvghbjnkml,kmjnhbgvfcdxc"))
        self.excel_lineEdit.setText(_translate("MainWindow", "http///cvghbjnkml,kmjnhbgvfcdxc"))
        self.paint_lineEdit.setText(_translate("MainWindow", "http///cvghbjnkml,kmjnhbgvfcdxc"))
        self.game_lineEdit.setText(_translate("MainWindow", "http///cvghbjnkml,kmjnhbgvfcdxc"))
        self.terminal_lineEdit.setText(_translate("MainWindow", "http///cvghbjnkml,kmjnhbgvfcdxc"))
        self.calc_lineEdit.setText(_translate("MainWindow", "http///cvghbjnkml,kmjnhbgvfcdxc"))
        self.settings_lineEdit.setText(_translate("MainWindow", "http///cvghbjnkml,kmjnhbgvfcdxc"))
        self.calendar_lineEdit.setText(_translate("MainWindow", "http///cvghbjnkml,kmjnhbgvfcdxc"))
        self.notebook_lineEdit.setText(_translate("MainWindow", "http///cvghbjnkml,kmjnhbgvfcdxc"))
        self.photo_lineEdit.setText(_translate("MainWindow", "http///cvghbjnkml,kmjnhbgvfcdxc"))
        self.camera_lineEdit.setText(_translate("MainWindow", "http///cvghbjnkml,kmjnhbgvfcdxc"))
        self.watch_lineEdit.setText(_translate("MainWindow", "http///cvghbjnkml,kmjnhbgvfcdxc"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Пути"))
        self.browser_label.setText(_translate("MainWindow", "Браузер"))
        self.mail_label.setText(_translate("MainWindow", "Почта"))
        self.youtube_label.setText(_translate("MainWindow", "Youtube"))
        self.vk_label.setText(_translate("MainWindow", "Vk"))
        self.kinopoisk_label.setText(_translate("MainWindow", "Kinopisk"))
        self.yandexmusic_label.setText(_translate("MainWindow", "Музыка"))
        self.wikipedia_label.setText(_translate("MainWindow", "Wikipedia"))
        self.ok_label.setText(_translate("MainWindow", "Одноклассники"))
        self.google_label.setText(_translate("MainWindow", "Google"))
        self.rambler_label.setText(_translate("MainWindow", "Rambler"))
        self.avito_label.setText(_translate("MainWindow", "Avito"))
        self.gismeteo_label.setText(_translate("MainWindow", "Gismeteo"))
        self.ozon_label.setText(_translate("MainWindow", "Ozon"))
        self.rbc_label.setText(_translate("MainWindow", "РБК"))
        self.yandexmarket_label.setText(_translate("MainWindow", "Яндекс Маркет"))
        self.gosuslugi_label.setText(_translate("MainWindow", "Госуслуги"))
        self.yandexeda_label.setText(_translate("MainWindow", "Яндекс Еда"))
        self.googletranslate_label.setText(_translate("MainWindow", "Переводчик"))
        self.save2_pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Ссылки"))
        self.save3_pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.city_label.setText(_translate("MainWindow", "Город"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Настройки"))

    def add_paths(self):
        try:
                self.telegram_lineEdit.setText(APP_PATHS['telegram'])
        except:
                self.telegram_lineEdit.setText('')
        try:
                self.calc_lineEdit.setText(APP_PATHS['calc'])
        except:
               self.calc_lineEdit.setText('')
        try:
                self.game_lineEdit.setText(APP_PATHS['game'])
        except:
               self.game_lineEdit.setText('')
        try:
                self.excel_lineEdit.setText(APP_PATHS['excel'])
        except:
               self.excel_lineEdit.setText('')
        try:
                self.paint_lineEdit.setText(APP_PATHS['paint'])
        except:
               self.paint_lineEdit.setText('')
        try:
                self.powerpoint_lineEdit.setText(APP_PATHS['powerpoint'])
        except:
               self.powerpoint_lineEdit.setText('')
        try:
                self.terminal_lineEdit.setText(APP_PATHS['terminal'])
        except:
               self.terminal_lineEdit.setText('')
        try:
                self.word_lineEdit.setText(APP_PATHS['word'])
        except:
               self.word_lineEdit.setText('')
        try:
                self.settings_lineEdit.setText(APP_PATHS['settings'])
        except:
               self.settings_lineEdit.setText('')
        try:
                self.calendar_lineEdit.setText(APP_PATHS['calendar'])
        except:
               self.calendar_lineEdit.setText('')
        try:
                self.notebook_lineEdit.setText(APP_PATHS['notebook'])
        except:
               self.notebook_lineEdit.setText('')
        try:
                self.photo_lineEdit.setText(APP_PATHS['photo'])
        except:
               self.photo_lineEdit.setText('')
        try:
                self.camera_lineEdit.setText(APP_PATHS['camera'])
        except:
               self.camera_lineEdit.setText('')
        try:
                self.watch_lineEdit.setText(APP_PATHS['watch'])
        except:
               self.watch_lineEdit.setText('')

    def add_websites(self):
        try:
                self.browser_lineEdit.setText(WEB_PATHS['browser'])
        except:
               self.browser_lineEdit.setText('')
        try:
                self.mail_lineEdit.setText(WEB_PATHS['mail'])
        except:
               self.mail_lineEdit.setText('')
        try:
                self.youtube_lineEdit.setText(WEB_PATHS['youtube'])
        except:
               self.youtube_lineEdit.setText('')
        try:
                self.vk_lineEdit.setText(WEB_PATHS['vk'])
        except:
               self.vk_lineEdit.setText('')
        try:
                self.kinopoisk_lineEdit.setText(WEB_PATHS['kinopoisk'])
        except:
               self.kinopoisk_lineEdit.setText('')
        try:
                self.yandexmusic_lineEdit.setText(WEB_PATHS['yandexmusic'])
        except:
               self.yandexmusic_lineEdit.setText('')
        try:
                self.wikipedia_lineEdit.setText(WEB_PATHS['wikipedia'])
        except:
               self.wikipedia_lineEdit.setText('')
        try:
                self.ok_lineEdit.setText(WEB_PATHS['ok'])
        except:
               self.ok_lineEdit.setText('')
        try:
                self.google_lineEdit.setText(WEB_PATHS['google'])
        except:
               self.google_lineEdit.setText('')
        try:
                self.rambler_lineEdit.setText(WEB_PATHS['rambler'])
        except:
               self.rambler_lineEdit.setText('')
        try:
                self.avito_lineEdit.setText(WEB_PATHS['avito'])
        except:
               self.avito_lineEdit.setText('')
        try:
                self.gismeteo_lineEdit.setText(WEB_PATHS['gismeteo'])
        except:
               self.gismeteo_lineEdit.setText('')
        try:
                self.ozon_lineEdit.setText(WEB_PATHS['ozon'])
        except:
               self.ozon_lineEdit.setText('')
        try:
                self.rbc_lineEdit.setText(WEB_PATHS['rbc'])
        except:
               self.rbc_lineEdit.setText('')
        try:
                self.yandexmarket_lineEdit.setText(WEB_PATHS['yandexmarket'])
        except:
               self.yandexmarket_lineEdit.setText('')
        try:
                self.gosuslugi_lineEdit.setText(WEB_PATHS['gosuslugi'])
        except:
               self.gosuslugi_lineEdit.setText('')
        try:
                self.yandexeda_lineEdit.setText(WEB_PATHS['yandexeda'])
        except:
               self.yandexeda_lineEdit.setText('')
        try:
                self.googletranslate_lineEdit.setText(WEB_PATHS['googletranslate'])
        except:
               self.googletranslate_lineEdit.setText('')

    def add_set(self):
        try:
                self.city_lineEdit.setText(SETTINGS['city'])
        except:
               self.city_lineEdit.setText('')

    def add_functions(self):
        self.launch_Button.clicked.connect(lambda: self.go())
        self.save_pushButton.clicked.connect(lambda: save_apps(self))
        self.save2_pushButton.clicked.connect(lambda: save_webs(self))
        self.save3_pushButton.clicked.connect(lambda: save_settings(self))

    def go(self):
        if active_count() == 1:
                t = Thread(target=speech_processing.main, args=(self,))
                t.start()
                self.launch_Button.setText("Стоп")
                self.launch_Button.setStyleSheet("QPushButton\n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(140, 104, 113);\n"
"    font: 14pt \"Comic Sans MS\";\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(177, 149, 158);\n"
"}")
        else:
              self.flag = False
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


if __name__ == "__main__":
    import sys
    import ctypes
    myappid='mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('./icons/bot.png'))
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon('./icons/bot.png'))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

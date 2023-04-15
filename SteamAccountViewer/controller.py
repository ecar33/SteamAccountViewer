from PyQt5.QtWidgets import *
from view import *
import datetime
import pytz
import time
import threading
import math

QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.clock()
        self.reset_pushButton.clicked.connect(lambda: self.reset())
        self.pushButton_page_1.clicked.connect(self.next_page)
        self.pushButton_page_2.clicked.connect(self.next_page)

        self.add_pushButton.clicked.connect(lambda: self.determine_function())
        self.subtract_pushButton.clicked.connect(lambda: self.determine_function())
        self.multiply_pushButton.clicked.connect(lambda: self.determine_function())
        self.divide_pushButton.clicked.connect(lambda: self.determine_function())

        self.exponent_pushButton.clicked.connect(lambda: self.determine_function())
        self.gcd_pushButton.clicked.connect(lambda: self.determine_function())
        self.modulo_pushButton.clicked.connect(lambda: self.determine_function())
        self.percent_pushButton.clicked.connect(lambda: self.determine_function())


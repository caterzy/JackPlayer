# This Python file uses the following encoding: utf-8
__author__ = 'JackRao'


import  sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle('JackRao')
win.show()

sys.exit(app.exec_())
# This Python file uses the following encoding: utf-8
__author__ = 'JackRao'


import  sys
from PyQt5.QtWidgets import *

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.iniUI()

    def iniUI(self):
        self.setWindowTitle("JackRap")
        self.statusBar().showMessage("状态栏")
        self.resize(400, 300)

        menu = self.menuBar()
        file_menu = menu.addMenu("文件")
        new_action = QAction('new file', self)
        new_action.setStatusTip('open new file')
        file_menu.addAction(new_action)
        exit_action = QAction("quit", self)
        exit_action.setStatusTip("quit app")
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut('Ctrl+Q')
        file_menu.addAction(exit_action)
        
        file_menu.addSeparator()
        file_menu = menu.addMenu("修改")

def main():
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())

main()
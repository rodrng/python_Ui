import sys

import googletrans
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

form_class = uic.loadUiType('ui/calculator.ui')[0] #ui 불러오기

class calculator_App(QMainWindow, form_class):
    def __init__(self): #초기화자
        super().__init__()
        self.setupUi(self) #만들어놓은 test.ui 연결
        self.setWindowTitle('한줄 번역기') # 윈도우 제목 설정
        self.setWindowIcon(QIcon('img/google-logo.png')) # 윈도우 아이콘 설정
        self.statusBar().showMessage('calculator Application Ver 1.0') # 윈도우 상태표시줄 입력
        self.btn_0.clicked.connect(self.calculator_button_clicked)
        self.btn_1.clicked.connect(self.calculator_button_clicked)
        self.btn_2.clicked.connect(self.calculator_button_clicked)
        self.btn_3.clicked.connect(self.calculator_button_clicked)
        self.btn_4.clicked.connect(self.calculator_button_clicked)
        self.btn_5.clicked.connect(self.calculator_button_clicked)
        self.btn_6.clicked.connect(self.calculator_button_clicked)
        self.btn_7.clicked.connect(self.calculator_button_clicked)
        self.btn_8.clicked.connect(self.calculator_button_clicked)
        self.btn_9.clicked.connect(self.calculator_button_clicked)
        # self.btn_add.clicked.connect(self.calculator_button_clicked)
        # self.btn_sub.clicked.connect(self.calculator_button_clicked)
        # self.btn_mul.clicked.connect(self.calculator_button_clicked)
        # self.btn_div.clicked.connect(self.calculator_button_clicked)
        # self.btn_result.clicked.connect(self.calculator_button_clicked)
        self.btn_claer.clicked.connect(self.claer)

    def calculator_button_clicked(self):
        btn_0 = input('첫번째 클릭한 숫자:')
        self.label.setText(btn_0)

    # cal = ''
    #
    # num1 = input('첫번째 클릭한 숫자:')
    # cal = cal + num1
    # # print(cal)
    # oper1 = input('사칙연산자:')
    # cal = cal + oper1
    # # print(cal)
    # num2 = input('두번째 클릭한 숫자:')
    # cal = cal + num2
    #
    # # print(cal)
    #
    # result = eval(cal)
    # print(f"{cal}={result}")

    def claer(self):
        self.btn_claer.clear()


app = QApplication(sys.argv)
window = calculator_App()
window.show()
app.exec_()
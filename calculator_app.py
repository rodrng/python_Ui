import sys

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

        num = [self.btn_0, self.btn_1, self.btn_2, self.btn_3, self.btn_4,
               self.btn_5, self.btn_6, self.btn_7, self.btn_8, self.btn_9]
        for number in num:
            number.clicked.connect(self.Nums)
        # self.btn_0.clicked.connect(self.btn_0_clicked)
        # self.btn_1.clicked.connect(self.btn_1_clicked)
        # self.btn_2.clicked.connect(self.btn_2_clicked)
        # self.btn_3.clicked.connect(self.btn_3_clicked)
        # self.btn_4.clicked.connect(self.btn_4_clicked)
        # self.btn_5.clicked.connect(self.btn_5_clicked)
        # self.btn_6.clicked.connect(self.btn_6_clicked)
        # self.btn_7.clicked.connect(self.btn_7_clicked)
        # self.btn_8.clicked.connect(self.btn_8_clicked)
        # self.btn_9.clicked.connect(self.btn_9_clicked)
        self.btn_add.clicked.connect(self.btn_add_clicked)
        self.btn_sub.clicked.connect(self.btn_sub_clicked)
        self.btn_mul.clicked.connect(self.btn_mul_clicked)
        self.btn_div.clicked.connect(self.btn_div_clicked)
        self.btn_result.clicked.connect(self.btn_result_clicked)
        self.btn_claer.clicked.connect(self.claer)

    def Nums(self):
        sender = self.sender()
        num_str = sender.text()
        if self.label.text() == '0':
            self.label.setText(num_str)
        else:
            self.label.setText(self.label.text() + num_str)

    def btn_result_clicked(self):
        cal = self.label.text()

        result = eval(cal)
        self.label.setText(str(result))
        # print(f"{cal}={result}")

    def btn_add_clicked(self):
        if self.label.text() == '0':
            self.label.setText('Error// Press Clear Button')
        else:
            self.label.setText(self.label.text() + ' + ')
    def btn_sub_clicked(self):
        if self.label.text() == '0':
            self.label.setText('Error// Press Clear Button')
        else:
            self.label.setText(self.label.text() + ' - ')
    def btn_mul_clicked(self):
        if self.label.text() == '0':
            self.label.setText('Error// Press Clear Button')
        else:
            self.label.setText(self.label.text() + ' * ')
    def btn_div_clicked(self):
        if self.label.text() == '0':
            self.label.setText('Error// Press Clear Button')
        else:
            self.label.setText(self.label.text() + ' / ')

    def claer(self):
        self.label.clear()

    # def calculator_button_clicked(self):
    # def btn_0_clicked(self):
    #     self.label.setText('0')
    # def btn_1_clicked(self):
    #     self.label.setText('1')
    # def btn_2_clicked(self):
    #     self.label.setText('2')
    # def btn_3_clicked(self):
    #     self.label.setText('3')
    # def btn_4_clicked(self):
    #     self.label.setText('4')
    # def btn_5_clicked(self):
    #     self.label.setText('5')
    # def btn_6_clicked(self):
    #     self.label.setText('6')
    # def btn_7_clicked(self):
    #     self.label.setText('7')
    # def btn_8_clicked(self):
    #     self.label.setText('8')
    # def btn_9_clicked(self):
    #     self.label.setText('9')
    # def btn_add_clicked(self):
    #     self.label.setText('＋')
    # def btn_sub_clicked(self):
    #     self.label.setText('－')
    # def btn_mul_clicked(self):
    #     self.label.setText('×')
    # def btn_div_clicked(self):
    #     self.label.setText('÷')
    # def btn_result_clicked(self):
    #     self.label.setText('=')


app = QApplication(sys.argv)
window = calculator_App()
window.show()
app.exec_()
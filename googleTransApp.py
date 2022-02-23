import sys

import googletrans
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

form_class = uic.loadUiType('ui/google_trans.ui')[0] #ui 불러오기

class TransApp(QMainWindow, form_class):
    def __init__(self): #초기화자
        super().__init__()
        self.setupUi(self) #만들어놓은 test.ui 연결
        self.setWindowTitle('한줄 번역기') # 윈도우 제목 설정
        self.setWindowIcon(QIcon('img/google-logo.png')) # 윈도우 아이콘 설정
        self.statusBar().showMessage('Google Trans Application Ver 1.0') # 윈도우 상태표시줄 입력
        self.push_btn.clicked.connect(self.trans_button_clicked)
        self.clear_btn.clicked.connect(self.clear_text)

    def trans_button_clicked(self):
        trans_txt = self.txt_ko.text() # 입력된 문자열 가져오기
        trans = googletrans.Translator()

        ret1 = trans.translate(trans_txt, dest='en') # 영어 번역 결과
        ret2 = trans.translate(trans_txt, dest='ja') # 일본어 번역 결과
        ret3 = trans.translate(trans_txt, dest='zh-cn') # 중국어 번역 결과

        self.txt_en.setText(ret1.text)
        self.txt_jp.setText(ret2.text)
        self.txt_cn.setText(ret3.text)


    def clear_text(self):
        self.txt_ko.clear()
        self.txt_en.clear()
        self.txt_jp.clear()
        self.txt_cn.clear()



app = QApplication(sys.argv)
window = TransApp()
window.show()
app.exec_()
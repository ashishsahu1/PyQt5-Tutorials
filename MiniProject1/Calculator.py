from typing import Container
import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setLayout(qtw.QVBoxLayout())
        # btn1 = qtw.QPushButton('test')
        # btn2 = qtw.QPushButton('test')
        # self.layout().addWidget(btn1)
        # self.layout().addWidget(btn2)

        self.keypad()

        self.show()
    def keypad(self):
        container= qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        resultField = qtw.QLineEdit()
        btnResult = qtw.QPushButton('Enter')
        btnClear = qtw.QPushButton('Clear')
        btn9 = qtw.QPushButton('9')
        btn8 = qtw.QPushButton('8')
        btn7 = qtw.QPushButton('7')
        btn6 = qtw.QPushButton('6')
        btn5 = qtw.QPushButton('5')
        btn4 = qtw.QPushButton('4')
        btn3 = qtw.QPushButton('3')
        btn2 = qtw.QPushButton('2')
        btn1 = qtw.QPushButton('1')
        btn0 = qtw.QPushButton('0')
        btnAdd = qtw.QPushButton('+')
        btnSub = qtw.QPushButton('-')
        btnMul = qtw.QPushButton('*')
        btnDiv = qtw.QPushButton('/')

        #adding the buttons to the layout
        container.layout().addWidget(resultField,0,0,)


app = qtw.QApplication([])
mw =  MainWindow()

app.exec_()
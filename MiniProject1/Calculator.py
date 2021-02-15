from typing import Container
import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(500,300,500,300)
        self.setLayout(qtw.QVBoxLayout())

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
        container.layout().addWidget(resultField,0,0,1,4)
        container.layout().addWidget(btnResult,1,0,1,2)
        container.layout().addWidget(btnClear,1,2,1,2)
        container.layout().addWidget(btn9,2,0)
        container.layout().addWidget(btn8,2,1)
        container.layout().addWidget(btn7,2,2)
        container.layout().addWidget(btnAdd,2,3)
        container.layout().addWidget(btn6,3,0)
        container.layout().addWidget(btn5,3,1)
        container.layout().addWidget(btn4,3,2)
        container.layout().addWidget(btnSub,3,3)
        container.layout().addWidget(btn3,4,0)
        container.layout().addWidget(btn2,4,1)
        container.layout().addWidget(btn1,4,2)
        container.layout().addWidget(btnMul,4,3)
        container.layout().addWidget(btn0,5,0,1,3)
        container.layout().addWidget(btnDiv,5,3)


        self.layout().addWidget(container)


app = qtw.QApplication([])
mw =  MainWindow()

app.exec_()
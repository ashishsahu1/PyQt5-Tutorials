from typing import Container
import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(500,300,500,300)
        self.setLayout(qtw.QVBoxLayout())

        self.keypad()
        self.tempNums = []
        self.finNums = []

        self.show()

    def keypad(self):
        container= qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        self.resultField = qtw.QLineEdit()
        btnResult = qtw.QPushButton('Enter',clicked = lambda:self.resultField.setText('Test') )
        btnClear = qtw.QPushButton('Clear', clicked = lambda:self.resultField.setText(''))
        btn9 = qtw.QPushButton('9', clicked = lambda:self.numPress('9'))
        btn8 = qtw.QPushButton('8', clicked = lambda:self.numPress('8'))
        btn7 = qtw.QPushButton('7', clicked = lambda:self.numPress('7'))
        btn6 = qtw.QPushButton('6', clicked = lambda:self.numPress('6'))
        btn5 = qtw.QPushButton('5', clicked = lambda:self.numPress('5'))
        btn4 = qtw.QPushButton('4', clicked = lambda:self.numPress('4'))
        btn3 = qtw.QPushButton('3', clicked = lambda:self.numPress('3'))
        btn2 = qtw.QPushButton('2', clicked = lambda:self.numPress('2'))
        btn1 = qtw.QPushButton('1', clicked = lambda:self.numPress('1'))
        btn0 = qtw.QPushButton('0', clicked = lambda:self.numPress('0'))
        btnAdd = qtw.QPushButton('+', clicked = lambda:self.funPress('+'))
        btnSub = qtw.QPushButton('-', clicked = lambda:self.funPress('-'))
        btnMul = qtw.QPushButton('*', clicked = lambda:self.funPress('*'))
        btnDiv = qtw.QPushButton('/',clicked = lambda:self.funPress('/'))

        #adding the buttons to the layout
        container.layout().addWidget(self.resultField,0,0,1,4)
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
    
    def numPress(self,key):
        self.tempNums.append((key))
        tempStr = ''.join(self.tempNums)
        if self.finNums:
            self.resultField.setText(''.join(self.finNums)+tempStr)
        else:
            self.resultField.setText(tempStr)

    def funPress(self,operator):
        tempStr = ''.join(self.tempNums)
        self.finNums.append(tempStr)
        

app = qtw.QApplication([])
mw =  MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))

app.exec_()
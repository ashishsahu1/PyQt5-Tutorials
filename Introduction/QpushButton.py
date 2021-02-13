from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
import sys
from PyQt5.QtGui import QIcon

'''
How to make or create a button in pyqt5?
We can create using a class known as QPushButton
'''


#driver class
class WindowExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,400,300)
        self.setWindowTitle("First Title")
        self.setWindowIcon(QIcon("../Images/design.png"))

        self.createButtons()

        self.show()

    def createButtons(self):
        btn1 = QPushButton("Click me",self)
        # btn1.move(200,200)
        btn1.setGeometry(50,50,100,100)
        btn1.setStyleSheet('background-color:Blue')

        btn2 = QPushButton("Click me",self)
        btn2.setGeometry(100,100,100,100)
        btn2.setIcon(QIcon('../Images/design.png'))

        

#creating our application
app = QApplication(sys.argv)

#creating window
window = WindowExample()

#event loop
sys.exit(app.exec_())
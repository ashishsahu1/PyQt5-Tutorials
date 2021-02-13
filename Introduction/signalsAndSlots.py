#Signal : signals are used to communicate between two objects
#it is a method of action

#slot: a function which is defined with the event that the button has to perform
#signal: connection between button and slot

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
        btn1 = QPushButton("Button1",self)
        # btn1.move(200,200)
        btn1.setGeometry(50,50,100,100)
        # btn1.setStyleSheet('background-color:Blue')
        btn1.clicked.connect(self.clickedBTN)

        btn2 = QPushButton("Button2",self)
        # btn1.move(200,200)
        btn2.setGeometry(150,50,100,100)
        # btn1.setStyleSheet('background-color:Blue')
        btn2.clicked.connect(self.clickedBTN2)

    #creeating slot
    def clickedBTN(self):
        print("Button 1 clicked")

    def clickedBTN2(self):
        print("Button 2 clicked")
        

#creating our application
app = QApplication(sys.argv)

#creating window
window = WindowExample()

#event loop
sys.exit(app.exec_())
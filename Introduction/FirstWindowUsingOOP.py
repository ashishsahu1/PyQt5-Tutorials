from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5.QtGui import QIcon

#driver class
class WindowExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,400,300)
        self.setWindowTitle("First Title")
        self.setWindowIcon(QIcon("../Images/design.png"))

        # self.setFixedHeight(400)
        # self.setFixedWidth(300)
        self.setWindowOpacity(0.95)
        self.setStyleSheet('background-color:#2A1E70')
        self.show()

#creating our application
app = QApplication(sys.argv)

#creating window
window = WindowExample()

#event loop
sys.exit(app.exec_())
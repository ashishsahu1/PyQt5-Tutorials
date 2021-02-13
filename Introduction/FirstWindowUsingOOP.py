from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5.QtGui import QIcon

#driver class
class WindowExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,400,300)
        self.setWindowTitle("First Title")
        self.show()

#creating our application
app = QApplication(sys.argv)

#creating window
window = WindowExample()

#event loop
sys.exit(app.exec_())
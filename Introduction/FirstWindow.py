import sys
from PyQt5.QtWidgets import QApplication, QWidget


#creating application
#object of QApplication
# app = QApplication([])
app = QApplication(sys.argv)

#there are three types, one of them being QWidget
#they are QWidget : main widget management , QDialog: dialog are short interaction window, QMainwindow
window = QWidget()
#show() helps us to show the windows
window.show()

#event loop
app.exec_()
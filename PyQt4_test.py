import sys
from PyQt5 import QtWidgets, QtGui


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQt!")
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.show()


app = QtWidgets.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())

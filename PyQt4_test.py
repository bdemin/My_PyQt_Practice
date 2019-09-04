import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQt!")
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.home()

    def home(self):
        btn =  QtWidgets.QPushButton('Quit', self)
        # btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.clicked.connect(self.close_application)
        
        btn.resize(btn.minimumSizeHint())
        btn.move(0, 0)

        self.show()

    def close_application(self):
        print('Application Terminated')
        sys.exit()


def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()

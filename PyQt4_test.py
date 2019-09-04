import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
window.setGeometry(50, 50, 500, 300)
window.setWindowTitle('Blah')

window.show()

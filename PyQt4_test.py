import sys

from PyQt5 import QtWidgets, QtGui, QtCore


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('PyQt!')
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        extractAction = QtWidgets.QAction('&GET TO THE CHOPPAH!', self)
        extractAction.setShortcut('Ctrl + Q')
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        openEditor = QtWidgets.QAction('&Editor', self)
        openEditor.setShortcut('Ctrl + E')
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)

        openFile = QtWidgets.QAction('&Open File', self)
        openFile.setShortcut('Ctrl + O')
        openFile.setStatusTip('Open Editor')
        openFile.triggered.connect(self.editor)
        
        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        
        editorMenu = mainMenu.addMenu('&Editor')
        editorMenu.addAction(openEditor)

        self.home()


    def home(self):
        btn =  QtWidgets.QPushButton('Quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(100, 100)

        extractAction = QtWidgets.QAction(QtGui.QIcon('icon.png'), 'Quit the application!', self)
        extractAction.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar('Action')
        self.toolBar.addAction(extractAction)

        fontChoice = QtWidgets.QAction('Font', self)
        fontChoice.triggered.connect(self.font_choice)
        self.toolBar.addAction(fontChoice)

        color = QtGui.QColor(0, 0, 0)
        fontColor = QtWidgets.QAction('Font BG Color', self)
        fontColor.triggered.connect(self.color_picker)
        self.toolBar.addAction(fontColor)

        checkBox = QtWidgets.QCheckBox('Enlarge Window', self)
        checkBox.move(300, 15)
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn = QtWidgets.QPushButton('Download', self)
        self.btn.move(200, 120)
        self.btn.clicked.connect(self.download)

        print(self.style().objectName())
        self.styleChoice = QtWidgets.QLabel('Windows', self)

        comboBox = QtWidgets.QComboBox(self)
        comboBox.addItem('motif')
        comboBox.addItem('Windows')
        comboBox.addItem('cde')
        comboBox.addItem('Plastique')
        comboBox.addItem('Cleanlooks')
        comboBox.addItem('windowsvista')

        comboBox.move(50, 250)
        self.styleChoice.move(50, 150)
        comboBox.activated[str].connect(self.style_choice)

        cal = QtWidgets.QCalendarWidget(self)
        cal.move(500, 200)
        cal.resize(200, 200)

        self.show()
    

    def editor(self):
        self.textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)


    def color_picker(self):
        color = QtWidgets.QColorDialog.getColor()
        self.styleChoice.setStyleSheet('QWidget {background-color: %s}' % color.name())
   
   
    def font_choice(self):
        font, valid = QtWidgets.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)
    
    
    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(text))


    def download(self):
        self.completed = 0
        
        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)


    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)


    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self, 'Exit Window', 'Exit the app?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            print('Quitting Now')
            sys.exit()
        else:
            pass
                                                    

def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()

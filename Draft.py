import sys

from PyQt5 import uic, QtGui

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QLabel, QFileDialog

from PyQt5.QtGui import QPixmap, QIcon, QPalette, QImage

from PyQt5.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('qt_1.ui')
        self.ui.setWindowTitle('Employee Selection')
        self.experience_1_box = self.ui.age_from
        self.exp1  = self.experience_1_box.value()
        self.exp1 += 1
        print(self.exp1)
        self.ui.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

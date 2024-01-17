from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class UiWindowQt(QMainWindow):

    def __init__(self):
        super(UiWindowQt, self).__init__()

        self.setObjectName("window_qt")

        self.resize(476, 300)

        self.button = QtWidgets.QPushButton(self)

        self.button.setGeometry(QtCore.QRect(254, 242, 131, 41))

        font = QtGui.QFont()

        font.setPointSize(10)

        font.setBold(False)

        font.setItalic(False)

        font.setUnderline(False)

        font.setWeight(50)

        font.setStrikeOut(False)

        self.button.setFont(font)

        self.button.setObjectName("button")

        self.text = QtWidgets.QLabel(self)

        self.text.setGeometry(QtCore.QRect(30, 30, 341, 41))

        font = QtGui.QFont()

        font.setPointSize(12)

        self.text.setFont(font)

        self.text.setObjectName("text")

        self.retranslate_ui(self)

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self, window_qt):
        _translate = QtCore.QCoreApplication.translate

        window_qt.setWindowTitle(_translate("window_qt", "Окно"))

        self.button.setText(_translate("window_qt", "PushButton"))

        self.text.setText(_translate("window_qt", "TextLabel"))


def application():
    app = QApplication(sys.argv)

    window = UiWindowQt()

    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    w.resize(250, 150)

    w.move(300, 300)

    w.setWindowTitle('Окно')

    w_text = QLabel(w)

    w_text.setText('Первая запись')

    w_text.move(10, 10)

    w_text.adjustSize()

    w.show()

    sys.exit(app.exec_())
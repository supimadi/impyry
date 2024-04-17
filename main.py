import sys
import os

from PyQt5.QtWidgets import QApplication

import qdarktheme

from impyry import MainWindow

def main():
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

    app = QApplication([])

    ex = MainWindow()
    ex.show()

    app.setStyleSheet(qdarktheme.load_stylesheet("light"))

    sys.exit(app.exec())


if __name__ == '__main__':
    main()

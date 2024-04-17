import typing


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QFileDialog, QLabel, QMainWindow, QPushButton,
    QTextEdit, QVBoxLayout, QWidget
)


class MainWindow(QMainWindow):
    def __init__(self, parent: typing.Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Impyry | Image to Python Binary Converter")

        self._layout = QVBoxLayout()

        self._container = QWidget()
        self._container.setLayout(self._layout)

        headline = QLabel("Image to Python Binary Converter")
        headline.setFont(QFont("Arial", 12))
        headline.setAlignment(Qt.AlignCenter) # type: ignore

        self.text_box = QTextEdit()
        self.convert_btn = QPushButton("Convert Images")

        self.file_dialog = QFileDialog(self, "Open Images", "", "Image Files (*.png *.jpg *.bmp *.svg *.jpeg)")

        self._layout.addSpacing(50)
        self._layout.addWidget(headline)
        self._layout.addSpacing(40)

        self._layout.addWidget(self.convert_btn)
        self._layout.addWidget(self.text_box)

        self.setCentralWidget(self._container)

    def process_images(self):
        pass

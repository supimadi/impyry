import os
import typing

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QFileDialog, QLabel, QMainWindow, QMessageBox, QPushButton,
    QTextEdit, QVBoxLayout, QWidget
)


class MainWindow(QMainWindow):
    def __init__(self, parent: typing.Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Impyry | Image to Python Binary Converter")
        self.setMinimumSize(320, 200)

        self._layout = QVBoxLayout()

        self._container = QWidget()
        self._container.setLayout(self._layout)

        headline = QLabel("Image to Python Binary Converter")
        headline.setFont(QFont("Arial", 12))
        headline.setAlignment(Qt.AlignCenter) # type: ignore

        self.file_dialog = QFileDialog(self)
        self.file_dialog.setFileMode(QFileDialog.ExistingFiles)

        self.convert_btn = QPushButton("Convert Images")
        self.convert_btn.clicked.connect(self.process_images)

        self._layout.addWidget(headline)
        self._layout.addWidget(self.convert_btn)
        self._layout.addStretch()

        self.setCentralWidget(self._container)

    def process_images(self):
        open_dialog = lambda: self.file_dialog.getOpenFileNames(self, "Open Images", "", "Image Files (*.png *.jpg *.bmp *.svg *.jpeg)")[0]

        image_path: list[str]  = open_dialog()
        image_buffer: list[str] = []

        for ip in image_path:
            image_name: str = ip.split("/")[-1].split(".")[0]

            try:
                int(image_name)
                continue
            except ValueError:
                pass

            with open(ip, "rb") as f:
                image_buffer.append(f"{image_name} = {f.read()}")

        if not os.path.exists("result"):
            os.makedirs("result")

        with open(f"result/image_assets.py", "w") as f:
            for image in image_buffer:
                f.write(f"{image}\n")

        QMessageBox.information(self, "Sucess Convert Image", "Successfully Convert Image to Python Binary")


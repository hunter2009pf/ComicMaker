from PySide6.QtWidgets import (
    QLabel,
    QWidget,
    QVBoxLayout,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from utils.log_util import logger


class ImgAboveTitle(QWidget):
    def __init__(
        self, project_path: str, img_path: str, title: str, click_callback=None
    ):
        super().__init__()
        self.project_path = project_path
        self.img_path = img_path
        self.title = title
        self.click_callback = click_callback
        self.initUI()

    def initUI(self):
        self.layout: QVBoxLayout = QVBoxLayout(self)
        # create a QPixmap to show the image
        pixmap = QPixmap(self.img_path)
        img_label = QLabel(self)
        img_label.setPixmap(pixmap)
        img_label.setFixedSize(200, 320)
        img_label.setScaledContents(True)

        # create a QLabel to show the title
        label = QLabel(self.title, self)

        label.setFixedSize(200, 40)

        # set the alignment of the QLabel to be centered
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # set the font of the QLabel to be bold
        label.setStyleSheet("font-weight: bold;")

        # set the font size of the QLabel to be 20
        label.setStyleSheet("font-size: 20px;")

        # set the background color of the QLabel to be white
        label.setStyleSheet("background-color: white;")

        # 为图片的 QLabel 添加点击事件
        img_label.mousePressEvent = self.on_click
        label.mousePressEvent = self.on_click

        self.layout.addWidget(img_label)
        # add the QLabel to the layout
        self.layout.addWidget(label)

    def on_click(self, event):
        logger.info(f"Clicked on {self.title}")
        if self.click_callback:
            self.click_callback(self.project_path, self.title)

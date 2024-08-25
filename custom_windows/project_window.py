from PySide6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QLabel,
)


class ProjectWindow(QMainWindow):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self, title: str = "New Project", project_path: str = ""):
        super().__init__()
        self.project_path = project_path
        self.setWindowTitle(title)
        # maxmize the window
        self.showMaximized()
        self.label = QLabel(f"Project Path: {self.project_path}")

        # set the font of the QLabel to be bold
        self.label.setStyleSheet("font-weight: bold;")

        # set the font size of the QLabel to be 20
        self.label.setStyleSheet("font-size: 120px;")

        # set the background color of the QLabel to be white
        self.label.setStyleSheet("background-color: white;")

        self.setCentralWidget(self.label)

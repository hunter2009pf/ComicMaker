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

    def __init__(self, title: str = "New Project"):
        super().__init__()
        self.setWindowTitle(title)
        # maxmize the window
        self.showMaximized()
        layout = QVBoxLayout()
        self.label = QLabel("New Project")
        layout.addWidget(self.label)
        self.setLayout(layout)

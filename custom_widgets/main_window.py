from PySide6.QtWidgets import (
    QMainWindow, 
    QPushButton,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)

from constants.fixed_strs import MainWindowConfig


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(MainWindowConfig.TITLE)

        # set up the default size of the main window
        self.resize(MainWindowConfig.WIDTH, MainWindowConfig.HEIGHT)

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked)
        self.button.clicked.connect(self.button_toggled)

        # Set the central widget of the Window.
        # self.setCentralWidget(self.button)

        self.label = QLabel("Hello World")
        self.input = QLineEdit()
        self.input .textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def button_clicked(self):
        print("Button clicked")
        self.button.setText("You already clicked me!")
        self.button.setEnabled(False)
        self.setWindowTitle("Button clicked")

    def button_toggled(self, checked):
        print("Button toggled:", checked)
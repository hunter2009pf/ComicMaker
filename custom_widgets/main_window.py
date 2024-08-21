from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QWidget,
)
from PySide6.QtGui import QAction, QPalette, QColor

from constants.fixed_strs import MainWindowConfig


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(MainWindowConfig.TITLE)

        # set up the default size of the main window
        self.resize(MainWindowConfig.WIDTH, MainWindowConfig.HEIGHT)

        # label = QLabel("你好，世界！")
        # font = label.font()
        # font.setPointSize(30)
        # label.setFont(font)
        # label.setAlignment(
        #     Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        # )

        
        # layout1 = QHBoxLayout()
        # layout2 = QVBoxLayout()
        # layout3 = QVBoxLayout()

        # layout1.setContentsMargins(0, 0, 0, 0)
        # layout1.setSpacing(20)

        # layout2.addWidget(Color('red'))
        # layout2.addWidget(Color('yellow'))
        # layout2.addWidget(Color('purple'))

        # layout1.addLayout( layout2 )

        # layout1.addWidget(Color('green'))

        # layout3.addWidget(Color('red'))
        # layout3.addWidget(Color('purple'))

        # layout1.addLayout( layout3 )

        layout = QGridLayout()

        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('green'), 1, 0)
        layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(Color('purple'), 2, 1)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        # self.button = QPushButton("Press Me!")
        # self.button.setCheckable(True)
        # self.button.clicked.connect(self.button_clicked)
        # self.button.clicked.connect(self.button_toggled)

        # Set the central widget of the Window.
        # self.setCentralWidget(self.button)

        # self.label = QLabel("Hello World")
        # self.input = QLineEdit()
        # self.input .textChanged.connect(self.label.setText)

        # layout = QVBoxLayout()
        # layout.addWidget(self.input)
        # layout.addWidget(self.label)

        # container = QWidget()
        # container.setLayout(layout)
        # self.setCentralWidget(container)
    
    def button_clicked(self):
        print("Button clicked")
        self.button.setText("You already clicked me!")
        self.button.setEnabled(False)
        self.setWindowTitle("Button clicked")

    def button_toggled(self, checked):
        print("Button toggled:", checked)

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())
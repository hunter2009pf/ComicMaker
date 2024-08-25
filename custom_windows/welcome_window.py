import os
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
    QToolBar,
    QMenu,
    QScrollArea,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QWidget,
)
from PySide6.QtGui import QAction, QPalette, QColor

from beans.comic_info import ComicInfo
from config.settings import PROJECT_ROOT_PATH
from constants.fixed_strs import MainWindowConfig
from custom_windows.project_window import ProjectWindow
from custom_widgets.img_above_title import ImgAboveTitle
from utils.log_util import logger
from utils.path_util import PathUtil


# Subclass QMainWindow to customize your application's main window
class WelcomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(MainWindowConfig.TITLE)
        # set up the default size of the main window
        self.resize(MainWindowConfig.WIDTH, MainWindowConfig.HEIGHT)
        # set up grid layout in a scrollable area
        self.scroll_area = QScrollArea(self)  # 创建滚动区域
        self.scroll_area.setWidgetResizable(True)  # 允许调整大小以适应内容
        self.grid_widget = QWidget(self)  # 创建一个QWidget作为网格布局的容器
        self.grid_layout = QGridLayout(self.grid_widget)  # 创建网格布局

        it = ImgAboveTitle(
            project_path="",
            img_path=PathUtil.get_path("assets/images/img_add.png"),
            title="创建新漫画",
            click_callback=self.create_new_project,
        )
        self.grid_layout.addWidget(it, 0, 0)
        # read existing projects from the project folder
        projects: list[ComicInfo] = []
        # get all directories in the project folder
        for directory in os.listdir(PROJECT_ROOT_PATH):
            logger.info(f"Processing directory: {directory}")
            ci = ComicInfo(
                project_name=directory,
                comic_cover_img_path=PathUtil.get_path(
                    relative_path="./assets/images/default_cover.png"
                ),
                project_path=PROJECT_ROOT_PATH + os.path.sep + directory,
            )
            cover_img_path = (
                PROJECT_ROOT_PATH
                + os.path.sep
                + directory
                + os.path.sep
                + "cover_image"
                + os.path.sep
                + "cover0.png"
            )
            if os.path.exists(cover_img_path):
                ci.comic_cover_img_path = cover_img_path
            projects.append(ci)
        length = len(projects)
        if length > 0:
            column = 3
            length += 1
            if length % column == 0:
                row = length // column
            else:
                row = length // column + 1
            for i in range(row):
                for j in range(column):
                    if i * column + j >= length:
                        break
                    if i == 0 and j == 0:
                        continue
                    item = ImgAboveTitle(
                        project_path=projects[i * column + j - 1].project_path,
                        img_path=projects[i * column + j - 1].comic_cover_img_path,
                        title=projects[i * column + j - 1].project_name,
                        click_callback=self.open_old_project,
                    )
                    self.grid_layout.addWidget(item, i, j)
        # for row in range(20):  # 假设有20行
        #     for column in range(10):  # 每行10个标签
        #         label = QLabel(f"Item {row},{column}", self)
        #         self.grid_layout.addWidget(label, row, column)

        self.grid_widget.setLayout(self.grid_layout)  # 为QWidget设置布局
        self.scroll_area.setWidget(self.grid_widget)  # 将QWidget设置为滚动区域的子控件

        self.scroll_area.resize(300, 300)  # 设置滚动区域的尺寸
        self.setCentralWidget(self.scroll_area)  # 将滚动区域设置为QWidget的布局

    def create_new_project(self, project_path: str, project_name: str):
        logger.info(f"create new project!")

    def open_old_project(self, project_path: str, project_name: str):
        self.w = ProjectWindow(
            title=project_name,
            project_path=project_path,
        )
        self.w.show()
        self.hide()

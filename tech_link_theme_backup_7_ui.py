# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tech_link_theme_backup_7.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QButtonGroup, QComboBox, QDateTimeEdit, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
from marquee_label import MarqueeLabel
from qtime_only_edit import TimeOnlyEdit
import Icon_rc
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1221, 950)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Icons/Logo_Cty_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0 #eaebeb,\n"
"    stop:1 #dfe1e5);\n"
"}\n"
"QComboBox {\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"    padding-left: 20px;\n"
"    background-color: white;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QComboBox:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 30px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    border-top: 6px solid #64748B;\n"
"    margin-right: 8px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #E5E5E5;\n"
"    border-radius: 6px;\n"
"    background-color: white;\n"
"    selection-background-color: #0AB1F9;\n"
"    selection-color: black;\n"
"    padding: 4px;\n"
"}")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1024, 800))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        sizePolicy.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy)
        self.header_frame.setMinimumSize(QSize(0, 60))
        self.header_frame.setMaximumSize(QSize(16777215, 60))
        self.header_frame.setStyleSheet(u"QFrame {\n"
"    background-color: white;\n"
"\n"
"    border: none;\n"
"}")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 5, 5, 5)
        self.label_2 = QLabel(self.header_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 0))
        self.label_2.setMaximumSize(QSize(60, 16777215))
        self.label_2.setStyleSheet(u"    background-color: transparent;\n"
"    border-radius: 8px;\n"
"    image: url(:/Icons/Logo_Cty_2.png);")

        self.horizontalLayout.addWidget(self.label_2)

        self.company_header_layout = QVBoxLayout()
        self.company_header_layout.setObjectName(u"company_header_layout")
        self.company_name = QLabel(self.header_frame)
        self.company_name.setObjectName(u"company_name")
        sizePolicy.setHeightForWidth(self.company_name.sizePolicy().hasHeightForWidth())
        self.company_name.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(30)
        font1.setBold(True)
        self.company_name.setFont(font1)
        self.company_name.setStyleSheet(u"\n"
"    color: #1E293B;\n"
"    letter-spacing: 1px;")

        self.company_header_layout.addWidget(self.company_name)


        self.horizontalLayout.addLayout(self.company_header_layout)

        self.pc_inform_label = QVBoxLayout()
        self.pc_inform_label.setObjectName(u"pc_inform_label")
        self.error_display = MarqueeLabel(self.header_frame)
        self.error_display.setObjectName(u"error_display")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.error_display.sizePolicy().hasHeightForWidth())
        self.error_display.setSizePolicy(sizePolicy1)
        self.error_display.setMinimumSize(QSize(300, 0))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.error_display.setFont(font2)
        self.error_display.setStyleSheet(u"padding-left: 10px;\n"
"color: #F90A0A;")

        self.pc_inform_label.addWidget(self.error_display)


        self.horizontalLayout.addLayout(self.pc_inform_label)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 3, -1, 3)
        self.eng_language = QPushButton(self.header_frame)
        self.language_btn_group = QButtonGroup(MainWindow)
        self.language_btn_group.setObjectName(u"language_btn_group")
        self.language_btn_group.addButton(self.eng_language)
        self.eng_language.setObjectName(u"eng_language")
        sizePolicy.setHeightForWidth(self.eng_language.sizePolicy().hasHeightForWidth())
        self.eng_language.setSizePolicy(sizePolicy)
        self.eng_language.setMinimumSize(QSize(80, 0))
        self.eng_language.setMaximumSize(QSize(80, 16777215))
        self.eng_language.setStyleSheet(u"\n"
"QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                    stop:0 #F8FAFC, stop:1 #E2E8F0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid #29A1D4;\n"
"}\n"
"QPushButton:checked{\n"
"		background: rgb(173, 173, 173);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/us_flag.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.eng_language.setIcon(icon1)
        self.eng_language.setIconSize(QSize(65, 65))
        self.eng_language.setCheckable(True)
        self.eng_language.setChecked(True)

        self.horizontalLayout_10.addWidget(self.eng_language)

        self.cn_language = QPushButton(self.header_frame)
        self.language_btn_group.addButton(self.cn_language)
        self.cn_language.setObjectName(u"cn_language")
        sizePolicy.setHeightForWidth(self.cn_language.sizePolicy().hasHeightForWidth())
        self.cn_language.setSizePolicy(sizePolicy)
        self.cn_language.setMinimumSize(QSize(80, 0))
        self.cn_language.setMaximumSize(QSize(80, 16777215))
        self.cn_language.setStyleSheet(u"\n"
"QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                    stop:0 #F8FAFC, stop:1 #E2E8F0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid #29A1D4;\n"
"}\n"
"QPushButton:checked{\n"
"		background: rgb(173, 173, 173);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/cn_flag.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cn_language.setIcon(icon2)
        self.cn_language.setIconSize(QSize(65, 65))
        self.cn_language.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.cn_language)


        self.horizontalLayout.addLayout(self.horizontalLayout_10)

        self.date_displ = QDateTimeEdit(self.header_frame)
        self.date_displ.setObjectName(u"date_displ")
        sizePolicy.setHeightForWidth(self.date_displ.sizePolicy().hasHeightForWidth())
        self.date_displ.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"MS Shell Dlg 2"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.date_displ.setFont(font3)
        self.date_displ.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"")
        self.date_displ.setFrame(True)
        self.date_displ.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.date_displ.setReadOnly(True)
        self.date_displ.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date_displ.setDateTime(QDateTime(QDate(2026, 1, 1), QTime(0, 0, 0)))
        self.date_displ.setMaximumTime(QTime(23, 59, 59))
        self.date_displ.setTimeSpec(Qt.LocalTime)

        self.horizontalLayout.addWidget(self.date_displ)


        self.verticalLayout.addWidget(self.header_frame)

        self.body_frame = QFrame(self.centralwidget)
        self.body_frame.setObjectName(u"body_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.body_frame.sizePolicy().hasHeightForWidth())
        self.body_frame.setSizePolicy(sizePolicy2)
        self.body_frame.setStyleSheet(u"QFrame{\n"
"background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0 #eaebeb,\n"
"    stop:1 #dfe1e5);\n"
"}")
        self.body_frame.setFrameShape(QFrame.StyledPanel)
        self.body_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.body_frame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.left_side_menu_widget = QCustomSlideMenu(self.body_frame)
        self.left_side_menu_widget.setObjectName(u"left_side_menu_widget")
        sizePolicy1.setHeightForWidth(self.left_side_menu_widget.sizePolicy().hasHeightForWidth())
        self.left_side_menu_widget.setSizePolicy(sizePolicy1)
        self.left_side_menu_widget.setMinimumSize(QSize(175, 0))
        self.left_side_menu_widget.setMaximumSize(QSize(175, 16777215))
        self.left_side_menu_widget.setStyleSheet(u"QWidget {\n"
"    background-color: white;\n"
"}\n"
"QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: left;\n"
"    padding: 12px 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                    stop:0 #F8FAFC, stop:1 #E2E8F0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-right: 5px solid #29A1D4;\n"
"}\n"
"QPushButton:checked {\n"
"	border-right: 5px solid #0AB1F9;\n"
"	color: #0AB1F9;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.left_side_menu_widget)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.home_page_btn = QPushButton(self.left_side_menu_widget)
        self.left_side_btn_group = QButtonGroup(MainWindow)
        self.left_side_btn_group.setObjectName(u"left_side_btn_group")
        self.left_side_btn_group.addButton(self.home_page_btn)
        self.home_page_btn.setObjectName(u"home_page_btn")
        sizePolicy.setHeightForWidth(self.home_page_btn.sizePolicy().hasHeightForWidth())
        self.home_page_btn.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(17)
        font4.setBold(True)
        self.home_page_btn.setFont(font4)
        self.home_page_btn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/home_off.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/Icons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.home_page_btn.setIcon(icon3)
        self.home_page_btn.setIconSize(QSize(30, 30))
        self.home_page_btn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.home_page_btn)

        self.chart_page_btn = QPushButton(self.left_side_menu_widget)
        self.left_side_btn_group.addButton(self.chart_page_btn)
        self.chart_page_btn.setObjectName(u"chart_page_btn")
        sizePolicy.setHeightForWidth(self.chart_page_btn.sizePolicy().hasHeightForWidth())
        self.chart_page_btn.setSizePolicy(sizePolicy)
        self.chart_page_btn.setFont(font4)
        self.chart_page_btn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/chart-line-up-down.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/Icons/chart-line-up-down_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.chart_page_btn.setIcon(icon4)
        self.chart_page_btn.setIconSize(QSize(30, 30))
        self.chart_page_btn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.chart_page_btn)

        self.device_page_btn = QPushButton(self.left_side_menu_widget)
        self.left_side_btn_group.addButton(self.device_page_btn)
        self.device_page_btn.setObjectName(u"device_page_btn")
        sizePolicy.setHeightForWidth(self.device_page_btn.sizePolicy().hasHeightForWidth())
        self.device_page_btn.setSizePolicy(sizePolicy)
        self.device_page_btn.setFont(font4)
        icon5 = QIcon()
        icon5.addFile(u":/Icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/Icons/settings (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.device_page_btn.setIcon(icon5)
        self.device_page_btn.setIconSize(QSize(35, 35))
        self.device_page_btn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.device_page_btn)

        self.history_page_btn = QPushButton(self.left_side_menu_widget)
        self.left_side_btn_group.addButton(self.history_page_btn)
        self.history_page_btn.setObjectName(u"history_page_btn")
        sizePolicy.setHeightForWidth(self.history_page_btn.sizePolicy().hasHeightForWidth())
        self.history_page_btn.setSizePolicy(sizePolicy)
        self.history_page_btn.setFont(font4)
        icon6 = QIcon()
        icon6.addFile(u":/Icons/stats.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/Icons/stats (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.history_page_btn.setIcon(icon6)
        self.history_page_btn.setIconSize(QSize(30, 30))
        self.history_page_btn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.history_page_btn)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.open_side_menu_btn = QPushButton(self.left_side_menu_widget)
        self.open_side_menu_btn.setObjectName(u"open_side_menu_btn")
        sizePolicy.setHeightForWidth(self.open_side_menu_btn.sizePolicy().hasHeightForWidth())
        self.open_side_menu_btn.setSizePolicy(sizePolicy)
        self.open_side_menu_btn.setFont(font4)
        self.open_side_menu_btn.setLayoutDirection(Qt.LeftToRight)
        self.open_side_menu_btn.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background: white;\n"
"}")
        self.open_side_menu_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.open_side_menu_btn)

        self.verticalLayout_3.setStretch(0, 8)
        self.verticalLayout_3.setStretch(1, 9)

        self.horizontalLayout_2.addWidget(self.left_side_menu_widget)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.stackedWidget_2 = QStackedWidget(self.body_frame)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.menu_page = QWidget()
        self.menu_page.setObjectName(u"menu_page")
        self.menu_page.setStyleSheet(u"QFrame {	\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #bfe2f7\n"
"            );\n"
"	border-radius: 20px;\n"
"}\n"
"QFrame:hover {	\n"
"	border: 1px solid rgb(0, 170, 255);\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.menu_page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, 3, 3)
        self.card_frame_7 = QFrame(self.menu_page)
        self.card_frame_7.setObjectName(u"card_frame_7")
        self.card_frame_7.setStyleSheet(u"color: black;")
        self.card_frame_7.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_21 = QVBoxLayout(self.card_frame_7)
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(5, 5, 5, 5)
        self.card_pressure_1 = QVBoxLayout()
        self.card_pressure_1.setSpacing(10)
        self.card_pressure_1.setObjectName(u"card_pressure_1")

        self.verticalLayout_21.addLayout(self.card_pressure_1)


        self.gridLayout_2.addWidget(self.card_frame_7, 0, 1, 1, 1)

        self.card_frame_8 = QFrame(self.menu_page)
        self.card_frame_8.setObjectName(u"card_frame_8")
        self.card_frame_8.setStyleSheet(u"color: black;")
        self.card_frame_8.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_25 = QVBoxLayout(self.card_frame_8)
        self.verticalLayout_25.setSpacing(5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(5, 5, 5, 5)
        self.card_pressure_2 = QVBoxLayout()
        self.card_pressure_2.setSpacing(10)
        self.card_pressure_2.setObjectName(u"card_pressure_2")

        self.verticalLayout_25.addLayout(self.card_pressure_2)


        self.gridLayout_2.addWidget(self.card_frame_8, 1, 0, 1, 1)

        self.card_frame_9 = QFrame(self.menu_page)
        self.card_frame_9.setObjectName(u"card_frame_9")
        self.card_frame_9.setStyleSheet(u"color: black;")
        self.card_frame_9.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_26 = QVBoxLayout(self.card_frame_9)
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(5, 5, 5, 5)
        self.card_pressure_3 = QVBoxLayout()
        self.card_pressure_3.setSpacing(10)
        self.card_pressure_3.setObjectName(u"card_pressure_3")

        self.verticalLayout_26.addLayout(self.card_pressure_3)


        self.gridLayout_2.addWidget(self.card_frame_9, 1, 1, 1, 1)

        self.card_frame_6 = QFrame(self.menu_page)
        self.card_frame_6.setObjectName(u"card_frame_6")
        self.card_frame_6.setStyleSheet(u"")
        self.card_frame_6.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_19 = QVBoxLayout(self.card_frame_6)
        self.verticalLayout_19.setSpacing(5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(5, 5, 5, 5)
        self.card_temperature = QVBoxLayout()
        self.card_temperature.setSpacing(10)
        self.card_temperature.setObjectName(u"card_temperature")

        self.verticalLayout_19.addLayout(self.card_temperature)


        self.gridLayout_2.addWidget(self.card_frame_6, 0, 0, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)

        self.verticalLayout_14.addLayout(self.gridLayout_2)

        self.stackedWidget_2.addWidget(self.menu_page)
        self.temp_press_page = QWidget()
        self.temp_press_page.setObjectName(u"temp_press_page")
        self.verticalLayout_12 = QVBoxLayout(self.temp_press_page)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pressure_page_header = QWidget(self.temp_press_page)
        self.pressure_page_header.setObjectName(u"pressure_page_header")
        self.pressure_page_header.setMaximumSize(QSize(16777215, 65))
        self.pressure_page_header.setStyleSheet(u"background-color: white;\n"
"border-radius:15px;")
        self.verticalLayout_38 = QVBoxLayout(self.pressure_page_header)
        self.verticalLayout_38.setSpacing(5)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 5, 0, 5)
        self.widget_63 = QWidget(self.pressure_page_header)
        self.widget_63.setObjectName(u"widget_63")
        self.widget_63.setStyleSheet(u"color: black;")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_63)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(10, 5, 10, 5)
        self.widget_9 = QWidget(self.widget_63)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMaximumSize(QSize(16777215, 100))
        self.widget_9.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #0B7EC8;\n"
"    border: 2px solid #0B7EC8;\n"
"    padding: 4px 4px;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #F0F9FF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #E0F2FE;\n"
"}")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_29.setSpacing(10)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.next_group_page_btn = QPushButton(self.widget_9)
        self.next_group_page_btn.setObjectName(u"next_group_page_btn")
        sizePolicy.setHeightForWidth(self.next_group_page_btn.sizePolicy().hasHeightForWidth())
        self.next_group_page_btn.setSizePolicy(sizePolicy)
        self.next_group_page_btn.setMaximumSize(QSize(16777215, 150))
        font5 = QFont()
        font5.setBold(True)
        self.next_group_page_btn.setFont(font5)
        self.next_group_page_btn.setStyleSheet(u"QPushButton{\n"
"	image: url(:/Icons/arrow-alt-circle-right.png)\n"
"}\n"
"QPushButton:pressed{\n"
"	image: url(:/Icons/arrow-alt-circle-right_blue.png)\n"
"}")
        self.next_group_page_btn.setIconSize(QSize(40, 40))
        self.next_group_page_btn.setCheckable(False)

        self.horizontalLayout_29.addWidget(self.next_group_page_btn)

        self.horizontalLayout_29.setStretch(0, 1)

        self.horizontalLayout_15.addWidget(self.widget_9)

        self.sys_state_stacked_wid_39 = QStackedWidget(self.widget_63)
        self.sys_state_stacked_wid_39.setObjectName(u"sys_state_stacked_wid_39")
        sizePolicy.setHeightForWidth(self.sys_state_stacked_wid_39.sizePolicy().hasHeightForWidth())
        self.sys_state_stacked_wid_39.setSizePolicy(sizePolicy)
        self.sys_state_stacked_wid_39.setStyleSheet(u"")
        self.error_light_52 = QWidget()
        self.error_light_52.setObjectName(u"error_light_52")
        self.horizontalLayout_441 = QHBoxLayout(self.error_light_52)
        self.horizontalLayout_441.setObjectName(u"horizontalLayout_441")
        self.horizontalLayout_441.setContentsMargins(0, 0, 0, 0)
        self.stop_light = QPushButton(self.error_light_52)
        self.stop_light.setObjectName(u"stop_light")
        sizePolicy.setHeightForWidth(self.stop_light.sizePolicy().hasHeightForWidth())
        self.stop_light.setSizePolicy(sizePolicy)
        font6 = QFont()
        font6.setPointSize(22)
        font6.setBold(True)
        self.stop_light.setFont(font6)
        self.stop_light.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #F90A0A; \n"
"padding-right: 3px;")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/record-button (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stop_light.setIcon(icon7)
        self.stop_light.setIconSize(QSize(30, 30))

        self.horizontalLayout_441.addWidget(self.stop_light)

        self.sys_state_stacked_wid_39.addWidget(self.error_light_52)
        self.running_light_52 = QWidget()
        self.running_light_52.setObjectName(u"running_light_52")
        self.horizontalLayout_439 = QHBoxLayout(self.running_light_52)
        self.horizontalLayout_439.setObjectName(u"horizontalLayout_439")
        self.horizontalLayout_439.setContentsMargins(0, 0, 0, 0)
        self.start_light = QPushButton(self.running_light_52)
        self.start_light.setObjectName(u"start_light")
        sizePolicy.setHeightForWidth(self.start_light.sizePolicy().hasHeightForWidth())
        self.start_light.setSizePolicy(sizePolicy)
        self.start_light.setFont(font6)
        self.start_light.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #10B981; \n"
"padding-right: 3px;")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/record-button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_light.setIcon(icon8)
        self.start_light.setIconSize(QSize(30, 30))

        self.horizontalLayout_439.addWidget(self.start_light)

        self.sys_state_stacked_wid_39.addWidget(self.running_light_52)

        self.horizontalLayout_15.addWidget(self.sys_state_stacked_wid_39)

        self.temp_unit_selection_combox = QComboBox(self.widget_63)
        self.temp_unit_selection_combox.addItem("")
        self.temp_unit_selection_combox.addItem("")
        self.temp_unit_selection_combox.setObjectName(u"temp_unit_selection_combox")
        sizePolicy1.setHeightForWidth(self.temp_unit_selection_combox.sizePolicy().hasHeightForWidth())
        self.temp_unit_selection_combox.setSizePolicy(sizePolicy1)
        self.temp_unit_selection_combox.setFont(font6)
        self.temp_unit_selection_combox.setStyleSheet(u"\n"
"    background-color: #F9FAFB;")

        self.horizontalLayout_15.addWidget(self.temp_unit_selection_combox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_4)

        self.widget_56 = QWidget(self.widget_63)
        self.widget_56.setObjectName(u"widget_56")
        self.widget_56.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B7EC8;\n"
"    color: white;\n"
"    border: none;\n"
"	padding: 5px;\n"
"    border-radius: 6px;\n"
"	padding-left:10px;\n"
"	padding-right:10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0968A3;\n"
"}")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_56)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.clear_data_btn = QPushButton(self.widget_56)
        self.clear_data_btn.setObjectName(u"clear_data_btn")
        sizePolicy.setHeightForWidth(self.clear_data_btn.sizePolicy().hasHeightForWidth())
        self.clear_data_btn.setSizePolicy(sizePolicy)
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(22)
        font7.setBold(True)
        self.clear_data_btn.setFont(font7)
        icon9 = QIcon()
        icon9.addFile(u":/Icons/data-cleaning.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clear_data_btn.setIcon(icon9)
        self.clear_data_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_9.addWidget(self.clear_data_btn)

        self.new_data_btn = QPushButton(self.widget_56)
        self.new_data_btn.setObjectName(u"new_data_btn")
        sizePolicy.setHeightForWidth(self.new_data_btn.sizePolicy().hasHeightForWidth())
        self.new_data_btn.setSizePolicy(sizePolicy)
        self.new_data_btn.setFont(font7)
        icon10 = QIcon()
        icon10.addFile(u":/Icons/folder-upload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.new_data_btn.setIcon(icon10)
        self.new_data_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_9.addWidget(self.new_data_btn)


        self.horizontalLayout_15.addWidget(self.widget_56)


        self.verticalLayout_38.addWidget(self.widget_63)


        self.verticalLayout_12.addWidget(self.pressure_page_header)

        self.stackedWidget = QStackedWidget(self.temp_press_page)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font8 = QFont()
        font8.setPointSize(15)
        self.stackedWidget.setFont(font8)
        self.stackedWidget.setStyleSheet(u"QStackedWidget {\n"
"    border: none;\n"
"}")
        self.pressure_page = QWidget()
        self.pressure_page.setObjectName(u"pressure_page")
        self.verticalLayout_6 = QVBoxLayout(self.pressure_page)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 2)
        self.stacked_pressure_page = QWidget(self.pressure_page)
        self.stacked_pressure_page.setObjectName(u"stacked_pressure_page")
        self.verticalLayout_10 = QVBoxLayout(self.stacked_pressure_page)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_pressure = QWidget(self.stacked_pressure_page)
        self.widget_pressure.setObjectName(u"widget_pressure")
        self.widget_pressure.setStyleSheet(u"background-color: white;\n"
"border-radius: 15px;")
        self.verticalLayout_63 = QVBoxLayout(self.widget_pressure)
        self.verticalLayout_63.setSpacing(10)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_pressure)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"QWidget#widget_6 {\n"
"    border-left: 4px solid rgb(22, 93, 200);\n"
"    border-radius: 10px;\n"
"}")
        self.gridLayout = QGridLayout(self.widget_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(10, 0, 5, 5)
        self.header_group_layout_2 = QHBoxLayout()
        self.header_group_layout_2.setObjectName(u"header_group_layout_2")
        self.widget_19 = QWidget(self.widget_6)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setStyleSheet(u"QWidget{\n"
"	color: rgb(251, 140, 0);\n"
"	border-left: none;\n"
"}")
        self.verticalLayout_20 = QVBoxLayout(self.widget_19)
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_164 = QLabel(self.widget_19)
        self.label_164.setObjectName(u"label_164")
        font9 = QFont()
        font9.setFamilies([u"MS Shell Dlg 2"])
        font9.setPointSize(19)
        font9.setBold(True)
        font9.setItalic(False)
        self.label_164.setFont(font9)
        self.label_164.setStyleSheet(u"")
        self.label_164.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_164)

        self.widget_20 = QWidget(self.widget_19)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_19.setSpacing(7)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_21 = QWidget(self.widget_20)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_20.setSpacing(7)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 2, 2, 2)
        self.label_168 = QLabel(self.widget_21)
        self.label_168.setObjectName(u"label_168")
        font10 = QFont()
        font10.setFamilies([u"MS Shell Dlg 2"])
        font10.setPointSize(16)
        font10.setBold(True)
        font10.setItalic(False)
        self.label_168.setFont(font10)
        self.label_168.setStyleSheet(u"color: rgb(229, 57, 53);")
        self.label_168.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_168)

        self.line_15 = QFrame(self.widget_21)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setStyleSheet(u"border: 1px solid rgb(22, 93, 200);")
        self.line_15.setFrameShape(QFrame.Shape.VLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_20.addWidget(self.line_15)

        self.label_170 = QLabel(self.widget_21)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setFont(font10)
        self.label_170.setStyleSheet(u"color: rgb(67, 160, 71);")
        self.label_170.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_170)

        self.horizontalLayout_20.setStretch(0, 1)
        self.horizontalLayout_20.setStretch(2, 1)

        self.horizontalLayout_19.addWidget(self.widget_21)

        self.horizontalLayout_19.setStretch(0, 6)

        self.verticalLayout_20.addWidget(self.widget_20)


        self.header_group_layout_2.addWidget(self.widget_19)

        self.clear_group_b = QPushButton(self.widget_6)
        self.clear_group_b.setObjectName(u"clear_group_b")
        sizePolicy.setHeightForWidth(self.clear_group_b.sizePolicy().hasHeightForWidth())
        self.clear_group_b.setSizePolicy(sizePolicy)
        icon11 = QIcon()
        icon11.addFile(u":/Icons/eraser_hover.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clear_group_b.setIcon(icon11)
        self.clear_group_b.setIconSize(QSize(42, 42))

        self.header_group_layout_2.addWidget(self.clear_group_b)

        self.header_group_layout_2.setStretch(0, 6)
        self.header_group_layout_2.setStretch(1, 1)

        self.gridLayout.addLayout(self.header_group_layout_2, 0, 4, 2, 1)

        self.widget_42 = QWidget(self.widget_6)
        self.widget_42.setObjectName(u"widget_42")
        self.horizontalLayout_45 = QHBoxLayout(self.widget_42)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(3, 5, 3, 3)
        self.refuel_btn_c_2 = QPushButton(self.widget_42)
        self.refuel_btn_c_2.setObjectName(u"refuel_btn_c_2")
        sizePolicy.setHeightForWidth(self.refuel_btn_c_2.sizePolicy().hasHeightForWidth())
        self.refuel_btn_c_2.setSizePolicy(sizePolicy)
        self.refuel_btn_c_2.setMinimumSize(QSize(0, 40))
        self.refuel_btn_c_2.setMaximumSize(QSize(16777215, 75))
        self.refuel_btn_c_2.setFont(font2)
        self.refuel_btn_c_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B7EC8;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 8px 12px;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0968A3;\n"
"}\n"
"QPushButton:pressed {\n"
"	color: white;\n"
"    background-color: #085A91;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #EF4444;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/Icons/gas-pump-alt.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refuel_btn_c_2.setIcon(icon12)
        self.refuel_btn_c_2.setIconSize(QSize(35, 35))
        self.refuel_btn_c_2.setCheckable(True)

        self.horizontalLayout_45.addWidget(self.refuel_btn_c_2)


        self.gridLayout.addWidget(self.widget_42, 17, 6, 1, 1)

        self.line_11 = QFrame(self.widget_6)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_11, 13, 1, 4, 1)

        self.line_8 = QFrame(self.widget_6)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_8, 6, 3, 6, 1)

        self.line_10 = QFrame(self.widget_6)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_10, 13, 3, 4, 1)

        self.line = QFrame(self.widget_6)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 12, 0, 1, 7)

        self.line_5 = QFrame(self.widget_6)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_5, 2, 3, 3, 1)

        self.line_9 = QFrame(self.widget_6)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_9, 13, 5, 4, 1)

        self.line_3 = QFrame(self.widget_6)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 2, 1, 3, 1)

        self.line_4 = QFrame(self.widget_6)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_4, 2, 5, 3, 1)

        self.line_2 = QFrame(self.widget_6)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 7)

        self.line_7 = QFrame(self.widget_6)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_7, 6, 1, 6, 1)

        self.line_6 = QFrame(self.widget_6)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_6, 6, 5, 6, 1)

        self.label_name_1 = QWidget(self.widget_6)
        self.label_name_1.setObjectName(u"label_name_1")
        self.horizontalLayout_11 = QHBoxLayout(self.label_name_1)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(3, 3, 3, 3)
        self.label_85 = QLabel(self.label_name_1)
        self.label_85.setObjectName(u"label_85")
        font11 = QFont()
        font11.setFamilies([u"Segoe UI"])
        font11.setPointSize(19)
        font11.setBold(True)
        font11.setItalic(False)
        self.label_85.setFont(font11)
        self.label_85.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #e3e6ee\n"
"            );\n"
"}")

        self.horizontalLayout_11.addWidget(self.label_85)


        self.gridLayout.addWidget(self.label_name_1, 2, 0, 1, 1)

        self.group_2_val_1 = QWidget(self.widget_6)
        self.group_2_val_1.setObjectName(u"group_2_val_1")
        self.horizontalLayout_578 = QHBoxLayout(self.group_2_val_1)
        self.horizontalLayout_578.setObjectName(u"horizontalLayout_578")
        self.horizontalLayout_578.setContentsMargins(3, 3, 6, 3)
        self.widget_335 = QWidget(self.group_2_val_1)
        self.widget_335.setObjectName(u"widget_335")
        self.widget_335.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_579 = QHBoxLayout(self.widget_335)
        self.horizontalLayout_579.setObjectName(u"horizontalLayout_579")
        self.horizontalLayout_579.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_11 = QSpinBox(self.widget_335)
        self.pressure_pv_b_11.setObjectName(u"pressure_pv_b_11")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_11.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_11.setSizePolicy(sizePolicy)
        self.pressure_pv_b_11.setFont(font11)
        self.pressure_pv_b_11.setStyleSheet(u"")
        self.pressure_pv_b_11.setWrapping(True)
        self.pressure_pv_b_11.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_11.setReadOnly(True)
        self.pressure_pv_b_11.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_11.setMaximum(9999999)

        self.horizontalLayout_579.addWidget(self.pressure_pv_b_11)

        self.line_59 = QFrame(self.widget_335)
        self.line_59.setObjectName(u"line_59")
        self.line_59.setStyleSheet(u"border: 1px solid rgb(22, 93, 200);")
        self.line_59.setFrameShape(QFrame.Shape.VLine)
        self.line_59.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_579.addWidget(self.line_59)

        self.pressure_sv_b_11 = QSpinBox(self.widget_335)
        self.pressure_sv_b_11.setObjectName(u"pressure_sv_b_11")
        sizePolicy.setHeightForWidth(self.pressure_sv_b_11.sizePolicy().hasHeightForWidth())
        self.pressure_sv_b_11.setSizePolicy(sizePolicy)
        self.pressure_sv_b_11.setFont(font11)
        self.pressure_sv_b_11.setStyleSheet(u"QSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_b_11.setWrapping(False)
        self.pressure_sv_b_11.setAlignment(Qt.AlignCenter)
        self.pressure_sv_b_11.setReadOnly(False)
        self.pressure_sv_b_11.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_b_11.setMaximum(9999999)

        self.horizontalLayout_579.addWidget(self.pressure_sv_b_11)


        self.horizontalLayout_578.addWidget(self.widget_335)

        self.set_cycle_b_btn = QPushButton(self.group_2_val_1)
        self.set_cycle_b_btn.setObjectName(u"set_cycle_b_btn")
        sizePolicy.setHeightForWidth(self.set_cycle_b_btn.sizePolicy().hasHeightForWidth())
        self.set_cycle_b_btn.setSizePolicy(sizePolicy)
        self.set_cycle_b_btn.setMinimumSize(QSize(0, 0))
        font12 = QFont()
        font12.setFamilies([u"Segoe UI"])
        font12.setPointSize(18)
        font12.setBold(True)
        self.set_cycle_b_btn.setFont(font12)
        self.set_cycle_b_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #10B981;\n"
"    color: white;\n"
"    border: 1px solid #0B7EC8;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(13, 152, 106);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #EF4444;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: white;\n"
"    color: #0B7EC8;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/Icons/infinite-cycle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon13.addFile(u":/Icons/arrows-repeat-1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.set_cycle_b_btn.setIcon(icon13)
        self.set_cycle_b_btn.setIconSize(QSize(30, 30))
        self.set_cycle_b_btn.setCheckable(True)

        self.horizontalLayout_578.addWidget(self.set_cycle_b_btn)

        self.horizontalLayout_578.setStretch(0, 6)
        self.horizontalLayout_578.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_2_val_1, 2, 4, 1, 1)

        self.label_name_2 = QWidget(self.widget_6)
        self.label_name_2.setObjectName(u"label_name_2")
        self.horizontalLayout_12 = QHBoxLayout(self.label_name_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(3, 3, 3, 3)
        self.label_83 = QLabel(self.label_name_2)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setFont(font11)
        self.label_83.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #e3e6ee\n"
"            );\n"
"}")

        self.horizontalLayout_12.addWidget(self.label_83)


        self.gridLayout.addWidget(self.label_name_2, 3, 0, 1, 1)

        self.group_1_val_2 = QWidget(self.widget_6)
        self.group_1_val_2.setObjectName(u"group_1_val_2")
        self.horizontalLayout_498 = QHBoxLayout(self.group_1_val_2)
        self.horizontalLayout_498.setObjectName(u"horizontalLayout_498")
        self.horizontalLayout_498.setContentsMargins(3, 3, 6, 3)
        self.widget_235 = QWidget(self.group_1_val_2)
        self.widget_235.setObjectName(u"widget_235")
        self.widget_235.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_499 = QHBoxLayout(self.widget_235)
        self.horizontalLayout_499.setObjectName(u"horizontalLayout_499")
        self.horizontalLayout_499.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_9 = QDoubleSpinBox(self.widget_235)
        self.pressure_pv_a_9.setObjectName(u"pressure_pv_a_9")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_9.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_9.setSizePolicy(sizePolicy)
        self.pressure_pv_a_9.setFont(font11)
        self.pressure_pv_a_9.setStyleSheet(u"")
        self.pressure_pv_a_9.setWrapping(True)
        self.pressure_pv_a_9.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_9.setReadOnly(True)
        self.pressure_pv_a_9.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_9.setDecimals(1)
        self.pressure_pv_a_9.setMaximum(999.000000000000000)
        self.pressure_pv_a_9.setValue(0.000000000000000)

        self.horizontalLayout_499.addWidget(self.pressure_pv_a_9)

        self.line_41 = QFrame(self.widget_235)
        self.line_41.setObjectName(u"line_41")
        self.line_41.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_41.setFrameShape(QFrame.Shape.VLine)
        self.line_41.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_499.addWidget(self.line_41)

        self.pressure_sv_a_9 = QDoubleSpinBox(self.widget_235)
        self.pressure_sv_a_9.setObjectName(u"pressure_sv_a_9")
        sizePolicy.setHeightForWidth(self.pressure_sv_a_9.sizePolicy().hasHeightForWidth())
        self.pressure_sv_a_9.setSizePolicy(sizePolicy)
        self.pressure_sv_a_9.setFont(font11)
        self.pressure_sv_a_9.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_a_9.setWrapping(False)
        self.pressure_sv_a_9.setAlignment(Qt.AlignCenter)
        self.pressure_sv_a_9.setReadOnly(False)
        self.pressure_sv_a_9.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_a_9.setDecimals(1)
        self.pressure_sv_a_9.setMaximum(999.000000000000000)
        self.pressure_sv_a_9.setValue(0.000000000000000)

        self.horizontalLayout_499.addWidget(self.pressure_sv_a_9)

        self.horizontalLayout_499.setStretch(0, 1)
        self.horizontalLayout_499.setStretch(2, 1)

        self.horizontalLayout_498.addWidget(self.widget_235)

        self.label_245 = QLabel(self.group_1_val_2)
        self.label_245.setObjectName(u"label_245")
        font13 = QFont()
        font13.setFamilies([u"Segoe UI"])
        font13.setPointSize(17)
        font13.setBold(True)
        font13.setItalic(False)
        self.label_245.setFont(font13)
        self.label_245.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_245.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_498.addWidget(self.label_245)

        self.horizontalLayout_498.setStretch(0, 6)
        self.horizontalLayout_498.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_1_val_2, 3, 2, 1, 1)

        self.group_1_val_1 = QWidget(self.widget_6)
        self.group_1_val_1.setObjectName(u"group_1_val_1")
        self.horizontalLayout_576 = QHBoxLayout(self.group_1_val_1)
        self.horizontalLayout_576.setObjectName(u"horizontalLayout_576")
        self.horizontalLayout_576.setContentsMargins(3, 3, 6, 3)
        self.widget_303 = QWidget(self.group_1_val_1)
        self.widget_303.setObjectName(u"widget_303")
        self.widget_303.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_577 = QHBoxLayout(self.widget_303)
        self.horizontalLayout_577.setObjectName(u"horizontalLayout_577")
        self.horizontalLayout_577.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_11 = QSpinBox(self.widget_303)
        self.pressure_pv_a_11.setObjectName(u"pressure_pv_a_11")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_11.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_11.setSizePolicy(sizePolicy)
        self.pressure_pv_a_11.setFont(font11)
        self.pressure_pv_a_11.setStyleSheet(u"")
        self.pressure_pv_a_11.setWrapping(True)
        self.pressure_pv_a_11.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_11.setReadOnly(True)
        self.pressure_pv_a_11.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_11.setMaximum(9999999)

        self.horizontalLayout_577.addWidget(self.pressure_pv_a_11)

        self.line_47 = QFrame(self.widget_303)
        self.line_47.setObjectName(u"line_47")
        self.line_47.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_47.setFrameShape(QFrame.Shape.VLine)
        self.line_47.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_577.addWidget(self.line_47)

        self.pressure_sv_a_11 = QSpinBox(self.widget_303)
        self.pressure_sv_a_11.setObjectName(u"pressure_sv_a_11")
        sizePolicy.setHeightForWidth(self.pressure_sv_a_11.sizePolicy().hasHeightForWidth())
        self.pressure_sv_a_11.setSizePolicy(sizePolicy)
        self.pressure_sv_a_11.setFont(font11)
        self.pressure_sv_a_11.setStyleSheet(u"QSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_a_11.setWrapping(False)
        self.pressure_sv_a_11.setAlignment(Qt.AlignCenter)
        self.pressure_sv_a_11.setReadOnly(False)
        self.pressure_sv_a_11.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_a_11.setMaximum(9999999)

        self.horizontalLayout_577.addWidget(self.pressure_sv_a_11)


        self.horizontalLayout_576.addWidget(self.widget_303)

        self.set_cycle_a_btn = QPushButton(self.group_1_val_1)
        self.set_cycle_a_btn.setObjectName(u"set_cycle_a_btn")
        sizePolicy.setHeightForWidth(self.set_cycle_a_btn.sizePolicy().hasHeightForWidth())
        self.set_cycle_a_btn.setSizePolicy(sizePolicy)
        self.set_cycle_a_btn.setMinimumSize(QSize(0, 0))
        self.set_cycle_a_btn.setFont(font12)
        self.set_cycle_a_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #10B981;\n"
"    color: white;\n"
"    border: 1px solid #0B7EC8;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(13, 152, 106);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #EF4444;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: white;\n"
"    color: #0B7EC8;\n"
"}")
        self.set_cycle_a_btn.setIcon(icon13)
        self.set_cycle_a_btn.setIconSize(QSize(30, 30))
        self.set_cycle_a_btn.setCheckable(True)

        self.horizontalLayout_576.addWidget(self.set_cycle_a_btn)

        self.horizontalLayout_576.setStretch(0, 6)
        self.horizontalLayout_576.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_1_val_1, 2, 2, 1, 1)

        self.group_3_val_1 = QWidget(self.widget_6)
        self.group_3_val_1.setObjectName(u"group_3_val_1")
        self.horizontalLayout_580 = QHBoxLayout(self.group_3_val_1)
        self.horizontalLayout_580.setObjectName(u"horizontalLayout_580")
        self.horizontalLayout_580.setContentsMargins(3, 3, 6, 3)
        self.widget_337 = QWidget(self.group_3_val_1)
        self.widget_337.setObjectName(u"widget_337")
        self.widget_337.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_581 = QHBoxLayout(self.widget_337)
        self.horizontalLayout_581.setObjectName(u"horizontalLayout_581")
        self.horizontalLayout_581.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_11 = QSpinBox(self.widget_337)
        self.pressure_pv_c_11.setObjectName(u"pressure_pv_c_11")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_11.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_11.setSizePolicy(sizePolicy)
        self.pressure_pv_c_11.setFont(font11)
        self.pressure_pv_c_11.setStyleSheet(u"")
        self.pressure_pv_c_11.setWrapping(True)
        self.pressure_pv_c_11.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_11.setReadOnly(True)
        self.pressure_pv_c_11.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_11.setMaximum(9999999)

        self.horizontalLayout_581.addWidget(self.pressure_pv_c_11)

        self.line_60 = QFrame(self.widget_337)
        self.line_60.setObjectName(u"line_60")
        self.line_60.setStyleSheet(u"border: 1px solid rgb(22, 93, 200);")
        self.line_60.setFrameShape(QFrame.Shape.VLine)
        self.line_60.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_581.addWidget(self.line_60)

        self.pressure_sv_c_11 = QSpinBox(self.widget_337)
        self.pressure_sv_c_11.setObjectName(u"pressure_sv_c_11")
        sizePolicy.setHeightForWidth(self.pressure_sv_c_11.sizePolicy().hasHeightForWidth())
        self.pressure_sv_c_11.setSizePolicy(sizePolicy)
        self.pressure_sv_c_11.setFont(font11)
        self.pressure_sv_c_11.setStyleSheet(u"QSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_c_11.setWrapping(False)
        self.pressure_sv_c_11.setAlignment(Qt.AlignCenter)
        self.pressure_sv_c_11.setReadOnly(False)
        self.pressure_sv_c_11.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_c_11.setMaximum(9999999)

        self.horizontalLayout_581.addWidget(self.pressure_sv_c_11)


        self.horizontalLayout_580.addWidget(self.widget_337)

        self.set_cycle_c_btn = QPushButton(self.group_3_val_1)
        self.set_cycle_c_btn.setObjectName(u"set_cycle_c_btn")
        sizePolicy.setHeightForWidth(self.set_cycle_c_btn.sizePolicy().hasHeightForWidth())
        self.set_cycle_c_btn.setSizePolicy(sizePolicy)
        self.set_cycle_c_btn.setMinimumSize(QSize(0, 0))
        self.set_cycle_c_btn.setFont(font12)
        self.set_cycle_c_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #10B981;\n"
"    color: white;\n"
"    border: 1px solid #0B7EC8;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(13, 152, 106);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #EF4444;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: white;\n"
"    color: #0B7EC8;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/Icons/infinite-cycle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon14.addFile(u":/Icons/arrows-repeat-1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon14.addFile(u":/newPrefix/rotate-reverse-white.png", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.set_cycle_c_btn.setIcon(icon14)
        self.set_cycle_c_btn.setIconSize(QSize(30, 30))
        self.set_cycle_c_btn.setCheckable(True)

        self.horizontalLayout_580.addWidget(self.set_cycle_c_btn)

        self.horizontalLayout_580.setStretch(0, 6)
        self.horizontalLayout_580.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_3_val_1, 2, 6, 1, 1)

        self.label_name_8 = QWidget(self.widget_6)
        self.label_name_8.setObjectName(u"label_name_8")
        self.horizontalLayout_35 = QHBoxLayout(self.label_name_8)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(3, 3, 3, 3)
        self.label_106 = QLabel(self.label_name_8)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setFont(font11)
        self.label_106.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #e3e6ee\n"
"            );\n"
"}")

        self.horizontalLayout_35.addWidget(self.label_106)


        self.gridLayout.addWidget(self.label_name_8, 10, 0, 1, 1)

        self.group_1_val_9 = QWidget(self.widget_6)
        self.group_1_val_9.setObjectName(u"group_1_val_9")
        self.horizontalLayout_348 = QHBoxLayout(self.group_1_val_9)
        self.horizontalLayout_348.setObjectName(u"horizontalLayout_348")
        self.horizontalLayout_348.setContentsMargins(3, 3, 6, 3)
        self.widget_299 = QWidget(self.group_1_val_9)
        self.widget_299.setObjectName(u"widget_299")
        self.widget_299.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_349 = QHBoxLayout(self.widget_299)
        self.horizontalLayout_349.setObjectName(u"horizontalLayout_349")
        self.horizontalLayout_349.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_5 = QDoubleSpinBox(self.widget_299)
        self.pressure_pv_a_5.setObjectName(u"pressure_pv_a_5")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_5.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_5.setSizePolicy(sizePolicy)
        self.pressure_pv_a_5.setFont(font11)
        self.pressure_pv_a_5.setWrapping(False)
        self.pressure_pv_a_5.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_5.setReadOnly(True)
        self.pressure_pv_a_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_5.setDecimals(2)
        self.pressure_pv_a_5.setMaximum(20.000000000000000)
        self.pressure_pv_a_5.setValue(0.000000000000000)

        self.horizontalLayout_349.addWidget(self.pressure_pv_a_5)

        self.horizontalLayout_349.setStretch(0, 1)

        self.horizontalLayout_348.addWidget(self.widget_299)

        self.label_267 = QLabel(self.group_1_val_9)
        self.label_267.setObjectName(u"label_267")
        self.label_267.setFont(font13)
        self.label_267.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_267.setAlignment(Qt.AlignCenter)
        self.label_267.setWordWrap(True)

        self.horizontalLayout_348.addWidget(self.label_267)

        self.horizontalLayout_348.setStretch(0, 6)
        self.horizontalLayout_348.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_1_val_9, 11, 2, 1, 1)

        self.group_1_val_6 = QWidget(self.widget_6)
        self.group_1_val_6.setObjectName(u"group_1_val_6")
        self.horizontalLayout_506 = QHBoxLayout(self.group_1_val_6)
        self.horizontalLayout_506.setObjectName(u"horizontalLayout_506")
        self.horizontalLayout_506.setContentsMargins(3, 3, 6, 3)
        self.widget_234 = QWidget(self.group_1_val_6)
        self.widget_234.setObjectName(u"widget_234")
        self.widget_234.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_507 = QHBoxLayout(self.widget_234)
        self.horizontalLayout_507.setObjectName(u"horizontalLayout_507")
        self.horizontalLayout_507.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_8 = QDoubleSpinBox(self.widget_234)
        self.pressure_pv_a_8.setObjectName(u"pressure_pv_a_8")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_8.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_8.setSizePolicy(sizePolicy)
        self.pressure_pv_a_8.setFont(font11)
        self.pressure_pv_a_8.setStyleSheet(u"")
        self.pressure_pv_a_8.setWrapping(True)
        self.pressure_pv_a_8.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_8.setReadOnly(True)
        self.pressure_pv_a_8.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_8.setDecimals(1)
        self.pressure_pv_a_8.setMaximum(999.000000000000000)
        self.pressure_pv_a_8.setValue(0.000000000000000)

        self.horizontalLayout_507.addWidget(self.pressure_pv_a_8)

        self.line_46 = QFrame(self.widget_234)
        self.line_46.setObjectName(u"line_46")
        self.line_46.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_46.setFrameShape(QFrame.Shape.VLine)
        self.line_46.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_507.addWidget(self.line_46)

        self.pressure_sv_a_8 = QDoubleSpinBox(self.widget_234)
        self.pressure_sv_a_8.setObjectName(u"pressure_sv_a_8")
        sizePolicy.setHeightForWidth(self.pressure_sv_a_8.sizePolicy().hasHeightForWidth())
        self.pressure_sv_a_8.setSizePolicy(sizePolicy)
        self.pressure_sv_a_8.setFont(font11)
        self.pressure_sv_a_8.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_a_8.setWrapping(False)
        self.pressure_sv_a_8.setAlignment(Qt.AlignCenter)
        self.pressure_sv_a_8.setReadOnly(False)
        self.pressure_sv_a_8.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_a_8.setDecimals(1)
        self.pressure_sv_a_8.setMaximum(999.000000000000000)
        self.pressure_sv_a_8.setValue(0.000000000000000)

        self.horizontalLayout_507.addWidget(self.pressure_sv_a_8)

        self.horizontalLayout_507.setStretch(0, 1)
        self.horizontalLayout_507.setStretch(2, 1)

        self.horizontalLayout_506.addWidget(self.widget_234)

        self.label_244 = QLabel(self.group_1_val_6)
        self.label_244.setObjectName(u"label_244")
        self.label_244.setFont(font13)
        self.label_244.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_244.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_506.addWidget(self.label_244)

        self.horizontalLayout_506.setStretch(0, 6)
        self.horizontalLayout_506.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_1_val_6, 8, 2, 1, 1)

        self.group_3_val_3 = QWidget(self.widget_6)
        self.group_3_val_3.setObjectName(u"group_3_val_3")
        self.horizontalLayout_546 = QHBoxLayout(self.group_3_val_3)
        self.horizontalLayout_546.setObjectName(u"horizontalLayout_546")
        self.horizontalLayout_546.setContentsMargins(3, 3, 6, 3)
        self.widget_290 = QWidget(self.group_3_val_3)
        self.widget_290.setObjectName(u"widget_290")
        self.widget_290.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_547 = QHBoxLayout(self.widget_290)
        self.horizontalLayout_547.setObjectName(u"horizontalLayout_547")
        self.horizontalLayout_547.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_10 = QDoubleSpinBox(self.widget_290)
        self.pressure_pv_c_10.setObjectName(u"pressure_pv_c_10")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_10.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_10.setSizePolicy(sizePolicy)
        self.pressure_pv_c_10.setFont(font11)
        self.pressure_pv_c_10.setStyleSheet(u"")
        self.pressure_pv_c_10.setWrapping(True)
        self.pressure_pv_c_10.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_10.setReadOnly(True)
        self.pressure_pv_c_10.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_10.setDecimals(1)
        self.pressure_pv_c_10.setMaximum(999.000000000000000)
        self.pressure_pv_c_10.setValue(0.000000000000000)

        self.horizontalLayout_547.addWidget(self.pressure_pv_c_10)

        self.line_57 = QFrame(self.widget_290)
        self.line_57.setObjectName(u"line_57")
        self.line_57.setStyleSheet(u"border: 1px solid rgb(22, 93, 200);")
        self.line_57.setFrameShape(QFrame.Shape.VLine)
        self.line_57.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_547.addWidget(self.line_57)

        self.pressure_sv_c_10 = QDoubleSpinBox(self.widget_290)
        self.pressure_sv_c_10.setObjectName(u"pressure_sv_c_10")
        sizePolicy.setHeightForWidth(self.pressure_sv_c_10.sizePolicy().hasHeightForWidth())
        self.pressure_sv_c_10.setSizePolicy(sizePolicy)
        self.pressure_sv_c_10.setFont(font11)
        self.pressure_sv_c_10.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_c_10.setWrapping(False)
        self.pressure_sv_c_10.setAlignment(Qt.AlignCenter)
        self.pressure_sv_c_10.setReadOnly(False)
        self.pressure_sv_c_10.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_c_10.setDecimals(1)
        self.pressure_sv_c_10.setMaximum(999.000000000000000)
        self.pressure_sv_c_10.setValue(0.000000000000000)

        self.horizontalLayout_547.addWidget(self.pressure_sv_c_10)

        self.horizontalLayout_547.setStretch(0, 1)
        self.horizontalLayout_547.setStretch(2, 1)

        self.horizontalLayout_546.addWidget(self.widget_290)

        self.label_262 = QLabel(self.group_3_val_3)
        self.label_262.setObjectName(u"label_262")
        self.label_262.setFont(font13)
        self.label_262.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_262.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_546.addWidget(self.label_262)

        self.horizontalLayout_546.setStretch(0, 6)
        self.horizontalLayout_546.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_3_val_3, 4, 6, 1, 1)

        self.group_2_val_9 = QWidget(self.widget_6)
        self.group_2_val_9.setObjectName(u"group_2_val_9")
        self.horizontalLayout_572 = QHBoxLayout(self.group_2_val_9)
        self.horizontalLayout_572.setObjectName(u"horizontalLayout_572")
        self.horizontalLayout_572.setContentsMargins(3, 3, 6, 3)
        self.widget_300 = QWidget(self.group_2_val_9)
        self.widget_300.setObjectName(u"widget_300")
        self.widget_300.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_573 = QHBoxLayout(self.widget_300)
        self.horizontalLayout_573.setObjectName(u"horizontalLayout_573")
        self.horizontalLayout_573.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_5 = QDoubleSpinBox(self.widget_300)
        self.pressure_pv_b_5.setObjectName(u"pressure_pv_b_5")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_5.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_5.setSizePolicy(sizePolicy)
        self.pressure_pv_b_5.setFont(font11)
        self.pressure_pv_b_5.setWrapping(False)
        self.pressure_pv_b_5.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_5.setReadOnly(True)
        self.pressure_pv_b_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_5.setDecimals(2)
        self.pressure_pv_b_5.setMaximum(20.000000000000000)
        self.pressure_pv_b_5.setValue(0.000000000000000)

        self.horizontalLayout_573.addWidget(self.pressure_pv_b_5)

        self.horizontalLayout_573.setStretch(0, 1)

        self.horizontalLayout_572.addWidget(self.widget_300)

        self.label_268 = QLabel(self.group_2_val_9)
        self.label_268.setObjectName(u"label_268")
        self.label_268.setFont(font13)
        self.label_268.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_268.setAlignment(Qt.AlignCenter)
        self.label_268.setWordWrap(True)

        self.horizontalLayout_572.addWidget(self.label_268)

        self.horizontalLayout_572.setStretch(0, 6)
        self.horizontalLayout_572.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_2_val_9, 11, 4, 1, 1)

        self.group_2_val_3 = QWidget(self.widget_6)
        self.group_2_val_3.setObjectName(u"group_2_val_3")
        self.horizontalLayout_510 = QHBoxLayout(self.group_2_val_3)
        self.horizontalLayout_510.setObjectName(u"horizontalLayout_510")
        self.horizontalLayout_510.setContentsMargins(3, 3, 6, 3)
        self.widget_238 = QWidget(self.group_2_val_3)
        self.widget_238.setObjectName(u"widget_238")
        self.widget_238.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_511 = QHBoxLayout(self.widget_238)
        self.horizontalLayout_511.setObjectName(u"horizontalLayout_511")
        self.horizontalLayout_511.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_10 = QDoubleSpinBox(self.widget_238)
        self.pressure_pv_b_10.setObjectName(u"pressure_pv_b_10")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_10.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_10.setSizePolicy(sizePolicy)
        self.pressure_pv_b_10.setFont(font11)
        self.pressure_pv_b_10.setStyleSheet(u"")
        self.pressure_pv_b_10.setWrapping(True)
        self.pressure_pv_b_10.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_10.setReadOnly(True)
        self.pressure_pv_b_10.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_10.setDecimals(1)
        self.pressure_pv_b_10.setMaximum(999.000000000000000)
        self.pressure_pv_b_10.setValue(0.000000000000000)

        self.horizontalLayout_511.addWidget(self.pressure_pv_b_10)

        self.line_54 = QFrame(self.widget_238)
        self.line_54.setObjectName(u"line_54")
        self.line_54.setStyleSheet(u"border: 1px solid rgb(22, 93, 200);")
        self.line_54.setFrameShape(QFrame.Shape.VLine)
        self.line_54.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_511.addWidget(self.line_54)

        self.pressure_sv_b_10 = QDoubleSpinBox(self.widget_238)
        self.pressure_sv_b_10.setObjectName(u"pressure_sv_b_10")
        sizePolicy.setHeightForWidth(self.pressure_sv_b_10.sizePolicy().hasHeightForWidth())
        self.pressure_sv_b_10.setSizePolicy(sizePolicy)
        self.pressure_sv_b_10.setFont(font11)
        self.pressure_sv_b_10.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_b_10.setWrapping(False)
        self.pressure_sv_b_10.setAlignment(Qt.AlignCenter)
        self.pressure_sv_b_10.setReadOnly(False)
        self.pressure_sv_b_10.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_b_10.setDecimals(1)
        self.pressure_sv_b_10.setMaximum(999.000000000000000)
        self.pressure_sv_b_10.setValue(0.000000000000000)

        self.horizontalLayout_511.addWidget(self.pressure_sv_b_10)

        self.horizontalLayout_511.setStretch(0, 1)
        self.horizontalLayout_511.setStretch(2, 1)

        self.horizontalLayout_510.addWidget(self.widget_238)

        self.label_248 = QLabel(self.group_2_val_3)
        self.label_248.setObjectName(u"label_248")
        self.label_248.setFont(font13)
        self.label_248.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_248.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_510.addWidget(self.label_248)

        self.horizontalLayout_510.setStretch(0, 6)
        self.horizontalLayout_510.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_2_val_3, 4, 4, 1, 1)

        self.group_1_val_3 = QWidget(self.widget_6)
        self.group_1_val_3.setObjectName(u"group_1_val_3")
        self.horizontalLayout_500 = QHBoxLayout(self.group_1_val_3)
        self.horizontalLayout_500.setObjectName(u"horizontalLayout_500")
        self.horizontalLayout_500.setContentsMargins(3, 3, 6, 3)
        self.widget_236 = QWidget(self.group_1_val_3)
        self.widget_236.setObjectName(u"widget_236")
        self.widget_236.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_501 = QHBoxLayout(self.widget_236)
        self.horizontalLayout_501.setObjectName(u"horizontalLayout_501")
        self.horizontalLayout_501.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_10 = QDoubleSpinBox(self.widget_236)
        self.pressure_pv_a_10.setObjectName(u"pressure_pv_a_10")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_10.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_10.setSizePolicy(sizePolicy)
        self.pressure_pv_a_10.setFont(font11)
        self.pressure_pv_a_10.setStyleSheet(u"")
        self.pressure_pv_a_10.setWrapping(True)
        self.pressure_pv_a_10.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_10.setReadOnly(True)
        self.pressure_pv_a_10.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_10.setDecimals(1)
        self.pressure_pv_a_10.setMaximum(999.000000000000000)
        self.pressure_pv_a_10.setValue(0.000000000000000)

        self.horizontalLayout_501.addWidget(self.pressure_pv_a_10)

        self.line_43 = QFrame(self.widget_236)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_43.setFrameShape(QFrame.Shape.VLine)
        self.line_43.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_501.addWidget(self.line_43)

        self.pressure_sv_a_10 = QDoubleSpinBox(self.widget_236)
        self.pressure_sv_a_10.setObjectName(u"pressure_sv_a_10")
        sizePolicy.setHeightForWidth(self.pressure_sv_a_10.sizePolicy().hasHeightForWidth())
        self.pressure_sv_a_10.setSizePolicy(sizePolicy)
        self.pressure_sv_a_10.setFont(font11)
        self.pressure_sv_a_10.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_a_10.setWrapping(False)
        self.pressure_sv_a_10.setAlignment(Qt.AlignCenter)
        self.pressure_sv_a_10.setReadOnly(False)
        self.pressure_sv_a_10.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_a_10.setDecimals(1)
        self.pressure_sv_a_10.setMaximum(999.000000000000000)
        self.pressure_sv_a_10.setValue(0.000000000000000)

        self.horizontalLayout_501.addWidget(self.pressure_sv_a_10)

        self.horizontalLayout_501.setStretch(0, 1)
        self.horizontalLayout_501.setStretch(2, 1)

        self.horizontalLayout_500.addWidget(self.widget_236)

        self.label_246 = QLabel(self.group_1_val_3)
        self.label_246.setObjectName(u"label_246")
        self.label_246.setFont(font13)
        self.label_246.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_246.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_500.addWidget(self.label_246)

        self.horizontalLayout_500.setStretch(0, 6)
        self.horizontalLayout_500.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_1_val_3, 4, 2, 1, 1)

        self.group_1_val_4 = QWidget(self.widget_6)
        self.group_1_val_4.setObjectName(u"group_1_val_4")
        self.horizontalLayout_502 = QHBoxLayout(self.group_1_val_4)
        self.horizontalLayout_502.setObjectName(u"horizontalLayout_502")
        self.horizontalLayout_502.setContentsMargins(3, 3, 6, 3)
        self.widget_232 = QWidget(self.group_1_val_4)
        self.widget_232.setObjectName(u"widget_232")
        self.widget_232.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_503 = QHBoxLayout(self.widget_232)
        self.horizontalLayout_503.setObjectName(u"horizontalLayout_503")
        self.horizontalLayout_503.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_6 = QDoubleSpinBox(self.widget_232)
        self.pressure_pv_a_6.setObjectName(u"pressure_pv_a_6")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_6.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_6.setSizePolicy(sizePolicy)
        self.pressure_pv_a_6.setFont(font11)
        self.pressure_pv_a_6.setStyleSheet(u"")
        self.pressure_pv_a_6.setWrapping(True)
        self.pressure_pv_a_6.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_6.setReadOnly(True)
        self.pressure_pv_a_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_6.setDecimals(1)
        self.pressure_pv_a_6.setMaximum(999.000000000000000)
        self.pressure_pv_a_6.setValue(0.000000000000000)

        self.horizontalLayout_503.addWidget(self.pressure_pv_a_6)

        self.line_44 = QFrame(self.widget_232)
        self.line_44.setObjectName(u"line_44")
        self.line_44.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_44.setFrameShape(QFrame.Shape.VLine)
        self.line_44.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_503.addWidget(self.line_44)

        self.pressure_sv_a_6 = QDoubleSpinBox(self.widget_232)
        self.pressure_sv_a_6.setObjectName(u"pressure_sv_a_6")
        sizePolicy.setHeightForWidth(self.pressure_sv_a_6.sizePolicy().hasHeightForWidth())
        self.pressure_sv_a_6.setSizePolicy(sizePolicy)
        self.pressure_sv_a_6.setFont(font11)
        self.pressure_sv_a_6.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_a_6.setWrapping(False)
        self.pressure_sv_a_6.setAlignment(Qt.AlignCenter)
        self.pressure_sv_a_6.setReadOnly(False)
        self.pressure_sv_a_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_a_6.setDecimals(1)
        self.pressure_sv_a_6.setMaximum(999.000000000000000)
        self.pressure_sv_a_6.setValue(0.000000000000000)

        self.horizontalLayout_503.addWidget(self.pressure_sv_a_6)

        self.horizontalLayout_503.setStretch(0, 1)
        self.horizontalLayout_503.setStretch(2, 1)

        self.horizontalLayout_502.addWidget(self.widget_232)

        self.label_242 = QLabel(self.group_1_val_4)
        self.label_242.setObjectName(u"label_242")
        self.label_242.setFont(font13)
        self.label_242.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_242.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_502.addWidget(self.label_242)

        self.horizontalLayout_502.setStretch(0, 6)
        self.horizontalLayout_502.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_1_val_4, 6, 2, 1, 1)

        self.label_name_5 = QWidget(self.widget_6)
        self.label_name_5.setObjectName(u"label_name_5")
        self.horizontalLayout_16 = QHBoxLayout(self.label_name_5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(3, 3, 3, 3)
        self.label_101 = QLabel(self.label_name_5)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setFont(font11)
        self.label_101.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #e3e6ee\n"
"            );\n"
"}")

        self.horizontalLayout_16.addWidget(self.label_101)


        self.gridLayout.addWidget(self.label_name_5, 7, 0, 1, 1)

        self.group_3_val_7 = QWidget(self.widget_6)
        self.group_3_val_7.setObjectName(u"group_3_val_7")
        self.horizontalLayout_548 = QHBoxLayout(self.group_3_val_7)
        self.horizontalLayout_548.setObjectName(u"horizontalLayout_548")
        self.horizontalLayout_548.setContentsMargins(3, 3, 6, 3)
        self.widget_291 = QWidget(self.group_3_val_7)
        self.widget_291.setObjectName(u"widget_291")
        self.widget_291.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_549 = QHBoxLayout(self.widget_291)
        self.horizontalLayout_549.setObjectName(u"horizontalLayout_549")
        self.horizontalLayout_549.setContentsMargins(2, 2, 2, 2)
        self.pressure_sv_c_5 = QDoubleSpinBox(self.widget_291)
        self.pressure_sv_c_5.setObjectName(u"pressure_sv_c_5")
        sizePolicy.setHeightForWidth(self.pressure_sv_c_5.sizePolicy().hasHeightForWidth())
        self.pressure_sv_c_5.setSizePolicy(sizePolicy)
        self.pressure_sv_c_5.setFont(font11)
        self.pressure_sv_c_5.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_c_5.setWrapping(False)
        self.pressure_sv_c_5.setAlignment(Qt.AlignCenter)
        self.pressure_sv_c_5.setReadOnly(False)
        self.pressure_sv_c_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_c_5.setDecimals(2)
        self.pressure_sv_c_5.setMaximum(20.000000000000000)
        self.pressure_sv_c_5.setValue(0.000000000000000)

        self.horizontalLayout_549.addWidget(self.pressure_sv_c_5)

        self.horizontalLayout_549.setStretch(0, 1)

        self.horizontalLayout_548.addWidget(self.widget_291)

        self.label_263 = QLabel(self.group_3_val_7)
        self.label_263.setObjectName(u"label_263")
        self.label_263.setFont(font13)
        self.label_263.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_263.setAlignment(Qt.AlignCenter)
        self.label_263.setWordWrap(True)

        self.horizontalLayout_548.addWidget(self.label_263)

        self.horizontalLayout_548.setStretch(0, 6)
        self.horizontalLayout_548.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_3_val_7, 9, 6, 1, 1)

        self.group_2_val_6 = QWidget(self.widget_6)
        self.group_2_val_6.setObjectName(u"group_2_val_6")
        self.horizontalLayout_526 = QHBoxLayout(self.group_2_val_6)
        self.horizontalLayout_526.setObjectName(u"horizontalLayout_526")
        self.horizontalLayout_526.setContentsMargins(3, 3, 6, 3)
        self.widget_284 = QWidget(self.group_2_val_6)
        self.widget_284.setObjectName(u"widget_284")
        self.widget_284.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_527 = QHBoxLayout(self.widget_284)
        self.horizontalLayout_527.setObjectName(u"horizontalLayout_527")
        self.horizontalLayout_527.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_8 = QDoubleSpinBox(self.widget_284)
        self.pressure_pv_b_8.setObjectName(u"pressure_pv_b_8")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_8.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_8.setSizePolicy(sizePolicy)
        self.pressure_pv_b_8.setFont(font11)
        self.pressure_pv_b_8.setStyleSheet(u"")
        self.pressure_pv_b_8.setWrapping(True)
        self.pressure_pv_b_8.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_8.setReadOnly(True)
        self.pressure_pv_b_8.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_8.setDecimals(1)
        self.pressure_pv_b_8.setMaximum(999.000000000000000)
        self.pressure_pv_b_8.setValue(0.000000000000000)

        self.horizontalLayout_527.addWidget(self.pressure_pv_b_8)

        self.line_55 = QFrame(self.widget_284)
        self.line_55.setObjectName(u"line_55")
        self.line_55.setStyleSheet(u"border: 1px solid rgb(22, 93, 200);")
        self.line_55.setFrameShape(QFrame.Shape.VLine)
        self.line_55.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_527.addWidget(self.line_55)

        self.pressure_sv_b_8 = QDoubleSpinBox(self.widget_284)
        self.pressure_sv_b_8.setObjectName(u"pressure_sv_b_8")
        sizePolicy.setHeightForWidth(self.pressure_sv_b_8.sizePolicy().hasHeightForWidth())
        self.pressure_sv_b_8.setSizePolicy(sizePolicy)
        self.pressure_sv_b_8.setFont(font11)
        self.pressure_sv_b_8.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_b_8.setWrapping(False)
        self.pressure_sv_b_8.setAlignment(Qt.AlignCenter)
        self.pressure_sv_b_8.setReadOnly(False)
        self.pressure_sv_b_8.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_b_8.setDecimals(1)
        self.pressure_sv_b_8.setMaximum(999.000000000000000)
        self.pressure_sv_b_8.setValue(0.000000000000000)

        self.horizontalLayout_527.addWidget(self.pressure_sv_b_8)

        self.horizontalLayout_527.setStretch(0, 1)
        self.horizontalLayout_527.setStretch(2, 1)

        self.horizontalLayout_526.addWidget(self.widget_284)

        self.label_256 = QLabel(self.group_2_val_6)
        self.label_256.setObjectName(u"label_256")
        self.label_256.setFont(font13)
        self.label_256.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_256.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_526.addWidget(self.label_256)

        self.horizontalLayout_526.setStretch(0, 6)
        self.horizontalLayout_526.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_2_val_6, 8, 4, 1, 1)

        self.group_1_val_7 = QWidget(self.widget_6)
        self.group_1_val_7.setObjectName(u"group_1_val_7")
        self.horizontalLayout_336 = QHBoxLayout(self.group_1_val_7)
        self.horizontalLayout_336.setObjectName(u"horizontalLayout_336")
        self.horizontalLayout_336.setContentsMargins(3, 3, 6, 3)
        self.widget_231 = QWidget(self.group_1_val_7)
        self.widget_231.setObjectName(u"widget_231")
        self.widget_231.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_340 = QHBoxLayout(self.widget_231)
        self.horizontalLayout_340.setObjectName(u"horizontalLayout_340")
        self.horizontalLayout_340.setContentsMargins(2, 2, 2, 2)
        self.pressure_sv_a_5 = QDoubleSpinBox(self.widget_231)
        self.pressure_sv_a_5.setObjectName(u"pressure_sv_a_5")
        sizePolicy.setHeightForWidth(self.pressure_sv_a_5.sizePolicy().hasHeightForWidth())
        self.pressure_sv_a_5.setSizePolicy(sizePolicy)
        self.pressure_sv_a_5.setFont(font11)
        self.pressure_sv_a_5.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_a_5.setWrapping(False)
        self.pressure_sv_a_5.setAlignment(Qt.AlignCenter)
        self.pressure_sv_a_5.setReadOnly(False)
        self.pressure_sv_a_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_a_5.setDecimals(2)
        self.pressure_sv_a_5.setMaximum(20.000000000000000)
        self.pressure_sv_a_5.setValue(0.000000000000000)

        self.horizontalLayout_340.addWidget(self.pressure_sv_a_5)

        self.horizontalLayout_340.setStretch(0, 1)

        self.horizontalLayout_336.addWidget(self.widget_231)

        self.label_241 = QLabel(self.group_1_val_7)
        self.label_241.setObjectName(u"label_241")
        self.label_241.setFont(font13)
        self.label_241.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_241.setAlignment(Qt.AlignCenter)
        self.label_241.setWordWrap(True)

        self.horizontalLayout_336.addWidget(self.label_241)

        self.horizontalLayout_336.setStretch(0, 6)
        self.horizontalLayout_336.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_1_val_7, 9, 2, 1, 1)

        self.label_name_4 = QWidget(self.widget_6)
        self.label_name_4.setObjectName(u"label_name_4")
        self.horizontalLayout_14 = QHBoxLayout(self.label_name_4)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(3, 3, 3, 3)
        self.label_100 = QLabel(self.label_name_4)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setFont(font11)
        self.label_100.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #e3e6ee\n"
"            );\n"
"}")

        self.horizontalLayout_14.addWidget(self.label_100)


        self.gridLayout.addWidget(self.label_name_4, 6, 0, 1, 1)

        self.group_2_val_8 = QWidget(self.widget_6)
        self.group_2_val_8.setObjectName(u"group_2_val_8")
        self.horizontalLayout_584 = QHBoxLayout(self.group_2_val_8)
        self.horizontalLayout_584.setObjectName(u"horizontalLayout_584")
        self.horizontalLayout_584.setContentsMargins(3, 3, 6, 3)
        self.widget_343 = QWidget(self.group_2_val_8)
        self.widget_343.setObjectName(u"widget_343")
        self.widget_343.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_585 = QHBoxLayout(self.widget_343)
        self.horizontalLayout_585.setObjectName(u"horizontalLayout_585")
        self.horizontalLayout_585.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_12 = QDoubleSpinBox(self.widget_343)
        self.pressure_pv_b_12.setObjectName(u"pressure_pv_b_12")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_12.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_12.setSizePolicy(sizePolicy)
        self.pressure_pv_b_12.setFont(font11)
        self.pressure_pv_b_12.setWrapping(False)
        self.pressure_pv_b_12.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_12.setReadOnly(True)
        self.pressure_pv_b_12.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_12.setDecimals(2)
        self.pressure_pv_b_12.setMaximum(20.000000000000000)
        self.pressure_pv_b_12.setValue(0.000000000000000)

        self.horizontalLayout_585.addWidget(self.pressure_pv_b_12)

        self.horizontalLayout_585.setStretch(0, 1)

        self.horizontalLayout_584.addWidget(self.widget_343)

        self.label_272 = QLabel(self.group_2_val_8)
        self.label_272.setObjectName(u"label_272")
        self.label_272.setFont(font13)
        self.label_272.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_272.setAlignment(Qt.AlignCenter)
        self.label_272.setWordWrap(True)

        self.horizontalLayout_584.addWidget(self.label_272)

        self.horizontalLayout_584.setStretch(0, 6)
        self.horizontalLayout_584.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_2_val_8, 10, 4, 1, 1)

        self.group_3_val_9 = QWidget(self.widget_6)
        self.group_3_val_9.setObjectName(u"group_3_val_9")
        self.horizontalLayout_574 = QHBoxLayout(self.group_3_val_9)
        self.horizontalLayout_574.setObjectName(u"horizontalLayout_574")
        self.horizontalLayout_574.setContentsMargins(3, 3, 6, 3)
        self.widget_301 = QWidget(self.group_3_val_9)
        self.widget_301.setObjectName(u"widget_301")
        self.widget_301.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_575 = QHBoxLayout(self.widget_301)
        self.horizontalLayout_575.setObjectName(u"horizontalLayout_575")
        self.horizontalLayout_575.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_5 = QDoubleSpinBox(self.widget_301)
        self.pressure_pv_c_5.setObjectName(u"pressure_pv_c_5")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_5.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_5.setSizePolicy(sizePolicy)
        self.pressure_pv_c_5.setFont(font11)
        self.pressure_pv_c_5.setWrapping(False)
        self.pressure_pv_c_5.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_5.setReadOnly(True)
        self.pressure_pv_c_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_5.setDecimals(2)
        self.pressure_pv_c_5.setMaximum(20.000000000000000)
        self.pressure_pv_c_5.setValue(0.000000000000000)

        self.horizontalLayout_575.addWidget(self.pressure_pv_c_5)

        self.horizontalLayout_575.setStretch(0, 1)

        self.horizontalLayout_574.addWidget(self.widget_301)

        self.label_269 = QLabel(self.group_3_val_9)
        self.label_269.setObjectName(u"label_269")
        self.label_269.setFont(font13)
        self.label_269.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_269.setAlignment(Qt.AlignCenter)
        self.label_269.setWordWrap(True)

        self.horizontalLayout_574.addWidget(self.label_269)

        self.horizontalLayout_574.setStretch(0, 6)
        self.horizontalLayout_574.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_3_val_9, 11, 6, 1, 1)

        self.label_name_9 = QWidget(self.widget_6)
        self.label_name_9.setObjectName(u"label_name_9")
        self.horizontalLayout_36 = QHBoxLayout(self.label_name_9)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(3, 3, 3, 3)
        self.label_105 = QLabel(self.label_name_9)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setFont(font11)
        self.label_105.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #e3e6ee\n"
"            );\n"
"}")

        self.horizontalLayout_36.addWidget(self.label_105)


        self.gridLayout.addWidget(self.label_name_9, 11, 0, 1, 1)

        self.group_1_val_5 = QWidget(self.widget_6)
        self.group_1_val_5.setObjectName(u"group_1_val_5")
        self.horizontalLayout_504 = QHBoxLayout(self.group_1_val_5)
        self.horizontalLayout_504.setObjectName(u"horizontalLayout_504")
        self.horizontalLayout_504.setContentsMargins(3, 3, 6, 3)
        self.widget_233 = QWidget(self.group_1_val_5)
        self.widget_233.setObjectName(u"widget_233")
        self.widget_233.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_505 = QHBoxLayout(self.widget_233)
        self.horizontalLayout_505.setObjectName(u"horizontalLayout_505")
        self.horizontalLayout_505.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_7 = QDoubleSpinBox(self.widget_233)
        self.pressure_pv_a_7.setObjectName(u"pressure_pv_a_7")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_7.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_7.setSizePolicy(sizePolicy)
        self.pressure_pv_a_7.setFont(font11)
        self.pressure_pv_a_7.setStyleSheet(u"")
        self.pressure_pv_a_7.setWrapping(True)
        self.pressure_pv_a_7.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_7.setReadOnly(True)
        self.pressure_pv_a_7.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_7.setDecimals(1)
        self.pressure_pv_a_7.setMaximum(999.000000000000000)
        self.pressure_pv_a_7.setValue(0.000000000000000)

        self.horizontalLayout_505.addWidget(self.pressure_pv_a_7)

        self.line_45 = QFrame(self.widget_233)
        self.line_45.setObjectName(u"line_45")
        self.line_45.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_45.setFrameShape(QFrame.Shape.VLine)
        self.line_45.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_505.addWidget(self.line_45)

        self.pressure_sv_a_7 = QDoubleSpinBox(self.widget_233)
        self.pressure_sv_a_7.setObjectName(u"pressure_sv_a_7")
        sizePolicy.setHeightForWidth(self.pressure_sv_a_7.sizePolicy().hasHeightForWidth())
        self.pressure_sv_a_7.setSizePolicy(sizePolicy)
        self.pressure_sv_a_7.setFont(font11)
        self.pressure_sv_a_7.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_a_7.setWrapping(False)
        self.pressure_sv_a_7.setAlignment(Qt.AlignCenter)
        self.pressure_sv_a_7.setReadOnly(False)
        self.pressure_sv_a_7.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_a_7.setDecimals(1)
        self.pressure_sv_a_7.setMaximum(999.000000000000000)
        self.pressure_sv_a_7.setValue(0.000000000000000)

        self.horizontalLayout_505.addWidget(self.pressure_sv_a_7)

        self.horizontalLayout_505.setStretch(0, 1)
        self.horizontalLayout_505.setStretch(2, 1)

        self.horizontalLayout_504.addWidget(self.widget_233)

        self.label_243 = QLabel(self.group_1_val_5)
        self.label_243.setObjectName(u"label_243")
        self.label_243.setFont(font13)
        self.label_243.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_243.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_504.addWidget(self.label_243)

        self.horizontalLayout_504.setStretch(0, 6)
        self.horizontalLayout_504.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_1_val_5, 7, 2, 1, 1)

        self.label_name_7 = QWidget(self.widget_6)
        self.label_name_7.setObjectName(u"label_name_7")
        self.horizontalLayout_32 = QHBoxLayout(self.label_name_7)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(3, 3, 3, 3)
        self.label_99 = QLabel(self.label_name_7)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setFont(font11)
        self.label_99.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #e3e6ee\n"
"            );\n"
"}")

        self.horizontalLayout_32.addWidget(self.label_99)


        self.gridLayout.addWidget(self.label_name_7, 9, 0, 1, 1)

        self.group_2_val_7 = QWidget(self.widget_6)
        self.group_2_val_7.setObjectName(u"group_2_val_7")
        self.horizontalLayout_520 = QHBoxLayout(self.group_2_val_7)
        self.horizontalLayout_520.setObjectName(u"horizontalLayout_520")
        self.horizontalLayout_520.setContentsMargins(3, 3, 6, 3)
        self.widget_272 = QWidget(self.group_2_val_7)
        self.widget_272.setObjectName(u"widget_272")
        self.widget_272.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_521 = QHBoxLayout(self.widget_272)
        self.horizontalLayout_521.setObjectName(u"horizontalLayout_521")
        self.horizontalLayout_521.setContentsMargins(2, 2, 2, 2)
        self.pressure_sv_b_5 = QDoubleSpinBox(self.widget_272)
        self.pressure_sv_b_5.setObjectName(u"pressure_sv_b_5")
        sizePolicy.setHeightForWidth(self.pressure_sv_b_5.sizePolicy().hasHeightForWidth())
        self.pressure_sv_b_5.setSizePolicy(sizePolicy)
        self.pressure_sv_b_5.setFont(font11)
        self.pressure_sv_b_5.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_b_5.setWrapping(False)
        self.pressure_sv_b_5.setAlignment(Qt.AlignCenter)
        self.pressure_sv_b_5.setReadOnly(False)
        self.pressure_sv_b_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_b_5.setDecimals(2)
        self.pressure_sv_b_5.setMaximum(20.000000000000000)
        self.pressure_sv_b_5.setValue(0.000000000000000)

        self.horizontalLayout_521.addWidget(self.pressure_sv_b_5)

        self.horizontalLayout_521.setStretch(0, 1)

        self.horizontalLayout_520.addWidget(self.widget_272)

        self.label_253 = QLabel(self.group_2_val_7)
        self.label_253.setObjectName(u"label_253")
        self.label_253.setFont(font13)
        self.label_253.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_253.setAlignment(Qt.AlignCenter)
        self.label_253.setWordWrap(True)

        self.horizontalLayout_520.addWidget(self.label_253)

        self.horizontalLayout_520.setStretch(0, 6)
        self.horizontalLayout_520.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_2_val_7, 9, 4, 1, 1)

        self.label_name_10 = QWidget(self.widget_6)
        self.label_name_10.setObjectName(u"label_name_10")
        self.horizontalLayout_37 = QHBoxLayout(self.label_name_10)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(3, 3, 3, 3)
        self.label_104 = QLabel(self.label_name_10)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setFont(font11)
        self.label_104.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #e3e6ee\n"
"            );\n"
"}")

        self.horizontalLayout_37.addWidget(self.label_104)


        self.gridLayout.addWidget(self.label_name_10, 13, 0, 1, 1)

        self.group_3_val_4 = QWidget(self.widget_6)
        self.group_3_val_4.setObjectName(u"group_3_val_4")
        self.horizontalLayout_550 = QHBoxLayout(self.group_3_val_4)
        self.horizontalLayout_550.setObjectName(u"horizontalLayout_550")
        self.horizontalLayout_550.setContentsMargins(3, 3, 6, 3)
        self.widget_292 = QWidget(self.group_3_val_4)
        self.widget_292.setObjectName(u"widget_292")
        self.widget_292.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_551 = QHBoxLayout(self.widget_292)
        self.horizontalLayout_551.setObjectName(u"horizontalLayout_551")
        self.horizontalLayout_551.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_6 = QDoubleSpinBox(self.widget_292)
        self.pressure_pv_c_6.setObjectName(u"pressure_pv_c_6")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_6.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_6.setSizePolicy(sizePolicy)
        self.pressure_pv_c_6.setFont(font11)
        self.pressure_pv_c_6.setStyleSheet(u"")
        self.pressure_pv_c_6.setWrapping(True)
        self.pressure_pv_c_6.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_6.setReadOnly(True)
        self.pressure_pv_c_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_6.setDecimals(1)
        self.pressure_pv_c_6.setMaximum(999.000000000000000)
        self.pressure_pv_c_6.setValue(0.000000000000000)

        self.horizontalLayout_551.addWidget(self.pressure_pv_c_6)

        self.line_36 = QFrame(self.widget_292)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setStyleSheet(u"border: 1px solid rgb(22, 93, 200);")
        self.line_36.setFrameShape(QFrame.Shape.VLine)
        self.line_36.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_551.addWidget(self.line_36)

        self.pressure_sv_c_6 = QDoubleSpinBox(self.widget_292)
        self.pressure_sv_c_6.setObjectName(u"pressure_sv_c_6")
        sizePolicy.setHeightForWidth(self.pressure_sv_c_6.sizePolicy().hasHeightForWidth())
        self.pressure_sv_c_6.setSizePolicy(sizePolicy)
        self.pressure_sv_c_6.setFont(font11)
        self.pressure_sv_c_6.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_c_6.setWrapping(False)
        self.pressure_sv_c_6.setAlignment(Qt.AlignCenter)
        self.pressure_sv_c_6.setReadOnly(False)
        self.pressure_sv_c_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_c_6.setDecimals(1)
        self.pressure_sv_c_6.setMaximum(999.000000000000000)
        self.pressure_sv_c_6.setValue(0.000000000000000)

        self.horizontalLayout_551.addWidget(self.pressure_sv_c_6)

        self.horizontalLayout_551.setStretch(0, 1)
        self.horizontalLayout_551.setStretch(2, 1)

        self.horizontalLayout_550.addWidget(self.widget_292)

        self.label_264 = QLabel(self.group_3_val_4)
        self.label_264.setObjectName(u"label_264")
        self.label_264.setFont(font13)
        self.label_264.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_264.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_550.addWidget(self.label_264)

        self.horizontalLayout_550.setStretch(0, 6)
        self.horizontalLayout_550.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_3_val_4, 6, 6, 1, 1)

        self.group_2_val_5 = QWidget(self.widget_6)
        self.group_2_val_5.setObjectName(u"group_2_val_5")
        self.horizontalLayout_524 = QHBoxLayout(self.group_2_val_5)
        self.horizontalLayout_524.setObjectName(u"horizontalLayout_524")
        self.horizontalLayout_524.setContentsMargins(3, 3, 6, 3)
        self.widget_274 = QWidget(self.group_2_val_5)
        self.widget_274.setObjectName(u"widget_274")
        self.widget_274.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_525 = QHBoxLayout(self.widget_274)
        self.horizontalLayout_525.setObjectName(u"horizontalLayout_525")
        self.horizontalLayout_525.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_7 = QDoubleSpinBox(self.widget_274)
        self.pressure_pv_b_7.setObjectName(u"pressure_pv_b_7")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_7.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_7.setSizePolicy(sizePolicy)
        self.pressure_pv_b_7.setFont(font11)
        self.pressure_pv_b_7.setStyleSheet(u"")
        self.pressure_pv_b_7.setWrapping(True)
        self.pressure_pv_b_7.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_7.setReadOnly(True)
        self.pressure_pv_b_7.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_7.setDecimals(1)
        self.pressure_pv_b_7.setMaximum(999.000000000000000)
        self.pressure_pv_b_7.setValue(0.000000000000000)

        self.horizontalLayout_525.addWidget(self.pressure_pv_b_7)

        self.line_51 = QFrame(self.widget_274)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setStyleSheet(u"border: 1px solid rgb(22, 93, 200);")
        self.line_51.setFrameShape(QFrame.Shape.VLine)
        self.line_51.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_525.addWidget(self.line_51)

        self.pressure_sv_b_7 = QDoubleSpinBox(self.widget_274)
        self.pressure_sv_b_7.setObjectName(u"pressure_sv_b_7")
        sizePolicy.setHeightForWidth(self.pressure_sv_b_7.sizePolicy().hasHeightForWidth())
        self.pressure_sv_b_7.setSizePolicy(sizePolicy)
        self.pressure_sv_b_7.setFont(font11)
        self.pressure_sv_b_7.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_b_7.setWrapping(False)
        self.pressure_sv_b_7.setAlignment(Qt.AlignCenter)
        self.pressure_sv_b_7.setReadOnly(False)
        self.pressure_sv_b_7.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_b_7.setDecimals(1)
        self.pressure_sv_b_7.setMaximum(999.000000000000000)
        self.pressure_sv_b_7.setValue(0.000000000000000)

        self.horizontalLayout_525.addWidget(self.pressure_sv_b_7)

        self.horizontalLayout_525.setStretch(0, 1)
        self.horizontalLayout_525.setStretch(2, 1)

        self.horizontalLayout_524.addWidget(self.widget_274)

        self.label_255 = QLabel(self.group_2_val_5)
        self.label_255.setObjectName(u"label_255")
        self.label_255.setFont(font13)
        self.label_255.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_255.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_524.addWidget(self.label_255)

        self.horizontalLayout_524.setStretch(0, 6)
        self.horizontalLayout_524.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_2_val_5, 7, 4, 1, 1)

        self.label_name_3 = QWidget(self.widget_6)
        self.label_name_3.setObjectName(u"label_name_3")
        self.horizontalLayout_13 = QHBoxLayout(self.label_name_3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(3, 3, 3, 3)
        self.label_84 = QLabel(self.label_name_3)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setFont(font11)
        self.label_84.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #e3e6ee\n"
"            );\n"
"}")

        self.horizontalLayout_13.addWidget(self.label_84)


        self.gridLayout.addWidget(self.label_name_3, 4, 0, 1, 1)

        self.group_2_val_2 = QWidget(self.widget_6)
        self.group_2_val_2.setObjectName(u"group_2_val_2")
        self.horizontalLayout_508 = QHBoxLayout(self.group_2_val_2)
        self.horizontalLayout_508.setObjectName(u"horizontalLayout_508")
        self.horizontalLayout_508.setContentsMargins(3, 3, 6, 3)
        self.widget_237 = QWidget(self.group_2_val_2)
        self.widget_237.setObjectName(u"widget_237")
        self.widget_237.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_509 = QHBoxLayout(self.widget_237)
        self.horizontalLayout_509.setObjectName(u"horizontalLayout_509")
        self.horizontalLayout_509.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_9 = QDoubleSpinBox(self.widget_237)
        self.pressure_pv_b_9.setObjectName(u"pressure_pv_b_9")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_9.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_9.setSizePolicy(sizePolicy)
        self.pressure_pv_b_9.setFont(font11)
        self.pressure_pv_b_9.setStyleSheet(u"")
        self.pressure_pv_b_9.setWrapping(True)
        self.pressure_pv_b_9.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_9.setReadOnly(True)
        self.pressure_pv_b_9.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_9.setDecimals(1)
        self.pressure_pv_b_9.setMaximum(999.000000000000000)
        self.pressure_pv_b_9.setValue(0.000000000000000)

        self.horizontalLayout_509.addWidget(self.pressure_pv_b_9)

        self.line_53 = QFrame(self.widget_237)
        self.line_53.setObjectName(u"line_53")
        self.line_53.setStyleSheet(u"border: 1px solid rgb(22, 93, 200);")
        self.line_53.setFrameShape(QFrame.Shape.VLine)
        self.line_53.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_509.addWidget(self.line_53)

        self.pressure_sv_b_9 = QDoubleSpinBox(self.widget_237)
        self.pressure_sv_b_9.setObjectName(u"pressure_sv_b_9")
        sizePolicy.setHeightForWidth(self.pressure_sv_b_9.sizePolicy().hasHeightForWidth())
        self.pressure_sv_b_9.setSizePolicy(sizePolicy)
        self.pressure_sv_b_9.setFont(font11)
        self.pressure_sv_b_9.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_b_9.setWrapping(False)
        self.pressure_sv_b_9.setAlignment(Qt.AlignCenter)
        self.pressure_sv_b_9.setReadOnly(False)
        self.pressure_sv_b_9.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_b_9.setDecimals(1)
        self.pressure_sv_b_9.setMaximum(999.000000000000000)
        self.pressure_sv_b_9.setValue(0.000000000000000)

        self.horizontalLayout_509.addWidget(self.pressure_sv_b_9)

        self.horizontalLayout_509.setStretch(0, 1)
        self.horizontalLayout_509.setStretch(2, 1)

        self.horizontalLayout_508.addWidget(self.widget_237)

        self.label_247 = QLabel(self.group_2_val_2)
        self.label_247.setObjectName(u"label_247")
        self.label_247.setFont(font13)
        self.label_247.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_247.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_508.addWidget(self.label_247)

        self.horizontalLayout_508.setStretch(0, 6)
        self.horizontalLayout_508.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_2_val_2, 3, 4, 1, 1)

        self.group_3_val_2 = QWidget(self.widget_6)
        self.group_3_val_2.setObjectName(u"group_3_val_2")
        self.horizontalLayout_544 = QHBoxLayout(self.group_3_val_2)
        self.horizontalLayout_544.setObjectName(u"horizontalLayout_544")
        self.horizontalLayout_544.setContentsMargins(3, 3, 6, 3)
        self.widget_289 = QWidget(self.group_3_val_2)
        self.widget_289.setObjectName(u"widget_289")
        self.widget_289.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_545 = QHBoxLayout(self.widget_289)
        self.horizontalLayout_545.setObjectName(u"horizontalLayout_545")
        self.horizontalLayout_545.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_9 = QDoubleSpinBox(self.widget_289)
        self.pressure_pv_c_9.setObjectName(u"pressure_pv_c_9")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_9.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_9.setSizePolicy(sizePolicy)
        self.pressure_pv_c_9.setFont(font11)
        self.pressure_pv_c_9.setStyleSheet(u"")
        self.pressure_pv_c_9.setWrapping(True)
        self.pressure_pv_c_9.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_9.setReadOnly(True)
        self.pressure_pv_c_9.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_9.setDecimals(1)
        self.pressure_pv_c_9.setMaximum(999.000000000000000)
        self.pressure_pv_c_9.setValue(0.000000000000000)

        self.horizontalLayout_545.addWidget(self.pressure_pv_c_9)

        self.line_56 = QFrame(self.widget_289)
        self.line_56.setObjectName(u"line_56")
        self.line_56.setStyleSheet(u"border: 1px solid rgb(22, 93, 200);")
        self.line_56.setFrameShape(QFrame.Shape.VLine)
        self.line_56.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_545.addWidget(self.line_56)

        self.pressure_sv_c_9 = QDoubleSpinBox(self.widget_289)
        self.pressure_sv_c_9.setObjectName(u"pressure_sv_c_9")
        sizePolicy.setHeightForWidth(self.pressure_sv_c_9.sizePolicy().hasHeightForWidth())
        self.pressure_sv_c_9.setSizePolicy(sizePolicy)
        self.pressure_sv_c_9.setFont(font11)
        self.pressure_sv_c_9.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_c_9.setWrapping(False)
        self.pressure_sv_c_9.setAlignment(Qt.AlignCenter)
        self.pressure_sv_c_9.setReadOnly(False)
        self.pressure_sv_c_9.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_c_9.setDecimals(1)
        self.pressure_sv_c_9.setMaximum(999.000000000000000)
        self.pressure_sv_c_9.setValue(0.000000000000000)

        self.horizontalLayout_545.addWidget(self.pressure_sv_c_9)

        self.horizontalLayout_545.setStretch(0, 1)
        self.horizontalLayout_545.setStretch(2, 1)

        self.horizontalLayout_544.addWidget(self.widget_289)

        self.label_261 = QLabel(self.group_3_val_2)
        self.label_261.setObjectName(u"label_261")
        self.label_261.setFont(font13)
        self.label_261.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_261.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_544.addWidget(self.label_261)

        self.horizontalLayout_544.setStretch(0, 6)
        self.horizontalLayout_544.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_3_val_2, 3, 6, 1, 1)

        self.label_name_6 = QWidget(self.widget_6)
        self.label_name_6.setObjectName(u"label_name_6")
        self.horizontalLayout_28 = QHBoxLayout(self.label_name_6)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(3, 3, 3, 3)
        self.label_102 = QLabel(self.label_name_6)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setFont(font11)
        self.label_102.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #e3e6ee\n"
"            );\n"
"}")

        self.horizontalLayout_28.addWidget(self.label_102)


        self.gridLayout.addWidget(self.label_name_6, 8, 0, 1, 1)

        self.group_1_val_8 = QWidget(self.widget_6)
        self.group_1_val_8.setObjectName(u"group_1_val_8")
        self.horizontalLayout_350 = QHBoxLayout(self.group_1_val_8)
        self.horizontalLayout_350.setObjectName(u"horizontalLayout_350")
        self.horizontalLayout_350.setContentsMargins(3, 3, 6, 3)
        self.widget_339 = QWidget(self.group_1_val_8)
        self.widget_339.setObjectName(u"widget_339")
        self.widget_339.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_351 = QHBoxLayout(self.widget_339)
        self.horizontalLayout_351.setObjectName(u"horizontalLayout_351")
        self.horizontalLayout_351.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_12 = QDoubleSpinBox(self.widget_339)
        self.pressure_pv_a_12.setObjectName(u"pressure_pv_a_12")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_12.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_12.setSizePolicy(sizePolicy)
        self.pressure_pv_a_12.setFont(font11)
        self.pressure_pv_a_12.setWrapping(False)
        self.pressure_pv_a_12.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_12.setReadOnly(True)
        self.pressure_pv_a_12.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_12.setDecimals(2)
        self.pressure_pv_a_12.setMaximum(20.000000000000000)
        self.pressure_pv_a_12.setValue(0.000000000000000)

        self.horizontalLayout_351.addWidget(self.pressure_pv_a_12)

        self.horizontalLayout_351.setStretch(0, 1)

        self.horizontalLayout_350.addWidget(self.widget_339)

        self.label_270 = QLabel(self.group_1_val_8)
        self.label_270.setObjectName(u"label_270")
        self.label_270.setFont(font13)
        self.label_270.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_270.setAlignment(Qt.AlignCenter)
        self.label_270.setWordWrap(True)

        self.horizontalLayout_350.addWidget(self.label_270)

        self.horizontalLayout_350.setStretch(0, 6)
        self.horizontalLayout_350.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_1_val_8, 10, 2, 1, 1)

        self.group_3_val_5 = QWidget(self.widget_6)
        self.group_3_val_5.setObjectName(u"group_3_val_5")
        self.horizontalLayout_552 = QHBoxLayout(self.group_3_val_5)
        self.horizontalLayout_552.setObjectName(u"horizontalLayout_552")
        self.horizontalLayout_552.setContentsMargins(3, 3, 6, 3)
        self.widget_293 = QWidget(self.group_3_val_5)
        self.widget_293.setObjectName(u"widget_293")
        self.widget_293.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_553 = QHBoxLayout(self.widget_293)
        self.horizontalLayout_553.setObjectName(u"horizontalLayout_553")
        self.horizontalLayout_553.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_7 = QDoubleSpinBox(self.widget_293)
        self.pressure_pv_c_7.setObjectName(u"pressure_pv_c_7")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_7.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_7.setSizePolicy(sizePolicy)
        self.pressure_pv_c_7.setFont(font11)
        self.pressure_pv_c_7.setStyleSheet(u"")
        self.pressure_pv_c_7.setWrapping(True)
        self.pressure_pv_c_7.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_7.setReadOnly(True)
        self.pressure_pv_c_7.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_7.setDecimals(1)
        self.pressure_pv_c_7.setMaximum(999.000000000000000)
        self.pressure_pv_c_7.setValue(0.000000000000000)

        self.horizontalLayout_553.addWidget(self.pressure_pv_c_7)

        self.line_37 = QFrame(self.widget_293)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setStyleSheet(u"border: 1px solid rgb(22, 93, 200);")
        self.line_37.setFrameShape(QFrame.Shape.VLine)
        self.line_37.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_553.addWidget(self.line_37)

        self.pressure_sv_c_7 = QDoubleSpinBox(self.widget_293)
        self.pressure_sv_c_7.setObjectName(u"pressure_sv_c_7")
        sizePolicy.setHeightForWidth(self.pressure_sv_c_7.sizePolicy().hasHeightForWidth())
        self.pressure_sv_c_7.setSizePolicy(sizePolicy)
        self.pressure_sv_c_7.setFont(font11)
        self.pressure_sv_c_7.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_c_7.setWrapping(False)
        self.pressure_sv_c_7.setAlignment(Qt.AlignCenter)
        self.pressure_sv_c_7.setReadOnly(False)
        self.pressure_sv_c_7.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_c_7.setDecimals(1)
        self.pressure_sv_c_7.setMaximum(999.000000000000000)
        self.pressure_sv_c_7.setValue(0.000000000000000)

        self.horizontalLayout_553.addWidget(self.pressure_sv_c_7)

        self.horizontalLayout_553.setStretch(0, 1)
        self.horizontalLayout_553.setStretch(2, 1)

        self.horizontalLayout_552.addWidget(self.widget_293)

        self.label_265 = QLabel(self.group_3_val_5)
        self.label_265.setObjectName(u"label_265")
        self.label_265.setFont(font13)
        self.label_265.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_265.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_552.addWidget(self.label_265)

        self.horizontalLayout_552.setStretch(0, 6)
        self.horizontalLayout_552.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_3_val_5, 7, 6, 1, 1)

        self.group_2_val_4 = QWidget(self.widget_6)
        self.group_2_val_4.setObjectName(u"group_2_val_4")
        self.horizontalLayout_522 = QHBoxLayout(self.group_2_val_4)
        self.horizontalLayout_522.setObjectName(u"horizontalLayout_522")
        self.horizontalLayout_522.setContentsMargins(3, 3, 6, 3)
        self.widget_273 = QWidget(self.group_2_val_4)
        self.widget_273.setObjectName(u"widget_273")
        self.widget_273.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_523 = QHBoxLayout(self.widget_273)
        self.horizontalLayout_523.setObjectName(u"horizontalLayout_523")
        self.horizontalLayout_523.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_6 = QDoubleSpinBox(self.widget_273)
        self.pressure_pv_b_6.setObjectName(u"pressure_pv_b_6")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_6.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_6.setSizePolicy(sizePolicy)
        self.pressure_pv_b_6.setFont(font11)
        self.pressure_pv_b_6.setStyleSheet(u"")
        self.pressure_pv_b_6.setWrapping(True)
        self.pressure_pv_b_6.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_6.setReadOnly(True)
        self.pressure_pv_b_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_6.setDecimals(1)
        self.pressure_pv_b_6.setMaximum(999.000000000000000)
        self.pressure_pv_b_6.setValue(0.000000000000000)

        self.horizontalLayout_523.addWidget(self.pressure_pv_b_6)

        self.line_50 = QFrame(self.widget_273)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setStyleSheet(u"border: 1px solid rgb(22, 93, 200);")
        self.line_50.setFrameShape(QFrame.Shape.VLine)
        self.line_50.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_523.addWidget(self.line_50)

        self.pressure_sv_b_6 = QDoubleSpinBox(self.widget_273)
        self.pressure_sv_b_6.setObjectName(u"pressure_sv_b_6")
        sizePolicy.setHeightForWidth(self.pressure_sv_b_6.sizePolicy().hasHeightForWidth())
        self.pressure_sv_b_6.setSizePolicy(sizePolicy)
        self.pressure_sv_b_6.setFont(font11)
        self.pressure_sv_b_6.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_b_6.setWrapping(False)
        self.pressure_sv_b_6.setAlignment(Qt.AlignCenter)
        self.pressure_sv_b_6.setReadOnly(False)
        self.pressure_sv_b_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_b_6.setDecimals(1)
        self.pressure_sv_b_6.setMaximum(999.000000000000000)
        self.pressure_sv_b_6.setValue(0.000000000000000)

        self.horizontalLayout_523.addWidget(self.pressure_sv_b_6)

        self.horizontalLayout_523.setStretch(0, 1)
        self.horizontalLayout_523.setStretch(2, 1)

        self.horizontalLayout_522.addWidget(self.widget_273)

        self.label_254 = QLabel(self.group_2_val_4)
        self.label_254.setObjectName(u"label_254")
        self.label_254.setFont(font13)
        self.label_254.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_254.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_522.addWidget(self.label_254)

        self.horizontalLayout_522.setStretch(0, 6)
        self.horizontalLayout_522.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_2_val_4, 6, 4, 1, 1)

        self.group_3_val_6 = QWidget(self.widget_6)
        self.group_3_val_6.setObjectName(u"group_3_val_6")
        self.horizontalLayout_554 = QHBoxLayout(self.group_3_val_6)
        self.horizontalLayout_554.setObjectName(u"horizontalLayout_554")
        self.horizontalLayout_554.setContentsMargins(3, 3, 6, 3)
        self.widget_294 = QWidget(self.group_3_val_6)
        self.widget_294.setObjectName(u"widget_294")
        self.widget_294.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_555 = QHBoxLayout(self.widget_294)
        self.horizontalLayout_555.setObjectName(u"horizontalLayout_555")
        self.horizontalLayout_555.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_8 = QDoubleSpinBox(self.widget_294)
        self.pressure_pv_c_8.setObjectName(u"pressure_pv_c_8")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_8.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_8.setSizePolicy(sizePolicy)
        self.pressure_pv_c_8.setFont(font11)
        self.pressure_pv_c_8.setStyleSheet(u"")
        self.pressure_pv_c_8.setWrapping(True)
        self.pressure_pv_c_8.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_8.setReadOnly(True)
        self.pressure_pv_c_8.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_8.setDecimals(1)
        self.pressure_pv_c_8.setMaximum(999.000000000000000)
        self.pressure_pv_c_8.setValue(0.000000000000000)

        self.horizontalLayout_555.addWidget(self.pressure_pv_c_8)

        self.line_58 = QFrame(self.widget_294)
        self.line_58.setObjectName(u"line_58")
        self.line_58.setStyleSheet(u"border: 1px solid rgb(22, 93, 200);")
        self.line_58.setFrameShape(QFrame.Shape.VLine)
        self.line_58.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_555.addWidget(self.line_58)

        self.pressure_sv_c_8 = QDoubleSpinBox(self.widget_294)
        self.pressure_sv_c_8.setObjectName(u"pressure_sv_c_8")
        sizePolicy.setHeightForWidth(self.pressure_sv_c_8.sizePolicy().hasHeightForWidth())
        self.pressure_sv_c_8.setSizePolicy(sizePolicy)
        self.pressure_sv_c_8.setFont(font11)
        self.pressure_sv_c_8.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_c_8.setWrapping(False)
        self.pressure_sv_c_8.setAlignment(Qt.AlignCenter)
        self.pressure_sv_c_8.setReadOnly(False)
        self.pressure_sv_c_8.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_c_8.setDecimals(1)
        self.pressure_sv_c_8.setMaximum(999.000000000000000)
        self.pressure_sv_c_8.setValue(0.000000000000000)

        self.horizontalLayout_555.addWidget(self.pressure_sv_c_8)

        self.horizontalLayout_555.setStretch(0, 1)
        self.horizontalLayout_555.setStretch(2, 1)

        self.horizontalLayout_554.addWidget(self.widget_294)

        self.label_266 = QLabel(self.group_3_val_6)
        self.label_266.setObjectName(u"label_266")
        self.label_266.setFont(font13)
        self.label_266.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_266.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_554.addWidget(self.label_266)

        self.horizontalLayout_554.setStretch(0, 6)
        self.horizontalLayout_554.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_3_val_6, 8, 6, 1, 1)

        self.group_3_val_8 = QWidget(self.widget_6)
        self.group_3_val_8.setObjectName(u"group_3_val_8")
        self.horizontalLayout_582 = QHBoxLayout(self.group_3_val_8)
        self.horizontalLayout_582.setObjectName(u"horizontalLayout_582")
        self.horizontalLayout_582.setContentsMargins(3, 3, 6, 3)
        self.widget_341 = QWidget(self.group_3_val_8)
        self.widget_341.setObjectName(u"widget_341")
        self.widget_341.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_583 = QHBoxLayout(self.widget_341)
        self.horizontalLayout_583.setObjectName(u"horizontalLayout_583")
        self.horizontalLayout_583.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_12 = QDoubleSpinBox(self.widget_341)
        self.pressure_pv_c_12.setObjectName(u"pressure_pv_c_12")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_12.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_12.setSizePolicy(sizePolicy)
        self.pressure_pv_c_12.setFont(font11)
        self.pressure_pv_c_12.setWrapping(False)
        self.pressure_pv_c_12.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_12.setReadOnly(True)
        self.pressure_pv_c_12.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_12.setDecimals(2)
        self.pressure_pv_c_12.setMaximum(20.000000000000000)
        self.pressure_pv_c_12.setValue(0.000000000000000)

        self.horizontalLayout_583.addWidget(self.pressure_pv_c_12)

        self.horizontalLayout_583.setStretch(0, 1)

        self.horizontalLayout_582.addWidget(self.widget_341)

        self.label_271 = QLabel(self.group_3_val_8)
        self.label_271.setObjectName(u"label_271")
        self.label_271.setFont(font13)
        self.label_271.setStyleSheet(u"QLabel{\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"}")
        self.label_271.setAlignment(Qt.AlignCenter)
        self.label_271.setWordWrap(True)

        self.horizontalLayout_582.addWidget(self.label_271)

        self.horizontalLayout_582.setStretch(0, 6)
        self.horizontalLayout_582.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_3_val_8, 10, 6, 1, 1)

        self.label_name_13 = QWidget(self.widget_6)
        self.label_name_13.setObjectName(u"label_name_13")
        self.horizontalLayout_40 = QHBoxLayout(self.label_name_13)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(3, 3, 3, 3)
        self.label_97 = QLabel(self.label_name_13)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setFont(font11)
        self.label_97.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #e3e6ee\n"
"            );\n"
"}")

        self.horizontalLayout_40.addWidget(self.label_97)


        self.gridLayout.addWidget(self.label_name_13, 16, 0, 1, 1)

        self.group_2_val_11 = QWidget(self.widget_6)
        self.group_2_val_11.setObjectName(u"group_2_val_11")
        self.horizontalLayout_532 = QHBoxLayout(self.group_2_val_11)
        self.horizontalLayout_532.setSpacing(7)
        self.horizontalLayout_532.setObjectName(u"horizontalLayout_532")
        self.horizontalLayout_532.setContentsMargins(3, 3, 6, 3)
        self.widget_286 = QWidget(self.group_2_val_11)
        self.widget_286.setObjectName(u"widget_286")
        self.widget_286.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_533 = QHBoxLayout(self.widget_286)
        self.horizontalLayout_533.setObjectName(u"horizontalLayout_533")
        self.horizontalLayout_533.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_2 = QDoubleSpinBox(self.widget_286)
        self.pressure_pv_b_2.setObjectName(u"pressure_pv_b_2")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_2.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_2.setSizePolicy(sizePolicy)
        self.pressure_pv_b_2.setFont(font11)
        self.pressure_pv_b_2.setStyleSheet(u"")
        self.pressure_pv_b_2.setWrapping(True)
        self.pressure_pv_b_2.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_2.setReadOnly(True)
        self.pressure_pv_b_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_2.setDecimals(1)
        self.pressure_pv_b_2.setMaximum(999.000000000000000)
        self.pressure_pv_b_2.setValue(0.000000000000000)

        self.horizontalLayout_533.addWidget(self.pressure_pv_b_2)

        self.horizontalLayout_533.setStretch(0, 1)

        self.horizontalLayout_532.addWidget(self.widget_286)

        self.stacked_cel_fah_press_b_2 = QStackedWidget(self.group_2_val_11)
        self.stacked_cel_fah_press_b_2.setObjectName(u"stacked_cel_fah_press_b_2")
        self.celsius_ap_44 = QWidget()
        self.celsius_ap_44.setObjectName(u"celsius_ap_44")
        self.horizontalLayout_534 = QHBoxLayout(self.celsius_ap_44)
        self.horizontalLayout_534.setObjectName(u"horizontalLayout_534")
        self.horizontalLayout_534.setContentsMargins(0, 0, 0, 0)
        self.label_392 = QLabel(self.celsius_ap_44)
        self.label_392.setObjectName(u"label_392")
        self.label_392.setFont(font13)
        self.label_392.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_392.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_534.addWidget(self.label_392)

        self.stacked_cel_fah_press_b_2.addWidget(self.celsius_ap_44)
        self.fahrenheit_ap_44 = QWidget()
        self.fahrenheit_ap_44.setObjectName(u"fahrenheit_ap_44")
        self.horizontalLayout_535 = QHBoxLayout(self.fahrenheit_ap_44)
        self.horizontalLayout_535.setObjectName(u"horizontalLayout_535")
        self.horizontalLayout_535.setContentsMargins(0, 0, 0, 0)
        self.label_393 = QLabel(self.fahrenheit_ap_44)
        self.label_393.setObjectName(u"label_393")
        self.label_393.setFont(font13)
        self.label_393.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_393.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_535.addWidget(self.label_393)

        self.stacked_cel_fah_press_b_2.addWidget(self.fahrenheit_ap_44)

        self.horizontalLayout_532.addWidget(self.stacked_cel_fah_press_b_2)

        self.horizontalLayout_532.setStretch(0, 6)
        self.horizontalLayout_532.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_2_val_11, 14, 4, 1, 1)

        self.group_2_val_12 = QWidget(self.widget_6)
        self.group_2_val_12.setObjectName(u"group_2_val_12")
        self.horizontalLayout_536 = QHBoxLayout(self.group_2_val_12)
        self.horizontalLayout_536.setSpacing(7)
        self.horizontalLayout_536.setObjectName(u"horizontalLayout_536")
        self.horizontalLayout_536.setContentsMargins(3, 3, 6, 3)
        self.widget_287 = QWidget(self.group_2_val_12)
        self.widget_287.setObjectName(u"widget_287")
        self.widget_287.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_537 = QHBoxLayout(self.widget_287)
        self.horizontalLayout_537.setObjectName(u"horizontalLayout_537")
        self.horizontalLayout_537.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_3 = QDoubleSpinBox(self.widget_287)
        self.pressure_pv_b_3.setObjectName(u"pressure_pv_b_3")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_3.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_3.setSizePolicy(sizePolicy)
        self.pressure_pv_b_3.setFont(font11)
        self.pressure_pv_b_3.setStyleSheet(u"")
        self.pressure_pv_b_3.setWrapping(True)
        self.pressure_pv_b_3.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_3.setReadOnly(True)
        self.pressure_pv_b_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_3.setDecimals(1)
        self.pressure_pv_b_3.setMaximum(999.000000000000000)
        self.pressure_pv_b_3.setValue(0.000000000000000)

        self.horizontalLayout_537.addWidget(self.pressure_pv_b_3)

        self.horizontalLayout_537.setStretch(0, 1)

        self.horizontalLayout_536.addWidget(self.widget_287)

        self.stacked_cel_fah_press_b_3 = QStackedWidget(self.group_2_val_12)
        self.stacked_cel_fah_press_b_3.setObjectName(u"stacked_cel_fah_press_b_3")
        self.celsius_ap_45 = QWidget()
        self.celsius_ap_45.setObjectName(u"celsius_ap_45")
        self.horizontalLayout_538 = QHBoxLayout(self.celsius_ap_45)
        self.horizontalLayout_538.setObjectName(u"horizontalLayout_538")
        self.horizontalLayout_538.setContentsMargins(0, 0, 0, 0)
        self.label_394 = QLabel(self.celsius_ap_45)
        self.label_394.setObjectName(u"label_394")
        self.label_394.setFont(font13)
        self.label_394.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_394.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_538.addWidget(self.label_394)

        self.stacked_cel_fah_press_b_3.addWidget(self.celsius_ap_45)
        self.fahrenheit_ap_45 = QWidget()
        self.fahrenheit_ap_45.setObjectName(u"fahrenheit_ap_45")
        self.horizontalLayout_539 = QHBoxLayout(self.fahrenheit_ap_45)
        self.horizontalLayout_539.setObjectName(u"horizontalLayout_539")
        self.horizontalLayout_539.setContentsMargins(0, 0, 0, 0)
        self.label_395 = QLabel(self.fahrenheit_ap_45)
        self.label_395.setObjectName(u"label_395")
        self.label_395.setFont(font13)
        self.label_395.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_395.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_539.addWidget(self.label_395)

        self.stacked_cel_fah_press_b_3.addWidget(self.fahrenheit_ap_45)

        self.horizontalLayout_536.addWidget(self.stacked_cel_fah_press_b_3)

        self.horizontalLayout_536.setStretch(0, 6)
        self.horizontalLayout_536.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_2_val_12, 15, 4, 1, 1)

        self.group_1_val_13 = QWidget(self.widget_6)
        self.group_1_val_13.setObjectName(u"group_1_val_13")
        self.horizontalLayout_346 = QHBoxLayout(self.group_1_val_13)
        self.horizontalLayout_346.setSpacing(7)
        self.horizontalLayout_346.setObjectName(u"horizontalLayout_346")
        self.horizontalLayout_346.setContentsMargins(3, 3, 6, 3)
        self.widget_271 = QWidget(self.group_1_val_13)
        self.widget_271.setObjectName(u"widget_271")
        self.widget_271.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_347 = QHBoxLayout(self.widget_271)
        self.horizontalLayout_347.setObjectName(u"horizontalLayout_347")
        self.horizontalLayout_347.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_4 = QDoubleSpinBox(self.widget_271)
        self.pressure_pv_a_4.setObjectName(u"pressure_pv_a_4")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_4.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_4.setSizePolicy(sizePolicy)
        self.pressure_pv_a_4.setFont(font11)
        self.pressure_pv_a_4.setStyleSheet(u"")
        self.pressure_pv_a_4.setWrapping(True)
        self.pressure_pv_a_4.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_4.setReadOnly(True)
        self.pressure_pv_a_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_4.setDecimals(1)
        self.pressure_pv_a_4.setMaximum(999.000000000000000)
        self.pressure_pv_a_4.setValue(0.000000000000000)

        self.horizontalLayout_347.addWidget(self.pressure_pv_a_4)

        self.horizontalLayout_347.setStretch(0, 1)

        self.horizontalLayout_346.addWidget(self.widget_271)

        self.stacked_cel_fah_press_a_4 = QStackedWidget(self.group_1_val_13)
        self.stacked_cel_fah_press_a_4.setObjectName(u"stacked_cel_fah_press_a_4")
        self.celsius_ap_42 = QWidget()
        self.celsius_ap_42.setObjectName(u"celsius_ap_42")
        self.horizontalLayout_518 = QHBoxLayout(self.celsius_ap_42)
        self.horizontalLayout_518.setObjectName(u"horizontalLayout_518")
        self.horizontalLayout_518.setContentsMargins(0, 0, 0, 0)
        self.label_383 = QLabel(self.celsius_ap_42)
        self.label_383.setObjectName(u"label_383")
        self.label_383.setFont(font13)
        self.label_383.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_383.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_518.addWidget(self.label_383)

        self.stacked_cel_fah_press_a_4.addWidget(self.celsius_ap_42)
        self.fahrenheit_ap_42 = QWidget()
        self.fahrenheit_ap_42.setObjectName(u"fahrenheit_ap_42")
        self.horizontalLayout_519 = QHBoxLayout(self.fahrenheit_ap_42)
        self.horizontalLayout_519.setObjectName(u"horizontalLayout_519")
        self.horizontalLayout_519.setContentsMargins(0, 0, 0, 0)
        self.label_384 = QLabel(self.fahrenheit_ap_42)
        self.label_384.setObjectName(u"label_384")
        self.label_384.setFont(font13)
        self.label_384.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_384.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_519.addWidget(self.label_384)

        self.stacked_cel_fah_press_a_4.addWidget(self.fahrenheit_ap_42)

        self.horizontalLayout_346.addWidget(self.stacked_cel_fah_press_a_4)

        self.horizontalLayout_346.setStretch(0, 6)
        self.horizontalLayout_346.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_1_val_13, 16, 2, 1, 1)

        self.group_3_val_13 = QWidget(self.widget_6)
        self.group_3_val_13.setObjectName(u"group_3_val_13")
        self.horizontalLayout_568 = QHBoxLayout(self.group_3_val_13)
        self.horizontalLayout_568.setSpacing(7)
        self.horizontalLayout_568.setObjectName(u"horizontalLayout_568")
        self.horizontalLayout_568.setContentsMargins(3, 3, 6, 3)
        self.widget_298 = QWidget(self.group_3_val_13)
        self.widget_298.setObjectName(u"widget_298")
        self.widget_298.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_569 = QHBoxLayout(self.widget_298)
        self.horizontalLayout_569.setObjectName(u"horizontalLayout_569")
        self.horizontalLayout_569.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_4 = QDoubleSpinBox(self.widget_298)
        self.pressure_pv_c_4.setObjectName(u"pressure_pv_c_4")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_4.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_4.setSizePolicy(sizePolicy)
        self.pressure_pv_c_4.setFont(font11)
        self.pressure_pv_c_4.setStyleSheet(u"")
        self.pressure_pv_c_4.setWrapping(True)
        self.pressure_pv_c_4.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_4.setReadOnly(True)
        self.pressure_pv_c_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_4.setDecimals(1)
        self.pressure_pv_c_4.setMaximum(999.000000000000000)
        self.pressure_pv_c_4.setValue(0.000000000000000)

        self.horizontalLayout_569.addWidget(self.pressure_pv_c_4)

        self.horizontalLayout_569.setStretch(0, 1)

        self.horizontalLayout_568.addWidget(self.widget_298)

        self.stacked_cel_fah_press_c_4 = QStackedWidget(self.group_3_val_13)
        self.stacked_cel_fah_press_c_4.setObjectName(u"stacked_cel_fah_press_c_4")
        self.celsius_ap_50 = QWidget()
        self.celsius_ap_50.setObjectName(u"celsius_ap_50")
        self.horizontalLayout_570 = QHBoxLayout(self.celsius_ap_50)
        self.horizontalLayout_570.setObjectName(u"horizontalLayout_570")
        self.horizontalLayout_570.setContentsMargins(0, 0, 0, 0)
        self.label_403 = QLabel(self.celsius_ap_50)
        self.label_403.setObjectName(u"label_403")
        self.label_403.setFont(font13)
        self.label_403.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_403.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_570.addWidget(self.label_403)

        self.stacked_cel_fah_press_c_4.addWidget(self.celsius_ap_50)
        self.fahrenheit_ap_50 = QWidget()
        self.fahrenheit_ap_50.setObjectName(u"fahrenheit_ap_50")
        self.horizontalLayout_571 = QHBoxLayout(self.fahrenheit_ap_50)
        self.horizontalLayout_571.setObjectName(u"horizontalLayout_571")
        self.horizontalLayout_571.setContentsMargins(0, 0, 0, 0)
        self.label_404 = QLabel(self.fahrenheit_ap_50)
        self.label_404.setObjectName(u"label_404")
        self.label_404.setFont(font13)
        self.label_404.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_404.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_571.addWidget(self.label_404)

        self.stacked_cel_fah_press_c_4.addWidget(self.fahrenheit_ap_50)

        self.horizontalLayout_568.addWidget(self.stacked_cel_fah_press_c_4)

        self.horizontalLayout_568.setStretch(0, 6)
        self.horizontalLayout_568.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_3_val_13, 16, 6, 1, 1)

        self.group_2_val_13 = QWidget(self.widget_6)
        self.group_2_val_13.setObjectName(u"group_2_val_13")
        self.horizontalLayout_540 = QHBoxLayout(self.group_2_val_13)
        self.horizontalLayout_540.setSpacing(7)
        self.horizontalLayout_540.setObjectName(u"horizontalLayout_540")
        self.horizontalLayout_540.setContentsMargins(3, 3, 6, 3)
        self.widget_288 = QWidget(self.group_2_val_13)
        self.widget_288.setObjectName(u"widget_288")
        self.widget_288.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_541 = QHBoxLayout(self.widget_288)
        self.horizontalLayout_541.setObjectName(u"horizontalLayout_541")
        self.horizontalLayout_541.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_4 = QDoubleSpinBox(self.widget_288)
        self.pressure_pv_b_4.setObjectName(u"pressure_pv_b_4")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_4.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_4.setSizePolicy(sizePolicy)
        self.pressure_pv_b_4.setFont(font11)
        self.pressure_pv_b_4.setStyleSheet(u"")
        self.pressure_pv_b_4.setWrapping(True)
        self.pressure_pv_b_4.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_4.setReadOnly(True)
        self.pressure_pv_b_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_4.setDecimals(1)
        self.pressure_pv_b_4.setMaximum(999.000000000000000)
        self.pressure_pv_b_4.setValue(0.000000000000000)

        self.horizontalLayout_541.addWidget(self.pressure_pv_b_4)

        self.horizontalLayout_541.setStretch(0, 1)

        self.horizontalLayout_540.addWidget(self.widget_288)

        self.stacked_cel_fah_press_b_4 = QStackedWidget(self.group_2_val_13)
        self.stacked_cel_fah_press_b_4.setObjectName(u"stacked_cel_fah_press_b_4")
        self.celsius_ap_46 = QWidget()
        self.celsius_ap_46.setObjectName(u"celsius_ap_46")
        self.horizontalLayout_542 = QHBoxLayout(self.celsius_ap_46)
        self.horizontalLayout_542.setObjectName(u"horizontalLayout_542")
        self.horizontalLayout_542.setContentsMargins(0, 0, 0, 0)
        self.label_396 = QLabel(self.celsius_ap_46)
        self.label_396.setObjectName(u"label_396")
        self.label_396.setFont(font13)
        self.label_396.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_396.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_542.addWidget(self.label_396)

        self.stacked_cel_fah_press_b_4.addWidget(self.celsius_ap_46)
        self.fahrenheit_ap_46 = QWidget()
        self.fahrenheit_ap_46.setObjectName(u"fahrenheit_ap_46")
        self.horizontalLayout_543 = QHBoxLayout(self.fahrenheit_ap_46)
        self.horizontalLayout_543.setObjectName(u"horizontalLayout_543")
        self.horizontalLayout_543.setContentsMargins(0, 0, 0, 0)
        self.label_397 = QLabel(self.fahrenheit_ap_46)
        self.label_397.setObjectName(u"label_397")
        self.label_397.setFont(font13)
        self.label_397.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_397.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_543.addWidget(self.label_397)

        self.stacked_cel_fah_press_b_4.addWidget(self.fahrenheit_ap_46)

        self.horizontalLayout_540.addWidget(self.stacked_cel_fah_press_b_4)

        self.horizontalLayout_540.setStretch(0, 6)
        self.horizontalLayout_540.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_2_val_13, 16, 4, 1, 1)

        self.group_2_val_10 = QWidget(self.widget_6)
        self.group_2_val_10.setObjectName(u"group_2_val_10")
        self.horizontalLayout_528 = QHBoxLayout(self.group_2_val_10)
        self.horizontalLayout_528.setSpacing(7)
        self.horizontalLayout_528.setObjectName(u"horizontalLayout_528")
        self.horizontalLayout_528.setContentsMargins(3, 3, 6, 3)
        self.widget_285 = QWidget(self.group_2_val_10)
        self.widget_285.setObjectName(u"widget_285")
        self.widget_285.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_529 = QHBoxLayout(self.widget_285)
        self.horizontalLayout_529.setObjectName(u"horizontalLayout_529")
        self.horizontalLayout_529.setContentsMargins(2, 2, 2, 2)
        self.pressure_sv_b_1 = QDoubleSpinBox(self.widget_285)
        self.pressure_sv_b_1.setObjectName(u"pressure_sv_b_1")
        sizePolicy.setHeightForWidth(self.pressure_sv_b_1.sizePolicy().hasHeightForWidth())
        self.pressure_sv_b_1.setSizePolicy(sizePolicy)
        self.pressure_sv_b_1.setFont(font11)
        self.pressure_sv_b_1.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_b_1.setWrapping(False)
        self.pressure_sv_b_1.setAlignment(Qt.AlignCenter)
        self.pressure_sv_b_1.setReadOnly(False)
        self.pressure_sv_b_1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_b_1.setDecimals(1)
        self.pressure_sv_b_1.setMaximum(999.000000000000000)
        self.pressure_sv_b_1.setValue(0.000000000000000)

        self.horizontalLayout_529.addWidget(self.pressure_sv_b_1)

        self.horizontalLayout_529.setStretch(0, 1)

        self.horizontalLayout_528.addWidget(self.widget_285)

        self.stacked_cel_fah_press_b_1 = QStackedWidget(self.group_2_val_10)
        self.stacked_cel_fah_press_b_1.setObjectName(u"stacked_cel_fah_press_b_1")
        self.celsius_ap_43 = QWidget()
        self.celsius_ap_43.setObjectName(u"celsius_ap_43")
        self.horizontalLayout_530 = QHBoxLayout(self.celsius_ap_43)
        self.horizontalLayout_530.setObjectName(u"horizontalLayout_530")
        self.horizontalLayout_530.setContentsMargins(0, 0, 0, 0)
        self.label_281 = QLabel(self.celsius_ap_43)
        self.label_281.setObjectName(u"label_281")
        self.label_281.setFont(font13)
        self.label_281.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_281.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_530.addWidget(self.label_281)

        self.stacked_cel_fah_press_b_1.addWidget(self.celsius_ap_43)
        self.fahrenheit_ap_43 = QWidget()
        self.fahrenheit_ap_43.setObjectName(u"fahrenheit_ap_43")
        self.horizontalLayout_531 = QHBoxLayout(self.fahrenheit_ap_43)
        self.horizontalLayout_531.setObjectName(u"horizontalLayout_531")
        self.horizontalLayout_531.setContentsMargins(0, 0, 0, 0)
        self.label_366 = QLabel(self.fahrenheit_ap_43)
        self.label_366.setObjectName(u"label_366")
        self.label_366.setFont(font13)
        self.label_366.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_366.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_531.addWidget(self.label_366)

        self.stacked_cel_fah_press_b_1.addWidget(self.fahrenheit_ap_43)

        self.horizontalLayout_528.addWidget(self.stacked_cel_fah_press_b_1)

        self.horizontalLayout_528.setStretch(0, 6)
        self.horizontalLayout_528.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_2_val_10, 13, 4, 1, 1)

        self.group_1_val_12 = QWidget(self.widget_6)
        self.group_1_val_12.setObjectName(u"group_1_val_12")
        self.horizontalLayout_344 = QHBoxLayout(self.group_1_val_12)
        self.horizontalLayout_344.setSpacing(7)
        self.horizontalLayout_344.setObjectName(u"horizontalLayout_344")
        self.horizontalLayout_344.setContentsMargins(3, 3, 6, 3)
        self.widget_270 = QWidget(self.group_1_val_12)
        self.widget_270.setObjectName(u"widget_270")
        self.widget_270.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_345 = QHBoxLayout(self.widget_270)
        self.horizontalLayout_345.setObjectName(u"horizontalLayout_345")
        self.horizontalLayout_345.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_3 = QDoubleSpinBox(self.widget_270)
        self.pressure_pv_a_3.setObjectName(u"pressure_pv_a_3")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_3.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_3.setSizePolicy(sizePolicy)
        self.pressure_pv_a_3.setFont(font11)
        self.pressure_pv_a_3.setStyleSheet(u"")
        self.pressure_pv_a_3.setWrapping(True)
        self.pressure_pv_a_3.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_3.setReadOnly(True)
        self.pressure_pv_a_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_3.setDecimals(1)
        self.pressure_pv_a_3.setMaximum(999.000000000000000)
        self.pressure_pv_a_3.setValue(0.000000000000000)

        self.horizontalLayout_345.addWidget(self.pressure_pv_a_3)

        self.horizontalLayout_345.setStretch(0, 1)

        self.horizontalLayout_344.addWidget(self.widget_270)

        self.stacked_cel_fah_press_a_3 = QStackedWidget(self.group_1_val_12)
        self.stacked_cel_fah_press_a_3.setObjectName(u"stacked_cel_fah_press_a_3")
        self.celsius_ap_41 = QWidget()
        self.celsius_ap_41.setObjectName(u"celsius_ap_41")
        self.horizontalLayout_516 = QHBoxLayout(self.celsius_ap_41)
        self.horizontalLayout_516.setObjectName(u"horizontalLayout_516")
        self.horizontalLayout_516.setContentsMargins(0, 0, 0, 0)
        self.label_381 = QLabel(self.celsius_ap_41)
        self.label_381.setObjectName(u"label_381")
        self.label_381.setFont(font13)
        self.label_381.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_381.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_516.addWidget(self.label_381)

        self.stacked_cel_fah_press_a_3.addWidget(self.celsius_ap_41)
        self.fahrenheit_ap_41 = QWidget()
        self.fahrenheit_ap_41.setObjectName(u"fahrenheit_ap_41")
        self.horizontalLayout_517 = QHBoxLayout(self.fahrenheit_ap_41)
        self.horizontalLayout_517.setObjectName(u"horizontalLayout_517")
        self.horizontalLayout_517.setContentsMargins(0, 0, 0, 0)
        self.label_382 = QLabel(self.fahrenheit_ap_41)
        self.label_382.setObjectName(u"label_382")
        self.label_382.setFont(font13)
        self.label_382.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_382.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_517.addWidget(self.label_382)

        self.stacked_cel_fah_press_a_3.addWidget(self.fahrenheit_ap_41)

        self.horizontalLayout_344.addWidget(self.stacked_cel_fah_press_a_3)

        self.horizontalLayout_344.setStretch(0, 6)
        self.horizontalLayout_344.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_1_val_12, 15, 2, 1, 1)

        self.group_3_val_11 = QWidget(self.widget_6)
        self.group_3_val_11.setObjectName(u"group_3_val_11")
        self.horizontalLayout_560 = QHBoxLayout(self.group_3_val_11)
        self.horizontalLayout_560.setSpacing(7)
        self.horizontalLayout_560.setObjectName(u"horizontalLayout_560")
        self.horizontalLayout_560.setContentsMargins(3, 3, 6, 3)
        self.widget_296 = QWidget(self.group_3_val_11)
        self.widget_296.setObjectName(u"widget_296")
        self.widget_296.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_561 = QHBoxLayout(self.widget_296)
        self.horizontalLayout_561.setObjectName(u"horizontalLayout_561")
        self.horizontalLayout_561.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_2 = QDoubleSpinBox(self.widget_296)
        self.pressure_pv_c_2.setObjectName(u"pressure_pv_c_2")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_2.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_2.setSizePolicy(sizePolicy)
        self.pressure_pv_c_2.setFont(font11)
        self.pressure_pv_c_2.setStyleSheet(u"")
        self.pressure_pv_c_2.setWrapping(True)
        self.pressure_pv_c_2.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_2.setReadOnly(True)
        self.pressure_pv_c_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_2.setDecimals(1)
        self.pressure_pv_c_2.setMaximum(999.000000000000000)
        self.pressure_pv_c_2.setValue(0.000000000000000)

        self.horizontalLayout_561.addWidget(self.pressure_pv_c_2)

        self.horizontalLayout_561.setStretch(0, 1)

        self.horizontalLayout_560.addWidget(self.widget_296)

        self.stacked_cel_fah_press_c_2 = QStackedWidget(self.group_3_val_11)
        self.stacked_cel_fah_press_c_2.setObjectName(u"stacked_cel_fah_press_c_2")
        self.celsius_ap_48 = QWidget()
        self.celsius_ap_48.setObjectName(u"celsius_ap_48")
        self.horizontalLayout_562 = QHBoxLayout(self.celsius_ap_48)
        self.horizontalLayout_562.setObjectName(u"horizontalLayout_562")
        self.horizontalLayout_562.setContentsMargins(0, 0, 0, 0)
        self.label_282 = QLabel(self.celsius_ap_48)
        self.label_282.setObjectName(u"label_282")
        self.label_282.setFont(font13)
        self.label_282.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_282.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_562.addWidget(self.label_282)

        self.stacked_cel_fah_press_c_2.addWidget(self.celsius_ap_48)
        self.fahrenheit_ap_48 = QWidget()
        self.fahrenheit_ap_48.setObjectName(u"fahrenheit_ap_48")
        self.horizontalLayout_563 = QHBoxLayout(self.fahrenheit_ap_48)
        self.horizontalLayout_563.setObjectName(u"horizontalLayout_563")
        self.horizontalLayout_563.setContentsMargins(0, 0, 0, 0)
        self.label_400 = QLabel(self.fahrenheit_ap_48)
        self.label_400.setObjectName(u"label_400")
        self.label_400.setFont(font13)
        self.label_400.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_400.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_563.addWidget(self.label_400)

        self.stacked_cel_fah_press_c_2.addWidget(self.fahrenheit_ap_48)

        self.horizontalLayout_560.addWidget(self.stacked_cel_fah_press_c_2)

        self.horizontalLayout_560.setStretch(0, 6)
        self.horizontalLayout_560.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_3_val_11, 14, 6, 1, 1)

        self.label_name_12 = QWidget(self.widget_6)
        self.label_name_12.setObjectName(u"label_name_12")
        self.horizontalLayout_39 = QHBoxLayout(self.label_name_12)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(3, 3, 3, 3)
        self.label_98 = QLabel(self.label_name_12)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setFont(font11)
        self.label_98.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #e3e6ee\n"
"            );\n"
"}")

        self.horizontalLayout_39.addWidget(self.label_98)


        self.gridLayout.addWidget(self.label_name_12, 15, 0, 1, 1)

        self.label_name_11 = QWidget(self.widget_6)
        self.label_name_11.setObjectName(u"label_name_11")
        self.horizontalLayout_38 = QHBoxLayout(self.label_name_11)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(3, 3, 3, 3)
        self.label_103 = QLabel(self.label_name_11)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setFont(font11)
        self.label_103.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;\n"
"	border-left: none;\n"
"	color: rgb(97, 97, 97);\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #e3e6ee\n"
"            );\n"
"}")

        self.horizontalLayout_38.addWidget(self.label_103)


        self.gridLayout.addWidget(self.label_name_11, 14, 0, 1, 1)

        self.group_3_val_12 = QWidget(self.widget_6)
        self.group_3_val_12.setObjectName(u"group_3_val_12")
        self.horizontalLayout_564 = QHBoxLayout(self.group_3_val_12)
        self.horizontalLayout_564.setSpacing(7)
        self.horizontalLayout_564.setObjectName(u"horizontalLayout_564")
        self.horizontalLayout_564.setContentsMargins(3, 3, 6, 3)
        self.widget_297 = QWidget(self.group_3_val_12)
        self.widget_297.setObjectName(u"widget_297")
        self.widget_297.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_565 = QHBoxLayout(self.widget_297)
        self.horizontalLayout_565.setObjectName(u"horizontalLayout_565")
        self.horizontalLayout_565.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_3 = QDoubleSpinBox(self.widget_297)
        self.pressure_pv_c_3.setObjectName(u"pressure_pv_c_3")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_3.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_3.setSizePolicy(sizePolicy)
        self.pressure_pv_c_3.setFont(font11)
        self.pressure_pv_c_3.setStyleSheet(u"")
        self.pressure_pv_c_3.setWrapping(True)
        self.pressure_pv_c_3.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_3.setReadOnly(True)
        self.pressure_pv_c_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_3.setDecimals(1)
        self.pressure_pv_c_3.setMaximum(999.000000000000000)
        self.pressure_pv_c_3.setValue(0.000000000000000)

        self.horizontalLayout_565.addWidget(self.pressure_pv_c_3)

        self.horizontalLayout_565.setStretch(0, 1)

        self.horizontalLayout_564.addWidget(self.widget_297)

        self.stacked_cel_fah_press_c_3 = QStackedWidget(self.group_3_val_12)
        self.stacked_cel_fah_press_c_3.setObjectName(u"stacked_cel_fah_press_c_3")
        self.celsius_ap_49 = QWidget()
        self.celsius_ap_49.setObjectName(u"celsius_ap_49")
        self.horizontalLayout_566 = QHBoxLayout(self.celsius_ap_49)
        self.horizontalLayout_566.setObjectName(u"horizontalLayout_566")
        self.horizontalLayout_566.setContentsMargins(0, 0, 0, 0)
        self.label_401 = QLabel(self.celsius_ap_49)
        self.label_401.setObjectName(u"label_401")
        self.label_401.setFont(font13)
        self.label_401.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_401.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_566.addWidget(self.label_401)

        self.stacked_cel_fah_press_c_3.addWidget(self.celsius_ap_49)
        self.fahrenheit_ap_49 = QWidget()
        self.fahrenheit_ap_49.setObjectName(u"fahrenheit_ap_49")
        self.horizontalLayout_567 = QHBoxLayout(self.fahrenheit_ap_49)
        self.horizontalLayout_567.setObjectName(u"horizontalLayout_567")
        self.horizontalLayout_567.setContentsMargins(0, 0, 0, 0)
        self.label_402 = QLabel(self.fahrenheit_ap_49)
        self.label_402.setObjectName(u"label_402")
        self.label_402.setFont(font13)
        self.label_402.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_402.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_567.addWidget(self.label_402)

        self.stacked_cel_fah_press_c_3.addWidget(self.fahrenheit_ap_49)

        self.horizontalLayout_564.addWidget(self.stacked_cel_fah_press_c_3)

        self.horizontalLayout_564.setStretch(0, 6)
        self.horizontalLayout_564.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_3_val_12, 15, 6, 1, 1)

        self.group_3_val_10 = QWidget(self.widget_6)
        self.group_3_val_10.setObjectName(u"group_3_val_10")
        self.horizontalLayout_556 = QHBoxLayout(self.group_3_val_10)
        self.horizontalLayout_556.setSpacing(7)
        self.horizontalLayout_556.setObjectName(u"horizontalLayout_556")
        self.horizontalLayout_556.setContentsMargins(3, 3, 6, 3)
        self.widget_295 = QWidget(self.group_3_val_10)
        self.widget_295.setObjectName(u"widget_295")
        self.widget_295.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_557 = QHBoxLayout(self.widget_295)
        self.horizontalLayout_557.setObjectName(u"horizontalLayout_557")
        self.horizontalLayout_557.setContentsMargins(2, 2, 2, 2)
        self.pressure_sv_c_1 = QDoubleSpinBox(self.widget_295)
        self.pressure_sv_c_1.setObjectName(u"pressure_sv_c_1")
        sizePolicy.setHeightForWidth(self.pressure_sv_c_1.sizePolicy().hasHeightForWidth())
        self.pressure_sv_c_1.setSizePolicy(sizePolicy)
        self.pressure_sv_c_1.setFont(font11)
        self.pressure_sv_c_1.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_c_1.setWrapping(False)
        self.pressure_sv_c_1.setAlignment(Qt.AlignCenter)
        self.pressure_sv_c_1.setReadOnly(False)
        self.pressure_sv_c_1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_c_1.setDecimals(1)
        self.pressure_sv_c_1.setMaximum(999.000000000000000)
        self.pressure_sv_c_1.setValue(0.000000000000000)

        self.horizontalLayout_557.addWidget(self.pressure_sv_c_1)


        self.horizontalLayout_556.addWidget(self.widget_295)

        self.stacked_cel_fah_press_c_1 = QStackedWidget(self.group_3_val_10)
        self.stacked_cel_fah_press_c_1.setObjectName(u"stacked_cel_fah_press_c_1")
        self.celsius_ap_47 = QWidget()
        self.celsius_ap_47.setObjectName(u"celsius_ap_47")
        self.horizontalLayout_558 = QHBoxLayout(self.celsius_ap_47)
        self.horizontalLayout_558.setObjectName(u"horizontalLayout_558")
        self.horizontalLayout_558.setContentsMargins(0, 0, 0, 0)
        self.label_398 = QLabel(self.celsius_ap_47)
        self.label_398.setObjectName(u"label_398")
        self.label_398.setFont(font13)
        self.label_398.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_398.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_558.addWidget(self.label_398)

        self.stacked_cel_fah_press_c_1.addWidget(self.celsius_ap_47)
        self.fahrenheit_ap_47 = QWidget()
        self.fahrenheit_ap_47.setObjectName(u"fahrenheit_ap_47")
        self.horizontalLayout_559 = QHBoxLayout(self.fahrenheit_ap_47)
        self.horizontalLayout_559.setObjectName(u"horizontalLayout_559")
        self.horizontalLayout_559.setContentsMargins(0, 0, 0, 0)
        self.label_399 = QLabel(self.fahrenheit_ap_47)
        self.label_399.setObjectName(u"label_399")
        self.label_399.setFont(font13)
        self.label_399.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_399.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_559.addWidget(self.label_399)

        self.stacked_cel_fah_press_c_1.addWidget(self.fahrenheit_ap_47)

        self.horizontalLayout_556.addWidget(self.stacked_cel_fah_press_c_1)

        self.horizontalLayout_556.setStretch(0, 6)
        self.horizontalLayout_556.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_3_val_10, 13, 6, 1, 1)

        self.group_1_val_11 = QWidget(self.widget_6)
        self.group_1_val_11.setObjectName(u"group_1_val_11")
        self.horizontalLayout_342 = QHBoxLayout(self.group_1_val_11)
        self.horizontalLayout_342.setSpacing(7)
        self.horizontalLayout_342.setObjectName(u"horizontalLayout_342")
        self.horizontalLayout_342.setContentsMargins(3, 3, 6, 3)
        self.widget_265 = QWidget(self.group_1_val_11)
        self.widget_265.setObjectName(u"widget_265")
        self.widget_265.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_343 = QHBoxLayout(self.widget_265)
        self.horizontalLayout_343.setObjectName(u"horizontalLayout_343")
        self.horizontalLayout_343.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_2 = QDoubleSpinBox(self.widget_265)
        self.pressure_pv_a_2.setObjectName(u"pressure_pv_a_2")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_2.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_2.setSizePolicy(sizePolicy)
        self.pressure_pv_a_2.setFont(font11)
        self.pressure_pv_a_2.setStyleSheet(u"")
        self.pressure_pv_a_2.setWrapping(True)
        self.pressure_pv_a_2.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_2.setReadOnly(True)
        self.pressure_pv_a_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_2.setDecimals(1)
        self.pressure_pv_a_2.setMaximum(999.000000000000000)
        self.pressure_pv_a_2.setValue(0.000000000000000)

        self.horizontalLayout_343.addWidget(self.pressure_pv_a_2)

        self.horizontalLayout_343.setStretch(0, 1)

        self.horizontalLayout_342.addWidget(self.widget_265)

        self.stacked_cel_fah_press_a_2 = QStackedWidget(self.group_1_val_11)
        self.stacked_cel_fah_press_a_2.setObjectName(u"stacked_cel_fah_press_a_2")
        self.celsius_ap_40 = QWidget()
        self.celsius_ap_40.setObjectName(u"celsius_ap_40")
        self.horizontalLayout_514 = QHBoxLayout(self.celsius_ap_40)
        self.horizontalLayout_514.setObjectName(u"horizontalLayout_514")
        self.horizontalLayout_514.setContentsMargins(0, 0, 0, 0)
        self.label_379 = QLabel(self.celsius_ap_40)
        self.label_379.setObjectName(u"label_379")
        self.label_379.setFont(font13)
        self.label_379.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_379.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_514.addWidget(self.label_379)

        self.stacked_cel_fah_press_a_2.addWidget(self.celsius_ap_40)
        self.fahrenheit_ap_40 = QWidget()
        self.fahrenheit_ap_40.setObjectName(u"fahrenheit_ap_40")
        self.horizontalLayout_515 = QHBoxLayout(self.fahrenheit_ap_40)
        self.horizontalLayout_515.setObjectName(u"horizontalLayout_515")
        self.horizontalLayout_515.setContentsMargins(0, 0, 0, 0)
        self.label_380 = QLabel(self.fahrenheit_ap_40)
        self.label_380.setObjectName(u"label_380")
        self.label_380.setFont(font13)
        self.label_380.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_380.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_515.addWidget(self.label_380)

        self.stacked_cel_fah_press_a_2.addWidget(self.fahrenheit_ap_40)

        self.horizontalLayout_342.addWidget(self.stacked_cel_fah_press_a_2)

        self.horizontalLayout_342.setStretch(0, 6)
        self.horizontalLayout_342.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_1_val_11, 14, 2, 1, 1)

        self.widget_47 = QWidget(self.widget_6)
        self.widget_47.setObjectName(u"widget_47")
        self.horizontalLayout_54 = QHBoxLayout(self.widget_47)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(3, 3, 3, 3)
        self.vacuum_btn_a = QPushButton(self.widget_47)
        self.vacuum_btn_a.setObjectName(u"vacuum_btn_a")
        sizePolicy.setHeightForWidth(self.vacuum_btn_a.sizePolicy().hasHeightForWidth())
        self.vacuum_btn_a.setSizePolicy(sizePolicy)
        self.vacuum_btn_a.setMinimumSize(QSize(0, 40))
        self.vacuum_btn_a.setMaximumSize(QSize(16777215, 75))
        self.vacuum_btn_a.setFont(font2)
        self.vacuum_btn_a.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B7EC8;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 8px 12px;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0968A3;\n"
"}\n"
"QPushButton:pressed {\n"
"	color: white;\n"
"    background-color: #085A91;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #EF4444;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/Icons/pump.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.vacuum_btn_a.setIcon(icon15)
        self.vacuum_btn_a.setIconSize(QSize(35, 35))
        self.vacuum_btn_a.setCheckable(True)

        self.horizontalLayout_54.addWidget(self.vacuum_btn_a)


        self.gridLayout.addWidget(self.widget_47, 18, 2, 1, 1)

        self.header_group_layout_3 = QHBoxLayout()
        self.header_group_layout_3.setObjectName(u"header_group_layout_3")
        self.widget_22 = QWidget(self.widget_6)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setStyleSheet(u"QWidget{\n"
"	color: #6F00FF;\n"
"	border-left: none;\n"
"}")
        self.verticalLayout_22 = QVBoxLayout(self.widget_22)
        self.verticalLayout_22.setSpacing(5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_171 = QLabel(self.widget_22)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setFont(font9)
        self.label_171.setStyleSheet(u"")
        self.label_171.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_171)

        self.widget_23 = QWidget(self.widget_22)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_22.setSpacing(7)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.widget_24 = QWidget(self.widget_23)
        self.widget_24.setObjectName(u"widget_24")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_23.setSpacing(7)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 2, 2, 2)
        self.label_172 = QLabel(self.widget_24)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setFont(font10)
        self.label_172.setStyleSheet(u"color: rgb(229, 57, 53);")
        self.label_172.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_172)

        self.line_16 = QFrame(self.widget_24)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setStyleSheet(u"border: 1px solid rgb(22, 93, 200);")
        self.line_16.setFrameShape(QFrame.Shape.VLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_23.addWidget(self.line_16)

        self.label_175 = QLabel(self.widget_24)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setFont(font10)
        self.label_175.setStyleSheet(u"color: rgb(67, 160, 71);")
        self.label_175.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_175)

        self.horizontalLayout_23.setStretch(0, 1)
        self.horizontalLayout_23.setStretch(2, 1)

        self.horizontalLayout_22.addWidget(self.widget_24)

        self.horizontalLayout_22.setStretch(0, 6)

        self.verticalLayout_22.addWidget(self.widget_23)


        self.header_group_layout_3.addWidget(self.widget_22)

        self.clear_group_c = QPushButton(self.widget_6)
        self.clear_group_c.setObjectName(u"clear_group_c")
        sizePolicy.setHeightForWidth(self.clear_group_c.sizePolicy().hasHeightForWidth())
        self.clear_group_c.setSizePolicy(sizePolicy)
        self.clear_group_c.setIcon(icon11)
        self.clear_group_c.setIconSize(QSize(42, 42))

        self.header_group_layout_3.addWidget(self.clear_group_c)

        self.header_group_layout_3.setStretch(0, 6)
        self.header_group_layout_3.setStretch(1, 1)

        self.gridLayout.addLayout(self.header_group_layout_3, 0, 6, 2, 1)

        self.code_display = QLineEdit(self.widget_6)
        self.code_display.setObjectName(u"code_display")
        sizePolicy.setHeightForWidth(self.code_display.sizePolicy().hasHeightForWidth())
        self.code_display.setSizePolicy(sizePolicy)
        font14 = QFont()
        font14.setFamilies([u"Segoe UI"])
        font14.setPointSize(19)
        font14.setBold(True)
        self.code_display.setFont(font14)
        self.code_display.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.code_display, 0, 0, 2, 1)

        self.header_group_layout_1 = QHBoxLayout()
        self.header_group_layout_1.setObjectName(u"header_group_layout_1")
        self.widget = QWidget(self.widget_6)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget{\n"
"	color: rgb(30, 136, 229);\n"
"	border-left: none;\n"
"}")
        self.verticalLayout_18 = QVBoxLayout(self.widget)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_156 = QLabel(self.widget)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setFont(font9)
        self.label_156.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_156)

        self.widget_14 = QWidget(self.widget)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_17.setSpacing(7)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_17 = QWidget(self.widget_14)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setStyleSheet(u"")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_18.setSpacing(7)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 2, 2, 2)
        self.label_165 = QLabel(self.widget_17)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setFont(font10)
        self.label_165.setStyleSheet(u"color: rgb(229, 57, 53);")
        self.label_165.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_165)

        self.line_14 = QFrame(self.widget_17)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_14.setFrameShape(QFrame.Shape.VLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_18.addWidget(self.line_14)

        self.label_167 = QLabel(self.widget_17)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setFont(font10)
        self.label_167.setStyleSheet(u"color: rgb(67, 160, 71);")
        self.label_167.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_167)

        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(2, 1)

        self.horizontalLayout_17.addWidget(self.widget_17)

        self.horizontalLayout_17.setStretch(0, 6)

        self.verticalLayout_18.addWidget(self.widget_14)


        self.header_group_layout_1.addWidget(self.widget)

        self.clear_group_a = QPushButton(self.widget_6)
        self.clear_group_a.setObjectName(u"clear_group_a")
        sizePolicy.setHeightForWidth(self.clear_group_a.sizePolicy().hasHeightForWidth())
        self.clear_group_a.setSizePolicy(sizePolicy)
        self.clear_group_a.setIcon(icon11)
        self.clear_group_a.setIconSize(QSize(42, 42))

        self.header_group_layout_1.addWidget(self.clear_group_a)

        self.header_group_layout_1.setStretch(0, 6)
        self.header_group_layout_1.setStretch(1, 1)

        self.gridLayout.addLayout(self.header_group_layout_1, 0, 2, 2, 1)

        self.widget_44 = QWidget(self.widget_6)
        self.widget_44.setObjectName(u"widget_44")
        self.horizontalLayout_51 = QHBoxLayout(self.widget_44)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(3, 5, 3, 3)
        self.refuel_btn_a = QPushButton(self.widget_44)
        self.refuel_btn_a.setObjectName(u"refuel_btn_a")
        sizePolicy.setHeightForWidth(self.refuel_btn_a.sizePolicy().hasHeightForWidth())
        self.refuel_btn_a.setSizePolicy(sizePolicy)
        self.refuel_btn_a.setMinimumSize(QSize(0, 40))
        self.refuel_btn_a.setMaximumSize(QSize(16777215, 75))
        self.refuel_btn_a.setFont(font2)
        self.refuel_btn_a.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B7EC8;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 8px 12px;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0968A3;\n"
"}\n"
"QPushButton:pressed {\n"
"	color: white;\n"
"    background-color: #085A91;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #EF4444;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}")
        self.refuel_btn_a.setIcon(icon12)
        self.refuel_btn_a.setIconSize(QSize(35, 35))
        self.refuel_btn_a.setCheckable(True)

        self.horizontalLayout_51.addWidget(self.refuel_btn_a)


        self.gridLayout.addWidget(self.widget_44, 17, 2, 1, 1)

        self.widget_46 = QWidget(self.widget_6)
        self.widget_46.setObjectName(u"widget_46")
        self.horizontalLayout_53 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(3, 3, 3, 3)
        self.vacuum_btn_c = QPushButton(self.widget_46)
        self.vacuum_btn_c.setObjectName(u"vacuum_btn_c")
        sizePolicy.setHeightForWidth(self.vacuum_btn_c.sizePolicy().hasHeightForWidth())
        self.vacuum_btn_c.setSizePolicy(sizePolicy)
        self.vacuum_btn_c.setMinimumSize(QSize(0, 40))
        self.vacuum_btn_c.setMaximumSize(QSize(16777215, 75))
        self.vacuum_btn_c.setFont(font2)
        self.vacuum_btn_c.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B7EC8;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 8px 12px;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0968A3;\n"
"}\n"
"QPushButton:pressed {\n"
"	color: white;\n"
"    background-color: #085A91;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #EF4444;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}")
        self.vacuum_btn_c.setIcon(icon15)
        self.vacuum_btn_c.setIconSize(QSize(35, 35))
        self.vacuum_btn_c.setCheckable(True)

        self.horizontalLayout_53.addWidget(self.vacuum_btn_c)


        self.gridLayout.addWidget(self.widget_46, 18, 6, 1, 1)

        self.widget_45 = QWidget(self.widget_6)
        self.widget_45.setObjectName(u"widget_45")
        self.horizontalLayout_52 = QHBoxLayout(self.widget_45)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(3, 3, 3, 3)
        self.vacuum_btn_b = QPushButton(self.widget_45)
        self.vacuum_btn_b.setObjectName(u"vacuum_btn_b")
        sizePolicy.setHeightForWidth(self.vacuum_btn_b.sizePolicy().hasHeightForWidth())
        self.vacuum_btn_b.setSizePolicy(sizePolicy)
        self.vacuum_btn_b.setMinimumSize(QSize(0, 40))
        self.vacuum_btn_b.setMaximumSize(QSize(16777215, 75))
        self.vacuum_btn_b.setFont(font2)
        self.vacuum_btn_b.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B7EC8;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 8px 12px;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0968A3;\n"
"}\n"
"QPushButton:pressed {\n"
"	color: white;\n"
"    background-color: #085A91;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #EF4444;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}")
        self.vacuum_btn_b.setIcon(icon15)
        self.vacuum_btn_b.setIconSize(QSize(35, 35))
        self.vacuum_btn_b.setCheckable(True)

        self.horizontalLayout_52.addWidget(self.vacuum_btn_b)


        self.gridLayout.addWidget(self.widget_45, 18, 4, 1, 1)

        self.group_1_val_10 = QWidget(self.widget_6)
        self.group_1_val_10.setObjectName(u"group_1_val_10")
        self.horizontalLayout_288 = QHBoxLayout(self.group_1_val_10)
        self.horizontalLayout_288.setSpacing(7)
        self.horizontalLayout_288.setObjectName(u"horizontalLayout_288")
        self.horizontalLayout_288.setContentsMargins(3, 3, 6, 3)
        self.widget_264 = QWidget(self.group_1_val_10)
        self.widget_264.setObjectName(u"widget_264")
        self.widget_264.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_341 = QHBoxLayout(self.widget_264)
        self.horizontalLayout_341.setObjectName(u"horizontalLayout_341")
        self.horizontalLayout_341.setContentsMargins(2, 2, 2, 2)
        self.pressure_sv_a_1 = QDoubleSpinBox(self.widget_264)
        self.pressure_sv_a_1.setObjectName(u"pressure_sv_a_1")
        sizePolicy.setHeightForWidth(self.pressure_sv_a_1.sizePolicy().hasHeightForWidth())
        self.pressure_sv_a_1.setSizePolicy(sizePolicy)
        self.pressure_sv_a_1.setFont(font11)
        self.pressure_sv_a_1.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 2px solid #43A047;\n"
"}")
        self.pressure_sv_a_1.setWrapping(False)
        self.pressure_sv_a_1.setAlignment(Qt.AlignCenter)
        self.pressure_sv_a_1.setReadOnly(False)
        self.pressure_sv_a_1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_a_1.setDecimals(1)
        self.pressure_sv_a_1.setMaximum(999.000000000000000)
        self.pressure_sv_a_1.setValue(0.000000000000000)

        self.horizontalLayout_341.addWidget(self.pressure_sv_a_1)

        self.horizontalLayout_341.setStretch(0, 1)

        self.horizontalLayout_288.addWidget(self.widget_264)

        self.stacked_cel_fah_press_a_1 = QStackedWidget(self.group_1_val_10)
        self.stacked_cel_fah_press_a_1.setObjectName(u"stacked_cel_fah_press_a_1")
        self.celsius_ap_39 = QWidget()
        self.celsius_ap_39.setObjectName(u"celsius_ap_39")
        self.horizontalLayout_512 = QHBoxLayout(self.celsius_ap_39)
        self.horizontalLayout_512.setObjectName(u"horizontalLayout_512")
        self.horizontalLayout_512.setContentsMargins(0, 0, 0, 0)
        self.label_280 = QLabel(self.celsius_ap_39)
        self.label_280.setObjectName(u"label_280")
        self.label_280.setFont(font13)
        self.label_280.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_280.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_512.addWidget(self.label_280)

        self.stacked_cel_fah_press_a_1.addWidget(self.celsius_ap_39)
        self.fahrenheit_ap_39 = QWidget()
        self.fahrenheit_ap_39.setObjectName(u"fahrenheit_ap_39")
        self.horizontalLayout_513 = QHBoxLayout(self.fahrenheit_ap_39)
        self.horizontalLayout_513.setObjectName(u"horizontalLayout_513")
        self.horizontalLayout_513.setContentsMargins(0, 0, 0, 0)
        self.label_340 = QLabel(self.fahrenheit_ap_39)
        self.label_340.setObjectName(u"label_340")
        self.label_340.setFont(font13)
        self.label_340.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_340.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_513.addWidget(self.label_340)

        self.stacked_cel_fah_press_a_1.addWidget(self.fahrenheit_ap_39)

        self.horizontalLayout_288.addWidget(self.stacked_cel_fah_press_a_1)

        self.horizontalLayout_288.setStretch(0, 6)
        self.horizontalLayout_288.setStretch(1, 1)

        self.gridLayout.addWidget(self.group_1_val_10, 13, 2, 1, 1)

        self.widget_51 = QWidget(self.widget_6)
        self.widget_51.setObjectName(u"widget_51")
        self.horizontalLayout_58 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(3, 5, 3, 3)
        self.refuel_btn_b = QPushButton(self.widget_51)
        self.refuel_btn_b.setObjectName(u"refuel_btn_b")
        sizePolicy.setHeightForWidth(self.refuel_btn_b.sizePolicy().hasHeightForWidth())
        self.refuel_btn_b.setSizePolicy(sizePolicy)
        self.refuel_btn_b.setMinimumSize(QSize(0, 40))
        self.refuel_btn_b.setMaximumSize(QSize(16777215, 75))
        self.refuel_btn_b.setFont(font2)
        self.refuel_btn_b.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B7EC8;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 8px 12px;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0968A3;\n"
"}\n"
"QPushButton:pressed {\n"
"	color: white;\n"
"    background-color: #085A91;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #EF4444;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}")
        self.refuel_btn_b.setIcon(icon12)
        self.refuel_btn_b.setIconSize(QSize(35, 35))
        self.refuel_btn_b.setCheckable(True)

        self.horizontalLayout_58.addWidget(self.refuel_btn_b)


        self.gridLayout.addWidget(self.widget_51, 17, 4, 1, 1)

        self.widget_50 = QWidget(self.widget_6)
        self.widget_50.setObjectName(u"widget_50")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(3, 3, 3, 0)
        self.heat_btn_a = QPushButton(self.widget_50)
        self.heat_btn_a.setObjectName(u"heat_btn_a")
        sizePolicy.setHeightForWidth(self.heat_btn_a.sizePolicy().hasHeightForWidth())
        self.heat_btn_a.setSizePolicy(sizePolicy)
        self.heat_btn_a.setMinimumSize(QSize(0, 40))
        self.heat_btn_a.setMaximumSize(QSize(16777215, 75))
        self.heat_btn_a.setFont(font2)
        self.heat_btn_a.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B7EC8;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 8px 12px;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0968A3;\n"
"}\n"
"QPushButton:pressed {\n"
"	color: white;\n"
"    background-color: #085A91;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #EF4444;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/Icons/heat.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.heat_btn_a.setIcon(icon16)
        self.heat_btn_a.setIconSize(QSize(35, 35))
        self.heat_btn_a.setCheckable(True)

        self.horizontalLayout_21.addWidget(self.heat_btn_a)


        self.gridLayout.addWidget(self.widget_50, 19, 2, 1, 1)

        self.widget_48 = QWidget(self.widget_6)
        self.widget_48.setObjectName(u"widget_48")
        self.horizontalLayout_56 = QHBoxLayout(self.widget_48)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(3, 3, 3, 0)
        self.heat_btn_b = QPushButton(self.widget_48)
        self.heat_btn_b.setObjectName(u"heat_btn_b")
        sizePolicy.setHeightForWidth(self.heat_btn_b.sizePolicy().hasHeightForWidth())
        self.heat_btn_b.setSizePolicy(sizePolicy)
        self.heat_btn_b.setMinimumSize(QSize(0, 40))
        self.heat_btn_b.setMaximumSize(QSize(16777215, 75))
        self.heat_btn_b.setFont(font2)
        self.heat_btn_b.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B7EC8;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 8px 12px;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0968A3;\n"
"}\n"
"QPushButton:pressed {\n"
"	color: white;\n"
"    background-color: #085A91;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #EF4444;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}")
        self.heat_btn_b.setIcon(icon16)
        self.heat_btn_b.setIconSize(QSize(35, 35))
        self.heat_btn_b.setCheckable(True)

        self.horizontalLayout_56.addWidget(self.heat_btn_b)


        self.gridLayout.addWidget(self.widget_48, 19, 4, 1, 1)

        self.widget_49 = QWidget(self.widget_6)
        self.widget_49.setObjectName(u"widget_49")
        self.horizontalLayout_57 = QHBoxLayout(self.widget_49)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(3, 3, 3, 0)
        self.heat_btn_c = QPushButton(self.widget_49)
        self.heat_btn_c.setObjectName(u"heat_btn_c")
        sizePolicy.setHeightForWidth(self.heat_btn_c.sizePolicy().hasHeightForWidth())
        self.heat_btn_c.setSizePolicy(sizePolicy)
        self.heat_btn_c.setMinimumSize(QSize(0, 40))
        self.heat_btn_c.setMaximumSize(QSize(16777215, 75))
        self.heat_btn_c.setFont(font2)
        self.heat_btn_c.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B7EC8;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 8px 12px;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0968A3;\n"
"}\n"
"QPushButton:pressed {\n"
"	color: white;\n"
"    background-color: #085A91;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #EF4444;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}")
        self.heat_btn_c.setIcon(icon16)
        self.heat_btn_c.setIconSize(QSize(35, 35))
        self.heat_btn_c.setCheckable(True)

        self.horizontalLayout_57.addWidget(self.heat_btn_c)


        self.gridLayout.addWidget(self.widget_49, 19, 6, 1, 1)

        self.start_stop_stacked = QStackedWidget(self.widget_6)
        self.start_stop_stacked.setObjectName(u"start_stop_stacked")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_36 = QVBoxLayout(self.page)
        self.verticalLayout_36.setSpacing(5)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 5, 4, 0)
        self.start_btn = QPushButton(self.page)
        self.start_btn.setObjectName(u"start_btn")
        sizePolicy.setHeightForWidth(self.start_btn.sizePolicy().hasHeightForWidth())
        self.start_btn.setSizePolicy(sizePolicy)
        self.start_btn.setMaximumSize(QSize(16777215, 16777215))
        font15 = QFont()
        font15.setFamilies([u"Segoe UI"])
        font15.setPointSize(26)
        font15.setBold(True)
        self.start_btn.setFont(font15)
        self.start_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B7EC8;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0968A3;\n"
"}\n"
"QPushButton:pressed {\n"
"	color: white;\n"
"    background-color: #085A91;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/Icons/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_btn.setIcon(icon17)
        self.start_btn.setIconSize(QSize(45, 45))
        self.start_btn.setCheckable(True)

        self.verticalLayout_36.addWidget(self.start_btn)

        self.start_stop_stacked.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_37 = QVBoxLayout(self.page_2)
        self.verticalLayout_37.setSpacing(5)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 5, 4, 0)
        self.stop_btn = QPushButton(self.page_2)
        self.stop_btn.setObjectName(u"stop_btn")
        sizePolicy.setHeightForWidth(self.stop_btn.sizePolicy().hasHeightForWidth())
        self.stop_btn.setSizePolicy(sizePolicy)
        self.stop_btn.setMaximumSize(QSize(16777215, 16777215))
        self.stop_btn.setFont(font15)
        self.stop_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #EF4444;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 12px 24px;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(175, 49, 49);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: white;\n"
"    background-color: #085A91;\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u":/Icons/stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stop_btn.setIcon(icon18)
        self.stop_btn.setIconSize(QSize(35, 35))
        self.stop_btn.setCheckable(True)

        self.verticalLayout_37.addWidget(self.stop_btn)

        self.start_stop_stacked.addWidget(self.page_2)

        self.gridLayout.addWidget(self.start_stop_stacked, 17, 0, 3, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 1)
        self.gridLayout.setRowStretch(6, 1)
        self.gridLayout.setRowStretch(7, 1)
        self.gridLayout.setRowStretch(8, 1)
        self.gridLayout.setRowStretch(9, 1)
        self.gridLayout.setRowStretch(10, 1)
        self.gridLayout.setRowStretch(11, 1)
        self.gridLayout.setRowStretch(12, 1)
        self.gridLayout.setRowStretch(13, 1)
        self.gridLayout.setRowStretch(14, 1)
        self.gridLayout.setRowStretch(15, 1)
        self.gridLayout.setRowStretch(16, 1)

        self.verticalLayout_63.addWidget(self.widget_6)


        self.verticalLayout_10.addWidget(self.widget_pressure)

        self.verticalLayout_10.setStretch(0, 6)

        self.verticalLayout_6.addWidget(self.stacked_pressure_page)

        self.stackedWidget.addWidget(self.pressure_page)
        self.temperature_page = QWidget()
        self.temperature_page.setObjectName(u"temperature_page")
        self.verticalLayout_8 = QVBoxLayout(self.temperature_page)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 3)
        self.widget_temperature = QWidget(self.temperature_page)
        self.widget_temperature.setObjectName(u"widget_temperature")
        self.widget_temperature.setStyleSheet(u"background-color: white;\n"
"border-radius: 15px;")
        self.verticalLayout_56 = QVBoxLayout(self.widget_temperature)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 5, 0, 0)
        self.widget_77 = QWidget(self.widget_temperature)
        self.widget_77.setObjectName(u"widget_77")
        sizePolicy1.setHeightForWidth(self.widget_77.sizePolicy().hasHeightForWidth())
        self.widget_77.setSizePolicy(sizePolicy1)
        self.widget_77.setStyleSheet(u"QWidget#widget_77 {\n"
"    background-color: white;\n"
"    border-left: 4px solid rgb(22, 93, 200);\n"
"    border-radius: 6px;\n"
"}\n"
"QLabel{\n"
"	border: none;\n"
"	color: rgb(97, 97, 97)\n"
"}\n"
"Line{\n"
"	border: 2px solid #FB8C00;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.widget_77)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setContentsMargins(10, 5, 5, 5)
        self.line_17 = QFrame(self.widget_77)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_17.setFrameShape(QFrame.Shape.VLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_17, 1, 4, 9, 1)

        self.line_22 = QFrame(self.widget_77)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_22.setFrameShape(QFrame.Shape.HLine)
        self.line_22.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_22, 3, 1, 1, 1)

        self.line_13 = QFrame(self.widget_77)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_13.setFrameShape(QFrame.Shape.VLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_13, 1, 6, 9, 1)

        self.line_24 = QFrame(self.widget_77)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_24.setFrameShape(QFrame.Shape.HLine)
        self.line_24.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_24, 6, 1, 1, 1)

        self.widget_248 = QWidget(self.widget_77)
        self.widget_248.setObjectName(u"widget_248")
        self.horizontalLayout_320 = QHBoxLayout(self.widget_248)
        self.horizontalLayout_320.setSpacing(3)
        self.horizontalLayout_320.setObjectName(u"horizontalLayout_320")
        self.horizontalLayout_320.setContentsMargins(10, 0, 10, 0)
        self.widget_249 = QWidget(self.widget_248)
        self.widget_249.setObjectName(u"widget_249")
        self.widget_249.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_321 = QHBoxLayout(self.widget_249)
        self.horizontalLayout_321.setObjectName(u"horizontalLayout_321")
        self.horizontalLayout_321.setContentsMargins(2, 2, 2, 2)
        self.bt_l_alm_value = QDoubleSpinBox(self.widget_249)
        self.bt_l_alm_value.setObjectName(u"bt_l_alm_value")
        sizePolicy.setHeightForWidth(self.bt_l_alm_value.sizePolicy().hasHeightForWidth())
        self.bt_l_alm_value.setSizePolicy(sizePolicy)
        font16 = QFont()
        font16.setFamilies([u"Segoe UI"])
        font16.setPointSize(25)
        font16.setBold(True)
        font16.setItalic(False)
        self.bt_l_alm_value.setFont(font16)
        self.bt_l_alm_value.setStyleSheet(u"")
        self.bt_l_alm_value.setWrapping(False)
        self.bt_l_alm_value.setAlignment(Qt.AlignCenter)
        self.bt_l_alm_value.setReadOnly(False)
        self.bt_l_alm_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.bt_l_alm_value.setDecimals(1)
        self.bt_l_alm_value.setMaximum(999.000000000000000)
        self.bt_l_alm_value.setValue(0.000000000000000)

        self.horizontalLayout_321.addWidget(self.bt_l_alm_value)


        self.horizontalLayout_320.addWidget(self.widget_249)

        self.stacked_cel_fah_temp_b_4 = QStackedWidget(self.widget_248)
        self.stacked_cel_fah_temp_b_4.setObjectName(u"stacked_cel_fah_temp_b_4")
        self.celsius_bt_5 = QWidget()
        self.celsius_bt_5.setObjectName(u"celsius_bt_5")
        self.horizontalLayout_428 = QHBoxLayout(self.celsius_bt_5)
        self.horizontalLayout_428.setObjectName(u"horizontalLayout_428")
        self.horizontalLayout_428.setContentsMargins(0, 0, 0, 0)
        self.label_342 = QLabel(self.celsius_bt_5)
        self.label_342.setObjectName(u"label_342")
        font17 = QFont()
        font17.setFamilies([u"Segoe UI"])
        font17.setPointSize(20)
        font17.setBold(True)
        font17.setItalic(False)
        self.label_342.setFont(font17)
        self.label_342.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_342.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_428.addWidget(self.label_342)

        self.stacked_cel_fah_temp_b_4.addWidget(self.celsius_bt_5)
        self.fahrenheit_at_25 = QWidget()
        self.fahrenheit_at_25.setObjectName(u"fahrenheit_at_25")
        self.horizontalLayout_429 = QHBoxLayout(self.fahrenheit_at_25)
        self.horizontalLayout_429.setObjectName(u"horizontalLayout_429")
        self.horizontalLayout_429.setContentsMargins(0, 0, 0, 0)
        self.label_343 = QLabel(self.fahrenheit_at_25)
        self.label_343.setObjectName(u"label_343")
        self.label_343.setFont(font17)
        self.label_343.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_343.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_429.addWidget(self.label_343)

        self.stacked_cel_fah_temp_b_4.addWidget(self.fahrenheit_at_25)

        self.horizontalLayout_320.addWidget(self.stacked_cel_fah_temp_b_4)

        self.horizontalLayout_320.setStretch(0, 3)
        self.horizontalLayout_320.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_248, 5, 7, 1, 1)

        self.widget_261 = QWidget(self.widget_77)
        self.widget_261.setObjectName(u"widget_261")
        self.horizontalLayout_317 = QHBoxLayout(self.widget_261)
        self.horizontalLayout_317.setSpacing(3)
        self.horizontalLayout_317.setObjectName(u"horizontalLayout_317")
        self.horizontalLayout_317.setContentsMargins(10, 0, 10, 0)
        self.widget_262 = QWidget(self.widget_261)
        self.widget_262.setObjectName(u"widget_262")
        self.widget_262.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_318 = QHBoxLayout(self.widget_262)
        self.horizontalLayout_318.setObjectName(u"horizontalLayout_318")
        self.horizontalLayout_318.setContentsMargins(2, 2, 2, 2)
        self.bt_t3_offset_value = QDoubleSpinBox(self.widget_262)
        self.bt_t3_offset_value.setObjectName(u"bt_t3_offset_value")
        sizePolicy.setHeightForWidth(self.bt_t3_offset_value.sizePolicy().hasHeightForWidth())
        self.bt_t3_offset_value.setSizePolicy(sizePolicy)
        self.bt_t3_offset_value.setFont(font16)
        self.bt_t3_offset_value.setStyleSheet(u"")
        self.bt_t3_offset_value.setWrapping(False)
        self.bt_t3_offset_value.setAlignment(Qt.AlignCenter)
        self.bt_t3_offset_value.setReadOnly(False)
        self.bt_t3_offset_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.bt_t3_offset_value.setDecimals(1)
        self.bt_t3_offset_value.setMaximum(999.000000000000000)
        self.bt_t3_offset_value.setValue(0.000000000000000)

        self.horizontalLayout_318.addWidget(self.bt_t3_offset_value)


        self.horizontalLayout_317.addWidget(self.widget_262)

        self.stacked_cel_fah_temp_b_7 = QStackedWidget(self.widget_261)
        self.stacked_cel_fah_temp_b_7.setObjectName(u"stacked_cel_fah_temp_b_7")
        self.celsius_bt_8 = QWidget()
        self.celsius_bt_8.setObjectName(u"celsius_bt_8")
        self.horizontalLayout_437 = QHBoxLayout(self.celsius_bt_8)
        self.horizontalLayout_437.setObjectName(u"horizontalLayout_437")
        self.horizontalLayout_437.setContentsMargins(0, 0, 0, 0)
        self.label_348 = QLabel(self.celsius_bt_8)
        self.label_348.setObjectName(u"label_348")
        self.label_348.setFont(font17)
        self.label_348.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_348.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_437.addWidget(self.label_348)

        self.stacked_cel_fah_temp_b_7.addWidget(self.celsius_bt_8)
        self.fahrenheit_at_28 = QWidget()
        self.fahrenheit_at_28.setObjectName(u"fahrenheit_at_28")
        self.horizontalLayout_438 = QHBoxLayout(self.fahrenheit_at_28)
        self.horizontalLayout_438.setObjectName(u"horizontalLayout_438")
        self.horizontalLayout_438.setContentsMargins(0, 0, 0, 0)
        self.label_349 = QLabel(self.fahrenheit_at_28)
        self.label_349.setObjectName(u"label_349")
        self.label_349.setFont(font17)
        self.label_349.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_349.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_438.addWidget(self.label_349)

        self.stacked_cel_fah_temp_b_7.addWidget(self.fahrenheit_at_28)

        self.horizontalLayout_317.addWidget(self.stacked_cel_fah_temp_b_7)

        self.horizontalLayout_317.setStretch(0, 3)
        self.horizontalLayout_317.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_261, 9, 7, 1, 1)

        self.widget_257 = QWidget(self.widget_77)
        self.widget_257.setObjectName(u"widget_257")
        self.horizontalLayout_313 = QHBoxLayout(self.widget_257)
        self.horizontalLayout_313.setSpacing(3)
        self.horizontalLayout_313.setObjectName(u"horizontalLayout_313")
        self.horizontalLayout_313.setContentsMargins(10, 0, 10, 0)
        self.widget_258 = QWidget(self.widget_257)
        self.widget_258.setObjectName(u"widget_258")
        self.widget_258.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_314 = QHBoxLayout(self.widget_258)
        self.horizontalLayout_314.setObjectName(u"horizontalLayout_314")
        self.horizontalLayout_314.setContentsMargins(2, 2, 2, 2)
        self.bt_sv = QDoubleSpinBox(self.widget_258)
        self.bt_sv.setObjectName(u"bt_sv")
        sizePolicy.setHeightForWidth(self.bt_sv.sizePolicy().hasHeightForWidth())
        self.bt_sv.setSizePolicy(sizePolicy)
        self.bt_sv.setFont(font16)
        self.bt_sv.setStyleSheet(u"")
        self.bt_sv.setWrapping(False)
        self.bt_sv.setAlignment(Qt.AlignCenter)
        self.bt_sv.setReadOnly(False)
        self.bt_sv.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.bt_sv.setDecimals(1)
        self.bt_sv.setMaximum(999.000000000000000)
        self.bt_sv.setValue(0.000000000000000)

        self.horizontalLayout_314.addWidget(self.bt_sv)


        self.horizontalLayout_313.addWidget(self.widget_258)

        self.stacked_cel_fah_temp_b_2 = QStackedWidget(self.widget_257)
        self.stacked_cel_fah_temp_b_2.setObjectName(u"stacked_cel_fah_temp_b_2")
        self.celsius_bt_2 = QWidget()
        self.celsius_bt_2.setObjectName(u"celsius_bt_2")
        self.horizontalLayout_422 = QHBoxLayout(self.celsius_bt_2)
        self.horizontalLayout_422.setObjectName(u"horizontalLayout_422")
        self.horizontalLayout_422.setContentsMargins(0, 0, 0, 0)
        self.label_336 = QLabel(self.celsius_bt_2)
        self.label_336.setObjectName(u"label_336")
        self.label_336.setFont(font17)
        self.label_336.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_336.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_422.addWidget(self.label_336)

        self.stacked_cel_fah_temp_b_2.addWidget(self.celsius_bt_2)
        self.fahrenheit_at_22 = QWidget()
        self.fahrenheit_at_22.setObjectName(u"fahrenheit_at_22")
        self.horizontalLayout_423 = QHBoxLayout(self.fahrenheit_at_22)
        self.horizontalLayout_423.setObjectName(u"horizontalLayout_423")
        self.horizontalLayout_423.setContentsMargins(0, 0, 0, 0)
        self.label_337 = QLabel(self.fahrenheit_at_22)
        self.label_337.setObjectName(u"label_337")
        self.label_337.setFont(font17)
        self.label_337.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_337.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_423.addWidget(self.label_337)

        self.stacked_cel_fah_temp_b_2.addWidget(self.fahrenheit_at_22)

        self.horizontalLayout_313.addWidget(self.stacked_cel_fah_temp_b_2)

        self.horizontalLayout_313.setStretch(0, 3)
        self.horizontalLayout_313.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_257, 2, 7, 1, 1)

        self.widget_255 = QWidget(self.widget_77)
        self.widget_255.setObjectName(u"widget_255")
        self.horizontalLayout_170 = QHBoxLayout(self.widget_255)
        self.horizontalLayout_170.setSpacing(3)
        self.horizontalLayout_170.setObjectName(u"horizontalLayout_170")
        self.horizontalLayout_170.setContentsMargins(10, 0, 10, 0)
        self.widget_256 = QWidget(self.widget_255)
        self.widget_256.setObjectName(u"widget_256")
        self.widget_256.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_312 = QHBoxLayout(self.widget_256)
        self.horizontalLayout_312.setObjectName(u"horizontalLayout_312")
        self.horizontalLayout_312.setContentsMargins(2, 2, 2, 2)
        self.bt_pv = QDoubleSpinBox(self.widget_256)
        self.bt_pv.setObjectName(u"bt_pv")
        sizePolicy.setHeightForWidth(self.bt_pv.sizePolicy().hasHeightForWidth())
        self.bt_pv.setSizePolicy(sizePolicy)
        self.bt_pv.setFont(font16)
        self.bt_pv.setStyleSheet(u"")
        self.bt_pv.setWrapping(True)
        self.bt_pv.setAlignment(Qt.AlignCenter)
        self.bt_pv.setReadOnly(True)
        self.bt_pv.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.bt_pv.setDecimals(1)
        self.bt_pv.setMaximum(999.000000000000000)
        self.bt_pv.setValue(0.000000000000000)

        self.horizontalLayout_312.addWidget(self.bt_pv)


        self.horizontalLayout_170.addWidget(self.widget_256)

        self.stacked_cel_fah_temp_b_1 = QStackedWidget(self.widget_255)
        self.stacked_cel_fah_temp_b_1.setObjectName(u"stacked_cel_fah_temp_b_1")
        self.celsius_bt_1 = QWidget()
        self.celsius_bt_1.setObjectName(u"celsius_bt_1")
        self.horizontalLayout_420 = QHBoxLayout(self.celsius_bt_1)
        self.horizontalLayout_420.setObjectName(u"horizontalLayout_420")
        self.horizontalLayout_420.setContentsMargins(0, 0, 0, 0)
        self.label_334 = QLabel(self.celsius_bt_1)
        self.label_334.setObjectName(u"label_334")
        self.label_334.setFont(font17)
        self.label_334.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_334.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_420.addWidget(self.label_334)

        self.stacked_cel_fah_temp_b_1.addWidget(self.celsius_bt_1)
        self.fahrenheit_at_21 = QWidget()
        self.fahrenheit_at_21.setObjectName(u"fahrenheit_at_21")
        self.horizontalLayout_421 = QHBoxLayout(self.fahrenheit_at_21)
        self.horizontalLayout_421.setObjectName(u"horizontalLayout_421")
        self.horizontalLayout_421.setContentsMargins(0, 0, 0, 0)
        self.label_335 = QLabel(self.fahrenheit_at_21)
        self.label_335.setObjectName(u"label_335")
        self.label_335.setFont(font17)
        self.label_335.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_335.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_421.addWidget(self.label_335)

        self.stacked_cel_fah_temp_b_1.addWidget(self.fahrenheit_at_21)

        self.horizontalLayout_170.addWidget(self.stacked_cel_fah_temp_b_1)

        self.horizontalLayout_170.setStretch(0, 3)
        self.horizontalLayout_170.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_255, 1, 7, 1, 1)

        self.label_150 = QLabel(self.widget_77)
        self.label_150.setObjectName(u"label_150")
        sizePolicy.setHeightForWidth(self.label_150.sizePolicy().hasHeightForWidth())
        self.label_150.setSizePolicy(sizePolicy)
        font18 = QFont()
        font18.setPointSize(20)
        font18.setBold(True)
        font18.setItalic(False)
        self.label_150.setFont(font18)
        self.label_150.setStyleSheet(u"color: rgb(30, 136, 229);")
        self.label_150.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_150, 0, 5, 1, 1)

        self.label_123 = QLabel(self.widget_77)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setFont(font11)
        self.label_123.setStyleSheet(u"\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #e3e6ee\n"
"            );")
        self.label_123.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_123, 1, 1, 1, 1)

        self.label_124 = QLabel(self.widget_77)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setFont(font11)
        self.label_124.setStyleSheet(u"\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #e3e6ee\n"
"            );")
        self.label_124.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_124, 2, 1, 1, 1)

        self.label_125 = QLabel(self.widget_77)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setFont(font11)
        self.label_125.setStyleSheet(u"\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #e3e6ee\n"
"            );")
        self.label_125.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_125, 4, 1, 1, 1)

        self.label_126 = QLabel(self.widget_77)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setFont(font11)
        self.label_126.setStyleSheet(u"\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #e3e6ee\n"
"            );")
        self.label_126.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_126, 5, 1, 1, 1)

        self.widget_241 = QWidget(self.widget_77)
        self.widget_241.setObjectName(u"widget_241")
        self.horizontalLayout_300 = QHBoxLayout(self.widget_241)
        self.horizontalLayout_300.setSpacing(3)
        self.horizontalLayout_300.setObjectName(u"horizontalLayout_300")
        self.horizontalLayout_300.setContentsMargins(10, 0, 10, 0)
        self.widget_242 = QWidget(self.widget_241)
        self.widget_242.setObjectName(u"widget_242")
        self.widget_242.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_301 = QHBoxLayout(self.widget_242)
        self.horizontalLayout_301.setObjectName(u"horizontalLayout_301")
        self.horizontalLayout_301.setContentsMargins(2, 2, 2, 2)
        self.at_t3_offset_value = QDoubleSpinBox(self.widget_242)
        self.at_t3_offset_value.setObjectName(u"at_t3_offset_value")
        sizePolicy.setHeightForWidth(self.at_t3_offset_value.sizePolicy().hasHeightForWidth())
        self.at_t3_offset_value.setSizePolicy(sizePolicy)
        self.at_t3_offset_value.setFont(font16)
        self.at_t3_offset_value.setStyleSheet(u"")
        self.at_t3_offset_value.setWrapping(False)
        self.at_t3_offset_value.setAlignment(Qt.AlignCenter)
        self.at_t3_offset_value.setReadOnly(False)
        self.at_t3_offset_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.at_t3_offset_value.setDecimals(1)
        self.at_t3_offset_value.setMaximum(999.000000000000000)
        self.at_t3_offset_value.setValue(0.000000000000000)

        self.horizontalLayout_301.addWidget(self.at_t3_offset_value)


        self.horizontalLayout_300.addWidget(self.widget_242)

        self.stacked_cel_fah_temp_a_7 = QStackedWidget(self.widget_241)
        self.stacked_cel_fah_temp_a_7.setObjectName(u"stacked_cel_fah_temp_a_7")
        self.celsius_at_20 = QWidget()
        self.celsius_at_20.setObjectName(u"celsius_at_20")
        self.horizontalLayout_418 = QHBoxLayout(self.celsius_at_20)
        self.horizontalLayout_418.setObjectName(u"horizontalLayout_418")
        self.horizontalLayout_418.setContentsMargins(0, 0, 0, 0)
        self.label_332 = QLabel(self.celsius_at_20)
        self.label_332.setObjectName(u"label_332")
        self.label_332.setFont(font17)
        self.label_332.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_332.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_418.addWidget(self.label_332)

        self.stacked_cel_fah_temp_a_7.addWidget(self.celsius_at_20)
        self.fahrenheit_at_20 = QWidget()
        self.fahrenheit_at_20.setObjectName(u"fahrenheit_at_20")
        self.horizontalLayout_419 = QHBoxLayout(self.fahrenheit_at_20)
        self.horizontalLayout_419.setObjectName(u"horizontalLayout_419")
        self.horizontalLayout_419.setContentsMargins(0, 0, 0, 0)
        self.label_333 = QLabel(self.fahrenheit_at_20)
        self.label_333.setObjectName(u"label_333")
        self.label_333.setFont(font17)
        self.label_333.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_333.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_419.addWidget(self.label_333)

        self.stacked_cel_fah_temp_a_7.addWidget(self.fahrenheit_at_20)

        self.horizontalLayout_300.addWidget(self.stacked_cel_fah_temp_a_7)

        self.horizontalLayout_300.setStretch(0, 3)
        self.horizontalLayout_300.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_241, 9, 5, 1, 1)

        self.widget_259 = QWidget(self.widget_77)
        self.widget_259.setObjectName(u"widget_259")
        self.horizontalLayout_315 = QHBoxLayout(self.widget_259)
        self.horizontalLayout_315.setSpacing(3)
        self.horizontalLayout_315.setObjectName(u"horizontalLayout_315")
        self.horizontalLayout_315.setContentsMargins(10, 0, 10, 0)
        self.widget_260 = QWidget(self.widget_259)
        self.widget_260.setObjectName(u"widget_260")
        self.widget_260.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_316 = QHBoxLayout(self.widget_260)
        self.horizontalLayout_316.setObjectName(u"horizontalLayout_316")
        self.horizontalLayout_316.setContentsMargins(2, 2, 2, 2)
        self.bt_h_alm_value = QDoubleSpinBox(self.widget_260)
        self.bt_h_alm_value.setObjectName(u"bt_h_alm_value")
        sizePolicy.setHeightForWidth(self.bt_h_alm_value.sizePolicy().hasHeightForWidth())
        self.bt_h_alm_value.setSizePolicy(sizePolicy)
        self.bt_h_alm_value.setFont(font16)
        self.bt_h_alm_value.setStyleSheet(u"")
        self.bt_h_alm_value.setWrapping(False)
        self.bt_h_alm_value.setAlignment(Qt.AlignCenter)
        self.bt_h_alm_value.setReadOnly(False)
        self.bt_h_alm_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.bt_h_alm_value.setDecimals(1)
        self.bt_h_alm_value.setMaximum(999.000000000000000)
        self.bt_h_alm_value.setValue(0.000000000000000)

        self.horizontalLayout_316.addWidget(self.bt_h_alm_value)


        self.horizontalLayout_315.addWidget(self.widget_260)

        self.stacked_cel_fah_temp_b_3 = QStackedWidget(self.widget_259)
        self.stacked_cel_fah_temp_b_3.setObjectName(u"stacked_cel_fah_temp_b_3")
        self.celsius_bt_3 = QWidget()
        self.celsius_bt_3.setObjectName(u"celsius_bt_3")
        self.horizontalLayout_424 = QHBoxLayout(self.celsius_bt_3)
        self.horizontalLayout_424.setObjectName(u"horizontalLayout_424")
        self.horizontalLayout_424.setContentsMargins(0, 0, 0, 0)
        self.label_338 = QLabel(self.celsius_bt_3)
        self.label_338.setObjectName(u"label_338")
        self.label_338.setFont(font17)
        self.label_338.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_338.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_424.addWidget(self.label_338)

        self.stacked_cel_fah_temp_b_3.addWidget(self.celsius_bt_3)
        self.fahrenheit_at_23 = QWidget()
        self.fahrenheit_at_23.setObjectName(u"fahrenheit_at_23")
        self.horizontalLayout_425 = QHBoxLayout(self.fahrenheit_at_23)
        self.horizontalLayout_425.setObjectName(u"horizontalLayout_425")
        self.horizontalLayout_425.setContentsMargins(0, 0, 0, 0)
        self.label_339 = QLabel(self.fahrenheit_at_23)
        self.label_339.setObjectName(u"label_339")
        self.label_339.setFont(font17)
        self.label_339.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_339.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_425.addWidget(self.label_339)

        self.stacked_cel_fah_temp_b_3.addWidget(self.fahrenheit_at_23)

        self.horizontalLayout_315.addWidget(self.stacked_cel_fah_temp_b_3)

        self.horizontalLayout_315.setStretch(0, 3)
        self.horizontalLayout_315.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_259, 4, 7, 1, 1)

        self.line_26 = QFrame(self.widget_77)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_26.setFrameShape(QFrame.Shape.HLine)
        self.line_26.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_26, 6, 5, 1, 1)

        self.line_27 = QFrame(self.widget_77)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_27.setFrameShape(QFrame.Shape.HLine)
        self.line_27.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_27, 6, 7, 1, 1)

        self.line_28 = QFrame(self.widget_77)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_28.setFrameShape(QFrame.Shape.HLine)
        self.line_28.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_28, 6, 9, 1, 1)

        self.line_19 = QFrame(self.widget_77)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_19.setFrameShape(QFrame.Shape.HLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_19, 3, 5, 1, 1)

        self.line_23 = QFrame(self.widget_77)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_23.setFrameShape(QFrame.Shape.HLine)
        self.line_23.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_23, 3, 3, 1, 1)

        self.line_20 = QFrame(self.widget_77)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_20.setFrameShape(QFrame.Shape.HLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_20, 3, 7, 1, 1)

        self.line_21 = QFrame(self.widget_77)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_21.setFrameShape(QFrame.Shape.HLine)
        self.line_21.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_21, 3, 9, 1, 1)

        self.widget_239 = QWidget(self.widget_77)
        self.widget_239.setObjectName(u"widget_239")
        self.horizontalLayout_190 = QHBoxLayout(self.widget_239)
        self.horizontalLayout_190.setSpacing(3)
        self.horizontalLayout_190.setObjectName(u"horizontalLayout_190")
        self.horizontalLayout_190.setContentsMargins(10, 0, 10, 0)
        self.widget_240 = QWidget(self.widget_239)
        self.widget_240.setObjectName(u"widget_240")
        self.widget_240.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_299 = QHBoxLayout(self.widget_240)
        self.horizontalLayout_299.setObjectName(u"horizontalLayout_299")
        self.horizontalLayout_299.setContentsMargins(2, 2, 2, 2)
        self.at_h_alm_value = QDoubleSpinBox(self.widget_240)
        self.at_h_alm_value.setObjectName(u"at_h_alm_value")
        sizePolicy.setHeightForWidth(self.at_h_alm_value.sizePolicy().hasHeightForWidth())
        self.at_h_alm_value.setSizePolicy(sizePolicy)
        self.at_h_alm_value.setFont(font16)
        self.at_h_alm_value.setStyleSheet(u"")
        self.at_h_alm_value.setWrapping(False)
        self.at_h_alm_value.setAlignment(Qt.AlignCenter)
        self.at_h_alm_value.setReadOnly(False)
        self.at_h_alm_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.at_h_alm_value.setDecimals(1)
        self.at_h_alm_value.setMaximum(999.000000000000000)
        self.at_h_alm_value.setValue(0.000000000000000)

        self.horizontalLayout_299.addWidget(self.at_h_alm_value)


        self.horizontalLayout_190.addWidget(self.widget_240)

        self.stacked_cel_fah_temp_a_3 = QStackedWidget(self.widget_239)
        self.stacked_cel_fah_temp_a_3.setObjectName(u"stacked_cel_fah_temp_a_3")
        self.celsius_at_16 = QWidget()
        self.celsius_at_16.setObjectName(u"celsius_at_16")
        self.horizontalLayout_410 = QHBoxLayout(self.celsius_at_16)
        self.horizontalLayout_410.setObjectName(u"horizontalLayout_410")
        self.horizontalLayout_410.setContentsMargins(0, 0, 0, 0)
        self.label_324 = QLabel(self.celsius_at_16)
        self.label_324.setObjectName(u"label_324")
        self.label_324.setFont(font17)
        self.label_324.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_324.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_410.addWidget(self.label_324)

        self.stacked_cel_fah_temp_a_3.addWidget(self.celsius_at_16)
        self.fahrenheit_at_16 = QWidget()
        self.fahrenheit_at_16.setObjectName(u"fahrenheit_at_16")
        self.horizontalLayout_411 = QHBoxLayout(self.fahrenheit_at_16)
        self.horizontalLayout_411.setObjectName(u"horizontalLayout_411")
        self.horizontalLayout_411.setContentsMargins(0, 0, 0, 0)
        self.label_325 = QLabel(self.fahrenheit_at_16)
        self.label_325.setObjectName(u"label_325")
        self.label_325.setFont(font17)
        self.label_325.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_325.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_411.addWidget(self.label_325)

        self.stacked_cel_fah_temp_a_3.addWidget(self.fahrenheit_at_16)

        self.horizontalLayout_190.addWidget(self.stacked_cel_fah_temp_a_3)

        self.horizontalLayout_190.setStretch(0, 3)
        self.horizontalLayout_190.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_239, 4, 5, 1, 1)

        self.widget_214 = QWidget(self.widget_77)
        self.widget_214.setObjectName(u"widget_214")
        self.horizontalLayout_307 = QHBoxLayout(self.widget_214)
        self.horizontalLayout_307.setSpacing(3)
        self.horizontalLayout_307.setObjectName(u"horizontalLayout_307")
        self.horizontalLayout_307.setContentsMargins(10, 0, 10, 0)
        self.widget_243 = QWidget(self.widget_214)
        self.widget_243.setObjectName(u"widget_243")
        self.widget_243.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_308 = QHBoxLayout(self.widget_243)
        self.horizontalLayout_308.setObjectName(u"horizontalLayout_308")
        self.horizontalLayout_308.setContentsMargins(2, 2, 2, 2)
        self.ct_t2_offset_value = QDoubleSpinBox(self.widget_243)
        self.ct_t2_offset_value.setObjectName(u"ct_t2_offset_value")
        sizePolicy.setHeightForWidth(self.ct_t2_offset_value.sizePolicy().hasHeightForWidth())
        self.ct_t2_offset_value.setSizePolicy(sizePolicy)
        self.ct_t2_offset_value.setFont(font16)
        self.ct_t2_offset_value.setStyleSheet(u"")
        self.ct_t2_offset_value.setWrapping(False)
        self.ct_t2_offset_value.setAlignment(Qt.AlignCenter)
        self.ct_t2_offset_value.setReadOnly(False)
        self.ct_t2_offset_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ct_t2_offset_value.setDecimals(1)
        self.ct_t2_offset_value.setMaximum(999.000000000000000)
        self.ct_t2_offset_value.setValue(0.000000000000000)

        self.horizontalLayout_308.addWidget(self.ct_t2_offset_value)


        self.horizontalLayout_307.addWidget(self.widget_243)

        self.stacked_cel_fah_temp_c_6 = QStackedWidget(self.widget_214)
        self.stacked_cel_fah_temp_c_6.setObjectName(u"stacked_cel_fah_temp_c_6")
        self.celsius_ct_6 = QWidget()
        self.celsius_ct_6.setObjectName(u"celsius_ct_6")
        self.horizontalLayout_452 = QHBoxLayout(self.celsius_ct_6)
        self.horizontalLayout_452.setObjectName(u"horizontalLayout_452")
        self.horizontalLayout_452.setContentsMargins(0, 0, 0, 0)
        self.label_360 = QLabel(self.celsius_ct_6)
        self.label_360.setObjectName(u"label_360")
        self.label_360.setFont(font17)
        self.label_360.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_360.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_452.addWidget(self.label_360)

        self.stacked_cel_fah_temp_c_6.addWidget(self.celsius_ct_6)
        self.fahrenheit_ct_6 = QWidget()
        self.fahrenheit_ct_6.setObjectName(u"fahrenheit_ct_6")
        self.horizontalLayout_453 = QHBoxLayout(self.fahrenheit_ct_6)
        self.horizontalLayout_453.setObjectName(u"horizontalLayout_453")
        self.horizontalLayout_453.setContentsMargins(0, 0, 0, 0)
        self.label_361 = QLabel(self.fahrenheit_ct_6)
        self.label_361.setObjectName(u"label_361")
        self.label_361.setFont(font17)
        self.label_361.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_361.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_453.addWidget(self.label_361)

        self.stacked_cel_fah_temp_c_6.addWidget(self.fahrenheit_ct_6)

        self.horizontalLayout_307.addWidget(self.stacked_cel_fah_temp_c_6)

        self.horizontalLayout_307.setStretch(0, 3)
        self.horizontalLayout_307.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_214, 8, 9, 1, 1)

        self.widget_208 = QWidget(self.widget_77)
        self.widget_208.setObjectName(u"widget_208")
        self.horizontalLayout_303 = QHBoxLayout(self.widget_208)
        self.horizontalLayout_303.setSpacing(3)
        self.horizontalLayout_303.setObjectName(u"horizontalLayout_303")
        self.horizontalLayout_303.setContentsMargins(10, 0, 10, 0)
        self.widget_209 = QWidget(self.widget_208)
        self.widget_209.setObjectName(u"widget_209")
        self.widget_209.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_304 = QHBoxLayout(self.widget_209)
        self.horizontalLayout_304.setObjectName(u"horizontalLayout_304")
        self.horizontalLayout_304.setContentsMargins(2, 2, 2, 2)
        self.at_l_alm_value = QDoubleSpinBox(self.widget_209)
        self.at_l_alm_value.setObjectName(u"at_l_alm_value")
        sizePolicy.setHeightForWidth(self.at_l_alm_value.sizePolicy().hasHeightForWidth())
        self.at_l_alm_value.setSizePolicy(sizePolicy)
        self.at_l_alm_value.setFont(font16)
        self.at_l_alm_value.setStyleSheet(u"")
        self.at_l_alm_value.setWrapping(False)
        self.at_l_alm_value.setAlignment(Qt.AlignCenter)
        self.at_l_alm_value.setReadOnly(False)
        self.at_l_alm_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.at_l_alm_value.setDecimals(1)
        self.at_l_alm_value.setMaximum(999.000000000000000)
        self.at_l_alm_value.setValue(0.000000000000000)

        self.horizontalLayout_304.addWidget(self.at_l_alm_value)


        self.horizontalLayout_303.addWidget(self.widget_209)

        self.stacked_cel_fah_temp_a_4 = QStackedWidget(self.widget_208)
        self.stacked_cel_fah_temp_a_4.setObjectName(u"stacked_cel_fah_temp_a_4")
        self.celsius_at_17 = QWidget()
        self.celsius_at_17.setObjectName(u"celsius_at_17")
        self.horizontalLayout_412 = QHBoxLayout(self.celsius_at_17)
        self.horizontalLayout_412.setObjectName(u"horizontalLayout_412")
        self.horizontalLayout_412.setContentsMargins(0, 0, 0, 0)
        self.label_326 = QLabel(self.celsius_at_17)
        self.label_326.setObjectName(u"label_326")
        self.label_326.setFont(font17)
        self.label_326.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_326.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_412.addWidget(self.label_326)

        self.stacked_cel_fah_temp_a_4.addWidget(self.celsius_at_17)
        self.fahrenheit_at_17 = QWidget()
        self.fahrenheit_at_17.setObjectName(u"fahrenheit_at_17")
        self.horizontalLayout_413 = QHBoxLayout(self.fahrenheit_at_17)
        self.horizontalLayout_413.setObjectName(u"horizontalLayout_413")
        self.horizontalLayout_413.setContentsMargins(0, 0, 0, 0)
        self.label_327 = QLabel(self.fahrenheit_at_17)
        self.label_327.setObjectName(u"label_327")
        self.label_327.setFont(font17)
        self.label_327.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_327.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_413.addWidget(self.label_327)

        self.stacked_cel_fah_temp_a_4.addWidget(self.fahrenheit_at_17)

        self.horizontalLayout_303.addWidget(self.stacked_cel_fah_temp_a_4)

        self.horizontalLayout_303.setStretch(0, 3)
        self.horizontalLayout_303.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_208, 5, 5, 1, 1)

        self.widget_254 = QWidget(self.widget_77)
        self.widget_254.setObjectName(u"widget_254")
        self.horizontalLayout_326 = QHBoxLayout(self.widget_254)
        self.horizontalLayout_326.setSpacing(3)
        self.horizontalLayout_326.setObjectName(u"horizontalLayout_326")
        self.horizontalLayout_326.setContentsMargins(10, 0, 10, 0)
        self.widget_263 = QWidget(self.widget_254)
        self.widget_263.setObjectName(u"widget_263")
        self.widget_263.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_327 = QHBoxLayout(self.widget_263)
        self.horizontalLayout_327.setObjectName(u"horizontalLayout_327")
        self.horizontalLayout_327.setContentsMargins(2, 2, 2, 2)
        self.ct_t1_offset_value = QDoubleSpinBox(self.widget_263)
        self.ct_t1_offset_value.setObjectName(u"ct_t1_offset_value")
        sizePolicy.setHeightForWidth(self.ct_t1_offset_value.sizePolicy().hasHeightForWidth())
        self.ct_t1_offset_value.setSizePolicy(sizePolicy)
        self.ct_t1_offset_value.setFont(font16)
        self.ct_t1_offset_value.setStyleSheet(u"")
        self.ct_t1_offset_value.setWrapping(False)
        self.ct_t1_offset_value.setAlignment(Qt.AlignCenter)
        self.ct_t1_offset_value.setReadOnly(False)
        self.ct_t1_offset_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ct_t1_offset_value.setDecimals(1)
        self.ct_t1_offset_value.setMaximum(999.000000000000000)
        self.ct_t1_offset_value.setValue(0.000000000000000)

        self.horizontalLayout_327.addWidget(self.ct_t1_offset_value)


        self.horizontalLayout_326.addWidget(self.widget_263)

        self.stacked_cel_fah_temp_c_5 = QStackedWidget(self.widget_254)
        self.stacked_cel_fah_temp_c_5.setObjectName(u"stacked_cel_fah_temp_c_5")
        self.celsius_ct_5 = QWidget()
        self.celsius_ct_5.setObjectName(u"celsius_ct_5")
        self.horizontalLayout_450 = QHBoxLayout(self.celsius_ct_5)
        self.horizontalLayout_450.setObjectName(u"horizontalLayout_450")
        self.horizontalLayout_450.setContentsMargins(0, 0, 0, 0)
        self.label_358 = QLabel(self.celsius_ct_5)
        self.label_358.setObjectName(u"label_358")
        self.label_358.setFont(font17)
        self.label_358.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_358.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_450.addWidget(self.label_358)

        self.stacked_cel_fah_temp_c_5.addWidget(self.celsius_ct_5)
        self.fahrenheit_ct_5 = QWidget()
        self.fahrenheit_ct_5.setObjectName(u"fahrenheit_ct_5")
        self.horizontalLayout_451 = QHBoxLayout(self.fahrenheit_ct_5)
        self.horizontalLayout_451.setObjectName(u"horizontalLayout_451")
        self.horizontalLayout_451.setContentsMargins(0, 0, 0, 0)
        self.label_359 = QLabel(self.fahrenheit_ct_5)
        self.label_359.setObjectName(u"label_359")
        self.label_359.setFont(font17)
        self.label_359.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_359.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_451.addWidget(self.label_359)

        self.stacked_cel_fah_temp_c_5.addWidget(self.fahrenheit_ct_5)

        self.horizontalLayout_326.addWidget(self.stacked_cel_fah_temp_c_5)

        self.horizontalLayout_326.setStretch(0, 3)
        self.horizontalLayout_326.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_254, 7, 9, 1, 1)

        self.widget_252 = QWidget(self.widget_77)
        self.widget_252.setObjectName(u"widget_252")
        self.horizontalLayout_324 = QHBoxLayout(self.widget_252)
        self.horizontalLayout_324.setSpacing(3)
        self.horizontalLayout_324.setObjectName(u"horizontalLayout_324")
        self.horizontalLayout_324.setContentsMargins(10, 0, 10, 0)
        self.widget_253 = QWidget(self.widget_252)
        self.widget_253.setObjectName(u"widget_253")
        self.widget_253.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_325 = QHBoxLayout(self.widget_253)
        self.horizontalLayout_325.setObjectName(u"horizontalLayout_325")
        self.horizontalLayout_325.setContentsMargins(2, 2, 2, 2)
        self.bt_t1_offset_value = QDoubleSpinBox(self.widget_253)
        self.bt_t1_offset_value.setObjectName(u"bt_t1_offset_value")
        sizePolicy.setHeightForWidth(self.bt_t1_offset_value.sizePolicy().hasHeightForWidth())
        self.bt_t1_offset_value.setSizePolicy(sizePolicy)
        self.bt_t1_offset_value.setFont(font16)
        self.bt_t1_offset_value.setStyleSheet(u"")
        self.bt_t1_offset_value.setWrapping(False)
        self.bt_t1_offset_value.setAlignment(Qt.AlignCenter)
        self.bt_t1_offset_value.setReadOnly(False)
        self.bt_t1_offset_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.bt_t1_offset_value.setDecimals(1)
        self.bt_t1_offset_value.setMaximum(999.000000000000000)
        self.bt_t1_offset_value.setValue(0.000000000000000)

        self.horizontalLayout_325.addWidget(self.bt_t1_offset_value)


        self.horizontalLayout_324.addWidget(self.widget_253)

        self.stacked_cel_fah_temp_b_5 = QStackedWidget(self.widget_252)
        self.stacked_cel_fah_temp_b_5.setObjectName(u"stacked_cel_fah_temp_b_5")
        self.celsius_bt_6 = QWidget()
        self.celsius_bt_6.setObjectName(u"celsius_bt_6")
        self.horizontalLayout_430 = QHBoxLayout(self.celsius_bt_6)
        self.horizontalLayout_430.setObjectName(u"horizontalLayout_430")
        self.horizontalLayout_430.setContentsMargins(0, 0, 0, 0)
        self.label_344 = QLabel(self.celsius_bt_6)
        self.label_344.setObjectName(u"label_344")
        self.label_344.setFont(font17)
        self.label_344.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_344.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_430.addWidget(self.label_344)

        self.stacked_cel_fah_temp_b_5.addWidget(self.celsius_bt_6)
        self.fahrenheit_at_26 = QWidget()
        self.fahrenheit_at_26.setObjectName(u"fahrenheit_at_26")
        self.horizontalLayout_431 = QHBoxLayout(self.fahrenheit_at_26)
        self.horizontalLayout_431.setObjectName(u"horizontalLayout_431")
        self.horizontalLayout_431.setContentsMargins(0, 0, 0, 0)
        self.label_345 = QLabel(self.fahrenheit_at_26)
        self.label_345.setObjectName(u"label_345")
        self.label_345.setFont(font17)
        self.label_345.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_345.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_431.addWidget(self.label_345)

        self.stacked_cel_fah_temp_b_5.addWidget(self.fahrenheit_at_26)

        self.horizontalLayout_324.addWidget(self.stacked_cel_fah_temp_b_5)

        self.horizontalLayout_324.setStretch(0, 3)
        self.horizontalLayout_324.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_252, 7, 7, 1, 1)

        self.widget_210 = QWidget(self.widget_77)
        self.widget_210.setObjectName(u"widget_210")
        self.horizontalLayout_305 = QHBoxLayout(self.widget_210)
        self.horizontalLayout_305.setSpacing(3)
        self.horizontalLayout_305.setObjectName(u"horizontalLayout_305")
        self.horizontalLayout_305.setContentsMargins(10, 0, 10, 0)
        self.widget_213 = QWidget(self.widget_210)
        self.widget_213.setObjectName(u"widget_213")
        self.widget_213.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_306 = QHBoxLayout(self.widget_213)
        self.horizontalLayout_306.setObjectName(u"horizontalLayout_306")
        self.horizontalLayout_306.setContentsMargins(2, 2, 2, 2)
        self.bt_t2_offset_value = QDoubleSpinBox(self.widget_213)
        self.bt_t2_offset_value.setObjectName(u"bt_t2_offset_value")
        sizePolicy.setHeightForWidth(self.bt_t2_offset_value.sizePolicy().hasHeightForWidth())
        self.bt_t2_offset_value.setSizePolicy(sizePolicy)
        self.bt_t2_offset_value.setFont(font16)
        self.bt_t2_offset_value.setStyleSheet(u"")
        self.bt_t2_offset_value.setWrapping(False)
        self.bt_t2_offset_value.setAlignment(Qt.AlignCenter)
        self.bt_t2_offset_value.setReadOnly(False)
        self.bt_t2_offset_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.bt_t2_offset_value.setDecimals(1)
        self.bt_t2_offset_value.setMaximum(999.000000000000000)
        self.bt_t2_offset_value.setValue(0.000000000000000)

        self.horizontalLayout_306.addWidget(self.bt_t2_offset_value)


        self.horizontalLayout_305.addWidget(self.widget_213)

        self.stacked_cel_fah_temp_b_6 = QStackedWidget(self.widget_210)
        self.stacked_cel_fah_temp_b_6.setObjectName(u"stacked_cel_fah_temp_b_6")
        self.celsius_bt_7 = QWidget()
        self.celsius_bt_7.setObjectName(u"celsius_bt_7")
        self.horizontalLayout_435 = QHBoxLayout(self.celsius_bt_7)
        self.horizontalLayout_435.setObjectName(u"horizontalLayout_435")
        self.horizontalLayout_435.setContentsMargins(0, 0, 0, 0)
        self.label_346 = QLabel(self.celsius_bt_7)
        self.label_346.setObjectName(u"label_346")
        self.label_346.setFont(font17)
        self.label_346.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_346.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_435.addWidget(self.label_346)

        self.stacked_cel_fah_temp_b_6.addWidget(self.celsius_bt_7)
        self.fahrenheit_at_27 = QWidget()
        self.fahrenheit_at_27.setObjectName(u"fahrenheit_at_27")
        self.horizontalLayout_436 = QHBoxLayout(self.fahrenheit_at_27)
        self.horizontalLayout_436.setObjectName(u"horizontalLayout_436")
        self.horizontalLayout_436.setContentsMargins(0, 0, 0, 0)
        self.label_347 = QLabel(self.fahrenheit_at_27)
        self.label_347.setObjectName(u"label_347")
        self.label_347.setFont(font17)
        self.label_347.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_347.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_436.addWidget(self.label_347)

        self.stacked_cel_fah_temp_b_6.addWidget(self.fahrenheit_at_27)

        self.horizontalLayout_305.addWidget(self.stacked_cel_fah_temp_b_6)

        self.horizontalLayout_305.setStretch(0, 3)
        self.horizontalLayout_305.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_210, 8, 7, 1, 1)

        self.label_139 = QLabel(self.widget_77)
        self.label_139.setObjectName(u"label_139")
        sizePolicy.setHeightForWidth(self.label_139.sizePolicy().hasHeightForWidth())
        self.label_139.setSizePolicy(sizePolicy)
        self.label_139.setFont(font18)
        self.label_139.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_139.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_139, 0, 3, 1, 1)

        self.label_183 = QLabel(self.widget_77)
        self.label_183.setObjectName(u"label_183")
        sizePolicy.setHeightForWidth(self.label_183.sizePolicy().hasHeightForWidth())
        self.label_183.setSizePolicy(sizePolicy)
        self.label_183.setFont(font18)
        self.label_183.setStyleSheet(u"color: #6F00FF;")
        self.label_183.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_183, 0, 9, 1, 1)

        self.label_173 = QLabel(self.widget_77)
        self.label_173.setObjectName(u"label_173")
        sizePolicy.setHeightForWidth(self.label_173.sizePolicy().hasHeightForWidth())
        self.label_173.setSizePolicy(sizePolicy)
        self.label_173.setFont(font18)
        self.label_173.setStyleSheet(u"color: rgb(251, 140, 0);")
        self.label_173.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_173, 0, 7, 1, 1)

        self.line_18 = QFrame(self.widget_77)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_18.setFrameShape(QFrame.Shape.VLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_18, 1, 2, 9, 1)

        self.line_25 = QFrame(self.widget_77)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_25.setFrameShape(QFrame.Shape.HLine)
        self.line_25.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_25, 6, 3, 1, 1)

        self.line_12 = QFrame(self.widget_77)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setStyleSheet(u"border: 1px solid rgb(22, 93, 200)")
        self.line_12.setFrameShape(QFrame.Shape.VLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_12, 1, 8, 9, 1)

        self.widget_277 = QWidget(self.widget_77)
        self.widget_277.setObjectName(u"widget_277")
        self.horizontalLayout_330 = QHBoxLayout(self.widget_277)
        self.horizontalLayout_330.setSpacing(3)
        self.horizontalLayout_330.setObjectName(u"horizontalLayout_330")
        self.horizontalLayout_330.setContentsMargins(10, 0, 10, 0)
        self.widget_278 = QWidget(self.widget_277)
        self.widget_278.setObjectName(u"widget_278")
        self.widget_278.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_331 = QHBoxLayout(self.widget_278)
        self.horizontalLayout_331.setObjectName(u"horizontalLayout_331")
        self.horizontalLayout_331.setContentsMargins(2, 2, 2, 2)
        self.ct_sv = QDoubleSpinBox(self.widget_278)
        self.ct_sv.setObjectName(u"ct_sv")
        sizePolicy.setHeightForWidth(self.ct_sv.sizePolicy().hasHeightForWidth())
        self.ct_sv.setSizePolicy(sizePolicy)
        self.ct_sv.setFont(font16)
        self.ct_sv.setStyleSheet(u"")
        self.ct_sv.setWrapping(False)
        self.ct_sv.setAlignment(Qt.AlignCenter)
        self.ct_sv.setReadOnly(False)
        self.ct_sv.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ct_sv.setDecimals(1)
        self.ct_sv.setMaximum(999.000000000000000)
        self.ct_sv.setValue(0.000000000000000)

        self.horizontalLayout_331.addWidget(self.ct_sv)


        self.horizontalLayout_330.addWidget(self.widget_278)

        self.stacked_cel_fah_temp_c_2 = QStackedWidget(self.widget_277)
        self.stacked_cel_fah_temp_c_2.setObjectName(u"stacked_cel_fah_temp_c_2")
        self.celsius_ct_2 = QWidget()
        self.celsius_ct_2.setObjectName(u"celsius_ct_2")
        self.horizontalLayout_444 = QHBoxLayout(self.celsius_ct_2)
        self.horizontalLayout_444.setObjectName(u"horizontalLayout_444")
        self.horizontalLayout_444.setContentsMargins(0, 0, 0, 0)
        self.label_352 = QLabel(self.celsius_ct_2)
        self.label_352.setObjectName(u"label_352")
        self.label_352.setFont(font17)
        self.label_352.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_352.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_444.addWidget(self.label_352)

        self.stacked_cel_fah_temp_c_2.addWidget(self.celsius_ct_2)
        self.fahrenheit_ct_2 = QWidget()
        self.fahrenheit_ct_2.setObjectName(u"fahrenheit_ct_2")
        self.horizontalLayout_445 = QHBoxLayout(self.fahrenheit_ct_2)
        self.horizontalLayout_445.setObjectName(u"horizontalLayout_445")
        self.horizontalLayout_445.setContentsMargins(0, 0, 0, 0)
        self.label_353 = QLabel(self.fahrenheit_ct_2)
        self.label_353.setObjectName(u"label_353")
        self.label_353.setFont(font17)
        self.label_353.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_353.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_445.addWidget(self.label_353)

        self.stacked_cel_fah_temp_c_2.addWidget(self.fahrenheit_ct_2)

        self.horizontalLayout_330.addWidget(self.stacked_cel_fah_temp_c_2)

        self.horizontalLayout_330.setStretch(0, 3)
        self.horizontalLayout_330.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_277, 2, 9, 1, 1)

        self.widget_220 = QWidget(self.widget_77)
        self.widget_220.setObjectName(u"widget_220")
        self.horizontalLayout_167 = QHBoxLayout(self.widget_220)
        self.horizontalLayout_167.setSpacing(3)
        self.horizontalLayout_167.setObjectName(u"horizontalLayout_167")
        self.horizontalLayout_167.setContentsMargins(10, 0, 10, 0)
        self.widget_222 = QWidget(self.widget_220)
        self.widget_222.setObjectName(u"widget_222")
        self.widget_222.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_297 = QHBoxLayout(self.widget_222)
        self.horizontalLayout_297.setObjectName(u"horizontalLayout_297")
        self.horizontalLayout_297.setContentsMargins(2, 2, 2, 2)
        self.at_pv = QDoubleSpinBox(self.widget_222)
        self.at_pv.setObjectName(u"at_pv")
        sizePolicy.setHeightForWidth(self.at_pv.sizePolicy().hasHeightForWidth())
        self.at_pv.setSizePolicy(sizePolicy)
        self.at_pv.setFont(font16)
        self.at_pv.setStyleSheet(u"")
        self.at_pv.setWrapping(True)
        self.at_pv.setAlignment(Qt.AlignCenter)
        self.at_pv.setReadOnly(True)
        self.at_pv.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.at_pv.setDecimals(1)
        self.at_pv.setMaximum(999.000000000000000)
        self.at_pv.setValue(0.000000000000000)

        self.horizontalLayout_297.addWidget(self.at_pv)


        self.horizontalLayout_167.addWidget(self.widget_222)

        self.stacked_cel_fah_temp_a_1 = QStackedWidget(self.widget_220)
        self.stacked_cel_fah_temp_a_1.setObjectName(u"stacked_cel_fah_temp_a_1")
        self.celsius_at_14 = QWidget()
        self.celsius_at_14.setObjectName(u"celsius_at_14")
        self.horizontalLayout_406 = QHBoxLayout(self.celsius_at_14)
        self.horizontalLayout_406.setObjectName(u"horizontalLayout_406")
        self.horizontalLayout_406.setContentsMargins(0, 0, 0, 0)
        self.label_320 = QLabel(self.celsius_at_14)
        self.label_320.setObjectName(u"label_320")
        self.label_320.setFont(font17)
        self.label_320.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_320.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_406.addWidget(self.label_320)

        self.stacked_cel_fah_temp_a_1.addWidget(self.celsius_at_14)
        self.fahrenheit_at_14 = QWidget()
        self.fahrenheit_at_14.setObjectName(u"fahrenheit_at_14")
        self.horizontalLayout_407 = QHBoxLayout(self.fahrenheit_at_14)
        self.horizontalLayout_407.setObjectName(u"horizontalLayout_407")
        self.horizontalLayout_407.setContentsMargins(0, 0, 0, 0)
        self.label_321 = QLabel(self.fahrenheit_at_14)
        self.label_321.setObjectName(u"label_321")
        self.label_321.setFont(font17)
        self.label_321.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_321.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_407.addWidget(self.label_321)

        self.stacked_cel_fah_temp_a_1.addWidget(self.fahrenheit_at_14)

        self.horizontalLayout_167.addWidget(self.stacked_cel_fah_temp_a_1)

        self.horizontalLayout_167.setStretch(0, 3)
        self.horizontalLayout_167.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_220, 1, 5, 1, 1)

        self.widget_279 = QWidget(self.widget_77)
        self.widget_279.setObjectName(u"widget_279")
        self.horizontalLayout_332 = QHBoxLayout(self.widget_279)
        self.horizontalLayout_332.setSpacing(3)
        self.horizontalLayout_332.setObjectName(u"horizontalLayout_332")
        self.horizontalLayout_332.setContentsMargins(10, 0, 10, 0)
        self.widget_280 = QWidget(self.widget_279)
        self.widget_280.setObjectName(u"widget_280")
        self.widget_280.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_333 = QHBoxLayout(self.widget_280)
        self.horizontalLayout_333.setObjectName(u"horizontalLayout_333")
        self.horizontalLayout_333.setContentsMargins(2, 2, 2, 2)
        self.ct_h_alm_value = QDoubleSpinBox(self.widget_280)
        self.ct_h_alm_value.setObjectName(u"ct_h_alm_value")
        sizePolicy.setHeightForWidth(self.ct_h_alm_value.sizePolicy().hasHeightForWidth())
        self.ct_h_alm_value.setSizePolicy(sizePolicy)
        self.ct_h_alm_value.setFont(font16)
        self.ct_h_alm_value.setStyleSheet(u"")
        self.ct_h_alm_value.setWrapping(False)
        self.ct_h_alm_value.setAlignment(Qt.AlignCenter)
        self.ct_h_alm_value.setReadOnly(False)
        self.ct_h_alm_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ct_h_alm_value.setDecimals(1)
        self.ct_h_alm_value.setMaximum(999.000000000000000)
        self.ct_h_alm_value.setValue(0.000000000000000)

        self.horizontalLayout_333.addWidget(self.ct_h_alm_value)


        self.horizontalLayout_332.addWidget(self.widget_280)

        self.stacked_cel_fah_temp_c_3 = QStackedWidget(self.widget_279)
        self.stacked_cel_fah_temp_c_3.setObjectName(u"stacked_cel_fah_temp_c_3")
        self.celsius_ct_3 = QWidget()
        self.celsius_ct_3.setObjectName(u"celsius_ct_3")
        self.horizontalLayout_446 = QHBoxLayout(self.celsius_ct_3)
        self.horizontalLayout_446.setObjectName(u"horizontalLayout_446")
        self.horizontalLayout_446.setContentsMargins(0, 0, 0, 0)
        self.label_354 = QLabel(self.celsius_ct_3)
        self.label_354.setObjectName(u"label_354")
        self.label_354.setFont(font17)
        self.label_354.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_354.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_446.addWidget(self.label_354)

        self.stacked_cel_fah_temp_c_3.addWidget(self.celsius_ct_3)
        self.fahrenheit_ct_3 = QWidget()
        self.fahrenheit_ct_3.setObjectName(u"fahrenheit_ct_3")
        self.horizontalLayout_447 = QHBoxLayout(self.fahrenheit_ct_3)
        self.horizontalLayout_447.setObjectName(u"horizontalLayout_447")
        self.horizontalLayout_447.setContentsMargins(0, 0, 0, 0)
        self.label_355 = QLabel(self.fahrenheit_ct_3)
        self.label_355.setObjectName(u"label_355")
        self.label_355.setFont(font17)
        self.label_355.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_355.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_447.addWidget(self.label_355)

        self.stacked_cel_fah_temp_c_3.addWidget(self.fahrenheit_ct_3)

        self.horizontalLayout_332.addWidget(self.stacked_cel_fah_temp_c_3)

        self.horizontalLayout_332.setStretch(0, 3)
        self.horizontalLayout_332.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_279, 4, 9, 1, 1)

        self.widget_275 = QWidget(self.widget_77)
        self.widget_275.setObjectName(u"widget_275")
        self.horizontalLayout_173 = QHBoxLayout(self.widget_275)
        self.horizontalLayout_173.setSpacing(3)
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.horizontalLayout_173.setContentsMargins(10, 0, 10, 0)
        self.widget_276 = QWidget(self.widget_275)
        self.widget_276.setObjectName(u"widget_276")
        self.widget_276.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_329 = QHBoxLayout(self.widget_276)
        self.horizontalLayout_329.setObjectName(u"horizontalLayout_329")
        self.horizontalLayout_329.setContentsMargins(2, 2, 2, 2)
        self.ct_pv = QDoubleSpinBox(self.widget_276)
        self.ct_pv.setObjectName(u"ct_pv")
        sizePolicy.setHeightForWidth(self.ct_pv.sizePolicy().hasHeightForWidth())
        self.ct_pv.setSizePolicy(sizePolicy)
        self.ct_pv.setFont(font16)
        self.ct_pv.setStyleSheet(u"")
        self.ct_pv.setWrapping(True)
        self.ct_pv.setAlignment(Qt.AlignCenter)
        self.ct_pv.setReadOnly(True)
        self.ct_pv.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ct_pv.setDecimals(1)
        self.ct_pv.setMaximum(999.000000000000000)
        self.ct_pv.setValue(0.000000000000000)

        self.horizontalLayout_329.addWidget(self.ct_pv)


        self.horizontalLayout_173.addWidget(self.widget_276)

        self.stacked_cel_fah_temp_c_1 = QStackedWidget(self.widget_275)
        self.stacked_cel_fah_temp_c_1.setObjectName(u"stacked_cel_fah_temp_c_1")
        self.celsius_ct_1 = QWidget()
        self.celsius_ct_1.setObjectName(u"celsius_ct_1")
        self.horizontalLayout_442 = QHBoxLayout(self.celsius_ct_1)
        self.horizontalLayout_442.setObjectName(u"horizontalLayout_442")
        self.horizontalLayout_442.setContentsMargins(0, 0, 0, 0)
        self.label_350 = QLabel(self.celsius_ct_1)
        self.label_350.setObjectName(u"label_350")
        self.label_350.setFont(font17)
        self.label_350.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_350.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_442.addWidget(self.label_350)

        self.stacked_cel_fah_temp_c_1.addWidget(self.celsius_ct_1)
        self.fahrenheit_ct_1 = QWidget()
        self.fahrenheit_ct_1.setObjectName(u"fahrenheit_ct_1")
        self.horizontalLayout_443 = QHBoxLayout(self.fahrenheit_ct_1)
        self.horizontalLayout_443.setObjectName(u"horizontalLayout_443")
        self.horizontalLayout_443.setContentsMargins(0, 0, 0, 0)
        self.label_351 = QLabel(self.fahrenheit_ct_1)
        self.label_351.setObjectName(u"label_351")
        self.label_351.setFont(font17)
        self.label_351.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_351.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_443.addWidget(self.label_351)

        self.stacked_cel_fah_temp_c_1.addWidget(self.fahrenheit_ct_1)

        self.horizontalLayout_173.addWidget(self.stacked_cel_fah_temp_c_1)

        self.horizontalLayout_173.setStretch(0, 3)
        self.horizontalLayout_173.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_275, 1, 9, 1, 1)

        self.widget_228 = QWidget(self.widget_77)
        self.widget_228.setObjectName(u"widget_228")
        self.horizontalLayout_189 = QHBoxLayout(self.widget_228)
        self.horizontalLayout_189.setSpacing(3)
        self.horizontalLayout_189.setObjectName(u"horizontalLayout_189")
        self.horizontalLayout_189.setContentsMargins(10, 0, 10, 0)
        self.widget_230 = QWidget(self.widget_228)
        self.widget_230.setObjectName(u"widget_230")
        self.widget_230.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_298 = QHBoxLayout(self.widget_230)
        self.horizontalLayout_298.setObjectName(u"horizontalLayout_298")
        self.horizontalLayout_298.setContentsMargins(2, 2, 2, 2)
        self.at_sv = QDoubleSpinBox(self.widget_230)
        self.at_sv.setObjectName(u"at_sv")
        sizePolicy.setHeightForWidth(self.at_sv.sizePolicy().hasHeightForWidth())
        self.at_sv.setSizePolicy(sizePolicy)
        self.at_sv.setFont(font16)
        self.at_sv.setStyleSheet(u"")
        self.at_sv.setWrapping(False)
        self.at_sv.setAlignment(Qt.AlignCenter)
        self.at_sv.setReadOnly(False)
        self.at_sv.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.at_sv.setDecimals(1)
        self.at_sv.setMaximum(999.000000000000000)
        self.at_sv.setValue(0.000000000000000)

        self.horizontalLayout_298.addWidget(self.at_sv)


        self.horizontalLayout_189.addWidget(self.widget_230)

        self.stacked_cel_fah_temp_a_2 = QStackedWidget(self.widget_228)
        self.stacked_cel_fah_temp_a_2.setObjectName(u"stacked_cel_fah_temp_a_2")
        self.celsius_at_15 = QWidget()
        self.celsius_at_15.setObjectName(u"celsius_at_15")
        self.horizontalLayout_408 = QHBoxLayout(self.celsius_at_15)
        self.horizontalLayout_408.setObjectName(u"horizontalLayout_408")
        self.horizontalLayout_408.setContentsMargins(0, 0, 0, 0)
        self.label_322 = QLabel(self.celsius_at_15)
        self.label_322.setObjectName(u"label_322")
        self.label_322.setFont(font17)
        self.label_322.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_322.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_408.addWidget(self.label_322)

        self.stacked_cel_fah_temp_a_2.addWidget(self.celsius_at_15)
        self.fahrenheit_at_15 = QWidget()
        self.fahrenheit_at_15.setObjectName(u"fahrenheit_at_15")
        self.horizontalLayout_409 = QHBoxLayout(self.fahrenheit_at_15)
        self.horizontalLayout_409.setObjectName(u"horizontalLayout_409")
        self.horizontalLayout_409.setContentsMargins(0, 0, 0, 0)
        self.label_323 = QLabel(self.fahrenheit_at_15)
        self.label_323.setObjectName(u"label_323")
        self.label_323.setFont(font17)
        self.label_323.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_323.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_409.addWidget(self.label_323)

        self.stacked_cel_fah_temp_a_2.addWidget(self.fahrenheit_at_15)

        self.horizontalLayout_189.addWidget(self.stacked_cel_fah_temp_a_2)

        self.horizontalLayout_189.setStretch(0, 3)
        self.horizontalLayout_189.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_228, 2, 5, 1, 1)

        self.widget_250 = QWidget(self.widget_77)
        self.widget_250.setObjectName(u"widget_250")
        self.horizontalLayout_322 = QHBoxLayout(self.widget_250)
        self.horizontalLayout_322.setSpacing(3)
        self.horizontalLayout_322.setObjectName(u"horizontalLayout_322")
        self.horizontalLayout_322.setContentsMargins(10, 0, 10, 0)
        self.widget_251 = QWidget(self.widget_250)
        self.widget_251.setObjectName(u"widget_251")
        self.widget_251.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_323 = QHBoxLayout(self.widget_251)
        self.horizontalLayout_323.setObjectName(u"horizontalLayout_323")
        self.horizontalLayout_323.setContentsMargins(2, 2, 2, 2)
        self.ct_l_alm_value = QDoubleSpinBox(self.widget_251)
        self.ct_l_alm_value.setObjectName(u"ct_l_alm_value")
        sizePolicy.setHeightForWidth(self.ct_l_alm_value.sizePolicy().hasHeightForWidth())
        self.ct_l_alm_value.setSizePolicy(sizePolicy)
        self.ct_l_alm_value.setFont(font16)
        self.ct_l_alm_value.setStyleSheet(u"")
        self.ct_l_alm_value.setWrapping(False)
        self.ct_l_alm_value.setAlignment(Qt.AlignCenter)
        self.ct_l_alm_value.setReadOnly(False)
        self.ct_l_alm_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ct_l_alm_value.setDecimals(1)
        self.ct_l_alm_value.setMaximum(999.000000000000000)
        self.ct_l_alm_value.setValue(0.000000000000000)

        self.horizontalLayout_323.addWidget(self.ct_l_alm_value)


        self.horizontalLayout_322.addWidget(self.widget_251)

        self.stacked_cel_fah_temp_c_4 = QStackedWidget(self.widget_250)
        self.stacked_cel_fah_temp_c_4.setObjectName(u"stacked_cel_fah_temp_c_4")
        self.celsius_ct_4 = QWidget()
        self.celsius_ct_4.setObjectName(u"celsius_ct_4")
        self.horizontalLayout_448 = QHBoxLayout(self.celsius_ct_4)
        self.horizontalLayout_448.setObjectName(u"horizontalLayout_448")
        self.horizontalLayout_448.setContentsMargins(0, 0, 0, 0)
        self.label_356 = QLabel(self.celsius_ct_4)
        self.label_356.setObjectName(u"label_356")
        self.label_356.setFont(font17)
        self.label_356.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_356.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_448.addWidget(self.label_356)

        self.stacked_cel_fah_temp_c_4.addWidget(self.celsius_ct_4)
        self.fahrenheit_ct_4 = QWidget()
        self.fahrenheit_ct_4.setObjectName(u"fahrenheit_ct_4")
        self.horizontalLayout_449 = QHBoxLayout(self.fahrenheit_ct_4)
        self.horizontalLayout_449.setObjectName(u"horizontalLayout_449")
        self.horizontalLayout_449.setContentsMargins(0, 0, 0, 0)
        self.label_357 = QLabel(self.fahrenheit_ct_4)
        self.label_357.setObjectName(u"label_357")
        self.label_357.setFont(font17)
        self.label_357.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_357.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_449.addWidget(self.label_357)

        self.stacked_cel_fah_temp_c_4.addWidget(self.fahrenheit_ct_4)

        self.horizontalLayout_322.addWidget(self.stacked_cel_fah_temp_c_4)

        self.horizontalLayout_322.setStretch(0, 3)
        self.horizontalLayout_322.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_250, 5, 9, 1, 1)

        self.widget_281 = QWidget(self.widget_77)
        self.widget_281.setObjectName(u"widget_281")
        self.horizontalLayout_334 = QHBoxLayout(self.widget_281)
        self.horizontalLayout_334.setSpacing(3)
        self.horizontalLayout_334.setObjectName(u"horizontalLayout_334")
        self.horizontalLayout_334.setContentsMargins(10, 0, 10, 0)
        self.widget_282 = QWidget(self.widget_281)
        self.widget_282.setObjectName(u"widget_282")
        self.widget_282.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_335 = QHBoxLayout(self.widget_282)
        self.horizontalLayout_335.setObjectName(u"horizontalLayout_335")
        self.horizontalLayout_335.setContentsMargins(2, 2, 2, 2)
        self.ct_t3_offset_value = QDoubleSpinBox(self.widget_282)
        self.ct_t3_offset_value.setObjectName(u"ct_t3_offset_value")
        sizePolicy.setHeightForWidth(self.ct_t3_offset_value.sizePolicy().hasHeightForWidth())
        self.ct_t3_offset_value.setSizePolicy(sizePolicy)
        self.ct_t3_offset_value.setFont(font16)
        self.ct_t3_offset_value.setStyleSheet(u"")
        self.ct_t3_offset_value.setWrapping(False)
        self.ct_t3_offset_value.setAlignment(Qt.AlignCenter)
        self.ct_t3_offset_value.setReadOnly(False)
        self.ct_t3_offset_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ct_t3_offset_value.setDecimals(1)
        self.ct_t3_offset_value.setMaximum(999.000000000000000)
        self.ct_t3_offset_value.setValue(0.000000000000000)

        self.horizontalLayout_335.addWidget(self.ct_t3_offset_value)


        self.horizontalLayout_334.addWidget(self.widget_282)

        self.stacked_cel_fah_temp_c_7 = QStackedWidget(self.widget_281)
        self.stacked_cel_fah_temp_c_7.setObjectName(u"stacked_cel_fah_temp_c_7")
        self.celsius_ct_7 = QWidget()
        self.celsius_ct_7.setObjectName(u"celsius_ct_7")
        self.horizontalLayout_454 = QHBoxLayout(self.celsius_ct_7)
        self.horizontalLayout_454.setObjectName(u"horizontalLayout_454")
        self.horizontalLayout_454.setContentsMargins(0, 0, 0, 0)
        self.label_362 = QLabel(self.celsius_ct_7)
        self.label_362.setObjectName(u"label_362")
        self.label_362.setFont(font17)
        self.label_362.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_362.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_454.addWidget(self.label_362)

        self.stacked_cel_fah_temp_c_7.addWidget(self.celsius_ct_7)
        self.fahrenheit_ct_7 = QWidget()
        self.fahrenheit_ct_7.setObjectName(u"fahrenheit_ct_7")
        self.horizontalLayout_455 = QHBoxLayout(self.fahrenheit_ct_7)
        self.horizontalLayout_455.setObjectName(u"horizontalLayout_455")
        self.horizontalLayout_455.setContentsMargins(0, 0, 0, 0)
        self.label_363 = QLabel(self.fahrenheit_ct_7)
        self.label_363.setObjectName(u"label_363")
        self.label_363.setFont(font17)
        self.label_363.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_363.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_455.addWidget(self.label_363)

        self.stacked_cel_fah_temp_c_7.addWidget(self.fahrenheit_ct_7)

        self.horizontalLayout_334.addWidget(self.stacked_cel_fah_temp_c_7)

        self.horizontalLayout_334.setStretch(0, 3)
        self.horizontalLayout_334.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_281, 9, 9, 1, 1)

        self.label_135 = QLabel(self.widget_77)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setFont(font11)
        self.label_135.setStyleSheet(u"\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #e3e6ee\n"
"            );")
        self.label_135.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_135, 8, 1, 1, 1)

        self.widget_266 = QWidget(self.widget_77)
        self.widget_266.setObjectName(u"widget_266")
        self.horizontalLayout_337 = QHBoxLayout(self.widget_266)
        self.horizontalLayout_337.setSpacing(3)
        self.horizontalLayout_337.setObjectName(u"horizontalLayout_337")
        self.horizontalLayout_337.setContentsMargins(10, 0, 10, 0)
        self.widget_267 = QWidget(self.widget_266)
        self.widget_267.setObjectName(u"widget_267")
        self.widget_267.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_338 = QHBoxLayout(self.widget_267)
        self.horizontalLayout_338.setObjectName(u"horizontalLayout_338")
        self.horizontalLayout_338.setContentsMargins(2, 2, 2, 2)
        self.t0_offset_value = QDoubleSpinBox(self.widget_267)
        self.t0_offset_value.setObjectName(u"t0_offset_value")
        sizePolicy.setHeightForWidth(self.t0_offset_value.sizePolicy().hasHeightForWidth())
        self.t0_offset_value.setSizePolicy(sizePolicy)
        self.t0_offset_value.setFont(font16)
        self.t0_offset_value.setStyleSheet(u"")
        self.t0_offset_value.setWrapping(False)
        self.t0_offset_value.setAlignment(Qt.AlignCenter)
        self.t0_offset_value.setReadOnly(False)
        self.t0_offset_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t0_offset_value.setDecimals(1)
        self.t0_offset_value.setMaximum(999.000000000000000)
        self.t0_offset_value.setValue(0.000000000000000)

        self.horizontalLayout_338.addWidget(self.t0_offset_value)


        self.horizontalLayout_337.addWidget(self.widget_267)

        self.stacked_cel_fah_temp_t0_5 = QStackedWidget(self.widget_266)
        self.stacked_cel_fah_temp_t0_5.setObjectName(u"stacked_cel_fah_temp_t0_5")
        self.celsius_t0_5 = QWidget()
        self.celsius_t0_5.setObjectName(u"celsius_t0_5")
        self.horizontalLayout_464 = QHBoxLayout(self.celsius_t0_5)
        self.horizontalLayout_464.setObjectName(u"horizontalLayout_464")
        self.horizontalLayout_464.setContentsMargins(0, 0, 0, 0)
        self.label_364 = QLabel(self.celsius_t0_5)
        self.label_364.setObjectName(u"label_364")
        self.label_364.setFont(font17)
        self.label_364.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_364.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_464.addWidget(self.label_364)

        self.stacked_cel_fah_temp_t0_5.addWidget(self.celsius_t0_5)
        self.fahrenheit_t0_5 = QWidget()
        self.fahrenheit_t0_5.setObjectName(u"fahrenheit_t0_5")
        self.horizontalLayout_465 = QHBoxLayout(self.fahrenheit_t0_5)
        self.horizontalLayout_465.setObjectName(u"horizontalLayout_465")
        self.horizontalLayout_465.setContentsMargins(0, 0, 0, 0)
        self.label_365 = QLabel(self.fahrenheit_t0_5)
        self.label_365.setObjectName(u"label_365")
        self.label_365.setFont(font17)
        self.label_365.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_365.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_465.addWidget(self.label_365)

        self.stacked_cel_fah_temp_t0_5.addWidget(self.fahrenheit_t0_5)

        self.horizontalLayout_337.addWidget(self.stacked_cel_fah_temp_t0_5)

        self.horizontalLayout_337.setStretch(0, 3)
        self.horizontalLayout_337.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_266, 7, 3, 2, 1)

        self.widget_207 = QWidget(self.widget_77)
        self.widget_207.setObjectName(u"widget_207")
        self.horizontalLayout_296 = QHBoxLayout(self.widget_207)
        self.horizontalLayout_296.setSpacing(3)
        self.horizontalLayout_296.setObjectName(u"horizontalLayout_296")
        self.horizontalLayout_296.setContentsMargins(10, 0, 10, 0)
        self.widget_202 = QWidget(self.widget_207)
        self.widget_202.setObjectName(u"widget_202")
        self.widget_202.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_302 = QHBoxLayout(self.widget_202)
        self.horizontalLayout_302.setObjectName(u"horizontalLayout_302")
        self.horizontalLayout_302.setContentsMargins(2, 2, 2, 2)
        self.t0_l_alm_value = QDoubleSpinBox(self.widget_202)
        self.t0_l_alm_value.setObjectName(u"t0_l_alm_value")
        sizePolicy.setHeightForWidth(self.t0_l_alm_value.sizePolicy().hasHeightForWidth())
        self.t0_l_alm_value.setSizePolicy(sizePolicy)
        self.t0_l_alm_value.setFont(font16)
        self.t0_l_alm_value.setStyleSheet(u"")
        self.t0_l_alm_value.setWrapping(False)
        self.t0_l_alm_value.setAlignment(Qt.AlignCenter)
        self.t0_l_alm_value.setReadOnly(False)
        self.t0_l_alm_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t0_l_alm_value.setDecimals(1)
        self.t0_l_alm_value.setMaximum(999.000000000000000)
        self.t0_l_alm_value.setValue(0.000000000000000)

        self.horizontalLayout_302.addWidget(self.t0_l_alm_value)


        self.horizontalLayout_296.addWidget(self.widget_202)

        self.stacked_cel_fah_temp_t0_4 = QStackedWidget(self.widget_207)
        self.stacked_cel_fah_temp_t0_4.setObjectName(u"stacked_cel_fah_temp_t0_4")
        self.celsius_t0_4 = QWidget()
        self.celsius_t0_4.setObjectName(u"celsius_t0_4")
        self.horizontalLayout_462 = QHBoxLayout(self.celsius_t0_4)
        self.horizontalLayout_462.setObjectName(u"horizontalLayout_462")
        self.horizontalLayout_462.setContentsMargins(0, 0, 0, 0)
        self.label_259 = QLabel(self.celsius_t0_4)
        self.label_259.setObjectName(u"label_259")
        self.label_259.setFont(font17)
        self.label_259.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_259.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_462.addWidget(self.label_259)

        self.stacked_cel_fah_temp_t0_4.addWidget(self.celsius_t0_4)
        self.fahrenheit_t0_4 = QWidget()
        self.fahrenheit_t0_4.setObjectName(u"fahrenheit_t0_4")
        self.horizontalLayout_463 = QHBoxLayout(self.fahrenheit_t0_4)
        self.horizontalLayout_463.setObjectName(u"horizontalLayout_463")
        self.horizontalLayout_463.setContentsMargins(0, 0, 0, 0)
        self.label_260 = QLabel(self.fahrenheit_t0_4)
        self.label_260.setObjectName(u"label_260")
        self.label_260.setFont(font17)
        self.label_260.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_260.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_463.addWidget(self.label_260)

        self.stacked_cel_fah_temp_t0_4.addWidget(self.fahrenheit_t0_4)

        self.horizontalLayout_296.addWidget(self.stacked_cel_fah_temp_t0_4)

        self.horizontalLayout_296.setStretch(0, 3)
        self.horizontalLayout_296.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_207, 5, 3, 1, 1)

        self.widget_185 = QWidget(self.widget_77)
        self.widget_185.setObjectName(u"widget_185")
        self.horizontalLayout_163 = QHBoxLayout(self.widget_185)
        self.horizontalLayout_163.setSpacing(3)
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.horizontalLayout_163.setContentsMargins(10, 0, 10, 0)
        self.widget_172 = QWidget(self.widget_185)
        self.widget_172.setObjectName(u"widget_172")
        self.widget_172.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_285 = QHBoxLayout(self.widget_172)
        self.horizontalLayout_285.setObjectName(u"horizontalLayout_285")
        self.horizontalLayout_285.setContentsMargins(2, 2, 2, 2)
        self.t0_pv = QDoubleSpinBox(self.widget_172)
        self.t0_pv.setObjectName(u"t0_pv")
        sizePolicy.setHeightForWidth(self.t0_pv.sizePolicy().hasHeightForWidth())
        self.t0_pv.setSizePolicy(sizePolicy)
        self.t0_pv.setFont(font16)
        self.t0_pv.setStyleSheet(u"")
        self.t0_pv.setWrapping(True)
        self.t0_pv.setAlignment(Qt.AlignCenter)
        self.t0_pv.setReadOnly(True)
        self.t0_pv.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t0_pv.setDecimals(1)
        self.t0_pv.setMaximum(999.000000000000000)
        self.t0_pv.setValue(0.000000000000000)

        self.horizontalLayout_285.addWidget(self.t0_pv)


        self.horizontalLayout_163.addWidget(self.widget_172)

        self.stacked_cel_fah_temp_t0_1 = QStackedWidget(self.widget_185)
        self.stacked_cel_fah_temp_t0_1.setObjectName(u"stacked_cel_fah_temp_t0_1")
        self.celsius_t0_1 = QWidget()
        self.celsius_t0_1.setObjectName(u"celsius_t0_1")
        self.horizontalLayout_456 = QHBoxLayout(self.celsius_t0_1)
        self.horizontalLayout_456.setObjectName(u"horizontalLayout_456")
        self.horizontalLayout_456.setContentsMargins(0, 0, 0, 0)
        self.label_249 = QLabel(self.celsius_t0_1)
        self.label_249.setObjectName(u"label_249")
        self.label_249.setFont(font17)
        self.label_249.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_249.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_456.addWidget(self.label_249)

        self.stacked_cel_fah_temp_t0_1.addWidget(self.celsius_t0_1)
        self.fahrenheit_t0_1 = QWidget()
        self.fahrenheit_t0_1.setObjectName(u"fahrenheit_t0_1")
        self.horizontalLayout_457 = QHBoxLayout(self.fahrenheit_t0_1)
        self.horizontalLayout_457.setObjectName(u"horizontalLayout_457")
        self.horizontalLayout_457.setContentsMargins(0, 0, 0, 0)
        self.label_250 = QLabel(self.fahrenheit_t0_1)
        self.label_250.setObjectName(u"label_250")
        self.label_250.setFont(font17)
        self.label_250.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_250.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_457.addWidget(self.label_250)

        self.stacked_cel_fah_temp_t0_1.addWidget(self.fahrenheit_t0_1)

        self.horizontalLayout_163.addWidget(self.stacked_cel_fah_temp_t0_1)

        self.horizontalLayout_163.setStretch(0, 3)
        self.horizontalLayout_163.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_185, 1, 3, 1, 1)

        self.widget_193 = QWidget(self.widget_77)
        self.widget_193.setObjectName(u"widget_193")
        self.horizontalLayout_182 = QHBoxLayout(self.widget_193)
        self.horizontalLayout_182.setSpacing(3)
        self.horizontalLayout_182.setObjectName(u"horizontalLayout_182")
        self.horizontalLayout_182.setContentsMargins(10, 0, 10, 0)
        self.widget_174 = QWidget(self.widget_193)
        self.widget_174.setObjectName(u"widget_174")
        self.widget_174.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_286 = QHBoxLayout(self.widget_174)
        self.horizontalLayout_286.setObjectName(u"horizontalLayout_286")
        self.horizontalLayout_286.setContentsMargins(2, 2, 2, 2)
        self.t0_sv = QDoubleSpinBox(self.widget_174)
        self.t0_sv.setObjectName(u"t0_sv")
        sizePolicy.setHeightForWidth(self.t0_sv.sizePolicy().hasHeightForWidth())
        self.t0_sv.setSizePolicy(sizePolicy)
        self.t0_sv.setFont(font16)
        self.t0_sv.setStyleSheet(u"")
        self.t0_sv.setWrapping(False)
        self.t0_sv.setAlignment(Qt.AlignCenter)
        self.t0_sv.setReadOnly(False)
        self.t0_sv.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t0_sv.setDecimals(1)
        self.t0_sv.setMaximum(999.000000000000000)
        self.t0_sv.setValue(0.000000000000000)

        self.horizontalLayout_286.addWidget(self.t0_sv)


        self.horizontalLayout_182.addWidget(self.widget_174)

        self.stacked_cel_fah_temp_t0_2 = QStackedWidget(self.widget_193)
        self.stacked_cel_fah_temp_t0_2.setObjectName(u"stacked_cel_fah_temp_t0_2")
        self.celsius_t0_2 = QWidget()
        self.celsius_t0_2.setObjectName(u"celsius_t0_2")
        self.horizontalLayout_458 = QHBoxLayout(self.celsius_t0_2)
        self.horizontalLayout_458.setObjectName(u"horizontalLayout_458")
        self.horizontalLayout_458.setContentsMargins(0, 0, 0, 0)
        self.label_251 = QLabel(self.celsius_t0_2)
        self.label_251.setObjectName(u"label_251")
        self.label_251.setFont(font17)
        self.label_251.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_251.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_458.addWidget(self.label_251)

        self.stacked_cel_fah_temp_t0_2.addWidget(self.celsius_t0_2)
        self.fahrenheit_t0_2 = QWidget()
        self.fahrenheit_t0_2.setObjectName(u"fahrenheit_t0_2")
        self.horizontalLayout_459 = QHBoxLayout(self.fahrenheit_t0_2)
        self.horizontalLayout_459.setObjectName(u"horizontalLayout_459")
        self.horizontalLayout_459.setContentsMargins(0, 0, 0, 0)
        self.label_252 = QLabel(self.fahrenheit_t0_2)
        self.label_252.setObjectName(u"label_252")
        self.label_252.setFont(font17)
        self.label_252.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_252.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_459.addWidget(self.label_252)

        self.stacked_cel_fah_temp_t0_2.addWidget(self.fahrenheit_t0_2)

        self.horizontalLayout_182.addWidget(self.stacked_cel_fah_temp_t0_2)

        self.horizontalLayout_182.setStretch(0, 3)
        self.horizontalLayout_182.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_193, 2, 3, 1, 1)

        self.widget_195 = QWidget(self.widget_77)
        self.widget_195.setObjectName(u"widget_195")
        self.horizontalLayout_184 = QHBoxLayout(self.widget_195)
        self.horizontalLayout_184.setSpacing(3)
        self.horizontalLayout_184.setObjectName(u"horizontalLayout_184")
        self.horizontalLayout_184.setContentsMargins(10, 0, 10, 0)
        self.widget_186 = QWidget(self.widget_195)
        self.widget_186.setObjectName(u"widget_186")
        self.widget_186.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_287 = QHBoxLayout(self.widget_186)
        self.horizontalLayout_287.setObjectName(u"horizontalLayout_287")
        self.horizontalLayout_287.setContentsMargins(2, 2, 2, 2)
        self.t0_h_alm_value = QDoubleSpinBox(self.widget_186)
        self.t0_h_alm_value.setObjectName(u"t0_h_alm_value")
        sizePolicy.setHeightForWidth(self.t0_h_alm_value.sizePolicy().hasHeightForWidth())
        self.t0_h_alm_value.setSizePolicy(sizePolicy)
        self.t0_h_alm_value.setFont(font16)
        self.t0_h_alm_value.setStyleSheet(u"")
        self.t0_h_alm_value.setWrapping(False)
        self.t0_h_alm_value.setAlignment(Qt.AlignCenter)
        self.t0_h_alm_value.setReadOnly(False)
        self.t0_h_alm_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t0_h_alm_value.setDecimals(1)
        self.t0_h_alm_value.setMaximum(999.000000000000000)
        self.t0_h_alm_value.setValue(0.000000000000000)

        self.horizontalLayout_287.addWidget(self.t0_h_alm_value)


        self.horizontalLayout_184.addWidget(self.widget_186)

        self.stacked_cel_fah_temp_t0_3 = QStackedWidget(self.widget_195)
        self.stacked_cel_fah_temp_t0_3.setObjectName(u"stacked_cel_fah_temp_t0_3")
        self.celsius_t0_3 = QWidget()
        self.celsius_t0_3.setObjectName(u"celsius_t0_3")
        self.horizontalLayout_460 = QHBoxLayout(self.celsius_t0_3)
        self.horizontalLayout_460.setObjectName(u"horizontalLayout_460")
        self.horizontalLayout_460.setContentsMargins(0, 0, 0, 0)
        self.label_257 = QLabel(self.celsius_t0_3)
        self.label_257.setObjectName(u"label_257")
        self.label_257.setFont(font17)
        self.label_257.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_257.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_460.addWidget(self.label_257)

        self.stacked_cel_fah_temp_t0_3.addWidget(self.celsius_t0_3)
        self.fahrenheit_t0_3 = QWidget()
        self.fahrenheit_t0_3.setObjectName(u"fahrenheit_t0_3")
        self.horizontalLayout_461 = QHBoxLayout(self.fahrenheit_t0_3)
        self.horizontalLayout_461.setObjectName(u"horizontalLayout_461")
        self.horizontalLayout_461.setContentsMargins(0, 0, 0, 0)
        self.label_258 = QLabel(self.fahrenheit_t0_3)
        self.label_258.setObjectName(u"label_258")
        self.label_258.setFont(font17)
        self.label_258.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_258.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_461.addWidget(self.label_258)

        self.stacked_cel_fah_temp_t0_3.addWidget(self.fahrenheit_t0_3)

        self.horizontalLayout_184.addWidget(self.stacked_cel_fah_temp_t0_3)

        self.horizontalLayout_184.setStretch(0, 3)
        self.horizontalLayout_184.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_195, 4, 3, 1, 1)

        self.widget_246 = QWidget(self.widget_77)
        self.widget_246.setObjectName(u"widget_246")
        self.horizontalLayout_311 = QHBoxLayout(self.widget_246)
        self.horizontalLayout_311.setSpacing(3)
        self.horizontalLayout_311.setObjectName(u"horizontalLayout_311")
        self.horizontalLayout_311.setContentsMargins(10, 0, 10, 0)
        self.widget_247 = QWidget(self.widget_246)
        self.widget_247.setObjectName(u"widget_247")
        self.widget_247.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_319 = QHBoxLayout(self.widget_247)
        self.horizontalLayout_319.setObjectName(u"horizontalLayout_319")
        self.horizontalLayout_319.setContentsMargins(2, 2, 2, 2)
        self.at_t1_offset_value = QDoubleSpinBox(self.widget_247)
        self.at_t1_offset_value.setObjectName(u"at_t1_offset_value")
        sizePolicy.setHeightForWidth(self.at_t1_offset_value.sizePolicy().hasHeightForWidth())
        self.at_t1_offset_value.setSizePolicy(sizePolicy)
        self.at_t1_offset_value.setFont(font16)
        self.at_t1_offset_value.setStyleSheet(u"")
        self.at_t1_offset_value.setWrapping(False)
        self.at_t1_offset_value.setAlignment(Qt.AlignCenter)
        self.at_t1_offset_value.setReadOnly(False)
        self.at_t1_offset_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.at_t1_offset_value.setDecimals(1)
        self.at_t1_offset_value.setMaximum(999.000000000000000)
        self.at_t1_offset_value.setValue(0.000000000000000)

        self.horizontalLayout_319.addWidget(self.at_t1_offset_value)


        self.horizontalLayout_311.addWidget(self.widget_247)

        self.stacked_cel_fah_temp_a_5 = QStackedWidget(self.widget_246)
        self.stacked_cel_fah_temp_a_5.setObjectName(u"stacked_cel_fah_temp_a_5")
        self.celsius_at_18 = QWidget()
        self.celsius_at_18.setObjectName(u"celsius_at_18")
        self.horizontalLayout_414 = QHBoxLayout(self.celsius_at_18)
        self.horizontalLayout_414.setObjectName(u"horizontalLayout_414")
        self.horizontalLayout_414.setContentsMargins(0, 0, 0, 0)
        self.label_328 = QLabel(self.celsius_at_18)
        self.label_328.setObjectName(u"label_328")
        self.label_328.setFont(font17)
        self.label_328.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_328.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_414.addWidget(self.label_328)

        self.stacked_cel_fah_temp_a_5.addWidget(self.celsius_at_18)
        self.fahrenheit_at_18 = QWidget()
        self.fahrenheit_at_18.setObjectName(u"fahrenheit_at_18")
        self.horizontalLayout_415 = QHBoxLayout(self.fahrenheit_at_18)
        self.horizontalLayout_415.setObjectName(u"horizontalLayout_415")
        self.horizontalLayout_415.setContentsMargins(0, 0, 0, 0)
        self.label_329 = QLabel(self.fahrenheit_at_18)
        self.label_329.setObjectName(u"label_329")
        self.label_329.setFont(font17)
        self.label_329.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_329.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_415.addWidget(self.label_329)

        self.stacked_cel_fah_temp_a_5.addWidget(self.fahrenheit_at_18)

        self.horizontalLayout_311.addWidget(self.stacked_cel_fah_temp_a_5)

        self.horizontalLayout_311.setStretch(0, 3)
        self.horizontalLayout_311.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_246, 7, 5, 1, 1)

        self.widget_244 = QWidget(self.widget_77)
        self.widget_244.setObjectName(u"widget_244")
        self.horizontalLayout_309 = QHBoxLayout(self.widget_244)
        self.horizontalLayout_309.setSpacing(3)
        self.horizontalLayout_309.setObjectName(u"horizontalLayout_309")
        self.horizontalLayout_309.setContentsMargins(10, 0, 10, 0)
        self.widget_245 = QWidget(self.widget_244)
        self.widget_245.setObjectName(u"widget_245")
        self.widget_245.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_310 = QHBoxLayout(self.widget_245)
        self.horizontalLayout_310.setObjectName(u"horizontalLayout_310")
        self.horizontalLayout_310.setContentsMargins(2, 2, 2, 2)
        self.at_t2_offset_value = QDoubleSpinBox(self.widget_245)
        self.at_t2_offset_value.setObjectName(u"at_t2_offset_value")
        sizePolicy.setHeightForWidth(self.at_t2_offset_value.sizePolicy().hasHeightForWidth())
        self.at_t2_offset_value.setSizePolicy(sizePolicy)
        self.at_t2_offset_value.setFont(font16)
        self.at_t2_offset_value.setStyleSheet(u"")
        self.at_t2_offset_value.setWrapping(False)
        self.at_t2_offset_value.setAlignment(Qt.AlignCenter)
        self.at_t2_offset_value.setReadOnly(False)
        self.at_t2_offset_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.at_t2_offset_value.setDecimals(1)
        self.at_t2_offset_value.setMaximum(999.000000000000000)
        self.at_t2_offset_value.setValue(0.000000000000000)

        self.horizontalLayout_310.addWidget(self.at_t2_offset_value)


        self.horizontalLayout_309.addWidget(self.widget_245)

        self.stacked_cel_fah_temp_a_6 = QStackedWidget(self.widget_244)
        self.stacked_cel_fah_temp_a_6.setObjectName(u"stacked_cel_fah_temp_a_6")
        self.celsius_at_19 = QWidget()
        self.celsius_at_19.setObjectName(u"celsius_at_19")
        self.horizontalLayout_416 = QHBoxLayout(self.celsius_at_19)
        self.horizontalLayout_416.setObjectName(u"horizontalLayout_416")
        self.horizontalLayout_416.setContentsMargins(0, 0, 0, 0)
        self.label_330 = QLabel(self.celsius_at_19)
        self.label_330.setObjectName(u"label_330")
        self.label_330.setFont(font17)
        self.label_330.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_330.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_416.addWidget(self.label_330)

        self.stacked_cel_fah_temp_a_6.addWidget(self.celsius_at_19)
        self.fahrenheit_at_19 = QWidget()
        self.fahrenheit_at_19.setObjectName(u"fahrenheit_at_19")
        self.horizontalLayout_417 = QHBoxLayout(self.fahrenheit_at_19)
        self.horizontalLayout_417.setObjectName(u"horizontalLayout_417")
        self.horizontalLayout_417.setContentsMargins(0, 0, 0, 0)
        self.label_331 = QLabel(self.fahrenheit_at_19)
        self.label_331.setObjectName(u"label_331")
        self.label_331.setFont(font17)
        self.label_331.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_331.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_417.addWidget(self.label_331)

        self.stacked_cel_fah_temp_a_6.addWidget(self.fahrenheit_at_19)

        self.horizontalLayout_309.addWidget(self.stacked_cel_fah_temp_a_6)

        self.horizontalLayout_309.setStretch(0, 3)
        self.horizontalLayout_309.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_244, 8, 5, 1, 1)

        self.label_133 = QLabel(self.widget_77)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setFont(font11)
        self.label_133.setStyleSheet(u"\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #e3e6ee\n"
"            );")
        self.label_133.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_133, 7, 1, 1, 1)

        self.label_134 = QLabel(self.widget_77)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setFont(font11)
        self.label_134.setStyleSheet(u"\n"
"	background: qlineargradient(\n"
"                x1:0, y1:0,\n"
"                x2:1, y2:0,\n"
"                stop:0 #f8f9fc,\n"
"                stop:1 #e3e6ee\n"
"            );")
        self.label_134.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_134, 9, 1, 1, 1)

        self.widget_18 = QWidget(self.widget_77)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B7EC8;\n"
"    color: white;\n"
"    border: none;\n"
"	padding: 5px;\n"
"    border-radius: 6px;\n"
"	padding-left:10px;\n"
"	padding-right:10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0968A3;\n"
"}\n"
"QPushButton:pressed {\n"
"	color: white;\n"
"    background-color: #085A91;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #EF4444;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_33.setSpacing(10)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(10, 0, 10, 0)
        self.heat_btn_t0 = QPushButton(self.widget_18)
        self.heat_btn_t0.setObjectName(u"heat_btn_t0")
        sizePolicy.setHeightForWidth(self.heat_btn_t0.sizePolicy().hasHeightForWidth())
        self.heat_btn_t0.setSizePolicy(sizePolicy)
        self.heat_btn_t0.setMaximumSize(QSize(16777215, 150))
        self.heat_btn_t0.setFont(font12)
        self.heat_btn_t0.setStyleSheet(u"")
        self.heat_btn_t0.setIcon(icon16)
        self.heat_btn_t0.setIconSize(QSize(35, 35))
        self.heat_btn_t0.setCheckable(True)

        self.horizontalLayout_33.addWidget(self.heat_btn_t0)


        self.gridLayout_3.addWidget(self.widget_18, 9, 3, 1, 1)


        self.verticalLayout_56.addWidget(self.widget_77)


        self.verticalLayout_8.addWidget(self.widget_temperature)

        self.verticalLayout_8.setStretch(0, 8)
        self.stackedWidget.addWidget(self.temperature_page)

        self.verticalLayout_12.addWidget(self.stackedWidget)

        self.stackedWidget_2.addWidget(self.temp_press_page)
        self.device_page = QWidget()
        self.device_page.setObjectName(u"device_page")
        self.verticalLayout_5 = QVBoxLayout(self.device_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.ver_layout_device = QVBoxLayout()
        self.ver_layout_device.setObjectName(u"ver_layout_device")
        self.stackedWidget_3 = QStackedWidget(self.device_page)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.connection_page = QWidget()
        self.connection_page.setObjectName(u"connection_page")
        self.verticalLayout_27 = QVBoxLayout(self.connection_page)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.device_frame = QFrame(self.connection_page)
        self.device_frame.setObjectName(u"device_frame")
        self.device_frame.setMinimumSize(QSize(0, 800))
        self.device_frame.setStyleSheet(u"QFrame {\n"
"    background-color: white;\n"
"    border-radius: 12px;\n"
"    border: 1px solid #E5E5E5;\n"
"}\n"
"QFrame:hover {\n"
"    border: 1px solid #0B7EC8;\n"
"}")
        self.device_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_24 = QVBoxLayout(self.device_frame)
        self.verticalLayout_24.setSpacing(10)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 15, 0, 5)
        self.connection_status_layout = QHBoxLayout()
        self.connection_status_layout.setSpacing(0)
        self.connection_status_layout.setObjectName(u"connection_status_layout")
        self.connection_status_layout.setContentsMargins(5, 5, 5, 5)
        self.plc_io_btn = QPushButton(self.device_frame)
        self.plc_io_btn.setObjectName(u"plc_io_btn")
        sizePolicy.setHeightForWidth(self.plc_io_btn.sizePolicy().hasHeightForWidth())
        self.plc_io_btn.setSizePolicy(sizePolicy)
        self.plc_io_btn.setMinimumSize(QSize(0, 300))
        self.plc_io_btn.setStyleSheet(u"font-size: 24px; \n"
"color: #0B7EC8;\n"
"border: none;\n"
"image:url(:/Icons/Image_20260416155332_127_10.png)")

        self.connection_status_layout.addWidget(self.plc_io_btn)


        self.verticalLayout_24.addLayout(self.connection_status_layout)

        self.widget_15 = QWidget(self.device_frame)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.widget_15)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 10, 10, 5)
        self.connection_group = QGroupBox(self.widget_15)
        self.connection_group.setObjectName(u"connection_group")
        font19 = QFont()
        font19.setFamilies([u"Segoe UI"])
        font19.setPointSize(15)
        font19.setBold(True)
        self.connection_group.setFont(font19)
        self.connection_group.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #E5E5E5;\n"
"    border-radius: 6px;\n"
"    margin-top: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 5px 0 5px;\n"
"    color: #374151;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: black;\n"
"	border: none;\n"
"}\n"
"\n"
"QSpinBox {\n"
"	color: black;\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    background-color: #F9FAFB;\n"
"}\n"
"QSpinBox:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"    background-color: white;\n"
"}\n"
"QDoubleSpinBox {\n"
"	color: black;\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    background-color: #F9FAFB;\n"
"}\n"
"QDoubleSpinBox:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"    background-color: white;\n"
"}\n"
"QLineEdit {\n"
"	color: black;\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    background-color: #F9"
                        "FAFB;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"    background-color: white;\n"
"}")
        self.gridLayout_4 = QGridLayout(self.connection_group)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_31 = QWidget(self.connection_group)
        self.widget_31.setObjectName(u"widget_31")
        self.horizontalLayout_41 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_41.setSpacing(10)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.sys_state_stacked_wid_42 = QStackedWidget(self.widget_31)
        self.sys_state_stacked_wid_42.setObjectName(u"sys_state_stacked_wid_42")
        sizePolicy.setHeightForWidth(self.sys_state_stacked_wid_42.sizePolicy().hasHeightForWidth())
        self.sys_state_stacked_wid_42.setSizePolicy(sizePolicy)
        self.sys_state_stacked_wid_42.setStyleSheet(u"")
        self.running_light_34 = QWidget()
        self.running_light_34.setObjectName(u"running_light_34")
        self.horizontalLayout_473 = QHBoxLayout(self.running_light_34)
        self.horizontalLayout_473.setObjectName(u"horizontalLayout_473")
        self.horizontalLayout_473.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.running_light_34)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        font20 = QFont()
        font20.setPointSize(18)
        font20.setBold(True)
        self.pushButton_6.setFont(font20)
        self.pushButton_6.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #10B981; \n"
"padding-right: 3px;")
        self.pushButton_6.setIcon(icon8)
        self.pushButton_6.setIconSize(QSize(30, 30))

        self.horizontalLayout_473.addWidget(self.pushButton_6)

        self.sys_state_stacked_wid_42.addWidget(self.running_light_34)
        self.error_light_34 = QWidget()
        self.error_light_34.setObjectName(u"error_light_34")
        self.horizontalLayout_474 = QHBoxLayout(self.error_light_34)
        self.horizontalLayout_474.setObjectName(u"horizontalLayout_474")
        self.horizontalLayout_474.setContentsMargins(0, 0, 0, 0)
        self.pushButton_23 = QPushButton(self.error_light_34)
        self.pushButton_23.setObjectName(u"pushButton_23")
        sizePolicy.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy)
        self.pushButton_23.setFont(font20)
        self.pushButton_23.setStyleSheet(u"QPushButton{	\n"
"	border: 2px solid #E5E5E5; \n"
"	border-radius: 10px;\n"
"	color: #F90A0A; \n"
"	padding-right: 3px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #E5E5E5; \n"
"	border-radius: 10px;\n"
"}")
        self.pushButton_23.setIcon(icon7)
        self.pushButton_23.setIconSize(QSize(30, 30))

        self.horizontalLayout_474.addWidget(self.pushButton_23)

        self.sys_state_stacked_wid_42.addWidget(self.error_light_34)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_8 = QHBoxLayout(self.page_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_22 = QPushButton(self.page_3)
        self.pushButton_22.setObjectName(u"pushButton_22")
        sizePolicy.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy)
        self.pushButton_22.setFont(font20)
        self.pushButton_22.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: orange; \n"
"padding-right: 3px;")
        icon19 = QIcon()
        icon19.addFile(u":/Icons/record-button (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_22.setIcon(icon19)
        self.pushButton_22.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.pushButton_22)

        self.sys_state_stacked_wid_42.addWidget(self.page_3)

        self.horizontalLayout_41.addWidget(self.sys_state_stacked_wid_42)

        self.write_time_input = QSpinBox(self.widget_31)
        self.write_time_input.setObjectName(u"write_time_input")
        sizePolicy.setHeightForWidth(self.write_time_input.sizePolicy().hasHeightForWidth())
        self.write_time_input.setSizePolicy(sizePolicy)
        self.write_time_input.setMinimumSize(QSize(0, 0))
        font21 = QFont()
        font21.setPointSize(21)
        font21.setBold(True)
        self.write_time_input.setFont(font21)
        self.write_time_input.setAlignment(Qt.AlignCenter)
        self.write_time_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.write_time_input.setMinimum(300)
        self.write_time_input.setMaximum(1000)
        self.write_time_input.setValue(500)

        self.horizontalLayout_41.addWidget(self.write_time_input)

        self.horizontalLayout_41.setStretch(0, 1)
        self.horizontalLayout_41.setStretch(1, 2)

        self.gridLayout_4.addWidget(self.widget_31, 1, 2, 1, 2)

        self.widget_28 = QWidget(self.connection_group)
        self.widget_28.setObjectName(u"widget_28")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_31.setSpacing(10)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.sys_state_stacked_wid_40 = QStackedWidget(self.widget_28)
        self.sys_state_stacked_wid_40.setObjectName(u"sys_state_stacked_wid_40")
        sizePolicy.setHeightForWidth(self.sys_state_stacked_wid_40.sizePolicy().hasHeightForWidth())
        self.sys_state_stacked_wid_40.setSizePolicy(sizePolicy)
        self.sys_state_stacked_wid_40.setStyleSheet(u"")
        self.running_light_32 = QWidget()
        self.running_light_32.setObjectName(u"running_light_32")
        self.running_light_32.setStyleSheet(u"")
        self.horizontalLayout_328 = QHBoxLayout(self.running_light_32)
        self.horizontalLayout_328.setObjectName(u"horizontalLayout_328")
        self.horizontalLayout_328.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.running_light_32)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setFont(font20)
        self.pushButton_4.setStyleSheet(u"QPushButton{	\n"
"	border: 2px solid #E5E5E5; \n"
"	border-radius: 10px;\n"
"	color: #10B981; \n"
"	padding-right: 3px;\n"
"}\n"
"QPushButton:hover {\n"
"	none;\n"
"}")
        self.pushButton_4.setIcon(icon8)
        self.pushButton_4.setIconSize(QSize(30, 30))

        self.horizontalLayout_328.addWidget(self.pushButton_4)

        self.sys_state_stacked_wid_40.addWidget(self.running_light_32)
        self.error_light_32 = QWidget()
        self.error_light_32.setObjectName(u"error_light_32")
        self.horizontalLayout_339 = QHBoxLayout(self.error_light_32)
        self.horizontalLayout_339.setObjectName(u"horizontalLayout_339")
        self.horizontalLayout_339.setContentsMargins(0, 0, 0, 0)
        self.pushButton_21 = QPushButton(self.error_light_32)
        self.pushButton_21.setObjectName(u"pushButton_21")
        sizePolicy.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)
        self.pushButton_21.setFont(font20)
        self.pushButton_21.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #F90A0A; \n"
"padding-right: 3px;")
        self.pushButton_21.setIcon(icon7)
        self.pushButton_21.setIconSize(QSize(30, 30))

        self.horizontalLayout_339.addWidget(self.pushButton_21)

        self.sys_state_stacked_wid_40.addWidget(self.error_light_32)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_7 = QHBoxLayout(self.page_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_24 = QPushButton(self.page_4)
        self.pushButton_24.setObjectName(u"pushButton_24")
        sizePolicy.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy)
        self.pushButton_24.setFont(font20)
        self.pushButton_24.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: orange; \n"
"padding-right: 3px;")
        self.pushButton_24.setIcon(icon19)
        self.pushButton_24.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.pushButton_24)

        self.sys_state_stacked_wid_40.addWidget(self.page_4)

        self.horizontalLayout_31.addWidget(self.sys_state_stacked_wid_40)

        self.read_time_input = QSpinBox(self.widget_28)
        self.read_time_input.setObjectName(u"read_time_input")
        sizePolicy.setHeightForWidth(self.read_time_input.sizePolicy().hasHeightForWidth())
        self.read_time_input.setSizePolicy(sizePolicy)
        self.read_time_input.setMinimumSize(QSize(0, 0))
        self.read_time_input.setFont(font21)
        self.read_time_input.setAlignment(Qt.AlignCenter)
        self.read_time_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.read_time_input.setMinimum(100)
        self.read_time_input.setMaximum(1000)
        self.read_time_input.setValue(500)

        self.horizontalLayout_31.addWidget(self.read_time_input)

        self.horizontalLayout_31.setStretch(0, 1)
        self.horizontalLayout_31.setStretch(1, 2)

        self.gridLayout_4.addWidget(self.widget_28, 0, 2, 1, 2)

        self.total_cycle_label_2 = QPushButton(self.connection_group)
        self.total_cycle_label_2.setObjectName(u"total_cycle_label_2")
        sizePolicy.setHeightForWidth(self.total_cycle_label_2.sizePolicy().hasHeightForWidth())
        self.total_cycle_label_2.setSizePolicy(sizePolicy)
        font22 = QFont()
        font22.setFamilies([u"MS Shell Dlg 2"])
        font22.setPointSize(19)
        font22.setBold(True)
        self.total_cycle_label_2.setFont(font22)
        self.total_cycle_label_2.setStyleSheet(u"QPushButton {\n"
"    color: rgb(251, 140, 0);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: left;\n"
"}")
        self.total_cycle_label_2.setIconSize(QSize(55, 55))
        self.total_cycle_label_2.setCheckable(True)

        self.gridLayout_4.addWidget(self.total_cycle_label_2, 4, 0, 1, 1)

        self.total_cycle_label = QPushButton(self.connection_group)
        self.total_cycle_label.setObjectName(u"total_cycle_label")
        sizePolicy.setHeightForWidth(self.total_cycle_label.sizePolicy().hasHeightForWidth())
        self.total_cycle_label.setSizePolicy(sizePolicy)
        self.total_cycle_label.setFont(font22)
        self.total_cycle_label.setStyleSheet(u"QPushButton {\n"
"    color: rgb(30, 136, 229);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: left;\n"
"}")
        self.total_cycle_label.setIconSize(QSize(55, 55))
        self.total_cycle_label.setCheckable(True)

        self.gridLayout_4.addWidget(self.total_cycle_label, 3, 0, 1, 1)

        self.total_cycle_label_3 = QPushButton(self.connection_group)
        self.total_cycle_label_3.setObjectName(u"total_cycle_label_3")
        sizePolicy.setHeightForWidth(self.total_cycle_label_3.sizePolicy().hasHeightForWidth())
        self.total_cycle_label_3.setSizePolicy(sizePolicy)
        self.total_cycle_label_3.setFont(font22)
        self.total_cycle_label_3.setStyleSheet(u"QPushButton {\n"
"    color: #6F00FF;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: left;\n"
"}")
        self.total_cycle_label_3.setIconSize(QSize(55, 55))
        self.total_cycle_label_3.setCheckable(True)

        self.gridLayout_4.addWidget(self.total_cycle_label_3, 5, 0, 1, 1)

        self.read_plc_label = QPushButton(self.connection_group)
        self.read_plc_label.setObjectName(u"read_plc_label")
        sizePolicy.setHeightForWidth(self.read_plc_label.sizePolicy().hasHeightForWidth())
        self.read_plc_label.setSizePolicy(sizePolicy)
        self.read_plc_label.setFont(font22)
        self.read_plc_label.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: left;\n"
"}")
        self.read_plc_label.setIconSize(QSize(55, 55))
        self.read_plc_label.setCheckable(True)

        self.gridLayout_4.addWidget(self.read_plc_label, 0, 0, 1, 1)

        self.write_table_label = QPushButton(self.connection_group)
        self.write_table_label.setObjectName(u"write_table_label")
        sizePolicy.setHeightForWidth(self.write_table_label.sizePolicy().hasHeightForWidth())
        self.write_table_label.setSizePolicy(sizePolicy)
        self.write_table_label.setFont(font22)
        self.write_table_label.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: left;\n"
"}")
        icon20 = QIcon()
        icon20.addFile(u":/Icons/to-do-list.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.write_table_label.setIcon(icon20)
        self.write_table_label.setIconSize(QSize(55, 55))
        self.write_table_label.setCheckable(True)

        self.gridLayout_4.addWidget(self.write_table_label, 2, 0, 1, 1)

        self.write_plc_label = QPushButton(self.connection_group)
        self.write_plc_label.setObjectName(u"write_plc_label")
        sizePolicy.setHeightForWidth(self.write_plc_label.sizePolicy().hasHeightForWidth())
        self.write_plc_label.setSizePolicy(sizePolicy)
        self.write_plc_label.setFont(font22)
        self.write_plc_label.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: left;\n"
"}")
        self.write_plc_label.setIconSize(QSize(55, 55))
        self.write_plc_label.setCheckable(True)

        self.gridLayout_4.addWidget(self.write_plc_label, 1, 0, 1, 1)

        self.table_write_cycle = QDoubleSpinBox(self.connection_group)
        self.table_write_cycle.setObjectName(u"table_write_cycle")
        sizePolicy.setHeightForWidth(self.table_write_cycle.sizePolicy().hasHeightForWidth())
        self.table_write_cycle.setSizePolicy(sizePolicy)
        self.table_write_cycle.setMinimumSize(QSize(0, 0))
        self.table_write_cycle.setFont(font21)
        self.table_write_cycle.setAlignment(Qt.AlignCenter)
        self.table_write_cycle.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.table_write_cycle.setDecimals(1)
        self.table_write_cycle.setValue(1.000000000000000)

        self.gridLayout_4.addWidget(self.table_write_cycle, 2, 2, 1, 1)

        self.widget_36 = QWidget(self.connection_group)
        self.widget_36.setObjectName(u"widget_36")
        self.widget_36.setStyleSheet(u"QSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget\n"
"{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.horizontalLayout_46 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_46.setSpacing(10)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.cycle_b_displ_3 = QSpinBox(self.widget_36)
        self.cycle_b_displ_3.setObjectName(u"cycle_b_displ_3")
        sizePolicy.setHeightForWidth(self.cycle_b_displ_3.sizePolicy().hasHeightForWidth())
        self.cycle_b_displ_3.setSizePolicy(sizePolicy)
        font23 = QFont()
        font23.setFamilies([u"Segoe UI"])
        font23.setPointSize(21)
        font23.setBold(True)
        font23.setItalic(False)
        self.cycle_b_displ_3.setFont(font23)
        self.cycle_b_displ_3.setStyleSheet(u"color: rgb(251, 140, 0);\n"
"padding-left: 20px;")
        self.cycle_b_displ_3.setWrapping(True)
        self.cycle_b_displ_3.setFrame(False)
        self.cycle_b_displ_3.setAlignment(Qt.AlignCenter)
        self.cycle_b_displ_3.setReadOnly(True)
        self.cycle_b_displ_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.cycle_b_displ_3.setMaximum(9999999)
        self.cycle_b_displ_3.setValue(0)
        self.cycle_b_displ_3.setDisplayIntegerBase(10)

        self.horizontalLayout_46.addWidget(self.cycle_b_displ_3)

        self.reset_cycle_b_btn = QPushButton(self.widget_36)
        self.reset_cycle_b_btn.setObjectName(u"reset_cycle_b_btn")
        sizePolicy.setHeightForWidth(self.reset_cycle_b_btn.sizePolicy().hasHeightForWidth())
        self.reset_cycle_b_btn.setSizePolicy(sizePolicy)
        self.reset_cycle_b_btn.setMinimumSize(QSize(75, 0))
        self.reset_cycle_b_btn.setFont(font12)
        self.reset_cycle_b_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #0B7EC8;\n"
"    border: 1px solid #0B7EC8;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #F0F9FF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #E0F2FE;\n"
"}")
        icon21 = QIcon()
        icon21.addFile(u":/Icons/broom.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.reset_cycle_b_btn.setIcon(icon21)
        self.reset_cycle_b_btn.setIconSize(QSize(50, 50))

        self.horizontalLayout_46.addWidget(self.reset_cycle_b_btn)


        self.gridLayout_4.addWidget(self.widget_36, 4, 2, 1, 2)

        self.widget_35 = QWidget(self.connection_group)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setStyleSheet(u"QSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget\n"
"{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.horizontalLayout_44 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_44.setSpacing(10)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.cycle_a_displ_3 = QSpinBox(self.widget_35)
        self.cycle_a_displ_3.setObjectName(u"cycle_a_displ_3")
        sizePolicy.setHeightForWidth(self.cycle_a_displ_3.sizePolicy().hasHeightForWidth())
        self.cycle_a_displ_3.setSizePolicy(sizePolicy)
        self.cycle_a_displ_3.setFont(font23)
        self.cycle_a_displ_3.setStyleSheet(u"color: rgb(30, 136, 229);\n"
"padding-left: 20px;")
        self.cycle_a_displ_3.setWrapping(True)
        self.cycle_a_displ_3.setFrame(False)
        self.cycle_a_displ_3.setAlignment(Qt.AlignCenter)
        self.cycle_a_displ_3.setReadOnly(True)
        self.cycle_a_displ_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.cycle_a_displ_3.setMaximum(9999999)
        self.cycle_a_displ_3.setValue(0)

        self.horizontalLayout_44.addWidget(self.cycle_a_displ_3)

        self.reset_cycle_a_btn = QPushButton(self.widget_35)
        self.reset_cycle_a_btn.setObjectName(u"reset_cycle_a_btn")
        sizePolicy.setHeightForWidth(self.reset_cycle_a_btn.sizePolicy().hasHeightForWidth())
        self.reset_cycle_a_btn.setSizePolicy(sizePolicy)
        self.reset_cycle_a_btn.setMinimumSize(QSize(75, 0))
        self.reset_cycle_a_btn.setFont(font12)
        self.reset_cycle_a_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #0B7EC8;\n"
"    border: 1px solid #0B7EC8;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #F0F9FF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #E0F2FE;\n"
"}")
        self.reset_cycle_a_btn.setIcon(icon21)
        self.reset_cycle_a_btn.setIconSize(QSize(50, 50))

        self.horizontalLayout_44.addWidget(self.reset_cycle_a_btn)


        self.gridLayout_4.addWidget(self.widget_35, 3, 2, 1, 2)

        self.widget_37 = QWidget(self.connection_group)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setStyleSheet(u"QSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget\n"
"{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.horizontalLayout_48 = QHBoxLayout(self.widget_37)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.cycle_c_displ_3 = QSpinBox(self.widget_37)
        self.cycle_c_displ_3.setObjectName(u"cycle_c_displ_3")
        sizePolicy.setHeightForWidth(self.cycle_c_displ_3.sizePolicy().hasHeightForWidth())
        self.cycle_c_displ_3.setSizePolicy(sizePolicy)
        self.cycle_c_displ_3.setFont(font23)
        self.cycle_c_displ_3.setStyleSheet(u"color: #6F00FF;\n"
"padding-left: 20px;")
        self.cycle_c_displ_3.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.cycle_c_displ_3.setWrapping(True)
        self.cycle_c_displ_3.setFrame(False)
        self.cycle_c_displ_3.setAlignment(Qt.AlignCenter)
        self.cycle_c_displ_3.setReadOnly(True)
        self.cycle_c_displ_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.cycle_c_displ_3.setMaximum(9999999)
        self.cycle_c_displ_3.setValue(0)
        self.cycle_c_displ_3.setDisplayIntegerBase(10)

        self.horizontalLayout_48.addWidget(self.cycle_c_displ_3)

        self.reset_cycle_c_btn = QPushButton(self.widget_37)
        self.reset_cycle_c_btn.setObjectName(u"reset_cycle_c_btn")
        sizePolicy.setHeightForWidth(self.reset_cycle_c_btn.sizePolicy().hasHeightForWidth())
        self.reset_cycle_c_btn.setSizePolicy(sizePolicy)
        self.reset_cycle_c_btn.setMinimumSize(QSize(75, 0))
        self.reset_cycle_c_btn.setFont(font12)
        self.reset_cycle_c_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #0B7EC8;\n"
"    border: 1px solid #0B7EC8;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #F0F9FF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #E0F2FE;\n"
"}")
        self.reset_cycle_c_btn.setIcon(icon21)
        self.reset_cycle_c_btn.setIconSize(QSize(50, 50))

        self.horizontalLayout_48.addWidget(self.reset_cycle_c_btn)


        self.gridLayout_4.addWidget(self.widget_37, 5, 2, 1, 2)

        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 1)
        self.gridLayout_4.setRowStretch(2, 1)
        self.gridLayout_4.setRowStretch(3, 1)
        self.gridLayout_4.setRowStretch(4, 1)
        self.gridLayout_4.setRowStretch(5, 1)

        self.verticalLayout_9.addWidget(self.connection_group)


        self.verticalLayout_24.addWidget(self.widget_15)

        self.verticalLayout_24.setStretch(0, 4)
        self.verticalLayout_24.setStretch(1, 7)

        self.verticalLayout_27.addWidget(self.device_frame)

        self.stackedWidget_3.addWidget(self.connection_page)
        self.i_o_page = QWidget()
        self.i_o_page.setObjectName(u"i_o_page")
        self.verticalLayout_40 = QVBoxLayout(self.i_o_page)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.device_frame_2 = QFrame(self.i_o_page)
        self.device_frame_2.setObjectName(u"device_frame_2")
        self.device_frame_2.setMinimumSize(QSize(0, 800))
        self.device_frame_2.setStyleSheet(u"QFrame {\n"
"    background-color: white;\n"
"    border-radius: 12px;\n"
"    border: 1px solid #E5E5E5;\n"
"    margin: 5px;\n"
"}\n"
"QFrame:hover {\n"
"    border: 1px solid #0B7EC8;\n"
"}")
        self.device_frame_2.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_28 = QVBoxLayout(self.device_frame_2)
        self.verticalLayout_28.setSpacing(10)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 15, 0, 15)
        self.widget_26 = QWidget(self.device_frame_2)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setStyleSheet(u"")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_24.setSpacing(10)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(10, 0, 10, 0)
        self.i_o_group_1 = QGroupBox(self.widget_26)
        self.i_o_group_1.setObjectName(u"i_o_group_1")
        font24 = QFont()
        font24.setFamilies([u"Segoe UI"])
        font24.setPointSize(16)
        font24.setBold(True)
        self.i_o_group_1.setFont(font24)
        self.i_o_group_1.setStyleSheet(u"QWidget{\n"
"	border: 2px solid #E5E5E5; \n"
"	border-radius: 20px;\n"
"}\n"
"QGroupBox {\n"
"    border: 2px solid #E5E5E5;\n"
"    border-radius: 6px;\n"
"    margin-top: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 5px 0 5px;\n"
"    color: #374151;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #D12323;\n"
"	border: none;\n"
"}\n"
"\n"
"QSpinBox {\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    background-color: #F9FAFB;\n"
"}\n"
"QSpinBox:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    background-color: #F9FAFB;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"    background-color: white;\n"
"}")
        self.gridLayout_7 = QGridLayout(self.i_o_group_1)
        self.gridLayout_7.setSpacing(10)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(10, 15, 10, 10)
        self.i_o_group_1_switch_3 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_3.setObjectName(u"i_o_group_1_switch_3")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_3.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_3.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_3.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.off_light_9 = QWidget()
        self.off_light_9.setObjectName(u"off_light_9")
        self.horizontalLayout_487 = QHBoxLayout(self.off_light_9)
        self.horizontalLayout_487.setObjectName(u"horizontalLayout_487")
        self.horizontalLayout_487.setContentsMargins(0, 0, 0, 0)
        self.pushButton_59 = QPushButton(self.off_light_9)
        self.pushButton_59.setObjectName(u"pushButton_59")
        sizePolicy.setHeightForWidth(self.pushButton_59.sizePolicy().hasHeightForWidth())
        self.pushButton_59.setSizePolicy(sizePolicy)
        font25 = QFont()
        font25.setPointSize(15)
        font25.setBold(True)
        self.pushButton_59.setFont(font25)
        self.pushButton_59.setIcon(icon7)
        self.pushButton_59.setIconSize(QSize(45, 45))

        self.horizontalLayout_487.addWidget(self.pushButton_59)

        self.i_o_group_1_switch_3.addWidget(self.off_light_9)
        self.on_light_9 = QWidget()
        self.on_light_9.setObjectName(u"on_light_9")
        self.horizontalLayout_486 = QHBoxLayout(self.on_light_9)
        self.horizontalLayout_486.setObjectName(u"horizontalLayout_486")
        self.horizontalLayout_486.setContentsMargins(0, 0, 0, 0)
        self.pushButton_58 = QPushButton(self.on_light_9)
        self.pushButton_58.setObjectName(u"pushButton_58")
        sizePolicy.setHeightForWidth(self.pushButton_58.sizePolicy().hasHeightForWidth())
        self.pushButton_58.setSizePolicy(sizePolicy)
        self.pushButton_58.setFont(font25)
        self.pushButton_58.setIcon(icon8)
        self.pushButton_58.setIconSize(QSize(45, 45))

        self.horizontalLayout_486.addWidget(self.pushButton_58)

        self.i_o_group_1_switch_3.addWidget(self.on_light_9)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_3, 2, 1, 1, 1)

        self.i_o_group_1_switch_5 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_5.setObjectName(u"i_o_group_1_switch_5")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_5.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_5.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_5.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.off_light_11 = QWidget()
        self.off_light_11.setObjectName(u"off_light_11")
        self.horizontalLayout_491 = QHBoxLayout(self.off_light_11)
        self.horizontalLayout_491.setObjectName(u"horizontalLayout_491")
        self.horizontalLayout_491.setContentsMargins(0, 0, 0, 0)
        self.pushButton_63 = QPushButton(self.off_light_11)
        self.pushButton_63.setObjectName(u"pushButton_63")
        sizePolicy.setHeightForWidth(self.pushButton_63.sizePolicy().hasHeightForWidth())
        self.pushButton_63.setSizePolicy(sizePolicy)
        self.pushButton_63.setFont(font25)
        self.pushButton_63.setIcon(icon7)
        self.pushButton_63.setIconSize(QSize(45, 45))

        self.horizontalLayout_491.addWidget(self.pushButton_63)

        self.i_o_group_1_switch_5.addWidget(self.off_light_11)
        self.on_light_11 = QWidget()
        self.on_light_11.setObjectName(u"on_light_11")
        self.horizontalLayout_490 = QHBoxLayout(self.on_light_11)
        self.horizontalLayout_490.setObjectName(u"horizontalLayout_490")
        self.horizontalLayout_490.setContentsMargins(0, 0, 0, 0)
        self.pushButton_62 = QPushButton(self.on_light_11)
        self.pushButton_62.setObjectName(u"pushButton_62")
        sizePolicy.setHeightForWidth(self.pushButton_62.sizePolicy().hasHeightForWidth())
        self.pushButton_62.setSizePolicy(sizePolicy)
        self.pushButton_62.setFont(font25)
        self.pushButton_62.setIcon(icon8)
        self.pushButton_62.setIconSize(QSize(45, 45))

        self.horizontalLayout_490.addWidget(self.pushButton_62)

        self.i_o_group_1_switch_5.addWidget(self.on_light_11)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_5, 4, 1, 1, 1)

        self.i_o_group_1_switch_6 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_6.setObjectName(u"i_o_group_1_switch_6")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_6.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_6.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_6.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.off_light_12 = QWidget()
        self.off_light_12.setObjectName(u"off_light_12")
        self.horizontalLayout_493 = QHBoxLayout(self.off_light_12)
        self.horizontalLayout_493.setObjectName(u"horizontalLayout_493")
        self.horizontalLayout_493.setContentsMargins(0, 0, 0, 0)
        self.pushButton_65 = QPushButton(self.off_light_12)
        self.pushButton_65.setObjectName(u"pushButton_65")
        sizePolicy.setHeightForWidth(self.pushButton_65.sizePolicy().hasHeightForWidth())
        self.pushButton_65.setSizePolicy(sizePolicy)
        self.pushButton_65.setFont(font25)
        self.pushButton_65.setIcon(icon7)
        self.pushButton_65.setIconSize(QSize(45, 45))

        self.horizontalLayout_493.addWidget(self.pushButton_65)

        self.i_o_group_1_switch_6.addWidget(self.off_light_12)
        self.on_light_12 = QWidget()
        self.on_light_12.setObjectName(u"on_light_12")
        self.horizontalLayout_492 = QHBoxLayout(self.on_light_12)
        self.horizontalLayout_492.setObjectName(u"horizontalLayout_492")
        self.horizontalLayout_492.setContentsMargins(0, 0, 0, 0)
        self.pushButton_64 = QPushButton(self.on_light_12)
        self.pushButton_64.setObjectName(u"pushButton_64")
        sizePolicy.setHeightForWidth(self.pushButton_64.sizePolicy().hasHeightForWidth())
        self.pushButton_64.setSizePolicy(sizePolicy)
        self.pushButton_64.setFont(font25)
        self.pushButton_64.setIcon(icon8)
        self.pushButton_64.setIconSize(QSize(45, 45))

        self.horizontalLayout_492.addWidget(self.pushButton_64)

        self.i_o_group_1_switch_6.addWidget(self.on_light_12)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_6, 5, 1, 1, 1)

        self.i_o_group_1_switch_7 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_7.setObjectName(u"i_o_group_1_switch_7")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_7.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_7.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_7.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.off_light_13 = QWidget()
        self.off_light_13.setObjectName(u"off_light_13")
        self.horizontalLayout_495 = QHBoxLayout(self.off_light_13)
        self.horizontalLayout_495.setObjectName(u"horizontalLayout_495")
        self.horizontalLayout_495.setContentsMargins(0, 0, 0, 0)
        self.pushButton_67 = QPushButton(self.off_light_13)
        self.pushButton_67.setObjectName(u"pushButton_67")
        sizePolicy.setHeightForWidth(self.pushButton_67.sizePolicy().hasHeightForWidth())
        self.pushButton_67.setSizePolicy(sizePolicy)
        self.pushButton_67.setFont(font25)
        self.pushButton_67.setIcon(icon7)
        self.pushButton_67.setIconSize(QSize(45, 45))

        self.horizontalLayout_495.addWidget(self.pushButton_67)

        self.i_o_group_1_switch_7.addWidget(self.off_light_13)
        self.on_light_13 = QWidget()
        self.on_light_13.setObjectName(u"on_light_13")
        self.horizontalLayout_494 = QHBoxLayout(self.on_light_13)
        self.horizontalLayout_494.setObjectName(u"horizontalLayout_494")
        self.horizontalLayout_494.setContentsMargins(0, 0, 0, 0)
        self.pushButton_66 = QPushButton(self.on_light_13)
        self.pushButton_66.setObjectName(u"pushButton_66")
        sizePolicy.setHeightForWidth(self.pushButton_66.sizePolicy().hasHeightForWidth())
        self.pushButton_66.setSizePolicy(sizePolicy)
        self.pushButton_66.setFont(font25)
        self.pushButton_66.setIcon(icon8)
        self.pushButton_66.setIconSize(QSize(45, 45))

        self.horizontalLayout_494.addWidget(self.pushButton_66)

        self.i_o_group_1_switch_7.addWidget(self.on_light_13)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_7, 6, 1, 1, 1)

        self.i_o_group_1_switch_2 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_2.setObjectName(u"i_o_group_1_switch_2")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_2.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_2.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_2.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.off_light_8 = QWidget()
        self.off_light_8.setObjectName(u"off_light_8")
        self.horizontalLayout_485 = QHBoxLayout(self.off_light_8)
        self.horizontalLayout_485.setObjectName(u"horizontalLayout_485")
        self.horizontalLayout_485.setContentsMargins(0, 0, 0, 0)
        self.pushButton_57 = QPushButton(self.off_light_8)
        self.pushButton_57.setObjectName(u"pushButton_57")
        sizePolicy.setHeightForWidth(self.pushButton_57.sizePolicy().hasHeightForWidth())
        self.pushButton_57.setSizePolicy(sizePolicy)
        self.pushButton_57.setFont(font25)
        self.pushButton_57.setIcon(icon7)
        self.pushButton_57.setIconSize(QSize(45, 45))

        self.horizontalLayout_485.addWidget(self.pushButton_57)

        self.i_o_group_1_switch_2.addWidget(self.off_light_8)
        self.on_light_8 = QWidget()
        self.on_light_8.setObjectName(u"on_light_8")
        self.horizontalLayout_484 = QHBoxLayout(self.on_light_8)
        self.horizontalLayout_484.setObjectName(u"horizontalLayout_484")
        self.horizontalLayout_484.setContentsMargins(0, 0, 0, 0)
        self.pushButton_56 = QPushButton(self.on_light_8)
        self.pushButton_56.setObjectName(u"pushButton_56")
        sizePolicy.setHeightForWidth(self.pushButton_56.sizePolicy().hasHeightForWidth())
        self.pushButton_56.setSizePolicy(sizePolicy)
        self.pushButton_56.setFont(font25)
        self.pushButton_56.setIcon(icon8)
        self.pushButton_56.setIconSize(QSize(45, 45))

        self.horizontalLayout_484.addWidget(self.pushButton_56)

        self.i_o_group_1_switch_2.addWidget(self.on_light_8)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_2, 1, 1, 1, 1)

        self.di_name_1 = QLabel(self.i_o_group_1)
        self.di_name_1.setObjectName(u"di_name_1")
        font26 = QFont()
        font26.setPointSize(20)
        font26.setBold(True)
        self.di_name_1.setFont(font26)

        self.gridLayout_7.addWidget(self.di_name_1, 0, 0, 1, 1)

        self.i_o_group_1_switch_1 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_1.setObjectName(u"i_o_group_1_switch_1")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_1.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_1.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_1.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.off_light_1 = QWidget()
        self.off_light_1.setObjectName(u"off_light_1")
        self.horizontalLayout_471 = QHBoxLayout(self.off_light_1)
        self.horizontalLayout_471.setObjectName(u"horizontalLayout_471")
        self.horizontalLayout_471.setContentsMargins(0, 0, 0, 0)
        self.pushButton_43 = QPushButton(self.off_light_1)
        self.pushButton_43.setObjectName(u"pushButton_43")
        sizePolicy.setHeightForWidth(self.pushButton_43.sizePolicy().hasHeightForWidth())
        self.pushButton_43.setSizePolicy(sizePolicy)
        self.pushButton_43.setFont(font25)
        self.pushButton_43.setIcon(icon7)
        self.pushButton_43.setIconSize(QSize(45, 45))

        self.horizontalLayout_471.addWidget(self.pushButton_43)

        self.i_o_group_1_switch_1.addWidget(self.off_light_1)
        self.on_light_1 = QWidget()
        self.on_light_1.setObjectName(u"on_light_1")
        self.horizontalLayout_470 = QHBoxLayout(self.on_light_1)
        self.horizontalLayout_470.setObjectName(u"horizontalLayout_470")
        self.horizontalLayout_470.setContentsMargins(0, 0, 0, 0)
        self.pushButton_42 = QPushButton(self.on_light_1)
        self.pushButton_42.setObjectName(u"pushButton_42")
        sizePolicy.setHeightForWidth(self.pushButton_42.sizePolicy().hasHeightForWidth())
        self.pushButton_42.setSizePolicy(sizePolicy)
        self.pushButton_42.setFont(font25)
        self.pushButton_42.setIcon(icon8)
        self.pushButton_42.setIconSize(QSize(45, 45))

        self.horizontalLayout_470.addWidget(self.pushButton_42)

        self.i_o_group_1_switch_1.addWidget(self.on_light_1)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_1, 0, 1, 1, 1)

        self.i_o_group_1_switch_4 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_4.setObjectName(u"i_o_group_1_switch_4")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_4.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_4.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_4.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.off_light_10 = QWidget()
        self.off_light_10.setObjectName(u"off_light_10")
        self.horizontalLayout_489 = QHBoxLayout(self.off_light_10)
        self.horizontalLayout_489.setObjectName(u"horizontalLayout_489")
        self.horizontalLayout_489.setContentsMargins(0, 0, 0, 0)
        self.pushButton_61 = QPushButton(self.off_light_10)
        self.pushButton_61.setObjectName(u"pushButton_61")
        sizePolicy.setHeightForWidth(self.pushButton_61.sizePolicy().hasHeightForWidth())
        self.pushButton_61.setSizePolicy(sizePolicy)
        self.pushButton_61.setFont(font25)
        self.pushButton_61.setIcon(icon7)
        self.pushButton_61.setIconSize(QSize(45, 45))

        self.horizontalLayout_489.addWidget(self.pushButton_61)

        self.i_o_group_1_switch_4.addWidget(self.off_light_10)
        self.on_light_10 = QWidget()
        self.on_light_10.setObjectName(u"on_light_10")
        self.horizontalLayout_488 = QHBoxLayout(self.on_light_10)
        self.horizontalLayout_488.setObjectName(u"horizontalLayout_488")
        self.horizontalLayout_488.setContentsMargins(0, 0, 0, 0)
        self.pushButton_60 = QPushButton(self.on_light_10)
        self.pushButton_60.setObjectName(u"pushButton_60")
        sizePolicy.setHeightForWidth(self.pushButton_60.sizePolicy().hasHeightForWidth())
        self.pushButton_60.setSizePolicy(sizePolicy)
        self.pushButton_60.setFont(font25)
        self.pushButton_60.setIcon(icon8)
        self.pushButton_60.setIconSize(QSize(45, 45))

        self.horizontalLayout_488.addWidget(self.pushButton_60)

        self.i_o_group_1_switch_4.addWidget(self.on_light_10)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_4, 3, 1, 1, 1)

        self.di_name_2 = QLabel(self.i_o_group_1)
        self.di_name_2.setObjectName(u"di_name_2")
        self.di_name_2.setFont(font26)

        self.gridLayout_7.addWidget(self.di_name_2, 1, 0, 1, 1)

        self.di_name_3 = QLabel(self.i_o_group_1)
        self.di_name_3.setObjectName(u"di_name_3")
        self.di_name_3.setFont(font26)

        self.gridLayout_7.addWidget(self.di_name_3, 2, 0, 1, 1)

        self.i_o_group_1_switch_8 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_8.setObjectName(u"i_o_group_1_switch_8")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_8.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_8.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_8.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.off_light_14 = QWidget()
        self.off_light_14.setObjectName(u"off_light_14")
        self.horizontalLayout_497 = QHBoxLayout(self.off_light_14)
        self.horizontalLayout_497.setObjectName(u"horizontalLayout_497")
        self.horizontalLayout_497.setContentsMargins(0, 0, 0, 0)
        self.pushButton_69 = QPushButton(self.off_light_14)
        self.pushButton_69.setObjectName(u"pushButton_69")
        sizePolicy.setHeightForWidth(self.pushButton_69.sizePolicy().hasHeightForWidth())
        self.pushButton_69.setSizePolicy(sizePolicy)
        self.pushButton_69.setFont(font25)
        self.pushButton_69.setIcon(icon7)
        self.pushButton_69.setIconSize(QSize(45, 45))

        self.horizontalLayout_497.addWidget(self.pushButton_69)

        self.i_o_group_1_switch_8.addWidget(self.off_light_14)
        self.on_light_14 = QWidget()
        self.on_light_14.setObjectName(u"on_light_14")
        self.horizontalLayout_496 = QHBoxLayout(self.on_light_14)
        self.horizontalLayout_496.setObjectName(u"horizontalLayout_496")
        self.horizontalLayout_496.setContentsMargins(0, 0, 0, 0)
        self.pushButton_68 = QPushButton(self.on_light_14)
        self.pushButton_68.setObjectName(u"pushButton_68")
        sizePolicy.setHeightForWidth(self.pushButton_68.sizePolicy().hasHeightForWidth())
        self.pushButton_68.setSizePolicy(sizePolicy)
        self.pushButton_68.setFont(font25)
        self.pushButton_68.setIcon(icon8)
        self.pushButton_68.setIconSize(QSize(45, 45))

        self.horizontalLayout_496.addWidget(self.pushButton_68)

        self.i_o_group_1_switch_8.addWidget(self.on_light_14)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_8, 7, 1, 1, 1)

        self.di_name_4 = QLabel(self.i_o_group_1)
        self.di_name_4.setObjectName(u"di_name_4")
        self.di_name_4.setFont(font26)

        self.gridLayout_7.addWidget(self.di_name_4, 3, 0, 1, 1)

        self.di_name_5 = QLabel(self.i_o_group_1)
        self.di_name_5.setObjectName(u"di_name_5")
        self.di_name_5.setFont(font26)

        self.gridLayout_7.addWidget(self.di_name_5, 4, 0, 1, 1)

        self.di_name_6 = QLabel(self.i_o_group_1)
        self.di_name_6.setObjectName(u"di_name_6")
        self.di_name_6.setFont(font26)

        self.gridLayout_7.addWidget(self.di_name_6, 5, 0, 1, 1)

        self.di_name_7 = QLabel(self.i_o_group_1)
        self.di_name_7.setObjectName(u"di_name_7")
        self.di_name_7.setFont(font26)

        self.gridLayout_7.addWidget(self.di_name_7, 6, 0, 1, 1)

        self.di_name_8 = QLabel(self.i_o_group_1)
        self.di_name_8.setObjectName(u"di_name_8")
        self.di_name_8.setFont(font26)

        self.gridLayout_7.addWidget(self.di_name_8, 7, 0, 1, 1)

        self.di_name_11 = QLabel(self.i_o_group_1)
        self.di_name_11.setObjectName(u"di_name_11")
        self.di_name_11.setFont(font26)

        self.gridLayout_7.addWidget(self.di_name_11, 10, 0, 1, 1)

        self.i_o_group_1_switch_11 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_11.setObjectName(u"i_o_group_1_switch_11")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_11.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_11.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_11.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.off_light_17 = QWidget()
        self.off_light_17.setObjectName(u"off_light_17")
        self.horizontalLayout_590 = QHBoxLayout(self.off_light_17)
        self.horizontalLayout_590.setObjectName(u"horizontalLayout_590")
        self.horizontalLayout_590.setContentsMargins(0, 0, 0, 0)
        self.pushButton_74 = QPushButton(self.off_light_17)
        self.pushButton_74.setObjectName(u"pushButton_74")
        sizePolicy.setHeightForWidth(self.pushButton_74.sizePolicy().hasHeightForWidth())
        self.pushButton_74.setSizePolicy(sizePolicy)
        self.pushButton_74.setFont(font25)
        self.pushButton_74.setIcon(icon7)
        self.pushButton_74.setIconSize(QSize(45, 45))

        self.horizontalLayout_590.addWidget(self.pushButton_74)

        self.i_o_group_1_switch_11.addWidget(self.off_light_17)
        self.on_light_17 = QWidget()
        self.on_light_17.setObjectName(u"on_light_17")
        self.horizontalLayout_591 = QHBoxLayout(self.on_light_17)
        self.horizontalLayout_591.setObjectName(u"horizontalLayout_591")
        self.horizontalLayout_591.setContentsMargins(0, 0, 0, 0)
        self.pushButton_75 = QPushButton(self.on_light_17)
        self.pushButton_75.setObjectName(u"pushButton_75")
        sizePolicy.setHeightForWidth(self.pushButton_75.sizePolicy().hasHeightForWidth())
        self.pushButton_75.setSizePolicy(sizePolicy)
        self.pushButton_75.setFont(font25)
        self.pushButton_75.setIcon(icon8)
        self.pushButton_75.setIconSize(QSize(45, 45))

        self.horizontalLayout_591.addWidget(self.pushButton_75)

        self.i_o_group_1_switch_11.addWidget(self.on_light_17)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_11, 10, 1, 1, 1)

        self.di_name_12 = QLabel(self.i_o_group_1)
        self.di_name_12.setObjectName(u"di_name_12")
        self.di_name_12.setFont(font26)

        self.gridLayout_7.addWidget(self.di_name_12, 11, 0, 1, 1)

        self.di_name_9 = QLabel(self.i_o_group_1)
        self.di_name_9.setObjectName(u"di_name_9")
        self.di_name_9.setFont(font26)

        self.gridLayout_7.addWidget(self.di_name_9, 8, 0, 1, 1)

        self.di_name_10 = QLabel(self.i_o_group_1)
        self.di_name_10.setObjectName(u"di_name_10")
        self.di_name_10.setFont(font26)

        self.gridLayout_7.addWidget(self.di_name_10, 9, 0, 1, 1)

        self.i_o_group_1_switch_9 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_9.setObjectName(u"i_o_group_1_switch_9")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_9.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_9.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_9.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.off_light_15 = QWidget()
        self.off_light_15.setObjectName(u"off_light_15")
        self.horizontalLayout_586 = QHBoxLayout(self.off_light_15)
        self.horizontalLayout_586.setObjectName(u"horizontalLayout_586")
        self.horizontalLayout_586.setContentsMargins(0, 0, 0, 0)
        self.pushButton_70 = QPushButton(self.off_light_15)
        self.pushButton_70.setObjectName(u"pushButton_70")
        sizePolicy.setHeightForWidth(self.pushButton_70.sizePolicy().hasHeightForWidth())
        self.pushButton_70.setSizePolicy(sizePolicy)
        self.pushButton_70.setFont(font25)
        self.pushButton_70.setIcon(icon7)
        self.pushButton_70.setIconSize(QSize(45, 45))

        self.horizontalLayout_586.addWidget(self.pushButton_70)

        self.i_o_group_1_switch_9.addWidget(self.off_light_15)
        self.on_light_15 = QWidget()
        self.on_light_15.setObjectName(u"on_light_15")
        self.horizontalLayout_587 = QHBoxLayout(self.on_light_15)
        self.horizontalLayout_587.setObjectName(u"horizontalLayout_587")
        self.horizontalLayout_587.setContentsMargins(0, 0, 0, 0)
        self.pushButton_71 = QPushButton(self.on_light_15)
        self.pushButton_71.setObjectName(u"pushButton_71")
        sizePolicy.setHeightForWidth(self.pushButton_71.sizePolicy().hasHeightForWidth())
        self.pushButton_71.setSizePolicy(sizePolicy)
        self.pushButton_71.setFont(font25)
        self.pushButton_71.setIcon(icon8)
        self.pushButton_71.setIconSize(QSize(45, 45))

        self.horizontalLayout_587.addWidget(self.pushButton_71)

        self.i_o_group_1_switch_9.addWidget(self.on_light_15)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_9, 8, 1, 1, 1)

        self.i_o_group_1_switch_10 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_10.setObjectName(u"i_o_group_1_switch_10")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_10.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_10.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_10.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.off_light_16 = QWidget()
        self.off_light_16.setObjectName(u"off_light_16")
        self.horizontalLayout_588 = QHBoxLayout(self.off_light_16)
        self.horizontalLayout_588.setObjectName(u"horizontalLayout_588")
        self.horizontalLayout_588.setContentsMargins(0, 0, 0, 0)
        self.pushButton_72 = QPushButton(self.off_light_16)
        self.pushButton_72.setObjectName(u"pushButton_72")
        sizePolicy.setHeightForWidth(self.pushButton_72.sizePolicy().hasHeightForWidth())
        self.pushButton_72.setSizePolicy(sizePolicy)
        self.pushButton_72.setFont(font25)
        self.pushButton_72.setIcon(icon7)
        self.pushButton_72.setIconSize(QSize(45, 45))

        self.horizontalLayout_588.addWidget(self.pushButton_72)

        self.i_o_group_1_switch_10.addWidget(self.off_light_16)
        self.on_light_16 = QWidget()
        self.on_light_16.setObjectName(u"on_light_16")
        self.horizontalLayout_589 = QHBoxLayout(self.on_light_16)
        self.horizontalLayout_589.setObjectName(u"horizontalLayout_589")
        self.horizontalLayout_589.setContentsMargins(0, 0, 0, 0)
        self.pushButton_73 = QPushButton(self.on_light_16)
        self.pushButton_73.setObjectName(u"pushButton_73")
        sizePolicy.setHeightForWidth(self.pushButton_73.sizePolicy().hasHeightForWidth())
        self.pushButton_73.setSizePolicy(sizePolicy)
        self.pushButton_73.setFont(font25)
        self.pushButton_73.setIcon(icon8)
        self.pushButton_73.setIconSize(QSize(45, 45))

        self.horizontalLayout_589.addWidget(self.pushButton_73)

        self.i_o_group_1_switch_10.addWidget(self.on_light_16)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_10, 9, 1, 1, 1)

        self.di_name_13 = QLabel(self.i_o_group_1)
        self.di_name_13.setObjectName(u"di_name_13")
        self.di_name_13.setFont(font26)

        self.gridLayout_7.addWidget(self.di_name_13, 12, 0, 1, 1)

        self.i_o_group_1_switch_12 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_12.setObjectName(u"i_o_group_1_switch_12")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_12.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_12.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_12.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.off_light_18 = QWidget()
        self.off_light_18.setObjectName(u"off_light_18")
        self.horizontalLayout_592 = QHBoxLayout(self.off_light_18)
        self.horizontalLayout_592.setObjectName(u"horizontalLayout_592")
        self.horizontalLayout_592.setContentsMargins(0, 0, 0, 0)
        self.pushButton_76 = QPushButton(self.off_light_18)
        self.pushButton_76.setObjectName(u"pushButton_76")
        sizePolicy.setHeightForWidth(self.pushButton_76.sizePolicy().hasHeightForWidth())
        self.pushButton_76.setSizePolicy(sizePolicy)
        self.pushButton_76.setFont(font25)
        self.pushButton_76.setIcon(icon7)
        self.pushButton_76.setIconSize(QSize(45, 45))

        self.horizontalLayout_592.addWidget(self.pushButton_76)

        self.i_o_group_1_switch_12.addWidget(self.off_light_18)
        self.on_light_18 = QWidget()
        self.on_light_18.setObjectName(u"on_light_18")
        self.horizontalLayout_593 = QHBoxLayout(self.on_light_18)
        self.horizontalLayout_593.setObjectName(u"horizontalLayout_593")
        self.horizontalLayout_593.setContentsMargins(0, 0, 0, 0)
        self.pushButton_77 = QPushButton(self.on_light_18)
        self.pushButton_77.setObjectName(u"pushButton_77")
        sizePolicy.setHeightForWidth(self.pushButton_77.sizePolicy().hasHeightForWidth())
        self.pushButton_77.setSizePolicy(sizePolicy)
        self.pushButton_77.setFont(font25)
        self.pushButton_77.setIcon(icon8)
        self.pushButton_77.setIconSize(QSize(45, 45))

        self.horizontalLayout_593.addWidget(self.pushButton_77)

        self.i_o_group_1_switch_12.addWidget(self.on_light_18)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_12, 11, 1, 1, 1)

        self.i_o_group_1_switch_13 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_13.setObjectName(u"i_o_group_1_switch_13")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_13.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_13.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_13.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.off_light_19 = QWidget()
        self.off_light_19.setObjectName(u"off_light_19")
        self.horizontalLayout_594 = QHBoxLayout(self.off_light_19)
        self.horizontalLayout_594.setObjectName(u"horizontalLayout_594")
        self.horizontalLayout_594.setContentsMargins(0, 0, 0, 0)
        self.pushButton_78 = QPushButton(self.off_light_19)
        self.pushButton_78.setObjectName(u"pushButton_78")
        sizePolicy.setHeightForWidth(self.pushButton_78.sizePolicy().hasHeightForWidth())
        self.pushButton_78.setSizePolicy(sizePolicy)
        self.pushButton_78.setFont(font25)
        self.pushButton_78.setIcon(icon7)
        self.pushButton_78.setIconSize(QSize(45, 45))

        self.horizontalLayout_594.addWidget(self.pushButton_78)

        self.i_o_group_1_switch_13.addWidget(self.off_light_19)
        self.on_light_19 = QWidget()
        self.on_light_19.setObjectName(u"on_light_19")
        self.horizontalLayout_595 = QHBoxLayout(self.on_light_19)
        self.horizontalLayout_595.setObjectName(u"horizontalLayout_595")
        self.horizontalLayout_595.setContentsMargins(0, 0, 0, 0)
        self.pushButton_79 = QPushButton(self.on_light_19)
        self.pushButton_79.setObjectName(u"pushButton_79")
        sizePolicy.setHeightForWidth(self.pushButton_79.sizePolicy().hasHeightForWidth())
        self.pushButton_79.setSizePolicy(sizePolicy)
        self.pushButton_79.setFont(font25)
        self.pushButton_79.setIcon(icon8)
        self.pushButton_79.setIconSize(QSize(45, 45))

        self.horizontalLayout_595.addWidget(self.pushButton_79)

        self.i_o_group_1_switch_13.addWidget(self.on_light_19)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_13, 12, 1, 1, 1)

        self.gridLayout_7.setColumnStretch(1, 1)

        self.horizontalLayout_24.addWidget(self.i_o_group_1)

        self.i_o_group_3 = QGroupBox(self.widget_26)
        self.i_o_group_3.setObjectName(u"i_o_group_3")
        self.i_o_group_3.setFont(font24)
        self.i_o_group_3.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #E5E5E5;\n"
"    border-radius: 6px;\n"
"    margin-top: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 5px 0 5px;\n"
"    color: #374151;\n"
"}\n"
"\n"
"QLabel {\n"
"	border: none;\n"
"	color: #E6AC2E;\n"
"}\n"
"\n"
"QSpinBox {\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    background-color: #F9FAFB;\n"
"}\n"
"QSpinBox:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    background-color: #F9FAFB;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"    background-color: white;\n"
"}")
        self.gridLayout_5 = QGridLayout(self.i_o_group_3)
        self.gridLayout_5.setSpacing(10)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(10, 15, 10, 10)
        self.t0_value = QDoubleSpinBox(self.i_o_group_3)
        self.t0_value.setObjectName(u"t0_value")
        sizePolicy.setHeightForWidth(self.t0_value.sizePolicy().hasHeightForWidth())
        self.t0_value.setSizePolicy(sizePolicy)
        self.t0_value.setFont(font6)
        self.t0_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.t0_value.setAlignment(Qt.AlignCenter)
        self.t0_value.setReadOnly(True)
        self.t0_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t0_value.setDecimals(1)
        self.t0_value.setMinimum(-9999.899999999999636)
        self.t0_value.setMaximum(9999.899999999999636)

        self.gridLayout_5.addWidget(self.t0_value, 0, 1, 1, 1)

        self.ai_name_1 = QLabel(self.i_o_group_3)
        self.ai_name_1.setObjectName(u"ai_name_1")
        self.ai_name_1.setFont(font26)

        self.gridLayout_5.addWidget(self.ai_name_1, 0, 0, 1, 1)

        self.t1_1_value = QDoubleSpinBox(self.i_o_group_3)
        self.t1_1_value.setObjectName(u"t1_1_value")
        sizePolicy.setHeightForWidth(self.t1_1_value.sizePolicy().hasHeightForWidth())
        self.t1_1_value.setSizePolicy(sizePolicy)
        self.t1_1_value.setFont(font6)
        self.t1_1_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.t1_1_value.setAlignment(Qt.AlignCenter)
        self.t1_1_value.setReadOnly(True)
        self.t1_1_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t1_1_value.setDecimals(1)
        self.t1_1_value.setMinimum(-9999.899999999999636)
        self.t1_1_value.setMaximum(9999.899999999999636)

        self.gridLayout_5.addWidget(self.t1_1_value, 0, 3, 1, 1)

        self.ai_name_15 = QLabel(self.i_o_group_3)
        self.ai_name_15.setObjectName(u"ai_name_15")
        self.ai_name_15.setFont(font26)

        self.gridLayout_5.addWidget(self.ai_name_15, 7, 2, 1, 1)

        self.ai_name_14 = QLabel(self.i_o_group_3)
        self.ai_name_14.setObjectName(u"ai_name_14")
        self.ai_name_14.setFont(font26)

        self.gridLayout_5.addWidget(self.ai_name_14, 6, 2, 1, 1)

        self.ai_name_12 = QLabel(self.i_o_group_3)
        self.ai_name_12.setObjectName(u"ai_name_12")
        self.ai_name_12.setFont(font26)

        self.gridLayout_5.addWidget(self.ai_name_12, 7, 0, 1, 1)

        self.ai_name_13 = QLabel(self.i_o_group_3)
        self.ai_name_13.setObjectName(u"ai_name_13")
        self.ai_name_13.setFont(font26)

        self.gridLayout_5.addWidget(self.ai_name_13, 9, 0, 1, 1)

        self.ai_name_16 = QLabel(self.i_o_group_3)
        self.ai_name_16.setObjectName(u"ai_name_16")
        self.ai_name_16.setFont(font26)

        self.gridLayout_5.addWidget(self.ai_name_16, 9, 2, 1, 1)

        self.ai_name_4 = QLabel(self.i_o_group_3)
        self.ai_name_4.setObjectName(u"ai_name_4")
        self.ai_name_4.setFont(font26)

        self.gridLayout_5.addWidget(self.ai_name_4, 1, 2, 1, 1)

        self.ai_name_3 = QLabel(self.i_o_group_3)
        self.ai_name_3.setObjectName(u"ai_name_3")
        self.ai_name_3.setFont(font26)

        self.gridLayout_5.addWidget(self.ai_name_3, 1, 0, 1, 1)

        self.ai_name_5 = QLabel(self.i_o_group_3)
        self.ai_name_5.setObjectName(u"ai_name_5")
        self.ai_name_5.setFont(font26)

        self.gridLayout_5.addWidget(self.ai_name_5, 2, 0, 1, 1)

        self.ai_name_2 = QLabel(self.i_o_group_3)
        self.ai_name_2.setObjectName(u"ai_name_2")
        self.ai_name_2.setFont(font26)

        self.gridLayout_5.addWidget(self.ai_name_2, 0, 2, 1, 1)

        self.ai_name_6 = QLabel(self.i_o_group_3)
        self.ai_name_6.setObjectName(u"ai_name_6")
        self.ai_name_6.setFont(font26)

        self.gridLayout_5.addWidget(self.ai_name_6, 2, 2, 1, 1)

        self.ai_name_7 = QLabel(self.i_o_group_3)
        self.ai_name_7.setObjectName(u"ai_name_7")
        self.ai_name_7.setFont(font26)

        self.gridLayout_5.addWidget(self.ai_name_7, 3, 0, 1, 1)

        self.ai_name_8 = QLabel(self.i_o_group_3)
        self.ai_name_8.setObjectName(u"ai_name_8")
        self.ai_name_8.setFont(font26)

        self.gridLayout_5.addWidget(self.ai_name_8, 3, 2, 1, 1)

        self.ai_name_9 = QLabel(self.i_o_group_3)
        self.ai_name_9.setObjectName(u"ai_name_9")
        self.ai_name_9.setFont(font26)

        self.gridLayout_5.addWidget(self.ai_name_9, 4, 0, 1, 1)

        self.ai_name_10 = QLabel(self.i_o_group_3)
        self.ai_name_10.setObjectName(u"ai_name_10")
        self.ai_name_10.setFont(font26)

        self.gridLayout_5.addWidget(self.ai_name_10, 4, 2, 1, 1)

        self.ai_name_11 = QLabel(self.i_o_group_3)
        self.ai_name_11.setObjectName(u"ai_name_11")
        self.ai_name_11.setFont(font26)

        self.gridLayout_5.addWidget(self.ai_name_11, 6, 0, 1, 1)

        self.t1_2_value = QDoubleSpinBox(self.i_o_group_3)
        self.t1_2_value.setObjectName(u"t1_2_value")
        sizePolicy.setHeightForWidth(self.t1_2_value.sizePolicy().hasHeightForWidth())
        self.t1_2_value.setSizePolicy(sizePolicy)
        self.t1_2_value.setFont(font6)
        self.t1_2_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.t1_2_value.setAlignment(Qt.AlignCenter)
        self.t1_2_value.setReadOnly(True)
        self.t1_2_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t1_2_value.setDecimals(1)
        self.t1_2_value.setMinimum(-9999.899999999999636)
        self.t1_2_value.setMaximum(9999.899999999999636)

        self.gridLayout_5.addWidget(self.t1_2_value, 1, 1, 1, 1)

        self.t1_3_value = QDoubleSpinBox(self.i_o_group_3)
        self.t1_3_value.setObjectName(u"t1_3_value")
        sizePolicy.setHeightForWidth(self.t1_3_value.sizePolicy().hasHeightForWidth())
        self.t1_3_value.setSizePolicy(sizePolicy)
        self.t1_3_value.setFont(font6)
        self.t1_3_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.t1_3_value.setAlignment(Qt.AlignCenter)
        self.t1_3_value.setReadOnly(True)
        self.t1_3_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t1_3_value.setDecimals(1)
        self.t1_3_value.setMinimum(-9999.899999999999636)
        self.t1_3_value.setMaximum(9999.899999999999636)

        self.gridLayout_5.addWidget(self.t1_3_value, 1, 3, 1, 1)

        self.t2_1_value = QDoubleSpinBox(self.i_o_group_3)
        self.t2_1_value.setObjectName(u"t2_1_value")
        sizePolicy.setHeightForWidth(self.t2_1_value.sizePolicy().hasHeightForWidth())
        self.t2_1_value.setSizePolicy(sizePolicy)
        self.t2_1_value.setFont(font6)
        self.t2_1_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.t2_1_value.setAlignment(Qt.AlignCenter)
        self.t2_1_value.setReadOnly(True)
        self.t2_1_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t2_1_value.setDecimals(1)
        self.t2_1_value.setMinimum(-9999.899999999999636)
        self.t2_1_value.setMaximum(9999.899999999999636)

        self.gridLayout_5.addWidget(self.t2_1_value, 2, 1, 1, 1)

        self.t2_2_value = QDoubleSpinBox(self.i_o_group_3)
        self.t2_2_value.setObjectName(u"t2_2_value")
        sizePolicy.setHeightForWidth(self.t2_2_value.sizePolicy().hasHeightForWidth())
        self.t2_2_value.setSizePolicy(sizePolicy)
        self.t2_2_value.setFont(font6)
        self.t2_2_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.t2_2_value.setAlignment(Qt.AlignCenter)
        self.t2_2_value.setReadOnly(True)
        self.t2_2_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t2_2_value.setDecimals(1)
        self.t2_2_value.setMinimum(-9999.899999999999636)
        self.t2_2_value.setMaximum(9999.899999999999636)

        self.gridLayout_5.addWidget(self.t2_2_value, 2, 3, 1, 1)

        self.t2_3_value = QDoubleSpinBox(self.i_o_group_3)
        self.t2_3_value.setObjectName(u"t2_3_value")
        sizePolicy.setHeightForWidth(self.t2_3_value.sizePolicy().hasHeightForWidth())
        self.t2_3_value.setSizePolicy(sizePolicy)
        self.t2_3_value.setFont(font6)
        self.t2_3_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.t2_3_value.setAlignment(Qt.AlignCenter)
        self.t2_3_value.setReadOnly(True)
        self.t2_3_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t2_3_value.setDecimals(1)
        self.t2_3_value.setMinimum(-9999.899999999999636)
        self.t2_3_value.setMaximum(9999.899999999999636)

        self.gridLayout_5.addWidget(self.t2_3_value, 3, 1, 1, 1)

        self.t3_1_value = QDoubleSpinBox(self.i_o_group_3)
        self.t3_1_value.setObjectName(u"t3_1_value")
        sizePolicy.setHeightForWidth(self.t3_1_value.sizePolicy().hasHeightForWidth())
        self.t3_1_value.setSizePolicy(sizePolicy)
        self.t3_1_value.setFont(font6)
        self.t3_1_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.t3_1_value.setAlignment(Qt.AlignCenter)
        self.t3_1_value.setReadOnly(True)
        self.t3_1_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t3_1_value.setDecimals(1)
        self.t3_1_value.setMinimum(-9999.899999999999636)
        self.t3_1_value.setMaximum(9999.899999999999636)

        self.gridLayout_5.addWidget(self.t3_1_value, 3, 3, 1, 1)

        self.t3_2_value = QDoubleSpinBox(self.i_o_group_3)
        self.t3_2_value.setObjectName(u"t3_2_value")
        sizePolicy.setHeightForWidth(self.t3_2_value.sizePolicy().hasHeightForWidth())
        self.t3_2_value.setSizePolicy(sizePolicy)
        self.t3_2_value.setFont(font6)
        self.t3_2_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.t3_2_value.setAlignment(Qt.AlignCenter)
        self.t3_2_value.setReadOnly(True)
        self.t3_2_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t3_2_value.setDecimals(1)
        self.t3_2_value.setMinimum(-9999.899999999999636)
        self.t3_2_value.setMaximum(9999.899999999999636)

        self.gridLayout_5.addWidget(self.t3_2_value, 4, 1, 1, 1)

        self.t3_3_value = QDoubleSpinBox(self.i_o_group_3)
        self.t3_3_value.setObjectName(u"t3_3_value")
        sizePolicy.setHeightForWidth(self.t3_3_value.sizePolicy().hasHeightForWidth())
        self.t3_3_value.setSizePolicy(sizePolicy)
        self.t3_3_value.setFont(font6)
        self.t3_3_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.t3_3_value.setAlignment(Qt.AlignCenter)
        self.t3_3_value.setReadOnly(True)
        self.t3_3_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t3_3_value.setDecimals(1)
        self.t3_3_value.setMinimum(-9999.899999999999636)
        self.t3_3_value.setMaximum(9999.899999999999636)

        self.gridLayout_5.addWidget(self.t3_3_value, 4, 3, 1, 1)

        self.p1_value = QDoubleSpinBox(self.i_o_group_3)
        self.p1_value.setObjectName(u"p1_value")
        sizePolicy.setHeightForWidth(self.p1_value.sizePolicy().hasHeightForWidth())
        self.p1_value.setSizePolicy(sizePolicy)
        self.p1_value.setFont(font6)
        self.p1_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.p1_value.setAlignment(Qt.AlignCenter)
        self.p1_value.setReadOnly(True)
        self.p1_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.p1_value.setDecimals(1)
        self.p1_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.p1_value, 6, 1, 1, 1)

        self.p2_value = QDoubleSpinBox(self.i_o_group_3)
        self.p2_value.setObjectName(u"p2_value")
        sizePolicy.setHeightForWidth(self.p2_value.sizePolicy().hasHeightForWidth())
        self.p2_value.setSizePolicy(sizePolicy)
        self.p2_value.setFont(font6)
        self.p2_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.p2_value.setAlignment(Qt.AlignCenter)
        self.p2_value.setReadOnly(True)
        self.p2_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.p2_value.setDecimals(1)
        self.p2_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.p2_value, 7, 1, 1, 1)

        self.p3_value = QDoubleSpinBox(self.i_o_group_3)
        self.p3_value.setObjectName(u"p3_value")
        sizePolicy.setHeightForWidth(self.p3_value.sizePolicy().hasHeightForWidth())
        self.p3_value.setSizePolicy(sizePolicy)
        self.p3_value.setFont(font6)
        self.p3_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.p3_value.setAlignment(Qt.AlignCenter)
        self.p3_value.setReadOnly(True)
        self.p3_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.p3_value.setDecimals(1)
        self.p3_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.p3_value, 9, 1, 1, 1)

        self.fp1_value = QDoubleSpinBox(self.i_o_group_3)
        self.fp1_value.setObjectName(u"fp1_value")
        sizePolicy.setHeightForWidth(self.fp1_value.sizePolicy().hasHeightForWidth())
        self.fp1_value.setSizePolicy(sizePolicy)
        self.fp1_value.setFont(font6)
        self.fp1_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.fp1_value.setAlignment(Qt.AlignCenter)
        self.fp1_value.setReadOnly(True)
        self.fp1_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.fp1_value.setDecimals(1)
        self.fp1_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.fp1_value, 6, 3, 1, 1)

        self.fp2_value = QDoubleSpinBox(self.i_o_group_3)
        self.fp2_value.setObjectName(u"fp2_value")
        sizePolicy.setHeightForWidth(self.fp2_value.sizePolicy().hasHeightForWidth())
        self.fp2_value.setSizePolicy(sizePolicy)
        self.fp2_value.setFont(font6)
        self.fp2_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.fp2_value.setAlignment(Qt.AlignCenter)
        self.fp2_value.setReadOnly(True)
        self.fp2_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.fp2_value.setDecimals(1)
        self.fp2_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.fp2_value, 7, 3, 1, 1)

        self.fp3_value = QDoubleSpinBox(self.i_o_group_3)
        self.fp3_value.setObjectName(u"fp3_value")
        sizePolicy.setHeightForWidth(self.fp3_value.sizePolicy().hasHeightForWidth())
        self.fp3_value.setSizePolicy(sizePolicy)
        self.fp3_value.setFont(font6)
        self.fp3_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.fp3_value.setAlignment(Qt.AlignCenter)
        self.fp3_value.setReadOnly(True)
        self.fp3_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.fp3_value.setDecimals(1)
        self.fp3_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.fp3_value, 9, 3, 1, 1)

        self.gridLayout_5.setColumnStretch(1, 1)
        self.gridLayout_5.setColumnStretch(3, 1)

        self.horizontalLayout_24.addWidget(self.i_o_group_3)

        self.i_o_group_2 = QGroupBox(self.widget_26)
        self.i_o_group_2.setObjectName(u"i_o_group_2")
        self.i_o_group_2.setFont(font24)
        self.i_o_group_2.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #E5E5E5;\n"
"    border-radius: 6px;\n"
"    margin-top: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 5px 0 5px;\n"
"    color: #374151;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #D12323;\n"
"	border: none;\n"
"}\n"
"\n"
"QSpinBox {\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    background-color: #F9FAFB;\n"
"}\n"
"QSpinBox:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    background-color: #F9FAFB;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"    background-color: white;\n"
"}")
        self.gridLayout_6 = QGridLayout(self.i_o_group_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.db_file_path = QPushButton(self.i_o_group_2)
        self.db_file_path.setObjectName(u"db_file_path")
        sizePolicy.setHeightForWidth(self.db_file_path.sizePolicy().hasHeightForWidth())
        self.db_file_path.setSizePolicy(sizePolicy)
        self.db_file_path.setFont(font22)
        self.db_file_path.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: left;\n"
"}")
        icon22 = QIcon()
        icon22.addFile(u":/Icons/search (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.db_file_path.setIcon(icon22)
        self.db_file_path.setIconSize(QSize(55, 55))
        self.db_file_path.setCheckable(True)

        self.gridLayout_6.addWidget(self.db_file_path, 0, 0, 1, 1)

        self.db_file_path_edit = QLineEdit(self.i_o_group_2)
        self.db_file_path_edit.setObjectName(u"db_file_path_edit")
        sizePolicy.setHeightForWidth(self.db_file_path_edit.sizePolicy().hasHeightForWidth())
        self.db_file_path_edit.setSizePolicy(sizePolicy)
        font27 = QFont()
        font27.setPointSize(19)
        font27.setBold(True)
        self.db_file_path_edit.setFont(font27)
        self.db_file_path_edit.setPlaceholderText(u"Enter Path Folder")

        self.gridLayout_6.addWidget(self.db_file_path_edit, 0, 1, 1, 1)

        self.ip_plc_address = QPushButton(self.i_o_group_2)
        self.ip_plc_address.setObjectName(u"ip_plc_address")
        sizePolicy.setHeightForWidth(self.ip_plc_address.sizePolicy().hasHeightForWidth())
        self.ip_plc_address.setSizePolicy(sizePolicy)
        self.ip_plc_address.setFont(font22)
        self.ip_plc_address.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: left;\n"
"}")
        icon23 = QIcon()
        icon23.addFile(u":/Icons/ip-address.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ip_plc_address.setIcon(icon23)
        self.ip_plc_address.setIconSize(QSize(55, 55))
        self.ip_plc_address.setCheckable(True)

        self.gridLayout_6.addWidget(self.ip_plc_address, 1, 0, 1, 1)

        self.plc_ip_address_edit = QLineEdit(self.i_o_group_2)
        self.plc_ip_address_edit.setObjectName(u"plc_ip_address_edit")
        sizePolicy.setHeightForWidth(self.plc_ip_address_edit.sizePolicy().hasHeightForWidth())
        self.plc_ip_address_edit.setSizePolicy(sizePolicy)
        self.plc_ip_address_edit.setFont(font27)
        self.plc_ip_address_edit.setPlaceholderText(u"Enter IP Address: 172.16.100.***")

        self.gridLayout_6.addWidget(self.plc_ip_address_edit, 1, 1, 1, 1)

        self.db_number = QPushButton(self.i_o_group_2)
        self.db_number.setObjectName(u"db_number")
        sizePolicy.setHeightForWidth(self.db_number.sizePolicy().hasHeightForWidth())
        self.db_number.setSizePolicy(sizePolicy)
        self.db_number.setFont(font22)
        self.db_number.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: left;\n"
"}")
        icon24 = QIcon()
        icon24.addFile(u":/Icons/server-setting.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.db_number.setIcon(icon24)
        self.db_number.setIconSize(QSize(55, 55))
        self.db_number.setCheckable(True)

        self.gridLayout_6.addWidget(self.db_number, 2, 0, 1, 1)

        self.db_number_input = QSpinBox(self.i_o_group_2)
        self.db_number_input.setObjectName(u"db_number_input")
        sizePolicy.setHeightForWidth(self.db_number_input.sizePolicy().hasHeightForWidth())
        self.db_number_input.setSizePolicy(sizePolicy)
        self.db_number_input.setMinimumSize(QSize(0, 0))
        self.db_number_input.setFont(font27)
        self.db_number_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_number_input.setSpecialValueText(u"")
        self.db_number_input.setValue(1)

        self.gridLayout_6.addWidget(self.db_number_input, 2, 1, 1, 1)

        self.write_plc_label_2 = QPushButton(self.i_o_group_2)
        self.write_plc_label_2.setObjectName(u"write_plc_label_2")
        sizePolicy.setHeightForWidth(self.write_plc_label_2.sizePolicy().hasHeightForWidth())
        self.write_plc_label_2.setSizePolicy(sizePolicy)
        self.write_plc_label_2.setFont(font22)
        self.write_plc_label_2.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: left;\n"
"}")
        icon25 = QIcon()
        icon25.addFile(u":/Icons/security.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.write_plc_label_2.setIcon(icon25)
        self.write_plc_label_2.setIconSize(QSize(55, 55))
        self.write_plc_label_2.setCheckable(True)

        self.gridLayout_6.addWidget(self.write_plc_label_2, 3, 0, 1, 1)

        self.db_data_size_input = QSpinBox(self.i_o_group_2)
        self.db_data_size_input.setObjectName(u"db_data_size_input")
        sizePolicy.setHeightForWidth(self.db_data_size_input.sizePolicy().hasHeightForWidth())
        self.db_data_size_input.setSizePolicy(sizePolicy)
        self.db_data_size_input.setMinimumSize(QSize(0, 0))
        self.db_data_size_input.setFont(font27)
        self.db_data_size_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_data_size_input.setMaximum(1024)
        self.db_data_size_input.setValue(0)

        self.gridLayout_6.addWidget(self.db_data_size_input, 3, 1, 1, 1)


        self.horizontalLayout_24.addWidget(self.i_o_group_2)

        self.horizontalLayout_24.setStretch(0, 1)
        self.horizontalLayout_24.setStretch(1, 2)
        self.horizontalLayout_24.setStretch(2, 2)

        self.verticalLayout_28.addWidget(self.widget_26)

        self.widget_29 = QWidget(self.device_frame_2)
        self.widget_29.setObjectName(u"widget_29")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_27.setSpacing(10)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.widget_30 = QWidget(self.widget_29)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setMaximumSize(QSize(16777215, 16777215))
        self.widget_30.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #0B7EC8;\n"
"    border: 2px solid #0B7EC8;\n"
"    padding: 4px 4px;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #F0F9FF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #E0F2FE;\n"
"}")
        self.horizontalLayout_30 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_30.setSpacing(10)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(10, 0, 10, 0)
        self.back_connection_page_btn = QPushButton(self.widget_30)
        self.back_connection_page_btn.setObjectName(u"back_connection_page_btn")
        sizePolicy.setHeightForWidth(self.back_connection_page_btn.sizePolicy().hasHeightForWidth())
        self.back_connection_page_btn.setSizePolicy(sizePolicy)
        self.back_connection_page_btn.setMaximumSize(QSize(16777215, 16777215))
        self.back_connection_page_btn.setFont(font26)
        self.back_connection_page_btn.setStyleSheet(u"")
        self.back_connection_page_btn.setIconSize(QSize(40, 40))
        self.back_connection_page_btn.setCheckable(False)

        self.horizontalLayout_30.addWidget(self.back_connection_page_btn)

        self.back_home_page_btn = QPushButton(self.widget_30)
        self.back_home_page_btn.setObjectName(u"back_home_page_btn")
        sizePolicy.setHeightForWidth(self.back_home_page_btn.sizePolicy().hasHeightForWidth())
        self.back_home_page_btn.setSizePolicy(sizePolicy)
        self.back_home_page_btn.setMaximumSize(QSize(16777215, 16777215))
        self.back_home_page_btn.setFont(font26)
        self.back_home_page_btn.setStyleSheet(u"")
        self.back_home_page_btn.setIconSize(QSize(40, 40))
        self.back_home_page_btn.setCheckable(False)

        self.horizontalLayout_30.addWidget(self.back_home_page_btn)

        self.horizontalLayout_30.setStretch(0, 1)
        self.horizontalLayout_30.setStretch(1, 1)

        self.horizontalLayout_27.addWidget(self.widget_30)


        self.verticalLayout_28.addWidget(self.widget_29)

        self.verticalLayout_28.setStretch(0, 15)
        self.verticalLayout_28.setStretch(1, 1)

        self.verticalLayout_40.addWidget(self.device_frame_2)

        self.stackedWidget_3.addWidget(self.i_o_page)

        self.ver_layout_device.addWidget(self.stackedWidget_3)


        self.verticalLayout_5.addLayout(self.ver_layout_device)

        self.stackedWidget_2.addWidget(self.device_page)
        self.history_page = QWidget()
        self.history_page.setObjectName(u"history_page")
        self.verticalLayout_13 = QVBoxLayout(self.history_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.dashboard_stacked_widget = QWidget(self.history_page)
        self.dashboard_stacked_widget.setObjectName(u"dashboard_stacked_widget")
        self.verticalLayout_59 = QVBoxLayout(self.dashboard_stacked_widget)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.stacked_list_report = QWidget(self.dashboard_stacked_widget)
        self.stacked_list_report.setObjectName(u"stacked_list_report")
        self.stacked_list_report.setStyleSheet(u"QWidget{ \n"
"	background-color: #f8fafc; \n"
"	border-radius: 20px;\n"
"}")
        self.verticalLayout_60 = QVBoxLayout(self.stacked_list_report)
        self.verticalLayout_60.setSpacing(2)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.stacked_list_report)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 0, 0)
        self.search_icon = QPushButton(self.widget_2)
        self.search_icon.setObjectName(u"search_icon")
        sizePolicy.setHeightForWidth(self.search_icon.sizePolicy().hasHeightForWidth())
        self.search_icon.setSizePolicy(sizePolicy)
        self.search_icon.setStyleSheet(u"padding: 5px;")
        icon26 = QIcon()
        icon26.addFile(u":/Icons/search_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_icon.setIcon(icon26)
        self.search_icon.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.search_icon)

        self.search_data = QLineEdit(self.widget_2)
        self.search_data.setObjectName(u"search_data")
        sizePolicy.setHeightForWidth(self.search_data.sizePolicy().hasHeightForWidth())
        self.search_data.setSizePolicy(sizePolicy)
        font28 = QFont()
        font28.setPointSize(14)
        font28.setBold(True)
        self.search_data.setFont(font28)
        self.search_data.setStyleSheet(u"QLineEdit {\n"
"    background-color: transparent; \n"
"	border: none; \n"
"	color: #1e2937;\n"
"	padding: 6px 4px;\n"
"    selection-background-color: #3b82f6;\n"
"    selection-color: #ffffff;\n"
"}")

        self.horizontalLayout_3.addWidget(self.search_data)

        self.multi_search_data = QWidget(self.widget_2)
        self.multi_search_data.setObjectName(u"multi_search_data")
        sizePolicy1.setHeightForWidth(self.multi_search_data.sizePolicy().hasHeightForWidth())
        self.multi_search_data.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.multi_search_data)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.line_31 = QFrame(self.multi_search_data)
        self.line_31.setObjectName(u"line_31")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line_31.sizePolicy().hasHeightForWidth())
        self.line_31.setSizePolicy(sizePolicy3)
        self.line_31.setMinimumSize(QSize(15, 0))
        self.line_31.setStyleSheet(u"border:3px solid black;")
        self.line_31.setFrameShape(QFrame.Shape.HLine)
        self.line_31.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_31)

        self.search_data_start_label_2 = QLabel(self.multi_search_data)
        self.search_data_start_label_2.setObjectName(u"search_data_start_label_2")
        font29 = QFont()
        font29.setPointSize(16)
        font29.setBold(True)
        self.search_data_start_label_2.setFont(font29)
        self.search_data_start_label_2.setStyleSheet(u"QLabel {\n"
"    background-color: transparent; \n"
"	border: none; \n"
"	color: #1e2937;\n"
"	padding: 6px 4px;\n"
"    selection-background-color: #3b82f6;\n"
"    selection-color: #ffffff;\n"
"}")

        self.horizontalLayout_4.addWidget(self.search_data_start_label_2)

        self.select_group_name = QComboBox(self.multi_search_data)
        self.select_group_name.addItem("")
        self.select_group_name.addItem("")
        self.select_group_name.addItem("")
        self.select_group_name.addItem("")
        self.select_group_name.setObjectName(u"select_group_name")
        sizePolicy.setHeightForWidth(self.select_group_name.sizePolicy().hasHeightForWidth())
        self.select_group_name.setSizePolicy(sizePolicy)
        self.select_group_name.setFont(font24)

        self.horizontalLayout_4.addWidget(self.select_group_name)

        self.line_32 = QFrame(self.multi_search_data)
        self.line_32.setObjectName(u"line_32")
        sizePolicy3.setHeightForWidth(self.line_32.sizePolicy().hasHeightForWidth())
        self.line_32.setSizePolicy(sizePolicy3)
        self.line_32.setMinimumSize(QSize(15, 0))
        self.line_32.setStyleSheet(u"border:3px solid black;")
        self.line_32.setFrameShape(QFrame.Shape.HLine)
        self.line_32.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_32)

        self.search_data_start_label = QLabel(self.multi_search_data)
        self.search_data_start_label.setObjectName(u"search_data_start_label")
        self.search_data_start_label.setFont(font29)
        self.search_data_start_label.setStyleSheet(u"QLabel {\n"
"    background-color: transparent; \n"
"	border: none; \n"
"	color: #1e2937;\n"
"	padding: 6px 4px;\n"
"    selection-background-color: #3b82f6;\n"
"    selection-color: #ffffff;\n"
"}")

        self.horizontalLayout_4.addWidget(self.search_data_start_label)

        self.search_data_start_edit = TimeOnlyEdit(self.multi_search_data)
        self.search_data_start_edit.setObjectName(u"search_data_start_edit")
        sizePolicy.setHeightForWidth(self.search_data_start_edit.sizePolicy().hasHeightForWidth())
        self.search_data_start_edit.setSizePolicy(sizePolicy)
        self.search_data_start_edit.setFont(font29)
        self.search_data_start_edit.setStyleSheet(u"QDateTimeEdit{\n"
"	border: 2px solid rgb(191, 191, 191);\n"
"	border-radius: 5px;\n"
"}\n"
"QCalendarWidget {\n"
"    background-color: #eff6ff;\n"
"    border: 1px solid #bfdbfe;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QCalendarWidget #qt_calendar_navigationbar {\n"
"    background-color: #eff6ff;\n"
"    padding: 6px 8px;\n"
"    border-bottom: 1px solid #bfdbfe;\n"
"    border-radius: 8px 8px 0 0;\n"
"}\n"
"QCalendarWidget QToolButton {\n"
"    color: #1e40af;\n"
"    background-color: #dbeafe;\n"
"    border: 1px solid #bfdbfe;\n"
"    border-radius: 6px;\n"
"    font-size: 22px;\n"
"	font-weight: 700;\n"
"    padding: 6px 16px;\n"
"}\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: #bfdbfe;\n"
"}\n"
"QCalendarWidget QToolButton:pressed {\n"
"    background-color: #1e40af;\n"
"    color: #ffffff;\n"
"}\n"
"QCalendarWidget QToolButton::menu-indicator { image: none; }\n"
"\n"
"QCalendarWidget QSpinBox {\n"
"    color: #1e3a8a;\n"
"    background-color: #dbeafe;\n"
"    border: 1px solid "
                        "#bfdbfe;\n"
"    border-radius: 6px;\n"
"    font-size: 18px;\n"
"	font-weight: 700;\n"
"    padding: 2px 4px;\n"
"    selection-background-color: #1e40af;\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"    background-color: #eff6ff;\n"
"    color: #1e3a8a;\n"
"    border: 1px solid #bfdbfe;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"}\n"
"QCalendarWidget QMenu::item:selected {\n"
"    background-color: #1e40af;\n"
"    color: #ffffff;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView {\n"
"    background-color: #eff6ff;\n"
"    color: #1e3a8a;\n"
"    selection-background-color: #1e3a8a;\n"
"    selection-color: #ffffff;\n"
"	font: 12px;\n"
"	font-weight: 700;\n"
"    outline: none;\n"
"}\n"
"\n"
"QCalendarWidget::section {\n"
"    background-color: #eff6ff;\n"
"    color: #3b82f6;\n"
"    font-size: 22px;\n"
"	font-weight: 700;\n"
"    padding: 6px 12px;\n"
"    border: none;\n"
"}\n"
"QCalendarWidget QTableView {\n"
"    font-size: 22px;\n"
"	font-weight: 700;\n"
"    paddi"
                        "ng: 2px 4px;\n"
"}\n"
"QCalendarWidget QTableView::item {\n"
"    min-width: 52px;\n"
"    min-height: 60px;\n"
"}\n"
"QCalendarWidget QTableView QHeaderView::section {\n"
"    font-size: 18px;\n"
"    padding: 10px 0;\n"
"    min-height: 60px;\n"
"}\n"
"")
        self.search_data_start_edit.setAlignment(Qt.AlignCenter)
        self.search_data_start_edit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.search_data_start_edit.setCurrentSection(QDateTimeEdit.HourSection)
        self.search_data_start_edit.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.search_data_start_edit)

        self.line_30 = QFrame(self.multi_search_data)
        self.line_30.setObjectName(u"line_30")
        sizePolicy3.setHeightForWidth(self.line_30.sizePolicy().hasHeightForWidth())
        self.line_30.setSizePolicy(sizePolicy3)
        self.line_30.setMinimumSize(QSize(15, 0))
        self.line_30.setStyleSheet(u"border:3px solid black;")
        self.line_30.setFrameShape(QFrame.Shape.HLine)
        self.line_30.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_30)

        self.search_data_end_label = QLabel(self.multi_search_data)
        self.search_data_end_label.setObjectName(u"search_data_end_label")
        self.search_data_end_label.setFont(font29)

        self.horizontalLayout_4.addWidget(self.search_data_end_label)

        self.search_data_end_edit = TimeOnlyEdit(self.multi_search_data)
        self.search_data_end_edit.setObjectName(u"search_data_end_edit")
        sizePolicy.setHeightForWidth(self.search_data_end_edit.sizePolicy().hasHeightForWidth())
        self.search_data_end_edit.setSizePolicy(sizePolicy)
        self.search_data_end_edit.setFont(font29)
        self.search_data_end_edit.setStyleSheet(u"QDateTimeEdit{\n"
"	border: 2px solid rgb(191, 191, 191);\n"
"	border-radius: 5px;\n"
"}\n"
"QCalendarWidget {\n"
"    background-color: #eff6ff;\n"
"    border: 1px solid #bfdbfe;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QCalendarWidget #qt_calendar_navigationbar {\n"
"    background-color: #eff6ff;\n"
"    padding: 6px 8px;\n"
"    border-bottom: 1px solid #bfdbfe;\n"
"    border-radius: 8px 8px 0 0;\n"
"}\n"
"QCalendarWidget QToolButton {\n"
"    color: #1e40af;\n"
"    background-color: #dbeafe;\n"
"    border: 1px solid #bfdbfe;\n"
"    border-radius: 6px;\n"
"    font-size: 22px;\n"
"	font-weight: 700;\n"
"    padding: 6px 16px;\n"
"}\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: #bfdbfe;\n"
"}\n"
"QCalendarWidget QToolButton:pressed {\n"
"    background-color: #1e40af;\n"
"    color: #ffffff;\n"
"}\n"
"QCalendarWidget QToolButton::menu-indicator { image: none; }\n"
"\n"
"QCalendarWidget QSpinBox {\n"
"    color: #1e3a8a;\n"
"    background-color: #dbeafe;\n"
"    border: 1px solid "
                        "#bfdbfe;\n"
"    border-radius: 6px;\n"
"    font-size: 18px;\n"
"	font-weight: 700;\n"
"    padding: 2px 4px;\n"
"    selection-background-color: #1e40af;\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"    background-color: #eff6ff;\n"
"    color: #1e3a8a;\n"
"    border: 1px solid #bfdbfe;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"}\n"
"QCalendarWidget QMenu::item:selected {\n"
"    background-color: #1e40af;\n"
"    color: #ffffff;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView {\n"
"    background-color: #eff6ff;\n"
"    color: #1e3a8a;\n"
"    selection-background-color: #1e3a8a;\n"
"    selection-color: #ffffff;\n"
"	font: 12px;\n"
"	font-weight: 700;\n"
"    outline: none;\n"
"}\n"
"\n"
"QCalendarWidget::section {\n"
"    background-color: #eff6ff;\n"
"    color: #3b82f6;\n"
"    font-size: 22px;\n"
"	font-weight: 700;\n"
"    padding: 6px 12px;\n"
"    border: none;\n"
"}\n"
"QCalendarWidget QTableView {\n"
"    font-size: 22px;\n"
"	font-weight: 700;\n"
"    paddi"
                        "ng: 2px 4px;\n"
"}\n"
"QCalendarWidget QTableView::item {\n"
"    min-width: 52px;\n"
"    min-height: 60px;\n"
"}\n"
"QCalendarWidget QTableView QHeaderView::section {\n"
"    font-size: 18px;\n"
"    padding: 10px 0;\n"
"    min-height: 60px;\n"
"}\n"
"")
        self.search_data_end_edit.setAlignment(Qt.AlignCenter)
        self.search_data_end_edit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.search_data_end_edit.setCurrentSection(QDateTimeEdit.HourSection)
        self.search_data_end_edit.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.search_data_end_edit)


        self.horizontalLayout_3.addWidget(self.multi_search_data)

        self.label_info = QLabel(self.widget_2)
        self.label_info.setObjectName(u"label_info")
        font30 = QFont()
        font30.setPointSize(13)
        font30.setItalic(True)
        self.label_info.setFont(font30)

        self.horizontalLayout_3.addWidget(self.label_info)

        self.clear_history_search = QPushButton(self.widget_2)
        self.clear_history_search.setObjectName(u"clear_history_search")
        sizePolicy.setHeightForWidth(self.clear_history_search.sizePolicy().hasHeightForWidth())
        self.clear_history_search.setSizePolicy(sizePolicy)
        self.clear_history_search.setMinimumSize(QSize(45, 0))
        icon27 = QIcon()
        icon27.addFile(u":/Icons/circle-xmark.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clear_history_search.setIcon(icon27)
        self.clear_history_search.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.clear_history_search)

        self.list_query_btn = QHBoxLayout()
        self.list_query_btn.setObjectName(u"list_query_btn")
        self.list_query_btn.setContentsMargins(-1, -1, -1, 0)
        self.export_all_tables_to_excel_btn = QPushButton(self.widget_2)
        self.export_all_tables_to_excel_btn.setObjectName(u"export_all_tables_to_excel_btn")
        sizePolicy.setHeightForWidth(self.export_all_tables_to_excel_btn.sizePolicy().hasHeightForWidth())
        self.export_all_tables_to_excel_btn.setSizePolicy(sizePolicy)
        self.export_all_tables_to_excel_btn.setFont(font29)
        self.export_all_tables_to_excel_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B7EC8;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0968A3;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #085A91;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #94A3B8;\n"
"    color: #CBD5E1;\n"
"}")
        icon28 = QIcon()
        icon28.addFile(u":/Icons/xlsx-file-format.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.export_all_tables_to_excel_btn.setIcon(icon28)
        self.export_all_tables_to_excel_btn.setIconSize(QSize(35, 35))

        self.list_query_btn.addWidget(self.export_all_tables_to_excel_btn)


        self.horizontalLayout_3.addLayout(self.list_query_btn)


        self.verticalLayout_60.addWidget(self.widget_2)

        self.stacked_list_history_page = QStackedWidget(self.stacked_list_report)
        self.stacked_list_history_page.setObjectName(u"stacked_list_history_page")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_15 = QVBoxLayout(self.page_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.list_history = QTableWidget(self.page_5)
        if (self.list_history.columnCount() < 9):
            self.list_history.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.list_history.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.list_history.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.list_history.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.list_history.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.list_history.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.list_history.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.list_history.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.list_history.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.list_history.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.list_history.setObjectName(u"list_history")
        self.list_history.setFont(font29)
        self.list_history.setStyleSheet(u"QTableWidget {\n"
"    background-color: #ffffff; border: 1px solid #BFC8D3; border-radius: 8px;\n"
"    gridline-color: #BFC8D3; color: #334155;\n"
"    selection-background-color: #dbeafe; selection-color: #1e40af; outline: none;\n"
"}\n"
"QTableWidget::item { padding: 8px 14px; border-bottom: 1px solid #f1f5f9; }\n"
"QTableWidget::item:selected { background-color: #dbeafe; color: #1e40af; }\n"
"QTableWidget::item:hover { background-color: rgb(222, 225, 226); }\n"
"QHeaderView::section {\n"
"    background-color: #f8fafc; color: #1e40af; font-family: \"Segoe UI\";\n"
"    font-size: 16px; font-weight: 700; letter-spacing: 1.5px;\n"
"    padding: 10px 14px; border: none; border-bottom: 2px solid #3b82f6;\n"
"    border-right: 1px solid #e2e8f0;\n"
"}\n"
"QHeaderView::section:last { border-right: none; }\n"
"QScrollBar:vertical { background: #f8fafc; width: 20px; border-radius: 4px; }\n"
"QScrollBar::handle:vertical { background: #cbd5e1; border-radius: 4px; min-height: 24px; }\n"
"QScrollBar::handle:vertical:"
                        "hover { background: #94a3b8; }\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0px; }\n"
"QScrollBar:horizontal { background: #f8fafc; height: 8px; border-radius: 4px; }\n"
"QScrollBar::handle:horizontal { background: #cbd5e1; border-radius: 4px; min-width: 24px; }\n"
"QScrollBar::handle:horizontal:hover { background: #94a3b8; }\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal { width: 0px; }")
        self.list_history.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.list_history.setAutoScrollMargin(25)
        self.list_history.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_history.setDragEnabled(False)
        self.list_history.setSortingEnabled(False)
        self.list_history.horizontalHeader().setCascadingSectionResizes(True)
        self.list_history.horizontalHeader().setStretchLastSection(True)
        self.list_history.verticalHeader().setVisible(False)
        self.list_history.verticalHeader().setDefaultSectionSize(40)

        self.verticalLayout_15.addWidget(self.list_history)

        self.stacked_list_history_page.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_7 = QVBoxLayout(self.page_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.list_history_2 = QTableWidget(self.page_6)
        if (self.list_history_2.columnCount() < 9):
            self.list_history_2.setColumnCount(9)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.list_history_2.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.list_history_2.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.list_history_2.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.list_history_2.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.list_history_2.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.list_history_2.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.list_history_2.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.list_history_2.setHorizontalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.list_history_2.setHorizontalHeaderItem(8, __qtablewidgetitem17)
        self.list_history_2.setObjectName(u"list_history_2")
        self.list_history_2.setFont(font29)
        self.list_history_2.setStyleSheet(u"QTableWidget {\n"
"    background-color: #ffffff; border: 1px solid #BFC8D3; border-radius: 8px;\n"
"    gridline-color: #BFC8D3; color: #334155;\n"
"    selection-background-color: #dbeafe; selection-color: #1e40af; outline: none;\n"
"}\n"
"QTableWidget::item { padding: 8px 14px; border-bottom: 1px solid #f1f5f9; }\n"
"QTableWidget::item:selected { background-color: #dbeafe; color: #1e40af; }\n"
"QTableWidget::item:hover { background-color: rgb(222, 225, 226); }\n"
"QHeaderView::section {\n"
"    background-color: #f8fafc; color: #1e40af; font-family: \"Segoe UI\";\n"
"    font-size: 16px; font-weight: 700; letter-spacing: 1.5px;\n"
"    padding: 10px 14px; border: none; border-bottom: 2px solid #3b82f6;\n"
"    border-right: 1px solid #e2e8f0;\n"
"}\n"
"QHeaderView::section:last { border-right: none; }\n"
"QScrollBar:vertical { background: #f8fafc; width: 20px; border-radius: 4px; }\n"
"QScrollBar::handle:vertical { background: #cbd5e1; border-radius: 4px; min-height: 24px; }\n"
"QScrollBar::handle:vertical:"
                        "hover { background: #94a3b8; }\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0px; }\n"
"QScrollBar:horizontal { background: #f8fafc; height: 8px; border-radius: 4px; }\n"
"QScrollBar::handle:horizontal { background: #cbd5e1; border-radius: 4px; min-width: 24px; }\n"
"QScrollBar::handle:horizontal:hover { background: #94a3b8; }\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal { width: 0px; }")
        self.list_history_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.list_history_2.setAutoScrollMargin(25)
        self.list_history_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_history_2.horizontalHeader().setStretchLastSection(True)
        self.list_history_2.verticalHeader().setVisible(False)
        self.list_history_2.verticalHeader().setDefaultSectionSize(40)

        self.verticalLayout_7.addWidget(self.list_history_2)

        self.stacked_list_history_page.addWidget(self.page_6)

        self.verticalLayout_60.addWidget(self.stacked_list_history_page)

        self.verticalLayout_60.setStretch(1, 1)

        self.verticalLayout_59.addWidget(self.stacked_list_report)

        self.verticalLayout_59.setStretch(0, 9)

        self.verticalLayout_13.addWidget(self.dashboard_stacked_widget)

        self.stackedWidget_2.addWidget(self.history_page)

        self.verticalLayout_11.addWidget(self.stackedWidget_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_11)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.body_frame)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(1)
        self.sys_state_stacked_wid_39.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stacked_cel_fah_press_b_2.setCurrentIndex(0)
        self.stacked_cel_fah_press_b_3.setCurrentIndex(0)
        self.stacked_cel_fah_press_a_4.setCurrentIndex(0)
        self.stacked_cel_fah_press_c_4.setCurrentIndex(0)
        self.stacked_cel_fah_press_b_4.setCurrentIndex(0)
        self.stacked_cel_fah_press_b_1.setCurrentIndex(0)
        self.stacked_cel_fah_press_a_3.setCurrentIndex(0)
        self.stacked_cel_fah_press_c_2.setCurrentIndex(0)
        self.stacked_cel_fah_press_c_3.setCurrentIndex(0)
        self.stacked_cel_fah_press_c_1.setCurrentIndex(0)
        self.stacked_cel_fah_press_a_2.setCurrentIndex(0)
        self.stacked_cel_fah_press_a_1.setCurrentIndex(0)
        self.start_stop_stacked.setCurrentIndex(0)
        self.stacked_cel_fah_temp_b_4.setCurrentIndex(0)
        self.stacked_cel_fah_temp_b_7.setCurrentIndex(0)
        self.stacked_cel_fah_temp_b_2.setCurrentIndex(0)
        self.stacked_cel_fah_temp_b_1.setCurrentIndex(0)
        self.stacked_cel_fah_temp_a_7.setCurrentIndex(0)
        self.stacked_cel_fah_temp_b_3.setCurrentIndex(0)
        self.stacked_cel_fah_temp_a_3.setCurrentIndex(0)
        self.stacked_cel_fah_temp_c_6.setCurrentIndex(0)
        self.stacked_cel_fah_temp_a_4.setCurrentIndex(0)
        self.stacked_cel_fah_temp_c_5.setCurrentIndex(0)
        self.stacked_cel_fah_temp_b_5.setCurrentIndex(0)
        self.stacked_cel_fah_temp_b_6.setCurrentIndex(0)
        self.stacked_cel_fah_temp_c_2.setCurrentIndex(0)
        self.stacked_cel_fah_temp_a_1.setCurrentIndex(0)
        self.stacked_cel_fah_temp_c_3.setCurrentIndex(0)
        self.stacked_cel_fah_temp_c_1.setCurrentIndex(0)
        self.stacked_cel_fah_temp_a_2.setCurrentIndex(0)
        self.stacked_cel_fah_temp_c_4.setCurrentIndex(0)
        self.stacked_cel_fah_temp_c_7.setCurrentIndex(0)
        self.stacked_cel_fah_temp_t0_5.setCurrentIndex(0)
        self.stacked_cel_fah_temp_t0_4.setCurrentIndex(0)
        self.stacked_cel_fah_temp_t0_1.setCurrentIndex(0)
        self.stacked_cel_fah_temp_t0_2.setCurrentIndex(0)
        self.stacked_cel_fah_temp_t0_3.setCurrentIndex(0)
        self.stacked_cel_fah_temp_a_5.setCurrentIndex(0)
        self.stacked_cel_fah_temp_a_6.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(1)
        self.sys_state_stacked_wid_42.setCurrentIndex(1)
        self.sys_state_stacked_wid_40.setCurrentIndex(2)
        self.i_o_group_1_switch_3.setCurrentIndex(0)
        self.i_o_group_1_switch_5.setCurrentIndex(0)
        self.i_o_group_1_switch_6.setCurrentIndex(0)
        self.i_o_group_1_switch_7.setCurrentIndex(0)
        self.i_o_group_1_switch_2.setCurrentIndex(0)
        self.i_o_group_1_switch_1.setCurrentIndex(0)
        self.i_o_group_1_switch_4.setCurrentIndex(0)
        self.i_o_group_1_switch_8.setCurrentIndex(0)
        self.i_o_group_1_switch_11.setCurrentIndex(0)
        self.i_o_group_1_switch_9.setCurrentIndex(0)
        self.i_o_group_1_switch_10.setCurrentIndex(0)
        self.i_o_group_1_switch_12.setCurrentIndex(0)
        self.i_o_group_1_switch_13.setCurrentIndex(0)
        self.stacked_list_history_page.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tech-Link - Production System", None))
        self.label_2.setText("")
        self.company_name.setText(QCoreApplication.translate("MainWindow", u"TECH-LINK", None))
        self.error_display.setText("")
        self.eng_language.setText("")
        self.cn_language.setText("")
        self.date_displ.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy hh:mm:ss", None))
        self.home_page_btn.setText(QCoreApplication.translate("MainWindow", u" Group", None))
        self.chart_page_btn.setText(QCoreApplication.translate("MainWindow", u" Chart", None))
        self.device_page_btn.setText(QCoreApplication.translate("MainWindow", u" Setting", None))
        self.history_page_btn.setText(QCoreApplication.translate("MainWindow", u" History", None))
        self.open_side_menu_btn.setText("")
        self.next_group_page_btn.setText("")
        self.stop_light.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.start_light.setText(QCoreApplication.translate("MainWindow", u"Running", None))
        self.temp_unit_selection_combox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u00b0C ", None))
        self.temp_unit_selection_combox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u00b0F", None))

        self.clear_data_btn.setText(QCoreApplication.translate("MainWindow", u" Clear Data", None))
        self.new_data_btn.setText(QCoreApplication.translate("MainWindow", u" Import Data", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"Group B", None))
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"PV", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"SV", None))
        self.clear_group_b.setText("")
        self.refuel_btn_c_2.setText(QCoreApplication.translate("MainWindow", u" Oil Fill C", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Cycle Setting:", None))
        self.set_cycle_b_btn.setText("")
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Oil Start time:", None))
        self.pressure_pv_a_9.setPrefix("")
        self.pressure_pv_a_9.setSuffix("")
        self.pressure_sv_a_9.setPrefix("")
        self.pressure_sv_a_9.setSuffix("")
        self.label_245.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.set_cycle_a_btn.setText("")
        self.set_cycle_c_btn.setText("")
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"ITV Pressure:", None))
        self.pressure_pv_a_5.setPrefix("")
        self.pressure_pv_a_5.setSuffix("")
        self.label_267.setText(QCoreApplication.translate("MainWindow", u"Bar", None))
        self.pressure_pv_a_8.setPrefix("")
        self.pressure_pv_a_8.setSuffix("")
        self.pressure_sv_a_8.setPrefix("")
        self.pressure_sv_a_8.setSuffix("")
        self.label_244.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_c_10.setPrefix("")
        self.pressure_pv_c_10.setSuffix("")
        self.pressure_sv_c_10.setPrefix("")
        self.pressure_sv_c_10.setSuffix("")
        self.label_262.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_b_5.setPrefix("")
        self.pressure_pv_b_5.setSuffix("")
        self.label_268.setText(QCoreApplication.translate("MainWindow", u"Bar", None))
        self.pressure_pv_b_10.setPrefix("")
        self.pressure_pv_b_10.setSuffix("")
        self.pressure_sv_b_10.setPrefix("")
        self.pressure_sv_b_10.setSuffix("")
        self.label_248.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_a_10.setPrefix("")
        self.pressure_pv_a_10.setSuffix("")
        self.pressure_sv_a_10.setPrefix("")
        self.pressure_sv_a_10.setSuffix("")
        self.label_246.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_a_6.setPrefix("")
        self.pressure_pv_a_6.setSuffix("")
        self.pressure_sv_a_6.setPrefix("")
        self.pressure_sv_a_6.setSuffix("")
        self.label_242.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Air Holding time:", None))
        self.pressure_sv_c_5.setPrefix("")
        self.pressure_sv_c_5.setSuffix("")
        self.label_263.setText(QCoreApplication.translate("MainWindow", u"Bar", None))
        self.pressure_pv_b_8.setPrefix("")
        self.pressure_pv_b_8.setSuffix("")
        self.pressure_sv_b_8.setPrefix("")
        self.pressure_sv_b_8.setSuffix("")
        self.label_256.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_sv_a_5.setPrefix("")
        self.pressure_sv_a_5.setSuffix("")
        self.label_241.setText(QCoreApplication.translate("MainWindow", u"Bar", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Air Filling time:", None))
        self.pressure_pv_b_12.setPrefix("")
        self.pressure_pv_b_12.setSuffix("")
        self.label_272.setText(QCoreApplication.translate("MainWindow", u"Bar", None))
        self.pressure_pv_c_5.setPrefix("")
        self.pressure_pv_c_5.setSuffix("")
        self.label_269.setText(QCoreApplication.translate("MainWindow", u"Bar", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Pipe Pressure:", None))
        self.pressure_pv_a_7.setPrefix("")
        self.pressure_pv_a_7.setSuffix("")
        self.pressure_sv_a_7.setPrefix("")
        self.pressure_sv_a_7.setSuffix("")
        self.label_243.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Pressure Setting:", None))
        self.pressure_sv_b_5.setPrefix("")
        self.pressure_sv_b_5.setSuffix("")
        self.label_253.setText(QCoreApplication.translate("MainWindow", u"Bar", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Temp Setting:", None))
        self.pressure_pv_c_6.setPrefix("")
        self.pressure_pv_c_6.setSuffix("")
        self.pressure_sv_c_6.setPrefix("")
        self.pressure_sv_c_6.setSuffix("")
        self.label_264.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_b_7.setPrefix("")
        self.pressure_pv_b_7.setSuffix("")
        self.pressure_sv_b_7.setPrefix("")
        self.pressure_sv_b_7.setSuffix("")
        self.label_255.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Oil End time:", None))
        self.pressure_pv_b_9.setPrefix("")
        self.pressure_pv_b_9.setSuffix("")
        self.pressure_sv_b_9.setPrefix("")
        self.pressure_sv_b_9.setSuffix("")
        self.label_247.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_c_9.setPrefix("")
        self.pressure_pv_c_9.setSuffix("")
        self.pressure_sv_c_9.setPrefix("")
        self.pressure_sv_c_9.setSuffix("")
        self.label_261.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Air Bleeding time:", None))
        self.pressure_pv_a_12.setPrefix("")
        self.pressure_pv_a_12.setSuffix("")
        self.label_270.setText(QCoreApplication.translate("MainWindow", u"Bar", None))
        self.pressure_pv_c_7.setPrefix("")
        self.pressure_pv_c_7.setSuffix("")
        self.pressure_sv_c_7.setPrefix("")
        self.pressure_sv_c_7.setSuffix("")
        self.label_265.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_b_6.setPrefix("")
        self.pressure_pv_b_6.setSuffix("")
        self.pressure_sv_b_6.setPrefix("")
        self.pressure_sv_b_6.setSuffix("")
        self.label_254.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_c_8.setPrefix("")
        self.pressure_pv_c_8.setSuffix("")
        self.pressure_sv_c_8.setPrefix("")
        self.pressure_sv_c_8.setSuffix("")
        self.label_266.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_c_12.setPrefix("")
        self.pressure_pv_c_12.setSuffix("")
        self.label_271.setText(QCoreApplication.translate("MainWindow", u"Bar", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"End Temperature:", None))
        self.pressure_pv_b_2.setPrefix("")
        self.pressure_pv_b_2.setSuffix("")
        self.label_392.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_393.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_pv_b_3.setPrefix("")
        self.pressure_pv_b_3.setSuffix("")
        self.label_394.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_395.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_pv_a_4.setPrefix("")
        self.pressure_pv_a_4.setSuffix("")
        self.label_383.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_384.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_pv_c_4.setPrefix("")
        self.pressure_pv_c_4.setSuffix("")
        self.label_403.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_404.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_pv_b_4.setPrefix("")
        self.pressure_pv_b_4.setSuffix("")
        self.label_396.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_397.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_sv_b_1.setPrefix("")
        self.pressure_sv_b_1.setSuffix("")
        self.label_281.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_366.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_pv_a_3.setPrefix("")
        self.pressure_pv_a_3.setSuffix("")
        self.label_381.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_382.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_pv_c_2.setPrefix("")
        self.pressure_pv_c_2.setSuffix("")
        self.label_282.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_400.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Mid Temperature:", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Front Temperature:", None))
        self.pressure_pv_c_3.setPrefix("")
        self.pressure_pv_c_3.setSuffix("")
        self.label_401.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_402.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_sv_c_1.setPrefix("")
        self.pressure_sv_c_1.setSuffix("")
        self.label_398.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_399.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_pv_a_2.setPrefix("")
        self.pressure_pv_a_2.setSuffix("")
        self.label_379.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_380.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.vacuum_btn_a.setText(QCoreApplication.translate("MainWindow", u" Pressure A", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"Group C", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"PV", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"SV", None))
        self.clear_group_c.setText("")
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"Group A", None))
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"PV", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"SV", None))
        self.clear_group_a.setText("")
        self.refuel_btn_a.setText(QCoreApplication.translate("MainWindow", u" Oil Fill A", None))
        self.vacuum_btn_c.setText(QCoreApplication.translate("MainWindow", u" Pressure C", None))
        self.vacuum_btn_b.setText(QCoreApplication.translate("MainWindow", u" Pressure B", None))
        self.pressure_sv_a_1.setPrefix("")
        self.pressure_sv_a_1.setSuffix("")
        self.label_280.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_340.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.refuel_btn_b.setText(QCoreApplication.translate("MainWindow", u" Oil Fill B", None))
        self.heat_btn_a.setText(QCoreApplication.translate("MainWindow", u" Heating A", None))
        self.heat_btn_b.setText(QCoreApplication.translate("MainWindow", u" Heating B", None))
        self.heat_btn_c.setText(QCoreApplication.translate("MainWindow", u" Heating C", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u" Start", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u" Stop", None))
        self.bt_l_alm_value.setPrefix("")
        self.bt_l_alm_value.setSuffix("")
        self.label_342.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_343.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.bt_t3_offset_value.setPrefix("")
        self.bt_t3_offset_value.setSuffix("")
        self.label_348.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_349.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.bt_sv.setPrefix("")
        self.bt_sv.setSuffix("")
        self.label_336.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_337.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.bt_pv.setPrefix("")
        self.bt_pv.setSuffix("")
        self.label_334.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_335.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"Temperature A", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"PV:", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"SV:", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"H.Alm Value:", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"L.Alm Value:", None))
        self.at_t3_offset_value.setPrefix("")
        self.at_t3_offset_value.setSuffix("")
        self.label_332.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_333.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.bt_h_alm_value.setPrefix("")
        self.bt_h_alm_value.setSuffix("")
        self.label_338.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_339.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.at_h_alm_value.setPrefix("")
        self.at_h_alm_value.setSuffix("")
        self.label_324.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_325.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.ct_t2_offset_value.setPrefix("")
        self.ct_t2_offset_value.setSuffix("")
        self.label_360.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_361.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.at_l_alm_value.setPrefix("")
        self.at_l_alm_value.setSuffix("")
        self.label_326.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_327.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.ct_t1_offset_value.setPrefix("")
        self.ct_t1_offset_value.setSuffix("")
        self.label_358.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_359.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.bt_t1_offset_value.setPrefix("")
        self.bt_t1_offset_value.setSuffix("")
        self.label_344.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_345.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.bt_t2_offset_value.setPrefix("")
        self.bt_t2_offset_value.setSuffix("")
        self.label_346.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_347.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"Temperature Oven", None))
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"Temperature C", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"Temperature B", None))
        self.ct_sv.setPrefix("")
        self.ct_sv.setSuffix("")
        self.label_352.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_353.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.at_pv.setPrefix("")
        self.at_pv.setSuffix("")
        self.label_320.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_321.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.ct_h_alm_value.setPrefix("")
        self.ct_h_alm_value.setSuffix("")
        self.label_354.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_355.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.ct_pv.setPrefix("")
        self.ct_pv.setSuffix("")
        self.label_350.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_351.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.at_sv.setPrefix("")
        self.at_sv.setSuffix("")
        self.label_322.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_323.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.ct_l_alm_value.setPrefix("")
        self.ct_l_alm_value.setSuffix("")
        self.label_356.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_357.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.ct_t3_offset_value.setPrefix("")
        self.ct_t3_offset_value.setSuffix("")
        self.label_362.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_363.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"Offset Mid:", None))
        self.t0_offset_value.setPrefix("")
        self.t0_offset_value.setSuffix("")
        self.label_364.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_365.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.t0_l_alm_value.setPrefix("")
        self.t0_l_alm_value.setSuffix("")
        self.label_259.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_260.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.t0_pv.setPrefix("")
        self.t0_pv.setSuffix("")
        self.label_249.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_250.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.t0_sv.setPrefix("")
        self.t0_sv.setSuffix("")
        self.label_251.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_252.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.t0_h_alm_value.setPrefix("")
        self.t0_h_alm_value.setSuffix("")
        self.label_257.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_258.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.at_t1_offset_value.setPrefix("")
        self.at_t1_offset_value.setSuffix("")
        self.label_328.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_329.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.at_t2_offset_value.setPrefix("")
        self.at_t2_offset_value.setSuffix("")
        self.label_330.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_331.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"Offset Front:", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"Offset End:", None))
        self.heat_btn_t0.setText(QCoreApplication.translate("MainWindow", u" Heating T0", None))
        self.plc_io_btn.setText("")
        self.connection_group.setTitle(QCoreApplication.translate("MainWindow", u"Connection Settings", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Online", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Offline", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Try Connecting...", None))
        self.write_time_input.setSuffix(QCoreApplication.translate("MainWindow", u" ms ~ 1000 ms", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Online", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Offline", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Try Connecting...", None))
        self.read_time_input.setSuffix(QCoreApplication.translate("MainWindow", u" ms ~ 1000 ms", None))
        self.total_cycle_label_2.setText(QCoreApplication.translate("MainWindow", u" Total Test Time B:", None))
        self.total_cycle_label.setText(QCoreApplication.translate("MainWindow", u" Total Test Time A:", None))
        self.total_cycle_label_3.setText(QCoreApplication.translate("MainWindow", u" Total Test Time C:", None))
        self.read_plc_label.setText(QCoreApplication.translate("MainWindow", u" PLC Read:", None))
        self.write_table_label.setText(QCoreApplication.translate("MainWindow", u" History Cycle:", None))
        self.write_plc_label.setText(QCoreApplication.translate("MainWindow", u" PLC Write:", None))
        self.table_write_cycle.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.cycle_b_displ_3.setSuffix("")
        self.cycle_b_displ_3.setPrefix("")
        self.reset_cycle_b_btn.setText("")
        self.cycle_a_displ_3.setSuffix("")
        self.cycle_a_displ_3.setPrefix("")
        self.reset_cycle_a_btn.setText("")
        self.cycle_c_displ_3.setSuffix("")
        self.cycle_c_displ_3.setPrefix("")
        self.reset_cycle_c_btn.setText("")
        self.i_o_group_1.setTitle(QCoreApplication.translate("MainWindow", u"DI", None))
        self.pushButton_59.setText("")
        self.pushButton_58.setText("")
        self.pushButton_63.setText("")
        self.pushButton_62.setText("")
        self.pushButton_65.setText("")
        self.pushButton_64.setText("")
        self.pushButton_67.setText("")
        self.pushButton_66.setText("")
        self.pushButton_57.setText("")
        self.pushButton_56.setText("")
        self.di_name_1.setText(QCoreApplication.translate("MainWindow", u"T0 Heat:", None))
        self.pushButton_43.setText("")
        self.pushButton_42.setText("")
        self.pushButton_61.setText("")
        self.pushButton_60.setText("")
        self.di_name_2.setText(QCoreApplication.translate("MainWindow", u"P1 Heat:", None))
        self.di_name_3.setText(QCoreApplication.translate("MainWindow", u"P1 Press:", None))
        self.pushButton_69.setText("")
        self.pushButton_68.setText("")
        self.di_name_4.setText(QCoreApplication.translate("MainWindow", u"P1 Oil:", None))
        self.di_name_5.setText(QCoreApplication.translate("MainWindow", u"P1 Count:", None))
        self.di_name_6.setText(QCoreApplication.translate("MainWindow", u"P2 Heat:", None))
        self.di_name_7.setText(QCoreApplication.translate("MainWindow", u"P2 Press:", None))
        self.di_name_8.setText(QCoreApplication.translate("MainWindow", u"P2 Oil:", None))
        self.di_name_11.setText(QCoreApplication.translate("MainWindow", u"P3 Press:", None))
        self.pushButton_74.setText("")
        self.pushButton_75.setText("")
        self.di_name_12.setText(QCoreApplication.translate("MainWindow", u"P3 Oil:", None))
        self.di_name_9.setText(QCoreApplication.translate("MainWindow", u"P2 Count:", None))
        self.di_name_10.setText(QCoreApplication.translate("MainWindow", u"P3 Heat:", None))
        self.pushButton_70.setText("")
        self.pushButton_71.setText("")
        self.pushButton_72.setText("")
        self.pushButton_73.setText("")
        self.di_name_13.setText(QCoreApplication.translate("MainWindow", u"P3 Count:", None))
        self.pushButton_76.setText("")
        self.pushButton_77.setText("")
        self.pushButton_78.setText("")
        self.pushButton_79.setText("")
        self.i_o_group_3.setTitle(QCoreApplication.translate("MainWindow", u"AI", None))
        self.ai_name_1.setText(QCoreApplication.translate("MainWindow", u"T0:", None))
        self.ai_name_15.setText(QCoreApplication.translate("MainWindow", u"ITV-2:", None))
        self.ai_name_14.setText(QCoreApplication.translate("MainWindow", u"ITV-1:", None))
        self.ai_name_12.setText(QCoreApplication.translate("MainWindow", u"P2:", None))
        self.ai_name_13.setText(QCoreApplication.translate("MainWindow", u"P3:", None))
        self.ai_name_16.setText(QCoreApplication.translate("MainWindow", u"ITV-3:", None))
        self.ai_name_4.setText(QCoreApplication.translate("MainWindow", u"T1-3:", None))
        self.ai_name_3.setText(QCoreApplication.translate("MainWindow", u"T1-2:", None))
        self.ai_name_5.setText(QCoreApplication.translate("MainWindow", u"T2-1:", None))
        self.ai_name_2.setText(QCoreApplication.translate("MainWindow", u"T1-1:", None))
        self.ai_name_6.setText(QCoreApplication.translate("MainWindow", u"T2-2:", None))
        self.ai_name_7.setText(QCoreApplication.translate("MainWindow", u"T2-3:", None))
        self.ai_name_8.setText(QCoreApplication.translate("MainWindow", u"T3-1:", None))
        self.ai_name_9.setText(QCoreApplication.translate("MainWindow", u"T3-2:", None))
        self.ai_name_10.setText(QCoreApplication.translate("MainWindow", u"T3-3:", None))
        self.ai_name_11.setText(QCoreApplication.translate("MainWindow", u"P1:", None))
        self.i_o_group_2.setTitle(QCoreApplication.translate("MainWindow", u"Total Test Time", None))
        self.db_file_path.setText(QCoreApplication.translate("MainWindow", u" DB Path:", None))
        self.db_file_path_edit.setText("")
        self.ip_plc_address.setText(QCoreApplication.translate("MainWindow", u" IP:", None))
        self.plc_ip_address_edit.setText("")
        self.db_number.setText(QCoreApplication.translate("MainWindow", u" DB:", None))
        self.write_plc_label_2.setText(QCoreApplication.translate("MainWindow", u" Size Data:", None))
        self.db_data_size_input.setSuffix(QCoreApplication.translate("MainWindow", u" ~ 2056", None))
        self.back_connection_page_btn.setText(QCoreApplication.translate("MainWindow", u"Connection Page", None))
        self.back_home_page_btn.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.search_icon.setText("")
        self.search_data.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[Name]", None))
        self.search_data_start_label_2.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.select_group_name.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.select_group_name.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.select_group_name.setItemText(2, QCoreApplication.translate("MainWindow", u"B", None))
        self.select_group_name.setItemText(3, QCoreApplication.translate("MainWindow", u"C", None))

        self.search_data_start_label.setText(QCoreApplication.translate("MainWindow", u"Start:", None))
        self.search_data_start_edit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm - dd/MM/yyyy", None))
        self.search_data_end_label.setText(QCoreApplication.translate("MainWindow", u"End:", None))
        self.search_data_end_edit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm - dd/MM/yyyy", None))
        self.label_info.setText("")
        self.clear_history_search.setText("")
        self.export_all_tables_to_excel_btn.setText(QCoreApplication.translate("MainWindow", u" Export to Excel", None))
        ___qtablewidgetitem = self.list_history.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"No.", None))
        ___qtablewidgetitem1 = self.list_history.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name.", None))
        ___qtablewidgetitem2 = self.list_history.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Group.", None))
        ___qtablewidgetitem3 = self.list_history.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Pressure.", None))
        ___qtablewidgetitem4 = self.list_history.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"T-Oven.", None))
        ___qtablewidgetitem5 = self.list_history.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Front.", None))
        ___qtablewidgetitem6 = self.list_history.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Middle.", None))
        ___qtablewidgetitem7 = self.list_history.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"End.", None))
        ___qtablewidgetitem8 = self.list_history.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Date.", None))
        ___qtablewidgetitem9 = self.list_history_2.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"No.", None))
        ___qtablewidgetitem10 = self.list_history_2.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Name.", None))
        ___qtablewidgetitem11 = self.list_history_2.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Group.", None))
        ___qtablewidgetitem12 = self.list_history_2.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Pressure.", None))
        ___qtablewidgetitem13 = self.list_history_2.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"T-Oven.", None))
        ___qtablewidgetitem14 = self.list_history_2.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Front.", None))
        ___qtablewidgetitem15 = self.list_history_2.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Middle.", None))
        ___qtablewidgetitem16 = self.list_history_2.horizontalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"End.", None))
        ___qtablewidgetitem17 = self.list_history_2.horizontalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Date.", None))
    # retranslateUi


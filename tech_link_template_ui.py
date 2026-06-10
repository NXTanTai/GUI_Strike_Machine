# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tech_link_template.ui'
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
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
from marquee_label import MarqueeLabel
from qtime_only_edit import TimeOnlyEdit
import Icon_rc
import resources_rc
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 960)
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
        self.logo_btn = QPushButton(self.header_frame)
        self.logo_btn.setObjectName(u"logo_btn")
        sizePolicy.setHeightForWidth(self.logo_btn.sizePolicy().hasHeightForWidth())
        self.logo_btn.setSizePolicy(sizePolicy)
        self.logo_btn.setMinimumSize(QSize(80, 0))
        self.logo_btn.setMaximumSize(QSize(80, 16777215))
        self.logo_btn.setStyleSheet(u"background-color: transparent;\n"
"border-radius: 8px;")
        self.logo_btn.setIcon(icon)
        self.logo_btn.setIconSize(QSize(60, 60))
        self.logo_btn.setCheckable(True)

        self.horizontalLayout.addWidget(self.logo_btn)

        self.company_header_layout = QVBoxLayout()
        self.company_header_layout.setObjectName(u"company_header_layout")
        self.company_name = QLabel(self.header_frame)
        self.company_name.setObjectName(u"company_name")
        sizePolicy.setHeightForWidth(self.company_name.sizePolicy().hasHeightForWidth())
        self.company_name.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(35)
        font1.setBold(True)
        self.company_name.setFont(font1)
        self.company_name.setStyleSheet(u"color: #1E293B;")

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
        self.clear_data_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_9.addWidget(self.clear_data_btn)

        self.new_data_btn = QPushButton(self.widget_56)
        self.new_data_btn.setObjectName(u"new_data_btn")
        sizePolicy.setHeightForWidth(self.new_data_btn.sizePolicy().hasHeightForWidth())
        self.new_data_btn.setSizePolicy(sizePolicy)
        self.new_data_btn.setFont(font7)
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
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(10, 0, 5, 0)

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
        font9 = QFont()
        font9.setFamilies([u"Segoe UI"])
        font9.setPointSize(15)
        font9.setBold(True)
        self.connection_group.setFont(font9)
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
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setContentsMargins(10, 15, 10, 15)
        self.read_plc_label = QPushButton(self.connection_group)
        self.read_plc_label.setObjectName(u"read_plc_label")
        sizePolicy.setHeightForWidth(self.read_plc_label.sizePolicy().hasHeightForWidth())
        self.read_plc_label.setSizePolicy(sizePolicy)
        font10 = QFont()
        font10.setFamilies([u"MS Shell Dlg 2"])
        font10.setPointSize(19)
        font10.setBold(True)
        self.read_plc_label.setFont(font10)
        self.read_plc_label.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: left;\n"
"}")
        self.read_plc_label.setIconSize(QSize(55, 55))
        self.read_plc_label.setCheckable(True)

        self.gridLayout_4.addWidget(self.read_plc_label, 0, 0, 1, 1)

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
        font11 = QFont()
        font11.setPointSize(18)
        font11.setBold(True)
        self.pushButton_4.setFont(font11)
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
        self.pushButton_21.setFont(font11)
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
        self.pushButton_24.setFont(font11)
        self.pushButton_24.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: orange; \n"
"padding-right: 3px;")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/record-button (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_24.setIcon(icon9)
        self.pushButton_24.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.pushButton_24)

        self.sys_state_stacked_wid_40.addWidget(self.page_4)

        self.horizontalLayout_31.addWidget(self.sys_state_stacked_wid_40)

        self.read_time_input = QSpinBox(self.widget_28)
        self.read_time_input.setObjectName(u"read_time_input")
        sizePolicy.setHeightForWidth(self.read_time_input.sizePolicy().hasHeightForWidth())
        self.read_time_input.setSizePolicy(sizePolicy)
        self.read_time_input.setMinimumSize(QSize(0, 0))
        font12 = QFont()
        font12.setFamilies([u"Segoe UI"])
        font12.setPointSize(24)
        font12.setBold(True)
        self.read_time_input.setFont(font12)
        self.read_time_input.setAlignment(Qt.AlignCenter)
        self.read_time_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.read_time_input.setMinimum(100)
        self.read_time_input.setMaximum(1000)
        self.read_time_input.setValue(500)

        self.horizontalLayout_31.addWidget(self.read_time_input)

        self.horizontalLayout_31.setStretch(0, 3)
        self.horizontalLayout_31.setStretch(1, 2)

        self.gridLayout_4.addWidget(self.widget_28, 0, 1, 1, 1)

        self.write_plc_label = QPushButton(self.connection_group)
        self.write_plc_label.setObjectName(u"write_plc_label")
        sizePolicy.setHeightForWidth(self.write_plc_label.sizePolicy().hasHeightForWidth())
        self.write_plc_label.setSizePolicy(sizePolicy)
        self.write_plc_label.setFont(font10)
        self.write_plc_label.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: left;\n"
"}")
        self.write_plc_label.setIconSize(QSize(55, 55))
        self.write_plc_label.setCheckable(True)

        self.gridLayout_4.addWidget(self.write_plc_label, 1, 0, 1, 1)

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
        self.pushButton_6.setFont(font11)
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
        self.pushButton_23.setFont(font11)
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
        self.pushButton_22.setFont(font11)
        self.pushButton_22.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: orange; \n"
"padding-right: 3px;")
        self.pushButton_22.setIcon(icon9)
        self.pushButton_22.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.pushButton_22)

        self.sys_state_stacked_wid_42.addWidget(self.page_3)

        self.horizontalLayout_41.addWidget(self.sys_state_stacked_wid_42)

        self.write_time_input = QSpinBox(self.widget_31)
        self.write_time_input.setObjectName(u"write_time_input")
        sizePolicy.setHeightForWidth(self.write_time_input.sizePolicy().hasHeightForWidth())
        self.write_time_input.setSizePolicy(sizePolicy)
        self.write_time_input.setMinimumSize(QSize(0, 0))
        self.write_time_input.setFont(font12)
        self.write_time_input.setAlignment(Qt.AlignCenter)
        self.write_time_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.write_time_input.setMinimum(300)
        self.write_time_input.setMaximum(1000)
        self.write_time_input.setValue(500)

        self.horizontalLayout_41.addWidget(self.write_time_input)

        self.horizontalLayout_41.setStretch(0, 3)
        self.horizontalLayout_41.setStretch(1, 2)

        self.gridLayout_4.addWidget(self.widget_31, 1, 1, 1, 1)

        self.write_table_label = QPushButton(self.connection_group)
        self.write_table_label.setObjectName(u"write_table_label")
        sizePolicy.setHeightForWidth(self.write_table_label.sizePolicy().hasHeightForWidth())
        self.write_table_label.setSizePolicy(sizePolicy)
        self.write_table_label.setFont(font10)
        self.write_table_label.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: left;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/Icons/to-do-list.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.write_table_label.setIcon(icon10)
        self.write_table_label.setIconSize(QSize(55, 55))
        self.write_table_label.setCheckable(True)

        self.gridLayout_4.addWidget(self.write_table_label, 2, 0, 1, 1)

        self.table_write_cycle = QDoubleSpinBox(self.connection_group)
        self.table_write_cycle.setObjectName(u"table_write_cycle")
        sizePolicy.setHeightForWidth(self.table_write_cycle.sizePolicy().hasHeightForWidth())
        self.table_write_cycle.setSizePolicy(sizePolicy)
        self.table_write_cycle.setMinimumSize(QSize(0, 0))
        self.table_write_cycle.setFont(font12)
        self.table_write_cycle.setAlignment(Qt.AlignCenter)
        self.table_write_cycle.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.table_write_cycle.setDecimals(1)
        self.table_write_cycle.setValue(1.000000000000000)

        self.gridLayout_4.addWidget(self.table_write_cycle, 2, 1, 1, 1)

        self.total_cycle_label = QPushButton(self.connection_group)
        self.total_cycle_label.setObjectName(u"total_cycle_label")
        sizePolicy.setHeightForWidth(self.total_cycle_label.sizePolicy().hasHeightForWidth())
        self.total_cycle_label.setSizePolicy(sizePolicy)
        self.total_cycle_label.setFont(font10)
        self.total_cycle_label.setStyleSheet(u"QPushButton {\n"
"    color: rgb(30, 136, 229);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: left;\n"
"}")
        self.total_cycle_label.setIconSize(QSize(55, 55))
        self.total_cycle_label.setCheckable(True)

        self.gridLayout_4.addWidget(self.total_cycle_label, 3, 0, 1, 1)

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
        font13 = QFont()
        font13.setFamilies([u"Segoe UI"])
        font13.setPointSize(24)
        font13.setBold(True)
        font13.setItalic(False)
        self.cycle_a_displ_3.setFont(font13)
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
        font14 = QFont()
        font14.setFamilies([u"Segoe UI"])
        font14.setPointSize(18)
        font14.setBold(True)
        self.reset_cycle_a_btn.setFont(font14)
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
        icon11 = QIcon()
        icon11.addFile(u":/Icons/broom.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.reset_cycle_a_btn.setIcon(icon11)
        self.reset_cycle_a_btn.setIconSize(QSize(50, 50))

        self.horizontalLayout_44.addWidget(self.reset_cycle_a_btn)

        self.horizontalLayout_44.setStretch(0, 3)
        self.horizontalLayout_44.setStretch(1, 2)

        self.gridLayout_4.addWidget(self.widget_35, 3, 1, 1, 1)

        self.total_cycle_label_2 = QPushButton(self.connection_group)
        self.total_cycle_label_2.setObjectName(u"total_cycle_label_2")
        sizePolicy.setHeightForWidth(self.total_cycle_label_2.sizePolicy().hasHeightForWidth())
        self.total_cycle_label_2.setSizePolicy(sizePolicy)
        self.total_cycle_label_2.setFont(font10)
        self.total_cycle_label_2.setStyleSheet(u"QPushButton {\n"
"    color: rgb(251, 140, 0);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: left;\n"
"}")
        self.total_cycle_label_2.setIconSize(QSize(55, 55))
        self.total_cycle_label_2.setCheckable(True)

        self.gridLayout_4.addWidget(self.total_cycle_label_2, 4, 0, 1, 1)

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
        self.cycle_b_displ_3.setFont(font13)
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
        self.reset_cycle_b_btn.setFont(font14)
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
        self.reset_cycle_b_btn.setIcon(icon11)
        self.reset_cycle_b_btn.setIconSize(QSize(50, 50))

        self.horizontalLayout_46.addWidget(self.reset_cycle_b_btn)

        self.horizontalLayout_46.setStretch(0, 3)
        self.horizontalLayout_46.setStretch(1, 2)

        self.gridLayout_4.addWidget(self.widget_36, 4, 1, 1, 1)

        self.total_cycle_label_3 = QPushButton(self.connection_group)
        self.total_cycle_label_3.setObjectName(u"total_cycle_label_3")
        sizePolicy.setHeightForWidth(self.total_cycle_label_3.sizePolicy().hasHeightForWidth())
        self.total_cycle_label_3.setSizePolicy(sizePolicy)
        self.total_cycle_label_3.setFont(font10)
        self.total_cycle_label_3.setStyleSheet(u"QPushButton {\n"
"    color: #6F00FF;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: left;\n"
"}")
        self.total_cycle_label_3.setIconSize(QSize(55, 55))
        self.total_cycle_label_3.setCheckable(True)

        self.gridLayout_4.addWidget(self.total_cycle_label_3, 5, 0, 1, 1)

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
        self.cycle_c_displ_3.setFont(font13)
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
        self.reset_cycle_c_btn.setFont(font14)
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
        self.reset_cycle_c_btn.setIcon(icon11)
        self.reset_cycle_c_btn.setIconSize(QSize(50, 50))

        self.horizontalLayout_48.addWidget(self.reset_cycle_c_btn)

        self.horizontalLayout_48.setStretch(0, 3)
        self.horizontalLayout_48.setStretch(1, 2)

        self.gridLayout_4.addWidget(self.widget_37, 5, 1, 1, 1)

        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 1)
        self.gridLayout_4.setRowStretch(2, 1)
        self.gridLayout_4.setRowStretch(3, 1)
        self.gridLayout_4.setRowStretch(4, 1)
        self.gridLayout_4.setRowStretch(5, 1)
        self.gridLayout_4.setColumnStretch(1, 1)

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
        self.verticalLayout_28.setContentsMargins(0, 15, 0, 10)
        self.widget_26 = QWidget(self.device_frame_2)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setStyleSheet(u"")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_24.setSpacing(10)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(10, 0, 10, 0)
        self.i_o_group_1 = QGroupBox(self.widget_26)
        self.i_o_group_1.setObjectName(u"i_o_group_1")
        font15 = QFont()
        font15.setFamilies([u"Segoe UI"])
        font15.setPointSize(16)
        font15.setBold(True)
        self.i_o_group_1.setFont(font15)
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
        self.gridLayout_7.setContentsMargins(0, 15, 10, 10)

        self.horizontalLayout_24.addWidget(self.i_o_group_1)

        self.i_o_group_3 = QGroupBox(self.widget_26)
        self.i_o_group_3.setObjectName(u"i_o_group_3")
        self.i_o_group_3.setFont(font15)
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
        self.gridLayout_5.setContentsMargins(0, 15, 10, 10)

        self.horizontalLayout_24.addWidget(self.i_o_group_3)

        self.i_o_group_2 = QGroupBox(self.widget_26)
        self.i_o_group_2.setObjectName(u"i_o_group_2")
        self.i_o_group_2.setFont(font15)
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
        self.gridLayout_6.setSpacing(10)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(10, 15, 10, 10)

        self.horizontalLayout_24.addWidget(self.i_o_group_2)

        self.horizontalLayout_24.setStretch(0, 1)
        self.horizontalLayout_24.setStretch(1, 1)
        self.horizontalLayout_24.setStretch(2, 1)

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
        font16 = QFont()
        font16.setPointSize(20)
        font16.setBold(True)
        self.back_connection_page_btn.setFont(font16)
        self.back_connection_page_btn.setStyleSheet(u"")
        self.back_connection_page_btn.setIconSize(QSize(40, 40))
        self.back_connection_page_btn.setCheckable(False)

        self.horizontalLayout_30.addWidget(self.back_connection_page_btn)

        self.back_home_page_btn = QPushButton(self.widget_30)
        self.back_home_page_btn.setObjectName(u"back_home_page_btn")
        sizePolicy.setHeightForWidth(self.back_home_page_btn.sizePolicy().hasHeightForWidth())
        self.back_home_page_btn.setSizePolicy(sizePolicy)
        self.back_home_page_btn.setMaximumSize(QSize(16777215, 16777215))
        self.back_home_page_btn.setFont(font16)
        self.back_home_page_btn.setStyleSheet(u"")
        self.back_home_page_btn.setIconSize(QSize(40, 40))
        self.back_home_page_btn.setCheckable(False)

        self.horizontalLayout_30.addWidget(self.back_home_page_btn)

        self.horizontalLayout_30.setStretch(0, 1)
        self.horizontalLayout_30.setStretch(1, 1)

        self.horizontalLayout_27.addWidget(self.widget_30)


        self.verticalLayout_28.addWidget(self.widget_29)

        self.verticalLayout_28.setStretch(0, 8)
        self.verticalLayout_28.setStretch(1, 1)

        self.verticalLayout_40.addWidget(self.device_frame_2)

        self.stackedWidget_3.addWidget(self.i_o_page)

        self.ver_layout_device.addWidget(self.stackedWidget_3)


        self.verticalLayout_5.addLayout(self.ver_layout_device)

        self.stackedWidget_2.addWidget(self.device_page)
        self.table_page = QWidget()
        self.table_page.setObjectName(u"table_page")
        self.verticalLayout_13 = QVBoxLayout(self.table_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.dashboard_stacked_widget = QWidget(self.table_page)
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
        self.horizontalLayout_3.setContentsMargins(5, 2, 5, 0)
        self.search_icon = QPushButton(self.widget_2)
        self.search_icon.setObjectName(u"search_icon")
        sizePolicy.setHeightForWidth(self.search_icon.sizePolicy().hasHeightForWidth())
        self.search_icon.setSizePolicy(sizePolicy)
        self.search_icon.setStyleSheet(u"padding: 5px;")
        icon12 = QIcon()
        icon12.addFile(u":/Icons/search_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_icon.setIcon(icon12)
        self.search_icon.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.search_icon)

        self.search_data = QLineEdit(self.widget_2)
        self.search_data.setObjectName(u"search_data")
        sizePolicy.setHeightForWidth(self.search_data.sizePolicy().hasHeightForWidth())
        self.search_data.setSizePolicy(sizePolicy)
        font17 = QFont()
        font17.setPointSize(14)
        font17.setBold(True)
        self.search_data.setFont(font17)
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
        font18 = QFont()
        font18.setPointSize(16)
        font18.setBold(True)
        self.search_data_start_label_2.setFont(font18)
        self.search_data_start_label_2.setStyleSheet(u"QLabel {\n"
"    background-color: transparent; \n"
"	border: none; \n"
"	color: #1e2937;\n"
"	padding: 6px 4px;\n"
"    selection-background-color: #3b82f6;\n"
"    selection-color: #ffffff;\n"
"}")
        self.search_data_start_label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.search_data_start_label_2)

        self.select_group_name = QComboBox(self.multi_search_data)
        self.select_group_name.addItem("")
        self.select_group_name.addItem("")
        self.select_group_name.addItem("")
        self.select_group_name.addItem("")
        self.select_group_name.setObjectName(u"select_group_name")
        sizePolicy.setHeightForWidth(self.select_group_name.sizePolicy().hasHeightForWidth())
        self.select_group_name.setSizePolicy(sizePolicy)
        self.select_group_name.setFont(font15)

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
        self.search_data_start_label.setFont(font18)
        self.search_data_start_label.setStyleSheet(u"QLabel {\n"
"    background-color: transparent; \n"
"	border: none; \n"
"	color: #1e2937;\n"
"	padding: 6px 4px;\n"
"    selection-background-color: #3b82f6;\n"
"    selection-color: #ffffff;\n"
"}")
        self.search_data_start_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.search_data_start_label)

        self.search_data_start_edit = TimeOnlyEdit(self.multi_search_data)
        self.search_data_start_edit.setObjectName(u"search_data_start_edit")
        sizePolicy.setHeightForWidth(self.search_data_start_edit.sizePolicy().hasHeightForWidth())
        self.search_data_start_edit.setSizePolicy(sizePolicy)
        self.search_data_start_edit.setFont(font18)
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
        self.search_data_end_label.setFont(font18)
        self.search_data_end_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.search_data_end_label)

        self.search_data_end_edit = TimeOnlyEdit(self.multi_search_data)
        self.search_data_end_edit.setObjectName(u"search_data_end_edit")
        sizePolicy.setHeightForWidth(self.search_data_end_edit.sizePolicy().hasHeightForWidth())
        self.search_data_end_edit.setSizePolicy(sizePolicy)
        self.search_data_end_edit.setFont(font18)
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
        font19 = QFont()
        font19.setPointSize(13)
        font19.setItalic(True)
        self.label_info.setFont(font19)

        self.horizontalLayout_3.addWidget(self.label_info)

        self.clear_history_search = QPushButton(self.widget_2)
        self.clear_history_search.setObjectName(u"clear_history_search")
        sizePolicy.setHeightForWidth(self.clear_history_search.sizePolicy().hasHeightForWidth())
        self.clear_history_search.setSizePolicy(sizePolicy)
        self.clear_history_search.setMinimumSize(QSize(45, 0))
        icon13 = QIcon()
        icon13.addFile(u":/Icons/circle-xmark.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clear_history_search.setIcon(icon13)
        self.clear_history_search.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.clear_history_search)

        self.list_query_btn = QHBoxLayout()
        self.list_query_btn.setObjectName(u"list_query_btn")
        self.list_query_btn.setContentsMargins(-1, -1, -1, 0)
        self.export_all_tables_to_excel_btn = QPushButton(self.widget_2)
        self.export_all_tables_to_excel_btn.setObjectName(u"export_all_tables_to_excel_btn")
        sizePolicy.setHeightForWidth(self.export_all_tables_to_excel_btn.sizePolicy().hasHeightForWidth())
        self.export_all_tables_to_excel_btn.setSizePolicy(sizePolicy)
        self.export_all_tables_to_excel_btn.setFont(font18)
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
        icon14 = QIcon()
        icon14.addFile(u":/Icons/xlsx-file-format.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.export_all_tables_to_excel_btn.setIcon(icon14)
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
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.list_history.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.list_history.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.list_history.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.list_history.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.list_history.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.list_history.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.list_history.setObjectName(u"list_history")
        self.list_history.setFont(font18)
        self.list_history.setStyleSheet(u"QTableWidget {\n"
"    border: 1px solid #BFC8D3; \n"
"    border-radius: 8px;\n"
"    gridline-color: #BFC8D3; \n"
"    color: #334155;\n"
"    outline: none;\n"
"}\n"
"QTableWidget::item { \n"
"    padding: 8px 14px; \n"
"    border-bottom: 1px solid #f1f5f9;\n"
"}\n"
"QTableWidget::item:selected { \n"
"    background-color: #dbeafe; \n"
"    color: #1e40af; \n"
"}\n"
"QTableWidget::item:hover { \n"
"    background-color: rgb(222, 225, 226); \n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #f8fafc; color: #1e40af; font-family: \"Segoe UI\";\n"
"    font-size: 16px; font-weight: 700; letter-spacing: 1.5px;\n"
"    padding: 10px 14px; border: none; border-bottom: 2px solid #3b82f6;\n"
"    border-right: 1px solid #e2e8f0;\n"
"}\n"
"QHeaderView::section:last { border-right: none; }\n"
"QScrollBar:vertical { background: #f8fafc; width: 20px; border-radius: 4px; }\n"
"QScrollBar::handle:vertical { background: #cbd5e1; border-radius: 4px; min-height: 24px; }\n"
"QScrollBar::handle:vertical:hover { backg"
                        "round: #94a3b8; }\n"
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
        self.list_history.setWordWrap(False)
        self.list_history.horizontalHeader().setCascadingSectionResizes(True)
        self.list_history.horizontalHeader().setMinimumSectionSize(55)
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
        self.list_history_2.setFont(font18)
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

        self.stackedWidget_2.addWidget(self.table_page)

        self.verticalLayout_11.addWidget(self.stackedWidget_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_11)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.body_frame)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(3)
        self.sys_state_stacked_wid_39.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(1)
        self.sys_state_stacked_wid_40.setCurrentIndex(2)
        self.sys_state_stacked_wid_42.setCurrentIndex(2)
        self.stacked_list_history_page.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tech-Link - Strike Machine System", None))
        self.logo_btn.setText("")
        self.company_name.setText(QCoreApplication.translate("MainWindow", u"TECH-LINK", None))
        self.error_display.setText("")
        self.eng_language.setText("")
        self.cn_language.setText("")
        self.date_displ.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy hh:mm:ss", None))
        self.home_page_btn.setText(QCoreApplication.translate("MainWindow", u" First Page", None))
        self.chart_page_btn.setText(QCoreApplication.translate("MainWindow", u" Second Page", None))
        self.device_page_btn.setText(QCoreApplication.translate("MainWindow", u" Third Page", None))
        self.history_page_btn.setText(QCoreApplication.translate("MainWindow", u" Fouth Page", None))
        self.open_side_menu_btn.setText("")
        self.next_group_page_btn.setText("")
        self.stop_light.setText(QCoreApplication.translate("MainWindow", u"Light Off", None))
        self.start_light.setText(QCoreApplication.translate("MainWindow", u"Light On", None))
        self.clear_data_btn.setText(QCoreApplication.translate("MainWindow", u" Button", None))
        self.new_data_btn.setText(QCoreApplication.translate("MainWindow", u" Button", None))
        self.plc_io_btn.setText("")
        self.connection_group.setTitle(QCoreApplication.translate("MainWindow", u"Connection Settings", None))
        self.read_plc_label.setText(QCoreApplication.translate("MainWindow", u" PLC Read:", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Online", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Offline", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Try Connecting...", None))
        self.read_time_input.setSuffix(QCoreApplication.translate("MainWindow", u" ms", None))
        self.write_plc_label.setText(QCoreApplication.translate("MainWindow", u" PLC Write:", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Online", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Offline", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Try Connecting...", None))
        self.write_time_input.setSuffix(QCoreApplication.translate("MainWindow", u" ms", None))
        self.write_table_label.setText(QCoreApplication.translate("MainWindow", u" History Cycle:", None))
        self.table_write_cycle.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.total_cycle_label.setText(QCoreApplication.translate("MainWindow", u" Total Test Time A:", None))
        self.cycle_a_displ_3.setSuffix("")
        self.cycle_a_displ_3.setPrefix("")
        self.reset_cycle_a_btn.setText("")
        self.total_cycle_label_2.setText(QCoreApplication.translate("MainWindow", u" Total Test Time B:", None))
        self.cycle_b_displ_3.setSuffix("")
        self.cycle_b_displ_3.setPrefix("")
        self.reset_cycle_b_btn.setText("")
        self.total_cycle_label_3.setText(QCoreApplication.translate("MainWindow", u" Total Test Time C:", None))
        self.cycle_c_displ_3.setSuffix("")
        self.cycle_c_displ_3.setPrefix("")
        self.reset_cycle_c_btn.setText("")
        self.i_o_group_1.setTitle(QCoreApplication.translate("MainWindow", u"Group Box", None))
        self.i_o_group_3.setTitle(QCoreApplication.translate("MainWindow", u"Group Box", None))
        self.i_o_group_2.setTitle(QCoreApplication.translate("MainWindow", u"Group Box", None))
        self.back_connection_page_btn.setText(QCoreApplication.translate("MainWindow", u"Previus Page", None))
        self.back_home_page_btn.setText(QCoreApplication.translate("MainWindow", u"Next Page", None))
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
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Header 1.", None))
        ___qtablewidgetitem1 = self.list_history.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Header 2.", None))
        ___qtablewidgetitem2 = self.list_history.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Header 3.", None))
        ___qtablewidgetitem3 = self.list_history.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Header 4.", None))
        ___qtablewidgetitem4 = self.list_history.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Header 5.", None))
        ___qtablewidgetitem5 = self.list_history.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Header 6.", None))
        ___qtablewidgetitem6 = self.list_history.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Header 7.", None))
        ___qtablewidgetitem7 = self.list_history.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Header 8.", None))
        ___qtablewidgetitem8 = self.list_history.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Header 9.", None))
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


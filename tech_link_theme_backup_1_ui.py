# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tech_link_theme_backup_1.ui'
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
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
import Icon_rc
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1024, 720))
        MainWindow.setMaximumSize(QSize(1300, 1050))
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/newPrefix/Logo_Cty_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #d1d3d3,\n"
"        stop:1 #c3c7cc);\n"
"}\n"
"QDoubleSpinBox:hover{\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QSpinBox:hover{\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"\n"
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
"    selection-colo"
                        "r: black;\n"
"    padding: 4px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1024, 720))
        self.centralwidget.setMaximumSize(QSize(1300, 1050))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        sizePolicy.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy)
        self.header_frame.setMinimumSize(QSize(0, 50))
        self.header_frame.setMaximumSize(QSize(16777215, 200))
        self.header_frame.setStyleSheet(u"QFrame {\n"
"    background-color: white;\n"
"\n"
"    border: none;\n"
"}")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 5, 5, 5)
        self.logo_frame = QFrame(self.header_frame)
        self.logo_frame.setObjectName(u"logo_frame")
        sizePolicy.setHeightForWidth(self.logo_frame.sizePolicy().hasHeightForWidth())
        self.logo_frame.setSizePolicy(sizePolicy)
        self.logo_frame.setMinimumSize(QSize(40, 35))
        self.logo_frame.setMaximumSize(QSize(16777215, 16777215))
        self.logo_frame.setStyleSheet(u"QFrame {\n"
"    background-color: transparent;\n"
"    border-radius: 8px;\n"
"    image: url(:/newPrefix/Logo_Cty_2.png);\n"
"}")
        self.logo_frame.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout.addWidget(self.logo_frame)

        self.company_header_layout = QVBoxLayout()
        self.company_header_layout.setObjectName(u"company_header_layout")
        self.company_name = QLabel(self.header_frame)
        self.company_name.setObjectName(u"company_name")
        sizePolicy.setHeightForWidth(self.company_name.sizePolicy().hasHeightForWidth())
        self.company_name.setSizePolicy(sizePolicy)
        self.company_name.setStyleSheet(u"    font-size: 26px;\n"
"    font-weight: bold;\n"
"    color: #1E293B;\n"
"    letter-spacing: 1px;")

        self.company_header_layout.addWidget(self.company_name)


        self.horizontalLayout.addLayout(self.company_header_layout)

        self.pc_inform_label = QVBoxLayout()
        self.pc_inform_label.setObjectName(u"pc_inform_label")
        self.horizontalSpacer_4 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.pc_inform_label.addItem(self.horizontalSpacer_4)


        self.horizontalLayout.addLayout(self.pc_inform_label)

        self.language_switch_layout = QHBoxLayout()
        self.language_switch_layout.setObjectName(u"language_switch_layout")
        self.label = QLabel(self.header_frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.language_switch_layout.addWidget(self.label)

        self.language_selection_combox = QComboBox(self.header_frame)
        self.language_selection_combox.addItem("")
        self.language_selection_combox.addItem("")
        self.language_selection_combox.setObjectName(u"language_selection_combox")
        sizePolicy.setHeightForWidth(self.language_selection_combox.sizePolicy().hasHeightForWidth())
        self.language_selection_combox.setSizePolicy(sizePolicy)
        self.language_selection_combox.setFont(font1)
        self.language_selection_combox.setStyleSheet(u"")

        self.language_switch_layout.addWidget(self.language_selection_combox)

        self.language_switch_layout.setStretch(0, 1)

        self.horizontalLayout.addLayout(self.language_switch_layout)

        self.date_displ = QDateTimeEdit(self.header_frame)
        self.date_displ.setObjectName(u"date_displ")
        sizePolicy.setHeightForWidth(self.date_displ.sizePolicy().hasHeightForWidth())
        self.date_displ.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.date_displ.setFont(font2)
        self.date_displ.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"")
        self.date_displ.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.date_displ.setReadOnly(True)
        self.date_displ.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date_displ.setDateTime(QDateTime(QDate(2026, 1, 1), QTime(0, 0, 0)))
        self.date_displ.setMaximumTime(QTime(23, 59, 59))
        self.date_displ.setTimeSpec(Qt.TimeZone)

        self.horizontalLayout.addWidget(self.date_displ)

        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout.addWidget(self.header_frame)

        self.body_frame = QFrame(self.centralwidget)
        self.body_frame.setObjectName(u"body_frame")
        sizePolicy.setHeightForWidth(self.body_frame.sizePolicy().hasHeightForWidth())
        self.body_frame.setSizePolicy(sizePolicy)
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
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 25, 0, 10)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.home_page_btn = QPushButton(self.left_side_menu_widget)
        self.left_side_buttonGroup = QButtonGroup(MainWindow)
        self.left_side_buttonGroup.setObjectName(u"left_side_buttonGroup")
        self.left_side_buttonGroup.addButton(self.home_page_btn)
        self.home_page_btn.setObjectName(u"home_page_btn")
        sizePolicy.setHeightForWidth(self.home_page_btn.sizePolicy().hasHeightForWidth())
        self.home_page_btn.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.home_page_btn.setFont(font3)
        self.home_page_btn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/home_off.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/newPrefix/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.home_page_btn.setIcon(icon1)
        self.home_page_btn.setIconSize(QSize(30, 30))
        self.home_page_btn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.home_page_btn)

        self.pressure_page_btn = QPushButton(self.left_side_menu_widget)
        self.left_side_buttonGroup.addButton(self.pressure_page_btn)
        self.pressure_page_btn.setObjectName(u"pressure_page_btn")
        sizePolicy.setHeightForWidth(self.pressure_page_btn.sizePolicy().hasHeightForWidth())
        self.pressure_page_btn.setSizePolicy(sizePolicy)
        self.pressure_page_btn.setFont(font3)
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/filter.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/newPrefix/filter_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pressure_page_btn.setIcon(icon2)
        self.pressure_page_btn.setIconSize(QSize(30, 30))
        self.pressure_page_btn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pressure_page_btn)

        self.temperature_page_btn = QPushButton(self.left_side_menu_widget)
        self.left_side_buttonGroup.addButton(self.temperature_page_btn)
        self.temperature_page_btn.setObjectName(u"temperature_page_btn")
        sizePolicy.setHeightForWidth(self.temperature_page_btn.sizePolicy().hasHeightForWidth())
        self.temperature_page_btn.setSizePolicy(sizePolicy)
        self.temperature_page_btn.setFont(font3)
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/oven.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/newPrefix/oven_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.temperature_page_btn.setIcon(icon3)
        self.temperature_page_btn.setIconSize(QSize(30, 30))
        self.temperature_page_btn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.temperature_page_btn)

        self.device_page_btn = QPushButton(self.left_side_menu_widget)
        self.left_side_buttonGroup.addButton(self.device_page_btn)
        self.device_page_btn.setObjectName(u"device_page_btn")
        sizePolicy.setHeightForWidth(self.device_page_btn.sizePolicy().hasHeightForWidth())
        self.device_page_btn.setSizePolicy(sizePolicy)
        self.device_page_btn.setFont(font3)
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/newPrefix/settings (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.device_page_btn.setIcon(icon4)
        self.device_page_btn.setIconSize(QSize(30, 30))
        self.device_page_btn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.device_page_btn)

        self.chart_page_btn = QPushButton(self.left_side_menu_widget)
        self.left_side_buttonGroup.addButton(self.chart_page_btn)
        self.chart_page_btn.setObjectName(u"chart_page_btn")
        sizePolicy.setHeightForWidth(self.chart_page_btn.sizePolicy().hasHeightForWidth())
        self.chart_page_btn.setSizePolicy(sizePolicy)
        self.chart_page_btn.setFont(font3)
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/stats.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/newPrefix/stats (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.chart_page_btn.setIcon(icon5)
        self.chart_page_btn.setIconSize(QSize(30, 30))
        self.chart_page_btn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.chart_page_btn)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.open_side_menu_btn = QPushButton(self.left_side_menu_widget)
        self.open_side_menu_btn.setObjectName(u"open_side_menu_btn")
        sizePolicy.setHeightForWidth(self.open_side_menu_btn.sizePolicy().hasHeightForWidth())
        self.open_side_menu_btn.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.open_side_menu_btn.setFont(font4)
        self.open_side_menu_btn.setLayoutDirection(Qt.LeftToRight)
        self.open_side_menu_btn.setStyleSheet(u"text-align: center;")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/align-justify.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.open_side_menu_btn.setIcon(icon6)
        self.open_side_menu_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.open_side_menu_btn)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 2)

        self.horizontalLayout_2.addWidget(self.left_side_menu_widget)

        self.stackedWidget = QStackedWidget(self.body_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QStackedWidget {\n"
"    border: none;\n"
"}")
        self.menu_page = QWidget()
        self.menu_page.setObjectName(u"menu_page")
        self.menu_page.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.menu_page)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 5, 5)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.card_frame_6 = QFrame(self.menu_page)
        self.card_frame_6.setObjectName(u"card_frame_6")
        self.card_frame_6.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B7EC8;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 8px 18px;\n"
"    border-radius: 6px;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0968A3;\n"
"}")
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

        self.card_frame_9 = QFrame(self.menu_page)
        self.card_frame_9.setObjectName(u"card_frame_9")
        self.card_frame_9.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B7EC8;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 8px 18px;\n"
"    border-radius: 6px;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0968A3;\n"
"}")
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

        self.card_frame_8 = QFrame(self.menu_page)
        self.card_frame_8.setObjectName(u"card_frame_8")
        self.card_frame_8.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B7EC8;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 8px 18px;\n"
"    border-radius: 6px;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0968A3;\n"
"}")
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

        self.card_frame_7 = QFrame(self.menu_page)
        self.card_frame_7.setObjectName(u"card_frame_7")
        self.card_frame_7.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B7EC8;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 8px 18px;\n"
"    border-radius: 6px;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0968A3;\n"
"}")
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


        self.verticalLayout_5.addLayout(self.gridLayout_2)

        self.stackedWidget.addWidget(self.menu_page)
        self.pressure_page = QWidget()
        self.pressure_page.setObjectName(u"pressure_page")
        self.verticalLayout_6 = QVBoxLayout(self.pressure_page)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(3, 0, 0, 3)
        self.stacked_pressure_page = QStackedWidget(self.pressure_page)
        self.stacked_pressure_page.setObjectName(u"stacked_pressure_page")
        self.pressure_layout = QWidget()
        self.pressure_layout.setObjectName(u"pressure_layout")
        self.pressure_layout.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}\n"
"")
        self.verticalLayout_10 = QVBoxLayout(self.pressure_layout)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 5, 0, 0)
        self.pressure_page_header = QWidget(self.pressure_layout)
        self.pressure_page_header.setObjectName(u"pressure_page_header")
        self.pressure_page_header.setMaximumSize(QSize(16777215, 75))
        self.pressure_page_header.setStyleSheet(u"background-color: white;\n"
"border-radius:15px;")
        self.verticalLayout_38 = QVBoxLayout(self.pressure_page_header)
        self.verticalLayout_38.setSpacing(5)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 5, 0, 5)
        self.widget_63 = QWidget(self.pressure_page_header)
        self.widget_63.setObjectName(u"widget_63")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_63)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.stacked_group_name = QStackedWidget(self.widget_63)
        self.stacked_group_name.setObjectName(u"stacked_group_name")
        self.group_a_page = QWidget()
        self.group_a_page.setObjectName(u"group_a_page")
        self.horizontalLayout_23 = QHBoxLayout(self.group_a_page)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_126 = QLabel(self.group_a_page)
        self.label_126.setObjectName(u"label_126")
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        self.label_126.setFont(font5)
        self.label_126.setStyleSheet(u"padding-left: 20px;\n"
"padding-right: 20px;\n"
"color: rgb(0, 0, 0);")
        self.label_126.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.label_126)

        self.stacked_group_name.addWidget(self.group_a_page)
        self.group_b_page = QWidget()
        self.group_b_page.setObjectName(u"group_b_page")
        self.horizontalLayout_24 = QHBoxLayout(self.group_b_page)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_127 = QLabel(self.group_b_page)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setFont(font5)
        self.label_127.setStyleSheet(u"padding-left: 20px;\n"
"padding-right: 20px;\n"
"color: rgb(0, 0, 0);")
        self.label_127.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.label_127)

        self.stacked_group_name.addWidget(self.group_b_page)
        self.group_c_page = QWidget()
        self.group_c_page.setObjectName(u"group_c_page")
        self.horizontalLayout_25 = QHBoxLayout(self.group_c_page)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_129 = QLabel(self.group_c_page)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setFont(font5)
        self.label_129.setStyleSheet(u"padding-left: 20px;\n"
"padding-right: 20px;\n"
"color: rgb(0, 0, 0);")
        self.label_129.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.label_129)

        self.stacked_group_name.addWidget(self.group_c_page)

        self.horizontalLayout_15.addWidget(self.stacked_group_name)

        self.sys_state_stacked_wid_10 = QStackedWidget(self.widget_63)
        self.sys_state_stacked_wid_10.setObjectName(u"sys_state_stacked_wid_10")
        sizePolicy.setHeightForWidth(self.sys_state_stacked_wid_10.sizePolicy().hasHeightForWidth())
        self.sys_state_stacked_wid_10.setSizePolicy(sizePolicy)
        self.running_light = QWidget()
        self.running_light.setObjectName(u"running_light")
        self.horizontalLayout_97 = QHBoxLayout(self.running_light)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.running_label = QLabel(self.running_light)
        self.running_label.setObjectName(u"running_label")
        sizePolicy.setHeightForWidth(self.running_label.sizePolicy().hasHeightForWidth())
        self.running_label.setSizePolicy(sizePolicy)
        self.running_label.setStyleSheet(u"font-size: 14px; \n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #10B981; \n"
"font-weight: 500; \n"
"padding-right: 3px;")

        self.horizontalLayout_97.addWidget(self.running_label)

        self.sys_state_stacked_wid_10.addWidget(self.running_light)
        self.stop_light = QWidget()
        self.stop_light.setObjectName(u"stop_light")
        self.horizontalLayout_99 = QHBoxLayout(self.stop_light)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.stop_label = QLabel(self.stop_light)
        self.stop_label.setObjectName(u"stop_label")
        sizePolicy.setHeightForWidth(self.stop_label.sizePolicy().hasHeightForWidth())
        self.stop_label.setSizePolicy(sizePolicy)
        self.stop_label.setStyleSheet(u"font-size: 14px; \n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #F90A0A; \n"
"font-weight: 500; \n"
"padding-right: 3px;")

        self.horizontalLayout_99.addWidget(self.stop_label)

        self.sys_state_stacked_wid_10.addWidget(self.stop_light)

        self.horizontalLayout_15.addWidget(self.sys_state_stacked_wid_10)

        self.widget_9 = QWidget(self.widget_63)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMaximumSize(QSize(16777215, 100))
        self.widget_9.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #0B7EC8;\n"
"    border: 2px solid #0B7EC8;\n"
"    padding: 12px 12px;\n"
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
        self.previus_group_page_btn = QPushButton(self.widget_9)
        self.previus_group_page_btn.setObjectName(u"previus_group_page_btn")
        sizePolicy.setHeightForWidth(self.previus_group_page_btn.sizePolicy().hasHeightForWidth())
        self.previus_group_page_btn.setSizePolicy(sizePolicy)
        self.previus_group_page_btn.setMaximumSize(QSize(16777215, 150))
        font6 = QFont()
        font6.setBold(True)
        self.previus_group_page_btn.setFont(font6)
        self.previus_group_page_btn.setStyleSheet(u"QPushButton{\n"
"	image: url(:/newPrefix/arrow-alt-circle-left.png);\n"
"}\n"
"QPushButton:pressed{\n"
"	image: url(:/newPrefix/arrow-alt-circle-left_blue.png)\n"
"}")
        self.previus_group_page_btn.setIconSize(QSize(40, 40))
        self.previus_group_page_btn.setCheckable(False)

        self.horizontalLayout_29.addWidget(self.previus_group_page_btn)

        self.next_group_page_btn = QPushButton(self.widget_9)
        self.next_group_page_btn.setObjectName(u"next_group_page_btn")
        sizePolicy.setHeightForWidth(self.next_group_page_btn.sizePolicy().hasHeightForWidth())
        self.next_group_page_btn.setSizePolicy(sizePolicy)
        self.next_group_page_btn.setMaximumSize(QSize(16777215, 150))
        self.next_group_page_btn.setFont(font6)
        self.next_group_page_btn.setStyleSheet(u"QPushButton{\n"
"	image: url(:/newPrefix/arrow-alt-circle-right.png)\n"
"}\n"
"QPushButton:pressed{\n"
"	image: url(:/newPrefix/arrow-alt-circle-right_blue.png)\n"
"}")
        self.next_group_page_btn.setIconSize(QSize(40, 40))
        self.next_group_page_btn.setCheckable(False)

        self.horizontalLayout_29.addWidget(self.next_group_page_btn)

        self.horizontalLayout_29.setStretch(0, 1)
        self.horizontalLayout_29.setStretch(1, 1)

        self.horizontalLayout_15.addWidget(self.widget_9)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)

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
        font7.setPointSize(12)
        font7.setBold(True)
        self.clear_data_btn.setFont(font7)
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/data-cleaning.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clear_data_btn.setIcon(icon7)

        self.horizontalLayout_9.addWidget(self.clear_data_btn)

        self.save_data_btn = QPushButton(self.widget_56)
        self.save_data_btn.setObjectName(u"save_data_btn")
        sizePolicy.setHeightForWidth(self.save_data_btn.sizePolicy().hasHeightForWidth())
        self.save_data_btn.setSizePolicy(sizePolicy)
        self.save_data_btn.setFont(font7)
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/folder-upload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save_data_btn.setIcon(icon8)

        self.horizontalLayout_9.addWidget(self.save_data_btn)


        self.horizontalLayout_15.addWidget(self.widget_56)

        self.stacked_group_combox = QStackedWidget(self.widget_63)
        self.stacked_group_combox.setObjectName(u"stacked_group_combox")
        self.group_a_combox = QWidget()
        self.group_a_combox.setObjectName(u"group_a_combox")
        self.verticalLayout_17 = QVBoxLayout(self.group_a_combox)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.data_selection_combobox_a = QComboBox(self.group_a_combox)
        self.data_selection_combobox_a.addItem("")
        self.data_selection_combobox_a.setObjectName(u"data_selection_combobox_a")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.data_selection_combobox_a.sizePolicy().hasHeightForWidth())
        self.data_selection_combobox_a.setSizePolicy(sizePolicy1)
        self.data_selection_combobox_a.setMinimumSize(QSize(0, 40))
        font8 = QFont()
        font8.setPointSize(11)
        font8.setBold(True)
        self.data_selection_combobox_a.setFont(font8)
        self.data_selection_combobox_a.setStyleSheet(u"")
        self.data_selection_combobox_a.setIconSize(QSize(35, 35))

        self.verticalLayout_17.addWidget(self.data_selection_combobox_a)

        self.stacked_group_combox.addWidget(self.group_a_combox)
        self.group_b_combox = QWidget()
        self.group_b_combox.setObjectName(u"group_b_combox")
        self.verticalLayout_35 = QVBoxLayout(self.group_b_combox)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.data_selection_combobox_b = QComboBox(self.group_b_combox)
        self.data_selection_combobox_b.addItem("")
        self.data_selection_combobox_b.setObjectName(u"data_selection_combobox_b")
        sizePolicy1.setHeightForWidth(self.data_selection_combobox_b.sizePolicy().hasHeightForWidth())
        self.data_selection_combobox_b.setSizePolicy(sizePolicy1)
        self.data_selection_combobox_b.setMinimumSize(QSize(0, 40))
        self.data_selection_combobox_b.setFont(font8)
        self.data_selection_combobox_b.setStyleSheet(u"")
        self.data_selection_combobox_b.setIconSize(QSize(35, 35))

        self.verticalLayout_35.addWidget(self.data_selection_combobox_b)

        self.stacked_group_combox.addWidget(self.group_b_combox)
        self.group_c_combox = QWidget()
        self.group_c_combox.setObjectName(u"group_c_combox")
        self.verticalLayout_33 = QVBoxLayout(self.group_c_combox)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.data_selection_combobox_c = QComboBox(self.group_c_combox)
        self.data_selection_combobox_c.addItem("")
        self.data_selection_combobox_c.setObjectName(u"data_selection_combobox_c")
        sizePolicy1.setHeightForWidth(self.data_selection_combobox_c.sizePolicy().hasHeightForWidth())
        self.data_selection_combobox_c.setSizePolicy(sizePolicy1)
        self.data_selection_combobox_c.setMinimumSize(QSize(0, 40))
        self.data_selection_combobox_c.setFont(font8)
        self.data_selection_combobox_c.setStyleSheet(u"")
        self.data_selection_combobox_c.setIconSize(QSize(35, 35))

        self.verticalLayout_33.addWidget(self.data_selection_combobox_c)

        self.stacked_group_combox.addWidget(self.group_c_combox)

        self.horizontalLayout_15.addWidget(self.stacked_group_combox)


        self.verticalLayout_38.addWidget(self.widget_63)


        self.verticalLayout_10.addWidget(self.pressure_page_header)

        self.widget_pressure_time = QWidget(self.pressure_layout)
        self.widget_pressure_time.setObjectName(u"widget_pressure_time")
        self.widget_pressure_time.setStyleSheet(u"background-color: white;\n"
"border-radius: 15px;")
        self.verticalLayout_63 = QVBoxLayout(self.widget_pressure_time)
        self.verticalLayout_63.setSpacing(10)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 5, 0, 0)
        self.widget_18 = QWidget(self.widget_pressure_time)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_61 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_61.setSpacing(10)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.widget_18)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setFont(font)
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 837, 50))
        self.scrollAreaWidgetContents_3.setMinimumSize(QSize(690, 0))
        self.horizontalLayout_16 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(15, 0, 0, 0)
        self.widget_19 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_39 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_39.setSpacing(10)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.widget_19)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setFont(font1)
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/filters(1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon9)
        self.pushButton_6.setIconSize(QSize(30, 30))

        self.horizontalLayout_39.addWidget(self.pushButton_6)


        self.horizontalLayout_16.addWidget(self.widget_19)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_3)

        self.widget_6 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(290, 0))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_17.setSpacing(10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_102 = QLabel(self.widget_6)
        self.label_102.setObjectName(u"label_102")
        sizePolicy.setHeightForWidth(self.label_102.sizePolicy().hasHeightForWidth())
        self.label_102.setSizePolicy(sizePolicy)
        font9 = QFont()
        font9.setPointSize(12)
        font9.setBold(True)
        font9.setItalic(False)
        self.label_102.setFont(font9)
        self.label_102.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-left: 20px;")
        self.label_102.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_102)

        self.spinBox_2 = QSpinBox(self.widget_6)
        self.spinBox_2.setObjectName(u"spinBox_2")
        sizePolicy.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy)
        self.spinBox_2.setFont(font7)
        self.spinBox_2.setStyleSheet(u"")
        self.spinBox_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.spinBox_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_2.setMaximum(999999999)

        self.horizontalLayout_17.addWidget(self.spinBox_2)


        self.horizontalLayout_16.addWidget(self.widget_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_2)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_61.addWidget(self.scrollArea_3)


        self.verticalLayout_63.addWidget(self.widget_18)

        self.widget_46 = QWidget(self.widget_pressure_time)
        self.widget_46.setObjectName(u"widget_46")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_35.setSpacing(15)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_7 = QScrollArea(self.widget_46)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        sizePolicy.setHeightForWidth(self.scrollArea_7.sizePolicy().hasHeightForWidth())
        self.scrollArea_7.setSizePolicy(sizePolicy)
        self.scrollArea_7.setStyleSheet(u"QScrollArea{\n"
"	border-radius: 10px;\n"
"}\n"
"QFrame {\n"
"    background-color: #F8FAFC;\n"
"    border-left: 4px solid #43A047;\n"
"    border-radius: 6px;\n"
"}\n"
"QStackedWidget {\n"
"	border: none;\n"
"}")
        self.scrollArea_7.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_7.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 812, 236))
        self.scrollAreaWidgetContents_7.setStyleSheet(u"\n"
"    background-color: white;\n"
"	padding: 2px;\n"
"")
        self.verticalLayout_64 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 5, 0)
        self.widget_10 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"border: none;")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_36.setSpacing(5)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.widget_90 = QWidget(self.widget_10)
        self.widget_90.setObjectName(u"widget_90")
        self.widget_90.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_94 = QHBoxLayout(self.widget_90)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(15, 0, 15, 0)
        self.label_112 = QLabel(self.widget_90)
        self.label_112.setObjectName(u"label_112")
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        font10.setPointSize(13)
        font10.setBold(True)
        font10.setItalic(False)
        self.label_112.setFont(font10)

        self.horizontalLayout_94.addWidget(self.label_112)


        self.horizontalLayout_36.addWidget(self.widget_90)

        self.widget_139 = QWidget(self.widget_10)
        self.widget_139.setObjectName(u"widget_139")
        self.widget_139.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_128 = QHBoxLayout(self.widget_139)
        self.horizontalLayout_128.setSpacing(10)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.horizontalLayout_128.setContentsMargins(18, 15, 10, 5)
        self.widget_51 = QWidget(self.widget_139)
        self.widget_51.setObjectName(u"widget_51")
        self.widget_51.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout_125 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_125.setSpacing(0)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalLayout_125.setContentsMargins(2, 2, 2, 2)
        self.refuel_start_time_input = QDoubleSpinBox(self.widget_51)
        self.refuel_start_time_input.setObjectName(u"refuel_start_time_input")
        sizePolicy1.setHeightForWidth(self.refuel_start_time_input.sizePolicy().hasHeightForWidth())
        self.refuel_start_time_input.setSizePolicy(sizePolicy1)
        font11 = QFont()
        font11.setFamilies([u"Segoe UI"])
        font11.setPointSize(14)
        font11.setBold(True)
        font11.setItalic(False)
        self.refuel_start_time_input.setFont(font11)
        self.refuel_start_time_input.setStyleSheet(u"")
        self.refuel_start_time_input.setAlignment(Qt.AlignCenter)
        self.refuel_start_time_input.setReadOnly(False)
        self.refuel_start_time_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.refuel_start_time_input.setDecimals(1)
        self.refuel_start_time_input.setMaximum(999.000000000000000)
        self.refuel_start_time_input.setValue(0.000000000000000)

        self.horizontalLayout_125.addWidget(self.refuel_start_time_input)

        self.label_25 = QLabel(self.widget_51)
        self.label_25.setObjectName(u"label_25")
        font12 = QFont()
        font12.setFamilies([u"Segoe UI"])
        font12.setPointSize(15)
        font12.setBold(True)
        self.label_25.setFont(font12)
        self.label_25.setStyleSheet(u"border: none;\n"
"")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_125.addWidget(self.label_25)

        self.refuel_end_time_input = QDoubleSpinBox(self.widget_51)
        self.refuel_end_time_input.setObjectName(u"refuel_end_time_input")
        sizePolicy1.setHeightForWidth(self.refuel_end_time_input.sizePolicy().hasHeightForWidth())
        self.refuel_end_time_input.setSizePolicy(sizePolicy1)
        self.refuel_end_time_input.setFont(font11)
        self.refuel_end_time_input.setStyleSheet(u"")
        self.refuel_end_time_input.setAlignment(Qt.AlignCenter)
        self.refuel_end_time_input.setReadOnly(False)
        self.refuel_end_time_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.refuel_end_time_input.setDecimals(1)
        self.refuel_end_time_input.setMaximum(999.000000000000000)
        self.refuel_end_time_input.setValue(999.000000000000000)

        self.horizontalLayout_125.addWidget(self.refuel_end_time_input)


        self.horizontalLayout_128.addWidget(self.widget_51)

        self.horizontalLayout_128.setStretch(0, 2)

        self.horizontalLayout_36.addWidget(self.widget_139)


        self.verticalLayout_64.addWidget(self.widget_10)

        self.widget_48 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_48.setObjectName(u"widget_48")
        sizePolicy1.setHeightForWidth(self.widget_48.sizePolicy().hasHeightForWidth())
        self.widget_48.setSizePolicy(sizePolicy1)
        self.widget_48.setStyleSheet(u"")
        self.horizontalLayout_95 = QHBoxLayout(self.widget_48)
        self.horizontalLayout_95.setSpacing(5)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, 0, 10, 0)
        self.widget_80 = QWidget(self.widget_48)
        self.widget_80.setObjectName(u"widget_80")
        sizePolicy.setHeightForWidth(self.widget_80.sizePolicy().hasHeightForWidth())
        self.widget_80.setSizePolicy(sizePolicy)
        self.verticalLayout_65 = QVBoxLayout(self.widget_80)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.widget_81 = QWidget(self.widget_80)
        self.widget_81.setObjectName(u"widget_81")
        self.widget_81.setStyleSheet(u"border-left: None;\n"
"border-radius: 5px;")
        self.verticalLayout_66 = QVBoxLayout(self.widget_81)
        self.verticalLayout_66.setSpacing(10)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(5, 0, 0, 0)
        self.widget_47 = QWidget(self.widget_81)
        self.widget_47.setObjectName(u"widget_47")
        self.verticalLayout_67 = QVBoxLayout(self.widget_47)
        self.verticalLayout_67.setSpacing(15)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(10, 10, 10, 10)
        self.widget_91 = QWidget(self.widget_47)
        self.widget_91.setObjectName(u"widget_91")
        self.widget_91.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_96 = QHBoxLayout(self.widget_91)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(0, 0, 5, 0)
        self.label_113 = QLabel(self.widget_91)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setFont(font10)

        self.horizontalLayout_96.addWidget(self.label_113)


        self.verticalLayout_67.addWidget(self.widget_91)

        self.widget_92 = QWidget(self.widget_47)
        self.widget_92.setObjectName(u"widget_92")
        self.widget_92.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_123 = QHBoxLayout(self.widget_92)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalLayout_123.setContentsMargins(0, 0, 5, 0)
        self.label_114 = QLabel(self.widget_92)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setFont(font10)

        self.horizontalLayout_123.addWidget(self.label_114)


        self.verticalLayout_67.addWidget(self.widget_92)

        self.widget_93 = QWidget(self.widget_47)
        self.widget_93.setObjectName(u"widget_93")
        self.widget_93.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_131 = QHBoxLayout(self.widget_93)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_131.setContentsMargins(0, 0, 5, 0)
        self.label_115 = QLabel(self.widget_93)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setFont(font10)

        self.horizontalLayout_131.addWidget(self.label_115)


        self.verticalLayout_67.addWidget(self.widget_93)


        self.verticalLayout_66.addWidget(self.widget_47)


        self.verticalLayout_65.addWidget(self.widget_81)


        self.horizontalLayout_95.addWidget(self.widget_80)

        self.widget_49 = QWidget(self.widget_48)
        self.widget_49.setObjectName(u"widget_49")
        self.widget_49.setStyleSheet(u"border-left: None;")
        self.verticalLayout_68 = QVBoxLayout(self.widget_49)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.widget_50 = QWidget(self.widget_49)
        self.widget_50.setObjectName(u"widget_50")
        self.widget_50.setMinimumSize(QSize(175, 0))
        self.widget_50.setMaximumSize(QSize(275, 16777215))
        self.widget_50.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QSpinBox:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}")
        self.verticalLayout_69 = QVBoxLayout(self.widget_50)
        self.verticalLayout_69.setSpacing(15)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 10, 0, 10)
        self.widget_142 = QWidget(self.widget_50)
        self.widget_142.setObjectName(u"widget_142")
        self.widget_142.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_132 = QHBoxLayout(self.widget_142)
        self.horizontalLayout_132.setSpacing(10)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalLayout_132.setContentsMargins(10, 0, 0, 0)
        self.widget_52 = QWidget(self.widget_142)
        self.widget_52.setObjectName(u"widget_52")
        self.widget_52.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout_134 = QHBoxLayout(self.widget_52)
        self.horizontalLayout_134.setSpacing(0)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.horizontalLayout_134.setContentsMargins(2, 2, 2, 2)
        self.filling_time_input = QDoubleSpinBox(self.widget_52)
        self.filling_time_input.setObjectName(u"filling_time_input")
        sizePolicy1.setHeightForWidth(self.filling_time_input.sizePolicy().hasHeightForWidth())
        self.filling_time_input.setSizePolicy(sizePolicy1)
        self.filling_time_input.setFont(font11)
        self.filling_time_input.setStyleSheet(u"")
        self.filling_time_input.setAlignment(Qt.AlignCenter)
        self.filling_time_input.setReadOnly(False)
        self.filling_time_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.filling_time_input.setDecimals(1)
        self.filling_time_input.setMaximum(999.000000000000000)
        self.filling_time_input.setValue(999.000000000000000)

        self.horizontalLayout_134.addWidget(self.filling_time_input)


        self.horizontalLayout_132.addWidget(self.widget_52)

        self.horizontalLayout_132.setStretch(0, 2)

        self.verticalLayout_69.addWidget(self.widget_142)

        self.widget_145 = QWidget(self.widget_50)
        self.widget_145.setObjectName(u"widget_145")
        self.widget_145.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_135 = QHBoxLayout(self.widget_145)
        self.horizontalLayout_135.setSpacing(10)
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.horizontalLayout_135.setContentsMargins(10, 0, 0, 0)
        self.widget_53 = QWidget(self.widget_145)
        self.widget_53.setObjectName(u"widget_53")
        self.widget_53.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout_137 = QHBoxLayout(self.widget_53)
        self.horizontalLayout_137.setSpacing(0)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalLayout_137.setContentsMargins(2, 2, 2, 2)
        self.g_holding_time_input = QDoubleSpinBox(self.widget_53)
        self.g_holding_time_input.setObjectName(u"g_holding_time_input")
        sizePolicy1.setHeightForWidth(self.g_holding_time_input.sizePolicy().hasHeightForWidth())
        self.g_holding_time_input.setSizePolicy(sizePolicy1)
        self.g_holding_time_input.setFont(font11)
        self.g_holding_time_input.setStyleSheet(u"")
        self.g_holding_time_input.setAlignment(Qt.AlignCenter)
        self.g_holding_time_input.setReadOnly(False)
        self.g_holding_time_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.g_holding_time_input.setDecimals(1)
        self.g_holding_time_input.setMaximum(999.000000000000000)
        self.g_holding_time_input.setValue(999.000000000000000)

        self.horizontalLayout_137.addWidget(self.g_holding_time_input)


        self.horizontalLayout_135.addWidget(self.widget_53)

        self.horizontalLayout_135.setStretch(0, 2)

        self.verticalLayout_69.addWidget(self.widget_145)

        self.widget_154 = QWidget(self.widget_50)
        self.widget_154.setObjectName(u"widget_154")
        self.widget_154.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_143 = QHBoxLayout(self.widget_154)
        self.horizontalLayout_143.setSpacing(10)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalLayout_143.setContentsMargins(10, 0, 0, 0)
        self.widget_54 = QWidget(self.widget_154)
        self.widget_54.setObjectName(u"widget_54")
        self.widget_54.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout_140 = QHBoxLayout(self.widget_54)
        self.horizontalLayout_140.setSpacing(0)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.horizontalLayout_140.setContentsMargins(2, 2, 2, 2)
        self.bleeding_time_input = QDoubleSpinBox(self.widget_54)
        self.bleeding_time_input.setObjectName(u"bleeding_time_input")
        sizePolicy1.setHeightForWidth(self.bleeding_time_input.sizePolicy().hasHeightForWidth())
        self.bleeding_time_input.setSizePolicy(sizePolicy1)
        self.bleeding_time_input.setFont(font11)
        self.bleeding_time_input.setStyleSheet(u"")
        self.bleeding_time_input.setAlignment(Qt.AlignCenter)
        self.bleeding_time_input.setReadOnly(False)
        self.bleeding_time_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.bleeding_time_input.setDecimals(1)
        self.bleeding_time_input.setMaximum(999.000000000000000)
        self.bleeding_time_input.setValue(999.000000000000000)

        self.horizontalLayout_140.addWidget(self.bleeding_time_input)


        self.horizontalLayout_143.addWidget(self.widget_54)

        self.horizontalLayout_143.setStretch(0, 2)

        self.verticalLayout_69.addWidget(self.widget_154)


        self.verticalLayout_68.addWidget(self.widget_50)


        self.horizontalLayout_95.addWidget(self.widget_49)

        self.line_14 = QFrame(self.widget_48)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.Shape.VLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_95.addWidget(self.line_14)

        self.widget_55 = QWidget(self.widget_48)
        self.widget_55.setObjectName(u"widget_55")
        sizePolicy.setHeightForWidth(self.widget_55.sizePolicy().hasHeightForWidth())
        self.widget_55.setSizePolicy(sizePolicy)
        self.widget_55.setStyleSheet(u"")
        self.horizontalLayout_163 = QHBoxLayout(self.widget_55)
        self.horizontalLayout_163.setSpacing(5)
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.horizontalLayout_163.setContentsMargins(0, 0, 0, 0)
        self.widget_107 = QWidget(self.widget_55)
        self.widget_107.setObjectName(u"widget_107")
        sizePolicy.setHeightForWidth(self.widget_107.sizePolicy().hasHeightForWidth())
        self.widget_107.setSizePolicy(sizePolicy)
        self.verticalLayout_84 = QVBoxLayout(self.widget_107)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.widget_108 = QWidget(self.widget_107)
        self.widget_108.setObjectName(u"widget_108")
        self.widget_108.setStyleSheet(u"border-left: None;\n"
"border-radius: 5px;")
        self.verticalLayout_85 = QVBoxLayout(self.widget_108)
        self.verticalLayout_85.setSpacing(10)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(5, 0, 0, 0)
        self.widget_109 = QWidget(self.widget_108)
        self.widget_109.setObjectName(u"widget_109")
        self.verticalLayout_86 = QVBoxLayout(self.widget_109)
        self.verticalLayout_86.setSpacing(15)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 10, 0, 10)
        self.widget_110 = QWidget(self.widget_109)
        self.widget_110.setObjectName(u"widget_110")
        self.widget_110.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_190 = QHBoxLayout(self.widget_110)
        self.horizontalLayout_190.setObjectName(u"horizontalLayout_190")
        self.horizontalLayout_190.setContentsMargins(0, 0, 5, 0)
        self.label_128 = QLabel(self.widget_110)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setFont(font10)

        self.horizontalLayout_190.addWidget(self.label_128)


        self.verticalLayout_86.addWidget(self.widget_110)


        self.verticalLayout_85.addWidget(self.widget_109)


        self.verticalLayout_84.addWidget(self.widget_108)


        self.horizontalLayout_163.addWidget(self.widget_107)

        self.widget_114 = QWidget(self.widget_55)
        self.widget_114.setObjectName(u"widget_114")
        self.widget_114.setStyleSheet(u"border-left: None;")
        self.verticalLayout_87 = QVBoxLayout(self.widget_114)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.widget_115 = QWidget(self.widget_114)
        self.widget_115.setObjectName(u"widget_115")
        self.widget_115.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QSpinBox:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}")
        self.verticalLayout_88 = QVBoxLayout(self.widget_115)
        self.verticalLayout_88.setSpacing(15)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 10, 0, 10)
        self.widget_167 = QWidget(self.widget_115)
        self.widget_167.setObjectName(u"widget_167")
        self.widget_167.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_37 = QHBoxLayout(self.widget_167)
        self.horizontalLayout_37.setSpacing(10)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(10, 0, 0, 0)
        self.widget_118 = QWidget(self.widget_167)
        self.widget_118.setObjectName(u"widget_118")
        self.widget_118.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout_192 = QHBoxLayout(self.widget_118)
        self.horizontalLayout_192.setObjectName(u"horizontalLayout_192")
        self.horizontalLayout_192.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_displ = QDoubleSpinBox(self.widget_118)
        self.pressure_pv_displ.setObjectName(u"pressure_pv_displ")
        sizePolicy1.setHeightForWidth(self.pressure_pv_displ.sizePolicy().hasHeightForWidth())
        self.pressure_pv_displ.setSizePolicy(sizePolicy1)
        self.pressure_pv_displ.setFont(font11)
        self.pressure_pv_displ.setStyleSheet(u"")
        self.pressure_pv_displ.setAlignment(Qt.AlignCenter)
        self.pressure_pv_displ.setReadOnly(True)
        self.pressure_pv_displ.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_displ.setDecimals(1)
        self.pressure_pv_displ.setMaximum(999.000000000000000)
        self.pressure_pv_displ.setValue(999.000000000000000)

        self.horizontalLayout_192.addWidget(self.pressure_pv_displ)

        self.label_30 = QLabel(self.widget_118)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font12)
        self.label_30.setStyleSheet(u"border: none;\n"
"")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_192.addWidget(self.label_30)

        self.pressure_sv_input = QDoubleSpinBox(self.widget_118)
        self.pressure_sv_input.setObjectName(u"pressure_sv_input")
        sizePolicy1.setHeightForWidth(self.pressure_sv_input.sizePolicy().hasHeightForWidth())
        self.pressure_sv_input.setSizePolicy(sizePolicy1)
        self.pressure_sv_input.setFont(font11)
        self.pressure_sv_input.setStyleSheet(u"")
        self.pressure_sv_input.setAlignment(Qt.AlignCenter)
        self.pressure_sv_input.setReadOnly(False)
        self.pressure_sv_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_input.setDecimals(1)
        self.pressure_sv_input.setMaximum(999.000000000000000)
        self.pressure_sv_input.setValue(999.000000000000000)

        self.horizontalLayout_192.addWidget(self.pressure_sv_input)


        self.horizontalLayout_37.addWidget(self.widget_118)


        self.verticalLayout_88.addWidget(self.widget_167)


        self.verticalLayout_87.addWidget(self.widget_115)


        self.horizontalLayout_163.addWidget(self.widget_114)


        self.horizontalLayout_95.addWidget(self.widget_55)

        self.horizontalLayout_95.setStretch(1, 1)
        self.horizontalLayout_95.setStretch(3, 2)

        self.verticalLayout_64.addWidget(self.widget_48)

        self.verticalLayout_64.setStretch(0, 1)
        self.verticalLayout_64.setStretch(1, 3)
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.horizontalLayout_35.addWidget(self.scrollArea_7)


        self.verticalLayout_63.addWidget(self.widget_46)


        self.verticalLayout_10.addWidget(self.widget_pressure_time)

        self.widget_temperature = QWidget(self.pressure_layout)
        self.widget_temperature.setObjectName(u"widget_temperature")
        self.widget_temperature.setStyleSheet(u"background-color: white;\n"
"border-radius: 15px;")
        self.verticalLayout_56 = QVBoxLayout(self.widget_temperature)
        self.verticalLayout_56.setSpacing(10)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 5, 0, 0)
        self.widget_13 = QWidget(self.widget_temperature)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMaximumSize(QSize(16777215, 50))
        self.widget_13.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.horizontalLayout_60 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(15, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.widget_13)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setFont(font1)
        icon10 = QIcon()
        icon10.addFile(u":/newPrefix/temperature-high.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon10)
        self.pushButton_5.setIconSize(QSize(30, 30))

        self.horizontalLayout_60.addWidget(self.pushButton_5)

        self.scrollArea_2 = QScrollArea(self.widget_13)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 690, 50))
        self.scrollAreaWidgetContents_2.setMinimumSize(QSize(690, 0))
        self.horizontalLayout_13 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 20, 0)
        self.widget_20 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_40 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.stacked_cel_fah_switch = QStackedWidget(self.widget_20)
        self.stacked_cel_fah_switch.setObjectName(u"stacked_cel_fah_switch")
        self.celsius_btn_page = QWidget()
        self.celsius_btn_page.setObjectName(u"celsius_btn_page")
        self.horizontalLayout_4 = QHBoxLayout(self.celsius_btn_page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.celsius_btn = QPushButton(self.celsius_btn_page)
        self.celsius_btn.setObjectName(u"celsius_btn")
        sizePolicy.setHeightForWidth(self.celsius_btn.sizePolicy().hasHeightForWidth())
        self.celsius_btn.setSizePolicy(sizePolicy)
        self.celsius_btn.setMaximumSize(QSize(110, 16777215))
        font13 = QFont()
        font13.setPointSize(13)
        font13.setBold(True)
        self.celsius_btn.setFont(font13)
        self.celsius_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #F0F9FF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #E0F2FE;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/newPrefix/sort.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.celsius_btn.setIcon(icon11)
        self.celsius_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.celsius_btn)

        self.stacked_cel_fah_switch.addWidget(self.celsius_btn_page)
        self.fahrenheit_btn_page = QWidget()
        self.fahrenheit_btn_page.setObjectName(u"fahrenheit_btn_page")
        self.horizontalLayout_5 = QHBoxLayout(self.fahrenheit_btn_page)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.fahrenheit_btn = QPushButton(self.fahrenheit_btn_page)
        self.fahrenheit_btn.setObjectName(u"fahrenheit_btn")
        sizePolicy.setHeightForWidth(self.fahrenheit_btn.sizePolicy().hasHeightForWidth())
        self.fahrenheit_btn.setSizePolicy(sizePolicy)
        self.fahrenheit_btn.setMaximumSize(QSize(110, 16777215))
        self.fahrenheit_btn.setFont(font13)
        self.fahrenheit_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #F0F9FF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #E0F2FE;\n"
"}")
        self.fahrenheit_btn.setIcon(icon11)
        self.fahrenheit_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.fahrenheit_btn)

        self.stacked_cel_fah_switch.addWidget(self.fahrenheit_btn_page)

        self.horizontalLayout_40.addWidget(self.stacked_cel_fah_switch)


        self.horizontalLayout_13.addWidget(self.widget_20)

        self.widget_5 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(280, 0))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 0, 10, 0)
        self.label_78 = QLabel(self.widget_5)
        self.label_78.setObjectName(u"label_78")
        sizePolicy.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy)
        self.label_78.setFont(font9)
        self.label_78.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_78)

        self.label_21 = QLabel(self.widget_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font12)
        self.label_21.setStyleSheet(u"border: none;\n"
"")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_21)

        self.label_79 = QLabel(self.widget_5)
        self.label_79.setObjectName(u"label_79")
        sizePolicy.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy)
        self.label_79.setFont(font9)
        self.label_79.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_79)

        self.label_22 = QLabel(self.widget_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font12)
        self.label_22.setStyleSheet(u"border: none;\n"
"")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_22)

        self.label_80 = QLabel(self.widget_5)
        self.label_80.setObjectName(u"label_80")
        sizePolicy.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy)
        self.label_80.setFont(font9)
        self.label_80.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_80)


        self.horizontalLayout_13.addWidget(self.widget_5)

        self.label_77 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_77.setObjectName(u"label_77")
        sizePolicy.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy)
        self.label_77.setFont(font9)
        self.label_77.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_77)

        self.label_56 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_56.setObjectName(u"label_56")
        sizePolicy.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy)
        self.label_56.setFont(font9)
        self.label_56.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_56)

        self.label_271 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_271.setObjectName(u"label_271")
        self.label_271.setFont(font12)
        self.label_271.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_271.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_271)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 2)
        self.horizontalLayout_13.setStretch(2, 1)
        self.horizontalLayout_13.setStretch(3, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_60.addWidget(self.scrollArea_2)

        self.horizontalLayout_60.setStretch(0, 1)
        self.horizontalLayout_60.setStretch(1, 6)

        self.verticalLayout_56.addWidget(self.widget_13)

        self.scrollArea_4 = QScrollArea(self.widget_temperature)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy)
        self.scrollArea_4.setStyleSheet(u"QScrollArea{\n"
"	border-radius: 10px;\n"
"}\n"
"QFrame {\n"
"    background-color: #F8FAFC;\n"
"    border-left: 4px solid #FB8C00;\n"
"    border-radius: 6px;\n"
"}\n"
"QStackedWidget {\n"
"	border: none;\n"
"}")
        self.scrollArea_4.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_4.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 861, 237))
        self.scrollAreaWidgetContents_4.setStyleSheet(u"\n"
"    background-color: white;\n"
"	padding: 2px;\n"
"")
        self.verticalLayout_54 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 5, 0)
        self.widget_21 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_21.setObjectName(u"widget_21")
        sizePolicy1.setHeightForWidth(self.widget_21.sizePolicy().hasHeightForWidth())
        self.widget_21.setSizePolicy(sizePolicy1)
        self.widget_21.setStyleSheet(u"")
        self.horizontalLayout_59 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_59.setSpacing(5)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.widget_76 = QWidget(self.widget_21)
        self.widget_76.setObjectName(u"widget_76")
        sizePolicy.setHeightForWidth(self.widget_76.sizePolicy().hasHeightForWidth())
        self.widget_76.setSizePolicy(sizePolicy)
        self.verticalLayout_55 = QVBoxLayout(self.widget_76)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.widget_77 = QWidget(self.widget_76)
        self.widget_77.setObjectName(u"widget_77")
        self.widget_77.setStyleSheet(u"border-left: None;\n"
"border-radius: 5px;")
        self.verticalLayout_44 = QVBoxLayout(self.widget_77)
        self.verticalLayout_44.setSpacing(10)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(5, 0, 0, 0)
        self.widget_11 = QWidget(self.widget_77)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_45 = QVBoxLayout(self.widget_11)
        self.verticalLayout_45.setSpacing(15)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(10, 10, 10, 10)
        self.widget_82 = QWidget(self.widget_11)
        self.widget_82.setObjectName(u"widget_82")
        self.widget_82.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_64 = QHBoxLayout(self.widget_82)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 5, 0)
        self.label_104 = QLabel(self.widget_82)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setFont(font10)

        self.horizontalLayout_64.addWidget(self.label_104)


        self.verticalLayout_45.addWidget(self.widget_82)

        self.widget_83 = QWidget(self.widget_11)
        self.widget_83.setObjectName(u"widget_83")
        self.widget_83.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_65 = QHBoxLayout(self.widget_83)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 5, 0)
        self.label_105 = QLabel(self.widget_83)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setFont(font10)

        self.horizontalLayout_65.addWidget(self.label_105)


        self.verticalLayout_45.addWidget(self.widget_83)

        self.widget_84 = QWidget(self.widget_11)
        self.widget_84.setObjectName(u"widget_84")
        self.widget_84.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_66 = QHBoxLayout(self.widget_84)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 5, 0)
        self.label_106 = QLabel(self.widget_84)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setFont(font10)

        self.horizontalLayout_66.addWidget(self.label_106)


        self.verticalLayout_45.addWidget(self.widget_84)

        self.widget_85 = QWidget(self.widget_11)
        self.widget_85.setObjectName(u"widget_85")
        self.widget_85.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_67 = QHBoxLayout(self.widget_85)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 5, 0)
        self.label_107 = QLabel(self.widget_85)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setFont(font10)

        self.horizontalLayout_67.addWidget(self.label_107)


        self.verticalLayout_45.addWidget(self.widget_85)


        self.verticalLayout_44.addWidget(self.widget_11)


        self.verticalLayout_55.addWidget(self.widget_77)


        self.horizontalLayout_59.addWidget(self.widget_76)

        self.line_7 = QFrame(self.widget_21)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_59.addWidget(self.line_7)

        self.widget_22 = QWidget(self.widget_21)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setStyleSheet(u"border-left: None;")
        self.verticalLayout_46 = QVBoxLayout(self.widget_22)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.widget_27 = QWidget(self.widget_22)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QSpinBox:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"}")
        self.verticalLayout_47 = QVBoxLayout(self.widget_27)
        self.verticalLayout_47.setSpacing(15)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 10, 0, 10)
        self.widget_137 = QWidget(self.widget_27)
        self.widget_137.setObjectName(u"widget_137")
        self.widget_137.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_126 = QHBoxLayout(self.widget_137)
        self.horizontalLayout_126.setSpacing(10)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_126.setContentsMargins(10, 0, 0, 0)
        self.sys_state_stacked_wid_8 = QStackedWidget(self.widget_137)
        self.sys_state_stacked_wid_8.setObjectName(u"sys_state_stacked_wid_8")
        sizePolicy.setHeightForWidth(self.sys_state_stacked_wid_8.sizePolicy().hasHeightForWidth())
        self.sys_state_stacked_wid_8.setSizePolicy(sizePolicy)
        self.running_light_10 = QWidget()
        self.running_light_10.setObjectName(u"running_light_10")
        self.horizontalLayout_88 = QHBoxLayout(self.running_light_10)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.running_label_10 = QLabel(self.running_light_10)
        self.running_label_10.setObjectName(u"running_label_10")
        sizePolicy.setHeightForWidth(self.running_label_10.sizePolicy().hasHeightForWidth())
        self.running_label_10.setSizePolicy(sizePolicy)
        self.running_label_10.setStyleSheet(u"font-size: 14px; \n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #10B981; \n"
"font-weight: 500; \n"
"padding-right: 3px;")

        self.horizontalLayout_88.addWidget(self.running_label_10)

        self.sys_state_stacked_wid_8.addWidget(self.running_light_10)
        self.wating_light_10 = QWidget()
        self.wating_light_10.setObjectName(u"wating_light_10")
        self.horizontalLayout_89 = QHBoxLayout(self.wating_light_10)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.waiting_label_10 = QLabel(self.wating_light_10)
        self.waiting_label_10.setObjectName(u"waiting_label_10")
        sizePolicy.setHeightForWidth(self.waiting_label_10.sizePolicy().hasHeightForWidth())
        self.waiting_label_10.setSizePolicy(sizePolicy)
        self.waiting_label_10.setFont(font6)
        self.waiting_label_10.setStyleSheet(u"font-size: 14px; \n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: rgb(255, 170, 0); \n"
"font-weight: 500; \n"
"padding-right: 3px;\n"
"")

        self.horizontalLayout_89.addWidget(self.waiting_label_10)

        self.sys_state_stacked_wid_8.addWidget(self.wating_light_10)
        self.error_light_10 = QWidget()
        self.error_light_10.setObjectName(u"error_light_10")
        self.horizontalLayout_90 = QHBoxLayout(self.error_light_10)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.error_label_10 = QLabel(self.error_light_10)
        self.error_label_10.setObjectName(u"error_label_10")
        sizePolicy.setHeightForWidth(self.error_label_10.sizePolicy().hasHeightForWidth())
        self.error_label_10.setSizePolicy(sizePolicy)
        self.error_label_10.setStyleSheet(u"font-size: 14px; \n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #F90A0A; \n"
"font-weight: 500; \n"
"padding-right: 3px;")

        self.horizontalLayout_90.addWidget(self.error_label_10)

        self.sys_state_stacked_wid_8.addWidget(self.error_light_10)

        self.horizontalLayout_126.addWidget(self.sys_state_stacked_wid_8)

        self.widget_23 = QWidget(self.widget_137)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout_62 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(2, 2, 2, 2)
        self.high_temp_input_1 = QDoubleSpinBox(self.widget_23)
        self.high_temp_input_1.setObjectName(u"high_temp_input_1")
        sizePolicy1.setHeightForWidth(self.high_temp_input_1.sizePolicy().hasHeightForWidth())
        self.high_temp_input_1.setSizePolicy(sizePolicy1)
        self.high_temp_input_1.setFont(font11)
        self.high_temp_input_1.setStyleSheet(u"")
        self.high_temp_input_1.setAlignment(Qt.AlignCenter)
        self.high_temp_input_1.setReadOnly(False)
        self.high_temp_input_1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.high_temp_input_1.setDecimals(1)
        self.high_temp_input_1.setMaximum(999.000000000000000)
        self.high_temp_input_1.setValue(0.000000000000000)

        self.horizontalLayout_62.addWidget(self.high_temp_input_1)

        self.label_10 = QLabel(self.widget_23)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font12)
        self.label_10.setStyleSheet(u"border: none;\n"
"")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.label_10)

        self.pv_value_displ_1 = QDoubleSpinBox(self.widget_23)
        self.pv_value_displ_1.setObjectName(u"pv_value_displ_1")
        sizePolicy1.setHeightForWidth(self.pv_value_displ_1.sizePolicy().hasHeightForWidth())
        self.pv_value_displ_1.setSizePolicy(sizePolicy1)
        self.pv_value_displ_1.setFont(font11)
        self.pv_value_displ_1.setStyleSheet(u"")
        self.pv_value_displ_1.setAlignment(Qt.AlignCenter)
        self.pv_value_displ_1.setReadOnly(True)
        self.pv_value_displ_1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pv_value_displ_1.setDecimals(1)
        self.pv_value_displ_1.setMaximum(999.000000000000000)
        self.pv_value_displ_1.setValue(0.000000000000000)

        self.horizontalLayout_62.addWidget(self.pv_value_displ_1)

        self.label_11 = QLabel(self.widget_23)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font12)
        self.label_11.setStyleSheet(u"border: none;\n"
"")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.label_11)

        self.low_temp_input_1 = QDoubleSpinBox(self.widget_23)
        self.low_temp_input_1.setObjectName(u"low_temp_input_1")
        sizePolicy1.setHeightForWidth(self.low_temp_input_1.sizePolicy().hasHeightForWidth())
        self.low_temp_input_1.setSizePolicy(sizePolicy1)
        self.low_temp_input_1.setFont(font11)
        self.low_temp_input_1.setStyleSheet(u"")
        self.low_temp_input_1.setAlignment(Qt.AlignCenter)
        self.low_temp_input_1.setReadOnly(False)
        self.low_temp_input_1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.low_temp_input_1.setDecimals(1)
        self.low_temp_input_1.setMaximum(999.000000000000000)
        self.low_temp_input_1.setValue(0.000000000000000)

        self.horizontalLayout_62.addWidget(self.low_temp_input_1)


        self.horizontalLayout_126.addWidget(self.widget_23)

        self.sv_value_input_1 = QDoubleSpinBox(self.widget_137)
        self.sv_value_input_1.setObjectName(u"sv_value_input_1")
        sizePolicy1.setHeightForWidth(self.sv_value_input_1.sizePolicy().hasHeightForWidth())
        self.sv_value_input_1.setSizePolicy(sizePolicy1)
        self.sv_value_input_1.setFont(font11)
        self.sv_value_input_1.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.sv_value_input_1.setAlignment(Qt.AlignCenter)
        self.sv_value_input_1.setReadOnly(False)
        self.sv_value_input_1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_input_1.setDecimals(1)
        self.sv_value_input_1.setMinimum(-999.000000000000000)
        self.sv_value_input_1.setMaximum(999.000000000000000)

        self.horizontalLayout_126.addWidget(self.sv_value_input_1)

        self.offset_value_input_1 = QDoubleSpinBox(self.widget_137)
        self.offset_value_input_1.setObjectName(u"offset_value_input_1")
        sizePolicy1.setHeightForWidth(self.offset_value_input_1.sizePolicy().hasHeightForWidth())
        self.offset_value_input_1.setSizePolicy(sizePolicy1)
        self.offset_value_input_1.setFont(font11)
        self.offset_value_input_1.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.offset_value_input_1.setAlignment(Qt.AlignCenter)
        self.offset_value_input_1.setReadOnly(False)
        self.offset_value_input_1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.offset_value_input_1.setDecimals(1)
        self.offset_value_input_1.setMinimum(-999.000000000000000)
        self.offset_value_input_1.setMaximum(999.000000000000000)

        self.horizontalLayout_126.addWidget(self.offset_value_input_1)

        self.stackedWidget_7 = QStackedWidget(self.widget_137)
        self.stackedWidget_7.setObjectName(u"stackedWidget_7")
        self.celsius_displ_1 = QWidget()
        self.celsius_displ_1.setObjectName(u"celsius_displ_1")
        self.horizontalLayout_8 = QHBoxLayout(self.celsius_displ_1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_177 = QLabel(self.celsius_displ_1)
        self.label_177.setObjectName(u"label_177")
        font14 = QFont()
        font14.setFamilies([u"Segoe UI"])
        font14.setPointSize(15)
        font14.setBold(True)
        font14.setItalic(False)
        self.label_177.setFont(font14)
        self.label_177.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_177.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_177)

        self.stackedWidget_7.addWidget(self.celsius_displ_1)
        self.fahrenheit_displ_1 = QWidget()
        self.fahrenheit_displ_1.setObjectName(u"fahrenheit_displ_1")
        self.horizontalLayout_10 = QHBoxLayout(self.fahrenheit_displ_1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_178 = QLabel(self.fahrenheit_displ_1)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setFont(font14)
        self.label_178.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_178.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_178)

        self.stackedWidget_7.addWidget(self.fahrenheit_displ_1)

        self.horizontalLayout_126.addWidget(self.stackedWidget_7)

        self.horizontalLayout_126.setStretch(0, 1)
        self.horizontalLayout_126.setStretch(1, 2)
        self.horizontalLayout_126.setStretch(2, 1)
        self.horizontalLayout_126.setStretch(3, 1)

        self.verticalLayout_47.addWidget(self.widget_137)

        self.widget_140 = QWidget(self.widget_27)
        self.widget_140.setObjectName(u"widget_140")
        self.widget_140.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_129 = QHBoxLayout(self.widget_140)
        self.horizontalLayout_129.setSpacing(10)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalLayout_129.setContentsMargins(10, 0, 0, 0)
        self.sys_state_stacked_wid_9 = QStackedWidget(self.widget_140)
        self.sys_state_stacked_wid_9.setObjectName(u"sys_state_stacked_wid_9")
        sizePolicy.setHeightForWidth(self.sys_state_stacked_wid_9.sizePolicy().hasHeightForWidth())
        self.sys_state_stacked_wid_9.setSizePolicy(sizePolicy)
        self.running_light_11 = QWidget()
        self.running_light_11.setObjectName(u"running_light_11")
        self.horizontalLayout_91 = QHBoxLayout(self.running_light_11)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.running_label_11 = QLabel(self.running_light_11)
        self.running_label_11.setObjectName(u"running_label_11")
        sizePolicy.setHeightForWidth(self.running_label_11.sizePolicy().hasHeightForWidth())
        self.running_label_11.setSizePolicy(sizePolicy)
        self.running_label_11.setStyleSheet(u"font-size: 14px; \n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #10B981; \n"
"font-weight: 500; \n"
"padding-right: 3px;")

        self.horizontalLayout_91.addWidget(self.running_label_11)

        self.sys_state_stacked_wid_9.addWidget(self.running_light_11)
        self.wating_light_11 = QWidget()
        self.wating_light_11.setObjectName(u"wating_light_11")
        self.horizontalLayout_92 = QHBoxLayout(self.wating_light_11)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.waiting_label_11 = QLabel(self.wating_light_11)
        self.waiting_label_11.setObjectName(u"waiting_label_11")
        sizePolicy.setHeightForWidth(self.waiting_label_11.sizePolicy().hasHeightForWidth())
        self.waiting_label_11.setSizePolicy(sizePolicy)
        self.waiting_label_11.setFont(font6)
        self.waiting_label_11.setStyleSheet(u"font-size: 14px; \n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: rgb(255, 170, 0); \n"
"font-weight: 500; \n"
"padding-right: 3px;\n"
"")

        self.horizontalLayout_92.addWidget(self.waiting_label_11)

        self.sys_state_stacked_wid_9.addWidget(self.wating_light_11)
        self.error_light_11 = QWidget()
        self.error_light_11.setObjectName(u"error_light_11")
        self.horizontalLayout_93 = QHBoxLayout(self.error_light_11)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.error_label_11 = QLabel(self.error_light_11)
        self.error_label_11.setObjectName(u"error_label_11")
        sizePolicy.setHeightForWidth(self.error_label_11.sizePolicy().hasHeightForWidth())
        self.error_label_11.setSizePolicy(sizePolicy)
        self.error_label_11.setStyleSheet(u"font-size: 14px; \n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #F90A0A; \n"
"font-weight: 500; \n"
"padding-right: 3px;")

        self.horizontalLayout_93.addWidget(self.error_label_11)

        self.sys_state_stacked_wid_9.addWidget(self.error_light_11)

        self.horizontalLayout_129.addWidget(self.sys_state_stacked_wid_9)

        self.widget_25 = QWidget(self.widget_140)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout_63 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(2, 2, 2, 2)
        self.high_temp_input_2 = QDoubleSpinBox(self.widget_25)
        self.high_temp_input_2.setObjectName(u"high_temp_input_2")
        sizePolicy1.setHeightForWidth(self.high_temp_input_2.sizePolicy().hasHeightForWidth())
        self.high_temp_input_2.setSizePolicy(sizePolicy1)
        self.high_temp_input_2.setFont(font11)
        self.high_temp_input_2.setStyleSheet(u"")
        self.high_temp_input_2.setAlignment(Qt.AlignCenter)
        self.high_temp_input_2.setReadOnly(False)
        self.high_temp_input_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.high_temp_input_2.setDecimals(1)
        self.high_temp_input_2.setMaximum(999.000000000000000)
        self.high_temp_input_2.setValue(0.000000000000000)

        self.horizontalLayout_63.addWidget(self.high_temp_input_2)

        self.label_12 = QLabel(self.widget_25)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font12)
        self.label_12.setStyleSheet(u"border: none;\n"
"")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.label_12)

        self.pv_value_displ_2 = QDoubleSpinBox(self.widget_25)
        self.pv_value_displ_2.setObjectName(u"pv_value_displ_2")
        sizePolicy1.setHeightForWidth(self.pv_value_displ_2.sizePolicy().hasHeightForWidth())
        self.pv_value_displ_2.setSizePolicy(sizePolicy1)
        self.pv_value_displ_2.setFont(font11)
        self.pv_value_displ_2.setStyleSheet(u"")
        self.pv_value_displ_2.setAlignment(Qt.AlignCenter)
        self.pv_value_displ_2.setReadOnly(True)
        self.pv_value_displ_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pv_value_displ_2.setDecimals(1)
        self.pv_value_displ_2.setMaximum(999.000000000000000)
        self.pv_value_displ_2.setValue(0.000000000000000)

        self.horizontalLayout_63.addWidget(self.pv_value_displ_2)

        self.label_13 = QLabel(self.widget_25)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font12)
        self.label_13.setStyleSheet(u"border: none;\n"
"")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.label_13)

        self.low_temp_input_2 = QDoubleSpinBox(self.widget_25)
        self.low_temp_input_2.setObjectName(u"low_temp_input_2")
        sizePolicy1.setHeightForWidth(self.low_temp_input_2.sizePolicy().hasHeightForWidth())
        self.low_temp_input_2.setSizePolicy(sizePolicy1)
        self.low_temp_input_2.setFont(font11)
        self.low_temp_input_2.setStyleSheet(u"")
        self.low_temp_input_2.setAlignment(Qt.AlignCenter)
        self.low_temp_input_2.setReadOnly(False)
        self.low_temp_input_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.low_temp_input_2.setDecimals(1)
        self.low_temp_input_2.setMaximum(999.000000000000000)
        self.low_temp_input_2.setValue(0.000000000000000)

        self.horizontalLayout_63.addWidget(self.low_temp_input_2)


        self.horizontalLayout_129.addWidget(self.widget_25)

        self.sv_value_input_2 = QDoubleSpinBox(self.widget_140)
        self.sv_value_input_2.setObjectName(u"sv_value_input_2")
        sizePolicy1.setHeightForWidth(self.sv_value_input_2.sizePolicy().hasHeightForWidth())
        self.sv_value_input_2.setSizePolicy(sizePolicy1)
        self.sv_value_input_2.setFont(font11)
        self.sv_value_input_2.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.sv_value_input_2.setAlignment(Qt.AlignCenter)
        self.sv_value_input_2.setReadOnly(False)
        self.sv_value_input_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_input_2.setDecimals(1)
        self.sv_value_input_2.setMinimum(-999.000000000000000)
        self.sv_value_input_2.setMaximum(999.000000000000000)

        self.horizontalLayout_129.addWidget(self.sv_value_input_2)

        self.offset_value_input_2 = QDoubleSpinBox(self.widget_140)
        self.offset_value_input_2.setObjectName(u"offset_value_input_2")
        sizePolicy1.setHeightForWidth(self.offset_value_input_2.sizePolicy().hasHeightForWidth())
        self.offset_value_input_2.setSizePolicy(sizePolicy1)
        self.offset_value_input_2.setFont(font11)
        self.offset_value_input_2.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.offset_value_input_2.setAlignment(Qt.AlignCenter)
        self.offset_value_input_2.setReadOnly(False)
        self.offset_value_input_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.offset_value_input_2.setDecimals(1)
        self.offset_value_input_2.setMinimum(-999.000000000000000)
        self.offset_value_input_2.setMaximum(999.000000000000000)

        self.horizontalLayout_129.addWidget(self.offset_value_input_2)

        self.stackedWidget_8 = QStackedWidget(self.widget_140)
        self.stackedWidget_8.setObjectName(u"stackedWidget_8")
        self.celsius_displ_2 = QWidget()
        self.celsius_displ_2.setObjectName(u"celsius_displ_2")
        self.horizontalLayout_11 = QHBoxLayout(self.celsius_displ_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_179 = QLabel(self.celsius_displ_2)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setFont(font14)
        self.label_179.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_179.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_179)

        self.stackedWidget_8.addWidget(self.celsius_displ_2)
        self.fahrenheit_displ_2 = QWidget()
        self.fahrenheit_displ_2.setObjectName(u"fahrenheit_displ_2")
        self.horizontalLayout_18 = QHBoxLayout(self.fahrenheit_displ_2)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_180 = QLabel(self.fahrenheit_displ_2)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setFont(font14)
        self.label_180.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_180.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_180)

        self.stackedWidget_8.addWidget(self.fahrenheit_displ_2)

        self.horizontalLayout_129.addWidget(self.stackedWidget_8)

        self.horizontalLayout_129.setStretch(0, 1)
        self.horizontalLayout_129.setStretch(1, 2)
        self.horizontalLayout_129.setStretch(2, 1)
        self.horizontalLayout_129.setStretch(3, 1)

        self.verticalLayout_47.addWidget(self.widget_140)

        self.widget_149 = QWidget(self.widget_27)
        self.widget_149.setObjectName(u"widget_149")
        self.widget_149.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_138 = QHBoxLayout(self.widget_149)
        self.horizontalLayout_138.setSpacing(10)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.horizontalLayout_138.setContentsMargins(10, 0, 0, 0)
        self.sys_state_stacked_wid_6 = QStackedWidget(self.widget_149)
        self.sys_state_stacked_wid_6.setObjectName(u"sys_state_stacked_wid_6")
        sizePolicy.setHeightForWidth(self.sys_state_stacked_wid_6.sizePolicy().hasHeightForWidth())
        self.sys_state_stacked_wid_6.setSizePolicy(sizePolicy)
        self.running_light_8 = QWidget()
        self.running_light_8.setObjectName(u"running_light_8")
        self.horizontalLayout_82 = QHBoxLayout(self.running_light_8)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.running_label_8 = QLabel(self.running_light_8)
        self.running_label_8.setObjectName(u"running_label_8")
        sizePolicy.setHeightForWidth(self.running_label_8.sizePolicy().hasHeightForWidth())
        self.running_label_8.setSizePolicy(sizePolicy)
        self.running_label_8.setStyleSheet(u"font-size: 14px; \n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #10B981; \n"
"font-weight: 500; \n"
"padding-right: 3px;")

        self.horizontalLayout_82.addWidget(self.running_label_8)

        self.sys_state_stacked_wid_6.addWidget(self.running_light_8)
        self.wating_light_8 = QWidget()
        self.wating_light_8.setObjectName(u"wating_light_8")
        self.horizontalLayout_83 = QHBoxLayout(self.wating_light_8)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.waiting_label_8 = QLabel(self.wating_light_8)
        self.waiting_label_8.setObjectName(u"waiting_label_8")
        sizePolicy.setHeightForWidth(self.waiting_label_8.sizePolicy().hasHeightForWidth())
        self.waiting_label_8.setSizePolicy(sizePolicy)
        self.waiting_label_8.setFont(font6)
        self.waiting_label_8.setStyleSheet(u"font-size: 14px; \n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: rgb(255, 170, 0); \n"
"font-weight: 500; \n"
"padding-right: 3px;\n"
"")

        self.horizontalLayout_83.addWidget(self.waiting_label_8)

        self.sys_state_stacked_wid_6.addWidget(self.wating_light_8)
        self.error_light_8 = QWidget()
        self.error_light_8.setObjectName(u"error_light_8")
        self.horizontalLayout_84 = QHBoxLayout(self.error_light_8)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.error_label_8 = QLabel(self.error_light_8)
        self.error_label_8.setObjectName(u"error_label_8")
        sizePolicy.setHeightForWidth(self.error_label_8.sizePolicy().hasHeightForWidth())
        self.error_label_8.setSizePolicy(sizePolicy)
        self.error_label_8.setStyleSheet(u"font-size: 14px; \n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #F90A0A; \n"
"font-weight: 500; \n"
"padding-right: 3px;")

        self.horizontalLayout_84.addWidget(self.error_label_8)

        self.sys_state_stacked_wid_6.addWidget(self.error_light_8)

        self.horizontalLayout_138.addWidget(self.sys_state_stacked_wid_6)

        self.widget_26 = QWidget(self.widget_149)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout_71 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(2, 2, 2, 2)
        self.high_temp_input_3 = QDoubleSpinBox(self.widget_26)
        self.high_temp_input_3.setObjectName(u"high_temp_input_3")
        sizePolicy1.setHeightForWidth(self.high_temp_input_3.sizePolicy().hasHeightForWidth())
        self.high_temp_input_3.setSizePolicy(sizePolicy1)
        self.high_temp_input_3.setFont(font11)
        self.high_temp_input_3.setStyleSheet(u"")
        self.high_temp_input_3.setAlignment(Qt.AlignCenter)
        self.high_temp_input_3.setReadOnly(False)
        self.high_temp_input_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.high_temp_input_3.setDecimals(1)
        self.high_temp_input_3.setMaximum(999.000000000000000)
        self.high_temp_input_3.setValue(0.000000000000000)

        self.horizontalLayout_71.addWidget(self.high_temp_input_3)

        self.label_15 = QLabel(self.widget_26)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font12)
        self.label_15.setStyleSheet(u"border: none;\n"
"")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_71.addWidget(self.label_15)

        self.pv_value_displ_3 = QDoubleSpinBox(self.widget_26)
        self.pv_value_displ_3.setObjectName(u"pv_value_displ_3")
        sizePolicy1.setHeightForWidth(self.pv_value_displ_3.sizePolicy().hasHeightForWidth())
        self.pv_value_displ_3.setSizePolicy(sizePolicy1)
        self.pv_value_displ_3.setFont(font11)
        self.pv_value_displ_3.setStyleSheet(u"")
        self.pv_value_displ_3.setAlignment(Qt.AlignCenter)
        self.pv_value_displ_3.setReadOnly(True)
        self.pv_value_displ_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pv_value_displ_3.setDecimals(1)
        self.pv_value_displ_3.setMaximum(999.000000000000000)
        self.pv_value_displ_3.setValue(0.000000000000000)

        self.horizontalLayout_71.addWidget(self.pv_value_displ_3)

        self.label_16 = QLabel(self.widget_26)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font12)
        self.label_16.setStyleSheet(u"border: none;\n"
"")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_71.addWidget(self.label_16)

        self.low_temp_input_3 = QDoubleSpinBox(self.widget_26)
        self.low_temp_input_3.setObjectName(u"low_temp_input_3")
        sizePolicy1.setHeightForWidth(self.low_temp_input_3.sizePolicy().hasHeightForWidth())
        self.low_temp_input_3.setSizePolicy(sizePolicy1)
        self.low_temp_input_3.setFont(font11)
        self.low_temp_input_3.setStyleSheet(u"")
        self.low_temp_input_3.setAlignment(Qt.AlignCenter)
        self.low_temp_input_3.setReadOnly(False)
        self.low_temp_input_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.low_temp_input_3.setDecimals(1)
        self.low_temp_input_3.setMaximum(999.000000000000000)
        self.low_temp_input_3.setValue(0.000000000000000)

        self.horizontalLayout_71.addWidget(self.low_temp_input_3)


        self.horizontalLayout_138.addWidget(self.widget_26)

        self.sv_value_input_3 = QDoubleSpinBox(self.widget_149)
        self.sv_value_input_3.setObjectName(u"sv_value_input_3")
        sizePolicy1.setHeightForWidth(self.sv_value_input_3.sizePolicy().hasHeightForWidth())
        self.sv_value_input_3.setSizePolicy(sizePolicy1)
        self.sv_value_input_3.setFont(font11)
        self.sv_value_input_3.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.sv_value_input_3.setAlignment(Qt.AlignCenter)
        self.sv_value_input_3.setReadOnly(False)
        self.sv_value_input_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_input_3.setDecimals(1)
        self.sv_value_input_3.setMinimum(-999.000000000000000)
        self.sv_value_input_3.setMaximum(999.000000000000000)

        self.horizontalLayout_138.addWidget(self.sv_value_input_3)

        self.offset_value_input_3 = QDoubleSpinBox(self.widget_149)
        self.offset_value_input_3.setObjectName(u"offset_value_input_3")
        sizePolicy1.setHeightForWidth(self.offset_value_input_3.sizePolicy().hasHeightForWidth())
        self.offset_value_input_3.setSizePolicy(sizePolicy1)
        self.offset_value_input_3.setFont(font11)
        self.offset_value_input_3.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.offset_value_input_3.setAlignment(Qt.AlignCenter)
        self.offset_value_input_3.setReadOnly(False)
        self.offset_value_input_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.offset_value_input_3.setDecimals(1)
        self.offset_value_input_3.setMinimum(-999.000000000000000)
        self.offset_value_input_3.setMaximum(999.000000000000000)

        self.horizontalLayout_138.addWidget(self.offset_value_input_3)

        self.stackedWidget_9 = QStackedWidget(self.widget_149)
        self.stackedWidget_9.setObjectName(u"stackedWidget_9")
        self.celsius_displ_3 = QWidget()
        self.celsius_displ_3.setObjectName(u"celsius_displ_3")
        self.horizontalLayout_19 = QHBoxLayout(self.celsius_displ_3)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_181 = QLabel(self.celsius_displ_3)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setFont(font14)
        self.label_181.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_181.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.label_181)

        self.stackedWidget_9.addWidget(self.celsius_displ_3)
        self.fahrenheit_displ_3 = QWidget()
        self.fahrenheit_displ_3.setObjectName(u"fahrenheit_displ_3")
        self.horizontalLayout_20 = QHBoxLayout(self.fahrenheit_displ_3)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_182 = QLabel(self.fahrenheit_displ_3)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setFont(font14)
        self.label_182.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_182.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.label_182)

        self.stackedWidget_9.addWidget(self.fahrenheit_displ_3)

        self.horizontalLayout_138.addWidget(self.stackedWidget_9)

        self.horizontalLayout_138.setStretch(0, 1)
        self.horizontalLayout_138.setStretch(1, 2)
        self.horizontalLayout_138.setStretch(2, 1)
        self.horizontalLayout_138.setStretch(3, 1)

        self.verticalLayout_47.addWidget(self.widget_149)

        self.widget_150 = QWidget(self.widget_27)
        self.widget_150.setObjectName(u"widget_150")
        self.widget_150.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_139 = QHBoxLayout(self.widget_150)
        self.horizontalLayout_139.setSpacing(10)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.horizontalLayout_139.setContentsMargins(10, 0, 0, 0)
        self.sys_state_stacked_wid_7 = QStackedWidget(self.widget_150)
        self.sys_state_stacked_wid_7.setObjectName(u"sys_state_stacked_wid_7")
        sizePolicy.setHeightForWidth(self.sys_state_stacked_wid_7.sizePolicy().hasHeightForWidth())
        self.sys_state_stacked_wid_7.setSizePolicy(sizePolicy)
        self.running_light_9 = QWidget()
        self.running_light_9.setObjectName(u"running_light_9")
        self.horizontalLayout_85 = QHBoxLayout(self.running_light_9)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.running_label_9 = QLabel(self.running_light_9)
        self.running_label_9.setObjectName(u"running_label_9")
        sizePolicy.setHeightForWidth(self.running_label_9.sizePolicy().hasHeightForWidth())
        self.running_label_9.setSizePolicy(sizePolicy)
        self.running_label_9.setStyleSheet(u"font-size: 14px; \n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #10B981; \n"
"font-weight: 500; \n"
"padding-right: 3px;")

        self.horizontalLayout_85.addWidget(self.running_label_9)

        self.sys_state_stacked_wid_7.addWidget(self.running_light_9)
        self.wating_light_9 = QWidget()
        self.wating_light_9.setObjectName(u"wating_light_9")
        self.horizontalLayout_86 = QHBoxLayout(self.wating_light_9)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.waiting_label_9 = QLabel(self.wating_light_9)
        self.waiting_label_9.setObjectName(u"waiting_label_9")
        sizePolicy.setHeightForWidth(self.waiting_label_9.sizePolicy().hasHeightForWidth())
        self.waiting_label_9.setSizePolicy(sizePolicy)
        self.waiting_label_9.setFont(font6)
        self.waiting_label_9.setStyleSheet(u"font-size: 14px; \n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: rgb(255, 170, 0); \n"
"font-weight: 500; \n"
"padding-right: 3px;\n"
"")

        self.horizontalLayout_86.addWidget(self.waiting_label_9)

        self.sys_state_stacked_wid_7.addWidget(self.wating_light_9)
        self.error_light_9 = QWidget()
        self.error_light_9.setObjectName(u"error_light_9")
        self.horizontalLayout_87 = QHBoxLayout(self.error_light_9)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.error_label_9 = QLabel(self.error_light_9)
        self.error_label_9.setObjectName(u"error_label_9")
        sizePolicy.setHeightForWidth(self.error_label_9.sizePolicy().hasHeightForWidth())
        self.error_label_9.setSizePolicy(sizePolicy)
        self.error_label_9.setStyleSheet(u"font-size: 14px; \n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #F90A0A; \n"
"font-weight: 500; \n"
"padding-right: 3px;")

        self.horizontalLayout_87.addWidget(self.error_label_9)

        self.sys_state_stacked_wid_7.addWidget(self.error_light_9)

        self.horizontalLayout_139.addWidget(self.sys_state_stacked_wid_7)

        self.widget_40 = QWidget(self.widget_150)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout_72 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(2, 2, 2, 2)
        self.high_temp_input_4 = QDoubleSpinBox(self.widget_40)
        self.high_temp_input_4.setObjectName(u"high_temp_input_4")
        sizePolicy1.setHeightForWidth(self.high_temp_input_4.sizePolicy().hasHeightForWidth())
        self.high_temp_input_4.setSizePolicy(sizePolicy1)
        self.high_temp_input_4.setFont(font11)
        self.high_temp_input_4.setStyleSheet(u"")
        self.high_temp_input_4.setAlignment(Qt.AlignCenter)
        self.high_temp_input_4.setReadOnly(False)
        self.high_temp_input_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.high_temp_input_4.setDecimals(1)
        self.high_temp_input_4.setMaximum(999.000000000000000)
        self.high_temp_input_4.setValue(0.000000000000000)

        self.horizontalLayout_72.addWidget(self.high_temp_input_4)

        self.label_17 = QLabel(self.widget_40)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font12)
        self.label_17.setStyleSheet(u"border: none;\n"
"")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_72.addWidget(self.label_17)

        self.pv_value_displ_4 = QDoubleSpinBox(self.widget_40)
        self.pv_value_displ_4.setObjectName(u"pv_value_displ_4")
        sizePolicy1.setHeightForWidth(self.pv_value_displ_4.sizePolicy().hasHeightForWidth())
        self.pv_value_displ_4.setSizePolicy(sizePolicy1)
        self.pv_value_displ_4.setFont(font11)
        self.pv_value_displ_4.setStyleSheet(u"")
        self.pv_value_displ_4.setAlignment(Qt.AlignCenter)
        self.pv_value_displ_4.setReadOnly(True)
        self.pv_value_displ_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pv_value_displ_4.setDecimals(1)
        self.pv_value_displ_4.setMaximum(999.000000000000000)
        self.pv_value_displ_4.setValue(0.000000000000000)

        self.horizontalLayout_72.addWidget(self.pv_value_displ_4)

        self.label_18 = QLabel(self.widget_40)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font12)
        self.label_18.setStyleSheet(u"border: none;\n"
"")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_72.addWidget(self.label_18)

        self.low_temp_input_4 = QDoubleSpinBox(self.widget_40)
        self.low_temp_input_4.setObjectName(u"low_temp_input_4")
        sizePolicy1.setHeightForWidth(self.low_temp_input_4.sizePolicy().hasHeightForWidth())
        self.low_temp_input_4.setSizePolicy(sizePolicy1)
        self.low_temp_input_4.setFont(font11)
        self.low_temp_input_4.setStyleSheet(u"")
        self.low_temp_input_4.setAlignment(Qt.AlignCenter)
        self.low_temp_input_4.setReadOnly(False)
        self.low_temp_input_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.low_temp_input_4.setDecimals(1)
        self.low_temp_input_4.setMaximum(999.000000000000000)
        self.low_temp_input_4.setValue(0.000000000000000)

        self.horizontalLayout_72.addWidget(self.low_temp_input_4)


        self.horizontalLayout_139.addWidget(self.widget_40)

        self.sv_value_input_4 = QDoubleSpinBox(self.widget_150)
        self.sv_value_input_4.setObjectName(u"sv_value_input_4")
        sizePolicy1.setHeightForWidth(self.sv_value_input_4.sizePolicy().hasHeightForWidth())
        self.sv_value_input_4.setSizePolicy(sizePolicy1)
        self.sv_value_input_4.setFont(font11)
        self.sv_value_input_4.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.sv_value_input_4.setAlignment(Qt.AlignCenter)
        self.sv_value_input_4.setReadOnly(False)
        self.sv_value_input_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_input_4.setDecimals(1)
        self.sv_value_input_4.setMinimum(-999.000000000000000)
        self.sv_value_input_4.setMaximum(999.000000000000000)

        self.horizontalLayout_139.addWidget(self.sv_value_input_4)

        self.offset_value_input_4 = QDoubleSpinBox(self.widget_150)
        self.offset_value_input_4.setObjectName(u"offset_value_input_4")
        sizePolicy1.setHeightForWidth(self.offset_value_input_4.sizePolicy().hasHeightForWidth())
        self.offset_value_input_4.setSizePolicy(sizePolicy1)
        self.offset_value_input_4.setFont(font11)
        self.offset_value_input_4.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.offset_value_input_4.setAlignment(Qt.AlignCenter)
        self.offset_value_input_4.setReadOnly(True)
        self.offset_value_input_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.offset_value_input_4.setDecimals(1)
        self.offset_value_input_4.setMinimum(-999.000000000000000)
        self.offset_value_input_4.setMaximum(999.000000000000000)

        self.horizontalLayout_139.addWidget(self.offset_value_input_4)

        self.stackedWidget_10 = QStackedWidget(self.widget_150)
        self.stackedWidget_10.setObjectName(u"stackedWidget_10")
        self.celsius_displ_4 = QWidget()
        self.celsius_displ_4.setObjectName(u"celsius_displ_4")
        self.horizontalLayout_21 = QHBoxLayout(self.celsius_displ_4)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_183 = QLabel(self.celsius_displ_4)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setFont(font14)
        self.label_183.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_183.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_183)

        self.stackedWidget_10.addWidget(self.celsius_displ_4)
        self.fahrenheit_displ_4 = QWidget()
        self.fahrenheit_displ_4.setObjectName(u"fahrenheit_displ_4")
        self.horizontalLayout_22 = QHBoxLayout(self.fahrenheit_displ_4)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_184 = QLabel(self.fahrenheit_displ_4)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setFont(font14)
        self.label_184.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_184.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_184)

        self.stackedWidget_10.addWidget(self.fahrenheit_displ_4)

        self.horizontalLayout_139.addWidget(self.stackedWidget_10)

        self.horizontalLayout_139.setStretch(0, 1)
        self.horizontalLayout_139.setStretch(1, 2)
        self.horizontalLayout_139.setStretch(2, 1)
        self.horizontalLayout_139.setStretch(3, 1)

        self.verticalLayout_47.addWidget(self.widget_150)


        self.verticalLayout_46.addWidget(self.widget_27)


        self.horizontalLayout_59.addWidget(self.widget_22)


        self.verticalLayout_54.addWidget(self.widget_21)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_56.addWidget(self.scrollArea_4)

        self.verticalLayout_56.setStretch(1, 7)

        self.verticalLayout_10.addWidget(self.widget_temperature)

        self.widget_group_btn = QWidget(self.pressure_layout)
        self.widget_group_btn.setObjectName(u"widget_group_btn")
        self.widget_group_btn.setMaximumSize(QSize(16777215, 100))
        self.widget_group_btn.setFont(font)
        self.widget_group_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #10B981;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 12px 24px;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #059669;\n"
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
        self.horizontalLayout_14 = QHBoxLayout(self.widget_group_btn)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.stacked_btn_group_1 = QStackedWidget(self.widget_group_btn)
        self.stacked_btn_group_1.setObjectName(u"stacked_btn_group_1")
        self.btn_group_a = QWidget()
        self.btn_group_a.setObjectName(u"btn_group_a")
        self.horizontalLayout_41 = QHBoxLayout(self.btn_group_a)
        self.horizontalLayout_41.setSpacing(10)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.heat_btn_a = QPushButton(self.btn_group_a)
        self.heat_btn_a.setObjectName(u"heat_btn_a")
        sizePolicy.setHeightForWidth(self.heat_btn_a.sizePolicy().hasHeightForWidth())
        self.heat_btn_a.setSizePolicy(sizePolicy)
        self.heat_btn_a.setMaximumSize(QSize(16777215, 150))
        self.heat_btn_a.setFont(font7)
        self.heat_btn_a.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/newPrefix/heat.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.heat_btn_a.setIcon(icon12)
        self.heat_btn_a.setIconSize(QSize(30, 30))
        self.heat_btn_a.setCheckable(True)

        self.horizontalLayout_41.addWidget(self.heat_btn_a)

        self.refuel_btn_a = QPushButton(self.btn_group_a)
        self.refuel_btn_a.setObjectName(u"refuel_btn_a")
        sizePolicy.setHeightForWidth(self.refuel_btn_a.sizePolicy().hasHeightForWidth())
        self.refuel_btn_a.setSizePolicy(sizePolicy)
        self.refuel_btn_a.setMaximumSize(QSize(16777215, 150))
        self.refuel_btn_a.setFont(font7)
        self.refuel_btn_a.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u":/newPrefix/gas-pump-alt.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refuel_btn_a.setIcon(icon13)
        self.refuel_btn_a.setIconSize(QSize(30, 30))
        self.refuel_btn_a.setCheckable(True)

        self.horizontalLayout_41.addWidget(self.refuel_btn_a)

        self.vacuum_btn_a = QPushButton(self.btn_group_a)
        self.vacuum_btn_a.setObjectName(u"vacuum_btn_a")
        sizePolicy.setHeightForWidth(self.vacuum_btn_a.sizePolicy().hasHeightForWidth())
        self.vacuum_btn_a.setSizePolicy(sizePolicy)
        self.vacuum_btn_a.setMaximumSize(QSize(16777215, 150))
        self.vacuum_btn_a.setFont(font7)
        self.vacuum_btn_a.setStyleSheet(u"")
        icon14 = QIcon()
        icon14.addFile(u":/newPrefix/pump.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.vacuum_btn_a.setIcon(icon14)
        self.vacuum_btn_a.setIconSize(QSize(30, 30))
        self.vacuum_btn_a.setCheckable(True)

        self.horizontalLayout_41.addWidget(self.vacuum_btn_a)

        self.stacked_btn_group_1.addWidget(self.btn_group_a)
        self.btn_group_b = QWidget()
        self.btn_group_b.setObjectName(u"btn_group_b")
        self.horizontalLayout_43 = QHBoxLayout(self.btn_group_b)
        self.horizontalLayout_43.setSpacing(10)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.heat_btn_b = QPushButton(self.btn_group_b)
        self.heat_btn_b.setObjectName(u"heat_btn_b")
        sizePolicy.setHeightForWidth(self.heat_btn_b.sizePolicy().hasHeightForWidth())
        self.heat_btn_b.setSizePolicy(sizePolicy)
        self.heat_btn_b.setMaximumSize(QSize(16777215, 150))
        self.heat_btn_b.setFont(font7)
        self.heat_btn_b.setStyleSheet(u"")
        self.heat_btn_b.setCheckable(True)

        self.horizontalLayout_43.addWidget(self.heat_btn_b)

        self.refuel_btn_b = QPushButton(self.btn_group_b)
        self.refuel_btn_b.setObjectName(u"refuel_btn_b")
        sizePolicy.setHeightForWidth(self.refuel_btn_b.sizePolicy().hasHeightForWidth())
        self.refuel_btn_b.setSizePolicy(sizePolicy)
        self.refuel_btn_b.setMaximumSize(QSize(16777215, 150))
        self.refuel_btn_b.setFont(font7)
        self.refuel_btn_b.setStyleSheet(u"")
        self.refuel_btn_b.setCheckable(True)

        self.horizontalLayout_43.addWidget(self.refuel_btn_b)

        self.vacuum_btn_b = QPushButton(self.btn_group_b)
        self.vacuum_btn_b.setObjectName(u"vacuum_btn_b")
        sizePolicy.setHeightForWidth(self.vacuum_btn_b.sizePolicy().hasHeightForWidth())
        self.vacuum_btn_b.setSizePolicy(sizePolicy)
        self.vacuum_btn_b.setMaximumSize(QSize(16777215, 150))
        self.vacuum_btn_b.setFont(font7)
        self.vacuum_btn_b.setStyleSheet(u"")
        self.vacuum_btn_b.setCheckable(True)

        self.horizontalLayout_43.addWidget(self.vacuum_btn_b)

        self.stacked_btn_group_1.addWidget(self.btn_group_b)
        self.btn_group_c = QWidget()
        self.btn_group_c.setObjectName(u"btn_group_c")
        self.horizontalLayout_42 = QHBoxLayout(self.btn_group_c)
        self.horizontalLayout_42.setSpacing(10)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.heat_btn_c = QPushButton(self.btn_group_c)
        self.heat_btn_c.setObjectName(u"heat_btn_c")
        sizePolicy.setHeightForWidth(self.heat_btn_c.sizePolicy().hasHeightForWidth())
        self.heat_btn_c.setSizePolicy(sizePolicy)
        self.heat_btn_c.setMaximumSize(QSize(16777215, 150))
        self.heat_btn_c.setFont(font7)
        self.heat_btn_c.setStyleSheet(u"")
        self.heat_btn_c.setCheckable(True)

        self.horizontalLayout_42.addWidget(self.heat_btn_c)

        self.refuel_btn_c = QPushButton(self.btn_group_c)
        self.refuel_btn_c.setObjectName(u"refuel_btn_c")
        sizePolicy.setHeightForWidth(self.refuel_btn_c.sizePolicy().hasHeightForWidth())
        self.refuel_btn_c.setSizePolicy(sizePolicy)
        self.refuel_btn_c.setMaximumSize(QSize(16777215, 150))
        self.refuel_btn_c.setFont(font7)
        self.refuel_btn_c.setStyleSheet(u"")
        self.refuel_btn_c.setCheckable(True)

        self.horizontalLayout_42.addWidget(self.refuel_btn_c)

        self.vacuum_btn_c = QPushButton(self.btn_group_c)
        self.vacuum_btn_c.setObjectName(u"vacuum_btn_c")
        sizePolicy.setHeightForWidth(self.vacuum_btn_c.sizePolicy().hasHeightForWidth())
        self.vacuum_btn_c.setSizePolicy(sizePolicy)
        self.vacuum_btn_c.setMaximumSize(QSize(16777215, 150))
        self.vacuum_btn_c.setFont(font7)
        self.vacuum_btn_c.setStyleSheet(u"")
        self.vacuum_btn_c.setCheckable(True)

        self.horizontalLayout_42.addWidget(self.vacuum_btn_c)

        self.stacked_btn_group_1.addWidget(self.btn_group_c)

        self.horizontalLayout_14.addWidget(self.stacked_btn_group_1)

        self.back_home_btn = QPushButton(self.widget_group_btn)
        self.back_home_btn.setObjectName(u"back_home_btn")
        sizePolicy.setHeightForWidth(self.back_home_btn.sizePolicy().hasHeightForWidth())
        self.back_home_btn.setSizePolicy(sizePolicy)
        self.back_home_btn.setFont(font7)
        self.back_home_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #0B7EC8;\n"
"    border: 1px solid #0B7EC8;\n"
"    padding: 12px 24px;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #F0F9FF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #E0F2FE;\n"
"}")

        self.horizontalLayout_14.addWidget(self.back_home_btn)

        self.horizontalLayout_14.setStretch(0, 3)
        self.horizontalLayout_14.setStretch(1, 1)

        self.verticalLayout_10.addWidget(self.widget_group_btn)

        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 4)
        self.verticalLayout_10.setStretch(2, 4)
        self.verticalLayout_10.setStretch(3, 1)
        self.stacked_pressure_page.addWidget(self.pressure_layout)

        self.verticalLayout_6.addWidget(self.stacked_pressure_page)

        self.stackedWidget.addWidget(self.pressure_page)
        self.temperature_page = QWidget()
        self.temperature_page.setObjectName(u"temperature_page")
        self.stackedWidget.addWidget(self.temperature_page)
        self.device_page = QWidget()
        self.device_page.setObjectName(u"device_page")
        self.verticalLayout_13 = QVBoxLayout(self.device_page)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.ver_layout_device = QVBoxLayout()
        self.ver_layout_device.setObjectName(u"ver_layout_device")
        self.device_frame = QFrame(self.device_page)
        self.device_frame.setObjectName(u"device_frame")
        self.device_frame.setStyleSheet(u"QFrame {\n"
"    background-color: white;\n"
"    border-radius: 12px;\n"
"    border: 1px solid #E5E5E5;\n"
"    margin: 5px;\n"
"}\n"
"QFrame:hover {\n"
"    border: 1px solid #0B7EC8;\n"
"}")
        self.device_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_24 = QVBoxLayout(self.device_frame)
        self.verticalLayout_24.setSpacing(15)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(20, 15, 20, 15)
        self.connection_status_layout = QHBoxLayout()
        self.connection_status_layout.setObjectName(u"connection_status_layout")
        self.device_icon = QLabel(self.device_frame)
        self.device_icon.setObjectName(u"device_icon")
        self.device_icon.setStyleSheet(u"font-size: 24px; \n"
"color: #0B7EC8;\n"
"border: none;\n"
"image:url(:/newPrefix/digital.png)")

        self.connection_status_layout.addWidget(self.device_icon)

        self.device_info_layout = QVBoxLayout()
        self.device_info_layout.setSpacing(2)
        self.device_info_layout.setObjectName(u"device_info_layout")
        self.name_device_label = QLabel(self.device_frame)
        self.name_device_label.setObjectName(u"name_device_label")
        self.name_device_label.setStyleSheet(u"font-size: 16px;\n"
"font-weight: 600;\n"
"color: #1E293B;\n"
"border-radius: 10px")

        self.device_info_layout.addWidget(self.name_device_label)

        self.type_device_label = QLabel(self.device_frame)
        self.type_device_label.setObjectName(u"type_device_label")
        self.type_device_label.setStyleSheet(u"font-size: 14px;\n"
"color: #64748B;\n"
"border: none;")

        self.device_info_layout.addWidget(self.type_device_label)


        self.connection_status_layout.addLayout(self.device_info_layout)

        self.status_device_label = QLabel(self.device_frame)
        self.status_device_label.setObjectName(u"status_device_label")
        self.status_device_label.setStyleSheet(u"font-size: 12px;\n"
"font-weight: 500;\n"
"color: #EF4444;")
        self.status_device_label.setTextFormat(Qt.RichText)

        self.connection_status_layout.addWidget(self.status_device_label)

        self.connection_status_layout.setStretch(0, 1)
        self.connection_status_layout.setStretch(1, 3)
        self.connection_status_layout.setStretch(2, 2)

        self.verticalLayout_24.addLayout(self.connection_status_layout)

        self.connection_group = QGroupBox(self.device_frame)
        self.connection_group.setObjectName(u"connection_group")
        self.connection_group.setFont(font6)
        self.connection_group.setStyleSheet(u"QGroupBox {\n"
"    font-weight: 500;\n"
"    border: 1px solid #E5E5E5;\n"
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
"}\n"
"\n"
"QSpinBox {\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    font-size: 18px;\n"
"    background-color: #F9FAFB;\n"
"    min-width: 100px;\n"
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
"    font-size: 18px;\n"
"    background-color: #F9FAFB;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"    background-color: white;\n"
"}")
        self.gridLayout_4 = QGridLayout(self.connection_group)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.plc_ip_address_edit = QLineEdit(self.connection_group)
        self.plc_ip_address_edit.setObjectName(u"plc_ip_address_edit")
        sizePolicy.setHeightForWidth(self.plc_ip_address_edit.sizePolicy().hasHeightForWidth())
        self.plc_ip_address_edit.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.plc_ip_address_edit, 0, 1, 1, 1)

        self.rack_input = QSpinBox(self.connection_group)
        self.rack_input.setObjectName(u"rack_input")
        sizePolicy.setHeightForWidth(self.rack_input.sizePolicy().hasHeightForWidth())
        self.rack_input.setSizePolicy(sizePolicy)
        self.rack_input.setMinimumSize(QSize(126, 0))
        self.rack_input.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout_4.addWidget(self.rack_input, 1, 1, 1, 1)

        self.slot_label = QLabel(self.connection_group)
        self.slot_label.setObjectName(u"slot_label")
        self.slot_label.setFont(font5)

        self.gridLayout_4.addWidget(self.slot_label, 2, 0, 1, 1)

        self.slot_input = QSpinBox(self.connection_group)
        self.slot_input.setObjectName(u"slot_input")
        sizePolicy.setHeightForWidth(self.slot_input.sizePolicy().hasHeightForWidth())
        self.slot_input.setSizePolicy(sizePolicy)
        self.slot_input.setMinimumSize(QSize(126, 0))
        self.slot_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.slot_input.setValue(1)

        self.gridLayout_4.addWidget(self.slot_input, 2, 1, 1, 1)

        self.slot_label_4 = QLabel(self.connection_group)
        self.slot_label_4.setObjectName(u"slot_label_4")
        self.slot_label_4.setFont(font5)

        self.gridLayout_4.addWidget(self.slot_label_4, 4, 0, 1, 1)

        self.plc_ip_address = QLabel(self.connection_group)
        self.plc_ip_address.setObjectName(u"plc_ip_address")
        self.plc_ip_address.setFont(font5)

        self.gridLayout_4.addWidget(self.plc_ip_address, 0, 0, 1, 1)

        self.rack_label = QLabel(self.connection_group)
        self.rack_label.setObjectName(u"rack_label")
        self.rack_label.setFont(font5)

        self.gridLayout_4.addWidget(self.rack_label, 1, 0, 1, 1)

        self.slot_label_2 = QLabel(self.connection_group)
        self.slot_label_2.setObjectName(u"slot_label_2")
        self.slot_label_2.setFont(font5)

        self.gridLayout_4.addWidget(self.slot_label_2, 3, 0, 1, 1)

        self.slot_input_2 = QSpinBox(self.connection_group)
        self.slot_input_2.setObjectName(u"slot_input_2")
        sizePolicy.setHeightForWidth(self.slot_input_2.sizePolicy().hasHeightForWidth())
        self.slot_input_2.setSizePolicy(sizePolicy)
        self.slot_input_2.setMinimumSize(QSize(126, 0))
        self.slot_input_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.slot_input_2.setValue(1)

        self.gridLayout_4.addWidget(self.slot_input_2, 3, 1, 1, 1)

        self.slot_input_3 = QSpinBox(self.connection_group)
        self.slot_input_3.setObjectName(u"slot_input_3")
        sizePolicy.setHeightForWidth(self.slot_input_3.sizePolicy().hasHeightForWidth())
        self.slot_input_3.setSizePolicy(sizePolicy)
        self.slot_input_3.setMinimumSize(QSize(126, 0))
        self.slot_input_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.slot_input_3.setValue(1)

        self.gridLayout_4.addWidget(self.slot_input_3, 5, 1, 1, 1)

        self.slot_input_4 = QSpinBox(self.connection_group)
        self.slot_input_4.setObjectName(u"slot_input_4")
        sizePolicy.setHeightForWidth(self.slot_input_4.sizePolicy().hasHeightForWidth())
        self.slot_input_4.setSizePolicy(sizePolicy)
        self.slot_input_4.setMinimumSize(QSize(126, 0))
        self.slot_input_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.slot_input_4.setValue(1)

        self.gridLayout_4.addWidget(self.slot_input_4, 4, 1, 1, 1)

        self.slot_label_3 = QLabel(self.connection_group)
        self.slot_label_3.setObjectName(u"slot_label_3")
        self.slot_label_3.setFont(font5)

        self.gridLayout_4.addWidget(self.slot_label_3, 5, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.connection_group)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_4.addWidget(self.pushButton_4, 0, 2, 1, 1)


        self.verticalLayout_24.addWidget(self.connection_group)

        self.connection_btn_layout = QHBoxLayout()
        self.connection_btn_layout.setObjectName(u"connection_btn_layout")
        self.plc_connect = QPushButton(self.device_frame)
        self.plc_connect.setObjectName(u"plc_connect")
        sizePolicy.setHeightForWidth(self.plc_connect.sizePolicy().hasHeightForWidth())
        self.plc_connect.setSizePolicy(sizePolicy)
        self.plc_connect.setStyleSheet(u"QPushButton {\n"
"    background-color: #10B981;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 12px 24px;\n"
"    border-radius: 8px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #059669;\n"
"}")

        self.connection_btn_layout.addWidget(self.plc_connect)

        self.dis_plc = QPushButton(self.device_frame)
        self.dis_plc.setObjectName(u"dis_plc")
        sizePolicy.setHeightForWidth(self.dis_plc.sizePolicy().hasHeightForWidth())
        self.dis_plc.setSizePolicy(sizePolicy)
        self.dis_plc.setStyleSheet(u"QPushButton {\n"
"    background-color: #EF4444;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 12px 24px;\n"
"    border-radius: 8px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #DC2626;\n"
"}")

        self.connection_btn_layout.addWidget(self.dis_plc)


        self.verticalLayout_24.addLayout(self.connection_btn_layout)

        self.verticalLayout_24.setStretch(0, 2)
        self.verticalLayout_24.setStretch(1, 5)
        self.verticalLayout_24.setStretch(2, 1)

        self.ver_layout_device.addWidget(self.device_frame)


        self.verticalLayout_13.addLayout(self.ver_layout_device)

        self.stackedWidget.addWidget(self.device_page)
        self.chart_page = QWidget()
        self.chart_page.setObjectName(u"chart_page")
        self.verticalLayout_62 = QVBoxLayout(self.chart_page)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.dashboard_stacked_widget = QStackedWidget(self.chart_page)
        self.dashboard_stacked_widget.setObjectName(u"dashboard_stacked_widget")
        self.overall_page = QWidget()
        self.overall_page.setObjectName(u"overall_page")
        self.verticalLayout_12 = QVBoxLayout(self.overall_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.card_widgets = QWidget(self.overall_page)
        self.card_widgets.setObjectName(u"card_widgets")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.card_widgets.sizePolicy().hasHeightForWidth())
        self.card_widgets.setSizePolicy(sizePolicy2)
        self.card_widgets.setStyleSheet(u"QFrame {\n"
"    background-color: white;\n"
"    border-radius: 5px;\n"
"    border: 1px solid #E5E5E5;\n"
"    \n"
"}\n"
"QFrame:hover {\n"
"    border: 1px solid #0B7EC8;\n"
"    \n"
"}")
        self.gridLayout = QGridLayout(self.card_widgets)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.card_frame = QFrame(self.card_widgets)
        self.card_frame.setObjectName(u"card_frame")
        self.card_frame.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B7EC8;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 8px 18px;\n"
"    border-radius: 6px;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0968A3;\n"
"}")
        self.card_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_18 = QVBoxLayout(self.card_frame)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(10, 10, 10, 10)
        self.card_content = QVBoxLayout()
        self.card_content.setObjectName(u"card_content")

        self.verticalLayout_18.addLayout(self.card_content)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.card_label = QLabel(self.card_frame)
        self.card_label.setObjectName(u"card_label")
        self.card_label.setStyleSheet(u"font-size: 14px;\n"
"color: #555555;\n"
"font-weight: 500;\n"
"margin-top: 8px;\n"
"border: none;")

        self.horizontalLayout_56.addWidget(self.card_label, 0, Qt.AlignHCenter)

        self.card_btn = QPushButton(self.card_frame)
        self.card_btn.setObjectName(u"card_btn")
        sizePolicy.setHeightForWidth(self.card_btn.sizePolicy().hasHeightForWidth())
        self.card_btn.setSizePolicy(sizePolicy)
        self.card_btn.setMinimumSize(QSize(0, 0))
        self.card_btn.setStyleSheet(u"")

        self.horizontalLayout_56.addWidget(self.card_btn, 0, Qt.AlignRight)


        self.verticalLayout_18.addLayout(self.horizontalLayout_56)

        self.verticalLayout_18.setStretch(0, 8)
        self.verticalLayout_18.setStretch(1, 1)

        self.gridLayout.addWidget(self.card_frame, 1, 0, 1, 1)

        self.card_frame_2 = QFrame(self.card_widgets)
        self.card_frame_2.setObjectName(u"card_frame_2")
        self.card_frame_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B7EC8;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 8px 18px;\n"
"    border-radius: 6px;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0968A3;\n"
"}")
        self.card_frame_2.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_20 = QVBoxLayout(self.card_frame_2)
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(10, 10, 10, 10)
        self.card_content_2 = QVBoxLayout()
        self.card_content_2.setObjectName(u"card_content_2")

        self.verticalLayout_20.addLayout(self.card_content_2)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.card_label_2 = QLabel(self.card_frame_2)
        self.card_label_2.setObjectName(u"card_label_2")
        self.card_label_2.setStyleSheet(u"font-size: 14px;\n"
"color: #555555;\n"
"font-weight: 500;\n"
"margin-top: 8px;\n"
"border: none;")

        self.horizontalLayout_57.addWidget(self.card_label_2, 0, Qt.AlignHCenter)

        self.card_btn_2 = QPushButton(self.card_frame_2)
        self.card_btn_2.setObjectName(u"card_btn_2")
        sizePolicy.setHeightForWidth(self.card_btn_2.sizePolicy().hasHeightForWidth())
        self.card_btn_2.setSizePolicy(sizePolicy)
        self.card_btn_2.setMinimumSize(QSize(0, 0))
        self.card_btn_2.setStyleSheet(u"")

        self.horizontalLayout_57.addWidget(self.card_btn_2, 0, Qt.AlignRight)


        self.verticalLayout_20.addLayout(self.horizontalLayout_57)

        self.verticalLayout_20.setStretch(0, 8)
        self.verticalLayout_20.setStretch(1, 1)

        self.gridLayout.addWidget(self.card_frame_2, 1, 1, 1, 1)

        self.stats_frame = QFrame(self.card_widgets)
        self.stats_frame.setObjectName(u"stats_frame")
        self.stats_frame.setStyleSheet(u"QFrame {\n"
"    background-color: white;\n"
"    border-radius: 12px;\n"
"    border: 1px solid #E5E5E5;\n"
"}\n"
"alignment: right;")
        self.stats_frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_58 = QHBoxLayout(self.stats_frame)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 10, 0, 10)
        self.stats_widget = QWidget(self.stats_frame)
        self.stats_widget.setObjectName(u"stats_widget")
        self.verticalLayout_22 = QVBoxLayout(self.stats_widget)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(15, 15, 15, 15)
        self.value_label = QPushButton(self.stats_widget)
        self.value_label.setObjectName(u"value_label")

        self.verticalLayout_22.addWidget(self.value_label)

        self.unit_label = QLabel(self.stats_widget)
        self.unit_label.setObjectName(u"unit_label")
        self.unit_label.setStyleSheet(u"font-size: 13px;\n"
"color: #888888;\n"
"font-weight: 500;\n"
"border: none;")
        self.unit_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.unit_label)

        self.title_label_stats = QLabel(self.stats_widget)
        self.title_label_stats.setObjectName(u"title_label_stats")
        self.title_label_stats.setStyleSheet(u"font-size: 14px;\n"
"color: #555555;\n"
"font-weight: 500;\n"
"margin-top: 8px;\n"
"border: none;")
        self.title_label_stats.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.title_label_stats)


        self.horizontalLayout_58.addWidget(self.stats_widget)

        self.stats_widget_2 = QWidget(self.stats_frame)
        self.stats_widget_2.setObjectName(u"stats_widget_2")
        self.verticalLayout_23 = QVBoxLayout(self.stats_widget_2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(15, 15, 15, 15)
        self.value_label_2 = QPushButton(self.stats_widget_2)
        self.value_label_2.setObjectName(u"value_label_2")

        self.verticalLayout_23.addWidget(self.value_label_2)

        self.unit_label_2 = QLabel(self.stats_widget_2)
        self.unit_label_2.setObjectName(u"unit_label_2")
        self.unit_label_2.setStyleSheet(u"font-size: 13px;\n"
"color: #888888;\n"
"font-weight: 500;\n"
"border: none;")
        self.unit_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.unit_label_2)

        self.title_label_stats_2 = QLabel(self.stats_widget_2)
        self.title_label_stats_2.setObjectName(u"title_label_stats_2")
        self.title_label_stats_2.setStyleSheet(u"font-size: 14px;\n"
"color: #555555;\n"
"font-weight: 500;\n"
"margin-top: 8px;\n"
"border: none;")
        self.title_label_stats_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.title_label_stats_2)


        self.horizontalLayout_58.addWidget(self.stats_widget_2)

        self.stats_widget_3 = QWidget(self.stats_frame)
        self.stats_widget_3.setObjectName(u"stats_widget_3")
        self.verticalLayout_57 = QVBoxLayout(self.stats_widget_3)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(15, 15, 15, 15)
        self.value_label_3 = QPushButton(self.stats_widget_3)
        self.value_label_3.setObjectName(u"value_label_3")

        self.verticalLayout_57.addWidget(self.value_label_3)

        self.unit_label_3 = QLabel(self.stats_widget_3)
        self.unit_label_3.setObjectName(u"unit_label_3")
        self.unit_label_3.setStyleSheet(u"font-size: 13px;\n"
"color: #888888;\n"
"font-weight: 500;\n"
"border: none;")
        self.unit_label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_57.addWidget(self.unit_label_3)

        self.title_label_stats_3 = QLabel(self.stats_widget_3)
        self.title_label_stats_3.setObjectName(u"title_label_stats_3")
        self.title_label_stats_3.setStyleSheet(u"font-size: 14px;\n"
"color: #555555;\n"
"font-weight: 500;\n"
"margin-top: 8px;\n"
"border: none;")
        self.title_label_stats_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_57.addWidget(self.title_label_stats_3)


        self.horizontalLayout_58.addWidget(self.stats_widget_3)

        self.stats_widget_4 = QWidget(self.stats_frame)
        self.stats_widget_4.setObjectName(u"stats_widget_4")
        self.verticalLayout_58 = QVBoxLayout(self.stats_widget_4)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(15, 15, 15, 15)
        self.value_label_4 = QPushButton(self.stats_widget_4)
        self.value_label_4.setObjectName(u"value_label_4")

        self.verticalLayout_58.addWidget(self.value_label_4)

        self.unit_label_4 = QLabel(self.stats_widget_4)
        self.unit_label_4.setObjectName(u"unit_label_4")
        self.unit_label_4.setStyleSheet(u"font-size: 13px;\n"
"color: #888888;\n"
"font-weight: 500;\n"
"border: none;")
        self.unit_label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_58.addWidget(self.unit_label_4)

        self.title_label_stats_4 = QLabel(self.stats_widget_4)
        self.title_label_stats_4.setObjectName(u"title_label_stats_4")
        self.title_label_stats_4.setStyleSheet(u"font-size: 14px;\n"
"color: #555555;\n"
"font-weight: 500;\n"
"margin-top: 8px;\n"
"border: none;")
        self.title_label_stats_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_58.addWidget(self.title_label_stats_4)


        self.horizontalLayout_58.addWidget(self.stats_widget_4)


        self.gridLayout.addWidget(self.stats_frame, 0, 0, 1, 2)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 5)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout_12.addWidget(self.card_widgets)

        self.dashboard_stacked_widget.addWidget(self.overall_page)
        self.list_page = QWidget()
        self.list_page.setObjectName(u"list_page")
        self.verticalLayout_59 = QVBoxLayout(self.list_page)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.stacked_list_report = QStackedWidget(self.list_page)
        self.stacked_list_report.setObjectName(u"stacked_list_report")
        self.list_err_page = QWidget()
        self.list_err_page.setObjectName(u"list_err_page")
        self.verticalLayout_60 = QVBoxLayout(self.list_err_page)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.list_err = QTableWidget(self.list_err_page)
        if (self.list_err.columnCount() < 4):
            self.list_err.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setText(u"0")
        self.list_err.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setText(u"1")
        self.list_err.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setText(u"2")
        self.list_err.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.list_err.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.list_err.rowCount() < 24):
            self.list_err.setRowCount(24)
        font15 = QFont()
        font15.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font15)
        self.list_err.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(16, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(17, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(18, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(19, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(20, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(21, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(22, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.list_err.setVerticalHeaderItem(23, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setText(u"No.")
        __qtablewidgetitem28.setFont(font6)
        self.list_err.setItem(0, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font6)
        self.list_err.setItem(0, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font6)
        self.list_err.setItem(0, 2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font6)
        self.list_err.setItem(0, 3, __qtablewidgetitem31)
        self.list_err.setObjectName(u"list_err")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.list_err.sizePolicy().hasHeightForWidth())
        self.list_err.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(255, 252, 253, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.list_err.setPalette(palette)
        self.list_err.setStyleSheet(u"QTableWidget {	\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 252, 253);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"	\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollArea {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: #F1F5F9;\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #CBD5E1;\n"
"    border-radius: 5px;\n"
"    min-height: 30px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: #94A3B8;\n"
"}\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60"
                        ");\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.list_err.setFrameShape(QFrame.NoFrame)
        self.list_err.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.list_err.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.list_err.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_err.setAlternatingRowColors(False)
        self.list_err.setSelectionMode(QAbstractItemView.NoSelection)
        self.list_err.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.list_err.setShowGrid(True)
        self.list_err.setGridStyle(Qt.SolidLine)
        self.list_err.setSortingEnabled(False)
        self.list_err.horizontalHeader().setVisible(False)
        self.list_err.horizontalHeader().setCascadingSectionResizes(True)
        self.list_err.horizontalHeader().setDefaultSectionSize(200)
        self.list_err.horizontalHeader().setStretchLastSection(True)
        self.list_err.verticalHeader().setVisible(False)
        self.list_err.verticalHeader().setCascadingSectionResizes(False)
        self.list_err.verticalHeader().setMinimumSectionSize(30)
        self.list_err.verticalHeader().setDefaultSectionSize(40)
        self.list_err.verticalHeader().setHighlightSections(False)
        self.list_err.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_60.addWidget(self.list_err)

        self.stacked_list_report.addWidget(self.list_err_page)
        self.list_done_page = QWidget()
        self.list_done_page.setObjectName(u"list_done_page")
        self.verticalLayout_61 = QVBoxLayout(self.list_done_page)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.list_done = QTableWidget(self.list_done_page)
        if (self.list_done.columnCount() < 5):
            self.list_done.setColumnCount(5)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setText(u"0")
        self.list_done.setHorizontalHeaderItem(0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setText(u"1")
        self.list_done.setHorizontalHeaderItem(1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setText(u"2")
        self.list_done.setHorizontalHeaderItem(2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setText(u"3")
        self.list_done.setHorizontalHeaderItem(3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.list_done.setHorizontalHeaderItem(4, __qtablewidgetitem36)
        if (self.list_done.rowCount() < 25):
            self.list_done.setRowCount(25)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFont(font15)
        self.list_done.setVerticalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(5, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(6, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(7, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(8, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(9, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(10, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(11, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(12, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(13, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(14, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(15, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(16, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(17, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(18, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(19, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(20, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(21, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(22, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(23, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.list_done.setVerticalHeaderItem(24, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setText(u"No.")
        __qtablewidgetitem62.setFont(font6)
        self.list_done.setItem(0, 0, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setFont(font6)
        self.list_done.setItem(0, 1, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setFont(font6)
        self.list_done.setItem(0, 2, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setFont(font6)
        self.list_done.setItem(0, 3, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setFont(font6)
        self.list_done.setItem(0, 4, __qtablewidgetitem66)
        self.list_done.setObjectName(u"list_done")
        sizePolicy3.setHeightForWidth(self.list_done.sizePolicy().hasHeightForWidth())
        self.list_done.setSizePolicy(sizePolicy3)
        palette1 = QPalette()
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.list_done.setPalette(palette1)
        self.list_done.setStyleSheet(u"QTableWidget {	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 252, 253);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"	\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollArea {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: #F1F5F9;\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #CBD5E1;\n"
"    border-radius: 5px;\n"
"    min-height: 30px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: #94A3B8;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: none;\n"
"    background-color: #F1F5F9;\n"
"    height: 10px;\n"
"    border-rad"
                        "ius: 5px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #CBD5E1;\n"
"    border-radius: 5px;\n"
"    min-height: 30px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: #94A3B8;\n"
"}\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.list_done.setFrameShape(QFrame.NoFrame)
        self.list_done.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.list_done.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.list_done.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_done.setAlternatingRowColors(False)
        self.list_done.setSelectionMode(QAbstractItemView.NoSelection)
        self.list_done.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.list_done.setShowGrid(True)
        self.list_done.setGridStyle(Qt.SolidLine)
        self.list_done.setSortingEnabled(False)
        self.list_done.horizontalHeader().setVisible(False)
        self.list_done.horizontalHeader().setCascadingSectionResizes(True)
        self.list_done.horizontalHeader().setDefaultSectionSize(150)
        self.list_done.horizontalHeader().setStretchLastSection(True)
        self.list_done.verticalHeader().setVisible(False)
        self.list_done.verticalHeader().setCascadingSectionResizes(False)
        self.list_done.verticalHeader().setMinimumSectionSize(30)
        self.list_done.verticalHeader().setDefaultSectionSize(40)
        self.list_done.verticalHeader().setHighlightSections(False)
        self.list_done.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_61.addWidget(self.list_done)

        self.stacked_list_report.addWidget(self.list_done_page)

        self.verticalLayout_59.addWidget(self.stacked_list_report)

        self.list_query_btn = QHBoxLayout()
        self.list_query_btn.setObjectName(u"list_query_btn")
        self.next_page_btn = QPushButton(self.list_page)
        self.next_page_btn.setObjectName(u"next_page_btn")
        sizePolicy.setHeightForWidth(self.next_page_btn.sizePolicy().hasHeightForWidth())
        self.next_page_btn.setSizePolicy(sizePolicy)
        self.next_page_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #0B7EC8;\n"
"    border: 1px solid #0B7EC8;\n"
"    padding: 12px 24px;\n"
"    border-radius: 8px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #F0F9FF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #E0F2FE;\n"
"}")

        self.list_query_btn.addWidget(self.next_page_btn)

        self.backward_btn = QPushButton(self.list_page)
        self.backward_btn.setObjectName(u"backward_btn")
        sizePolicy.setHeightForWidth(self.backward_btn.sizePolicy().hasHeightForWidth())
        self.backward_btn.setSizePolicy(sizePolicy)
        self.backward_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #0B7EC8;\n"
"    border: 1px solid #0B7EC8;\n"
"    padding: 12px 24px;\n"
"    border-radius: 8px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #F0F9FF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #E0F2FE;\n"
"}")

        self.list_query_btn.addWidget(self.backward_btn)


        self.verticalLayout_59.addLayout(self.list_query_btn)

        self.dashboard_stacked_widget.addWidget(self.list_page)

        self.verticalLayout_62.addWidget(self.dashboard_stacked_widget)

        self.stackedWidget.addWidget(self.chart_page)

        self.horizontalLayout_2.addWidget(self.stackedWidget)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 6)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.body_frame)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 12)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.stacked_group_name.setCurrentIndex(0)
        self.sys_state_stacked_wid_10.setCurrentIndex(0)
        self.stacked_group_combox.setCurrentIndex(1)
        self.stacked_cel_fah_switch.setCurrentIndex(0)
        self.sys_state_stacked_wid_8.setCurrentIndex(1)
        self.stackedWidget_7.setCurrentIndex(0)
        self.sys_state_stacked_wid_9.setCurrentIndex(1)
        self.stackedWidget_8.setCurrentIndex(0)
        self.sys_state_stacked_wid_6.setCurrentIndex(1)
        self.stackedWidget_9.setCurrentIndex(0)
        self.sys_state_stacked_wid_7.setCurrentIndex(1)
        self.stackedWidget_10.setCurrentIndex(0)
        self.stacked_btn_group_1.setCurrentIndex(2)
        self.dashboard_stacked_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tech-Link - Production System", None))
        self.company_name.setText(QCoreApplication.translate("MainWindow", u"TECH-LINK", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Language:", None))
        self.language_selection_combox.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))
        self.language_selection_combox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e2d\u56fd", None))

        self.date_displ.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy h:mm AP", None))
        self.home_page_btn.setText(QCoreApplication.translate("MainWindow", u" Home", None))
        self.pressure_page_btn.setText(QCoreApplication.translate("MainWindow", u" Pressure", None))
        self.temperature_page_btn.setText(QCoreApplication.translate("MainWindow", u" Oven", None))
        self.device_page_btn.setText(QCoreApplication.translate("MainWindow", u" Device", None))
        self.chart_page_btn.setText(QCoreApplication.translate("MainWindow", u" History", None))
        self.open_side_menu_btn.setText("")
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"Group A", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"Group B", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"Group C", None))
        self.running_label.setText(QCoreApplication.translate("MainWindow", u"\U0001f7e2 Running", None))
        self.stop_label.setText(QCoreApplication.translate("MainWindow", u"\U0001f7e2 Stop", None))
        self.previus_group_page_btn.setText("")
        self.next_group_page_btn.setText("")
        self.clear_data_btn.setText(QCoreApplication.translate("MainWindow", u" Clear Data", None))
        self.save_data_btn.setText(QCoreApplication.translate("MainWindow", u" Save Data", None))
        self.data_selection_combobox_a.setItemText(0, QCoreApplication.translate("MainWindow", u"Group Data A", None))

        self.data_selection_combobox_a.setCurrentText(QCoreApplication.translate("MainWindow", u"Group Data A", None))
        self.data_selection_combobox_b.setItemText(0, QCoreApplication.translate("MainWindow", u"Group Data B", None))

        self.data_selection_combobox_b.setCurrentText(QCoreApplication.translate("MainWindow", u"Group Data B", None))
        self.data_selection_combobox_c.setItemText(0, QCoreApplication.translate("MainWindow", u"Group Data C", None))

        self.data_selection_combobox_c.setCurrentText(QCoreApplication.translate("MainWindow", u"Group Data C", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u" Pressure", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Total Cycle:", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Refueling:", None))
        self.refuel_start_time_input.setPrefix(QCoreApplication.translate("MainWindow", u"Start: ", None))
        self.refuel_start_time_input.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.refuel_end_time_input.setPrefix(QCoreApplication.translate("MainWindow", u"End: ", None))
        self.refuel_end_time_input.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Filling:", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"G.Holding:", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Bleeding:", None))
        self.filling_time_input.setPrefix("")
        self.filling_time_input.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.g_holding_time_input.setPrefix("")
        self.g_holding_time_input.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.bleeding_time_input.setPrefix("")
        self.bleeding_time_input.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"Pressure:", None))
        self.pressure_pv_displ.setPrefix(QCoreApplication.translate("MainWindow", u"PV: ", None))
        self.pressure_pv_displ.setSuffix(QCoreApplication.translate("MainWindow", u" Bar", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pressure_sv_input.setPrefix(QCoreApplication.translate("MainWindow", u"SV: ", None))
        self.pressure_sv_input.setSuffix(QCoreApplication.translate("MainWindow", u" Bar", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u" Temperature", None))
        self.celsius_btn.setText(QCoreApplication.translate("MainWindow", u" \u00b0C", None))
        self.fahrenheit_btn.setText(QCoreApplication.translate("MainWindow", u" \u00b0F", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"H.Alm", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"PV", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"L.Alm ", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"SV", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.label_271.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Air Inlet:", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Front:", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Middle:", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Back:", None))
        self.running_label_10.setText(QCoreApplication.translate("MainWindow", u"\U0001f7e2 Stable", None))
        self.waiting_label_10.setText(QCoreApplication.translate("MainWindow", u"\U0001f7e2 Heating", None))
        self.error_label_10.setText(QCoreApplication.translate("MainWindow", u"\U0001f7e2 Out Range", None))
        self.high_temp_input_1.setPrefix("")
        self.high_temp_input_1.setSuffix("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pv_value_displ_1.setPrefix("")
        self.pv_value_displ_1.setSuffix("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.low_temp_input_1.setPrefix("")
        self.low_temp_input_1.setSuffix("")
        self.sv_value_input_1.setPrefix("")
        self.sv_value_input_1.setSuffix("")
        self.offset_value_input_1.setPrefix("")
        self.offset_value_input_1.setSuffix("")
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.running_label_11.setText(QCoreApplication.translate("MainWindow", u"\U0001f7e2 Stable", None))
        self.waiting_label_11.setText(QCoreApplication.translate("MainWindow", u"\U0001f7e2 Heating", None))
        self.error_label_11.setText(QCoreApplication.translate("MainWindow", u"\U0001f7e2 Out Range", None))
        self.high_temp_input_2.setPrefix("")
        self.high_temp_input_2.setSuffix("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pv_value_displ_2.setPrefix("")
        self.pv_value_displ_2.setSuffix("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.low_temp_input_2.setPrefix("")
        self.low_temp_input_2.setSuffix("")
        self.sv_value_input_2.setPrefix("")
        self.sv_value_input_2.setSuffix("")
        self.offset_value_input_2.setPrefix("")
        self.offset_value_input_2.setSuffix("")
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.running_label_8.setText(QCoreApplication.translate("MainWindow", u"\U0001f7e2 Stable", None))
        self.waiting_label_8.setText(QCoreApplication.translate("MainWindow", u"\U0001f7e2 Heating", None))
        self.error_label_8.setText(QCoreApplication.translate("MainWindow", u"\U0001f7e2 Out Range", None))
        self.high_temp_input_3.setPrefix("")
        self.high_temp_input_3.setSuffix("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pv_value_displ_3.setPrefix("")
        self.pv_value_displ_3.setSuffix("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.low_temp_input_3.setPrefix("")
        self.low_temp_input_3.setSuffix("")
        self.sv_value_input_3.setPrefix("")
        self.sv_value_input_3.setSuffix("")
        self.offset_value_input_3.setPrefix("")
        self.offset_value_input_3.setSuffix("")
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.running_label_9.setText(QCoreApplication.translate("MainWindow", u"\U0001f7e2 Stable", None))
        self.waiting_label_9.setText(QCoreApplication.translate("MainWindow", u"\U0001f7e2 Heating", None))
        self.error_label_9.setText(QCoreApplication.translate("MainWindow", u"\U0001f7e2 Out Range", None))
        self.high_temp_input_4.setPrefix("")
        self.high_temp_input_4.setSuffix("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pv_value_displ_4.setPrefix("")
        self.pv_value_displ_4.setSuffix("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.low_temp_input_4.setPrefix("")
        self.low_temp_input_4.setSuffix("")
        self.sv_value_input_4.setPrefix("")
        self.sv_value_input_4.setSuffix("")
        self.offset_value_input_4.setPrefix("")
        self.offset_value_input_4.setSuffix("")
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.heat_btn_a.setText(QCoreApplication.translate("MainWindow", u" Heating", None))
        self.refuel_btn_a.setText(QCoreApplication.translate("MainWindow", u" Refueling Start", None))
        self.vacuum_btn_a.setText(QCoreApplication.translate("MainWindow", u" Vacuum Pump", None))
        self.heat_btn_b.setText(QCoreApplication.translate("MainWindow", u"Heating", None))
        self.refuel_btn_b.setText(QCoreApplication.translate("MainWindow", u"Refueling Start", None))
        self.vacuum_btn_b.setText(QCoreApplication.translate("MainWindow", u"Vacuum Pump", None))
        self.heat_btn_c.setText(QCoreApplication.translate("MainWindow", u"Heating", None))
        self.refuel_btn_c.setText(QCoreApplication.translate("MainWindow", u"Refueling Start", None))
        self.vacuum_btn_c.setText(QCoreApplication.translate("MainWindow", u"Vacuum Pump", None))
        self.back_home_btn.setText(QCoreApplication.translate("MainWindow", u"\U0001f4c8 Back", None))
        self.device_icon.setText("")
        self.name_device_label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.type_device_label.setText(QCoreApplication.translate("MainWindow", u"Type: PLC", None))
        self.status_device_label.setText(QCoreApplication.translate("MainWindow", u"\U0001f534 Disconnected", None))
        self.connection_group.setTitle(QCoreApplication.translate("MainWindow", u"Connection Settings", None))
        self.plc_ip_address_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter IP address: 172.16.100.///", None))
        self.slot_label.setText(QCoreApplication.translate("MainWindow", u"Slot:", None))
        self.slot_label_4.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.plc_ip_address.setText(QCoreApplication.translate("MainWindow", u"IP address:", None))
        self.rack_label.setText(QCoreApplication.translate("MainWindow", u"Rack:", None))
        self.slot_label_2.setText(QCoreApplication.translate("MainWindow", u"DB:", None))
        self.slot_label_3.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.plc_connect.setText(QCoreApplication.translate("MainWindow", u"\U0001f50c Connect", None))
        self.dis_plc.setText(QCoreApplication.translate("MainWindow", u"\U000026d3\U0000fe0f\U0000200d\U0001f4a5 Disconnect", None))
        self.card_label.setText(QCoreApplication.translate("MainWindow", u" Unit of Weekdays", None))
        self.card_btn.setText(QCoreApplication.translate("MainWindow", u"\U0001f50dView Details", None))
        self.card_label_2.setText(QCoreApplication.translate("MainWindow", u" Issue of Weekdays", None))
        self.card_btn_2.setText(QCoreApplication.translate("MainWindow", u"\U0001f50dView Details", None))
        self.value_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.unit_label.setText(QCoreApplication.translate("MainWindow", u"units/day", None))
        self.title_label_stats.setText(QCoreApplication.translate("MainWindow", u"Production Output", None))
        self.value_label_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.unit_label_2.setText(QCoreApplication.translate("MainWindow", u"issues", None))
        self.title_label_stats_2.setText(QCoreApplication.translate("MainWindow", u"Issues Today", None))
        self.value_label_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.unit_label_3.setText(QCoreApplication.translate("MainWindow", u" min/unit", None))
        self.title_label_stats_3.setText(QCoreApplication.translate("MainWindow", u"Cycle Time", None))
        self.value_label_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.unit_label_4.setText(QCoreApplication.translate("MainWindow", u"time", None))
        self.title_label_stats_4.setText(QCoreApplication.translate("MainWindow", u"Working Time", None))
        ___qtablewidgetitem = self.list_err.horizontalHeaderItem(3)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"3", None))
        ___qtablewidgetitem1 = self.list_err.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        ___qtablewidgetitem2 = self.list_err.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        ___qtablewidgetitem3 = self.list_err.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        ___qtablewidgetitem4 = self.list_err.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        ___qtablewidgetitem5 = self.list_err.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        ___qtablewidgetitem6 = self.list_err.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        ___qtablewidgetitem7 = self.list_err.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        ___qtablewidgetitem8 = self.list_err.verticalHeaderItem(7)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        ___qtablewidgetitem9 = self.list_err.verticalHeaderItem(8)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        ___qtablewidgetitem10 = self.list_err.verticalHeaderItem(9)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        ___qtablewidgetitem11 = self.list_err.verticalHeaderItem(10)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        ___qtablewidgetitem12 = self.list_err.verticalHeaderItem(11)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        ___qtablewidgetitem13 = self.list_err.verticalHeaderItem(12)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"13", None))
        ___qtablewidgetitem14 = self.list_err.verticalHeaderItem(13)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"14", None))
        ___qtablewidgetitem15 = self.list_err.verticalHeaderItem(14)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        ___qtablewidgetitem16 = self.list_err.verticalHeaderItem(15)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"17", None))
        ___qtablewidgetitem17 = self.list_err.verticalHeaderItem(16)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"18", None))
        ___qtablewidgetitem18 = self.list_err.verticalHeaderItem(17)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"19", None))
        ___qtablewidgetitem19 = self.list_err.verticalHeaderItem(18)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"20", None))
        ___qtablewidgetitem20 = self.list_err.verticalHeaderItem(19)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"21", None))
        ___qtablewidgetitem21 = self.list_err.verticalHeaderItem(20)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"22", None))
        ___qtablewidgetitem22 = self.list_err.verticalHeaderItem(21)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"23", None))
        ___qtablewidgetitem23 = self.list_err.verticalHeaderItem(22)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"24", None))
        ___qtablewidgetitem24 = self.list_err.verticalHeaderItem(23)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"25", None))

        __sortingEnabled = self.list_err.isSortingEnabled()
        self.list_err.setSortingEnabled(False)
        ___qtablewidgetitem25 = self.list_err.item(0, 1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Type.", None))
        ___qtablewidgetitem26 = self.list_err.item(0, 2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Name.", None))
        ___qtablewidgetitem27 = self.list_err.item(0, 3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Date.", None))
        self.list_err.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem28 = self.list_done.horizontalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"4", None))
        ___qtablewidgetitem29 = self.list_done.verticalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"1", None))
        ___qtablewidgetitem30 = self.list_done.verticalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"2", None))
        ___qtablewidgetitem31 = self.list_done.verticalHeaderItem(2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"3", None))
        ___qtablewidgetitem32 = self.list_done.verticalHeaderItem(3)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"4", None))
        ___qtablewidgetitem33 = self.list_done.verticalHeaderItem(4)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"5", None))
        ___qtablewidgetitem34 = self.list_done.verticalHeaderItem(5)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"6", None))
        ___qtablewidgetitem35 = self.list_done.verticalHeaderItem(6)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"7", None))
        ___qtablewidgetitem36 = self.list_done.verticalHeaderItem(7)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"8", None))
        ___qtablewidgetitem37 = self.list_done.verticalHeaderItem(8)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"9", None))
        ___qtablewidgetitem38 = self.list_done.verticalHeaderItem(9)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"10", None))
        ___qtablewidgetitem39 = self.list_done.verticalHeaderItem(10)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"11", None))
        ___qtablewidgetitem40 = self.list_done.verticalHeaderItem(11)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"12", None))
        ___qtablewidgetitem41 = self.list_done.verticalHeaderItem(12)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"14", None))
        ___qtablewidgetitem42 = self.list_done.verticalHeaderItem(13)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"15", None))
        ___qtablewidgetitem43 = self.list_done.verticalHeaderItem(14)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"16", None))
        ___qtablewidgetitem44 = self.list_done.verticalHeaderItem(15)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"17", None))
        ___qtablewidgetitem45 = self.list_done.verticalHeaderItem(16)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"18", None))
        ___qtablewidgetitem46 = self.list_done.verticalHeaderItem(17)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"19", None))
        ___qtablewidgetitem47 = self.list_done.verticalHeaderItem(18)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"20", None))
        ___qtablewidgetitem48 = self.list_done.verticalHeaderItem(19)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"21", None))
        ___qtablewidgetitem49 = self.list_done.verticalHeaderItem(20)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"22", None))
        ___qtablewidgetitem50 = self.list_done.verticalHeaderItem(21)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"23", None))
        ___qtablewidgetitem51 = self.list_done.verticalHeaderItem(22)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"24", None))
        ___qtablewidgetitem52 = self.list_done.verticalHeaderItem(23)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"25", None))
        ___qtablewidgetitem53 = self.list_done.verticalHeaderItem(24)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"26", None))

        __sortingEnabled1 = self.list_done.isSortingEnabled()
        self.list_done.setSortingEnabled(False)
        ___qtablewidgetitem54 = self.list_done.item(0, 1)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Type.", None))
        ___qtablewidgetitem55 = self.list_done.item(0, 2)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Start.", None))
        ___qtablewidgetitem56 = self.list_done.item(0, 3)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Done.", None))
        ___qtablewidgetitem57 = self.list_done.item(0, 4)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Total Time.", None))
        self.list_done.setSortingEnabled(__sortingEnabled1)

        self.next_page_btn.setText(QCoreApplication.translate("MainWindow", u"\u2b05\ufe0f Next Page", None))
        self.backward_btn.setText(QCoreApplication.translate("MainWindow", u"\U0001f4c8 Go Back", None))
    # retranslateUi


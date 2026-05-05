# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tech_link_theme.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QButtonGroup, QComboBox,
    QDateTimeEdit, QDoubleSpinBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
import Icon_rc
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(1300, 1050))
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/newPrefix/Logo_Cty_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
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
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1024, 900))
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
        self.header_frame.setMaximumSize(QSize(16777215, 125))
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
        self.horizontalSpacer_4 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.pc_inform_label.addItem(self.horizontalSpacer_4)


        self.horizontalLayout.addLayout(self.pc_inform_label)

        self.language_switch_layout = QHBoxLayout()
        self.language_switch_layout.setObjectName(u"language_switch_layout")
        self.pushButton = QPushButton(self.header_frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(22)
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: left;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/language-exchange.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(30, 30))

        self.language_switch_layout.addWidget(self.pushButton)

        self.language_selection_combox = QComboBox(self.header_frame)
        self.language_selection_combox.addItem("")
        self.language_selection_combox.addItem("")
        self.language_selection_combox.setObjectName(u"language_selection_combox")
        sizePolicy.setHeightForWidth(self.language_selection_combox.sizePolicy().hasHeightForWidth())
        self.language_selection_combox.setSizePolicy(sizePolicy)
        self.language_selection_combox.setFont(font2)
        self.language_selection_combox.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.language_switch_layout.addWidget(self.language_selection_combox)


        self.horizontalLayout.addLayout(self.language_switch_layout)

        self.date_displ = QDateTimeEdit(self.header_frame)
        self.date_displ.setObjectName(u"date_displ")
        sizePolicy.setHeightForWidth(self.date_displ.sizePolicy().hasHeightForWidth())
        self.date_displ.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"MS Shell Dlg 2"])
        font3.setPointSize(22)
        font3.setBold(True)
        self.date_displ.setFont(font3)
        self.date_displ.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"")
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.body_frame.sizePolicy().hasHeightForWidth())
        self.body_frame.setSizePolicy(sizePolicy1)
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
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.home_page_btn = QPushButton(self.left_side_menu_widget)
        self.left_side_buttonGroup = QButtonGroup(MainWindow)
        self.left_side_buttonGroup.setObjectName(u"left_side_buttonGroup")
        self.left_side_buttonGroup.addButton(self.home_page_btn)
        self.home_page_btn.setObjectName(u"home_page_btn")
        sizePolicy.setHeightForWidth(self.home_page_btn.sizePolicy().hasHeightForWidth())
        self.home_page_btn.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(17)
        font4.setBold(True)
        self.home_page_btn.setFont(font4)
        self.home_page_btn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/home_off.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/newPrefix/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.home_page_btn.setIcon(icon2)
        self.home_page_btn.setIconSize(QSize(30, 30))
        self.home_page_btn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.home_page_btn)

        self.chart_page_btn = QPushButton(self.left_side_menu_widget)
        self.left_side_buttonGroup.addButton(self.chart_page_btn)
        self.chart_page_btn.setObjectName(u"chart_page_btn")
        sizePolicy.setHeightForWidth(self.chart_page_btn.sizePolicy().hasHeightForWidth())
        self.chart_page_btn.setSizePolicy(sizePolicy)
        self.chart_page_btn.setFont(font4)
        self.chart_page_btn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/chart-line-up-down.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/newPrefix/chart-line-up-down_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.chart_page_btn.setIcon(icon3)
        self.chart_page_btn.setIconSize(QSize(30, 30))
        self.chart_page_btn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.chart_page_btn)

        self.device_page_btn = QPushButton(self.left_side_menu_widget)
        self.left_side_buttonGroup.addButton(self.device_page_btn)
        self.device_page_btn.setObjectName(u"device_page_btn")
        sizePolicy.setHeightForWidth(self.device_page_btn.sizePolicy().hasHeightForWidth())
        self.device_page_btn.setSizePolicy(sizePolicy)
        self.device_page_btn.setFont(font4)
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/newPrefix/settings (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.device_page_btn.setIcon(icon4)
        self.device_page_btn.setIconSize(QSize(30, 30))
        self.device_page_btn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.device_page_btn)

        self.history_page_btn = QPushButton(self.left_side_menu_widget)
        self.left_side_buttonGroup.addButton(self.history_page_btn)
        self.history_page_btn.setObjectName(u"history_page_btn")
        sizePolicy.setHeightForWidth(self.history_page_btn.sizePolicy().hasHeightForWidth())
        self.history_page_btn.setSizePolicy(sizePolicy)
        self.history_page_btn.setFont(font4)
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/stats.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/newPrefix/stats (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.history_page_btn.setIcon(icon5)
        self.history_page_btn.setIconSize(QSize(30, 30))
        self.history_page_btn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.history_page_btn)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.open_side_menu_btn = QPushButton(self.left_side_menu_widget)
        self.open_side_menu_btn.setObjectName(u"open_side_menu_btn")
        sizePolicy.setHeightForWidth(self.open_side_menu_btn.sizePolicy().hasHeightForWidth())
        self.open_side_menu_btn.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.open_side_menu_btn.setFont(font5)
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

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.stackedWidget_2 = QStackedWidget(self.body_frame)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.menu_page = QWidget()
        self.menu_page.setObjectName(u"menu_page")
        self.menu_page.setStyleSheet(u"QWidget{\n"
"	background-color: white;\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.menu_page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
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
        self.card_frame_6.setStyleSheet(u"color: black;")
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


        self.verticalLayout_14.addLayout(self.gridLayout_2)

        self.stackedWidget_2.addWidget(self.menu_page)
        self.temp_press_page = QWidget()
        self.temp_press_page.setObjectName(u"temp_press_page")
        self.verticalLayout_12 = QVBoxLayout(self.temp_press_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pressure_page_header = QWidget(self.temp_press_page)
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
        self.widget_63.setStyleSheet(u"color: black;")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_63)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(10, 5, 10, 5)
        self.sys_state_stacked_wid_39 = QStackedWidget(self.widget_63)
        self.sys_state_stacked_wid_39.setObjectName(u"sys_state_stacked_wid_39")
        sizePolicy.setHeightForWidth(self.sys_state_stacked_wid_39.sizePolicy().hasHeightForWidth())
        self.sys_state_stacked_wid_39.setSizePolicy(sizePolicy)
        self.sys_state_stacked_wid_39.setStyleSheet(u"")
        self.running_light_52 = QWidget()
        self.running_light_52.setObjectName(u"running_light_52")
        self.horizontalLayout_439 = QHBoxLayout(self.running_light_52)
        self.horizontalLayout_439.setObjectName(u"horizontalLayout_439")
        self.horizontalLayout_439.setContentsMargins(0, 0, 0, 0)
        self.pushButton_39 = QPushButton(self.running_light_52)
        self.pushButton_39.setObjectName(u"pushButton_39")
        sizePolicy.setHeightForWidth(self.pushButton_39.sizePolicy().hasHeightForWidth())
        self.pushButton_39.setSizePolicy(sizePolicy)
        font6 = QFont()
        font6.setPointSize(15)
        font6.setBold(True)
        self.pushButton_39.setFont(font6)
        self.pushButton_39.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #10B981; \n"
"padding-right: 3px;")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/record-button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_39.setIcon(icon7)
        self.pushButton_39.setIconSize(QSize(30, 30))

        self.horizontalLayout_439.addWidget(self.pushButton_39)

        self.sys_state_stacked_wid_39.addWidget(self.running_light_52)
        self.wating_light_52 = QWidget()
        self.wating_light_52.setObjectName(u"wating_light_52")
        self.horizontalLayout_440 = QHBoxLayout(self.wating_light_52)
        self.horizontalLayout_440.setObjectName(u"horizontalLayout_440")
        self.horizontalLayout_440.setContentsMargins(0, 0, 0, 0)
        self.pushButton_40 = QPushButton(self.wating_light_52)
        self.pushButton_40.setObjectName(u"pushButton_40")
        sizePolicy.setHeightForWidth(self.pushButton_40.sizePolicy().hasHeightForWidth())
        self.pushButton_40.setSizePolicy(sizePolicy)
        self.pushButton_40.setFont(font6)
        self.pushButton_40.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #FB8C00; \n"
"padding-right: 3px;")
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/record-button (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_40.setIcon(icon8)
        self.pushButton_40.setIconSize(QSize(30, 30))

        self.horizontalLayout_440.addWidget(self.pushButton_40)

        self.sys_state_stacked_wid_39.addWidget(self.wating_light_52)
        self.error_light_52 = QWidget()
        self.error_light_52.setObjectName(u"error_light_52")
        self.horizontalLayout_441 = QHBoxLayout(self.error_light_52)
        self.horizontalLayout_441.setObjectName(u"horizontalLayout_441")
        self.horizontalLayout_441.setContentsMargins(0, 0, 0, 0)
        self.pushButton_41 = QPushButton(self.error_light_52)
        self.pushButton_41.setObjectName(u"pushButton_41")
        sizePolicy.setHeightForWidth(self.pushButton_41.sizePolicy().hasHeightForWidth())
        self.pushButton_41.setSizePolicy(sizePolicy)
        font7 = QFont()
        font7.setPointSize(18)
        font7.setBold(True)
        self.pushButton_41.setFont(font7)
        self.pushButton_41.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #F90A0A; \n"
"padding-right: 3px;")
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/record-button (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_41.setIcon(icon9)
        self.pushButton_41.setIconSize(QSize(30, 30))

        self.horizontalLayout_441.addWidget(self.pushButton_41)

        self.sys_state_stacked_wid_39.addWidget(self.error_light_52)

        self.horizontalLayout_15.addWidget(self.sys_state_stacked_wid_39)

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
        self.previus_group_page_btn = QPushButton(self.widget_9)
        self.previus_group_page_btn.setObjectName(u"previus_group_page_btn")
        sizePolicy.setHeightForWidth(self.previus_group_page_btn.sizePolicy().hasHeightForWidth())
        self.previus_group_page_btn.setSizePolicy(sizePolicy)
        self.previus_group_page_btn.setMaximumSize(QSize(16777215, 150))
        font8 = QFont()
        font8.setBold(True)
        self.previus_group_page_btn.setFont(font8)
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
        self.next_group_page_btn.setFont(font8)
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

        self.temp_unit_selection_combox = QComboBox(self.widget_63)
        self.temp_unit_selection_combox.addItem("")
        self.temp_unit_selection_combox.addItem("")
        self.temp_unit_selection_combox.setObjectName(u"temp_unit_selection_combox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.temp_unit_selection_combox.sizePolicy().hasHeightForWidth())
        self.temp_unit_selection_combox.setSizePolicy(sizePolicy2)
        self.temp_unit_selection_combox.setFont(font7)
        self.temp_unit_selection_combox.setStyleSheet(u"\n"
"    background-color: #F9FAFB;")

        self.horizontalLayout_15.addWidget(self.temp_unit_selection_combox)

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
        font9 = QFont()
        font9.setFamilies([u"Segoe UI"])
        font9.setPointSize(18)
        font9.setBold(True)
        self.clear_data_btn.setFont(font9)
        icon10 = QIcon()
        icon10.addFile(u":/newPrefix/data-cleaning.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clear_data_btn.setIcon(icon10)

        self.horizontalLayout_9.addWidget(self.clear_data_btn)

        self.new_data_btn = QPushButton(self.widget_56)
        self.new_data_btn.setObjectName(u"new_data_btn")
        sizePolicy.setHeightForWidth(self.new_data_btn.sizePolicy().hasHeightForWidth())
        self.new_data_btn.setSizePolicy(sizePolicy)
        self.new_data_btn.setFont(font9)
        icon11 = QIcon()
        icon11.addFile(u":/newPrefix/folder-upload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.new_data_btn.setIcon(icon11)

        self.horizontalLayout_9.addWidget(self.new_data_btn)


        self.horizontalLayout_15.addWidget(self.widget_56)

        self.data_selection_combobox_b = QComboBox(self.widget_63)
        self.data_selection_combobox_b.addItem("")
        self.data_selection_combobox_b.setObjectName(u"data_selection_combobox_b")
        sizePolicy2.setHeightForWidth(self.data_selection_combobox_b.sizePolicy().hasHeightForWidth())
        self.data_selection_combobox_b.setSizePolicy(sizePolicy2)
        self.data_selection_combobox_b.setMinimumSize(QSize(0, 40))
        self.data_selection_combobox_b.setFont(font7)
        self.data_selection_combobox_b.setStyleSheet(u"")
        self.data_selection_combobox_b.setIconSize(QSize(35, 35))

        self.horizontalLayout_15.addWidget(self.data_selection_combobox_b)


        self.verticalLayout_38.addWidget(self.widget_63)


        self.verticalLayout_12.addWidget(self.pressure_page_header)

        self.stackedWidget = QStackedWidget(self.temp_press_page)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font10 = QFont()
        font10.setPointSize(15)
        self.stackedWidget.setFont(font10)
        self.stackedWidget.setStyleSheet(u"QStackedWidget {\n"
"    border: none;\n"
"}")
        self.pressure_page = QWidget()
        self.pressure_page.setObjectName(u"pressure_page")
        self.verticalLayout_6 = QVBoxLayout(self.pressure_page)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(3, 5, 0, 3)
        self.stacked_pressure_page = QWidget(self.pressure_page)
        self.stacked_pressure_page.setObjectName(u"stacked_pressure_page")
        self.verticalLayout_10 = QVBoxLayout(self.stacked_pressure_page)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_pressure_time = QWidget(self.stacked_pressure_page)
        self.widget_pressure_time.setObjectName(u"widget_pressure_time")
        self.widget_pressure_time.setStyleSheet(u"background-color: white;\n"
"border-radius: 15px;")
        self.verticalLayout_63 = QVBoxLayout(self.widget_pressure_time)
        self.verticalLayout_63.setSpacing(10)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_pressure_time)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"QWidget {\n"
"    border-left: 4px solid #43A047;\n"
"    border-radius: 15px;\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 5, 10, 5)
        self.name_pressure_widget = QWidget(self.widget_6)
        self.name_pressure_widget.setObjectName(u"name_pressure_widget")
        self.name_pressure_widget.setStyleSheet(u"border-left: None;\n"
"border-radius: 15px;")
        self.verticalLayout_39 = QVBoxLayout(self.name_pressure_widget)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(5, 0, 0, 5)
        self.widget_73 = QWidget(self.name_pressure_widget)
        self.widget_73.setObjectName(u"widget_73")
        self.verticalLayout_23 = QVBoxLayout(self.widget_73)
        self.verticalLayout_23.setSpacing(10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(5, 5, 5, 5)
        self.label_166 = QLabel(self.widget_73)
        self.label_166.setObjectName(u"label_166")
        font11 = QFont()
        font11.setFamilies([u"MS Shell Dlg 2"])
        font11.setPointSize(18)
        font11.setBold(True)
        font11.setItalic(False)
        self.label_166.setFont(font11)
        self.label_166.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_166.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_166)

        self.label_160 = QLabel(self.widget_73)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setFont(font11)
        self.label_160.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_160.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_160)


        self.verticalLayout_39.addWidget(self.widget_73)

        self.widget_7 = QWidget(self.name_pressure_widget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.widget_7)
        self.verticalLayout_15.setSpacing(10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_76 = QLabel(self.widget_7)
        self.label_76.setObjectName(u"label_76")
        font12 = QFont()
        font12.setFamilies([u"Segoe UI"])
        font12.setPointSize(22)
        font12.setBold(True)
        font12.setItalic(False)
        self.label_76.setFont(font12)

        self.verticalLayout_15.addWidget(self.label_76)

        self.label_77 = QLabel(self.widget_7)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font12)

        self.verticalLayout_15.addWidget(self.label_77)

        self.label_78 = QLabel(self.widget_7)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font12)

        self.verticalLayout_15.addWidget(self.label_78)

        self.label_79 = QLabel(self.widget_7)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font12)

        self.verticalLayout_15.addWidget(self.label_79)

        self.label_75 = QLabel(self.widget_7)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font12)

        self.verticalLayout_15.addWidget(self.label_75)

        self.label_80 = QLabel(self.widget_7)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setFont(font12)

        self.verticalLayout_15.addWidget(self.label_80)

        self.label_81 = QLabel(self.widget_7)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setFont(font12)

        self.verticalLayout_15.addWidget(self.label_81)

        self.label_82 = QLabel(self.widget_7)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setFont(font12)

        self.verticalLayout_15.addWidget(self.label_82)

        self.label_83 = QLabel(self.widget_7)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setFont(font12)

        self.verticalLayout_15.addWidget(self.label_83)

        self.label_84 = QLabel(self.widget_7)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setFont(font12)

        self.verticalLayout_15.addWidget(self.label_84)

        self.verticalLayout_15.setStretch(0, 1)
        self.verticalLayout_15.setStretch(1, 1)
        self.verticalLayout_15.setStretch(2, 1)
        self.verticalLayout_15.setStretch(3, 1)
        self.verticalLayout_15.setStretch(4, 1)
        self.verticalLayout_15.setStretch(5, 1)
        self.verticalLayout_15.setStretch(6, 1)
        self.verticalLayout_15.setStretch(7, 1)
        self.verticalLayout_15.setStretch(8, 1)
        self.verticalLayout_15.setStretch(9, 1)

        self.verticalLayout_39.addWidget(self.widget_7)

        self.verticalLayout_39.setStretch(1, 10)

        self.horizontalLayout_7.addWidget(self.name_pressure_widget)

        self.line_4 = QFrame(self.widget_6)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line_4)

        self.press_a_widget = QWidget(self.widget_6)
        self.press_a_widget.setObjectName(u"press_a_widget")
        sizePolicy.setHeightForWidth(self.press_a_widget.sizePolicy().hasHeightForWidth())
        self.press_a_widget.setSizePolicy(sizePolicy)
        self.press_a_widget.setStyleSheet(u"border-left: None;")
        self.verticalLayout_29 = QVBoxLayout(self.press_a_widget)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 5)
        self.widget_68 = QWidget(self.press_a_widget)
        self.widget_68.setObjectName(u"widget_68")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_68)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 5, 0, 5)
        self.widget = QWidget(self.widget_68)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"color: rgb(30, 136, 229);")
        self.verticalLayout_18 = QVBoxLayout(self.widget)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_156 = QLabel(self.widget)
        self.label_156.setObjectName(u"label_156")
        font13 = QFont()
        font13.setFamilies([u"MS Shell Dlg 2"])
        font13.setPointSize(19)
        font13.setBold(True)
        font13.setItalic(False)
        self.label_156.setFont(font13)
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
        font14 = QFont()
        font14.setFamilies([u"MS Shell Dlg 2"])
        font14.setPointSize(16)
        font14.setBold(True)
        font14.setItalic(False)
        self.label_165.setFont(font14)
        self.label_165.setStyleSheet(u"color: rgb(229, 57, 53);")
        self.label_165.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_165)

        self.line_14 = QFrame(self.widget_17)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setStyleSheet(u"border: 2px solid rgb(30, 136, 229);")
        self.line_14.setFrameShape(QFrame.Shape.VLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_18.addWidget(self.line_14)

        self.label_167 = QLabel(self.widget_17)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setFont(font14)
        self.label_167.setStyleSheet(u"\n"
"color: rgb(67, 160, 71);")
        self.label_167.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_167)

        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(2, 1)

        self.horizontalLayout_17.addWidget(self.widget_17)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer)

        self.horizontalLayout_17.setStretch(0, 4)
        self.horizontalLayout_17.setStretch(1, 1)

        self.verticalLayout_18.addWidget(self.widget_14)


        self.horizontalLayout_14.addWidget(self.widget)


        self.verticalLayout_29.addWidget(self.widget_68)

        self.widget_58 = QWidget(self.press_a_widget)
        self.widget_58.setObjectName(u"widget_58")
        self.widget_58.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.verticalLayout_43 = QVBoxLayout(self.widget_58)
        self.verticalLayout_43.setSpacing(10)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.widget_264 = QWidget(self.widget_58)
        self.widget_264.setObjectName(u"widget_264")
        self.horizontalLayout_284 = QHBoxLayout(self.widget_264)
        self.horizontalLayout_284.setSpacing(7)
        self.horizontalLayout_284.setObjectName(u"horizontalLayout_284")
        self.horizontalLayout_284.setContentsMargins(0, 0, 0, 0)
        self.widget_170 = QWidget(self.widget_264)
        self.widget_170.setObjectName(u"widget_170")
        self.widget_170.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_288 = QHBoxLayout(self.widget_170)
        self.horizontalLayout_288.setObjectName(u"horizontalLayout_288")
        self.horizontalLayout_288.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_1 = QDoubleSpinBox(self.widget_170)
        self.pressure_pv_a_1.setObjectName(u"pressure_pv_a_1")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_1.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_1.setSizePolicy(sizePolicy)
        font15 = QFont()
        font15.setFamilies([u"Segoe UI"])
        font15.setPointSize(20)
        font15.setBold(True)
        font15.setItalic(False)
        self.pressure_pv_a_1.setFont(font15)
        self.pressure_pv_a_1.setStyleSheet(u"")
        self.pressure_pv_a_1.setWrapping(True)
        self.pressure_pv_a_1.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_1.setReadOnly(True)
        self.pressure_pv_a_1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_1.setDecimals(1)
        self.pressure_pv_a_1.setMaximum(999.000000000000000)
        self.pressure_pv_a_1.setValue(0.000000000000000)

        self.horizontalLayout_288.addWidget(self.pressure_pv_a_1)

        self.line = QFrame(self.widget_170)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"border: 2px solid rgb(30, 136, 229);")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_288.addWidget(self.line)

        self.pressure_sv_a_1 = QDoubleSpinBox(self.widget_170)
        self.pressure_sv_a_1.setObjectName(u"pressure_sv_a_1")
        sizePolicy.setHeightForWidth(self.pressure_sv_a_1.sizePolicy().hasHeightForWidth())
        self.pressure_sv_a_1.setSizePolicy(sizePolicy)
        self.pressure_sv_a_1.setFont(font15)
        self.pressure_sv_a_1.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_a_1.setWrapping(False)
        self.pressure_sv_a_1.setAlignment(Qt.AlignCenter)
        self.pressure_sv_a_1.setReadOnly(False)
        self.pressure_sv_a_1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_a_1.setDecimals(1)
        self.pressure_sv_a_1.setMaximum(999.000000000000000)
        self.pressure_sv_a_1.setValue(0.000000000000000)

        self.horizontalLayout_288.addWidget(self.pressure_sv_a_1)

        self.horizontalLayout_288.setStretch(0, 1)
        self.horizontalLayout_288.setStretch(2, 1)

        self.horizontalLayout_284.addWidget(self.widget_170)

        self.stacked_cel_fah_press_a_1 = QStackedWidget(self.widget_264)
        self.stacked_cel_fah_press_a_1.setObjectName(u"stacked_cel_fah_press_a_1")
        self.celsius_ap_15 = QWidget()
        self.celsius_ap_15.setObjectName(u"celsius_ap_15")
        self.horizontalLayout_390 = QHBoxLayout(self.celsius_ap_15)
        self.horizontalLayout_390.setObjectName(u"horizontalLayout_390")
        self.horizontalLayout_390.setContentsMargins(0, 0, 0, 0)
        self.label_274 = QLabel(self.celsius_ap_15)
        self.label_274.setObjectName(u"label_274")
        font16 = QFont()
        font16.setFamilies([u"Segoe UI"])
        font16.setPointSize(17)
        font16.setBold(True)
        font16.setItalic(False)
        self.label_274.setFont(font16)
        self.label_274.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_274.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_390.addWidget(self.label_274)

        self.stacked_cel_fah_press_a_1.addWidget(self.celsius_ap_15)
        self.fahrenheit_ap_15 = QWidget()
        self.fahrenheit_ap_15.setObjectName(u"fahrenheit_ap_15")
        self.horizontalLayout_391 = QHBoxLayout(self.fahrenheit_ap_15)
        self.horizontalLayout_391.setObjectName(u"horizontalLayout_391")
        self.horizontalLayout_391.setContentsMargins(0, 0, 0, 0)
        self.label_314 = QLabel(self.fahrenheit_ap_15)
        self.label_314.setObjectName(u"label_314")
        self.label_314.setFont(font16)
        self.label_314.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_314.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_391.addWidget(self.label_314)

        self.stacked_cel_fah_press_a_1.addWidget(self.fahrenheit_ap_15)

        self.horizontalLayout_284.addWidget(self.stacked_cel_fah_press_a_1)

        self.horizontalLayout_284.setStretch(0, 3)
        self.horizontalLayout_284.setStretch(1, 1)

        self.verticalLayout_43.addWidget(self.widget_264)

        self.widget_265 = QWidget(self.widget_58)
        self.widget_265.setObjectName(u"widget_265")
        self.horizontalLayout_289 = QHBoxLayout(self.widget_265)
        self.horizontalLayout_289.setSpacing(7)
        self.horizontalLayout_289.setObjectName(u"horizontalLayout_289")
        self.horizontalLayout_289.setContentsMargins(0, 0, 0, 0)
        self.widget_171 = QWidget(self.widget_265)
        self.widget_171.setObjectName(u"widget_171")
        self.widget_171.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_290 = QHBoxLayout(self.widget_171)
        self.horizontalLayout_290.setObjectName(u"horizontalLayout_290")
        self.horizontalLayout_290.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_2 = QDoubleSpinBox(self.widget_171)
        self.pressure_pv_a_2.setObjectName(u"pressure_pv_a_2")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_2.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_2.setSizePolicy(sizePolicy)
        self.pressure_pv_a_2.setFont(font15)
        self.pressure_pv_a_2.setStyleSheet(u"")
        self.pressure_pv_a_2.setWrapping(True)
        self.pressure_pv_a_2.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_2.setReadOnly(True)
        self.pressure_pv_a_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_2.setDecimals(1)
        self.pressure_pv_a_2.setMaximum(999.000000000000000)
        self.pressure_pv_a_2.setValue(0.000000000000000)

        self.horizontalLayout_290.addWidget(self.pressure_pv_a_2)

        self.line_2 = QFrame(self.widget_171)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"border: 2px solid rgb(30, 136, 229);")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_290.addWidget(self.line_2)

        self.pressure_sv_a_2 = QDoubleSpinBox(self.widget_171)
        self.pressure_sv_a_2.setObjectName(u"pressure_sv_a_2")
        sizePolicy.setHeightForWidth(self.pressure_sv_a_2.sizePolicy().hasHeightForWidth())
        self.pressure_sv_a_2.setSizePolicy(sizePolicy)
        self.pressure_sv_a_2.setFont(font15)
        self.pressure_sv_a_2.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_a_2.setWrapping(False)
        self.pressure_sv_a_2.setAlignment(Qt.AlignCenter)
        self.pressure_sv_a_2.setReadOnly(False)
        self.pressure_sv_a_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_a_2.setDecimals(1)
        self.pressure_sv_a_2.setMaximum(999.000000000000000)
        self.pressure_sv_a_2.setValue(0.000000000000000)

        self.horizontalLayout_290.addWidget(self.pressure_sv_a_2)

        self.horizontalLayout_290.setStretch(0, 1)
        self.horizontalLayout_290.setStretch(2, 1)

        self.horizontalLayout_289.addWidget(self.widget_171)

        self.stacked_cel_fah_press_a_2 = QStackedWidget(self.widget_265)
        self.stacked_cel_fah_press_a_2.setObjectName(u"stacked_cel_fah_press_a_2")
        self.celsius_ap_16 = QWidget()
        self.celsius_ap_16.setObjectName(u"celsius_ap_16")
        self.horizontalLayout_392 = QHBoxLayout(self.celsius_ap_16)
        self.horizontalLayout_392.setObjectName(u"horizontalLayout_392")
        self.horizontalLayout_392.setContentsMargins(0, 0, 0, 0)
        self.label_315 = QLabel(self.celsius_ap_16)
        self.label_315.setObjectName(u"label_315")
        self.label_315.setFont(font16)
        self.label_315.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_315.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_392.addWidget(self.label_315)

        self.stacked_cel_fah_press_a_2.addWidget(self.celsius_ap_16)
        self.fahrenheit_ap_16 = QWidget()
        self.fahrenheit_ap_16.setObjectName(u"fahrenheit_ap_16")
        self.horizontalLayout_393 = QHBoxLayout(self.fahrenheit_ap_16)
        self.horizontalLayout_393.setObjectName(u"horizontalLayout_393")
        self.horizontalLayout_393.setContentsMargins(0, 0, 0, 0)
        self.label_316 = QLabel(self.fahrenheit_ap_16)
        self.label_316.setObjectName(u"label_316")
        self.label_316.setFont(font16)
        self.label_316.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_316.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_393.addWidget(self.label_316)

        self.stacked_cel_fah_press_a_2.addWidget(self.fahrenheit_ap_16)

        self.horizontalLayout_289.addWidget(self.stacked_cel_fah_press_a_2)

        self.horizontalLayout_289.setStretch(0, 3)
        self.horizontalLayout_289.setStretch(1, 1)

        self.verticalLayout_43.addWidget(self.widget_265)

        self.widget_268 = QWidget(self.widget_58)
        self.widget_268.setObjectName(u"widget_268")
        self.horizontalLayout_291 = QHBoxLayout(self.widget_268)
        self.horizontalLayout_291.setSpacing(7)
        self.horizontalLayout_291.setObjectName(u"horizontalLayout_291")
        self.horizontalLayout_291.setContentsMargins(0, 0, 0, 0)
        self.widget_173 = QWidget(self.widget_268)
        self.widget_173.setObjectName(u"widget_173")
        self.widget_173.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_292 = QHBoxLayout(self.widget_173)
        self.horizontalLayout_292.setObjectName(u"horizontalLayout_292")
        self.horizontalLayout_292.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_3 = QDoubleSpinBox(self.widget_173)
        self.pressure_pv_a_3.setObjectName(u"pressure_pv_a_3")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_3.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_3.setSizePolicy(sizePolicy)
        self.pressure_pv_a_3.setFont(font15)
        self.pressure_pv_a_3.setStyleSheet(u"")
        self.pressure_pv_a_3.setWrapping(True)
        self.pressure_pv_a_3.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_3.setReadOnly(True)
        self.pressure_pv_a_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_3.setDecimals(1)
        self.pressure_pv_a_3.setMaximum(999.000000000000000)
        self.pressure_pv_a_3.setValue(0.000000000000000)

        self.horizontalLayout_292.addWidget(self.pressure_pv_a_3)

        self.line_3 = QFrame(self.widget_173)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"border: 2px solid rgb(30, 136, 229);")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_292.addWidget(self.line_3)

        self.pressure_sv_a_3 = QDoubleSpinBox(self.widget_173)
        self.pressure_sv_a_3.setObjectName(u"pressure_sv_a_3")
        sizePolicy.setHeightForWidth(self.pressure_sv_a_3.sizePolicy().hasHeightForWidth())
        self.pressure_sv_a_3.setSizePolicy(sizePolicy)
        self.pressure_sv_a_3.setFont(font15)
        self.pressure_sv_a_3.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_a_3.setWrapping(False)
        self.pressure_sv_a_3.setAlignment(Qt.AlignCenter)
        self.pressure_sv_a_3.setReadOnly(False)
        self.pressure_sv_a_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_a_3.setDecimals(1)
        self.pressure_sv_a_3.setMaximum(999.000000000000000)
        self.pressure_sv_a_3.setValue(0.000000000000000)

        self.horizontalLayout_292.addWidget(self.pressure_sv_a_3)

        self.horizontalLayout_292.setStretch(0, 1)
        self.horizontalLayout_292.setStretch(2, 1)

        self.horizontalLayout_291.addWidget(self.widget_173)

        self.stacked_cel_fah_press_a_3 = QStackedWidget(self.widget_268)
        self.stacked_cel_fah_press_a_3.setObjectName(u"stacked_cel_fah_press_a_3")
        self.celsius_ap_17 = QWidget()
        self.celsius_ap_17.setObjectName(u"celsius_ap_17")
        self.horizontalLayout_394 = QHBoxLayout(self.celsius_ap_17)
        self.horizontalLayout_394.setObjectName(u"horizontalLayout_394")
        self.horizontalLayout_394.setContentsMargins(0, 0, 0, 0)
        self.label_317 = QLabel(self.celsius_ap_17)
        self.label_317.setObjectName(u"label_317")
        self.label_317.setFont(font16)
        self.label_317.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_317.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_394.addWidget(self.label_317)

        self.stacked_cel_fah_press_a_3.addWidget(self.celsius_ap_17)
        self.fahrenheit_ap_17 = QWidget()
        self.fahrenheit_ap_17.setObjectName(u"fahrenheit_ap_17")
        self.horizontalLayout_395 = QHBoxLayout(self.fahrenheit_ap_17)
        self.horizontalLayout_395.setObjectName(u"horizontalLayout_395")
        self.horizontalLayout_395.setContentsMargins(0, 0, 0, 0)
        self.label_318 = QLabel(self.fahrenheit_ap_17)
        self.label_318.setObjectName(u"label_318")
        self.label_318.setFont(font16)
        self.label_318.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_318.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_395.addWidget(self.label_318)

        self.stacked_cel_fah_press_a_3.addWidget(self.fahrenheit_ap_17)

        self.horizontalLayout_291.addWidget(self.stacked_cel_fah_press_a_3)

        self.horizontalLayout_291.setStretch(0, 3)
        self.horizontalLayout_291.setStretch(1, 1)

        self.verticalLayout_43.addWidget(self.widget_268)

        self.widget_269 = QWidget(self.widget_58)
        self.widget_269.setObjectName(u"widget_269")
        self.horizontalLayout_293 = QHBoxLayout(self.widget_269)
        self.horizontalLayout_293.setSpacing(7)
        self.horizontalLayout_293.setObjectName(u"horizontalLayout_293")
        self.horizontalLayout_293.setContentsMargins(0, 0, 0, 0)
        self.widget_175 = QWidget(self.widget_269)
        self.widget_175.setObjectName(u"widget_175")
        self.widget_175.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_294 = QHBoxLayout(self.widget_175)
        self.horizontalLayout_294.setObjectName(u"horizontalLayout_294")
        self.horizontalLayout_294.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_4 = QDoubleSpinBox(self.widget_175)
        self.pressure_pv_a_4.setObjectName(u"pressure_pv_a_4")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_4.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_4.setSizePolicy(sizePolicy)
        self.pressure_pv_a_4.setFont(font15)
        self.pressure_pv_a_4.setStyleSheet(u"")
        self.pressure_pv_a_4.setWrapping(True)
        self.pressure_pv_a_4.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_4.setReadOnly(True)
        self.pressure_pv_a_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_4.setDecimals(1)
        self.pressure_pv_a_4.setMaximum(999.000000000000000)
        self.pressure_pv_a_4.setValue(0.000000000000000)

        self.horizontalLayout_294.addWidget(self.pressure_pv_a_4)

        self.line_8 = QFrame(self.widget_175)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setStyleSheet(u"border: 2px solid rgb(30, 136, 229);")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_294.addWidget(self.line_8)

        self.pressure_sv_a_4 = QDoubleSpinBox(self.widget_175)
        self.pressure_sv_a_4.setObjectName(u"pressure_sv_a_4")
        sizePolicy.setHeightForWidth(self.pressure_sv_a_4.sizePolicy().hasHeightForWidth())
        self.pressure_sv_a_4.setSizePolicy(sizePolicy)
        self.pressure_sv_a_4.setFont(font15)
        self.pressure_sv_a_4.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_a_4.setWrapping(False)
        self.pressure_sv_a_4.setAlignment(Qt.AlignCenter)
        self.pressure_sv_a_4.setReadOnly(False)
        self.pressure_sv_a_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_a_4.setDecimals(1)
        self.pressure_sv_a_4.setMaximum(999.000000000000000)
        self.pressure_sv_a_4.setValue(0.000000000000000)

        self.horizontalLayout_294.addWidget(self.pressure_sv_a_4)

        self.horizontalLayout_294.setStretch(0, 1)
        self.horizontalLayout_294.setStretch(2, 1)

        self.horizontalLayout_293.addWidget(self.widget_175)

        self.stacked_cel_fah_press_a_4 = QStackedWidget(self.widget_269)
        self.stacked_cel_fah_press_a_4.setObjectName(u"stacked_cel_fah_press_a_4")
        self.celsius_ap_18 = QWidget()
        self.celsius_ap_18.setObjectName(u"celsius_ap_18")
        self.horizontalLayout_396 = QHBoxLayout(self.celsius_ap_18)
        self.horizontalLayout_396.setObjectName(u"horizontalLayout_396")
        self.horizontalLayout_396.setContentsMargins(0, 0, 0, 0)
        self.label_319 = QLabel(self.celsius_ap_18)
        self.label_319.setObjectName(u"label_319")
        self.label_319.setFont(font16)
        self.label_319.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_319.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_396.addWidget(self.label_319)

        self.stacked_cel_fah_press_a_4.addWidget(self.celsius_ap_18)
        self.fahrenheit_ap_18 = QWidget()
        self.fahrenheit_ap_18.setObjectName(u"fahrenheit_ap_18")
        self.horizontalLayout_397 = QHBoxLayout(self.fahrenheit_ap_18)
        self.horizontalLayout_397.setObjectName(u"horizontalLayout_397")
        self.horizontalLayout_397.setContentsMargins(0, 0, 0, 0)
        self.label_340 = QLabel(self.fahrenheit_ap_18)
        self.label_340.setObjectName(u"label_340")
        self.label_340.setFont(font16)
        self.label_340.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_340.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_397.addWidget(self.label_340)

        self.stacked_cel_fah_press_a_4.addWidget(self.fahrenheit_ap_18)

        self.horizontalLayout_293.addWidget(self.stacked_cel_fah_press_a_4)

        self.horizontalLayout_293.setStretch(0, 3)
        self.horizontalLayout_293.setStretch(1, 1)

        self.verticalLayout_43.addWidget(self.widget_269)

        self.widget_270 = QWidget(self.widget_58)
        self.widget_270.setObjectName(u"widget_270")
        self.horizontalLayout_295 = QHBoxLayout(self.widget_270)
        self.horizontalLayout_295.setObjectName(u"horizontalLayout_295")
        self.horizontalLayout_295.setContentsMargins(0, 0, 0, 0)
        self.widget_180 = QWidget(self.widget_270)
        self.widget_180.setObjectName(u"widget_180")
        self.widget_180.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_336 = QHBoxLayout(self.widget_180)
        self.horizontalLayout_336.setObjectName(u"horizontalLayout_336")
        self.horizontalLayout_336.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_5 = QDoubleSpinBox(self.widget_180)
        self.pressure_pv_a_5.setObjectName(u"pressure_pv_a_5")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_5.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_5.setSizePolicy(sizePolicy)
        self.pressure_pv_a_5.setFont(font15)
        self.pressure_pv_a_5.setStyleSheet(u"")
        self.pressure_pv_a_5.setWrapping(True)
        self.pressure_pv_a_5.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_5.setReadOnly(True)
        self.pressure_pv_a_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_5.setDecimals(1)
        self.pressure_pv_a_5.setMaximum(999.000000000000000)
        self.pressure_pv_a_5.setValue(0.000000000000000)

        self.horizontalLayout_336.addWidget(self.pressure_pv_a_5)

        self.line_7 = QFrame(self.widget_180)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"border: 2px solid rgb(30, 136, 229);")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_336.addWidget(self.line_7)

        self.pressure_sv_a_5 = QDoubleSpinBox(self.widget_180)
        self.pressure_sv_a_5.setObjectName(u"pressure_sv_a_5")
        sizePolicy.setHeightForWidth(self.pressure_sv_a_5.sizePolicy().hasHeightForWidth())
        self.pressure_sv_a_5.setSizePolicy(sizePolicy)
        self.pressure_sv_a_5.setFont(font15)
        self.pressure_sv_a_5.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_a_5.setWrapping(False)
        self.pressure_sv_a_5.setAlignment(Qt.AlignCenter)
        self.pressure_sv_a_5.setReadOnly(False)
        self.pressure_sv_a_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_a_5.setDecimals(1)
        self.pressure_sv_a_5.setMaximum(999.000000000000000)
        self.pressure_sv_a_5.setValue(0.000000000000000)

        self.horizontalLayout_336.addWidget(self.pressure_sv_a_5)

        self.horizontalLayout_336.setStretch(0, 1)
        self.horizontalLayout_336.setStretch(2, 1)

        self.horizontalLayout_295.addWidget(self.widget_180)

        self.label_204 = QLabel(self.widget_270)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setFont(font16)
        self.label_204.setAlignment(Qt.AlignCenter)
        self.label_204.setWordWrap(True)

        self.horizontalLayout_295.addWidget(self.label_204)

        self.horizontalLayout_295.setStretch(0, 3)
        self.horizontalLayout_295.setStretch(1, 1)

        self.verticalLayout_43.addWidget(self.widget_270)

        self.widget_271 = QWidget(self.widget_58)
        self.widget_271.setObjectName(u"widget_271")
        self.horizontalLayout_340 = QHBoxLayout(self.widget_271)
        self.horizontalLayout_340.setObjectName(u"horizontalLayout_340")
        self.horizontalLayout_340.setContentsMargins(0, 0, 0, 0)
        self.widget_181 = QWidget(self.widget_271)
        self.widget_181.setObjectName(u"widget_181")
        self.widget_181.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_341 = QHBoxLayout(self.widget_181)
        self.horizontalLayout_341.setObjectName(u"horizontalLayout_341")
        self.horizontalLayout_341.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_6 = QDoubleSpinBox(self.widget_181)
        self.pressure_pv_a_6.setObjectName(u"pressure_pv_a_6")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_6.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_6.setSizePolicy(sizePolicy)
        self.pressure_pv_a_6.setFont(font15)
        self.pressure_pv_a_6.setStyleSheet(u"")
        self.pressure_pv_a_6.setWrapping(True)
        self.pressure_pv_a_6.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_6.setReadOnly(True)
        self.pressure_pv_a_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_6.setDecimals(1)
        self.pressure_pv_a_6.setMaximum(999.000000000000000)
        self.pressure_pv_a_6.setValue(0.000000000000000)

        self.horizontalLayout_341.addWidget(self.pressure_pv_a_6)

        self.line_9 = QFrame(self.widget_181)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setStyleSheet(u"border: 2px solid rgb(30, 136, 229);")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_341.addWidget(self.line_9)

        self.pressure_sv_a_6 = QDoubleSpinBox(self.widget_181)
        self.pressure_sv_a_6.setObjectName(u"pressure_sv_a_6")
        sizePolicy.setHeightForWidth(self.pressure_sv_a_6.sizePolicy().hasHeightForWidth())
        self.pressure_sv_a_6.setSizePolicy(sizePolicy)
        self.pressure_sv_a_6.setFont(font15)
        self.pressure_sv_a_6.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_a_6.setWrapping(False)
        self.pressure_sv_a_6.setAlignment(Qt.AlignCenter)
        self.pressure_sv_a_6.setReadOnly(False)
        self.pressure_sv_a_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_a_6.setDecimals(1)
        self.pressure_sv_a_6.setMaximum(999.000000000000000)
        self.pressure_sv_a_6.setValue(0.000000000000000)

        self.horizontalLayout_341.addWidget(self.pressure_sv_a_6)

        self.horizontalLayout_341.setStretch(0, 1)
        self.horizontalLayout_341.setStretch(2, 1)

        self.horizontalLayout_340.addWidget(self.widget_181)

        self.label_213 = QLabel(self.widget_271)
        self.label_213.setObjectName(u"label_213")
        self.label_213.setFont(font16)
        self.label_213.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_340.addWidget(self.label_213)

        self.horizontalLayout_340.setStretch(0, 3)
        self.horizontalLayout_340.setStretch(1, 1)

        self.verticalLayout_43.addWidget(self.widget_271)

        self.widget_272 = QWidget(self.widget_58)
        self.widget_272.setObjectName(u"widget_272")
        self.horizontalLayout_342 = QHBoxLayout(self.widget_272)
        self.horizontalLayout_342.setObjectName(u"horizontalLayout_342")
        self.horizontalLayout_342.setContentsMargins(0, 0, 0, 0)
        self.widget_182 = QWidget(self.widget_272)
        self.widget_182.setObjectName(u"widget_182")
        self.widget_182.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_343 = QHBoxLayout(self.widget_182)
        self.horizontalLayout_343.setObjectName(u"horizontalLayout_343")
        self.horizontalLayout_343.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_7 = QDoubleSpinBox(self.widget_182)
        self.pressure_pv_a_7.setObjectName(u"pressure_pv_a_7")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_7.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_7.setSizePolicy(sizePolicy)
        self.pressure_pv_a_7.setFont(font15)
        self.pressure_pv_a_7.setStyleSheet(u"")
        self.pressure_pv_a_7.setWrapping(True)
        self.pressure_pv_a_7.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_7.setReadOnly(True)
        self.pressure_pv_a_7.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_7.setDecimals(1)
        self.pressure_pv_a_7.setMaximum(999.000000000000000)
        self.pressure_pv_a_7.setValue(0.000000000000000)

        self.horizontalLayout_343.addWidget(self.pressure_pv_a_7)

        self.line_10 = QFrame(self.widget_182)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setStyleSheet(u"border: 2px solid rgb(30, 136, 229);")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_343.addWidget(self.line_10)

        self.pressure_sv_a_7 = QDoubleSpinBox(self.widget_182)
        self.pressure_sv_a_7.setObjectName(u"pressure_sv_a_7")
        sizePolicy.setHeightForWidth(self.pressure_sv_a_7.sizePolicy().hasHeightForWidth())
        self.pressure_sv_a_7.setSizePolicy(sizePolicy)
        self.pressure_sv_a_7.setFont(font15)
        self.pressure_sv_a_7.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_a_7.setWrapping(False)
        self.pressure_sv_a_7.setAlignment(Qt.AlignCenter)
        self.pressure_sv_a_7.setReadOnly(False)
        self.pressure_sv_a_7.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_a_7.setDecimals(1)
        self.pressure_sv_a_7.setMaximum(999.000000000000000)
        self.pressure_sv_a_7.setValue(0.000000000000000)

        self.horizontalLayout_343.addWidget(self.pressure_sv_a_7)

        self.horizontalLayout_343.setStretch(0, 1)
        self.horizontalLayout_343.setStretch(2, 1)

        self.horizontalLayout_342.addWidget(self.widget_182)

        self.label_214 = QLabel(self.widget_272)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setFont(font16)
        self.label_214.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_342.addWidget(self.label_214)

        self.horizontalLayout_342.setStretch(0, 3)
        self.horizontalLayout_342.setStretch(1, 1)

        self.verticalLayout_43.addWidget(self.widget_272)

        self.widget_273 = QWidget(self.widget_58)
        self.widget_273.setObjectName(u"widget_273")
        self.horizontalLayout_344 = QHBoxLayout(self.widget_273)
        self.horizontalLayout_344.setObjectName(u"horizontalLayout_344")
        self.horizontalLayout_344.setContentsMargins(0, 0, 0, 0)
        self.widget_183 = QWidget(self.widget_273)
        self.widget_183.setObjectName(u"widget_183")
        self.widget_183.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_345 = QHBoxLayout(self.widget_183)
        self.horizontalLayout_345.setObjectName(u"horizontalLayout_345")
        self.horizontalLayout_345.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_8 = QDoubleSpinBox(self.widget_183)
        self.pressure_pv_a_8.setObjectName(u"pressure_pv_a_8")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_8.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_8.setSizePolicy(sizePolicy)
        self.pressure_pv_a_8.setFont(font15)
        self.pressure_pv_a_8.setStyleSheet(u"")
        self.pressure_pv_a_8.setWrapping(True)
        self.pressure_pv_a_8.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_8.setReadOnly(True)
        self.pressure_pv_a_8.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_8.setDecimals(1)
        self.pressure_pv_a_8.setMaximum(999.000000000000000)
        self.pressure_pv_a_8.setValue(0.000000000000000)

        self.horizontalLayout_345.addWidget(self.pressure_pv_a_8)

        self.line_11 = QFrame(self.widget_183)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setStyleSheet(u"border: 2px solid rgb(30, 136, 229);")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_345.addWidget(self.line_11)

        self.pressure_sv_a_8 = QDoubleSpinBox(self.widget_183)
        self.pressure_sv_a_8.setObjectName(u"pressure_sv_a_8")
        sizePolicy.setHeightForWidth(self.pressure_sv_a_8.sizePolicy().hasHeightForWidth())
        self.pressure_sv_a_8.setSizePolicy(sizePolicy)
        self.pressure_sv_a_8.setFont(font15)
        self.pressure_sv_a_8.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_a_8.setWrapping(False)
        self.pressure_sv_a_8.setAlignment(Qt.AlignCenter)
        self.pressure_sv_a_8.setReadOnly(False)
        self.pressure_sv_a_8.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_a_8.setDecimals(1)
        self.pressure_sv_a_8.setMaximum(999.000000000000000)
        self.pressure_sv_a_8.setValue(0.000000000000000)

        self.horizontalLayout_345.addWidget(self.pressure_sv_a_8)

        self.horizontalLayout_345.setStretch(0, 1)
        self.horizontalLayout_345.setStretch(2, 1)

        self.horizontalLayout_344.addWidget(self.widget_183)

        self.label_215 = QLabel(self.widget_273)
        self.label_215.setObjectName(u"label_215")
        self.label_215.setFont(font16)
        self.label_215.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_344.addWidget(self.label_215)

        self.horizontalLayout_344.setStretch(0, 3)
        self.horizontalLayout_344.setStretch(1, 1)

        self.verticalLayout_43.addWidget(self.widget_273)

        self.widget_274 = QWidget(self.widget_58)
        self.widget_274.setObjectName(u"widget_274")
        self.horizontalLayout_346 = QHBoxLayout(self.widget_274)
        self.horizontalLayout_346.setObjectName(u"horizontalLayout_346")
        self.horizontalLayout_346.setContentsMargins(0, 0, 0, 0)
        self.widget_184 = QWidget(self.widget_274)
        self.widget_184.setObjectName(u"widget_184")
        self.widget_184.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_347 = QHBoxLayout(self.widget_184)
        self.horizontalLayout_347.setObjectName(u"horizontalLayout_347")
        self.horizontalLayout_347.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_9 = QDoubleSpinBox(self.widget_184)
        self.pressure_pv_a_9.setObjectName(u"pressure_pv_a_9")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_9.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_9.setSizePolicy(sizePolicy)
        self.pressure_pv_a_9.setFont(font15)
        self.pressure_pv_a_9.setStyleSheet(u"")
        self.pressure_pv_a_9.setWrapping(True)
        self.pressure_pv_a_9.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_9.setReadOnly(True)
        self.pressure_pv_a_9.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_9.setDecimals(1)
        self.pressure_pv_a_9.setMaximum(999.000000000000000)
        self.pressure_pv_a_9.setValue(0.000000000000000)

        self.horizontalLayout_347.addWidget(self.pressure_pv_a_9)

        self.line_12 = QFrame(self.widget_184)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setStyleSheet(u"border: 2px solid rgb(30, 136, 229);")
        self.line_12.setFrameShape(QFrame.Shape.VLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_347.addWidget(self.line_12)

        self.pressure_sv_a_9 = QDoubleSpinBox(self.widget_184)
        self.pressure_sv_a_9.setObjectName(u"pressure_sv_a_9")
        sizePolicy.setHeightForWidth(self.pressure_sv_a_9.sizePolicy().hasHeightForWidth())
        self.pressure_sv_a_9.setSizePolicy(sizePolicy)
        self.pressure_sv_a_9.setFont(font15)
        self.pressure_sv_a_9.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_a_9.setWrapping(False)
        self.pressure_sv_a_9.setAlignment(Qt.AlignCenter)
        self.pressure_sv_a_9.setReadOnly(False)
        self.pressure_sv_a_9.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_a_9.setDecimals(1)
        self.pressure_sv_a_9.setMaximum(999.000000000000000)
        self.pressure_sv_a_9.setValue(0.000000000000000)

        self.horizontalLayout_347.addWidget(self.pressure_sv_a_9)

        self.horizontalLayout_347.setStretch(0, 1)
        self.horizontalLayout_347.setStretch(2, 1)

        self.horizontalLayout_346.addWidget(self.widget_184)

        self.label_216 = QLabel(self.widget_274)
        self.label_216.setObjectName(u"label_216")
        self.label_216.setFont(font16)
        self.label_216.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_346.addWidget(self.label_216)

        self.horizontalLayout_346.setStretch(0, 3)
        self.horizontalLayout_346.setStretch(1, 1)

        self.verticalLayout_43.addWidget(self.widget_274)

        self.widget_283 = QWidget(self.widget_58)
        self.widget_283.setObjectName(u"widget_283")
        self.horizontalLayout_348 = QHBoxLayout(self.widget_283)
        self.horizontalLayout_348.setObjectName(u"horizontalLayout_348")
        self.horizontalLayout_348.setContentsMargins(0, 0, 0, 0)
        self.widget_187 = QWidget(self.widget_283)
        self.widget_187.setObjectName(u"widget_187")
        self.widget_187.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_349 = QHBoxLayout(self.widget_187)
        self.horizontalLayout_349.setObjectName(u"horizontalLayout_349")
        self.horizontalLayout_349.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_a_10 = QDoubleSpinBox(self.widget_187)
        self.pressure_pv_a_10.setObjectName(u"pressure_pv_a_10")
        sizePolicy.setHeightForWidth(self.pressure_pv_a_10.sizePolicy().hasHeightForWidth())
        self.pressure_pv_a_10.setSizePolicy(sizePolicy)
        self.pressure_pv_a_10.setFont(font15)
        self.pressure_pv_a_10.setStyleSheet(u"")
        self.pressure_pv_a_10.setWrapping(True)
        self.pressure_pv_a_10.setAlignment(Qt.AlignCenter)
        self.pressure_pv_a_10.setReadOnly(True)
        self.pressure_pv_a_10.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_a_10.setDecimals(1)
        self.pressure_pv_a_10.setMaximum(999.000000000000000)
        self.pressure_pv_a_10.setValue(0.000000000000000)

        self.horizontalLayout_349.addWidget(self.pressure_pv_a_10)

        self.line_13 = QFrame(self.widget_187)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setStyleSheet(u"border: 2px solid rgb(30, 136, 229);")
        self.line_13.setFrameShape(QFrame.Shape.VLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_349.addWidget(self.line_13)

        self.pressure_sv_a_10 = QDoubleSpinBox(self.widget_187)
        self.pressure_sv_a_10.setObjectName(u"pressure_sv_a_10")
        sizePolicy.setHeightForWidth(self.pressure_sv_a_10.sizePolicy().hasHeightForWidth())
        self.pressure_sv_a_10.setSizePolicy(sizePolicy)
        self.pressure_sv_a_10.setFont(font15)
        self.pressure_sv_a_10.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_a_10.setWrapping(False)
        self.pressure_sv_a_10.setAlignment(Qt.AlignCenter)
        self.pressure_sv_a_10.setReadOnly(False)
        self.pressure_sv_a_10.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_a_10.setDecimals(1)
        self.pressure_sv_a_10.setMaximum(999.000000000000000)
        self.pressure_sv_a_10.setValue(0.000000000000000)

        self.horizontalLayout_349.addWidget(self.pressure_sv_a_10)

        self.horizontalLayout_349.setStretch(0, 1)
        self.horizontalLayout_349.setStretch(2, 1)

        self.horizontalLayout_348.addWidget(self.widget_187)

        self.label_222 = QLabel(self.widget_283)
        self.label_222.setObjectName(u"label_222")
        self.label_222.setFont(font16)
        self.label_222.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_348.addWidget(self.label_222)

        self.horizontalLayout_348.setStretch(0, 3)
        self.horizontalLayout_348.setStretch(1, 1)

        self.verticalLayout_43.addWidget(self.widget_283)

        self.verticalLayout_43.setStretch(0, 1)
        self.verticalLayout_43.setStretch(1, 1)
        self.verticalLayout_43.setStretch(2, 1)
        self.verticalLayout_43.setStretch(3, 1)
        self.verticalLayout_43.setStretch(4, 1)
        self.verticalLayout_43.setStretch(5, 1)
        self.verticalLayout_43.setStretch(6, 1)
        self.verticalLayout_43.setStretch(7, 1)
        self.verticalLayout_43.setStretch(8, 1)
        self.verticalLayout_43.setStretch(9, 1)

        self.verticalLayout_29.addWidget(self.widget_58)


        self.horizontalLayout_7.addWidget(self.press_a_widget)

        self.line_5 = QFrame(self.widget_6)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line_5)

        self.press_b_widget = QWidget(self.widget_6)
        self.press_b_widget.setObjectName(u"press_b_widget")
        sizePolicy.setHeightForWidth(self.press_b_widget.sizePolicy().hasHeightForWidth())
        self.press_b_widget.setSizePolicy(sizePolicy)
        self.press_b_widget.setStyleSheet(u"border-left: None;")
        self.verticalLayout_30 = QVBoxLayout(self.press_b_widget)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 5)
        self.widget_69 = QWidget(self.press_b_widget)
        self.widget_69.setObjectName(u"widget_69")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_69)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(5, 5, 5, 5)
        self.widget_19 = QWidget(self.widget_69)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setStyleSheet(u"color: rgb(251, 140, 0);")
        self.verticalLayout_20 = QVBoxLayout(self.widget_19)
        self.verticalLayout_20.setSpacing(10)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_164 = QLabel(self.widget_19)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setFont(font13)
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
        self.label_168.setFont(font14)
        self.label_168.setStyleSheet(u"color: rgb(229, 57, 53);")
        self.label_168.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_168)

        self.line_15 = QFrame(self.widget_21)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setStyleSheet(u"border: 2px solid rgb(251, 140, 0);")
        self.line_15.setFrameShape(QFrame.Shape.VLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_20.addWidget(self.line_15)

        self.label_170 = QLabel(self.widget_21)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setFont(font14)
        self.label_170.setStyleSheet(u"color: rgb(67, 160, 71);")
        self.label_170.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_170)

        self.horizontalLayout_20.setStretch(0, 1)
        self.horizontalLayout_20.setStretch(2, 1)

        self.horizontalLayout_19.addWidget(self.widget_21)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_19.setStretch(0, 4)
        self.horizontalLayout_19.setStretch(1, 1)

        self.verticalLayout_20.addWidget(self.widget_20)


        self.horizontalLayout_16.addWidget(self.widget_19)


        self.verticalLayout_30.addWidget(self.widget_69)

        self.widget_59 = QWidget(self.press_b_widget)
        self.widget_59.setObjectName(u"widget_59")
        self.widget_59.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.verticalLayout_44 = QVBoxLayout(self.widget_59)
        self.verticalLayout_44.setSpacing(10)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.widget_284 = QWidget(self.widget_59)
        self.widget_284.setObjectName(u"widget_284")
        self.horizontalLayout_350 = QHBoxLayout(self.widget_284)
        self.horizontalLayout_350.setSpacing(7)
        self.horizontalLayout_350.setObjectName(u"horizontalLayout_350")
        self.horizontalLayout_350.setContentsMargins(0, 0, 0, 0)
        self.widget_176 = QWidget(self.widget_284)
        self.widget_176.setObjectName(u"widget_176")
        self.widget_176.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_351 = QHBoxLayout(self.widget_176)
        self.horizontalLayout_351.setObjectName(u"horizontalLayout_351")
        self.horizontalLayout_351.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_1 = QDoubleSpinBox(self.widget_176)
        self.pressure_pv_b_1.setObjectName(u"pressure_pv_b_1")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_1.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_1.setSizePolicy(sizePolicy)
        self.pressure_pv_b_1.setFont(font15)
        self.pressure_pv_b_1.setStyleSheet(u"")
        self.pressure_pv_b_1.setWrapping(True)
        self.pressure_pv_b_1.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_1.setReadOnly(True)
        self.pressure_pv_b_1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_1.setDecimals(1)
        self.pressure_pv_b_1.setMaximum(999.000000000000000)
        self.pressure_pv_b_1.setValue(0.000000000000000)

        self.horizontalLayout_351.addWidget(self.pressure_pv_b_1)

        self.line_31 = QFrame(self.widget_176)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setStyleSheet(u"border: 2px solid rgb(251, 140, 0);")
        self.line_31.setFrameShape(QFrame.Shape.VLine)
        self.line_31.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_351.addWidget(self.line_31)

        self.pressure_sv_b_1 = QDoubleSpinBox(self.widget_176)
        self.pressure_sv_b_1.setObjectName(u"pressure_sv_b_1")
        sizePolicy.setHeightForWidth(self.pressure_sv_b_1.sizePolicy().hasHeightForWidth())
        self.pressure_sv_b_1.setSizePolicy(sizePolicy)
        self.pressure_sv_b_1.setFont(font15)
        self.pressure_sv_b_1.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_b_1.setWrapping(False)
        self.pressure_sv_b_1.setAlignment(Qt.AlignCenter)
        self.pressure_sv_b_1.setReadOnly(False)
        self.pressure_sv_b_1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_b_1.setDecimals(1)
        self.pressure_sv_b_1.setMaximum(999.000000000000000)
        self.pressure_sv_b_1.setValue(0.000000000000000)

        self.horizontalLayout_351.addWidget(self.pressure_sv_b_1)

        self.horizontalLayout_351.setStretch(0, 1)
        self.horizontalLayout_351.setStretch(2, 1)

        self.horizontalLayout_350.addWidget(self.widget_176)

        self.stacked_cel_fah_press_b_1 = QStackedWidget(self.widget_284)
        self.stacked_cel_fah_press_b_1.setObjectName(u"stacked_cel_fah_press_b_1")
        self.celsius_ap_19 = QWidget()
        self.celsius_ap_19.setObjectName(u"celsius_ap_19")
        self.horizontalLayout_398 = QHBoxLayout(self.celsius_ap_19)
        self.horizontalLayout_398.setObjectName(u"horizontalLayout_398")
        self.horizontalLayout_398.setContentsMargins(0, 0, 0, 0)
        self.label_275 = QLabel(self.celsius_ap_19)
        self.label_275.setObjectName(u"label_275")
        self.label_275.setFont(font16)
        self.label_275.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_275.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_398.addWidget(self.label_275)

        self.stacked_cel_fah_press_b_1.addWidget(self.celsius_ap_19)
        self.fahrenheit_ap_19 = QWidget()
        self.fahrenheit_ap_19.setObjectName(u"fahrenheit_ap_19")
        self.horizontalLayout_399 = QHBoxLayout(self.fahrenheit_ap_19)
        self.horizontalLayout_399.setObjectName(u"horizontalLayout_399")
        self.horizontalLayout_399.setContentsMargins(0, 0, 0, 0)
        self.label_341 = QLabel(self.fahrenheit_ap_19)
        self.label_341.setObjectName(u"label_341")
        self.label_341.setFont(font16)
        self.label_341.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_341.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_399.addWidget(self.label_341)

        self.stacked_cel_fah_press_b_1.addWidget(self.fahrenheit_ap_19)

        self.horizontalLayout_350.addWidget(self.stacked_cel_fah_press_b_1)

        self.horizontalLayout_350.setStretch(0, 3)
        self.horizontalLayout_350.setStretch(1, 1)

        self.verticalLayout_44.addWidget(self.widget_284)

        self.widget_285 = QWidget(self.widget_59)
        self.widget_285.setObjectName(u"widget_285")
        self.horizontalLayout_352 = QHBoxLayout(self.widget_285)
        self.horizontalLayout_352.setSpacing(7)
        self.horizontalLayout_352.setObjectName(u"horizontalLayout_352")
        self.horizontalLayout_352.setContentsMargins(0, 0, 0, 0)
        self.widget_177 = QWidget(self.widget_285)
        self.widget_177.setObjectName(u"widget_177")
        self.widget_177.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_353 = QHBoxLayout(self.widget_177)
        self.horizontalLayout_353.setObjectName(u"horizontalLayout_353")
        self.horizontalLayout_353.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_2 = QDoubleSpinBox(self.widget_177)
        self.pressure_pv_b_2.setObjectName(u"pressure_pv_b_2")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_2.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_2.setSizePolicy(sizePolicy)
        self.pressure_pv_b_2.setFont(font15)
        self.pressure_pv_b_2.setStyleSheet(u"")
        self.pressure_pv_b_2.setWrapping(True)
        self.pressure_pv_b_2.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_2.setReadOnly(True)
        self.pressure_pv_b_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_2.setDecimals(1)
        self.pressure_pv_b_2.setMaximum(999.000000000000000)
        self.pressure_pv_b_2.setValue(0.000000000000000)

        self.horizontalLayout_353.addWidget(self.pressure_pv_b_2)

        self.line_32 = QFrame(self.widget_177)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setStyleSheet(u"border: 2px solid rgb(251, 140, 0);")
        self.line_32.setFrameShape(QFrame.Shape.VLine)
        self.line_32.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_353.addWidget(self.line_32)

        self.pressure_sv_b_2 = QDoubleSpinBox(self.widget_177)
        self.pressure_sv_b_2.setObjectName(u"pressure_sv_b_2")
        sizePolicy.setHeightForWidth(self.pressure_sv_b_2.sizePolicy().hasHeightForWidth())
        self.pressure_sv_b_2.setSizePolicy(sizePolicy)
        self.pressure_sv_b_2.setFont(font15)
        self.pressure_sv_b_2.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_b_2.setWrapping(False)
        self.pressure_sv_b_2.setAlignment(Qt.AlignCenter)
        self.pressure_sv_b_2.setReadOnly(False)
        self.pressure_sv_b_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_b_2.setDecimals(1)
        self.pressure_sv_b_2.setMaximum(999.000000000000000)
        self.pressure_sv_b_2.setValue(0.000000000000000)

        self.horizontalLayout_353.addWidget(self.pressure_sv_b_2)

        self.horizontalLayout_353.setStretch(0, 1)
        self.horizontalLayout_353.setStretch(2, 1)

        self.horizontalLayout_352.addWidget(self.widget_177)

        self.stacked_cel_fah_press_b_2 = QStackedWidget(self.widget_285)
        self.stacked_cel_fah_press_b_2.setObjectName(u"stacked_cel_fah_press_b_2")
        self.celsius_ap_20 = QWidget()
        self.celsius_ap_20.setObjectName(u"celsius_ap_20")
        self.horizontalLayout_400 = QHBoxLayout(self.celsius_ap_20)
        self.horizontalLayout_400.setObjectName(u"horizontalLayout_400")
        self.horizontalLayout_400.setContentsMargins(0, 0, 0, 0)
        self.label_366 = QLabel(self.celsius_ap_20)
        self.label_366.setObjectName(u"label_366")
        self.label_366.setFont(font16)
        self.label_366.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_366.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_400.addWidget(self.label_366)

        self.stacked_cel_fah_press_b_2.addWidget(self.celsius_ap_20)
        self.fahrenheit_ap_20 = QWidget()
        self.fahrenheit_ap_20.setObjectName(u"fahrenheit_ap_20")
        self.horizontalLayout_401 = QHBoxLayout(self.fahrenheit_ap_20)
        self.horizontalLayout_401.setObjectName(u"horizontalLayout_401")
        self.horizontalLayout_401.setContentsMargins(0, 0, 0, 0)
        self.label_367 = QLabel(self.fahrenheit_ap_20)
        self.label_367.setObjectName(u"label_367")
        self.label_367.setFont(font16)
        self.label_367.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_367.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_401.addWidget(self.label_367)

        self.stacked_cel_fah_press_b_2.addWidget(self.fahrenheit_ap_20)

        self.horizontalLayout_352.addWidget(self.stacked_cel_fah_press_b_2)

        self.horizontalLayout_352.setStretch(0, 3)
        self.horizontalLayout_352.setStretch(1, 1)

        self.verticalLayout_44.addWidget(self.widget_285)

        self.widget_286 = QWidget(self.widget_59)
        self.widget_286.setObjectName(u"widget_286")
        self.horizontalLayout_354 = QHBoxLayout(self.widget_286)
        self.horizontalLayout_354.setSpacing(7)
        self.horizontalLayout_354.setObjectName(u"horizontalLayout_354")
        self.horizontalLayout_354.setContentsMargins(0, 0, 0, 0)
        self.widget_178 = QWidget(self.widget_286)
        self.widget_178.setObjectName(u"widget_178")
        self.widget_178.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_355 = QHBoxLayout(self.widget_178)
        self.horizontalLayout_355.setObjectName(u"horizontalLayout_355")
        self.horizontalLayout_355.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_3 = QDoubleSpinBox(self.widget_178)
        self.pressure_pv_b_3.setObjectName(u"pressure_pv_b_3")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_3.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_3.setSizePolicy(sizePolicy)
        self.pressure_pv_b_3.setFont(font15)
        self.pressure_pv_b_3.setStyleSheet(u"")
        self.pressure_pv_b_3.setWrapping(True)
        self.pressure_pv_b_3.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_3.setReadOnly(True)
        self.pressure_pv_b_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_3.setDecimals(1)
        self.pressure_pv_b_3.setMaximum(999.000000000000000)
        self.pressure_pv_b_3.setValue(0.000000000000000)

        self.horizontalLayout_355.addWidget(self.pressure_pv_b_3)

        self.line_33 = QFrame(self.widget_178)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setStyleSheet(u"border: 2px solid rgb(251, 140, 0);")
        self.line_33.setFrameShape(QFrame.Shape.VLine)
        self.line_33.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_355.addWidget(self.line_33)

        self.pressure_sv_b_3 = QDoubleSpinBox(self.widget_178)
        self.pressure_sv_b_3.setObjectName(u"pressure_sv_b_3")
        sizePolicy.setHeightForWidth(self.pressure_sv_b_3.sizePolicy().hasHeightForWidth())
        self.pressure_sv_b_3.setSizePolicy(sizePolicy)
        self.pressure_sv_b_3.setFont(font15)
        self.pressure_sv_b_3.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_b_3.setWrapping(False)
        self.pressure_sv_b_3.setAlignment(Qt.AlignCenter)
        self.pressure_sv_b_3.setReadOnly(False)
        self.pressure_sv_b_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_b_3.setDecimals(1)
        self.pressure_sv_b_3.setMaximum(999.000000000000000)
        self.pressure_sv_b_3.setValue(0.000000000000000)

        self.horizontalLayout_355.addWidget(self.pressure_sv_b_3)

        self.horizontalLayout_355.setStretch(0, 1)
        self.horizontalLayout_355.setStretch(2, 1)

        self.horizontalLayout_354.addWidget(self.widget_178)

        self.stacked_cel_fah_press_b_3 = QStackedWidget(self.widget_286)
        self.stacked_cel_fah_press_b_3.setObjectName(u"stacked_cel_fah_press_b_3")
        self.celsius_ap_21 = QWidget()
        self.celsius_ap_21.setObjectName(u"celsius_ap_21")
        self.horizontalLayout_402 = QHBoxLayout(self.celsius_ap_21)
        self.horizontalLayout_402.setObjectName(u"horizontalLayout_402")
        self.horizontalLayout_402.setContentsMargins(0, 0, 0, 0)
        self.label_368 = QLabel(self.celsius_ap_21)
        self.label_368.setObjectName(u"label_368")
        self.label_368.setFont(font16)
        self.label_368.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_368.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_402.addWidget(self.label_368)

        self.stacked_cel_fah_press_b_3.addWidget(self.celsius_ap_21)
        self.fahrenheit_ap_21 = QWidget()
        self.fahrenheit_ap_21.setObjectName(u"fahrenheit_ap_21")
        self.horizontalLayout_403 = QHBoxLayout(self.fahrenheit_ap_21)
        self.horizontalLayout_403.setObjectName(u"horizontalLayout_403")
        self.horizontalLayout_403.setContentsMargins(0, 0, 0, 0)
        self.label_369 = QLabel(self.fahrenheit_ap_21)
        self.label_369.setObjectName(u"label_369")
        self.label_369.setFont(font16)
        self.label_369.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_369.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_403.addWidget(self.label_369)

        self.stacked_cel_fah_press_b_3.addWidget(self.fahrenheit_ap_21)

        self.horizontalLayout_354.addWidget(self.stacked_cel_fah_press_b_3)

        self.horizontalLayout_354.setStretch(0, 3)
        self.horizontalLayout_354.setStretch(1, 1)

        self.verticalLayout_44.addWidget(self.widget_286)

        self.widget_287 = QWidget(self.widget_59)
        self.widget_287.setObjectName(u"widget_287")
        self.horizontalLayout_356 = QHBoxLayout(self.widget_287)
        self.horizontalLayout_356.setSpacing(7)
        self.horizontalLayout_356.setObjectName(u"horizontalLayout_356")
        self.horizontalLayout_356.setContentsMargins(0, 0, 0, 0)
        self.widget_179 = QWidget(self.widget_287)
        self.widget_179.setObjectName(u"widget_179")
        self.widget_179.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_357 = QHBoxLayout(self.widget_179)
        self.horizontalLayout_357.setObjectName(u"horizontalLayout_357")
        self.horizontalLayout_357.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_4 = QDoubleSpinBox(self.widget_179)
        self.pressure_pv_b_4.setObjectName(u"pressure_pv_b_4")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_4.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_4.setSizePolicy(sizePolicy)
        self.pressure_pv_b_4.setFont(font15)
        self.pressure_pv_b_4.setStyleSheet(u"")
        self.pressure_pv_b_4.setWrapping(True)
        self.pressure_pv_b_4.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_4.setReadOnly(True)
        self.pressure_pv_b_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_4.setDecimals(1)
        self.pressure_pv_b_4.setMaximum(999.000000000000000)
        self.pressure_pv_b_4.setValue(0.000000000000000)

        self.horizontalLayout_357.addWidget(self.pressure_pv_b_4)

        self.line_34 = QFrame(self.widget_179)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setStyleSheet(u"border: 2px solid rgb(251, 140, 0);")
        self.line_34.setFrameShape(QFrame.Shape.VLine)
        self.line_34.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_357.addWidget(self.line_34)

        self.pressure_sv_b_4 = QDoubleSpinBox(self.widget_179)
        self.pressure_sv_b_4.setObjectName(u"pressure_sv_b_4")
        sizePolicy.setHeightForWidth(self.pressure_sv_b_4.sizePolicy().hasHeightForWidth())
        self.pressure_sv_b_4.setSizePolicy(sizePolicy)
        self.pressure_sv_b_4.setFont(font15)
        self.pressure_sv_b_4.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_b_4.setWrapping(False)
        self.pressure_sv_b_4.setAlignment(Qt.AlignCenter)
        self.pressure_sv_b_4.setReadOnly(False)
        self.pressure_sv_b_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_b_4.setDecimals(1)
        self.pressure_sv_b_4.setMaximum(999.000000000000000)
        self.pressure_sv_b_4.setValue(0.000000000000000)

        self.horizontalLayout_357.addWidget(self.pressure_sv_b_4)

        self.horizontalLayout_357.setStretch(0, 1)
        self.horizontalLayout_357.setStretch(2, 1)

        self.horizontalLayout_356.addWidget(self.widget_179)

        self.stacked_cel_fah_press_b_4 = QStackedWidget(self.widget_287)
        self.stacked_cel_fah_press_b_4.setObjectName(u"stacked_cel_fah_press_b_4")
        self.celsius_ap_22 = QWidget()
        self.celsius_ap_22.setObjectName(u"celsius_ap_22")
        self.horizontalLayout_404 = QHBoxLayout(self.celsius_ap_22)
        self.horizontalLayout_404.setObjectName(u"horizontalLayout_404")
        self.horizontalLayout_404.setContentsMargins(0, 0, 0, 0)
        self.label_370 = QLabel(self.celsius_ap_22)
        self.label_370.setObjectName(u"label_370")
        self.label_370.setFont(font16)
        self.label_370.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_370.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_404.addWidget(self.label_370)

        self.stacked_cel_fah_press_b_4.addWidget(self.celsius_ap_22)
        self.fahrenheit_ap_22 = QWidget()
        self.fahrenheit_ap_22.setObjectName(u"fahrenheit_ap_22")
        self.horizontalLayout_405 = QHBoxLayout(self.fahrenheit_ap_22)
        self.horizontalLayout_405.setObjectName(u"horizontalLayout_405")
        self.horizontalLayout_405.setContentsMargins(0, 0, 0, 0)
        self.label_371 = QLabel(self.fahrenheit_ap_22)
        self.label_371.setObjectName(u"label_371")
        self.label_371.setFont(font16)
        self.label_371.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_371.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_405.addWidget(self.label_371)

        self.stacked_cel_fah_press_b_4.addWidget(self.fahrenheit_ap_22)

        self.horizontalLayout_356.addWidget(self.stacked_cel_fah_press_b_4)

        self.horizontalLayout_356.setStretch(0, 3)
        self.horizontalLayout_356.setStretch(1, 1)

        self.verticalLayout_44.addWidget(self.widget_287)

        self.widget_288 = QWidget(self.widget_59)
        self.widget_288.setObjectName(u"widget_288")
        self.horizontalLayout_358 = QHBoxLayout(self.widget_288)
        self.horizontalLayout_358.setObjectName(u"horizontalLayout_358")
        self.horizontalLayout_358.setContentsMargins(0, 0, 0, 0)
        self.widget_188 = QWidget(self.widget_288)
        self.widget_188.setObjectName(u"widget_188")
        self.widget_188.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_359 = QHBoxLayout(self.widget_188)
        self.horizontalLayout_359.setObjectName(u"horizontalLayout_359")
        self.horizontalLayout_359.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_5 = QDoubleSpinBox(self.widget_188)
        self.pressure_pv_b_5.setObjectName(u"pressure_pv_b_5")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_5.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_5.setSizePolicy(sizePolicy)
        self.pressure_pv_b_5.setFont(font15)
        self.pressure_pv_b_5.setStyleSheet(u"")
        self.pressure_pv_b_5.setWrapping(True)
        self.pressure_pv_b_5.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_5.setReadOnly(True)
        self.pressure_pv_b_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_5.setDecimals(1)
        self.pressure_pv_b_5.setMaximum(999.000000000000000)
        self.pressure_pv_b_5.setValue(0.000000000000000)

        self.horizontalLayout_359.addWidget(self.pressure_pv_b_5)

        self.line_35 = QFrame(self.widget_188)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setStyleSheet(u"border: 2px solid rgb(251, 140, 0);")
        self.line_35.setFrameShape(QFrame.Shape.VLine)
        self.line_35.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_359.addWidget(self.line_35)

        self.pressure_sv_b_5 = QDoubleSpinBox(self.widget_188)
        self.pressure_sv_b_5.setObjectName(u"pressure_sv_b_5")
        sizePolicy.setHeightForWidth(self.pressure_sv_b_5.sizePolicy().hasHeightForWidth())
        self.pressure_sv_b_5.setSizePolicy(sizePolicy)
        self.pressure_sv_b_5.setFont(font15)
        self.pressure_sv_b_5.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_b_5.setWrapping(False)
        self.pressure_sv_b_5.setAlignment(Qt.AlignCenter)
        self.pressure_sv_b_5.setReadOnly(False)
        self.pressure_sv_b_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_b_5.setDecimals(1)
        self.pressure_sv_b_5.setMaximum(999.000000000000000)
        self.pressure_sv_b_5.setValue(0.000000000000000)

        self.horizontalLayout_359.addWidget(self.pressure_sv_b_5)

        self.horizontalLayout_359.setStretch(0, 1)
        self.horizontalLayout_359.setStretch(2, 1)

        self.horizontalLayout_358.addWidget(self.widget_188)

        self.label_205 = QLabel(self.widget_288)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setFont(font16)
        self.label_205.setAlignment(Qt.AlignCenter)
        self.label_205.setWordWrap(True)

        self.horizontalLayout_358.addWidget(self.label_205)

        self.horizontalLayout_358.setStretch(0, 3)
        self.horizontalLayout_358.setStretch(1, 1)

        self.verticalLayout_44.addWidget(self.widget_288)

        self.widget_289 = QWidget(self.widget_59)
        self.widget_289.setObjectName(u"widget_289")
        self.horizontalLayout_360 = QHBoxLayout(self.widget_289)
        self.horizontalLayout_360.setObjectName(u"horizontalLayout_360")
        self.horizontalLayout_360.setContentsMargins(0, 0, 0, 0)
        self.widget_189 = QWidget(self.widget_289)
        self.widget_189.setObjectName(u"widget_189")
        self.widget_189.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_361 = QHBoxLayout(self.widget_189)
        self.horizontalLayout_361.setObjectName(u"horizontalLayout_361")
        self.horizontalLayout_361.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_6 = QDoubleSpinBox(self.widget_189)
        self.pressure_pv_b_6.setObjectName(u"pressure_pv_b_6")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_6.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_6.setSizePolicy(sizePolicy)
        self.pressure_pv_b_6.setFont(font15)
        self.pressure_pv_b_6.setStyleSheet(u"")
        self.pressure_pv_b_6.setWrapping(True)
        self.pressure_pv_b_6.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_6.setReadOnly(True)
        self.pressure_pv_b_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_6.setDecimals(1)
        self.pressure_pv_b_6.setMaximum(999.000000000000000)
        self.pressure_pv_b_6.setValue(0.000000000000000)

        self.horizontalLayout_361.addWidget(self.pressure_pv_b_6)

        self.line_36 = QFrame(self.widget_189)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setStyleSheet(u"border: 2px solid rgb(251, 140, 0);")
        self.line_36.setFrameShape(QFrame.Shape.VLine)
        self.line_36.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_361.addWidget(self.line_36)

        self.pressure_sv_b_6 = QDoubleSpinBox(self.widget_189)
        self.pressure_sv_b_6.setObjectName(u"pressure_sv_b_6")
        sizePolicy.setHeightForWidth(self.pressure_sv_b_6.sizePolicy().hasHeightForWidth())
        self.pressure_sv_b_6.setSizePolicy(sizePolicy)
        self.pressure_sv_b_6.setFont(font15)
        self.pressure_sv_b_6.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_b_6.setWrapping(False)
        self.pressure_sv_b_6.setAlignment(Qt.AlignCenter)
        self.pressure_sv_b_6.setReadOnly(False)
        self.pressure_sv_b_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_b_6.setDecimals(1)
        self.pressure_sv_b_6.setMaximum(999.000000000000000)
        self.pressure_sv_b_6.setValue(0.000000000000000)

        self.horizontalLayout_361.addWidget(self.pressure_sv_b_6)

        self.horizontalLayout_361.setStretch(0, 1)
        self.horizontalLayout_361.setStretch(2, 1)

        self.horizontalLayout_360.addWidget(self.widget_189)

        self.label_217 = QLabel(self.widget_289)
        self.label_217.setObjectName(u"label_217")
        self.label_217.setFont(font16)
        self.label_217.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_360.addWidget(self.label_217)

        self.horizontalLayout_360.setStretch(0, 3)
        self.horizontalLayout_360.setStretch(1, 1)

        self.verticalLayout_44.addWidget(self.widget_289)

        self.widget_290 = QWidget(self.widget_59)
        self.widget_290.setObjectName(u"widget_290")
        self.horizontalLayout_362 = QHBoxLayout(self.widget_290)
        self.horizontalLayout_362.setObjectName(u"horizontalLayout_362")
        self.horizontalLayout_362.setContentsMargins(0, 0, 0, 0)
        self.widget_190 = QWidget(self.widget_290)
        self.widget_190.setObjectName(u"widget_190")
        self.widget_190.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_364 = QHBoxLayout(self.widget_190)
        self.horizontalLayout_364.setObjectName(u"horizontalLayout_364")
        self.horizontalLayout_364.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_7 = QDoubleSpinBox(self.widget_190)
        self.pressure_pv_b_7.setObjectName(u"pressure_pv_b_7")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_7.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_7.setSizePolicy(sizePolicy)
        self.pressure_pv_b_7.setFont(font15)
        self.pressure_pv_b_7.setStyleSheet(u"")
        self.pressure_pv_b_7.setWrapping(True)
        self.pressure_pv_b_7.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_7.setReadOnly(True)
        self.pressure_pv_b_7.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_7.setDecimals(1)
        self.pressure_pv_b_7.setMaximum(999.000000000000000)
        self.pressure_pv_b_7.setValue(0.000000000000000)

        self.horizontalLayout_364.addWidget(self.pressure_pv_b_7)

        self.line_37 = QFrame(self.widget_190)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setStyleSheet(u"border: 2px solid rgb(251, 140, 0);")
        self.line_37.setFrameShape(QFrame.Shape.VLine)
        self.line_37.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_364.addWidget(self.line_37)

        self.pressure_sv_b_7 = QDoubleSpinBox(self.widget_190)
        self.pressure_sv_b_7.setObjectName(u"pressure_sv_b_7")
        sizePolicy.setHeightForWidth(self.pressure_sv_b_7.sizePolicy().hasHeightForWidth())
        self.pressure_sv_b_7.setSizePolicy(sizePolicy)
        self.pressure_sv_b_7.setFont(font15)
        self.pressure_sv_b_7.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_b_7.setWrapping(False)
        self.pressure_sv_b_7.setAlignment(Qt.AlignCenter)
        self.pressure_sv_b_7.setReadOnly(False)
        self.pressure_sv_b_7.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_b_7.setDecimals(1)
        self.pressure_sv_b_7.setMaximum(999.000000000000000)
        self.pressure_sv_b_7.setValue(0.000000000000000)

        self.horizontalLayout_364.addWidget(self.pressure_sv_b_7)

        self.horizontalLayout_364.setStretch(0, 1)
        self.horizontalLayout_364.setStretch(2, 1)

        self.horizontalLayout_362.addWidget(self.widget_190)

        self.label_218 = QLabel(self.widget_290)
        self.label_218.setObjectName(u"label_218")
        self.label_218.setFont(font16)
        self.label_218.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_362.addWidget(self.label_218)

        self.horizontalLayout_362.setStretch(0, 3)
        self.horizontalLayout_362.setStretch(1, 1)

        self.verticalLayout_44.addWidget(self.widget_290)

        self.widget_291 = QWidget(self.widget_59)
        self.widget_291.setObjectName(u"widget_291")
        self.horizontalLayout_365 = QHBoxLayout(self.widget_291)
        self.horizontalLayout_365.setObjectName(u"horizontalLayout_365")
        self.horizontalLayout_365.setContentsMargins(0, 0, 0, 0)
        self.widget_191 = QWidget(self.widget_291)
        self.widget_191.setObjectName(u"widget_191")
        self.widget_191.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_366 = QHBoxLayout(self.widget_191)
        self.horizontalLayout_366.setObjectName(u"horizontalLayout_366")
        self.horizontalLayout_366.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_8 = QDoubleSpinBox(self.widget_191)
        self.pressure_pv_b_8.setObjectName(u"pressure_pv_b_8")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_8.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_8.setSizePolicy(sizePolicy)
        self.pressure_pv_b_8.setFont(font15)
        self.pressure_pv_b_8.setStyleSheet(u"")
        self.pressure_pv_b_8.setWrapping(True)
        self.pressure_pv_b_8.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_8.setReadOnly(True)
        self.pressure_pv_b_8.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_8.setDecimals(1)
        self.pressure_pv_b_8.setMaximum(999.000000000000000)
        self.pressure_pv_b_8.setValue(0.000000000000000)

        self.horizontalLayout_366.addWidget(self.pressure_pv_b_8)

        self.line_38 = QFrame(self.widget_191)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setStyleSheet(u"border: 2px solid rgb(251, 140, 0);")
        self.line_38.setFrameShape(QFrame.Shape.VLine)
        self.line_38.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_366.addWidget(self.line_38)

        self.pressure_sv_b_8 = QDoubleSpinBox(self.widget_191)
        self.pressure_sv_b_8.setObjectName(u"pressure_sv_b_8")
        sizePolicy.setHeightForWidth(self.pressure_sv_b_8.sizePolicy().hasHeightForWidth())
        self.pressure_sv_b_8.setSizePolicy(sizePolicy)
        self.pressure_sv_b_8.setFont(font15)
        self.pressure_sv_b_8.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_b_8.setWrapping(False)
        self.pressure_sv_b_8.setAlignment(Qt.AlignCenter)
        self.pressure_sv_b_8.setReadOnly(False)
        self.pressure_sv_b_8.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_b_8.setDecimals(1)
        self.pressure_sv_b_8.setMaximum(999.000000000000000)
        self.pressure_sv_b_8.setValue(0.000000000000000)

        self.horizontalLayout_366.addWidget(self.pressure_sv_b_8)

        self.horizontalLayout_366.setStretch(0, 1)
        self.horizontalLayout_366.setStretch(2, 1)

        self.horizontalLayout_365.addWidget(self.widget_191)

        self.label_219 = QLabel(self.widget_291)
        self.label_219.setObjectName(u"label_219")
        self.label_219.setFont(font16)
        self.label_219.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_365.addWidget(self.label_219)

        self.horizontalLayout_365.setStretch(0, 3)
        self.horizontalLayout_365.setStretch(1, 1)

        self.verticalLayout_44.addWidget(self.widget_291)

        self.widget_292 = QWidget(self.widget_59)
        self.widget_292.setObjectName(u"widget_292")
        self.horizontalLayout_367 = QHBoxLayout(self.widget_292)
        self.horizontalLayout_367.setObjectName(u"horizontalLayout_367")
        self.horizontalLayout_367.setContentsMargins(0, 0, 0, 0)
        self.widget_192 = QWidget(self.widget_292)
        self.widget_192.setObjectName(u"widget_192")
        self.widget_192.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_368 = QHBoxLayout(self.widget_192)
        self.horizontalLayout_368.setObjectName(u"horizontalLayout_368")
        self.horizontalLayout_368.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_9 = QDoubleSpinBox(self.widget_192)
        self.pressure_pv_b_9.setObjectName(u"pressure_pv_b_9")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_9.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_9.setSizePolicy(sizePolicy)
        self.pressure_pv_b_9.setFont(font15)
        self.pressure_pv_b_9.setStyleSheet(u"")
        self.pressure_pv_b_9.setWrapping(True)
        self.pressure_pv_b_9.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_9.setReadOnly(True)
        self.pressure_pv_b_9.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_9.setDecimals(1)
        self.pressure_pv_b_9.setMaximum(999.000000000000000)
        self.pressure_pv_b_9.setValue(0.000000000000000)

        self.horizontalLayout_368.addWidget(self.pressure_pv_b_9)

        self.line_39 = QFrame(self.widget_192)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setStyleSheet(u"border: 2px solid rgb(251, 140, 0);")
        self.line_39.setFrameShape(QFrame.Shape.VLine)
        self.line_39.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_368.addWidget(self.line_39)

        self.pressure_sv_b_9 = QDoubleSpinBox(self.widget_192)
        self.pressure_sv_b_9.setObjectName(u"pressure_sv_b_9")
        sizePolicy.setHeightForWidth(self.pressure_sv_b_9.sizePolicy().hasHeightForWidth())
        self.pressure_sv_b_9.setSizePolicy(sizePolicy)
        self.pressure_sv_b_9.setFont(font15)
        self.pressure_sv_b_9.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_b_9.setWrapping(False)
        self.pressure_sv_b_9.setAlignment(Qt.AlignCenter)
        self.pressure_sv_b_9.setReadOnly(False)
        self.pressure_sv_b_9.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_b_9.setDecimals(1)
        self.pressure_sv_b_9.setMaximum(999.000000000000000)
        self.pressure_sv_b_9.setValue(0.000000000000000)

        self.horizontalLayout_368.addWidget(self.pressure_sv_b_9)

        self.horizontalLayout_368.setStretch(0, 1)
        self.horizontalLayout_368.setStretch(2, 1)

        self.horizontalLayout_367.addWidget(self.widget_192)

        self.label_220 = QLabel(self.widget_292)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setFont(font16)
        self.label_220.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_367.addWidget(self.label_220)

        self.horizontalLayout_367.setStretch(0, 3)
        self.horizontalLayout_367.setStretch(1, 1)

        self.verticalLayout_44.addWidget(self.widget_292)

        self.widget_293 = QWidget(self.widget_59)
        self.widget_293.setObjectName(u"widget_293")
        self.horizontalLayout_369 = QHBoxLayout(self.widget_293)
        self.horizontalLayout_369.setObjectName(u"horizontalLayout_369")
        self.horizontalLayout_369.setContentsMargins(0, 0, 0, 0)
        self.widget_194 = QWidget(self.widget_293)
        self.widget_194.setObjectName(u"widget_194")
        self.widget_194.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_370 = QHBoxLayout(self.widget_194)
        self.horizontalLayout_370.setObjectName(u"horizontalLayout_370")
        self.horizontalLayout_370.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_b_10 = QDoubleSpinBox(self.widget_194)
        self.pressure_pv_b_10.setObjectName(u"pressure_pv_b_10")
        sizePolicy.setHeightForWidth(self.pressure_pv_b_10.sizePolicy().hasHeightForWidth())
        self.pressure_pv_b_10.setSizePolicy(sizePolicy)
        self.pressure_pv_b_10.setFont(font15)
        self.pressure_pv_b_10.setStyleSheet(u"")
        self.pressure_pv_b_10.setWrapping(True)
        self.pressure_pv_b_10.setAlignment(Qt.AlignCenter)
        self.pressure_pv_b_10.setReadOnly(True)
        self.pressure_pv_b_10.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_b_10.setDecimals(1)
        self.pressure_pv_b_10.setMaximum(999.000000000000000)
        self.pressure_pv_b_10.setValue(0.000000000000000)

        self.horizontalLayout_370.addWidget(self.pressure_pv_b_10)

        self.line_40 = QFrame(self.widget_194)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setStyleSheet(u"border: 2px solid rgb(251, 140, 0);")
        self.line_40.setFrameShape(QFrame.Shape.VLine)
        self.line_40.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_370.addWidget(self.line_40)

        self.pressure_sv_b_10 = QDoubleSpinBox(self.widget_194)
        self.pressure_sv_b_10.setObjectName(u"pressure_sv_b_10")
        sizePolicy.setHeightForWidth(self.pressure_sv_b_10.sizePolicy().hasHeightForWidth())
        self.pressure_sv_b_10.setSizePolicy(sizePolicy)
        self.pressure_sv_b_10.setFont(font15)
        self.pressure_sv_b_10.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_b_10.setWrapping(False)
        self.pressure_sv_b_10.setAlignment(Qt.AlignCenter)
        self.pressure_sv_b_10.setReadOnly(False)
        self.pressure_sv_b_10.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_b_10.setDecimals(1)
        self.pressure_sv_b_10.setMaximum(999.000000000000000)
        self.pressure_sv_b_10.setValue(0.000000000000000)

        self.horizontalLayout_370.addWidget(self.pressure_sv_b_10)

        self.horizontalLayout_370.setStretch(0, 1)
        self.horizontalLayout_370.setStretch(2, 1)

        self.horizontalLayout_369.addWidget(self.widget_194)

        self.label_223 = QLabel(self.widget_293)
        self.label_223.setObjectName(u"label_223")
        self.label_223.setFont(font16)
        self.label_223.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_369.addWidget(self.label_223)

        self.horizontalLayout_369.setStretch(0, 3)
        self.horizontalLayout_369.setStretch(1, 1)

        self.verticalLayout_44.addWidget(self.widget_293)

        self.verticalLayout_44.setStretch(0, 1)
        self.verticalLayout_44.setStretch(1, 1)
        self.verticalLayout_44.setStretch(2, 1)
        self.verticalLayout_44.setStretch(3, 1)
        self.verticalLayout_44.setStretch(4, 1)
        self.verticalLayout_44.setStretch(5, 1)
        self.verticalLayout_44.setStretch(6, 1)
        self.verticalLayout_44.setStretch(7, 1)
        self.verticalLayout_44.setStretch(8, 1)
        self.verticalLayout_44.setStretch(9, 1)

        self.verticalLayout_30.addWidget(self.widget_59)


        self.horizontalLayout_7.addWidget(self.press_b_widget)

        self.line_6 = QFrame(self.widget_6)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line_6)

        self.press_c_widget = QWidget(self.widget_6)
        self.press_c_widget.setObjectName(u"press_c_widget")
        sizePolicy.setHeightForWidth(self.press_c_widget.sizePolicy().hasHeightForWidth())
        self.press_c_widget.setSizePolicy(sizePolicy)
        self.press_c_widget.setStyleSheet(u"border-left: None;")
        self.verticalLayout_31 = QVBoxLayout(self.press_c_widget)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 5)
        self.widget_70 = QWidget(self.press_c_widget)
        self.widget_70.setObjectName(u"widget_70")
        self.horizontalLayout_43 = QHBoxLayout(self.widget_70)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.widget_53 = QWidget(self.widget_70)
        self.widget_53.setObjectName(u"widget_53")
        self.horizontalLayout_363 = QHBoxLayout(self.widget_53)
        self.horizontalLayout_363.setSpacing(0)
        self.horizontalLayout_363.setObjectName(u"horizontalLayout_363")
        self.horizontalLayout_363.setContentsMargins(5, 5, 5, 5)
        self.widget_22 = QWidget(self.widget_53)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setStyleSheet(u"color: #6F00FF;")
        self.verticalLayout_22 = QVBoxLayout(self.widget_22)
        self.verticalLayout_22.setSpacing(10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_171 = QLabel(self.widget_22)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setFont(font13)
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
        self.label_172.setFont(font14)
        self.label_172.setStyleSheet(u"color: rgb(229, 57, 53);")
        self.label_172.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_172)

        self.line_16 = QFrame(self.widget_24)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setStyleSheet(u"border: 2px solid #6F00FF;")
        self.line_16.setFrameShape(QFrame.Shape.VLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_23.addWidget(self.line_16)

        self.label_175 = QLabel(self.widget_24)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setFont(font14)
        self.label_175.setStyleSheet(u"color: rgb(67, 160, 71);")
        self.label_175.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_175)

        self.horizontalLayout_23.setStretch(0, 1)
        self.horizontalLayout_23.setStretch(2, 1)

        self.horizontalLayout_22.addWidget(self.widget_24)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_22.setStretch(0, 4)
        self.horizontalLayout_22.setStretch(1, 1)

        self.verticalLayout_22.addWidget(self.widget_23)


        self.horizontalLayout_363.addWidget(self.widget_22)


        self.horizontalLayout_43.addWidget(self.widget_53)


        self.verticalLayout_31.addWidget(self.widget_70)

        self.widget_60 = QWidget(self.press_c_widget)
        self.widget_60.setObjectName(u"widget_60")
        self.widget_60.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.verticalLayout_46 = QVBoxLayout(self.widget_60)
        self.verticalLayout_46.setSpacing(10)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.widget_294 = QWidget(self.widget_60)
        self.widget_294.setObjectName(u"widget_294")
        self.horizontalLayout_371 = QHBoxLayout(self.widget_294)
        self.horizontalLayout_371.setSpacing(7)
        self.horizontalLayout_371.setObjectName(u"horizontalLayout_371")
        self.horizontalLayout_371.setContentsMargins(0, 0, 0, 0)
        self.widget_196 = QWidget(self.widget_294)
        self.widget_196.setObjectName(u"widget_196")
        self.widget_196.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_372 = QHBoxLayout(self.widget_196)
        self.horizontalLayout_372.setObjectName(u"horizontalLayout_372")
        self.horizontalLayout_372.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_1 = QDoubleSpinBox(self.widget_196)
        self.pressure_pv_c_1.setObjectName(u"pressure_pv_c_1")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_1.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_1.setSizePolicy(sizePolicy)
        self.pressure_pv_c_1.setFont(font15)
        self.pressure_pv_c_1.setStyleSheet(u"")
        self.pressure_pv_c_1.setWrapping(True)
        self.pressure_pv_c_1.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_1.setReadOnly(True)
        self.pressure_pv_c_1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_1.setDecimals(1)
        self.pressure_pv_c_1.setMaximum(999.000000000000000)
        self.pressure_pv_c_1.setValue(0.000000000000000)

        self.horizontalLayout_372.addWidget(self.pressure_pv_c_1)

        self.line_21 = QFrame(self.widget_196)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setStyleSheet(u"border: 2px solid #6F00FF;")
        self.line_21.setFrameShape(QFrame.Shape.VLine)
        self.line_21.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_372.addWidget(self.line_21)

        self.pressure_sv_c_1 = QDoubleSpinBox(self.widget_196)
        self.pressure_sv_c_1.setObjectName(u"pressure_sv_c_1")
        sizePolicy.setHeightForWidth(self.pressure_sv_c_1.sizePolicy().hasHeightForWidth())
        self.pressure_sv_c_1.setSizePolicy(sizePolicy)
        self.pressure_sv_c_1.setFont(font15)
        self.pressure_sv_c_1.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_c_1.setWrapping(False)
        self.pressure_sv_c_1.setAlignment(Qt.AlignCenter)
        self.pressure_sv_c_1.setReadOnly(False)
        self.pressure_sv_c_1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_c_1.setDecimals(1)
        self.pressure_sv_c_1.setMaximum(999.000000000000000)
        self.pressure_sv_c_1.setValue(0.000000000000000)

        self.horizontalLayout_372.addWidget(self.pressure_sv_c_1)

        self.horizontalLayout_372.setStretch(0, 1)
        self.horizontalLayout_372.setStretch(2, 1)

        self.horizontalLayout_371.addWidget(self.widget_196)

        self.stacked_cel_fah_press_c_1 = QStackedWidget(self.widget_294)
        self.stacked_cel_fah_press_c_1.setObjectName(u"stacked_cel_fah_press_c_1")
        self.celsius_ap_23 = QWidget()
        self.celsius_ap_23.setObjectName(u"celsius_ap_23")
        self.horizontalLayout_426 = QHBoxLayout(self.celsius_ap_23)
        self.horizontalLayout_426.setObjectName(u"horizontalLayout_426")
        self.horizontalLayout_426.setContentsMargins(0, 0, 0, 0)
        self.label_276 = QLabel(self.celsius_ap_23)
        self.label_276.setObjectName(u"label_276")
        self.label_276.setFont(font16)
        self.label_276.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_276.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_426.addWidget(self.label_276)

        self.stacked_cel_fah_press_c_1.addWidget(self.celsius_ap_23)
        self.fahrenheit_ap_23 = QWidget()
        self.fahrenheit_ap_23.setObjectName(u"fahrenheit_ap_23")
        self.horizontalLayout_427 = QHBoxLayout(self.fahrenheit_ap_23)
        self.horizontalLayout_427.setObjectName(u"horizontalLayout_427")
        self.horizontalLayout_427.setContentsMargins(0, 0, 0, 0)
        self.label_372 = QLabel(self.fahrenheit_ap_23)
        self.label_372.setObjectName(u"label_372")
        self.label_372.setFont(font16)
        self.label_372.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_372.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_427.addWidget(self.label_372)

        self.stacked_cel_fah_press_c_1.addWidget(self.fahrenheit_ap_23)

        self.horizontalLayout_371.addWidget(self.stacked_cel_fah_press_c_1)

        self.horizontalLayout_371.setStretch(0, 3)
        self.horizontalLayout_371.setStretch(1, 1)

        self.verticalLayout_46.addWidget(self.widget_294)

        self.widget_295 = QWidget(self.widget_60)
        self.widget_295.setObjectName(u"widget_295")
        self.horizontalLayout_373 = QHBoxLayout(self.widget_295)
        self.horizontalLayout_373.setSpacing(7)
        self.horizontalLayout_373.setObjectName(u"horizontalLayout_373")
        self.horizontalLayout_373.setContentsMargins(0, 0, 0, 0)
        self.widget_197 = QWidget(self.widget_295)
        self.widget_197.setObjectName(u"widget_197")
        self.widget_197.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_374 = QHBoxLayout(self.widget_197)
        self.horizontalLayout_374.setObjectName(u"horizontalLayout_374")
        self.horizontalLayout_374.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_2 = QDoubleSpinBox(self.widget_197)
        self.pressure_pv_c_2.setObjectName(u"pressure_pv_c_2")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_2.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_2.setSizePolicy(sizePolicy)
        self.pressure_pv_c_2.setFont(font15)
        self.pressure_pv_c_2.setStyleSheet(u"")
        self.pressure_pv_c_2.setWrapping(True)
        self.pressure_pv_c_2.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_2.setReadOnly(True)
        self.pressure_pv_c_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_2.setDecimals(1)
        self.pressure_pv_c_2.setMaximum(999.000000000000000)
        self.pressure_pv_c_2.setValue(0.000000000000000)

        self.horizontalLayout_374.addWidget(self.pressure_pv_c_2)

        self.line_22 = QFrame(self.widget_197)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setStyleSheet(u"border: 2px solid #6F00FF;")
        self.line_22.setFrameShape(QFrame.Shape.VLine)
        self.line_22.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_374.addWidget(self.line_22)

        self.pressure_sv_c_2 = QDoubleSpinBox(self.widget_197)
        self.pressure_sv_c_2.setObjectName(u"pressure_sv_c_2")
        sizePolicy.setHeightForWidth(self.pressure_sv_c_2.sizePolicy().hasHeightForWidth())
        self.pressure_sv_c_2.setSizePolicy(sizePolicy)
        self.pressure_sv_c_2.setFont(font15)
        self.pressure_sv_c_2.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_c_2.setWrapping(False)
        self.pressure_sv_c_2.setAlignment(Qt.AlignCenter)
        self.pressure_sv_c_2.setReadOnly(False)
        self.pressure_sv_c_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_c_2.setDecimals(1)
        self.pressure_sv_c_2.setMaximum(999.000000000000000)
        self.pressure_sv_c_2.setValue(0.000000000000000)

        self.horizontalLayout_374.addWidget(self.pressure_sv_c_2)

        self.horizontalLayout_374.setStretch(0, 1)
        self.horizontalLayout_374.setStretch(2, 1)

        self.horizontalLayout_373.addWidget(self.widget_197)

        self.stacked_cel_fah_press_c_2 = QStackedWidget(self.widget_295)
        self.stacked_cel_fah_press_c_2.setObjectName(u"stacked_cel_fah_press_c_2")
        self.celsius_ap_24 = QWidget()
        self.celsius_ap_24.setObjectName(u"celsius_ap_24")
        self.horizontalLayout_432 = QHBoxLayout(self.celsius_ap_24)
        self.horizontalLayout_432.setObjectName(u"horizontalLayout_432")
        self.horizontalLayout_432.setContentsMargins(0, 0, 0, 0)
        self.label_373 = QLabel(self.celsius_ap_24)
        self.label_373.setObjectName(u"label_373")
        self.label_373.setFont(font16)
        self.label_373.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_373.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_432.addWidget(self.label_373)

        self.stacked_cel_fah_press_c_2.addWidget(self.celsius_ap_24)
        self.fahrenheit_ap_24 = QWidget()
        self.fahrenheit_ap_24.setObjectName(u"fahrenheit_ap_24")
        self.horizontalLayout_433 = QHBoxLayout(self.fahrenheit_ap_24)
        self.horizontalLayout_433.setObjectName(u"horizontalLayout_433")
        self.horizontalLayout_433.setContentsMargins(0, 0, 0, 0)
        self.label_374 = QLabel(self.fahrenheit_ap_24)
        self.label_374.setObjectName(u"label_374")
        self.label_374.setFont(font16)
        self.label_374.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_374.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_433.addWidget(self.label_374)

        self.stacked_cel_fah_press_c_2.addWidget(self.fahrenheit_ap_24)

        self.horizontalLayout_373.addWidget(self.stacked_cel_fah_press_c_2)

        self.horizontalLayout_373.setStretch(0, 3)
        self.horizontalLayout_373.setStretch(1, 1)

        self.verticalLayout_46.addWidget(self.widget_295)

        self.widget_296 = QWidget(self.widget_60)
        self.widget_296.setObjectName(u"widget_296")
        self.horizontalLayout_375 = QHBoxLayout(self.widget_296)
        self.horizontalLayout_375.setSpacing(7)
        self.horizontalLayout_375.setObjectName(u"horizontalLayout_375")
        self.horizontalLayout_375.setContentsMargins(0, 0, 0, 0)
        self.widget_198 = QWidget(self.widget_296)
        self.widget_198.setObjectName(u"widget_198")
        self.widget_198.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_376 = QHBoxLayout(self.widget_198)
        self.horizontalLayout_376.setObjectName(u"horizontalLayout_376")
        self.horizontalLayout_376.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_3 = QDoubleSpinBox(self.widget_198)
        self.pressure_pv_c_3.setObjectName(u"pressure_pv_c_3")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_3.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_3.setSizePolicy(sizePolicy)
        self.pressure_pv_c_3.setFont(font15)
        self.pressure_pv_c_3.setStyleSheet(u"")
        self.pressure_pv_c_3.setWrapping(True)
        self.pressure_pv_c_3.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_3.setReadOnly(True)
        self.pressure_pv_c_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_3.setDecimals(1)
        self.pressure_pv_c_3.setMaximum(999.000000000000000)
        self.pressure_pv_c_3.setValue(0.000000000000000)

        self.horizontalLayout_376.addWidget(self.pressure_pv_c_3)

        self.line_23 = QFrame(self.widget_198)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setStyleSheet(u"border: 2px solid #6F00FF;")
        self.line_23.setFrameShape(QFrame.Shape.VLine)
        self.line_23.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_376.addWidget(self.line_23)

        self.pressure_sv_c_3 = QDoubleSpinBox(self.widget_198)
        self.pressure_sv_c_3.setObjectName(u"pressure_sv_c_3")
        sizePolicy.setHeightForWidth(self.pressure_sv_c_3.sizePolicy().hasHeightForWidth())
        self.pressure_sv_c_3.setSizePolicy(sizePolicy)
        self.pressure_sv_c_3.setFont(font15)
        self.pressure_sv_c_3.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_c_3.setWrapping(False)
        self.pressure_sv_c_3.setAlignment(Qt.AlignCenter)
        self.pressure_sv_c_3.setReadOnly(False)
        self.pressure_sv_c_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_c_3.setDecimals(1)
        self.pressure_sv_c_3.setMaximum(999.000000000000000)
        self.pressure_sv_c_3.setValue(0.000000000000000)

        self.horizontalLayout_376.addWidget(self.pressure_sv_c_3)

        self.horizontalLayout_376.setStretch(0, 1)
        self.horizontalLayout_376.setStretch(2, 1)

        self.horizontalLayout_375.addWidget(self.widget_198)

        self.stacked_cel_fah_press_c_3 = QStackedWidget(self.widget_296)
        self.stacked_cel_fah_press_c_3.setObjectName(u"stacked_cel_fah_press_c_3")
        self.celsius_ap_25 = QWidget()
        self.celsius_ap_25.setObjectName(u"celsius_ap_25")
        self.horizontalLayout_434 = QHBoxLayout(self.celsius_ap_25)
        self.horizontalLayout_434.setObjectName(u"horizontalLayout_434")
        self.horizontalLayout_434.setContentsMargins(0, 0, 0, 0)
        self.label_375 = QLabel(self.celsius_ap_25)
        self.label_375.setObjectName(u"label_375")
        self.label_375.setFont(font16)
        self.label_375.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_375.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_434.addWidget(self.label_375)

        self.stacked_cel_fah_press_c_3.addWidget(self.celsius_ap_25)
        self.fahrenheit_ap_25 = QWidget()
        self.fahrenheit_ap_25.setObjectName(u"fahrenheit_ap_25")
        self.horizontalLayout_466 = QHBoxLayout(self.fahrenheit_ap_25)
        self.horizontalLayout_466.setObjectName(u"horizontalLayout_466")
        self.horizontalLayout_466.setContentsMargins(0, 0, 0, 0)
        self.label_376 = QLabel(self.fahrenheit_ap_25)
        self.label_376.setObjectName(u"label_376")
        self.label_376.setFont(font16)
        self.label_376.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_376.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_466.addWidget(self.label_376)

        self.stacked_cel_fah_press_c_3.addWidget(self.fahrenheit_ap_25)

        self.horizontalLayout_375.addWidget(self.stacked_cel_fah_press_c_3)

        self.horizontalLayout_375.setStretch(0, 3)
        self.horizontalLayout_375.setStretch(1, 1)

        self.verticalLayout_46.addWidget(self.widget_296)

        self.widget_297 = QWidget(self.widget_60)
        self.widget_297.setObjectName(u"widget_297")
        self.horizontalLayout_377 = QHBoxLayout(self.widget_297)
        self.horizontalLayout_377.setSpacing(7)
        self.horizontalLayout_377.setObjectName(u"horizontalLayout_377")
        self.horizontalLayout_377.setContentsMargins(0, 0, 0, 0)
        self.widget_199 = QWidget(self.widget_297)
        self.widget_199.setObjectName(u"widget_199")
        self.widget_199.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_378 = QHBoxLayout(self.widget_199)
        self.horizontalLayout_378.setObjectName(u"horizontalLayout_378")
        self.horizontalLayout_378.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_4 = QDoubleSpinBox(self.widget_199)
        self.pressure_pv_c_4.setObjectName(u"pressure_pv_c_4")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_4.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_4.setSizePolicy(sizePolicy)
        self.pressure_pv_c_4.setFont(font15)
        self.pressure_pv_c_4.setStyleSheet(u"")
        self.pressure_pv_c_4.setWrapping(True)
        self.pressure_pv_c_4.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_4.setReadOnly(True)
        self.pressure_pv_c_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_4.setDecimals(1)
        self.pressure_pv_c_4.setMaximum(999.000000000000000)
        self.pressure_pv_c_4.setValue(0.000000000000000)

        self.horizontalLayout_378.addWidget(self.pressure_pv_c_4)

        self.line_24 = QFrame(self.widget_199)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setStyleSheet(u"border: 2px solid #6F00FF;")
        self.line_24.setFrameShape(QFrame.Shape.VLine)
        self.line_24.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_378.addWidget(self.line_24)

        self.pressure_sv_c_4 = QDoubleSpinBox(self.widget_199)
        self.pressure_sv_c_4.setObjectName(u"pressure_sv_c_4")
        sizePolicy.setHeightForWidth(self.pressure_sv_c_4.sizePolicy().hasHeightForWidth())
        self.pressure_sv_c_4.setSizePolicy(sizePolicy)
        self.pressure_sv_c_4.setFont(font15)
        self.pressure_sv_c_4.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_c_4.setWrapping(False)
        self.pressure_sv_c_4.setAlignment(Qt.AlignCenter)
        self.pressure_sv_c_4.setReadOnly(False)
        self.pressure_sv_c_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_c_4.setDecimals(1)
        self.pressure_sv_c_4.setMaximum(999.000000000000000)
        self.pressure_sv_c_4.setValue(0.000000000000000)

        self.horizontalLayout_378.addWidget(self.pressure_sv_c_4)

        self.horizontalLayout_378.setStretch(0, 1)
        self.horizontalLayout_378.setStretch(2, 1)

        self.horizontalLayout_377.addWidget(self.widget_199)

        self.stacked_cel_fah_press_c_4 = QStackedWidget(self.widget_297)
        self.stacked_cel_fah_press_c_4.setObjectName(u"stacked_cel_fah_press_c_4")
        self.celsius_ap_26 = QWidget()
        self.celsius_ap_26.setObjectName(u"celsius_ap_26")
        self.horizontalLayout_467 = QHBoxLayout(self.celsius_ap_26)
        self.horizontalLayout_467.setObjectName(u"horizontalLayout_467")
        self.horizontalLayout_467.setContentsMargins(0, 0, 0, 0)
        self.label_377 = QLabel(self.celsius_ap_26)
        self.label_377.setObjectName(u"label_377")
        self.label_377.setFont(font16)
        self.label_377.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_377.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_467.addWidget(self.label_377)

        self.stacked_cel_fah_press_c_4.addWidget(self.celsius_ap_26)
        self.fahrenheit_ap_26 = QWidget()
        self.fahrenheit_ap_26.setObjectName(u"fahrenheit_ap_26")
        self.horizontalLayout_468 = QHBoxLayout(self.fahrenheit_ap_26)
        self.horizontalLayout_468.setObjectName(u"horizontalLayout_468")
        self.horizontalLayout_468.setContentsMargins(0, 0, 0, 0)
        self.label_378 = QLabel(self.fahrenheit_ap_26)
        self.label_378.setObjectName(u"label_378")
        self.label_378.setFont(font16)
        self.label_378.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_378.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_468.addWidget(self.label_378)

        self.stacked_cel_fah_press_c_4.addWidget(self.fahrenheit_ap_26)

        self.horizontalLayout_377.addWidget(self.stacked_cel_fah_press_c_4)

        self.horizontalLayout_377.setStretch(0, 3)
        self.horizontalLayout_377.setStretch(1, 1)

        self.verticalLayout_46.addWidget(self.widget_297)

        self.widget_298 = QWidget(self.widget_60)
        self.widget_298.setObjectName(u"widget_298")
        self.horizontalLayout_379 = QHBoxLayout(self.widget_298)
        self.horizontalLayout_379.setObjectName(u"horizontalLayout_379")
        self.horizontalLayout_379.setContentsMargins(0, 0, 0, 0)
        self.widget_200 = QWidget(self.widget_298)
        self.widget_200.setObjectName(u"widget_200")
        self.widget_200.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_380 = QHBoxLayout(self.widget_200)
        self.horizontalLayout_380.setObjectName(u"horizontalLayout_380")
        self.horizontalLayout_380.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_5 = QDoubleSpinBox(self.widget_200)
        self.pressure_pv_c_5.setObjectName(u"pressure_pv_c_5")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_5.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_5.setSizePolicy(sizePolicy)
        self.pressure_pv_c_5.setFont(font15)
        self.pressure_pv_c_5.setStyleSheet(u"")
        self.pressure_pv_c_5.setWrapping(True)
        self.pressure_pv_c_5.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_5.setReadOnly(True)
        self.pressure_pv_c_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_5.setDecimals(1)
        self.pressure_pv_c_5.setMaximum(999.000000000000000)
        self.pressure_pv_c_5.setValue(0.000000000000000)

        self.horizontalLayout_380.addWidget(self.pressure_pv_c_5)

        self.line_25 = QFrame(self.widget_200)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setStyleSheet(u"border: 2px solid #6F00FF;")
        self.line_25.setFrameShape(QFrame.Shape.VLine)
        self.line_25.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_380.addWidget(self.line_25)

        self.pressure_sv_c_5 = QDoubleSpinBox(self.widget_200)
        self.pressure_sv_c_5.setObjectName(u"pressure_sv_c_5")
        sizePolicy.setHeightForWidth(self.pressure_sv_c_5.sizePolicy().hasHeightForWidth())
        self.pressure_sv_c_5.setSizePolicy(sizePolicy)
        self.pressure_sv_c_5.setFont(font15)
        self.pressure_sv_c_5.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_c_5.setWrapping(False)
        self.pressure_sv_c_5.setAlignment(Qt.AlignCenter)
        self.pressure_sv_c_5.setReadOnly(False)
        self.pressure_sv_c_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_c_5.setDecimals(1)
        self.pressure_sv_c_5.setMaximum(999.000000000000000)
        self.pressure_sv_c_5.setValue(0.000000000000000)

        self.horizontalLayout_380.addWidget(self.pressure_sv_c_5)

        self.horizontalLayout_380.setStretch(0, 1)
        self.horizontalLayout_380.setStretch(2, 1)

        self.horizontalLayout_379.addWidget(self.widget_200)

        self.label_206 = QLabel(self.widget_298)
        self.label_206.setObjectName(u"label_206")
        self.label_206.setFont(font16)
        self.label_206.setAlignment(Qt.AlignCenter)
        self.label_206.setWordWrap(True)

        self.horizontalLayout_379.addWidget(self.label_206)

        self.horizontalLayout_379.setStretch(0, 3)
        self.horizontalLayout_379.setStretch(1, 1)

        self.verticalLayout_46.addWidget(self.widget_298)

        self.widget_299 = QWidget(self.widget_60)
        self.widget_299.setObjectName(u"widget_299")
        self.horizontalLayout_381 = QHBoxLayout(self.widget_299)
        self.horizontalLayout_381.setObjectName(u"horizontalLayout_381")
        self.horizontalLayout_381.setContentsMargins(0, 0, 0, 0)
        self.widget_201 = QWidget(self.widget_299)
        self.widget_201.setObjectName(u"widget_201")
        self.widget_201.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_382 = QHBoxLayout(self.widget_201)
        self.horizontalLayout_382.setObjectName(u"horizontalLayout_382")
        self.horizontalLayout_382.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_6 = QDoubleSpinBox(self.widget_201)
        self.pressure_pv_c_6.setObjectName(u"pressure_pv_c_6")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_6.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_6.setSizePolicy(sizePolicy)
        self.pressure_pv_c_6.setFont(font15)
        self.pressure_pv_c_6.setStyleSheet(u"")
        self.pressure_pv_c_6.setWrapping(True)
        self.pressure_pv_c_6.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_6.setReadOnly(True)
        self.pressure_pv_c_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_6.setDecimals(1)
        self.pressure_pv_c_6.setMaximum(999.000000000000000)
        self.pressure_pv_c_6.setValue(0.000000000000000)

        self.horizontalLayout_382.addWidget(self.pressure_pv_c_6)

        self.line_26 = QFrame(self.widget_201)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setStyleSheet(u"border: 2px solid #6F00FF;")
        self.line_26.setFrameShape(QFrame.Shape.VLine)
        self.line_26.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_382.addWidget(self.line_26)

        self.pressure_sv_c_6 = QDoubleSpinBox(self.widget_201)
        self.pressure_sv_c_6.setObjectName(u"pressure_sv_c_6")
        sizePolicy.setHeightForWidth(self.pressure_sv_c_6.sizePolicy().hasHeightForWidth())
        self.pressure_sv_c_6.setSizePolicy(sizePolicy)
        self.pressure_sv_c_6.setFont(font15)
        self.pressure_sv_c_6.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_c_6.setWrapping(False)
        self.pressure_sv_c_6.setAlignment(Qt.AlignCenter)
        self.pressure_sv_c_6.setReadOnly(False)
        self.pressure_sv_c_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_c_6.setDecimals(1)
        self.pressure_sv_c_6.setMaximum(999.000000000000000)
        self.pressure_sv_c_6.setValue(0.000000000000000)

        self.horizontalLayout_382.addWidget(self.pressure_sv_c_6)

        self.horizontalLayout_382.setStretch(0, 1)
        self.horizontalLayout_382.setStretch(2, 1)

        self.horizontalLayout_381.addWidget(self.widget_201)

        self.label_221 = QLabel(self.widget_299)
        self.label_221.setObjectName(u"label_221")
        self.label_221.setFont(font16)
        self.label_221.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_381.addWidget(self.label_221)

        self.horizontalLayout_381.setStretch(0, 3)
        self.horizontalLayout_381.setStretch(1, 1)

        self.verticalLayout_46.addWidget(self.widget_299)

        self.widget_300 = QWidget(self.widget_60)
        self.widget_300.setObjectName(u"widget_300")
        self.horizontalLayout_383 = QHBoxLayout(self.widget_300)
        self.horizontalLayout_383.setObjectName(u"horizontalLayout_383")
        self.horizontalLayout_383.setContentsMargins(0, 0, 0, 0)
        self.widget_203 = QWidget(self.widget_300)
        self.widget_203.setObjectName(u"widget_203")
        self.widget_203.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_384 = QHBoxLayout(self.widget_203)
        self.horizontalLayout_384.setObjectName(u"horizontalLayout_384")
        self.horizontalLayout_384.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_7 = QDoubleSpinBox(self.widget_203)
        self.pressure_pv_c_7.setObjectName(u"pressure_pv_c_7")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_7.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_7.setSizePolicy(sizePolicy)
        self.pressure_pv_c_7.setFont(font15)
        self.pressure_pv_c_7.setStyleSheet(u"")
        self.pressure_pv_c_7.setWrapping(True)
        self.pressure_pv_c_7.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_7.setReadOnly(True)
        self.pressure_pv_c_7.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_7.setDecimals(1)
        self.pressure_pv_c_7.setMaximum(999.000000000000000)
        self.pressure_pv_c_7.setValue(0.000000000000000)

        self.horizontalLayout_384.addWidget(self.pressure_pv_c_7)

        self.line_27 = QFrame(self.widget_203)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setStyleSheet(u"border: 2px solid #6F00FF;")
        self.line_27.setFrameShape(QFrame.Shape.VLine)
        self.line_27.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_384.addWidget(self.line_27)

        self.pressure_sv_c_7 = QDoubleSpinBox(self.widget_203)
        self.pressure_sv_c_7.setObjectName(u"pressure_sv_c_7")
        sizePolicy.setHeightForWidth(self.pressure_sv_c_7.sizePolicy().hasHeightForWidth())
        self.pressure_sv_c_7.setSizePolicy(sizePolicy)
        self.pressure_sv_c_7.setFont(font15)
        self.pressure_sv_c_7.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_c_7.setWrapping(False)
        self.pressure_sv_c_7.setAlignment(Qt.AlignCenter)
        self.pressure_sv_c_7.setReadOnly(False)
        self.pressure_sv_c_7.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_c_7.setDecimals(1)
        self.pressure_sv_c_7.setMaximum(999.000000000000000)
        self.pressure_sv_c_7.setValue(0.000000000000000)

        self.horizontalLayout_384.addWidget(self.pressure_sv_c_7)

        self.horizontalLayout_384.setStretch(0, 1)
        self.horizontalLayout_384.setStretch(2, 1)

        self.horizontalLayout_383.addWidget(self.widget_203)

        self.label_224 = QLabel(self.widget_300)
        self.label_224.setObjectName(u"label_224")
        self.label_224.setFont(font16)
        self.label_224.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_383.addWidget(self.label_224)

        self.horizontalLayout_383.setStretch(0, 3)
        self.horizontalLayout_383.setStretch(1, 1)

        self.verticalLayout_46.addWidget(self.widget_300)

        self.widget_301 = QWidget(self.widget_60)
        self.widget_301.setObjectName(u"widget_301")
        self.horizontalLayout_385 = QHBoxLayout(self.widget_301)
        self.horizontalLayout_385.setObjectName(u"horizontalLayout_385")
        self.horizontalLayout_385.setContentsMargins(0, 0, 0, 0)
        self.widget_204 = QWidget(self.widget_301)
        self.widget_204.setObjectName(u"widget_204")
        self.widget_204.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_386 = QHBoxLayout(self.widget_204)
        self.horizontalLayout_386.setObjectName(u"horizontalLayout_386")
        self.horizontalLayout_386.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_8 = QDoubleSpinBox(self.widget_204)
        self.pressure_pv_c_8.setObjectName(u"pressure_pv_c_8")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_8.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_8.setSizePolicy(sizePolicy)
        self.pressure_pv_c_8.setFont(font15)
        self.pressure_pv_c_8.setStyleSheet(u"")
        self.pressure_pv_c_8.setWrapping(True)
        self.pressure_pv_c_8.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_8.setReadOnly(True)
        self.pressure_pv_c_8.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_8.setDecimals(1)
        self.pressure_pv_c_8.setMaximum(999.000000000000000)
        self.pressure_pv_c_8.setValue(0.000000000000000)

        self.horizontalLayout_386.addWidget(self.pressure_pv_c_8)

        self.line_28 = QFrame(self.widget_204)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setStyleSheet(u"border: 2px solid #6F00FF;")
        self.line_28.setFrameShape(QFrame.Shape.VLine)
        self.line_28.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_386.addWidget(self.line_28)

        self.pressure_sv_c_8 = QDoubleSpinBox(self.widget_204)
        self.pressure_sv_c_8.setObjectName(u"pressure_sv_c_8")
        sizePolicy.setHeightForWidth(self.pressure_sv_c_8.sizePolicy().hasHeightForWidth())
        self.pressure_sv_c_8.setSizePolicy(sizePolicy)
        self.pressure_sv_c_8.setFont(font15)
        self.pressure_sv_c_8.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_c_8.setWrapping(False)
        self.pressure_sv_c_8.setAlignment(Qt.AlignCenter)
        self.pressure_sv_c_8.setReadOnly(False)
        self.pressure_sv_c_8.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_c_8.setDecimals(1)
        self.pressure_sv_c_8.setMaximum(999.000000000000000)
        self.pressure_sv_c_8.setValue(0.000000000000000)

        self.horizontalLayout_386.addWidget(self.pressure_sv_c_8)

        self.horizontalLayout_386.setStretch(0, 1)
        self.horizontalLayout_386.setStretch(2, 1)

        self.horizontalLayout_385.addWidget(self.widget_204)

        self.label_225 = QLabel(self.widget_301)
        self.label_225.setObjectName(u"label_225")
        self.label_225.setFont(font16)
        self.label_225.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_385.addWidget(self.label_225)

        self.horizontalLayout_385.setStretch(0, 3)
        self.horizontalLayout_385.setStretch(1, 1)

        self.verticalLayout_46.addWidget(self.widget_301)

        self.widget_302 = QWidget(self.widget_60)
        self.widget_302.setObjectName(u"widget_302")
        self.horizontalLayout_387 = QHBoxLayout(self.widget_302)
        self.horizontalLayout_387.setObjectName(u"horizontalLayout_387")
        self.horizontalLayout_387.setContentsMargins(0, 0, 0, 0)
        self.widget_205 = QWidget(self.widget_302)
        self.widget_205.setObjectName(u"widget_205")
        self.widget_205.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_388 = QHBoxLayout(self.widget_205)
        self.horizontalLayout_388.setObjectName(u"horizontalLayout_388")
        self.horizontalLayout_388.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_9 = QDoubleSpinBox(self.widget_205)
        self.pressure_pv_c_9.setObjectName(u"pressure_pv_c_9")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_9.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_9.setSizePolicy(sizePolicy)
        self.pressure_pv_c_9.setFont(font15)
        self.pressure_pv_c_9.setStyleSheet(u"")
        self.pressure_pv_c_9.setWrapping(True)
        self.pressure_pv_c_9.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_9.setReadOnly(True)
        self.pressure_pv_c_9.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_9.setDecimals(1)
        self.pressure_pv_c_9.setMaximum(999.000000000000000)
        self.pressure_pv_c_9.setValue(0.000000000000000)

        self.horizontalLayout_388.addWidget(self.pressure_pv_c_9)

        self.line_29 = QFrame(self.widget_205)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setStyleSheet(u"border: 2px solid #6F00FF;")
        self.line_29.setFrameShape(QFrame.Shape.VLine)
        self.line_29.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_388.addWidget(self.line_29)

        self.pressure_sv_c_9 = QDoubleSpinBox(self.widget_205)
        self.pressure_sv_c_9.setObjectName(u"pressure_sv_c_9")
        sizePolicy.setHeightForWidth(self.pressure_sv_c_9.sizePolicy().hasHeightForWidth())
        self.pressure_sv_c_9.setSizePolicy(sizePolicy)
        self.pressure_sv_c_9.setFont(font15)
        self.pressure_sv_c_9.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_c_9.setWrapping(False)
        self.pressure_sv_c_9.setAlignment(Qt.AlignCenter)
        self.pressure_sv_c_9.setReadOnly(False)
        self.pressure_sv_c_9.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_c_9.setDecimals(1)
        self.pressure_sv_c_9.setMaximum(999.000000000000000)
        self.pressure_sv_c_9.setValue(0.000000000000000)

        self.horizontalLayout_388.addWidget(self.pressure_sv_c_9)

        self.horizontalLayout_388.setStretch(0, 1)
        self.horizontalLayout_388.setStretch(2, 1)

        self.horizontalLayout_387.addWidget(self.widget_205)

        self.label_226 = QLabel(self.widget_302)
        self.label_226.setObjectName(u"label_226")
        self.label_226.setFont(font16)
        self.label_226.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_387.addWidget(self.label_226)

        self.horizontalLayout_387.setStretch(0, 3)
        self.horizontalLayout_387.setStretch(1, 1)

        self.verticalLayout_46.addWidget(self.widget_302)

        self.widget_303 = QWidget(self.widget_60)
        self.widget_303.setObjectName(u"widget_303")
        self.horizontalLayout_389 = QHBoxLayout(self.widget_303)
        self.horizontalLayout_389.setObjectName(u"horizontalLayout_389")
        self.horizontalLayout_389.setContentsMargins(0, 0, 0, 0)
        self.widget_206 = QWidget(self.widget_303)
        self.widget_206.setObjectName(u"widget_206")
        self.widget_206.setStyleSheet(u"QWidget{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QDoubleSpinBox\n"
"{\n"
"    border: none;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: none;\n"
"}")
        self.horizontalLayout_469 = QHBoxLayout(self.widget_206)
        self.horizontalLayout_469.setObjectName(u"horizontalLayout_469")
        self.horizontalLayout_469.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_c_10 = QDoubleSpinBox(self.widget_206)
        self.pressure_pv_c_10.setObjectName(u"pressure_pv_c_10")
        sizePolicy.setHeightForWidth(self.pressure_pv_c_10.sizePolicy().hasHeightForWidth())
        self.pressure_pv_c_10.setSizePolicy(sizePolicy)
        self.pressure_pv_c_10.setFont(font15)
        self.pressure_pv_c_10.setStyleSheet(u"")
        self.pressure_pv_c_10.setWrapping(True)
        self.pressure_pv_c_10.setAlignment(Qt.AlignCenter)
        self.pressure_pv_c_10.setReadOnly(True)
        self.pressure_pv_c_10.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_c_10.setDecimals(1)
        self.pressure_pv_c_10.setMaximum(999.000000000000000)
        self.pressure_pv_c_10.setValue(0.000000000000000)

        self.horizontalLayout_469.addWidget(self.pressure_pv_c_10)

        self.line_30 = QFrame(self.widget_206)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setStyleSheet(u"border: 2px solid #6F00FF;")
        self.line_30.setFrameShape(QFrame.Shape.VLine)
        self.line_30.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_469.addWidget(self.line_30)

        self.pressure_sv_c_10 = QDoubleSpinBox(self.widget_206)
        self.pressure_sv_c_10.setObjectName(u"pressure_sv_c_10")
        sizePolicy.setHeightForWidth(self.pressure_sv_c_10.sizePolicy().hasHeightForWidth())
        self.pressure_sv_c_10.setSizePolicy(sizePolicy)
        self.pressure_sv_c_10.setFont(font15)
        self.pressure_sv_c_10.setStyleSheet(u"QDoubleSpinBox:hover{\n"
"    border: 3px solid #43A047;\n"
"}")
        self.pressure_sv_c_10.setWrapping(False)
        self.pressure_sv_c_10.setAlignment(Qt.AlignCenter)
        self.pressure_sv_c_10.setReadOnly(False)
        self.pressure_sv_c_10.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_c_10.setDecimals(1)
        self.pressure_sv_c_10.setMaximum(999.000000000000000)
        self.pressure_sv_c_10.setValue(0.000000000000000)

        self.horizontalLayout_469.addWidget(self.pressure_sv_c_10)

        self.horizontalLayout_469.setStretch(0, 1)
        self.horizontalLayout_469.setStretch(2, 1)

        self.horizontalLayout_389.addWidget(self.widget_206)

        self.label_227 = QLabel(self.widget_303)
        self.label_227.setObjectName(u"label_227")
        self.label_227.setFont(font16)
        self.label_227.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_389.addWidget(self.label_227)

        self.horizontalLayout_389.setStretch(0, 3)
        self.horizontalLayout_389.setStretch(1, 1)

        self.verticalLayout_46.addWidget(self.widget_303)

        self.verticalLayout_46.setStretch(0, 1)
        self.verticalLayout_46.setStretch(1, 1)
        self.verticalLayout_46.setStretch(2, 1)
        self.verticalLayout_46.setStretch(3, 1)
        self.verticalLayout_46.setStretch(4, 1)
        self.verticalLayout_46.setStretch(5, 1)
        self.verticalLayout_46.setStretch(6, 1)
        self.verticalLayout_46.setStretch(7, 1)
        self.verticalLayout_46.setStretch(8, 1)
        self.verticalLayout_46.setStretch(9, 1)

        self.verticalLayout_31.addWidget(self.widget_60)


        self.horizontalLayout_7.addWidget(self.press_c_widget)

        self.horizontalLayout_7.setStretch(2, 1)
        self.horizontalLayout_7.setStretch(4, 1)
        self.horizontalLayout_7.setStretch(6, 1)

        self.verticalLayout_63.addWidget(self.widget_6)


        self.verticalLayout_10.addWidget(self.widget_pressure_time)

        self.widget_group_btn = QWidget(self.stacked_pressure_page)
        self.widget_group_btn.setObjectName(u"widget_group_btn")
        self.verticalLayout_7 = QVBoxLayout(self.widget_group_btn)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_group_btn_1 = QWidget(self.widget_group_btn)
        self.widget_group_btn_1.setObjectName(u"widget_group_btn_1")
        self.widget_group_btn_1.setMaximumSize(QSize(16777215, 100))
        self.widget_group_btn_1.setFont(font)
        self.widget_group_btn_1.setStyleSheet(u"QPushButton {\n"
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
        self.horizontalLayout_26 = QHBoxLayout(self.widget_group_btn_1)
        self.horizontalLayout_26.setSpacing(10)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_group_btn_1)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 5, 0)
        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.widget_2)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setStyleSheet(u"QSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget\n"
"{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.cycle_a_displ = QSpinBox(self.widget_11)
        self.cycle_a_displ.setObjectName(u"cycle_a_displ")
        sizePolicy.setHeightForWidth(self.cycle_a_displ.sizePolicy().hasHeightForWidth())
        self.cycle_a_displ.setSizePolicy(sizePolicy)
        font17 = QFont()
        font17.setFamilies([u"Segoe UI"])
        font17.setPointSize(18)
        font17.setBold(True)
        font17.setItalic(False)
        self.cycle_a_displ.setFont(font17)
        self.cycle_a_displ.setStyleSheet(u"color: rgb(30, 136, 229);\n"
"padding-left: 10px;")
        self.cycle_a_displ.setWrapping(True)
        self.cycle_a_displ.setAlignment(Qt.AlignCenter)
        self.cycle_a_displ.setReadOnly(True)
        self.cycle_a_displ.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.cycle_a_displ.setMaximum(999999)
        self.cycle_a_displ.setValue(999999)

        self.horizontalLayout_12.addWidget(self.cycle_a_displ)


        self.horizontalLayout_3.addWidget(self.widget_11)

        self.reset_cycle_a_btn = QPushButton(self.widget_2)
        self.reset_cycle_a_btn.setObjectName(u"reset_cycle_a_btn")
        sizePolicy.setHeightForWidth(self.reset_cycle_a_btn.sizePolicy().hasHeightForWidth())
        self.reset_cycle_a_btn.setSizePolicy(sizePolicy)
        self.reset_cycle_a_btn.setFont(font9)
        self.reset_cycle_a_btn.setStyleSheet(u"QPushButton {\n"
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
        icon12 = QIcon()
        icon12.addFile(u":/newPrefix/broom.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.reset_cycle_a_btn.setIcon(icon12)
        self.reset_cycle_a_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_3.addWidget(self.reset_cycle_a_btn)


        self.horizontalLayout_4.addWidget(self.widget_2)

        self.heat_btn_a = QPushButton(self.widget_3)
        self.heat_btn_a.setObjectName(u"heat_btn_a")
        sizePolicy.setHeightForWidth(self.heat_btn_a.sizePolicy().hasHeightForWidth())
        self.heat_btn_a.setSizePolicy(sizePolicy)
        self.heat_btn_a.setMaximumSize(QSize(16777215, 150))
        self.heat_btn_a.setFont(font9)
        self.heat_btn_a.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u":/newPrefix/heat.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.heat_btn_a.setIcon(icon13)
        self.heat_btn_a.setIconSize(QSize(25, 25))
        self.heat_btn_a.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.heat_btn_a)

        self.heat_btn_b = QPushButton(self.widget_3)
        self.heat_btn_b.setObjectName(u"heat_btn_b")
        sizePolicy.setHeightForWidth(self.heat_btn_b.sizePolicy().hasHeightForWidth())
        self.heat_btn_b.setSizePolicy(sizePolicy)
        self.heat_btn_b.setMaximumSize(QSize(16777215, 150))
        self.heat_btn_b.setFont(font9)
        self.heat_btn_b.setStyleSheet(u"")
        self.heat_btn_b.setIcon(icon13)
        self.heat_btn_b.setIconSize(QSize(25, 25))
        self.heat_btn_b.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.heat_btn_b)

        self.heat_btn_c = QPushButton(self.widget_3)
        self.heat_btn_c.setObjectName(u"heat_btn_c")
        sizePolicy.setHeightForWidth(self.heat_btn_c.sizePolicy().hasHeightForWidth())
        self.heat_btn_c.setSizePolicy(sizePolicy)
        self.heat_btn_c.setMaximumSize(QSize(16777215, 150))
        self.heat_btn_c.setFont(font9)
        self.heat_btn_c.setStyleSheet(u"")
        self.heat_btn_c.setIcon(icon13)
        self.heat_btn_c.setIconSize(QSize(25, 25))
        self.heat_btn_c.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.heat_btn_c)


        self.horizontalLayout_26.addWidget(self.widget_3)

        self.horizontalLayout_26.setStretch(0, 3)

        self.verticalLayout_7.addWidget(self.widget_group_btn_1)

        self.widget_group_btn_3 = QWidget(self.widget_group_btn)
        self.widget_group_btn_3.setObjectName(u"widget_group_btn_3")
        self.widget_group_btn_3.setMaximumSize(QSize(16777215, 100))
        self.widget_group_btn_3.setFont(font)
        self.widget_group_btn_3.setStyleSheet(u"QPushButton {\n"
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
        self.horizontalLayout_21 = QHBoxLayout(self.widget_group_btn_3)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_group_btn_3)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 0, 5, 0)
        self.widget_10 = QWidget(self.widget_5)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.widget_10)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setStyleSheet(u"QSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget\n"
"{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.cycle_b_displ = QSpinBox(self.widget_12)
        self.cycle_b_displ.setObjectName(u"cycle_b_displ")
        sizePolicy.setHeightForWidth(self.cycle_b_displ.sizePolicy().hasHeightForWidth())
        self.cycle_b_displ.setSizePolicy(sizePolicy)
        self.cycle_b_displ.setFont(font17)
        self.cycle_b_displ.setStyleSheet(u"color: rgb(251, 140, 0);\n"
"padding-left: 10px;")
        self.cycle_b_displ.setWrapping(True)
        self.cycle_b_displ.setAlignment(Qt.AlignCenter)
        self.cycle_b_displ.setReadOnly(True)
        self.cycle_b_displ.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.cycle_b_displ.setMaximum(999999)
        self.cycle_b_displ.setValue(999999)
        self.cycle_b_displ.setDisplayIntegerBase(10)

        self.horizontalLayout_13.addWidget(self.cycle_b_displ)


        self.horizontalLayout_10.addWidget(self.widget_12)

        self.reset_cycle_b_btn = QPushButton(self.widget_10)
        self.reset_cycle_b_btn.setObjectName(u"reset_cycle_b_btn")
        sizePolicy.setHeightForWidth(self.reset_cycle_b_btn.sizePolicy().hasHeightForWidth())
        self.reset_cycle_b_btn.setSizePolicy(sizePolicy)
        self.reset_cycle_b_btn.setFont(font9)
        self.reset_cycle_b_btn.setStyleSheet(u"QPushButton {\n"
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
        self.reset_cycle_b_btn.setIcon(icon12)
        self.reset_cycle_b_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_10.addWidget(self.reset_cycle_b_btn)


        self.horizontalLayout_5.addWidget(self.widget_10)

        self.vacuum_btn_b = QPushButton(self.widget_5)
        self.vacuum_btn_b.setObjectName(u"vacuum_btn_b")
        sizePolicy.setHeightForWidth(self.vacuum_btn_b.sizePolicy().hasHeightForWidth())
        self.vacuum_btn_b.setSizePolicy(sizePolicy)
        self.vacuum_btn_b.setMaximumSize(QSize(16777215, 150))
        self.vacuum_btn_b.setFont(font9)
        self.vacuum_btn_b.setStyleSheet(u"")
        icon14 = QIcon()
        icon14.addFile(u":/newPrefix/pump.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.vacuum_btn_b.setIcon(icon14)
        self.vacuum_btn_b.setIconSize(QSize(25, 25))
        self.vacuum_btn_b.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.vacuum_btn_b)

        self.vacuum_btn_a = QPushButton(self.widget_5)
        self.vacuum_btn_a.setObjectName(u"vacuum_btn_a")
        sizePolicy.setHeightForWidth(self.vacuum_btn_a.sizePolicy().hasHeightForWidth())
        self.vacuum_btn_a.setSizePolicy(sizePolicy)
        self.vacuum_btn_a.setMaximumSize(QSize(16777215, 150))
        self.vacuum_btn_a.setFont(font9)
        self.vacuum_btn_a.setStyleSheet(u"")
        self.vacuum_btn_a.setIcon(icon14)
        self.vacuum_btn_a.setIconSize(QSize(25, 25))
        self.vacuum_btn_a.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.vacuum_btn_a)

        self.vacuum_btn_c = QPushButton(self.widget_5)
        self.vacuum_btn_c.setObjectName(u"vacuum_btn_c")
        sizePolicy.setHeightForWidth(self.vacuum_btn_c.sizePolicy().hasHeightForWidth())
        self.vacuum_btn_c.setSizePolicy(sizePolicy)
        self.vacuum_btn_c.setMaximumSize(QSize(16777215, 150))
        self.vacuum_btn_c.setFont(font9)
        self.vacuum_btn_c.setStyleSheet(u"")
        self.vacuum_btn_c.setIcon(icon14)
        self.vacuum_btn_c.setIconSize(QSize(25, 25))
        self.vacuum_btn_c.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.vacuum_btn_c)


        self.horizontalLayout_21.addWidget(self.widget_5)


        self.verticalLayout_7.addWidget(self.widget_group_btn_3)

        self.widget_group_btn_2 = QWidget(self.widget_group_btn)
        self.widget_group_btn_2.setObjectName(u"widget_group_btn_2")
        self.widget_group_btn_2.setMaximumSize(QSize(16777215, 100))
        self.widget_group_btn_2.setFont(font)
        self.widget_group_btn_2.setStyleSheet(u"QPushButton {\n"
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
        self.horizontalLayout_25 = QHBoxLayout(self.widget_group_btn_2)
        self.horizontalLayout_25.setSpacing(10)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_group_btn_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 5, 0)
        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.widget_8)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setStyleSheet(u"QSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QWidget\n"
"{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.cycle_c_displ = QSpinBox(self.widget_13)
        self.cycle_c_displ.setObjectName(u"cycle_c_displ")
        sizePolicy.setHeightForWidth(self.cycle_c_displ.sizePolicy().hasHeightForWidth())
        self.cycle_c_displ.setSizePolicy(sizePolicy)
        self.cycle_c_displ.setFont(font17)
        self.cycle_c_displ.setStyleSheet(u"color: #6F00FF;\n"
"padding-left: 10px;")
        self.cycle_c_displ.setWrapping(True)
        self.cycle_c_displ.setAlignment(Qt.AlignCenter)
        self.cycle_c_displ.setReadOnly(True)
        self.cycle_c_displ.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.cycle_c_displ.setMaximum(999999)
        self.cycle_c_displ.setValue(999999)
        self.cycle_c_displ.setDisplayIntegerBase(10)

        self.horizontalLayout_11.addWidget(self.cycle_c_displ)


        self.horizontalLayout_8.addWidget(self.widget_13)

        self.reset_cycle_c_btn = QPushButton(self.widget_8)
        self.reset_cycle_c_btn.setObjectName(u"reset_cycle_c_btn")
        sizePolicy.setHeightForWidth(self.reset_cycle_c_btn.sizePolicy().hasHeightForWidth())
        self.reset_cycle_c_btn.setSizePolicy(sizePolicy)
        self.reset_cycle_c_btn.setFont(font9)
        self.reset_cycle_c_btn.setStyleSheet(u"QPushButton {\n"
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
        self.reset_cycle_c_btn.setIcon(icon12)
        self.reset_cycle_c_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_8.addWidget(self.reset_cycle_c_btn)


        self.horizontalLayout_6.addWidget(self.widget_8)

        self.refuel_btn_a = QPushButton(self.widget_4)
        self.refuel_btn_a.setObjectName(u"refuel_btn_a")
        sizePolicy.setHeightForWidth(self.refuel_btn_a.sizePolicy().hasHeightForWidth())
        self.refuel_btn_a.setSizePolicy(sizePolicy)
        self.refuel_btn_a.setMaximumSize(QSize(16777215, 150))
        self.refuel_btn_a.setFont(font9)
        self.refuel_btn_a.setStyleSheet(u"")
        icon15 = QIcon()
        icon15.addFile(u":/newPrefix/gas-pump-alt.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refuel_btn_a.setIcon(icon15)
        self.refuel_btn_a.setIconSize(QSize(25, 25))
        self.refuel_btn_a.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.refuel_btn_a)

        self.refuel_btn_b = QPushButton(self.widget_4)
        self.refuel_btn_b.setObjectName(u"refuel_btn_b")
        sizePolicy.setHeightForWidth(self.refuel_btn_b.sizePolicy().hasHeightForWidth())
        self.refuel_btn_b.setSizePolicy(sizePolicy)
        self.refuel_btn_b.setMaximumSize(QSize(16777215, 150))
        self.refuel_btn_b.setFont(font9)
        self.refuel_btn_b.setStyleSheet(u"")
        self.refuel_btn_b.setIcon(icon15)
        self.refuel_btn_b.setIconSize(QSize(25, 25))
        self.refuel_btn_b.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.refuel_btn_b)

        self.refuel_btn_c = QPushButton(self.widget_4)
        self.refuel_btn_c.setObjectName(u"refuel_btn_c")
        sizePolicy.setHeightForWidth(self.refuel_btn_c.sizePolicy().hasHeightForWidth())
        self.refuel_btn_c.setSizePolicy(sizePolicy)
        self.refuel_btn_c.setMaximumSize(QSize(16777215, 150))
        self.refuel_btn_c.setFont(font9)
        self.refuel_btn_c.setStyleSheet(u"")
        self.refuel_btn_c.setIcon(icon15)
        self.refuel_btn_c.setIconSize(QSize(25, 25))
        self.refuel_btn_c.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.refuel_btn_c)

        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 1)
        self.horizontalLayout_6.setStretch(3, 1)

        self.horizontalLayout_25.addWidget(self.widget_4)


        self.verticalLayout_7.addWidget(self.widget_group_btn_2)


        self.verticalLayout_10.addWidget(self.widget_group_btn)

        self.verticalLayout_10.setStretch(0, 6)

        self.verticalLayout_6.addWidget(self.stacked_pressure_page)

        self.stackedWidget.addWidget(self.pressure_page)
        self.temperature_page = QWidget()
        self.temperature_page.setObjectName(u"temperature_page")
        self.verticalLayout_8 = QVBoxLayout(self.temperature_page)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(3, 5, 0, 3)
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
        sizePolicy2.setHeightForWidth(self.widget_77.sizePolicy().hasHeightForWidth())
        self.widget_77.setSizePolicy(sizePolicy2)
        self.widget_77.setStyleSheet(u"QWidget {\n"
"    background-color: white;\n"
"    border-left: 4px solid #FB8C00;\n"
"    border-radius: 6px;\n"
"}")
        self.horizontalLayout_198 = QHBoxLayout(self.widget_77)
        self.horizontalLayout_198.setSpacing(5)
        self.horizontalLayout_198.setObjectName(u"horizontalLayout_198")
        self.horizontalLayout_198.setContentsMargins(5, 5, 15, 5)
        self.name_widget = QWidget(self.widget_77)
        self.name_widget.setObjectName(u"name_widget")
        self.name_widget.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}\n"
"QDoubleSpinBox\n"
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
        self.verticalLayout_64 = QVBoxLayout(self.name_widget)
        self.verticalLayout_64.setSpacing(10)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.label_118 = QLabel(self.name_widget)
        self.label_118.setObjectName(u"label_118")
        sizePolicy.setHeightForWidth(self.label_118.sizePolicy().hasHeightForWidth())
        self.label_118.setSizePolicy(sizePolicy)
        font18 = QFont()
        font18.setPointSize(22)
        font18.setBold(True)
        font18.setItalic(False)
        self.label_118.setFont(font18)
        self.label_118.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_118.setAlignment(Qt.AlignCenter)

        self.verticalLayout_64.addWidget(self.label_118)

        self.widget_16 = QWidget(self.name_widget)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.verticalLayout_16 = QVBoxLayout(self.widget_16)
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(5, 0, 5, 5)
        self.label_123 = QLabel(self.widget_16)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setFont(font16)
        self.label_123.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_123)

        self.label_124 = QLabel(self.widget_16)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setFont(font16)
        self.label_124.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_124)

        self.label_125 = QLabel(self.widget_16)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setFont(font16)
        self.label_125.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_125)

        self.label_126 = QLabel(self.widget_16)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setFont(font16)
        self.label_126.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_126)

        self.label_133 = QLabel(self.widget_16)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setFont(font16)
        self.label_133.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_133)

        self.label_132 = QLabel(self.widget_16)
        self.label_132.setObjectName(u"label_132")
        font19 = QFont()
        font19.setFamilies([u"Segoe UI"])
        font19.setPointSize(15)
        font19.setBold(True)
        font19.setItalic(False)
        self.label_132.setFont(font19)
        self.label_132.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_132)

        self.label_134 = QLabel(self.widget_16)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setFont(font19)
        self.label_134.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_134)


        self.verticalLayout_64.addWidget(self.widget_16)

        self.verticalLayout_64.setStretch(0, 1)
        self.verticalLayout_64.setStretch(1, 7)

        self.horizontalLayout_198.addWidget(self.name_widget)

        self.line_17 = QFrame(self.widget_77)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.Shape.VLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_198.addWidget(self.line_17)

        self.t0_widget = QWidget(self.widget_77)
        self.t0_widget.setObjectName(u"t0_widget")
        sizePolicy.setHeightForWidth(self.t0_widget.sizePolicy().hasHeightForWidth())
        self.t0_widget.setSizePolicy(sizePolicy)
        self.t0_widget.setStyleSheet(u"border-left: None;")
        self.verticalLayout_32 = QVBoxLayout(self.t0_widget)
        self.verticalLayout_32.setSpacing(10)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(5, 0, 5, 5)
        self.widget_71 = QWidget(self.t0_widget)
        self.widget_71.setObjectName(u"widget_71")
        self.horizontalLayout_65 = QHBoxLayout(self.widget_71)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_139 = QLabel(self.widget_71)
        self.label_139.setObjectName(u"label_139")
        sizePolicy.setHeightForWidth(self.label_139.sizePolicy().hasHeightForWidth())
        self.label_139.setSizePolicy(sizePolicy)
        self.label_139.setFont(font18)
        self.label_139.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_139.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.label_139)


        self.verticalLayout_32.addWidget(self.widget_71)

        self.widget_66 = QWidget(self.t0_widget)
        self.widget_66.setObjectName(u"widget_66")
        self.widget_66.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.verticalLayout_45 = QVBoxLayout(self.widget_66)
        self.verticalLayout_45.setSpacing(10)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.widget_185 = QWidget(self.widget_66)
        self.widget_185.setObjectName(u"widget_185")
        self.horizontalLayout_163 = QHBoxLayout(self.widget_185)
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.horizontalLayout_163.setContentsMargins(0, 0, 0, 0)
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
        self.label_249.setFont(font19)
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
        self.label_250.setFont(font19)
        self.label_250.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_250.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_457.addWidget(self.label_250)

        self.stacked_cel_fah_temp_t0_1.addWidget(self.fahrenheit_t0_1)

        self.horizontalLayout_163.addWidget(self.stacked_cel_fah_temp_t0_1)

        self.horizontalLayout_163.setStretch(0, 5)

        self.verticalLayout_45.addWidget(self.widget_185)

        self.widget_193 = QWidget(self.widget_66)
        self.widget_193.setObjectName(u"widget_193")
        self.horizontalLayout_182 = QHBoxLayout(self.widget_193)
        self.horizontalLayout_182.setObjectName(u"horizontalLayout_182")
        self.horizontalLayout_182.setContentsMargins(0, 0, 0, 0)
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
        self.label_251.setFont(font19)
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
        self.label_252.setFont(font19)
        self.label_252.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_252.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_459.addWidget(self.label_252)

        self.stacked_cel_fah_temp_t0_2.addWidget(self.fahrenheit_t0_2)

        self.horizontalLayout_182.addWidget(self.stacked_cel_fah_temp_t0_2)

        self.horizontalLayout_182.setStretch(0, 5)

        self.verticalLayout_45.addWidget(self.widget_193)

        self.widget_195 = QWidget(self.widget_66)
        self.widget_195.setObjectName(u"widget_195")
        self.horizontalLayout_184 = QHBoxLayout(self.widget_195)
        self.horizontalLayout_184.setObjectName(u"horizontalLayout_184")
        self.horizontalLayout_184.setContentsMargins(0, 0, 0, 0)
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
        self.label_257.setFont(font19)
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
        self.label_258.setFont(font19)
        self.label_258.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_258.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_461.addWidget(self.label_258)

        self.stacked_cel_fah_temp_t0_3.addWidget(self.fahrenheit_t0_3)

        self.horizontalLayout_184.addWidget(self.stacked_cel_fah_temp_t0_3)

        self.horizontalLayout_184.setStretch(0, 5)

        self.verticalLayout_45.addWidget(self.widget_195)

        self.widget_207 = QWidget(self.widget_66)
        self.widget_207.setObjectName(u"widget_207")
        self.horizontalLayout_296 = QHBoxLayout(self.widget_207)
        self.horizontalLayout_296.setObjectName(u"horizontalLayout_296")
        self.horizontalLayout_296.setContentsMargins(0, 0, 0, 0)
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
        self.label_259.setFont(font19)
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
        self.label_260.setFont(font19)
        self.label_260.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_260.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_463.addWidget(self.label_260)

        self.stacked_cel_fah_temp_t0_4.addWidget(self.fahrenheit_t0_4)

        self.horizontalLayout_296.addWidget(self.stacked_cel_fah_temp_t0_4)

        self.horizontalLayout_296.setStretch(0, 5)

        self.verticalLayout_45.addWidget(self.widget_207)

        self.widget_266 = QWidget(self.widget_66)
        self.widget_266.setObjectName(u"widget_266")
        self.horizontalLayout_337 = QHBoxLayout(self.widget_266)
        self.horizontalLayout_337.setObjectName(u"horizontalLayout_337")
        self.horizontalLayout_337.setContentsMargins(0, 0, 0, 0)
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
        self.label_364.setFont(font19)
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
        self.label_365.setFont(font19)
        self.label_365.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_365.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_465.addWidget(self.label_365)

        self.stacked_cel_fah_temp_t0_5.addWidget(self.fahrenheit_t0_5)

        self.horizontalLayout_337.addWidget(self.stacked_cel_fah_temp_t0_5)

        self.horizontalLayout_337.setStretch(0, 5)

        self.verticalLayout_45.addWidget(self.widget_266)

        self.label_135 = QLabel(self.widget_66)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setFont(font19)
        self.label_135.setAlignment(Qt.AlignCenter)

        self.verticalLayout_45.addWidget(self.label_135)

        self.label_136 = QLabel(self.widget_66)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setFont(font19)
        self.label_136.setAlignment(Qt.AlignCenter)

        self.verticalLayout_45.addWidget(self.label_136)

        self.verticalLayout_45.setStretch(0, 1)
        self.verticalLayout_45.setStretch(1, 1)
        self.verticalLayout_45.setStretch(2, 1)
        self.verticalLayout_45.setStretch(3, 1)
        self.verticalLayout_45.setStretch(4, 1)
        self.verticalLayout_45.setStretch(5, 1)
        self.verticalLayout_45.setStretch(6, 1)

        self.verticalLayout_32.addWidget(self.widget_66)

        self.verticalLayout_32.setStretch(0, 1)
        self.verticalLayout_32.setStretch(1, 7)

        self.horizontalLayout_198.addWidget(self.t0_widget)

        self.line_19 = QFrame(self.widget_77)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.Shape.VLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_198.addWidget(self.line_19)

        self.at_widget = QWidget(self.widget_77)
        self.at_widget.setObjectName(u"at_widget")
        sizePolicy.setHeightForWidth(self.at_widget.sizePolicy().hasHeightForWidth())
        self.at_widget.setSizePolicy(sizePolicy)
        self.at_widget.setStyleSheet(u"border-left: None;")
        self.verticalLayout_33 = QVBoxLayout(self.at_widget)
        self.verticalLayout_33.setSpacing(10)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(5, 0, 5, 5)
        self.widget_72 = QWidget(self.at_widget)
        self.widget_72.setObjectName(u"widget_72")
        self.horizontalLayout_71 = QHBoxLayout(self.widget_72)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.label_150 = QLabel(self.widget_72)
        self.label_150.setObjectName(u"label_150")
        sizePolicy.setHeightForWidth(self.label_150.sizePolicy().hasHeightForWidth())
        self.label_150.setSizePolicy(sizePolicy)
        self.label_150.setFont(font18)
        self.label_150.setStyleSheet(u"color: rgb(30, 136, 229);")
        self.label_150.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_71.addWidget(self.label_150)


        self.verticalLayout_33.addWidget(self.widget_72)

        self.widget_76 = QWidget(self.at_widget)
        self.widget_76.setObjectName(u"widget_76")
        self.widget_76.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.verticalLayout_47 = QVBoxLayout(self.widget_76)
        self.verticalLayout_47.setSpacing(10)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.widget_220 = QWidget(self.widget_76)
        self.widget_220.setObjectName(u"widget_220")
        self.horizontalLayout_167 = QHBoxLayout(self.widget_220)
        self.horizontalLayout_167.setObjectName(u"horizontalLayout_167")
        self.horizontalLayout_167.setContentsMargins(0, 0, 0, 0)
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
        self.label_320.setFont(font19)
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
        self.label_321.setFont(font19)
        self.label_321.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_321.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_407.addWidget(self.label_321)

        self.stacked_cel_fah_temp_a_1.addWidget(self.fahrenheit_at_14)

        self.horizontalLayout_167.addWidget(self.stacked_cel_fah_temp_a_1)

        self.horizontalLayout_167.setStretch(0, 5)

        self.verticalLayout_47.addWidget(self.widget_220)

        self.widget_228 = QWidget(self.widget_76)
        self.widget_228.setObjectName(u"widget_228")
        self.horizontalLayout_189 = QHBoxLayout(self.widget_228)
        self.horizontalLayout_189.setObjectName(u"horizontalLayout_189")
        self.horizontalLayout_189.setContentsMargins(0, 0, 0, 0)
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
        self.label_322.setFont(font19)
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
        self.label_323.setFont(font19)
        self.label_323.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_323.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_409.addWidget(self.label_323)

        self.stacked_cel_fah_temp_a_2.addWidget(self.fahrenheit_at_15)

        self.horizontalLayout_189.addWidget(self.stacked_cel_fah_temp_a_2)

        self.horizontalLayout_189.setStretch(0, 5)

        self.verticalLayout_47.addWidget(self.widget_228)

        self.widget_239 = QWidget(self.widget_76)
        self.widget_239.setObjectName(u"widget_239")
        self.horizontalLayout_190 = QHBoxLayout(self.widget_239)
        self.horizontalLayout_190.setObjectName(u"horizontalLayout_190")
        self.horizontalLayout_190.setContentsMargins(0, 0, 0, 0)
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
        self.label_324.setFont(font19)
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
        self.label_325.setFont(font19)
        self.label_325.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_325.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_411.addWidget(self.label_325)

        self.stacked_cel_fah_temp_a_3.addWidget(self.fahrenheit_at_16)

        self.horizontalLayout_190.addWidget(self.stacked_cel_fah_temp_a_3)

        self.horizontalLayout_190.setStretch(0, 5)

        self.verticalLayout_47.addWidget(self.widget_239)

        self.widget_208 = QWidget(self.widget_76)
        self.widget_208.setObjectName(u"widget_208")
        self.horizontalLayout_303 = QHBoxLayout(self.widget_208)
        self.horizontalLayout_303.setObjectName(u"horizontalLayout_303")
        self.horizontalLayout_303.setContentsMargins(0, 0, 0, 0)
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
        self.label_326.setFont(font19)
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
        self.label_327.setFont(font19)
        self.label_327.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_327.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_413.addWidget(self.label_327)

        self.stacked_cel_fah_temp_a_4.addWidget(self.fahrenheit_at_17)

        self.horizontalLayout_303.addWidget(self.stacked_cel_fah_temp_a_4)

        self.horizontalLayout_303.setStretch(0, 5)

        self.verticalLayout_47.addWidget(self.widget_208)

        self.widget_246 = QWidget(self.widget_76)
        self.widget_246.setObjectName(u"widget_246")
        self.horizontalLayout_311 = QHBoxLayout(self.widget_246)
        self.horizontalLayout_311.setObjectName(u"horizontalLayout_311")
        self.horizontalLayout_311.setContentsMargins(0, 0, 0, 0)
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
        self.label_328.setFont(font19)
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
        self.label_329.setFont(font19)
        self.label_329.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_329.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_415.addWidget(self.label_329)

        self.stacked_cel_fah_temp_a_5.addWidget(self.fahrenheit_at_18)

        self.horizontalLayout_311.addWidget(self.stacked_cel_fah_temp_a_5)

        self.horizontalLayout_311.setStretch(0, 5)

        self.verticalLayout_47.addWidget(self.widget_246)

        self.widget_244 = QWidget(self.widget_76)
        self.widget_244.setObjectName(u"widget_244")
        self.horizontalLayout_309 = QHBoxLayout(self.widget_244)
        self.horizontalLayout_309.setObjectName(u"horizontalLayout_309")
        self.horizontalLayout_309.setContentsMargins(0, 0, 0, 0)
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
        self.label_330.setFont(font19)
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
        self.label_331.setFont(font19)
        self.label_331.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_331.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_417.addWidget(self.label_331)

        self.stacked_cel_fah_temp_a_6.addWidget(self.fahrenheit_at_19)

        self.horizontalLayout_309.addWidget(self.stacked_cel_fah_temp_a_6)

        self.horizontalLayout_309.setStretch(0, 5)

        self.verticalLayout_47.addWidget(self.widget_244)

        self.widget_241 = QWidget(self.widget_76)
        self.widget_241.setObjectName(u"widget_241")
        self.horizontalLayout_300 = QHBoxLayout(self.widget_241)
        self.horizontalLayout_300.setObjectName(u"horizontalLayout_300")
        self.horizontalLayout_300.setContentsMargins(0, 0, 0, 0)
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
        self.label_332.setFont(font19)
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
        self.label_333.setFont(font19)
        self.label_333.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_333.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_419.addWidget(self.label_333)

        self.stacked_cel_fah_temp_a_7.addWidget(self.fahrenheit_at_20)

        self.horizontalLayout_300.addWidget(self.stacked_cel_fah_temp_a_7)

        self.horizontalLayout_300.setStretch(0, 5)

        self.verticalLayout_47.addWidget(self.widget_241)

        self.verticalLayout_47.setStretch(0, 1)
        self.verticalLayout_47.setStretch(1, 1)
        self.verticalLayout_47.setStretch(2, 1)
        self.verticalLayout_47.setStretch(3, 1)
        self.verticalLayout_47.setStretch(4, 1)
        self.verticalLayout_47.setStretch(5, 1)
        self.verticalLayout_47.setStretch(6, 1)

        self.verticalLayout_33.addWidget(self.widget_76)

        self.verticalLayout_33.setStretch(0, 1)
        self.verticalLayout_33.setStretch(1, 7)

        self.horizontalLayout_198.addWidget(self.at_widget)

        self.line_18 = QFrame(self.widget_77)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.Shape.VLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_198.addWidget(self.line_18)

        self.bt_widget = QWidget(self.widget_77)
        self.bt_widget.setObjectName(u"bt_widget")
        sizePolicy.setHeightForWidth(self.bt_widget.sizePolicy().hasHeightForWidth())
        self.bt_widget.setSizePolicy(sizePolicy)
        self.bt_widget.setStyleSheet(u"border-left: None;")
        self.verticalLayout_34 = QVBoxLayout(self.bt_widget)
        self.verticalLayout_34.setSpacing(10)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(5, 0, 5, 5)
        self.widget_79 = QWidget(self.bt_widget)
        self.widget_79.setObjectName(u"widget_79")
        self.horizontalLayout_78 = QHBoxLayout(self.widget_79)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.label_173 = QLabel(self.widget_79)
        self.label_173.setObjectName(u"label_173")
        sizePolicy.setHeightForWidth(self.label_173.sizePolicy().hasHeightForWidth())
        self.label_173.setSizePolicy(sizePolicy)
        self.label_173.setFont(font18)
        self.label_173.setStyleSheet(u"color: rgb(251, 140, 0);")
        self.label_173.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_78.addWidget(self.label_173)


        self.verticalLayout_34.addWidget(self.widget_79)

        self.widget_81 = QWidget(self.bt_widget)
        self.widget_81.setObjectName(u"widget_81")
        self.widget_81.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.verticalLayout_49 = QVBoxLayout(self.widget_81)
        self.verticalLayout_49.setSpacing(10)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.widget_255 = QWidget(self.widget_81)
        self.widget_255.setObjectName(u"widget_255")
        self.horizontalLayout_170 = QHBoxLayout(self.widget_255)
        self.horizontalLayout_170.setObjectName(u"horizontalLayout_170")
        self.horizontalLayout_170.setContentsMargins(0, 0, 0, 0)
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
        self.label_334.setFont(font19)
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
        self.label_335.setFont(font19)
        self.label_335.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_335.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_421.addWidget(self.label_335)

        self.stacked_cel_fah_temp_b_1.addWidget(self.fahrenheit_at_21)

        self.horizontalLayout_170.addWidget(self.stacked_cel_fah_temp_b_1)

        self.horizontalLayout_170.setStretch(0, 5)

        self.verticalLayout_49.addWidget(self.widget_255)

        self.widget_257 = QWidget(self.widget_81)
        self.widget_257.setObjectName(u"widget_257")
        self.horizontalLayout_313 = QHBoxLayout(self.widget_257)
        self.horizontalLayout_313.setObjectName(u"horizontalLayout_313")
        self.horizontalLayout_313.setContentsMargins(0, 0, 0, 0)
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
        self.label_336.setFont(font19)
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
        self.label_337.setFont(font19)
        self.label_337.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_337.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_423.addWidget(self.label_337)

        self.stacked_cel_fah_temp_b_2.addWidget(self.fahrenheit_at_22)

        self.horizontalLayout_313.addWidget(self.stacked_cel_fah_temp_b_2)

        self.horizontalLayout_313.setStretch(0, 5)

        self.verticalLayout_49.addWidget(self.widget_257)

        self.widget_259 = QWidget(self.widget_81)
        self.widget_259.setObjectName(u"widget_259")
        self.horizontalLayout_315 = QHBoxLayout(self.widget_259)
        self.horizontalLayout_315.setObjectName(u"horizontalLayout_315")
        self.horizontalLayout_315.setContentsMargins(0, 0, 0, 0)
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
        self.label_338.setFont(font19)
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
        self.label_339.setFont(font19)
        self.label_339.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_339.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_425.addWidget(self.label_339)

        self.stacked_cel_fah_temp_b_3.addWidget(self.fahrenheit_at_23)

        self.horizontalLayout_315.addWidget(self.stacked_cel_fah_temp_b_3)

        self.horizontalLayout_315.setStretch(0, 5)

        self.verticalLayout_49.addWidget(self.widget_259)

        self.widget_248 = QWidget(self.widget_81)
        self.widget_248.setObjectName(u"widget_248")
        self.horizontalLayout_320 = QHBoxLayout(self.widget_248)
        self.horizontalLayout_320.setObjectName(u"horizontalLayout_320")
        self.horizontalLayout_320.setContentsMargins(0, 0, 0, 0)
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
        self.label_342.setFont(font19)
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
        self.label_343.setFont(font19)
        self.label_343.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_343.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_429.addWidget(self.label_343)

        self.stacked_cel_fah_temp_b_4.addWidget(self.fahrenheit_at_25)

        self.horizontalLayout_320.addWidget(self.stacked_cel_fah_temp_b_4)

        self.horizontalLayout_320.setStretch(0, 5)

        self.verticalLayout_49.addWidget(self.widget_248)

        self.widget_252 = QWidget(self.widget_81)
        self.widget_252.setObjectName(u"widget_252")
        self.horizontalLayout_324 = QHBoxLayout(self.widget_252)
        self.horizontalLayout_324.setObjectName(u"horizontalLayout_324")
        self.horizontalLayout_324.setContentsMargins(0, 0, 0, 0)
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
        self.label_344.setFont(font19)
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
        self.label_345.setFont(font19)
        self.label_345.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_345.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_431.addWidget(self.label_345)

        self.stacked_cel_fah_temp_b_5.addWidget(self.fahrenheit_at_26)

        self.horizontalLayout_324.addWidget(self.stacked_cel_fah_temp_b_5)

        self.horizontalLayout_324.setStretch(0, 5)

        self.verticalLayout_49.addWidget(self.widget_252)

        self.widget_210 = QWidget(self.widget_81)
        self.widget_210.setObjectName(u"widget_210")
        self.horizontalLayout_305 = QHBoxLayout(self.widget_210)
        self.horizontalLayout_305.setObjectName(u"horizontalLayout_305")
        self.horizontalLayout_305.setContentsMargins(0, 0, 0, 0)
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
        self.label_346.setFont(font19)
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
        self.label_347.setFont(font19)
        self.label_347.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_347.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_436.addWidget(self.label_347)

        self.stacked_cel_fah_temp_b_6.addWidget(self.fahrenheit_at_27)

        self.horizontalLayout_305.addWidget(self.stacked_cel_fah_temp_b_6)

        self.horizontalLayout_305.setStretch(0, 5)

        self.verticalLayout_49.addWidget(self.widget_210)

        self.widget_261 = QWidget(self.widget_81)
        self.widget_261.setObjectName(u"widget_261")
        self.horizontalLayout_317 = QHBoxLayout(self.widget_261)
        self.horizontalLayout_317.setObjectName(u"horizontalLayout_317")
        self.horizontalLayout_317.setContentsMargins(0, 0, 0, 0)
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
        self.label_348.setFont(font19)
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
        self.label_349.setFont(font19)
        self.label_349.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_349.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_438.addWidget(self.label_349)

        self.stacked_cel_fah_temp_b_7.addWidget(self.fahrenheit_at_28)

        self.horizontalLayout_317.addWidget(self.stacked_cel_fah_temp_b_7)

        self.horizontalLayout_317.setStretch(0, 5)

        self.verticalLayout_49.addWidget(self.widget_261)

        self.verticalLayout_49.setStretch(0, 1)
        self.verticalLayout_49.setStretch(1, 1)
        self.verticalLayout_49.setStretch(2, 1)
        self.verticalLayout_49.setStretch(3, 1)
        self.verticalLayout_49.setStretch(4, 1)
        self.verticalLayout_49.setStretch(5, 1)
        self.verticalLayout_49.setStretch(6, 1)

        self.verticalLayout_34.addWidget(self.widget_81)

        self.verticalLayout_34.setStretch(0, 1)
        self.verticalLayout_34.setStretch(1, 7)

        self.horizontalLayout_198.addWidget(self.bt_widget)

        self.line_20 = QFrame(self.widget_77)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.Shape.VLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_198.addWidget(self.line_20)

        self.ct_widget = QWidget(self.widget_77)
        self.ct_widget.setObjectName(u"ct_widget")
        sizePolicy.setHeightForWidth(self.ct_widget.sizePolicy().hasHeightForWidth())
        self.ct_widget.setSizePolicy(sizePolicy)
        self.ct_widget.setStyleSheet(u"border-left: None;")
        self.verticalLayout_35 = QVBoxLayout(self.ct_widget)
        self.verticalLayout_35.setSpacing(10)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(5, 0, 5, 5)
        self.widget_84 = QWidget(self.ct_widget)
        self.widget_84.setObjectName(u"widget_84")
        self.horizontalLayout_79 = QHBoxLayout(self.widget_84)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.label_183 = QLabel(self.widget_84)
        self.label_183.setObjectName(u"label_183")
        sizePolicy.setHeightForWidth(self.label_183.sizePolicy().hasHeightForWidth())
        self.label_183.setSizePolicy(sizePolicy)
        self.label_183.setFont(font18)
        self.label_183.setStyleSheet(u"color: #6F00FF;")
        self.label_183.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_79.addWidget(self.label_183)


        self.verticalLayout_35.addWidget(self.widget_84)

        self.widget_90 = QWidget(self.ct_widget)
        self.widget_90.setObjectName(u"widget_90")
        self.widget_90.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: 2px solid #D1D5DB;\n"
"    border-radius: 15px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.verticalLayout_50 = QVBoxLayout(self.widget_90)
        self.verticalLayout_50.setSpacing(10)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.widget_275 = QWidget(self.widget_90)
        self.widget_275.setObjectName(u"widget_275")
        self.horizontalLayout_173 = QHBoxLayout(self.widget_275)
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.horizontalLayout_173.setContentsMargins(0, 0, 0, 0)
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
        self.label_350.setFont(font19)
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
        self.label_351.setFont(font19)
        self.label_351.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_351.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_443.addWidget(self.label_351)

        self.stacked_cel_fah_temp_c_1.addWidget(self.fahrenheit_ct_1)

        self.horizontalLayout_173.addWidget(self.stacked_cel_fah_temp_c_1)

        self.horizontalLayout_173.setStretch(0, 5)

        self.verticalLayout_50.addWidget(self.widget_275)

        self.widget_277 = QWidget(self.widget_90)
        self.widget_277.setObjectName(u"widget_277")
        self.horizontalLayout_330 = QHBoxLayout(self.widget_277)
        self.horizontalLayout_330.setObjectName(u"horizontalLayout_330")
        self.horizontalLayout_330.setContentsMargins(0, 0, 0, 0)
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
        self.label_352.setFont(font19)
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
        self.label_353.setFont(font19)
        self.label_353.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_353.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_445.addWidget(self.label_353)

        self.stacked_cel_fah_temp_c_2.addWidget(self.fahrenheit_ct_2)

        self.horizontalLayout_330.addWidget(self.stacked_cel_fah_temp_c_2)

        self.horizontalLayout_330.setStretch(0, 5)

        self.verticalLayout_50.addWidget(self.widget_277)

        self.widget_279 = QWidget(self.widget_90)
        self.widget_279.setObjectName(u"widget_279")
        self.horizontalLayout_332 = QHBoxLayout(self.widget_279)
        self.horizontalLayout_332.setObjectName(u"horizontalLayout_332")
        self.horizontalLayout_332.setContentsMargins(0, 0, 0, 0)
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
        self.label_354.setFont(font19)
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
        self.label_355.setFont(font19)
        self.label_355.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_355.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_447.addWidget(self.label_355)

        self.stacked_cel_fah_temp_c_3.addWidget(self.fahrenheit_ct_3)

        self.horizontalLayout_332.addWidget(self.stacked_cel_fah_temp_c_3)

        self.horizontalLayout_332.setStretch(0, 5)

        self.verticalLayout_50.addWidget(self.widget_279)

        self.widget_250 = QWidget(self.widget_90)
        self.widget_250.setObjectName(u"widget_250")
        self.horizontalLayout_322 = QHBoxLayout(self.widget_250)
        self.horizontalLayout_322.setObjectName(u"horizontalLayout_322")
        self.horizontalLayout_322.setContentsMargins(0, 0, 0, 0)
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
        self.label_356.setFont(font19)
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
        self.label_357.setFont(font19)
        self.label_357.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_357.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_449.addWidget(self.label_357)

        self.stacked_cel_fah_temp_c_4.addWidget(self.fahrenheit_ct_4)

        self.horizontalLayout_322.addWidget(self.stacked_cel_fah_temp_c_4)

        self.horizontalLayout_322.setStretch(0, 5)

        self.verticalLayout_50.addWidget(self.widget_250)

        self.widget_254 = QWidget(self.widget_90)
        self.widget_254.setObjectName(u"widget_254")
        self.horizontalLayout_326 = QHBoxLayout(self.widget_254)
        self.horizontalLayout_326.setObjectName(u"horizontalLayout_326")
        self.horizontalLayout_326.setContentsMargins(0, 0, 0, 0)
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
        self.label_358.setFont(font19)
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
        self.label_359.setFont(font19)
        self.label_359.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_359.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_451.addWidget(self.label_359)

        self.stacked_cel_fah_temp_c_5.addWidget(self.fahrenheit_ct_5)

        self.horizontalLayout_326.addWidget(self.stacked_cel_fah_temp_c_5)

        self.horizontalLayout_326.setStretch(0, 5)

        self.verticalLayout_50.addWidget(self.widget_254)

        self.widget_214 = QWidget(self.widget_90)
        self.widget_214.setObjectName(u"widget_214")
        self.horizontalLayout_307 = QHBoxLayout(self.widget_214)
        self.horizontalLayout_307.setObjectName(u"horizontalLayout_307")
        self.horizontalLayout_307.setContentsMargins(0, 0, 0, 0)
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
        self.label_360.setFont(font19)
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
        self.label_361.setFont(font19)
        self.label_361.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_361.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_453.addWidget(self.label_361)

        self.stacked_cel_fah_temp_c_6.addWidget(self.fahrenheit_ct_6)

        self.horizontalLayout_307.addWidget(self.stacked_cel_fah_temp_c_6)

        self.horizontalLayout_307.setStretch(0, 5)

        self.verticalLayout_50.addWidget(self.widget_214)

        self.widget_281 = QWidget(self.widget_90)
        self.widget_281.setObjectName(u"widget_281")
        self.horizontalLayout_334 = QHBoxLayout(self.widget_281)
        self.horizontalLayout_334.setObjectName(u"horizontalLayout_334")
        self.horizontalLayout_334.setContentsMargins(0, 0, 0, 0)
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
        self.label_362.setFont(font19)
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
        self.label_363.setFont(font19)
        self.label_363.setStyleSheet(u"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.label_363.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_455.addWidget(self.label_363)

        self.stacked_cel_fah_temp_c_7.addWidget(self.fahrenheit_ct_7)

        self.horizontalLayout_334.addWidget(self.stacked_cel_fah_temp_c_7)

        self.horizontalLayout_334.setStretch(0, 5)

        self.verticalLayout_50.addWidget(self.widget_281)

        self.verticalLayout_50.setStretch(0, 1)
        self.verticalLayout_50.setStretch(1, 1)
        self.verticalLayout_50.setStretch(2, 1)
        self.verticalLayout_50.setStretch(3, 1)
        self.verticalLayout_50.setStretch(4, 1)
        self.verticalLayout_50.setStretch(5, 1)
        self.verticalLayout_50.setStretch(6, 1)

        self.verticalLayout_35.addWidget(self.widget_90)

        self.verticalLayout_35.setStretch(0, 1)
        self.verticalLayout_35.setStretch(1, 7)

        self.horizontalLayout_198.addWidget(self.ct_widget)


        self.verticalLayout_56.addWidget(self.widget_77)


        self.verticalLayout_8.addWidget(self.widget_temperature)

        self.widget_18 = QWidget(self.temperature_page)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setStyleSheet(u"QPushButton {\n"
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
        self.horizontalLayout_33 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_33.setSpacing(10)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.heat_btn_t0 = QPushButton(self.widget_18)
        self.heat_btn_t0.setObjectName(u"heat_btn_t0")
        sizePolicy.setHeightForWidth(self.heat_btn_t0.sizePolicy().hasHeightForWidth())
        self.heat_btn_t0.setSizePolicy(sizePolicy)
        self.heat_btn_t0.setMaximumSize(QSize(16777215, 150))
        self.heat_btn_t0.setFont(font9)
        self.heat_btn_t0.setStyleSheet(u"")
        self.heat_btn_t0.setIcon(icon13)
        self.heat_btn_t0.setIconSize(QSize(30, 30))
        self.heat_btn_t0.setCheckable(True)

        self.horizontalLayout_33.addWidget(self.heat_btn_t0)

        self.back_home_btn = QPushButton(self.widget_18)
        self.back_home_btn.setObjectName(u"back_home_btn")
        sizePolicy.setHeightForWidth(self.back_home_btn.sizePolicy().hasHeightForWidth())
        self.back_home_btn.setSizePolicy(sizePolicy)
        self.back_home_btn.setFont(font9)
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

        self.horizontalLayout_33.addWidget(self.back_home_btn)


        self.verticalLayout_8.addWidget(self.widget_18)

        self.verticalLayout_8.setStretch(0, 8)
        self.verticalLayout_8.setStretch(1, 1)
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
"    margin: 5px;\n"
"}\n"
"QFrame:hover {\n"
"    border: 1px solid #0B7EC8;\n"
"}")
        self.device_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_24 = QVBoxLayout(self.device_frame)
        self.verticalLayout_24.setSpacing(10)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 15, 0, 15)
        self.connection_status_layout = QHBoxLayout()
        self.connection_status_layout.setSpacing(0)
        self.connection_status_layout.setObjectName(u"connection_status_layout")
        self.plc_io_btn = QPushButton(self.device_frame)
        self.plc_io_btn.setObjectName(u"plc_io_btn")
        sizePolicy.setHeightForWidth(self.plc_io_btn.sizePolicy().hasHeightForWidth())
        self.plc_io_btn.setSizePolicy(sizePolicy)
        self.plc_io_btn.setStyleSheet(u"font-size: 24px; \n"
"color: #0B7EC8;\n"
"border: none;\n"
"image:url(:/newPrefix/Image_20260416155332_127_10.png)")

        self.connection_status_layout.addWidget(self.plc_io_btn)


        self.verticalLayout_24.addLayout(self.connection_status_layout)

        self.widget_15 = QWidget(self.device_frame)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.widget_15)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.connection_group = QGroupBox(self.widget_15)
        self.connection_group.setObjectName(u"connection_group")
        font20 = QFont()
        font20.setFamilies([u"Segoe UI"])
        font20.setPointSize(12)
        font20.setBold(True)
        self.connection_group.setFont(font20)
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
"\n"
"QLineEdit {\n"
"	color: black;\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    background-color: #F9FAFB;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0B7EC8;\n"
"    background-color: white;\n"
"}")
        self.gridLayout_4 = QGridLayout(self.connection_group)
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(20, 25, 20, 25)
        self.db_data_size_input = QSpinBox(self.connection_group)
        self.db_data_size_input.setObjectName(u"db_data_size_input")
        sizePolicy.setHeightForWidth(self.db_data_size_input.sizePolicy().hasHeightForWidth())
        self.db_data_size_input.setSizePolicy(sizePolicy)
        self.db_data_size_input.setMinimumSize(QSize(0, 0))
        font21 = QFont()
        font21.setPointSize(16)
        font21.setBold(True)
        self.db_data_size_input.setFont(font21)
        self.db_data_size_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_data_size_input.setMaximum(1024)
        self.db_data_size_input.setValue(128)

        self.gridLayout_4.addWidget(self.db_data_size_input, 3, 2, 1, 1)

        self.slot_label_8 = QLabel(self.connection_group)
        self.slot_label_8.setObjectName(u"slot_label_8")
        self.slot_label_8.setFont(font21)

        self.gridLayout_4.addWidget(self.slot_label_8, 4, 0, 1, 1)

        self.slot_label_2 = QLabel(self.connection_group)
        self.slot_label_2.setObjectName(u"slot_label_2")
        self.slot_label_2.setFont(font21)

        self.gridLayout_4.addWidget(self.slot_label_2, 2, 0, 1, 1)

        self.slot_label_7 = QLabel(self.connection_group)
        self.slot_label_7.setObjectName(u"slot_label_7")
        self.slot_label_7.setFont(font21)

        self.gridLayout_4.addWidget(self.slot_label_7, 3, 0, 1, 1)

        self.db_number_input = QSpinBox(self.connection_group)
        self.db_number_input.setObjectName(u"db_number_input")
        sizePolicy.setHeightForWidth(self.db_number_input.sizePolicy().hasHeightForWidth())
        self.db_number_input.setSizePolicy(sizePolicy)
        self.db_number_input.setMinimumSize(QSize(0, 0))
        self.db_number_input.setFont(font21)
        self.db_number_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.db_number_input.setSpecialValueText(u"")
        self.db_number_input.setValue(1)

        self.gridLayout_4.addWidget(self.db_number_input, 2, 2, 1, 1)

        self.interupt_time_input = QSpinBox(self.connection_group)
        self.interupt_time_input.setObjectName(u"interupt_time_input")
        sizePolicy.setHeightForWidth(self.interupt_time_input.sizePolicy().hasHeightForWidth())
        self.interupt_time_input.setSizePolicy(sizePolicy)
        self.interupt_time_input.setMinimumSize(QSize(0, 0))
        self.interupt_time_input.setFont(font21)
        self.interupt_time_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.interupt_time_input.setMaximum(10000)
        self.interupt_time_input.setValue(250)

        self.gridLayout_4.addWidget(self.interupt_time_input, 4, 2, 1, 1)

        self.plc_ip_address = QLabel(self.connection_group)
        self.plc_ip_address.setObjectName(u"plc_ip_address")
        self.plc_ip_address.setFont(font21)

        self.gridLayout_4.addWidget(self.plc_ip_address, 1, 0, 1, 1)

        self.plc_ip_address_edit = QLineEdit(self.connection_group)
        self.plc_ip_address_edit.setObjectName(u"plc_ip_address_edit")
        sizePolicy.setHeightForWidth(self.plc_ip_address_edit.sizePolicy().hasHeightForWidth())
        self.plc_ip_address_edit.setSizePolicy(sizePolicy)
        self.plc_ip_address_edit.setFont(font21)
        self.plc_ip_address_edit.setPlaceholderText(u"Enter IP address: 172.16.100.///")

        self.gridLayout_4.addWidget(self.plc_ip_address_edit, 1, 2, 1, 1)

        self.plc_ip_address_2 = QLabel(self.connection_group)
        self.plc_ip_address_2.setObjectName(u"plc_ip_address_2")
        self.plc_ip_address_2.setFont(font21)

        self.gridLayout_4.addWidget(self.plc_ip_address_2, 0, 0, 1, 1)

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
        self.sys_state_stacked_wid_40.setStyleSheet(u"QLabel{\n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"padding-right: 3px;\n"
"}")
        self.running_light_32 = QWidget()
        self.running_light_32.setObjectName(u"running_light_32")
        self.horizontalLayout_328 = QHBoxLayout(self.running_light_32)
        self.horizontalLayout_328.setObjectName(u"horizontalLayout_328")
        self.horizontalLayout_328.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.running_light_32)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setFont(font7)
        self.pushButton_4.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #10B981; \n"
"padding-right: 3px;")
        self.pushButton_4.setIcon(icon7)
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
        self.pushButton_21.setFont(font7)
        self.pushButton_21.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #F90A0A; \n"
"padding-right: 3px;")
        self.pushButton_21.setIcon(icon9)
        self.pushButton_21.setIconSize(QSize(30, 30))

        self.horizontalLayout_339.addWidget(self.pushButton_21)

        self.sys_state_stacked_wid_40.addWidget(self.error_light_32)

        self.horizontalLayout_31.addWidget(self.sys_state_stacked_wid_40)

        self.rb_connect = QPushButton(self.widget_28)
        self.rb_connect.setObjectName(u"rb_connect")
        sizePolicy.setHeightForWidth(self.rb_connect.sizePolicy().hasHeightForWidth())
        self.rb_connect.setSizePolicy(sizePolicy)
        self.rb_connect.setFont(font7)
        self.rb_connect.setStyleSheet(u"QPushButton {\n"
"    background-color: #10B981;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 12px 24px;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #059669;\n"
"}")

        self.horizontalLayout_31.addWidget(self.rb_connect)

        self.dis_rb = QPushButton(self.widget_28)
        self.dis_rb.setObjectName(u"dis_rb")
        sizePolicy.setHeightForWidth(self.dis_rb.sizePolicy().hasHeightForWidth())
        self.dis_rb.setSizePolicy(sizePolicy)
        self.dis_rb.setFont(font7)
        self.dis_rb.setStyleSheet(u"QPushButton {\n"
"    background-color: #EF4444;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 12px 24px;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #DC2626;\n"
"}")

        self.horizontalLayout_31.addWidget(self.dis_rb)

        self.horizontalLayout_31.setStretch(0, 2)
        self.horizontalLayout_31.setStretch(1, 1)

        self.gridLayout_4.addWidget(self.widget_28, 0, 2, 1, 1)

        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 1)
        self.gridLayout_4.setRowStretch(2, 1)
        self.gridLayout_4.setRowStretch(3, 1)
        self.gridLayout_4.setRowStretch(4, 1)

        self.verticalLayout_9.addWidget(self.connection_group)

        self.widget_25 = QWidget(self.widget_15)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setStyleSheet(u"QPushButton {\n"
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
        self.verticalLayout_17 = QVBoxLayout(self.widget_25)
        self.verticalLayout_17.setSpacing(10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_27 = QWidget(self.widget_25)
        self.widget_27.setObjectName(u"widget_27")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.new_data_btn_2 = QPushButton(self.widget_27)
        self.new_data_btn_2.setObjectName(u"new_data_btn_2")
        sizePolicy.setHeightForWidth(self.new_data_btn_2.sizePolicy().hasHeightForWidth())
        self.new_data_btn_2.setSizePolicy(sizePolicy)
        self.new_data_btn_2.setFont(font9)
        self.new_data_btn_2.setIcon(icon11)
        self.new_data_btn_2.setIconSize(QSize(35, 35))

        self.horizontalLayout_28.addWidget(self.new_data_btn_2)

        self.clear_data_btn_2 = QPushButton(self.widget_27)
        self.clear_data_btn_2.setObjectName(u"clear_data_btn_2")
        sizePolicy.setHeightForWidth(self.clear_data_btn_2.sizePolicy().hasHeightForWidth())
        self.clear_data_btn_2.setSizePolicy(sizePolicy)
        self.clear_data_btn_2.setFont(font9)
        self.clear_data_btn_2.setIcon(icon10)
        self.clear_data_btn_2.setIconSize(QSize(35, 35))

        self.horizontalLayout_28.addWidget(self.clear_data_btn_2)

        self.horizontalLayout_28.setStretch(0, 1)
        self.horizontalLayout_28.setStretch(1, 1)

        self.verticalLayout_17.addWidget(self.widget_27)


        self.verticalLayout_9.addWidget(self.widget_25)

        self.verticalLayout_9.setStretch(0, 7)
        self.verticalLayout_9.setStretch(1, 1)

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
        self.i_o_group_1.setFont(font20)
        self.i_o_group_1.setStyleSheet(u"QGroupBox {\n"
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
        self.gridLayout_7.setContentsMargins(10, 10, 10, 10)
        self.i_o_group_1_switch_3 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_3.setObjectName(u"i_o_group_1_switch_3")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_3.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_3.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_3.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_9 = QWidget()
        self.on_light_9.setObjectName(u"on_light_9")
        self.horizontalLayout_486 = QHBoxLayout(self.on_light_9)
        self.horizontalLayout_486.setObjectName(u"horizontalLayout_486")
        self.horizontalLayout_486.setContentsMargins(0, 0, 0, 0)
        self.pushButton_58 = QPushButton(self.on_light_9)
        self.pushButton_58.setObjectName(u"pushButton_58")
        sizePolicy.setHeightForWidth(self.pushButton_58.sizePolicy().hasHeightForWidth())
        self.pushButton_58.setSizePolicy(sizePolicy)
        self.pushButton_58.setFont(font6)
        self.pushButton_58.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_58.setIcon(icon7)
        self.pushButton_58.setIconSize(QSize(45, 45))

        self.horizontalLayout_486.addWidget(self.pushButton_58)

        self.i_o_group_1_switch_3.addWidget(self.on_light_9)
        self.off_light_9 = QWidget()
        self.off_light_9.setObjectName(u"off_light_9")
        self.horizontalLayout_487 = QHBoxLayout(self.off_light_9)
        self.horizontalLayout_487.setObjectName(u"horizontalLayout_487")
        self.horizontalLayout_487.setContentsMargins(0, 0, 0, 0)
        self.pushButton_59 = QPushButton(self.off_light_9)
        self.pushButton_59.setObjectName(u"pushButton_59")
        sizePolicy.setHeightForWidth(self.pushButton_59.sizePolicy().hasHeightForWidth())
        self.pushButton_59.setSizePolicy(sizePolicy)
        self.pushButton_59.setFont(font6)
        self.pushButton_59.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_59.setIcon(icon9)
        self.pushButton_59.setIconSize(QSize(45, 45))

        self.horizontalLayout_487.addWidget(self.pushButton_59)

        self.i_o_group_1_switch_3.addWidget(self.off_light_9)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_3, 2, 1, 1, 1)

        self.i_o_group_1_switch_5 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_5.setObjectName(u"i_o_group_1_switch_5")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_5.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_5.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_5.setStyleSheet(u"")
        self.on_light_11 = QWidget()
        self.on_light_11.setObjectName(u"on_light_11")
        self.horizontalLayout_490 = QHBoxLayout(self.on_light_11)
        self.horizontalLayout_490.setObjectName(u"horizontalLayout_490")
        self.horizontalLayout_490.setContentsMargins(0, 0, 0, 0)
        self.pushButton_62 = QPushButton(self.on_light_11)
        self.pushButton_62.setObjectName(u"pushButton_62")
        sizePolicy.setHeightForWidth(self.pushButton_62.sizePolicy().hasHeightForWidth())
        self.pushButton_62.setSizePolicy(sizePolicy)
        self.pushButton_62.setFont(font6)
        self.pushButton_62.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_62.setIcon(icon7)
        self.pushButton_62.setIconSize(QSize(45, 45))

        self.horizontalLayout_490.addWidget(self.pushButton_62)

        self.i_o_group_1_switch_5.addWidget(self.on_light_11)
        self.off_light_11 = QWidget()
        self.off_light_11.setObjectName(u"off_light_11")
        self.horizontalLayout_491 = QHBoxLayout(self.off_light_11)
        self.horizontalLayout_491.setObjectName(u"horizontalLayout_491")
        self.horizontalLayout_491.setContentsMargins(0, 0, 0, 0)
        self.pushButton_63 = QPushButton(self.off_light_11)
        self.pushButton_63.setObjectName(u"pushButton_63")
        sizePolicy.setHeightForWidth(self.pushButton_63.sizePolicy().hasHeightForWidth())
        self.pushButton_63.setSizePolicy(sizePolicy)
        self.pushButton_63.setFont(font6)
        self.pushButton_63.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_63.setIcon(icon9)
        self.pushButton_63.setIconSize(QSize(45, 45))

        self.horizontalLayout_491.addWidget(self.pushButton_63)

        self.i_o_group_1_switch_5.addWidget(self.off_light_11)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_5, 4, 1, 1, 1)

        self.i_o_group_1_switch_6 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_6.setObjectName(u"i_o_group_1_switch_6")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_6.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_6.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_6.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_12 = QWidget()
        self.on_light_12.setObjectName(u"on_light_12")
        self.horizontalLayout_492 = QHBoxLayout(self.on_light_12)
        self.horizontalLayout_492.setObjectName(u"horizontalLayout_492")
        self.horizontalLayout_492.setContentsMargins(0, 0, 0, 0)
        self.pushButton_64 = QPushButton(self.on_light_12)
        self.pushButton_64.setObjectName(u"pushButton_64")
        sizePolicy.setHeightForWidth(self.pushButton_64.sizePolicy().hasHeightForWidth())
        self.pushButton_64.setSizePolicy(sizePolicy)
        self.pushButton_64.setFont(font6)
        self.pushButton_64.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_64.setIcon(icon7)
        self.pushButton_64.setIconSize(QSize(45, 45))

        self.horizontalLayout_492.addWidget(self.pushButton_64)

        self.i_o_group_1_switch_6.addWidget(self.on_light_12)
        self.off_light_12 = QWidget()
        self.off_light_12.setObjectName(u"off_light_12")
        self.horizontalLayout_493 = QHBoxLayout(self.off_light_12)
        self.horizontalLayout_493.setObjectName(u"horizontalLayout_493")
        self.horizontalLayout_493.setContentsMargins(0, 0, 0, 0)
        self.pushButton_65 = QPushButton(self.off_light_12)
        self.pushButton_65.setObjectName(u"pushButton_65")
        sizePolicy.setHeightForWidth(self.pushButton_65.sizePolicy().hasHeightForWidth())
        self.pushButton_65.setSizePolicy(sizePolicy)
        self.pushButton_65.setFont(font6)
        self.pushButton_65.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_65.setIcon(icon9)
        self.pushButton_65.setIconSize(QSize(45, 45))

        self.horizontalLayout_493.addWidget(self.pushButton_65)

        self.i_o_group_1_switch_6.addWidget(self.off_light_12)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_6, 5, 1, 1, 1)

        self.i_o_group_1_switch_7 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_7.setObjectName(u"i_o_group_1_switch_7")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_7.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_7.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_7.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_13 = QWidget()
        self.on_light_13.setObjectName(u"on_light_13")
        self.horizontalLayout_494 = QHBoxLayout(self.on_light_13)
        self.horizontalLayout_494.setObjectName(u"horizontalLayout_494")
        self.horizontalLayout_494.setContentsMargins(0, 0, 0, 0)
        self.pushButton_66 = QPushButton(self.on_light_13)
        self.pushButton_66.setObjectName(u"pushButton_66")
        sizePolicy.setHeightForWidth(self.pushButton_66.sizePolicy().hasHeightForWidth())
        self.pushButton_66.setSizePolicy(sizePolicy)
        self.pushButton_66.setFont(font6)
        self.pushButton_66.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_66.setIcon(icon7)
        self.pushButton_66.setIconSize(QSize(45, 45))

        self.horizontalLayout_494.addWidget(self.pushButton_66)

        self.i_o_group_1_switch_7.addWidget(self.on_light_13)
        self.off_light_13 = QWidget()
        self.off_light_13.setObjectName(u"off_light_13")
        self.horizontalLayout_495 = QHBoxLayout(self.off_light_13)
        self.horizontalLayout_495.setObjectName(u"horizontalLayout_495")
        self.horizontalLayout_495.setContentsMargins(0, 0, 0, 0)
        self.pushButton_67 = QPushButton(self.off_light_13)
        self.pushButton_67.setObjectName(u"pushButton_67")
        sizePolicy.setHeightForWidth(self.pushButton_67.sizePolicy().hasHeightForWidth())
        self.pushButton_67.setSizePolicy(sizePolicy)
        self.pushButton_67.setFont(font6)
        self.pushButton_67.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_67.setIcon(icon9)
        self.pushButton_67.setIconSize(QSize(45, 45))

        self.horizontalLayout_495.addWidget(self.pushButton_67)

        self.i_o_group_1_switch_7.addWidget(self.off_light_13)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_7, 6, 1, 1, 1)

        self.i_o_group_1_switch_2 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_2.setObjectName(u"i_o_group_1_switch_2")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_2.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_2.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_2.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_8 = QWidget()
        self.on_light_8.setObjectName(u"on_light_8")
        self.horizontalLayout_484 = QHBoxLayout(self.on_light_8)
        self.horizontalLayout_484.setObjectName(u"horizontalLayout_484")
        self.horizontalLayout_484.setContentsMargins(0, 0, 0, 0)
        self.pushButton_56 = QPushButton(self.on_light_8)
        self.pushButton_56.setObjectName(u"pushButton_56")
        sizePolicy.setHeightForWidth(self.pushButton_56.sizePolicy().hasHeightForWidth())
        self.pushButton_56.setSizePolicy(sizePolicy)
        self.pushButton_56.setFont(font6)
        self.pushButton_56.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_56.setIcon(icon7)
        self.pushButton_56.setIconSize(QSize(45, 45))

        self.horizontalLayout_484.addWidget(self.pushButton_56)

        self.i_o_group_1_switch_2.addWidget(self.on_light_8)
        self.off_light_8 = QWidget()
        self.off_light_8.setObjectName(u"off_light_8")
        self.horizontalLayout_485 = QHBoxLayout(self.off_light_8)
        self.horizontalLayout_485.setObjectName(u"horizontalLayout_485")
        self.horizontalLayout_485.setContentsMargins(0, 0, 0, 0)
        self.pushButton_57 = QPushButton(self.off_light_8)
        self.pushButton_57.setObjectName(u"pushButton_57")
        sizePolicy.setHeightForWidth(self.pushButton_57.sizePolicy().hasHeightForWidth())
        self.pushButton_57.setSizePolicy(sizePolicy)
        self.pushButton_57.setFont(font6)
        self.pushButton_57.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_57.setIcon(icon9)
        self.pushButton_57.setIconSize(QSize(45, 45))

        self.horizontalLayout_485.addWidget(self.pushButton_57)

        self.i_o_group_1_switch_2.addWidget(self.off_light_8)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_2, 1, 1, 1, 1)

        self.di_name_1 = QLabel(self.i_o_group_1)
        self.di_name_1.setObjectName(u"di_name_1")
        font22 = QFont()
        font22.setPointSize(20)
        font22.setBold(True)
        self.di_name_1.setFont(font22)

        self.gridLayout_7.addWidget(self.di_name_1, 0, 0, 1, 1)

        self.i_o_group_1_switch_1 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_1.setObjectName(u"i_o_group_1_switch_1")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_1.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_1.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_1.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_1 = QWidget()
        self.on_light_1.setObjectName(u"on_light_1")
        self.horizontalLayout_470 = QHBoxLayout(self.on_light_1)
        self.horizontalLayout_470.setObjectName(u"horizontalLayout_470")
        self.horizontalLayout_470.setContentsMargins(0, 0, 0, 0)
        self.pushButton_42 = QPushButton(self.on_light_1)
        self.pushButton_42.setObjectName(u"pushButton_42")
        sizePolicy.setHeightForWidth(self.pushButton_42.sizePolicy().hasHeightForWidth())
        self.pushButton_42.setSizePolicy(sizePolicy)
        self.pushButton_42.setFont(font6)
        self.pushButton_42.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_42.setIcon(icon7)
        self.pushButton_42.setIconSize(QSize(45, 45))

        self.horizontalLayout_470.addWidget(self.pushButton_42)

        self.i_o_group_1_switch_1.addWidget(self.on_light_1)
        self.off_light_1 = QWidget()
        self.off_light_1.setObjectName(u"off_light_1")
        self.horizontalLayout_471 = QHBoxLayout(self.off_light_1)
        self.horizontalLayout_471.setObjectName(u"horizontalLayout_471")
        self.horizontalLayout_471.setContentsMargins(0, 0, 0, 0)
        self.pushButton_43 = QPushButton(self.off_light_1)
        self.pushButton_43.setObjectName(u"pushButton_43")
        sizePolicy.setHeightForWidth(self.pushButton_43.sizePolicy().hasHeightForWidth())
        self.pushButton_43.setSizePolicy(sizePolicy)
        self.pushButton_43.setFont(font6)
        self.pushButton_43.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_43.setIcon(icon9)
        self.pushButton_43.setIconSize(QSize(45, 45))

        self.horizontalLayout_471.addWidget(self.pushButton_43)

        self.i_o_group_1_switch_1.addWidget(self.off_light_1)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_1, 0, 1, 1, 1)

        self.i_o_group_1_switch_4 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_4.setObjectName(u"i_o_group_1_switch_4")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_4.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_4.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_4.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_10 = QWidget()
        self.on_light_10.setObjectName(u"on_light_10")
        self.horizontalLayout_488 = QHBoxLayout(self.on_light_10)
        self.horizontalLayout_488.setObjectName(u"horizontalLayout_488")
        self.horizontalLayout_488.setContentsMargins(0, 0, 0, 0)
        self.pushButton_60 = QPushButton(self.on_light_10)
        self.pushButton_60.setObjectName(u"pushButton_60")
        sizePolicy.setHeightForWidth(self.pushButton_60.sizePolicy().hasHeightForWidth())
        self.pushButton_60.setSizePolicy(sizePolicy)
        self.pushButton_60.setFont(font6)
        self.pushButton_60.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_60.setIcon(icon7)
        self.pushButton_60.setIconSize(QSize(45, 45))

        self.horizontalLayout_488.addWidget(self.pushButton_60)

        self.i_o_group_1_switch_4.addWidget(self.on_light_10)
        self.off_light_10 = QWidget()
        self.off_light_10.setObjectName(u"off_light_10")
        self.horizontalLayout_489 = QHBoxLayout(self.off_light_10)
        self.horizontalLayout_489.setObjectName(u"horizontalLayout_489")
        self.horizontalLayout_489.setContentsMargins(0, 0, 0, 0)
        self.pushButton_61 = QPushButton(self.off_light_10)
        self.pushButton_61.setObjectName(u"pushButton_61")
        sizePolicy.setHeightForWidth(self.pushButton_61.sizePolicy().hasHeightForWidth())
        self.pushButton_61.setSizePolicy(sizePolicy)
        self.pushButton_61.setFont(font6)
        self.pushButton_61.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_61.setIcon(icon9)
        self.pushButton_61.setIconSize(QSize(45, 45))

        self.horizontalLayout_489.addWidget(self.pushButton_61)

        self.i_o_group_1_switch_4.addWidget(self.off_light_10)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_4, 3, 1, 1, 1)

        self.i_o_group_1_switch_8 = QStackedWidget(self.i_o_group_1)
        self.i_o_group_1_switch_8.setObjectName(u"i_o_group_1_switch_8")
        sizePolicy.setHeightForWidth(self.i_o_group_1_switch_8.sizePolicy().hasHeightForWidth())
        self.i_o_group_1_switch_8.setSizePolicy(sizePolicy)
        self.i_o_group_1_switch_8.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_14 = QWidget()
        self.on_light_14.setObjectName(u"on_light_14")
        self.horizontalLayout_496 = QHBoxLayout(self.on_light_14)
        self.horizontalLayout_496.setObjectName(u"horizontalLayout_496")
        self.horizontalLayout_496.setContentsMargins(0, 0, 0, 0)
        self.pushButton_68 = QPushButton(self.on_light_14)
        self.pushButton_68.setObjectName(u"pushButton_68")
        sizePolicy.setHeightForWidth(self.pushButton_68.sizePolicy().hasHeightForWidth())
        self.pushButton_68.setSizePolicy(sizePolicy)
        self.pushButton_68.setFont(font6)
        self.pushButton_68.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_68.setIcon(icon7)
        self.pushButton_68.setIconSize(QSize(45, 45))

        self.horizontalLayout_496.addWidget(self.pushButton_68)

        self.i_o_group_1_switch_8.addWidget(self.on_light_14)
        self.off_light_14 = QWidget()
        self.off_light_14.setObjectName(u"off_light_14")
        self.horizontalLayout_497 = QHBoxLayout(self.off_light_14)
        self.horizontalLayout_497.setObjectName(u"horizontalLayout_497")
        self.horizontalLayout_497.setContentsMargins(0, 0, 0, 0)
        self.pushButton_69 = QPushButton(self.off_light_14)
        self.pushButton_69.setObjectName(u"pushButton_69")
        sizePolicy.setHeightForWidth(self.pushButton_69.sizePolicy().hasHeightForWidth())
        self.pushButton_69.setSizePolicy(sizePolicy)
        self.pushButton_69.setFont(font6)
        self.pushButton_69.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_69.setIcon(icon9)
        self.pushButton_69.setIconSize(QSize(45, 45))

        self.horizontalLayout_497.addWidget(self.pushButton_69)

        self.i_o_group_1_switch_8.addWidget(self.off_light_14)

        self.gridLayout_7.addWidget(self.i_o_group_1_switch_8, 7, 1, 1, 1)

        self.di_name_2 = QLabel(self.i_o_group_1)
        self.di_name_2.setObjectName(u"di_name_2")
        self.di_name_2.setFont(font22)

        self.gridLayout_7.addWidget(self.di_name_2, 1, 0, 1, 1)

        self.di_name_3 = QLabel(self.i_o_group_1)
        self.di_name_3.setObjectName(u"di_name_3")
        self.di_name_3.setFont(font22)

        self.gridLayout_7.addWidget(self.di_name_3, 2, 0, 1, 1)

        self.di_name_4 = QLabel(self.i_o_group_1)
        self.di_name_4.setObjectName(u"di_name_4")
        self.di_name_4.setFont(font22)

        self.gridLayout_7.addWidget(self.di_name_4, 3, 0, 1, 1)

        self.di_name_5 = QLabel(self.i_o_group_1)
        self.di_name_5.setObjectName(u"di_name_5")
        self.di_name_5.setFont(font22)

        self.gridLayout_7.addWidget(self.di_name_5, 4, 0, 1, 1)

        self.di_name_6 = QLabel(self.i_o_group_1)
        self.di_name_6.setObjectName(u"di_name_6")
        self.di_name_6.setFont(font22)

        self.gridLayout_7.addWidget(self.di_name_6, 5, 0, 1, 1)

        self.di_name_7 = QLabel(self.i_o_group_1)
        self.di_name_7.setObjectName(u"di_name_7")
        self.di_name_7.setFont(font22)

        self.gridLayout_7.addWidget(self.di_name_7, 6, 0, 1, 1)

        self.di_name_8 = QLabel(self.i_o_group_1)
        self.di_name_8.setObjectName(u"di_name_8")
        self.di_name_8.setFont(font22)

        self.gridLayout_7.addWidget(self.di_name_8, 7, 0, 1, 1)

        self.gridLayout_7.setColumnStretch(1, 1)

        self.horizontalLayout_24.addWidget(self.i_o_group_1)

        self.i_o_group_2 = QGroupBox(self.widget_26)
        self.i_o_group_2.setObjectName(u"i_o_group_2")
        self.i_o_group_2.setFont(font20)
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
"QLabel{\n"
"	color: #2C81D1;\n"
"}\n"
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
        self.gridLayout_6.setContentsMargins(10, 10, 10, 10)
        self.i_o_group_2_switch_5 = QStackedWidget(self.i_o_group_2)
        self.i_o_group_2_switch_5.setObjectName(u"i_o_group_2_switch_5")
        sizePolicy.setHeightForWidth(self.i_o_group_2_switch_5.sizePolicy().hasHeightForWidth())
        self.i_o_group_2_switch_5.setSizePolicy(sizePolicy)
        self.i_o_group_2_switch_5.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_34 = QWidget()
        self.on_light_34.setObjectName(u"on_light_34")
        self.horizontalLayout_536 = QHBoxLayout(self.on_light_34)
        self.horizontalLayout_536.setObjectName(u"horizontalLayout_536")
        self.horizontalLayout_536.setContentsMargins(0, 0, 0, 0)
        self.pushButton_108 = QPushButton(self.on_light_34)
        self.pushButton_108.setObjectName(u"pushButton_108")
        sizePolicy.setHeightForWidth(self.pushButton_108.sizePolicy().hasHeightForWidth())
        self.pushButton_108.setSizePolicy(sizePolicy)
        self.pushButton_108.setFont(font6)
        self.pushButton_108.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_108.setIcon(icon7)
        self.pushButton_108.setIconSize(QSize(45, 45))

        self.horizontalLayout_536.addWidget(self.pushButton_108)

        self.i_o_group_2_switch_5.addWidget(self.on_light_34)
        self.off_light_34 = QWidget()
        self.off_light_34.setObjectName(u"off_light_34")
        self.horizontalLayout_537 = QHBoxLayout(self.off_light_34)
        self.horizontalLayout_537.setObjectName(u"horizontalLayout_537")
        self.horizontalLayout_537.setContentsMargins(0, 0, 0, 0)
        self.pushButton_109 = QPushButton(self.off_light_34)
        self.pushButton_109.setObjectName(u"pushButton_109")
        sizePolicy.setHeightForWidth(self.pushButton_109.sizePolicy().hasHeightForWidth())
        self.pushButton_109.setSizePolicy(sizePolicy)
        self.pushButton_109.setFont(font6)
        self.pushButton_109.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_109.setIcon(icon9)
        self.pushButton_109.setIconSize(QSize(45, 45))

        self.horizontalLayout_537.addWidget(self.pushButton_109)

        self.i_o_group_2_switch_5.addWidget(self.off_light_34)

        self.gridLayout_6.addWidget(self.i_o_group_2_switch_5, 2, 1, 1, 1)

        self.i_o_group_2_switch_6 = QStackedWidget(self.i_o_group_2)
        self.i_o_group_2_switch_6.setObjectName(u"i_o_group_2_switch_6")
        sizePolicy.setHeightForWidth(self.i_o_group_2_switch_6.sizePolicy().hasHeightForWidth())
        self.i_o_group_2_switch_6.setSizePolicy(sizePolicy)
        self.i_o_group_2_switch_6.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_35 = QWidget()
        self.on_light_35.setObjectName(u"on_light_35")
        self.horizontalLayout_538 = QHBoxLayout(self.on_light_35)
        self.horizontalLayout_538.setObjectName(u"horizontalLayout_538")
        self.horizontalLayout_538.setContentsMargins(0, 0, 0, 0)
        self.pushButton_110 = QPushButton(self.on_light_35)
        self.pushButton_110.setObjectName(u"pushButton_110")
        sizePolicy.setHeightForWidth(self.pushButton_110.sizePolicy().hasHeightForWidth())
        self.pushButton_110.setSizePolicy(sizePolicy)
        self.pushButton_110.setFont(font6)
        self.pushButton_110.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_110.setIcon(icon7)
        self.pushButton_110.setIconSize(QSize(45, 45))

        self.horizontalLayout_538.addWidget(self.pushButton_110)

        self.i_o_group_2_switch_6.addWidget(self.on_light_35)
        self.off_light_35 = QWidget()
        self.off_light_35.setObjectName(u"off_light_35")
        self.horizontalLayout_539 = QHBoxLayout(self.off_light_35)
        self.horizontalLayout_539.setObjectName(u"horizontalLayout_539")
        self.horizontalLayout_539.setContentsMargins(0, 0, 0, 0)
        self.pushButton_111 = QPushButton(self.off_light_35)
        self.pushButton_111.setObjectName(u"pushButton_111")
        sizePolicy.setHeightForWidth(self.pushButton_111.sizePolicy().hasHeightForWidth())
        self.pushButton_111.setSizePolicy(sizePolicy)
        self.pushButton_111.setFont(font6)
        self.pushButton_111.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_111.setIcon(icon9)
        self.pushButton_111.setIconSize(QSize(45, 45))

        self.horizontalLayout_539.addWidget(self.pushButton_111)

        self.i_o_group_2_switch_6.addWidget(self.off_light_35)

        self.gridLayout_6.addWidget(self.i_o_group_2_switch_6, 2, 3, 1, 1)

        self.i_o_group_2_switch_7 = QStackedWidget(self.i_o_group_2)
        self.i_o_group_2_switch_7.setObjectName(u"i_o_group_2_switch_7")
        sizePolicy.setHeightForWidth(self.i_o_group_2_switch_7.sizePolicy().hasHeightForWidth())
        self.i_o_group_2_switch_7.setSizePolicy(sizePolicy)
        self.i_o_group_2_switch_7.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_36 = QWidget()
        self.on_light_36.setObjectName(u"on_light_36")
        self.horizontalLayout_540 = QHBoxLayout(self.on_light_36)
        self.horizontalLayout_540.setObjectName(u"horizontalLayout_540")
        self.horizontalLayout_540.setContentsMargins(0, 0, 0, 0)
        self.pushButton_112 = QPushButton(self.on_light_36)
        self.pushButton_112.setObjectName(u"pushButton_112")
        sizePolicy.setHeightForWidth(self.pushButton_112.sizePolicy().hasHeightForWidth())
        self.pushButton_112.setSizePolicy(sizePolicy)
        self.pushButton_112.setFont(font6)
        self.pushButton_112.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_112.setIcon(icon7)
        self.pushButton_112.setIconSize(QSize(45, 45))

        self.horizontalLayout_540.addWidget(self.pushButton_112)

        self.i_o_group_2_switch_7.addWidget(self.on_light_36)
        self.off_light_36 = QWidget()
        self.off_light_36.setObjectName(u"off_light_36")
        self.horizontalLayout_541 = QHBoxLayout(self.off_light_36)
        self.horizontalLayout_541.setObjectName(u"horizontalLayout_541")
        self.horizontalLayout_541.setContentsMargins(0, 0, 0, 0)
        self.pushButton_113 = QPushButton(self.off_light_36)
        self.pushButton_113.setObjectName(u"pushButton_113")
        sizePolicy.setHeightForWidth(self.pushButton_113.sizePolicy().hasHeightForWidth())
        self.pushButton_113.setSizePolicy(sizePolicy)
        self.pushButton_113.setFont(font6)
        self.pushButton_113.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_113.setIcon(icon9)
        self.pushButton_113.setIconSize(QSize(45, 45))

        self.horizontalLayout_541.addWidget(self.pushButton_113)

        self.i_o_group_2_switch_7.addWidget(self.off_light_36)

        self.gridLayout_6.addWidget(self.i_o_group_2_switch_7, 3, 1, 1, 1)

        self.i_o_group_2_switch_8 = QStackedWidget(self.i_o_group_2)
        self.i_o_group_2_switch_8.setObjectName(u"i_o_group_2_switch_8")
        sizePolicy.setHeightForWidth(self.i_o_group_2_switch_8.sizePolicy().hasHeightForWidth())
        self.i_o_group_2_switch_8.setSizePolicy(sizePolicy)
        self.i_o_group_2_switch_8.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_37 = QWidget()
        self.on_light_37.setObjectName(u"on_light_37")
        self.horizontalLayout_542 = QHBoxLayout(self.on_light_37)
        self.horizontalLayout_542.setObjectName(u"horizontalLayout_542")
        self.horizontalLayout_542.setContentsMargins(0, 0, 0, 0)
        self.pushButton_114 = QPushButton(self.on_light_37)
        self.pushButton_114.setObjectName(u"pushButton_114")
        sizePolicy.setHeightForWidth(self.pushButton_114.sizePolicy().hasHeightForWidth())
        self.pushButton_114.setSizePolicy(sizePolicy)
        self.pushButton_114.setFont(font6)
        self.pushButton_114.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_114.setIcon(icon7)
        self.pushButton_114.setIconSize(QSize(45, 45))

        self.horizontalLayout_542.addWidget(self.pushButton_114)

        self.i_o_group_2_switch_8.addWidget(self.on_light_37)
        self.off_light_37 = QWidget()
        self.off_light_37.setObjectName(u"off_light_37")
        self.horizontalLayout_543 = QHBoxLayout(self.off_light_37)
        self.horizontalLayout_543.setObjectName(u"horizontalLayout_543")
        self.horizontalLayout_543.setContentsMargins(0, 0, 0, 0)
        self.pushButton_115 = QPushButton(self.off_light_37)
        self.pushButton_115.setObjectName(u"pushButton_115")
        sizePolicy.setHeightForWidth(self.pushButton_115.sizePolicy().hasHeightForWidth())
        self.pushButton_115.setSizePolicy(sizePolicy)
        self.pushButton_115.setFont(font6)
        self.pushButton_115.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_115.setIcon(icon9)
        self.pushButton_115.setIconSize(QSize(45, 45))

        self.horizontalLayout_543.addWidget(self.pushButton_115)

        self.i_o_group_2_switch_8.addWidget(self.off_light_37)

        self.gridLayout_6.addWidget(self.i_o_group_2_switch_8, 3, 3, 1, 1)

        self.i_o_group_2_switch_9 = QStackedWidget(self.i_o_group_2)
        self.i_o_group_2_switch_9.setObjectName(u"i_o_group_2_switch_9")
        sizePolicy.setHeightForWidth(self.i_o_group_2_switch_9.sizePolicy().hasHeightForWidth())
        self.i_o_group_2_switch_9.setSizePolicy(sizePolicy)
        self.i_o_group_2_switch_9.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_38 = QWidget()
        self.on_light_38.setObjectName(u"on_light_38")
        self.horizontalLayout_544 = QHBoxLayout(self.on_light_38)
        self.horizontalLayout_544.setObjectName(u"horizontalLayout_544")
        self.horizontalLayout_544.setContentsMargins(0, 0, 0, 0)
        self.pushButton_116 = QPushButton(self.on_light_38)
        self.pushButton_116.setObjectName(u"pushButton_116")
        sizePolicy.setHeightForWidth(self.pushButton_116.sizePolicy().hasHeightForWidth())
        self.pushButton_116.setSizePolicy(sizePolicy)
        self.pushButton_116.setFont(font6)
        self.pushButton_116.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_116.setIcon(icon7)
        self.pushButton_116.setIconSize(QSize(45, 45))

        self.horizontalLayout_544.addWidget(self.pushButton_116)

        self.i_o_group_2_switch_9.addWidget(self.on_light_38)
        self.off_light_38 = QWidget()
        self.off_light_38.setObjectName(u"off_light_38")
        self.horizontalLayout_545 = QHBoxLayout(self.off_light_38)
        self.horizontalLayout_545.setObjectName(u"horizontalLayout_545")
        self.horizontalLayout_545.setContentsMargins(0, 0, 0, 0)
        self.pushButton_117 = QPushButton(self.off_light_38)
        self.pushButton_117.setObjectName(u"pushButton_117")
        sizePolicy.setHeightForWidth(self.pushButton_117.sizePolicy().hasHeightForWidth())
        self.pushButton_117.setSizePolicy(sizePolicy)
        self.pushButton_117.setFont(font6)
        self.pushButton_117.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_117.setIcon(icon9)
        self.pushButton_117.setIconSize(QSize(45, 45))

        self.horizontalLayout_545.addWidget(self.pushButton_117)

        self.i_o_group_2_switch_9.addWidget(self.off_light_38)

        self.gridLayout_6.addWidget(self.i_o_group_2_switch_9, 4, 1, 1, 1)

        self.i_o_group_2_switch_10 = QStackedWidget(self.i_o_group_2)
        self.i_o_group_2_switch_10.setObjectName(u"i_o_group_2_switch_10")
        sizePolicy.setHeightForWidth(self.i_o_group_2_switch_10.sizePolicy().hasHeightForWidth())
        self.i_o_group_2_switch_10.setSizePolicy(sizePolicy)
        self.i_o_group_2_switch_10.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_39 = QWidget()
        self.on_light_39.setObjectName(u"on_light_39")
        self.horizontalLayout_546 = QHBoxLayout(self.on_light_39)
        self.horizontalLayout_546.setObjectName(u"horizontalLayout_546")
        self.horizontalLayout_546.setContentsMargins(0, 0, 0, 0)
        self.pushButton_118 = QPushButton(self.on_light_39)
        self.pushButton_118.setObjectName(u"pushButton_118")
        sizePolicy.setHeightForWidth(self.pushButton_118.sizePolicy().hasHeightForWidth())
        self.pushButton_118.setSizePolicy(sizePolicy)
        self.pushButton_118.setFont(font6)
        self.pushButton_118.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_118.setIcon(icon7)
        self.pushButton_118.setIconSize(QSize(45, 45))

        self.horizontalLayout_546.addWidget(self.pushButton_118)

        self.i_o_group_2_switch_10.addWidget(self.on_light_39)
        self.off_light_39 = QWidget()
        self.off_light_39.setObjectName(u"off_light_39")
        self.horizontalLayout_547 = QHBoxLayout(self.off_light_39)
        self.horizontalLayout_547.setObjectName(u"horizontalLayout_547")
        self.horizontalLayout_547.setContentsMargins(0, 0, 0, 0)
        self.pushButton_119 = QPushButton(self.off_light_39)
        self.pushButton_119.setObjectName(u"pushButton_119")
        sizePolicy.setHeightForWidth(self.pushButton_119.sizePolicy().hasHeightForWidth())
        self.pushButton_119.setSizePolicy(sizePolicy)
        self.pushButton_119.setFont(font6)
        self.pushButton_119.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_119.setIcon(icon9)
        self.pushButton_119.setIconSize(QSize(45, 45))

        self.horizontalLayout_547.addWidget(self.pushButton_119)

        self.i_o_group_2_switch_10.addWidget(self.off_light_39)

        self.gridLayout_6.addWidget(self.i_o_group_2_switch_10, 4, 3, 1, 1)

        self.i_o_group_2_switch_11 = QStackedWidget(self.i_o_group_2)
        self.i_o_group_2_switch_11.setObjectName(u"i_o_group_2_switch_11")
        sizePolicy.setHeightForWidth(self.i_o_group_2_switch_11.sizePolicy().hasHeightForWidth())
        self.i_o_group_2_switch_11.setSizePolicy(sizePolicy)
        self.i_o_group_2_switch_11.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_40 = QWidget()
        self.on_light_40.setObjectName(u"on_light_40")
        self.horizontalLayout_548 = QHBoxLayout(self.on_light_40)
        self.horizontalLayout_548.setObjectName(u"horizontalLayout_548")
        self.horizontalLayout_548.setContentsMargins(0, 0, 0, 0)
        self.pushButton_120 = QPushButton(self.on_light_40)
        self.pushButton_120.setObjectName(u"pushButton_120")
        sizePolicy.setHeightForWidth(self.pushButton_120.sizePolicy().hasHeightForWidth())
        self.pushButton_120.setSizePolicy(sizePolicy)
        self.pushButton_120.setFont(font6)
        self.pushButton_120.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_120.setIcon(icon7)
        self.pushButton_120.setIconSize(QSize(45, 45))

        self.horizontalLayout_548.addWidget(self.pushButton_120)

        self.i_o_group_2_switch_11.addWidget(self.on_light_40)
        self.off_light_40 = QWidget()
        self.off_light_40.setObjectName(u"off_light_40")
        self.horizontalLayout_549 = QHBoxLayout(self.off_light_40)
        self.horizontalLayout_549.setObjectName(u"horizontalLayout_549")
        self.horizontalLayout_549.setContentsMargins(0, 0, 0, 0)
        self.pushButton_121 = QPushButton(self.off_light_40)
        self.pushButton_121.setObjectName(u"pushButton_121")
        sizePolicy.setHeightForWidth(self.pushButton_121.sizePolicy().hasHeightForWidth())
        self.pushButton_121.setSizePolicy(sizePolicy)
        self.pushButton_121.setFont(font6)
        self.pushButton_121.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_121.setIcon(icon9)
        self.pushButton_121.setIconSize(QSize(45, 45))

        self.horizontalLayout_549.addWidget(self.pushButton_121)

        self.i_o_group_2_switch_11.addWidget(self.off_light_40)

        self.gridLayout_6.addWidget(self.i_o_group_2_switch_11, 5, 1, 1, 1)

        self.i_o_group_2_switch_12 = QStackedWidget(self.i_o_group_2)
        self.i_o_group_2_switch_12.setObjectName(u"i_o_group_2_switch_12")
        sizePolicy.setHeightForWidth(self.i_o_group_2_switch_12.sizePolicy().hasHeightForWidth())
        self.i_o_group_2_switch_12.setSizePolicy(sizePolicy)
        self.i_o_group_2_switch_12.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_41 = QWidget()
        self.on_light_41.setObjectName(u"on_light_41")
        self.horizontalLayout_550 = QHBoxLayout(self.on_light_41)
        self.horizontalLayout_550.setObjectName(u"horizontalLayout_550")
        self.horizontalLayout_550.setContentsMargins(0, 0, 0, 0)
        self.pushButton_122 = QPushButton(self.on_light_41)
        self.pushButton_122.setObjectName(u"pushButton_122")
        sizePolicy.setHeightForWidth(self.pushButton_122.sizePolicy().hasHeightForWidth())
        self.pushButton_122.setSizePolicy(sizePolicy)
        self.pushButton_122.setFont(font6)
        self.pushButton_122.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_122.setIcon(icon7)
        self.pushButton_122.setIconSize(QSize(45, 45))

        self.horizontalLayout_550.addWidget(self.pushButton_122)

        self.i_o_group_2_switch_12.addWidget(self.on_light_41)
        self.off_light_41 = QWidget()
        self.off_light_41.setObjectName(u"off_light_41")
        self.horizontalLayout_551 = QHBoxLayout(self.off_light_41)
        self.horizontalLayout_551.setObjectName(u"horizontalLayout_551")
        self.horizontalLayout_551.setContentsMargins(0, 0, 0, 0)
        self.pushButton_123 = QPushButton(self.off_light_41)
        self.pushButton_123.setObjectName(u"pushButton_123")
        sizePolicy.setHeightForWidth(self.pushButton_123.sizePolicy().hasHeightForWidth())
        self.pushButton_123.setSizePolicy(sizePolicy)
        self.pushButton_123.setFont(font6)
        self.pushButton_123.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_123.setIcon(icon9)
        self.pushButton_123.setIconSize(QSize(45, 45))

        self.horizontalLayout_551.addWidget(self.pushButton_123)

        self.i_o_group_2_switch_12.addWidget(self.off_light_41)

        self.gridLayout_6.addWidget(self.i_o_group_2_switch_12, 5, 3, 1, 1)

        self.dq_name_1 = QLabel(self.i_o_group_2)
        self.dq_name_1.setObjectName(u"dq_name_1")
        self.dq_name_1.setFont(font22)

        self.gridLayout_6.addWidget(self.dq_name_1, 0, 0, 1, 1)

        self.i_o_group_2_switch_13 = QStackedWidget(self.i_o_group_2)
        self.i_o_group_2_switch_13.setObjectName(u"i_o_group_2_switch_13")
        sizePolicy.setHeightForWidth(self.i_o_group_2_switch_13.sizePolicy().hasHeightForWidth())
        self.i_o_group_2_switch_13.setSizePolicy(sizePolicy)
        self.i_o_group_2_switch_13.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_42 = QWidget()
        self.on_light_42.setObjectName(u"on_light_42")
        self.horizontalLayout_552 = QHBoxLayout(self.on_light_42)
        self.horizontalLayout_552.setObjectName(u"horizontalLayout_552")
        self.horizontalLayout_552.setContentsMargins(0, 0, 0, 0)
        self.pushButton_124 = QPushButton(self.on_light_42)
        self.pushButton_124.setObjectName(u"pushButton_124")
        sizePolicy.setHeightForWidth(self.pushButton_124.sizePolicy().hasHeightForWidth())
        self.pushButton_124.setSizePolicy(sizePolicy)
        self.pushButton_124.setFont(font6)
        self.pushButton_124.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_124.setIcon(icon7)
        self.pushButton_124.setIconSize(QSize(45, 45))

        self.horizontalLayout_552.addWidget(self.pushButton_124)

        self.i_o_group_2_switch_13.addWidget(self.on_light_42)
        self.off_light_42 = QWidget()
        self.off_light_42.setObjectName(u"off_light_42")
        self.horizontalLayout_553 = QHBoxLayout(self.off_light_42)
        self.horizontalLayout_553.setObjectName(u"horizontalLayout_553")
        self.horizontalLayout_553.setContentsMargins(0, 0, 0, 0)
        self.pushButton_125 = QPushButton(self.off_light_42)
        self.pushButton_125.setObjectName(u"pushButton_125")
        sizePolicy.setHeightForWidth(self.pushButton_125.sizePolicy().hasHeightForWidth())
        self.pushButton_125.setSizePolicy(sizePolicy)
        self.pushButton_125.setFont(font6)
        self.pushButton_125.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_125.setIcon(icon9)
        self.pushButton_125.setIconSize(QSize(45, 45))

        self.horizontalLayout_553.addWidget(self.pushButton_125)

        self.i_o_group_2_switch_13.addWidget(self.off_light_42)

        self.gridLayout_6.addWidget(self.i_o_group_2_switch_13, 6, 1, 1, 1)

        self.dq_name_2 = QLabel(self.i_o_group_2)
        self.dq_name_2.setObjectName(u"dq_name_2")
        self.dq_name_2.setFont(font22)

        self.gridLayout_6.addWidget(self.dq_name_2, 0, 2, 1, 1)

        self.i_o_group_2_switch_15 = QStackedWidget(self.i_o_group_2)
        self.i_o_group_2_switch_15.setObjectName(u"i_o_group_2_switch_15")
        sizePolicy.setHeightForWidth(self.i_o_group_2_switch_15.sizePolicy().hasHeightForWidth())
        self.i_o_group_2_switch_15.setSizePolicy(sizePolicy)
        self.i_o_group_2_switch_15.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_44 = QWidget()
        self.on_light_44.setObjectName(u"on_light_44")
        self.horizontalLayout_556 = QHBoxLayout(self.on_light_44)
        self.horizontalLayout_556.setObjectName(u"horizontalLayout_556")
        self.horizontalLayout_556.setContentsMargins(0, 0, 0, 0)
        self.pushButton_128 = QPushButton(self.on_light_44)
        self.pushButton_128.setObjectName(u"pushButton_128")
        sizePolicy.setHeightForWidth(self.pushButton_128.sizePolicy().hasHeightForWidth())
        self.pushButton_128.setSizePolicy(sizePolicy)
        self.pushButton_128.setFont(font6)
        self.pushButton_128.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_128.setIcon(icon7)
        self.pushButton_128.setIconSize(QSize(45, 45))

        self.horizontalLayout_556.addWidget(self.pushButton_128)

        self.i_o_group_2_switch_15.addWidget(self.on_light_44)
        self.off_light_44 = QWidget()
        self.off_light_44.setObjectName(u"off_light_44")
        self.horizontalLayout_557 = QHBoxLayout(self.off_light_44)
        self.horizontalLayout_557.setObjectName(u"horizontalLayout_557")
        self.horizontalLayout_557.setContentsMargins(0, 0, 0, 0)
        self.pushButton_129 = QPushButton(self.off_light_44)
        self.pushButton_129.setObjectName(u"pushButton_129")
        sizePolicy.setHeightForWidth(self.pushButton_129.sizePolicy().hasHeightForWidth())
        self.pushButton_129.setSizePolicy(sizePolicy)
        self.pushButton_129.setFont(font6)
        self.pushButton_129.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_129.setIcon(icon9)
        self.pushButton_129.setIconSize(QSize(45, 45))

        self.horizontalLayout_557.addWidget(self.pushButton_129)

        self.i_o_group_2_switch_15.addWidget(self.off_light_44)

        self.gridLayout_6.addWidget(self.i_o_group_2_switch_15, 7, 1, 1, 1)

        self.dq_name_3 = QLabel(self.i_o_group_2)
        self.dq_name_3.setObjectName(u"dq_name_3")
        self.dq_name_3.setFont(font22)

        self.gridLayout_6.addWidget(self.dq_name_3, 1, 0, 1, 1)

        self.dq_name_4 = QLabel(self.i_o_group_2)
        self.dq_name_4.setObjectName(u"dq_name_4")
        self.dq_name_4.setFont(font22)

        self.gridLayout_6.addWidget(self.dq_name_4, 1, 2, 1, 1)

        self.dq_name_6 = QLabel(self.i_o_group_2)
        self.dq_name_6.setObjectName(u"dq_name_6")
        self.dq_name_6.setFont(font22)

        self.gridLayout_6.addWidget(self.dq_name_6, 2, 2, 1, 1)

        self.dq_name_5 = QLabel(self.i_o_group_2)
        self.dq_name_5.setObjectName(u"dq_name_5")
        self.dq_name_5.setFont(font22)

        self.gridLayout_6.addWidget(self.dq_name_5, 2, 0, 1, 1)

        self.dq_name_7 = QLabel(self.i_o_group_2)
        self.dq_name_7.setObjectName(u"dq_name_7")
        self.dq_name_7.setFont(font22)

        self.gridLayout_6.addWidget(self.dq_name_7, 3, 0, 1, 1)

        self.dq_name_8 = QLabel(self.i_o_group_2)
        self.dq_name_8.setObjectName(u"dq_name_8")
        self.dq_name_8.setFont(font22)

        self.gridLayout_6.addWidget(self.dq_name_8, 3, 2, 1, 1)

        self.dq_name_9 = QLabel(self.i_o_group_2)
        self.dq_name_9.setObjectName(u"dq_name_9")
        self.dq_name_9.setFont(font22)

        self.gridLayout_6.addWidget(self.dq_name_9, 4, 0, 1, 1)

        self.dq_name_10 = QLabel(self.i_o_group_2)
        self.dq_name_10.setObjectName(u"dq_name_10")
        self.dq_name_10.setFont(font22)

        self.gridLayout_6.addWidget(self.dq_name_10, 4, 2, 1, 1)

        self.dq_name_11 = QLabel(self.i_o_group_2)
        self.dq_name_11.setObjectName(u"dq_name_11")
        self.dq_name_11.setFont(font22)

        self.gridLayout_6.addWidget(self.dq_name_11, 5, 0, 1, 1)

        self.dq_name_13 = QLabel(self.i_o_group_2)
        self.dq_name_13.setObjectName(u"dq_name_13")
        self.dq_name_13.setFont(font22)

        self.gridLayout_6.addWidget(self.dq_name_13, 6, 0, 1, 1)

        self.dq_name_12 = QLabel(self.i_o_group_2)
        self.dq_name_12.setObjectName(u"dq_name_12")
        self.dq_name_12.setFont(font22)

        self.gridLayout_6.addWidget(self.dq_name_12, 5, 2, 1, 1)

        self.dq_name_14 = QLabel(self.i_o_group_2)
        self.dq_name_14.setObjectName(u"dq_name_14")
        self.dq_name_14.setFont(font22)

        self.gridLayout_6.addWidget(self.dq_name_14, 6, 2, 1, 1)

        self.dq_name_15 = QLabel(self.i_o_group_2)
        self.dq_name_15.setObjectName(u"dq_name_15")
        self.dq_name_15.setFont(font22)

        self.gridLayout_6.addWidget(self.dq_name_15, 7, 0, 1, 1)

        self.i_o_group_2_switch_14 = QStackedWidget(self.i_o_group_2)
        self.i_o_group_2_switch_14.setObjectName(u"i_o_group_2_switch_14")
        sizePolicy.setHeightForWidth(self.i_o_group_2_switch_14.sizePolicy().hasHeightForWidth())
        self.i_o_group_2_switch_14.setSizePolicy(sizePolicy)
        self.i_o_group_2_switch_14.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_43 = QWidget()
        self.on_light_43.setObjectName(u"on_light_43")
        self.horizontalLayout_554 = QHBoxLayout(self.on_light_43)
        self.horizontalLayout_554.setObjectName(u"horizontalLayout_554")
        self.horizontalLayout_554.setContentsMargins(0, 0, 0, 0)
        self.pushButton_126 = QPushButton(self.on_light_43)
        self.pushButton_126.setObjectName(u"pushButton_126")
        sizePolicy.setHeightForWidth(self.pushButton_126.sizePolicy().hasHeightForWidth())
        self.pushButton_126.setSizePolicy(sizePolicy)
        self.pushButton_126.setFont(font6)
        self.pushButton_126.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_126.setIcon(icon7)
        self.pushButton_126.setIconSize(QSize(45, 45))

        self.horizontalLayout_554.addWidget(self.pushButton_126)

        self.i_o_group_2_switch_14.addWidget(self.on_light_43)
        self.off_light_43 = QWidget()
        self.off_light_43.setObjectName(u"off_light_43")
        self.horizontalLayout_555 = QHBoxLayout(self.off_light_43)
        self.horizontalLayout_555.setObjectName(u"horizontalLayout_555")
        self.horizontalLayout_555.setContentsMargins(0, 0, 0, 0)
        self.pushButton_127 = QPushButton(self.off_light_43)
        self.pushButton_127.setObjectName(u"pushButton_127")
        sizePolicy.setHeightForWidth(self.pushButton_127.sizePolicy().hasHeightForWidth())
        self.pushButton_127.setSizePolicy(sizePolicy)
        self.pushButton_127.setFont(font6)
        self.pushButton_127.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_127.setIcon(icon9)
        self.pushButton_127.setIconSize(QSize(45, 45))

        self.horizontalLayout_555.addWidget(self.pushButton_127)

        self.i_o_group_2_switch_14.addWidget(self.off_light_43)

        self.gridLayout_6.addWidget(self.i_o_group_2_switch_14, 6, 3, 1, 1)

        self.i_o_group_2_switch_3 = QStackedWidget(self.i_o_group_2)
        self.i_o_group_2_switch_3.setObjectName(u"i_o_group_2_switch_3")
        sizePolicy.setHeightForWidth(self.i_o_group_2_switch_3.sizePolicy().hasHeightForWidth())
        self.i_o_group_2_switch_3.setSizePolicy(sizePolicy)
        self.i_o_group_2_switch_3.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_32 = QWidget()
        self.on_light_32.setObjectName(u"on_light_32")
        self.horizontalLayout_532 = QHBoxLayout(self.on_light_32)
        self.horizontalLayout_532.setObjectName(u"horizontalLayout_532")
        self.horizontalLayout_532.setContentsMargins(0, 0, 0, 0)
        self.pushButton_104 = QPushButton(self.on_light_32)
        self.pushButton_104.setObjectName(u"pushButton_104")
        sizePolicy.setHeightForWidth(self.pushButton_104.sizePolicy().hasHeightForWidth())
        self.pushButton_104.setSizePolicy(sizePolicy)
        self.pushButton_104.setFont(font6)
        self.pushButton_104.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_104.setIcon(icon7)
        self.pushButton_104.setIconSize(QSize(45, 45))

        self.horizontalLayout_532.addWidget(self.pushButton_104)

        self.i_o_group_2_switch_3.addWidget(self.on_light_32)
        self.off_light_32 = QWidget()
        self.off_light_32.setObjectName(u"off_light_32")
        self.horizontalLayout_533 = QHBoxLayout(self.off_light_32)
        self.horizontalLayout_533.setObjectName(u"horizontalLayout_533")
        self.horizontalLayout_533.setContentsMargins(0, 0, 0, 0)
        self.pushButton_105 = QPushButton(self.off_light_32)
        self.pushButton_105.setObjectName(u"pushButton_105")
        sizePolicy.setHeightForWidth(self.pushButton_105.sizePolicy().hasHeightForWidth())
        self.pushButton_105.setSizePolicy(sizePolicy)
        self.pushButton_105.setFont(font6)
        self.pushButton_105.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_105.setIcon(icon9)
        self.pushButton_105.setIconSize(QSize(45, 45))

        self.horizontalLayout_533.addWidget(self.pushButton_105)

        self.i_o_group_2_switch_3.addWidget(self.off_light_32)

        self.gridLayout_6.addWidget(self.i_o_group_2_switch_3, 1, 1, 1, 1)

        self.i_o_group_2_switch_4 = QStackedWidget(self.i_o_group_2)
        self.i_o_group_2_switch_4.setObjectName(u"i_o_group_2_switch_4")
        sizePolicy.setHeightForWidth(self.i_o_group_2_switch_4.sizePolicy().hasHeightForWidth())
        self.i_o_group_2_switch_4.setSizePolicy(sizePolicy)
        self.i_o_group_2_switch_4.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_33 = QWidget()
        self.on_light_33.setObjectName(u"on_light_33")
        self.horizontalLayout_534 = QHBoxLayout(self.on_light_33)
        self.horizontalLayout_534.setObjectName(u"horizontalLayout_534")
        self.horizontalLayout_534.setContentsMargins(0, 0, 0, 0)
        self.pushButton_106 = QPushButton(self.on_light_33)
        self.pushButton_106.setObjectName(u"pushButton_106")
        sizePolicy.setHeightForWidth(self.pushButton_106.sizePolicy().hasHeightForWidth())
        self.pushButton_106.setSizePolicy(sizePolicy)
        self.pushButton_106.setFont(font6)
        self.pushButton_106.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_106.setIcon(icon7)
        self.pushButton_106.setIconSize(QSize(45, 45))

        self.horizontalLayout_534.addWidget(self.pushButton_106)

        self.i_o_group_2_switch_4.addWidget(self.on_light_33)
        self.off_light_33 = QWidget()
        self.off_light_33.setObjectName(u"off_light_33")
        self.horizontalLayout_535 = QHBoxLayout(self.off_light_33)
        self.horizontalLayout_535.setObjectName(u"horizontalLayout_535")
        self.horizontalLayout_535.setContentsMargins(0, 0, 0, 0)
        self.pushButton_107 = QPushButton(self.off_light_33)
        self.pushButton_107.setObjectName(u"pushButton_107")
        sizePolicy.setHeightForWidth(self.pushButton_107.sizePolicy().hasHeightForWidth())
        self.pushButton_107.setSizePolicy(sizePolicy)
        self.pushButton_107.setFont(font6)
        self.pushButton_107.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_107.setIcon(icon9)
        self.pushButton_107.setIconSize(QSize(45, 45))

        self.horizontalLayout_535.addWidget(self.pushButton_107)

        self.i_o_group_2_switch_4.addWidget(self.off_light_33)

        self.gridLayout_6.addWidget(self.i_o_group_2_switch_4, 1, 3, 1, 1)

        self.i_o_group_2_switch_1 = QStackedWidget(self.i_o_group_2)
        self.i_o_group_2_switch_1.setObjectName(u"i_o_group_2_switch_1")
        sizePolicy.setHeightForWidth(self.i_o_group_2_switch_1.sizePolicy().hasHeightForWidth())
        self.i_o_group_2_switch_1.setSizePolicy(sizePolicy)
        self.i_o_group_2_switch_1.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_16 = QWidget()
        self.on_light_16.setObjectName(u"on_light_16")
        self.horizontalLayout_500 = QHBoxLayout(self.on_light_16)
        self.horizontalLayout_500.setObjectName(u"horizontalLayout_500")
        self.horizontalLayout_500.setContentsMargins(0, 0, 0, 0)
        self.pushButton_72 = QPushButton(self.on_light_16)
        self.pushButton_72.setObjectName(u"pushButton_72")
        sizePolicy.setHeightForWidth(self.pushButton_72.sizePolicy().hasHeightForWidth())
        self.pushButton_72.setSizePolicy(sizePolicy)
        self.pushButton_72.setFont(font6)
        self.pushButton_72.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_72.setIcon(icon7)
        self.pushButton_72.setIconSize(QSize(45, 45))

        self.horizontalLayout_500.addWidget(self.pushButton_72)

        self.i_o_group_2_switch_1.addWidget(self.on_light_16)
        self.off_light_16 = QWidget()
        self.off_light_16.setObjectName(u"off_light_16")
        self.horizontalLayout_501 = QHBoxLayout(self.off_light_16)
        self.horizontalLayout_501.setObjectName(u"horizontalLayout_501")
        self.horizontalLayout_501.setContentsMargins(0, 0, 0, 0)
        self.pushButton_73 = QPushButton(self.off_light_16)
        self.pushButton_73.setObjectName(u"pushButton_73")
        sizePolicy.setHeightForWidth(self.pushButton_73.sizePolicy().hasHeightForWidth())
        self.pushButton_73.setSizePolicy(sizePolicy)
        self.pushButton_73.setFont(font6)
        self.pushButton_73.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_73.setIcon(icon9)
        self.pushButton_73.setIconSize(QSize(45, 45))

        self.horizontalLayout_501.addWidget(self.pushButton_73)

        self.i_o_group_2_switch_1.addWidget(self.off_light_16)

        self.gridLayout_6.addWidget(self.i_o_group_2_switch_1, 0, 1, 1, 1)

        self.i_o_group_2_switch_2 = QStackedWidget(self.i_o_group_2)
        self.i_o_group_2_switch_2.setObjectName(u"i_o_group_2_switch_2")
        sizePolicy.setHeightForWidth(self.i_o_group_2_switch_2.sizePolicy().hasHeightForWidth())
        self.i_o_group_2_switch_2.setSizePolicy(sizePolicy)
        self.i_o_group_2_switch_2.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"}")
        self.on_light_31 = QWidget()
        self.on_light_31.setObjectName(u"on_light_31")
        self.horizontalLayout_530 = QHBoxLayout(self.on_light_31)
        self.horizontalLayout_530.setObjectName(u"horizontalLayout_530")
        self.horizontalLayout_530.setContentsMargins(0, 0, 0, 0)
        self.pushButton_102 = QPushButton(self.on_light_31)
        self.pushButton_102.setObjectName(u"pushButton_102")
        sizePolicy.setHeightForWidth(self.pushButton_102.sizePolicy().hasHeightForWidth())
        self.pushButton_102.setSizePolicy(sizePolicy)
        self.pushButton_102.setFont(font6)
        self.pushButton_102.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_102.setIcon(icon7)
        self.pushButton_102.setIconSize(QSize(45, 45))

        self.horizontalLayout_530.addWidget(self.pushButton_102)

        self.i_o_group_2_switch_2.addWidget(self.on_light_31)
        self.off_light_31 = QWidget()
        self.off_light_31.setObjectName(u"off_light_31")
        self.horizontalLayout_531 = QHBoxLayout(self.off_light_31)
        self.horizontalLayout_531.setObjectName(u"horizontalLayout_531")
        self.horizontalLayout_531.setContentsMargins(0, 0, 0, 0)
        self.pushButton_103 = QPushButton(self.off_light_31)
        self.pushButton_103.setObjectName(u"pushButton_103")
        sizePolicy.setHeightForWidth(self.pushButton_103.sizePolicy().hasHeightForWidth())
        self.pushButton_103.setSizePolicy(sizePolicy)
        self.pushButton_103.setFont(font6)
        self.pushButton_103.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 20px;")
        self.pushButton_103.setIcon(icon9)
        self.pushButton_103.setIconSize(QSize(45, 45))

        self.horizontalLayout_531.addWidget(self.pushButton_103)

        self.i_o_group_2_switch_2.addWidget(self.off_light_31)

        self.gridLayout_6.addWidget(self.i_o_group_2_switch_2, 0, 3, 1, 1)

        self.gridLayout_6.setColumnStretch(1, 1)
        self.gridLayout_6.setColumnStretch(3, 1)

        self.horizontalLayout_24.addWidget(self.i_o_group_2)

        self.i_o_group_3 = QGroupBox(self.widget_26)
        self.i_o_group_3.setObjectName(u"i_o_group_3")
        self.i_o_group_3.setFont(font20)
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
        self.gridLayout_5.setContentsMargins(10, 10, 10, 10)
        self.t0_value = QDoubleSpinBox(self.i_o_group_3)
        self.t0_value.setObjectName(u"t0_value")
        sizePolicy.setHeightForWidth(self.t0_value.sizePolicy().hasHeightForWidth())
        self.t0_value.setSizePolicy(sizePolicy)
        self.t0_value.setFont(font2)
        self.t0_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.t0_value.setAlignment(Qt.AlignCenter)
        self.t0_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t0_value.setDecimals(1)
        self.t0_value.setMinimum(-10.000000000000000)
        self.t0_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.t0_value, 0, 1, 1, 1)

        self.ai_name_1 = QLabel(self.i_o_group_3)
        self.ai_name_1.setObjectName(u"ai_name_1")
        self.ai_name_1.setFont(font22)

        self.gridLayout_5.addWidget(self.ai_name_1, 0, 0, 1, 1)

        self.t1_1_value = QDoubleSpinBox(self.i_o_group_3)
        self.t1_1_value.setObjectName(u"t1_1_value")
        sizePolicy.setHeightForWidth(self.t1_1_value.sizePolicy().hasHeightForWidth())
        self.t1_1_value.setSizePolicy(sizePolicy)
        self.t1_1_value.setFont(font2)
        self.t1_1_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.t1_1_value.setAlignment(Qt.AlignCenter)
        self.t1_1_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t1_1_value.setDecimals(1)
        self.t1_1_value.setMinimum(-10.000000000000000)
        self.t1_1_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.t1_1_value, 0, 3, 1, 1)

        self.ai_name_15 = QLabel(self.i_o_group_3)
        self.ai_name_15.setObjectName(u"ai_name_15")
        self.ai_name_15.setFont(font22)

        self.gridLayout_5.addWidget(self.ai_name_15, 7, 2, 1, 1)

        self.ai_name_14 = QLabel(self.i_o_group_3)
        self.ai_name_14.setObjectName(u"ai_name_14")
        self.ai_name_14.setFont(font22)

        self.gridLayout_5.addWidget(self.ai_name_14, 6, 2, 1, 1)

        self.ai_name_12 = QLabel(self.i_o_group_3)
        self.ai_name_12.setObjectName(u"ai_name_12")
        self.ai_name_12.setFont(font22)

        self.gridLayout_5.addWidget(self.ai_name_12, 7, 0, 1, 1)

        self.ai_name_13 = QLabel(self.i_o_group_3)
        self.ai_name_13.setObjectName(u"ai_name_13")
        self.ai_name_13.setFont(font22)

        self.gridLayout_5.addWidget(self.ai_name_13, 9, 0, 1, 1)

        self.ai_name_16 = QLabel(self.i_o_group_3)
        self.ai_name_16.setObjectName(u"ai_name_16")
        self.ai_name_16.setFont(font22)

        self.gridLayout_5.addWidget(self.ai_name_16, 9, 2, 1, 1)

        self.ai_name_4 = QLabel(self.i_o_group_3)
        self.ai_name_4.setObjectName(u"ai_name_4")
        self.ai_name_4.setFont(font22)

        self.gridLayout_5.addWidget(self.ai_name_4, 1, 2, 1, 1)

        self.ai_name_3 = QLabel(self.i_o_group_3)
        self.ai_name_3.setObjectName(u"ai_name_3")
        self.ai_name_3.setFont(font22)

        self.gridLayout_5.addWidget(self.ai_name_3, 1, 0, 1, 1)

        self.ai_name_5 = QLabel(self.i_o_group_3)
        self.ai_name_5.setObjectName(u"ai_name_5")
        self.ai_name_5.setFont(font22)

        self.gridLayout_5.addWidget(self.ai_name_5, 2, 0, 1, 1)

        self.ai_name_2 = QLabel(self.i_o_group_3)
        self.ai_name_2.setObjectName(u"ai_name_2")
        self.ai_name_2.setFont(font22)

        self.gridLayout_5.addWidget(self.ai_name_2, 0, 2, 1, 1)

        self.ai_name_6 = QLabel(self.i_o_group_3)
        self.ai_name_6.setObjectName(u"ai_name_6")
        self.ai_name_6.setFont(font22)

        self.gridLayout_5.addWidget(self.ai_name_6, 2, 2, 1, 1)

        self.ai_name_7 = QLabel(self.i_o_group_3)
        self.ai_name_7.setObjectName(u"ai_name_7")
        self.ai_name_7.setFont(font22)

        self.gridLayout_5.addWidget(self.ai_name_7, 3, 0, 1, 1)

        self.ai_name_8 = QLabel(self.i_o_group_3)
        self.ai_name_8.setObjectName(u"ai_name_8")
        self.ai_name_8.setFont(font22)

        self.gridLayout_5.addWidget(self.ai_name_8, 3, 2, 1, 1)

        self.ai_name_9 = QLabel(self.i_o_group_3)
        self.ai_name_9.setObjectName(u"ai_name_9")
        self.ai_name_9.setFont(font22)

        self.gridLayout_5.addWidget(self.ai_name_9, 4, 0, 1, 1)

        self.ai_name_10 = QLabel(self.i_o_group_3)
        self.ai_name_10.setObjectName(u"ai_name_10")
        self.ai_name_10.setFont(font22)

        self.gridLayout_5.addWidget(self.ai_name_10, 4, 2, 1, 1)

        self.ai_name_11 = QLabel(self.i_o_group_3)
        self.ai_name_11.setObjectName(u"ai_name_11")
        self.ai_name_11.setFont(font22)

        self.gridLayout_5.addWidget(self.ai_name_11, 6, 0, 1, 1)

        self.t1_2_value = QDoubleSpinBox(self.i_o_group_3)
        self.t1_2_value.setObjectName(u"t1_2_value")
        sizePolicy.setHeightForWidth(self.t1_2_value.sizePolicy().hasHeightForWidth())
        self.t1_2_value.setSizePolicy(sizePolicy)
        self.t1_2_value.setFont(font2)
        self.t1_2_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.t1_2_value.setAlignment(Qt.AlignCenter)
        self.t1_2_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t1_2_value.setDecimals(1)
        self.t1_2_value.setMinimum(-10.000000000000000)
        self.t1_2_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.t1_2_value, 1, 1, 1, 1)

        self.t1_3_value = QDoubleSpinBox(self.i_o_group_3)
        self.t1_3_value.setObjectName(u"t1_3_value")
        sizePolicy.setHeightForWidth(self.t1_3_value.sizePolicy().hasHeightForWidth())
        self.t1_3_value.setSizePolicy(sizePolicy)
        self.t1_3_value.setFont(font2)
        self.t1_3_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.t1_3_value.setAlignment(Qt.AlignCenter)
        self.t1_3_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t1_3_value.setDecimals(1)
        self.t1_3_value.setMinimum(-10.000000000000000)
        self.t1_3_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.t1_3_value, 1, 3, 1, 1)

        self.t2_1_value = QDoubleSpinBox(self.i_o_group_3)
        self.t2_1_value.setObjectName(u"t2_1_value")
        sizePolicy.setHeightForWidth(self.t2_1_value.sizePolicy().hasHeightForWidth())
        self.t2_1_value.setSizePolicy(sizePolicy)
        self.t2_1_value.setFont(font2)
        self.t2_1_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.t2_1_value.setAlignment(Qt.AlignCenter)
        self.t2_1_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t2_1_value.setDecimals(1)
        self.t2_1_value.setMinimum(-10.000000000000000)
        self.t2_1_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.t2_1_value, 2, 1, 1, 1)

        self.t2_2_value = QDoubleSpinBox(self.i_o_group_3)
        self.t2_2_value.setObjectName(u"t2_2_value")
        sizePolicy.setHeightForWidth(self.t2_2_value.sizePolicy().hasHeightForWidth())
        self.t2_2_value.setSizePolicy(sizePolicy)
        self.t2_2_value.setFont(font2)
        self.t2_2_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.t2_2_value.setAlignment(Qt.AlignCenter)
        self.t2_2_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t2_2_value.setDecimals(1)
        self.t2_2_value.setMinimum(-10.000000000000000)
        self.t2_2_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.t2_2_value, 2, 3, 1, 1)

        self.t2_3_value = QDoubleSpinBox(self.i_o_group_3)
        self.t2_3_value.setObjectName(u"t2_3_value")
        sizePolicy.setHeightForWidth(self.t2_3_value.sizePolicy().hasHeightForWidth())
        self.t2_3_value.setSizePolicy(sizePolicy)
        self.t2_3_value.setFont(font2)
        self.t2_3_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.t2_3_value.setAlignment(Qt.AlignCenter)
        self.t2_3_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t2_3_value.setDecimals(1)
        self.t2_3_value.setMinimum(-10.000000000000000)
        self.t2_3_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.t2_3_value, 3, 1, 1, 1)

        self.t3_1_value = QDoubleSpinBox(self.i_o_group_3)
        self.t3_1_value.setObjectName(u"t3_1_value")
        sizePolicy.setHeightForWidth(self.t3_1_value.sizePolicy().hasHeightForWidth())
        self.t3_1_value.setSizePolicy(sizePolicy)
        self.t3_1_value.setFont(font2)
        self.t3_1_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.t3_1_value.setAlignment(Qt.AlignCenter)
        self.t3_1_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t3_1_value.setDecimals(1)
        self.t3_1_value.setMinimum(-10.000000000000000)
        self.t3_1_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.t3_1_value, 3, 3, 1, 1)

        self.t3_2_value = QDoubleSpinBox(self.i_o_group_3)
        self.t3_2_value.setObjectName(u"t3_2_value")
        sizePolicy.setHeightForWidth(self.t3_2_value.sizePolicy().hasHeightForWidth())
        self.t3_2_value.setSizePolicy(sizePolicy)
        self.t3_2_value.setFont(font2)
        self.t3_2_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.t3_2_value.setAlignment(Qt.AlignCenter)
        self.t3_2_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t3_2_value.setDecimals(1)
        self.t3_2_value.setMinimum(-10.000000000000000)
        self.t3_2_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.t3_2_value, 4, 1, 1, 1)

        self.t3_3_value = QDoubleSpinBox(self.i_o_group_3)
        self.t3_3_value.setObjectName(u"t3_3_value")
        sizePolicy.setHeightForWidth(self.t3_3_value.sizePolicy().hasHeightForWidth())
        self.t3_3_value.setSizePolicy(sizePolicy)
        self.t3_3_value.setFont(font2)
        self.t3_3_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.t3_3_value.setAlignment(Qt.AlignCenter)
        self.t3_3_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t3_3_value.setDecimals(1)
        self.t3_3_value.setMinimum(-10.000000000000000)
        self.t3_3_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.t3_3_value, 4, 3, 1, 1)

        self.p1_value = QDoubleSpinBox(self.i_o_group_3)
        self.p1_value.setObjectName(u"p1_value")
        sizePolicy.setHeightForWidth(self.p1_value.sizePolicy().hasHeightForWidth())
        self.p1_value.setSizePolicy(sizePolicy)
        self.p1_value.setFont(font2)
        self.p1_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.p1_value.setAlignment(Qt.AlignCenter)
        self.p1_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.p1_value.setDecimals(1)
        self.p1_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.p1_value, 6, 1, 1, 1)

        self.p2_value = QDoubleSpinBox(self.i_o_group_3)
        self.p2_value.setObjectName(u"p2_value")
        sizePolicy.setHeightForWidth(self.p2_value.sizePolicy().hasHeightForWidth())
        self.p2_value.setSizePolicy(sizePolicy)
        self.p2_value.setFont(font2)
        self.p2_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.p2_value.setAlignment(Qt.AlignCenter)
        self.p2_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.p2_value.setDecimals(1)
        self.p2_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.p2_value, 7, 1, 1, 1)

        self.p3_value = QDoubleSpinBox(self.i_o_group_3)
        self.p3_value.setObjectName(u"p3_value")
        sizePolicy.setHeightForWidth(self.p3_value.sizePolicy().hasHeightForWidth())
        self.p3_value.setSizePolicy(sizePolicy)
        self.p3_value.setFont(font2)
        self.p3_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.p3_value.setAlignment(Qt.AlignCenter)
        self.p3_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.p3_value.setDecimals(1)
        self.p3_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.p3_value, 9, 1, 1, 1)

        self.fp1_value = QDoubleSpinBox(self.i_o_group_3)
        self.fp1_value.setObjectName(u"fp1_value")
        sizePolicy.setHeightForWidth(self.fp1_value.sizePolicy().hasHeightForWidth())
        self.fp1_value.setSizePolicy(sizePolicy)
        self.fp1_value.setFont(font2)
        self.fp1_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.fp1_value.setAlignment(Qt.AlignCenter)
        self.fp1_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.fp1_value.setDecimals(1)
        self.fp1_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.fp1_value, 6, 3, 1, 1)

        self.fp2_value = QDoubleSpinBox(self.i_o_group_3)
        self.fp2_value.setObjectName(u"fp2_value")
        sizePolicy.setHeightForWidth(self.fp2_value.sizePolicy().hasHeightForWidth())
        self.fp2_value.setSizePolicy(sizePolicy)
        self.fp2_value.setFont(font2)
        self.fp2_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.fp2_value.setAlignment(Qt.AlignCenter)
        self.fp2_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.fp2_value.setDecimals(1)
        self.fp2_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.fp2_value, 7, 3, 1, 1)

        self.fp3_value = QDoubleSpinBox(self.i_o_group_3)
        self.fp3_value.setObjectName(u"fp3_value")
        sizePolicy.setHeightForWidth(self.fp3_value.sizePolicy().hasHeightForWidth())
        self.fp3_value.setSizePolicy(sizePolicy)
        self.fp3_value.setFont(font2)
        self.fp3_value.setStyleSheet(u"border: 3px solid #E5E5E5; \n"
"border-radius: 20px;\n"
"color: #10B981;")
        self.fp3_value.setAlignment(Qt.AlignCenter)
        self.fp3_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.fp3_value.setDecimals(1)
        self.fp3_value.setMaximum(999.899999999999977)

        self.gridLayout_5.addWidget(self.fp3_value, 9, 3, 1, 1)

        self.gridLayout_5.setColumnStretch(1, 1)
        self.gridLayout_5.setColumnStretch(3, 1)

        self.horizontalLayout_24.addWidget(self.i_o_group_3)

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
        self.previus_group_page_btn_2 = QPushButton(self.widget_30)
        self.previus_group_page_btn_2.setObjectName(u"previus_group_page_btn_2")
        sizePolicy.setHeightForWidth(self.previus_group_page_btn_2.sizePolicy().hasHeightForWidth())
        self.previus_group_page_btn_2.setSizePolicy(sizePolicy)
        self.previus_group_page_btn_2.setMaximumSize(QSize(16777215, 150))
        self.previus_group_page_btn_2.setFont(font8)
        self.previus_group_page_btn_2.setStyleSheet(u"QPushButton{\n"
"	image: url(:/newPrefix/arrow-alt-circle-left.png);\n"
"}\n"
"QPushButton:pressed{\n"
"	image: url(:/newPrefix/arrow-alt-circle-left_blue.png)\n"
"}")
        self.previus_group_page_btn_2.setIconSize(QSize(40, 40))
        self.previus_group_page_btn_2.setCheckable(False)

        self.horizontalLayout_30.addWidget(self.previus_group_page_btn_2)

        self.next_group_page_btn_2 = QPushButton(self.widget_30)
        self.next_group_page_btn_2.setObjectName(u"next_group_page_btn_2")
        sizePolicy.setHeightForWidth(self.next_group_page_btn_2.sizePolicy().hasHeightForWidth())
        self.next_group_page_btn_2.setSizePolicy(sizePolicy)
        self.next_group_page_btn_2.setMaximumSize(QSize(16777215, 150))
        self.next_group_page_btn_2.setFont(font8)
        self.next_group_page_btn_2.setStyleSheet(u"QPushButton{\n"
"	image: url(:/newPrefix/arrow-alt-circle-right.png)\n"
"}\n"
"QPushButton:pressed{\n"
"	image: url(:/newPrefix/arrow-alt-circle-right_blue.png)\n"
"}")
        self.next_group_page_btn_2.setIconSize(QSize(40, 40))
        self.next_group_page_btn_2.setCheckable(False)

        self.horizontalLayout_30.addWidget(self.next_group_page_btn_2)

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
        self.verticalLayout_60.setSpacing(10)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 10, 0, 0)
        self.lineEdit = QLineEdit(self.stacked_list_report)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: transparent; border: none; color: #1e2937;\n"
"    font-family: \"Segoe UI\"; font-size: 15px; padding: 6px 4px;\n"
"    selection-background-color: #3b82f6;\n"
"    selection-color: #ffffff;\n"
"}")

        self.verticalLayout_60.addWidget(self.lineEdit)

        self.list_history = QTableWidget(self.stacked_list_report)
        if (self.list_history.columnCount() < 8):
            self.list_history.setColumnCount(8)
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
        if (self.list_history.rowCount() < 17):
            self.list_history.setRowCount(17)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.list_history.setVerticalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.list_history.setVerticalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.list_history.setVerticalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.list_history.setVerticalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.list_history.setVerticalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.list_history.setVerticalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.list_history.setVerticalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.list_history.setVerticalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.list_history.setVerticalHeaderItem(8, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.list_history.setVerticalHeaderItem(9, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.list_history.setVerticalHeaderItem(10, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.list_history.setVerticalHeaderItem(11, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.list_history.setVerticalHeaderItem(12, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.list_history.setVerticalHeaderItem(13, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.list_history.setVerticalHeaderItem(14, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.list_history.setVerticalHeaderItem(15, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.list_history.setVerticalHeaderItem(16, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.list_history.setItem(0, 0, __qtablewidgetitem25)
        self.list_history.setObjectName(u"list_history")
        self.list_history.setStyleSheet(u"QTableWidget {\n"
"    background-color: #ffffff; border: 1px solid #BFC8D3; border-radius: 8px;\n"
"    gridline-color: #BFC8D3; color: #334155; font-family: \"Segoe UI\"; font-size: 20px;\n"
"    selection-background-color: #dbeafe; selection-color: #1e40af; outline: none;\n"
"}\n"
"QTableWidget::item { padding: 8px 14px; border-bottom: 1px solid #f1f5f9; }\n"
"QTableWidget::item:selected { background-color: #dbeafe; color: #1e40af; }\n"
"QTableWidget::item:hover { background-color: #f8fafc; }\n"
"QHeaderView::section {\n"
"    background-color: #f8fafc; color: #1e40af; font-family: \"Segoe UI\";\n"
"    font-size: 16px; font-weight: 700; letter-spacing: 1.5px;\n"
"    padding: 10px 14px; border: none; border-bottom: 2px solid #3b82f6;\n"
"    border-right: 1px solid #e2e8f0;\n"
"}\n"
"QHeaderView::section:last { border-right: none; }\n"
"QScrollBar:vertical { background: #f8fafc; width: 8px; border-radius: 4px; }\n"
"QScrollBar::handle:vertical { background: #cbd5e1; border-radius: 4px; min-height: 24px; }\n"
""
                        "QScrollBar::handle:vertical:hover { background: #94a3b8; }\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0px; }\n"
"QScrollBar:horizontal { background: #f8fafc; height: 8px; border-radius: 4px; }\n"
"QScrollBar::handle:horizontal { background: #cbd5e1; border-radius: 4px; min-width: 24px; }\n"
"QScrollBar::handle:horizontal:hover { background: #94a3b8; }\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal { width: 0px; }")
        self.list_history.horizontalHeader().setStretchLastSection(True)
        self.list_history.verticalHeader().setVisible(False)
        self.list_history.verticalHeader().setDefaultSectionSize(40)

        self.verticalLayout_60.addWidget(self.list_history)


        self.verticalLayout_59.addWidget(self.stacked_list_report)

        self.list_query_btn = QHBoxLayout()
        self.list_query_btn.setObjectName(u"list_query_btn")
        self.list_query_btn.setContentsMargins(-1, -1, -1, 5)
        self.export_all_tables_to_excel_btn = QPushButton(self.dashboard_stacked_widget)
        self.export_all_tables_to_excel_btn.setObjectName(u"export_all_tables_to_excel_btn")
        sizePolicy.setHeightForWidth(self.export_all_tables_to_excel_btn.sizePolicy().hasHeightForWidth())
        self.export_all_tables_to_excel_btn.setSizePolicy(sizePolicy)
        self.export_all_tables_to_excel_btn.setFont(font21)
        self.export_all_tables_to_excel_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B7EC8;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 12px 24px;\n"
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

        self.list_query_btn.addWidget(self.export_all_tables_to_excel_btn)

        self.backward_btn = QPushButton(self.dashboard_stacked_widget)
        self.backward_btn.setObjectName(u"backward_btn")
        sizePolicy.setHeightForWidth(self.backward_btn.sizePolicy().hasHeightForWidth())
        self.backward_btn.setSizePolicy(sizePolicy)
        self.backward_btn.setFont(font21)
        self.backward_btn.setStyleSheet(u"QPushButton {\n"
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

        self.list_query_btn.addWidget(self.backward_btn)


        self.verticalLayout_59.addLayout(self.list_query_btn)

        self.verticalLayout_59.setStretch(0, 9)
        self.verticalLayout_59.setStretch(1, 1)

        self.verticalLayout_13.addWidget(self.dashboard_stacked_widget)

        self.stackedWidget_2.addWidget(self.history_page)

        self.verticalLayout_11.addWidget(self.stackedWidget_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_11)

        self.horizontalLayout_2.setStretch(0, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.body_frame)

        self.verticalLayout.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(2)
        self.sys_state_stacked_wid_39.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(0)
        self.stacked_cel_fah_press_a_1.setCurrentIndex(0)
        self.stacked_cel_fah_press_a_2.setCurrentIndex(0)
        self.stacked_cel_fah_press_a_3.setCurrentIndex(0)
        self.stacked_cel_fah_press_a_4.setCurrentIndex(0)
        self.stacked_cel_fah_press_b_1.setCurrentIndex(0)
        self.stacked_cel_fah_press_b_2.setCurrentIndex(0)
        self.stacked_cel_fah_press_b_3.setCurrentIndex(0)
        self.stacked_cel_fah_press_b_4.setCurrentIndex(0)
        self.stacked_cel_fah_press_c_1.setCurrentIndex(0)
        self.stacked_cel_fah_press_c_2.setCurrentIndex(0)
        self.stacked_cel_fah_press_c_3.setCurrentIndex(0)
        self.stacked_cel_fah_press_c_4.setCurrentIndex(0)
        self.stacked_cel_fah_temp_t0_1.setCurrentIndex(0)
        self.stacked_cel_fah_temp_t0_2.setCurrentIndex(0)
        self.stacked_cel_fah_temp_t0_3.setCurrentIndex(0)
        self.stacked_cel_fah_temp_t0_4.setCurrentIndex(0)
        self.stacked_cel_fah_temp_t0_5.setCurrentIndex(0)
        self.stacked_cel_fah_temp_a_1.setCurrentIndex(0)
        self.stacked_cel_fah_temp_a_2.setCurrentIndex(0)
        self.stacked_cel_fah_temp_a_3.setCurrentIndex(0)
        self.stacked_cel_fah_temp_a_4.setCurrentIndex(0)
        self.stacked_cel_fah_temp_a_5.setCurrentIndex(0)
        self.stacked_cel_fah_temp_a_6.setCurrentIndex(0)
        self.stacked_cel_fah_temp_a_7.setCurrentIndex(0)
        self.stacked_cel_fah_temp_b_1.setCurrentIndex(0)
        self.stacked_cel_fah_temp_b_2.setCurrentIndex(0)
        self.stacked_cel_fah_temp_b_3.setCurrentIndex(0)
        self.stacked_cel_fah_temp_b_4.setCurrentIndex(0)
        self.stacked_cel_fah_temp_b_5.setCurrentIndex(0)
        self.stacked_cel_fah_temp_b_6.setCurrentIndex(0)
        self.stacked_cel_fah_temp_b_7.setCurrentIndex(0)
        self.stacked_cel_fah_temp_c_1.setCurrentIndex(0)
        self.stacked_cel_fah_temp_c_2.setCurrentIndex(0)
        self.stacked_cel_fah_temp_c_3.setCurrentIndex(0)
        self.stacked_cel_fah_temp_c_4.setCurrentIndex(0)
        self.stacked_cel_fah_temp_c_5.setCurrentIndex(0)
        self.stacked_cel_fah_temp_c_6.setCurrentIndex(0)
        self.stacked_cel_fah_temp_c_7.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.sys_state_stacked_wid_40.setCurrentIndex(0)
        self.i_o_group_1_switch_3.setCurrentIndex(0)
        self.i_o_group_1_switch_5.setCurrentIndex(0)
        self.i_o_group_1_switch_6.setCurrentIndex(0)
        self.i_o_group_1_switch_7.setCurrentIndex(0)
        self.i_o_group_1_switch_2.setCurrentIndex(0)
        self.i_o_group_1_switch_1.setCurrentIndex(0)
        self.i_o_group_1_switch_4.setCurrentIndex(0)
        self.i_o_group_1_switch_8.setCurrentIndex(0)
        self.i_o_group_2_switch_5.setCurrentIndex(0)
        self.i_o_group_2_switch_6.setCurrentIndex(0)
        self.i_o_group_2_switch_7.setCurrentIndex(0)
        self.i_o_group_2_switch_8.setCurrentIndex(0)
        self.i_o_group_2_switch_9.setCurrentIndex(0)
        self.i_o_group_2_switch_10.setCurrentIndex(0)
        self.i_o_group_2_switch_11.setCurrentIndex(0)
        self.i_o_group_2_switch_12.setCurrentIndex(0)
        self.i_o_group_2_switch_13.setCurrentIndex(0)
        self.i_o_group_2_switch_15.setCurrentIndex(0)
        self.i_o_group_2_switch_14.setCurrentIndex(0)
        self.i_o_group_2_switch_3.setCurrentIndex(0)
        self.i_o_group_2_switch_4.setCurrentIndex(0)
        self.i_o_group_2_switch_1.setCurrentIndex(0)
        self.i_o_group_2_switch_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tech-Link - Production System", None))
        self.company_name.setText(QCoreApplication.translate("MainWindow", u"TECH-LINK", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u" Language:", None))
        self.language_selection_combox.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))
        self.language_selection_combox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e2d\u56fd", None))

        self.date_displ.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy h:mm:ss AP", None))
        self.home_page_btn.setText(QCoreApplication.translate("MainWindow", u" Group", None))
        self.chart_page_btn.setText(QCoreApplication.translate("MainWindow", u" Chart", None))
        self.device_page_btn.setText(QCoreApplication.translate("MainWindow", u" Setting", None))
        self.history_page_btn.setText(QCoreApplication.translate("MainWindow", u" History", None))
        self.open_side_menu_btn.setText("")
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"Running", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"Waiting", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.previus_group_page_btn.setText("")
        self.next_group_page_btn.setText("")
        self.temp_unit_selection_combox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u00b0C ", None))
        self.temp_unit_selection_combox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u00b0F", None))

        self.clear_data_btn.setText(QCoreApplication.translate("MainWindow", u" Clear Data", None))
        self.new_data_btn.setText(QCoreApplication.translate("MainWindow", u" New Data", None))
        self.data_selection_combobox_b.setItemText(0, QCoreApplication.translate("MainWindow", u"Group Data", None))

        self.data_selection_combobox_b.setCurrentText(QCoreApplication.translate("MainWindow", u"Group Data", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"Group A", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"Group A", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Temp Setting:", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Front Temperature:", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Mid Temperature:", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"End Temperature:", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Pressure Setting:", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Air Filling time:", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Air Holding time:", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Air Bleeding time:", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Oil Start time:", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Oil End time:", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"Group A", None))
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"PV", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"SV", None))
        self.pressure_pv_a_1.setPrefix("")
        self.pressure_pv_a_1.setSuffix("")
        self.pressure_sv_a_1.setPrefix("")
        self.pressure_sv_a_1.setSuffix("")
        self.label_274.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_314.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_pv_a_2.setPrefix("")
        self.pressure_pv_a_2.setSuffix("")
        self.pressure_sv_a_2.setPrefix("")
        self.pressure_sv_a_2.setSuffix("")
        self.label_315.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_316.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_pv_a_3.setPrefix("")
        self.pressure_pv_a_3.setSuffix("")
        self.pressure_sv_a_3.setPrefix("")
        self.pressure_sv_a_3.setSuffix("")
        self.label_317.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_318.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_pv_a_4.setPrefix("")
        self.pressure_pv_a_4.setSuffix("")
        self.pressure_sv_a_4.setPrefix("")
        self.pressure_sv_a_4.setSuffix("")
        self.label_319.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_340.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_pv_a_5.setPrefix("")
        self.pressure_pv_a_5.setSuffix("")
        self.pressure_sv_a_5.setPrefix("")
        self.pressure_sv_a_5.setSuffix("")
        self.label_204.setText(QCoreApplication.translate("MainWindow", u"Bar", None))
        self.pressure_pv_a_6.setPrefix("")
        self.pressure_pv_a_6.setSuffix("")
        self.pressure_sv_a_6.setPrefix("")
        self.pressure_sv_a_6.setSuffix("")
        self.label_213.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_a_7.setPrefix("")
        self.pressure_pv_a_7.setSuffix("")
        self.pressure_sv_a_7.setPrefix("")
        self.pressure_sv_a_7.setSuffix("")
        self.label_214.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_a_8.setPrefix("")
        self.pressure_pv_a_8.setSuffix("")
        self.pressure_sv_a_8.setPrefix("")
        self.pressure_sv_a_8.setSuffix("")
        self.label_215.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_a_9.setPrefix("")
        self.pressure_pv_a_9.setSuffix("")
        self.pressure_sv_a_9.setPrefix("")
        self.pressure_sv_a_9.setSuffix("")
        self.label_216.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_a_10.setPrefix("")
        self.pressure_pv_a_10.setSuffix("")
        self.pressure_sv_a_10.setPrefix("")
        self.pressure_sv_a_10.setSuffix("")
        self.label_222.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"Group B", None))
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"PV", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"SV", None))
        self.pressure_pv_b_1.setPrefix("")
        self.pressure_pv_b_1.setSuffix("")
        self.pressure_sv_b_1.setPrefix("")
        self.pressure_sv_b_1.setSuffix("")
        self.label_275.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_341.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_pv_b_2.setPrefix("")
        self.pressure_pv_b_2.setSuffix("")
        self.pressure_sv_b_2.setPrefix("")
        self.pressure_sv_b_2.setSuffix("")
        self.label_366.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_367.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_pv_b_3.setPrefix("")
        self.pressure_pv_b_3.setSuffix("")
        self.pressure_sv_b_3.setPrefix("")
        self.pressure_sv_b_3.setSuffix("")
        self.label_368.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_369.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_pv_b_4.setPrefix("")
        self.pressure_pv_b_4.setSuffix("")
        self.pressure_sv_b_4.setPrefix("")
        self.pressure_sv_b_4.setSuffix("")
        self.label_370.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_371.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_pv_b_5.setPrefix("")
        self.pressure_pv_b_5.setSuffix("")
        self.pressure_sv_b_5.setPrefix("")
        self.pressure_sv_b_5.setSuffix("")
        self.label_205.setText(QCoreApplication.translate("MainWindow", u"Bar", None))
        self.pressure_pv_b_6.setPrefix("")
        self.pressure_pv_b_6.setSuffix("")
        self.pressure_sv_b_6.setPrefix("")
        self.pressure_sv_b_6.setSuffix("")
        self.label_217.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_b_7.setPrefix("")
        self.pressure_pv_b_7.setSuffix("")
        self.pressure_sv_b_7.setPrefix("")
        self.pressure_sv_b_7.setSuffix("")
        self.label_218.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_b_8.setPrefix("")
        self.pressure_pv_b_8.setSuffix("")
        self.pressure_sv_b_8.setPrefix("")
        self.pressure_sv_b_8.setSuffix("")
        self.label_219.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_b_9.setPrefix("")
        self.pressure_pv_b_9.setSuffix("")
        self.pressure_sv_b_9.setPrefix("")
        self.pressure_sv_b_9.setSuffix("")
        self.label_220.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_b_10.setPrefix("")
        self.pressure_pv_b_10.setSuffix("")
        self.pressure_sv_b_10.setPrefix("")
        self.pressure_sv_b_10.setSuffix("")
        self.label_223.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"Group C", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"PV", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"SV", None))
        self.pressure_pv_c_1.setPrefix("")
        self.pressure_pv_c_1.setSuffix("")
        self.pressure_sv_c_1.setPrefix("")
        self.pressure_sv_c_1.setSuffix("")
        self.label_276.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_372.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_pv_c_2.setPrefix("")
        self.pressure_pv_c_2.setSuffix("")
        self.pressure_sv_c_2.setPrefix("")
        self.pressure_sv_c_2.setSuffix("")
        self.label_373.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_374.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_pv_c_3.setPrefix("")
        self.pressure_pv_c_3.setSuffix("")
        self.pressure_sv_c_3.setPrefix("")
        self.pressure_sv_c_3.setSuffix("")
        self.label_375.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_376.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_pv_c_4.setPrefix("")
        self.pressure_pv_c_4.setSuffix("")
        self.pressure_sv_c_4.setPrefix("")
        self.pressure_sv_c_4.setSuffix("")
        self.label_377.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_378.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.pressure_pv_c_5.setPrefix("")
        self.pressure_pv_c_5.setSuffix("")
        self.pressure_sv_c_5.setPrefix("")
        self.pressure_sv_c_5.setSuffix("")
        self.label_206.setText(QCoreApplication.translate("MainWindow", u"Bar", None))
        self.pressure_pv_c_6.setPrefix("")
        self.pressure_pv_c_6.setSuffix("")
        self.pressure_sv_c_6.setPrefix("")
        self.pressure_sv_c_6.setSuffix("")
        self.label_221.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_c_7.setPrefix("")
        self.pressure_pv_c_7.setSuffix("")
        self.pressure_sv_c_7.setPrefix("")
        self.pressure_sv_c_7.setSuffix("")
        self.label_224.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_c_8.setPrefix("")
        self.pressure_pv_c_8.setSuffix("")
        self.pressure_sv_c_8.setPrefix("")
        self.pressure_sv_c_8.setSuffix("")
        self.label_225.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_c_9.setPrefix("")
        self.pressure_pv_c_9.setSuffix("")
        self.pressure_sv_c_9.setPrefix("")
        self.pressure_sv_c_9.setSuffix("")
        self.label_226.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pressure_pv_c_10.setPrefix("")
        self.pressure_pv_c_10.setSuffix("")
        self.pressure_sv_c_10.setPrefix("")
        self.pressure_sv_c_10.setSuffix("")
        self.label_227.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.cycle_a_displ.setPrefix(QCoreApplication.translate("MainWindow", u"A Cycle: ", None))
        self.reset_cycle_a_btn.setText("")
        self.heat_btn_a.setText(QCoreApplication.translate("MainWindow", u" Heating A", None))
        self.heat_btn_b.setText(QCoreApplication.translate("MainWindow", u" Heating B", None))
        self.heat_btn_c.setText(QCoreApplication.translate("MainWindow", u" Heating C", None))
        self.cycle_b_displ.setPrefix(QCoreApplication.translate("MainWindow", u"B Cycle: ", None))
        self.reset_cycle_b_btn.setText("")
        self.vacuum_btn_b.setText(QCoreApplication.translate("MainWindow", u" A.Pump A", None))
        self.vacuum_btn_a.setText(QCoreApplication.translate("MainWindow", u" A.Pump B", None))
        self.vacuum_btn_c.setText(QCoreApplication.translate("MainWindow", u" A.Pump C", None))
        self.cycle_c_displ.setPrefix(QCoreApplication.translate("MainWindow", u"C Cycle: ", None))
        self.reset_cycle_c_btn.setText("")
        self.refuel_btn_a.setText(QCoreApplication.translate("MainWindow", u" O.Pump A", None))
        self.refuel_btn_b.setText(QCoreApplication.translate("MainWindow", u" O.Pump B", None))
        self.refuel_btn_c.setText(QCoreApplication.translate("MainWindow", u" O.Pump C", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"PV:", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"SV:", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"H.Alm Value:", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"L.Alm Value:", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"Offset Value:", None))
        self.label_132.setText("")
        self.label_134.setText("")
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"T0", None))
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
        self.t0_l_alm_value.setPrefix("")
        self.t0_l_alm_value.setSuffix("")
        self.label_259.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_260.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.t0_offset_value.setPrefix("")
        self.t0_offset_value.setSuffix("")
        self.label_364.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_365.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.label_135.setText("")
        self.label_136.setText("")
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"A-T", None))
        self.at_pv.setPrefix("")
        self.at_pv.setSuffix("")
        self.label_320.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_321.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.at_sv.setPrefix("")
        self.at_sv.setSuffix("")
        self.label_322.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_323.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.at_h_alm_value.setPrefix("")
        self.at_h_alm_value.setSuffix("")
        self.label_324.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_325.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.at_l_alm_value.setPrefix("")
        self.at_l_alm_value.setSuffix("")
        self.label_326.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_327.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.at_t1_offset_value.setPrefix(QCoreApplication.translate("MainWindow", u"Front: ", None))
        self.at_t1_offset_value.setSuffix("")
        self.label_328.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_329.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.at_t2_offset_value.setPrefix(QCoreApplication.translate("MainWindow", u"Mid: ", None))
        self.at_t2_offset_value.setSuffix("")
        self.label_330.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_331.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.at_t3_offset_value.setPrefix(QCoreApplication.translate("MainWindow", u"End: ", None))
        self.at_t3_offset_value.setSuffix("")
        self.label_332.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_333.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"B-T", None))
        self.bt_pv.setPrefix("")
        self.bt_pv.setSuffix("")
        self.label_334.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_335.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.bt_sv.setPrefix("")
        self.bt_sv.setSuffix("")
        self.label_336.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_337.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.bt_h_alm_value.setPrefix("")
        self.bt_h_alm_value.setSuffix("")
        self.label_338.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_339.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.bt_l_alm_value.setPrefix("")
        self.bt_l_alm_value.setSuffix("")
        self.label_342.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_343.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.bt_t1_offset_value.setPrefix(QCoreApplication.translate("MainWindow", u"Front: ", None))
        self.bt_t1_offset_value.setSuffix("")
        self.label_344.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_345.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.bt_t2_offset_value.setPrefix(QCoreApplication.translate("MainWindow", u"Mid: ", None))
        self.bt_t2_offset_value.setSuffix("")
        self.label_346.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_347.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.bt_t3_offset_value.setPrefix(QCoreApplication.translate("MainWindow", u"End: ", None))
        self.bt_t3_offset_value.setSuffix("")
        self.label_348.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_349.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"C-T", None))
        self.ct_pv.setPrefix("")
        self.ct_pv.setSuffix("")
        self.label_350.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_351.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.ct_sv.setPrefix("")
        self.ct_sv.setSuffix("")
        self.label_352.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_353.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.ct_h_alm_value.setPrefix("")
        self.ct_h_alm_value.setSuffix("")
        self.label_354.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_355.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.ct_l_alm_value.setPrefix("")
        self.ct_l_alm_value.setSuffix("")
        self.label_356.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_357.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.ct_t1_offset_value.setPrefix(QCoreApplication.translate("MainWindow", u"Front: ", None))
        self.ct_t1_offset_value.setSuffix("")
        self.label_358.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_359.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.ct_t2_offset_value.setPrefix(QCoreApplication.translate("MainWindow", u"Mid: ", None))
        self.ct_t2_offset_value.setSuffix("")
        self.label_360.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_361.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.ct_t3_offset_value.setPrefix(QCoreApplication.translate("MainWindow", u"End: ", None))
        self.ct_t3_offset_value.setSuffix("")
        self.label_362.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_363.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.heat_btn_t0.setText(QCoreApplication.translate("MainWindow", u" Heating T0", None))
        self.back_home_btn.setText(QCoreApplication.translate("MainWindow", u"\U0001f4c8 Back", None))
        self.plc_io_btn.setText("")
        self.connection_group.setTitle(QCoreApplication.translate("MainWindow", u"Connection Settings", None))
        self.db_data_size_input.setSuffix(QCoreApplication.translate("MainWindow", u" ~ 2056", None))
        self.slot_label_8.setText(QCoreApplication.translate("MainWindow", u"Interupt Time:", None))
        self.slot_label_2.setText(QCoreApplication.translate("MainWindow", u"DB:", None))
        self.slot_label_7.setText(QCoreApplication.translate("MainWindow", u"Size Data:", None))
        self.interupt_time_input.setSuffix(QCoreApplication.translate("MainWindow", u" ms ~ 10000 ms", None))
        self.plc_ip_address.setText(QCoreApplication.translate("MainWindow", u"IP address:", None))
        self.plc_ip_address_2.setText(QCoreApplication.translate("MainWindow", u"Connection:", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Connected", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Disconnected", None))
        self.rb_connect.setText(QCoreApplication.translate("MainWindow", u"\U0001f50c Connect", None))
        self.dis_rb.setText(QCoreApplication.translate("MainWindow", u"\u26d3\ufe0f\u200d Disconnect", None))
        self.new_data_btn_2.setText(QCoreApplication.translate("MainWindow", u" Save Data", None))
        self.clear_data_btn_2.setText(QCoreApplication.translate("MainWindow", u" Clear Data", None))
        self.i_o_group_1.setTitle(QCoreApplication.translate("MainWindow", u"DI", None))
        self.pushButton_58.setText("")
        self.pushButton_59.setText("")
        self.pushButton_62.setText("")
        self.pushButton_63.setText("")
        self.pushButton_64.setText("")
        self.pushButton_65.setText("")
        self.pushButton_66.setText("")
        self.pushButton_67.setText("")
        self.pushButton_56.setText("")
        self.pushButton_57.setText("")
        self.di_name_1.setText(QCoreApplication.translate("MainWindow", u"START:", None))
        self.pushButton_42.setText("")
        self.pushButton_43.setText("")
        self.pushButton_60.setText("")
        self.pushButton_61.setText("")
        self.pushButton_68.setText("")
        self.pushButton_69.setText("")
        self.di_name_2.setText(QCoreApplication.translate("MainWindow", u"STOP:", None))
        self.di_name_3.setText(QCoreApplication.translate("MainWindow", u"KT0:", None))
        self.di_name_4.setText(QCoreApplication.translate("MainWindow", u"KF1:", None))
        self.di_name_5.setText(QCoreApplication.translate("MainWindow", u"KF2:", None))
        self.di_name_6.setText(QCoreApplication.translate("MainWindow", u"KT1:", None))
        self.di_name_7.setText(QCoreApplication.translate("MainWindow", u"KT2:", None))
        self.di_name_8.setText(QCoreApplication.translate("MainWindow", u"KT3:", None))
        self.i_o_group_2.setTitle(QCoreApplication.translate("MainWindow", u"DQ", None))
        self.pushButton_108.setText("")
        self.pushButton_109.setText("")
        self.pushButton_110.setText("")
        self.pushButton_111.setText("")
        self.pushButton_112.setText("")
        self.pushButton_113.setText("")
        self.pushButton_114.setText("")
        self.pushButton_115.setText("")
        self.pushButton_116.setText("")
        self.pushButton_117.setText("")
        self.pushButton_118.setText("")
        self.pushButton_119.setText("")
        self.pushButton_120.setText("")
        self.pushButton_121.setText("")
        self.pushButton_122.setText("")
        self.pushButton_123.setText("")
        self.dq_name_1.setText(QCoreApplication.translate("MainWindow", u"R1:", None))
        self.pushButton_124.setText("")
        self.pushButton_125.setText("")
        self.dq_name_2.setText(QCoreApplication.translate("MainWindow", u"R2:", None))
        self.pushButton_128.setText("")
        self.pushButton_129.setText("")
        self.dq_name_3.setText(QCoreApplication.translate("MainWindow", u"R3:", None))
        self.dq_name_4.setText(QCoreApplication.translate("MainWindow", u"R4:", None))
        self.dq_name_6.setText(QCoreApplication.translate("MainWindow", u"R6:", None))
        self.dq_name_5.setText(QCoreApplication.translate("MainWindow", u"R5:", None))
        self.dq_name_7.setText(QCoreApplication.translate("MainWindow", u"R7:", None))
        self.dq_name_8.setText(QCoreApplication.translate("MainWindow", u"R8:", None))
        self.dq_name_9.setText(QCoreApplication.translate("MainWindow", u"R9:", None))
        self.dq_name_10.setText(QCoreApplication.translate("MainWindow", u"R10:", None))
        self.dq_name_11.setText(QCoreApplication.translate("MainWindow", u"R11:", None))
        self.dq_name_13.setText(QCoreApplication.translate("MainWindow", u"R13:", None))
        self.dq_name_12.setText(QCoreApplication.translate("MainWindow", u"R12:", None))
        self.dq_name_14.setText(QCoreApplication.translate("MainWindow", u"R14:", None))
        self.dq_name_15.setText(QCoreApplication.translate("MainWindow", u"R15:", None))
        self.pushButton_126.setText("")
        self.pushButton_127.setText("")
        self.pushButton_104.setText("")
        self.pushButton_105.setText("")
        self.pushButton_106.setText("")
        self.pushButton_107.setText("")
        self.pushButton_72.setText("")
        self.pushButton_73.setText("")
        self.pushButton_102.setText("")
        self.pushButton_103.setText("")
        self.i_o_group_3.setTitle(QCoreApplication.translate("MainWindow", u"AI", None))
        self.ai_name_1.setText(QCoreApplication.translate("MainWindow", u"T0:", None))
        self.ai_name_15.setText(QCoreApplication.translate("MainWindow", u"FP2:", None))
        self.ai_name_14.setText(QCoreApplication.translate("MainWindow", u"FP1:", None))
        self.ai_name_12.setText(QCoreApplication.translate("MainWindow", u"P2:", None))
        self.ai_name_13.setText(QCoreApplication.translate("MainWindow", u"P3:", None))
        self.ai_name_16.setText(QCoreApplication.translate("MainWindow", u"FP3:", None))
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
        self.previus_group_page_btn_2.setText("")
        self.next_group_page_btn_2.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\U0001f50d Searching", None))
        ___qtablewidgetitem = self.list_history.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"No.", None))
        ___qtablewidgetitem1 = self.list_history.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name.", None))
        ___qtablewidgetitem2 = self.list_history.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Pressure.", None))
        ___qtablewidgetitem3 = self.list_history.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Average.", None))
        ___qtablewidgetitem4 = self.list_history.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Front.", None))
        ___qtablewidgetitem5 = self.list_history.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Middle.", None))
        ___qtablewidgetitem6 = self.list_history.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"End.", None))
        ___qtablewidgetitem7 = self.list_history.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Date.", None))
        ___qtablewidgetitem8 = self.list_history.verticalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"1", None))
        ___qtablewidgetitem9 = self.list_history.verticalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"2", None))
        ___qtablewidgetitem10 = self.list_history.verticalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"3", None))
        ___qtablewidgetitem11 = self.list_history.verticalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"4", None))
        ___qtablewidgetitem12 = self.list_history.verticalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"5", None))
        ___qtablewidgetitem13 = self.list_history.verticalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"6", None))
        ___qtablewidgetitem14 = self.list_history.verticalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"7", None))
        ___qtablewidgetitem15 = self.list_history.verticalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"8", None))
        ___qtablewidgetitem16 = self.list_history.verticalHeaderItem(8)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"9", None))
        ___qtablewidgetitem17 = self.list_history.verticalHeaderItem(9)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"10", None))
        ___qtablewidgetitem18 = self.list_history.verticalHeaderItem(10)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"11", None))
        ___qtablewidgetitem19 = self.list_history.verticalHeaderItem(11)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"12", None))
        ___qtablewidgetitem20 = self.list_history.verticalHeaderItem(12)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"13", None))
        ___qtablewidgetitem21 = self.list_history.verticalHeaderItem(13)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"14", None))
        ___qtablewidgetitem22 = self.list_history.verticalHeaderItem(14)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"15", None))
        ___qtablewidgetitem23 = self.list_history.verticalHeaderItem(15)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"16", None))
        ___qtablewidgetitem24 = self.list_history.verticalHeaderItem(16)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"17", None))

        __sortingEnabled = self.list_history.isSortingEnabled()
        self.list_history.setSortingEnabled(False)
        self.list_history.setSortingEnabled(__sortingEnabled)

        self.export_all_tables_to_excel_btn.setText(QCoreApplication.translate("MainWindow", u"\U0001f4ca Export Data", None))
        self.backward_btn.setText(QCoreApplication.translate("MainWindow", u"\U0001f4c8 Go Back", None))
    # retranslateUi


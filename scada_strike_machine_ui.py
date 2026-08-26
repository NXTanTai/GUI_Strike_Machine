# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scada_strike_machine.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QButtonGroup, QDateTimeEdit,
    QFrame, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)
import Icon_rc
import resources_rc
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1024, 725)
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
        self.centralwidget.setMinimumSize(QSize(1024, 724))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        sizePolicy.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy)
        self.header_frame.setMinimumSize(QSize(0, 45))
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
        self.logo_btn.setIconSize(QSize(45, 45))
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
        font1.setPointSize(21)
        font1.setBold(True)
        self.company_name.setFont(font1)
        self.company_name.setStyleSheet(u"color: #1E293B;")

        self.company_header_layout.addWidget(self.company_name)


        self.horizontalLayout.addLayout(self.company_header_layout)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.warning_notification = QPushButton(self.header_frame)
        self.warning_notification.setObjectName(u"warning_notification")
        sizePolicy.setHeightForWidth(self.warning_notification.sizePolicy().hasHeightForWidth())
        self.warning_notification.setSizePolicy(sizePolicy)
        self.warning_notification.setStyleSheet(u"background-color: transparent;\n"
"border-radius: 8px;")

        self.horizontalLayout_49.addWidget(self.warning_notification)

        self.error_notification = QPushButton(self.header_frame)
        self.error_notification.setObjectName(u"error_notification")
        sizePolicy.setHeightForWidth(self.error_notification.sizePolicy().hasHeightForWidth())
        self.error_notification.setSizePolicy(sizePolicy)
        self.error_notification.setStyleSheet(u"background-color: transparent;\n"
"border-radius: 8px;")

        self.horizontalLayout_49.addWidget(self.error_notification)


        self.horizontalLayout.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 3, -1, 3)
        self.eng_language = QPushButton(self.header_frame)
        self.language_group_btn = QButtonGroup(MainWindow)
        self.language_group_btn.setObjectName(u"language_group_btn")
        self.language_group_btn.addButton(self.eng_language)
        self.eng_language.setObjectName(u"eng_language")
        sizePolicy.setHeightForWidth(self.eng_language.sizePolicy().hasHeightForWidth())
        self.eng_language.setSizePolicy(sizePolicy)
        self.eng_language.setMinimumSize(QSize(0, 0))
        self.eng_language.setMaximumSize(QSize(16777215, 16777215))
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
        self.eng_language.setIconSize(QSize(45, 45))
        self.eng_language.setCheckable(True)
        self.eng_language.setChecked(True)

        self.horizontalLayout_10.addWidget(self.eng_language)

        self.vn_language = QPushButton(self.header_frame)
        self.language_group_btn.addButton(self.vn_language)
        self.vn_language.setObjectName(u"vn_language")
        sizePolicy.setHeightForWidth(self.vn_language.sizePolicy().hasHeightForWidth())
        self.vn_language.setSizePolicy(sizePolicy)
        self.vn_language.setMinimumSize(QSize(0, 0))
        self.vn_language.setMaximumSize(QSize(16777215, 16777215))
        self.vn_language.setStyleSheet(u"\n"
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
        icon2.addFile(u":/Icons/Viet_Nam_flag.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.vn_language.setIcon(icon2)
        self.vn_language.setIconSize(QSize(45, 45))
        self.vn_language.setCheckable(True)
        self.vn_language.setChecked(False)

        self.horizontalLayout_10.addWidget(self.vn_language)

        self.cn_language = QPushButton(self.header_frame)
        self.language_group_btn.addButton(self.cn_language)
        self.cn_language.setObjectName(u"cn_language")
        sizePolicy.setHeightForWidth(self.cn_language.sizePolicy().hasHeightForWidth())
        self.cn_language.setSizePolicy(sizePolicy)
        self.cn_language.setMinimumSize(QSize(0, 0))
        self.cn_language.setMaximumSize(QSize(16777215, 16777215))
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
        icon3 = QIcon()
        icon3.addFile(u":/Icons/cn_flag.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cn_language.setIcon(icon3)
        self.cn_language.setIconSize(QSize(45, 45))
        self.cn_language.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.cn_language)


        self.horizontalLayout.addLayout(self.horizontalLayout_10)

        self.date_displ = QDateTimeEdit(self.header_frame)
        self.date_displ.setObjectName(u"date_displ")
        sizePolicy.setHeightForWidth(self.date_displ.sizePolicy().hasHeightForWidth())
        self.date_displ.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.date_displ.setFont(font2)
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
        self.plc_io_btn_2 = QPushButton(self.body_frame)
        self.plc_io_btn_2.setObjectName(u"plc_io_btn_2")
        sizePolicy.setHeightForWidth(self.plc_io_btn_2.sizePolicy().hasHeightForWidth())
        self.plc_io_btn_2.setSizePolicy(sizePolicy)
        self.plc_io_btn_2.setMinimumSize(QSize(0, 0))
        self.plc_io_btn_2.setStyleSheet(u"font-size: 24px; \n"
"color: #0B7EC8;\n"
"border: none;\n"
"image: url(:/Icons/Industrial_Furnace.PNG);")

        self.verticalLayout_2.addWidget(self.plc_io_btn_2)


        self.verticalLayout.addWidget(self.body_frame)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tech-Link - Strike Machine System", None))
        self.logo_btn.setText("")
        self.company_name.setText(QCoreApplication.translate("MainWindow", u"TECH-LINK", None))
        self.warning_notification.setText("")
        self.error_notification.setText("")
        self.eng_language.setText("")
        self.vn_language.setText("")
        self.cn_language.setText("")
        self.date_displ.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy hh:mm:ss", None))
#if QT_CONFIG(tooltip)
        self.plc_io_btn_2.setToolTip(QCoreApplication.translate("MainWindow", u"H\u00ea s\u1edd l\u00f4", None))
#endif // QT_CONFIG(tooltip)
        self.plc_io_btn_2.setText("")
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_query.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(860, 560)
        MainWindow.setStyleSheet(u"\n"
"QMainWindow { background-color: #f8fafc; }\n"
"QWidget#centralwidget { background-color: #f8fafc; }\n"
"QLabel#label_title {\n"
"    color: #1e2937; font-family: \"Segoe UI\"; font-size: 20px;\n"
"    font-weight: 700; letter-spacing: 1px;\n"
"}\n"
"QLabel#label_subtitle {\n"
"    color: #64748b; font-family: \"Segoe UI\"; font-size: 11px; letter-spacing: 2px;\n"
"}\n"
"QFrame#frame_search {\n"
"    background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px;\n"
"}\n"
"QLineEdit#lineEdit_search {\n"
"    background-color: transparent; border: none; color: #1e2937;\n"
"    font-family: \"Segoe UI\"; font-size: 13px; padding: 6px 4px;\n"
"    selection-background-color: #3b82f6;\n"
"    selection-color: #ffffff;\n"
"}\n"
"QLabel#label_icon { color: #94a3b8; font-size: 15px; padding-left: 6px; }\n"
"QPushButton#btn_clear {\n"
"    background-color: transparent; border: none; color: #94a3b8;\n"
"    font-size: 16px; font-weight: bold; padding: 0px 8px; border-radius: 4px;\n"
"}\n"
"QPushButton#b"
                        "tn_clear:hover { color: #475569; background-color: #f1f5f9; }\n"
"QLabel#label_info { color: #64748b; font-family: \"Segoe UI\"; font-size: 11px; font-style: italic; }\n"
"QTableWidget {\n"
"    background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px;\n"
"    gridline-color: #f1f5f9; color: #334155; font-family: \"Segoe UI\"; font-size: 13px;\n"
"    selection-background-color: #dbeafe; selection-color: #1e40af; outline: none;\n"
"}\n"
"QTableWidget::item { padding: 8px 14px; border-bottom: 1px solid #f1f5f9; }\n"
"QTableWidget::item:selected { background-color: #dbeafe; color: #1e40af; }\n"
"QTableWidget::item:hover { background-color: #f8fafc; }\n"
"QHeaderView::section {\n"
"    background-color: #f8fafc; color: #1e40af; font-family: \"Segoe UI\";\n"
"    font-size: 11px; font-weight: 700; letter-spacing: 1.5px;\n"
"    padding: 10px 14px; border: none; border-bottom: 2px solid #3b82f6;\n"
"    border-right: 1px solid #e2e8f0;\n"
"}\n"
"QHeaderView::section:last { border-right: none; }\n"
""
                        "QScrollBar:vertical { background: #f8fafc; width: 8px; border-radius: 4px; }\n"
"QScrollBar::handle:vertical { background: #cbd5e1; border-radius: 4px; min-height: 24px; }\n"
"QScrollBar::handle:vertical:hover { background: #94a3b8; }\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0px; }\n"
"QScrollBar:horizontal { background: #f8fafc; height: 8px; border-radius: 4px; }\n"
"QScrollBar::handle:horizontal { background: #cbd5e1; border-radius: 4px; min-width: 24px; }\n"
"QScrollBar::handle:horizontal:hover { background: #94a3b8; }\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal { width: 0px; }\n"
"QStatusBar {\n"
"    background-color: #f1f5f9; color: #64748b; font-family: \"Segoe UI\";\n"
"    font-size: 11px; border-top: 1px solid #e2e8f0;\n"
"}\n"
"   ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_main = QVBoxLayout(self.centralwidget)
        self.verticalLayout_main.setSpacing(0)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.verticalLayout_main.setContentsMargins(24, 20, 24, 20)
        self.horizontalLayout_header = QHBoxLayout()
        self.horizontalLayout_header.setSpacing(0)
        self.horizontalLayout_header.setObjectName(u"horizontalLayout_header")
        self.verticalLayout_title = QVBoxLayout()
        self.verticalLayout_title.setSpacing(2)
        self.verticalLayout_title.setObjectName(u"verticalLayout_title")
        self.label_subtitle = QLabel(self.centralwidget)
        self.label_subtitle.setObjectName(u"label_subtitle")

        self.verticalLayout_title.addWidget(self.label_subtitle)

        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")

        self.verticalLayout_title.addWidget(self.label_title)


        self.horizontalLayout_header.addLayout(self.verticalLayout_title)

        self.horizontalSpacer_header = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_header.addItem(self.horizontalSpacer_header)

        self.label_info = QLabel(self.centralwidget)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setAlignment(Qt.AlignRight|Qt.AlignVCenter)

        self.horizontalLayout_header.addWidget(self.label_info)


        self.verticalLayout_main.addLayout(self.horizontalLayout_header)

        self.verticalSpacer_1 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_main.addItem(self.verticalSpacer_1)

        self.frame_search = QFrame(self.centralwidget)
        self.frame_search.setObjectName(u"frame_search")
        self.frame_search.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_search = QHBoxLayout(self.frame_search)
        self.horizontalLayout_search.setSpacing(4)
        self.horizontalLayout_search.setObjectName(u"horizontalLayout_search")
        self.horizontalLayout_search.setContentsMargins(6, 0, 6, 0)
        self.label_icon = QLabel(self.frame_search)
        self.label_icon.setObjectName(u"label_icon")

        self.horizontalLayout_search.addWidget(self.label_icon)

        self.lineEdit_search = QLineEdit(self.frame_search)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setClearButtonEnabled(False)

        self.horizontalLayout_search.addWidget(self.lineEdit_search)

        self.btn_clear = QPushButton(self.frame_search)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMaximumWidth(32)

        self.horizontalLayout_search.addWidget(self.btn_clear)


        self.verticalLayout_main.addWidget(self.frame_search)

        self.verticalSpacer_2 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_main.addItem(self.verticalSpacer_2)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)

        self.verticalLayout_main.addWidget(self.tableWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Data Query", None))
        self.label_subtitle.setText(QCoreApplication.translate("MainWindow", u"RECORD MANAGEMENT", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Data Query", None))
        self.label_info.setText(QCoreApplication.translate("MainWindow", u"Showing all records", None))
        self.label_icon.setText(QCoreApplication.translate("MainWindow", u"\U0001f50d", None))
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search by Type...", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"\u2715", None))
#if QT_CONFIG(tooltip)
        self.btn_clear.setToolTip(QCoreApplication.translate("MainWindow", u"Clear search", None))
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"No.", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Date", None))
    # retranslateUi


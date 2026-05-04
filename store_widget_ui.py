# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'store_widget.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QStackedWidget, QVBoxLayout, QWidget)
import Icon_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(2480, 821)
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 380, 28, 41))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(15)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"border: none;\n"
"")
        self.widget_48 = QWidget(Form)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setGeometry(QRect(460, 460, 824, 292))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_48.sizePolicy().hasHeightForWidth())
        self.widget_48.setSizePolicy(sizePolicy)
        self.widget_48.setStyleSheet(u"")
        self.horizontalLayout_95 = QHBoxLayout(self.widget_48)
        self.horizontalLayout_95.setSpacing(5)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, 0, 10, 0)
        self.widget_80 = QWidget(self.widget_48)
        self.widget_80.setObjectName(u"widget_80")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_80.sizePolicy().hasHeightForWidth())
        self.widget_80.setSizePolicy(sizePolicy1)
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
        self.widget_49 = QWidget(self.widget_81)
        self.widget_49.setObjectName(u"widget_49")
        self.verticalLayout_67 = QVBoxLayout(self.widget_49)
        self.verticalLayout_67.setSpacing(15)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(10, 10, 10, 10)
        self.widget_91 = QWidget(self.widget_49)
        self.widget_91.setObjectName(u"widget_91")
        self.widget_91.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_96 = QHBoxLayout(self.widget_91)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(0, 0, 5, 0)
        self.label_113 = QLabel(self.widget_91)
        self.label_113.setObjectName(u"label_113")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_113.setFont(font1)

        self.horizontalLayout_96.addWidget(self.label_113)


        self.verticalLayout_67.addWidget(self.widget_91)

        self.widget_92 = QWidget(self.widget_49)
        self.widget_92.setObjectName(u"widget_92")
        self.widget_92.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_123 = QHBoxLayout(self.widget_92)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalLayout_123.setContentsMargins(0, 0, 5, 0)
        self.label_114 = QLabel(self.widget_92)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setFont(font1)

        self.horizontalLayout_123.addWidget(self.label_114)


        self.verticalLayout_67.addWidget(self.widget_92)

        self.widget_93 = QWidget(self.widget_49)
        self.widget_93.setObjectName(u"widget_93")
        self.widget_93.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_132 = QHBoxLayout(self.widget_93)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalLayout_132.setContentsMargins(0, 0, 5, 0)
        self.label_115 = QLabel(self.widget_93)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setFont(font1)

        self.horizontalLayout_132.addWidget(self.label_115)


        self.verticalLayout_67.addWidget(self.widget_93)


        self.verticalLayout_66.addWidget(self.widget_49)


        self.verticalLayout_65.addWidget(self.widget_81)


        self.horizontalLayout_95.addWidget(self.widget_80)

        self.widget_50 = QWidget(self.widget_48)
        self.widget_50.setObjectName(u"widget_50")
        self.widget_50.setStyleSheet(u"border-left: None;")
        self.verticalLayout_68 = QVBoxLayout(self.widget_50)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.widget_51 = QWidget(self.widget_50)
        self.widget_51.setObjectName(u"widget_51")
        self.widget_51.setMinimumSize(QSize(175, 0))
        self.widget_51.setMaximumSize(QSize(275, 16777215))
        self.widget_51.setStyleSheet(u"QDoubleSpinBox\n"
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
        self.verticalLayout_69 = QVBoxLayout(self.widget_51)
        self.verticalLayout_69.setSpacing(15)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 10, 0, 10)
        self.widget_143 = QWidget(self.widget_51)
        self.widget_143.setObjectName(u"widget_143")
        self.widget_143.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_134 = QHBoxLayout(self.widget_143)
        self.horizontalLayout_134.setSpacing(10)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.horizontalLayout_134.setContentsMargins(10, 0, 0, 0)
        self.widget_52 = QWidget(self.widget_143)
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
        self.horizontalLayout_135 = QHBoxLayout(self.widget_52)
        self.horizontalLayout_135.setSpacing(0)
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.horizontalLayout_135.setContentsMargins(2, 2, 2, 2)
        self.filling_time_input = QDoubleSpinBox(self.widget_52)
        self.filling_time_input.setObjectName(u"filling_time_input")
        sizePolicy.setHeightForWidth(self.filling_time_input.sizePolicy().hasHeightForWidth())
        self.filling_time_input.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(False)
        self.filling_time_input.setFont(font2)
        self.filling_time_input.setStyleSheet(u"")
        self.filling_time_input.setAlignment(Qt.AlignCenter)
        self.filling_time_input.setReadOnly(False)
        self.filling_time_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.filling_time_input.setDecimals(1)
        self.filling_time_input.setMaximum(999.000000000000000)
        self.filling_time_input.setValue(999.000000000000000)

        self.horizontalLayout_135.addWidget(self.filling_time_input)


        self.horizontalLayout_134.addWidget(self.widget_52)

        self.horizontalLayout_134.setStretch(0, 2)

        self.verticalLayout_69.addWidget(self.widget_143)

        self.widget_145 = QWidget(self.widget_51)
        self.widget_145.setObjectName(u"widget_145")
        self.widget_145.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_137 = QHBoxLayout(self.widget_145)
        self.horizontalLayout_137.setSpacing(10)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalLayout_137.setContentsMargins(10, 0, 0, 0)
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
        self.horizontalLayout_141 = QHBoxLayout(self.widget_53)
        self.horizontalLayout_141.setSpacing(0)
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.horizontalLayout_141.setContentsMargins(2, 2, 2, 2)
        self.g_holding_time_input = QDoubleSpinBox(self.widget_53)
        self.g_holding_time_input.setObjectName(u"g_holding_time_input")
        sizePolicy.setHeightForWidth(self.g_holding_time_input.sizePolicy().hasHeightForWidth())
        self.g_holding_time_input.setSizePolicy(sizePolicy)
        self.g_holding_time_input.setFont(font2)
        self.g_holding_time_input.setStyleSheet(u"")
        self.g_holding_time_input.setAlignment(Qt.AlignCenter)
        self.g_holding_time_input.setReadOnly(False)
        self.g_holding_time_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.g_holding_time_input.setDecimals(1)
        self.g_holding_time_input.setMaximum(999.000000000000000)
        self.g_holding_time_input.setValue(999.000000000000000)

        self.horizontalLayout_141.addWidget(self.g_holding_time_input)


        self.horizontalLayout_137.addWidget(self.widget_53)

        self.horizontalLayout_137.setStretch(0, 2)

        self.verticalLayout_69.addWidget(self.widget_145)

        self.widget_155 = QWidget(self.widget_51)
        self.widget_155.setObjectName(u"widget_155")
        self.widget_155.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_144 = QHBoxLayout(self.widget_155)
        self.horizontalLayout_144.setSpacing(10)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.horizontalLayout_144.setContentsMargins(10, 0, 0, 0)
        self.widget_54 = QWidget(self.widget_155)
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
        self.horizontalLayout_147 = QHBoxLayout(self.widget_54)
        self.horizontalLayout_147.setSpacing(0)
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.horizontalLayout_147.setContentsMargins(2, 2, 2, 2)
        self.bleeding_time_input = QDoubleSpinBox(self.widget_54)
        self.bleeding_time_input.setObjectName(u"bleeding_time_input")
        sizePolicy.setHeightForWidth(self.bleeding_time_input.sizePolicy().hasHeightForWidth())
        self.bleeding_time_input.setSizePolicy(sizePolicy)
        self.bleeding_time_input.setFont(font2)
        self.bleeding_time_input.setStyleSheet(u"")
        self.bleeding_time_input.setAlignment(Qt.AlignCenter)
        self.bleeding_time_input.setReadOnly(False)
        self.bleeding_time_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.bleeding_time_input.setDecimals(1)
        self.bleeding_time_input.setMaximum(999.000000000000000)
        self.bleeding_time_input.setValue(999.000000000000000)

        self.horizontalLayout_147.addWidget(self.bleeding_time_input)


        self.horizontalLayout_144.addWidget(self.widget_54)

        self.horizontalLayout_144.setStretch(0, 2)

        self.verticalLayout_69.addWidget(self.widget_155)


        self.verticalLayout_68.addWidget(self.widget_51)


        self.horizontalLayout_95.addWidget(self.widget_50)

        self.line_14 = QFrame(self.widget_48)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.Shape.VLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_95.addWidget(self.line_14)

        self.widget_55 = QWidget(self.widget_48)
        self.widget_55.setObjectName(u"widget_55")
        sizePolicy1.setHeightForWidth(self.widget_55.sizePolicy().hasHeightForWidth())
        self.widget_55.setSizePolicy(sizePolicy1)
        self.widget_55.setStyleSheet(u"")
        self.horizontalLayout_163 = QHBoxLayout(self.widget_55)
        self.horizontalLayout_163.setSpacing(5)
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.horizontalLayout_163.setContentsMargins(0, 0, 0, 0)
        self.widget_107 = QWidget(self.widget_55)
        self.widget_107.setObjectName(u"widget_107")
        sizePolicy1.setHeightForWidth(self.widget_107.sizePolicy().hasHeightForWidth())
        self.widget_107.setSizePolicy(sizePolicy1)
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
        self.label_128.setFont(font1)

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
        self.widget_116 = QWidget(self.widget_114)
        self.widget_116.setObjectName(u"widget_116")
        self.widget_116.setStyleSheet(u"QDoubleSpinBox\n"
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
        self.verticalLayout_88 = QVBoxLayout(self.widget_116)
        self.verticalLayout_88.setSpacing(15)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 10, 0, 10)
        self.widget_167 = QWidget(self.widget_116)
        self.widget_167.setObjectName(u"widget_167")
        self.widget_167.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_41 = QHBoxLayout(self.widget_167)
        self.horizontalLayout_41.setSpacing(10)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(10, 0, 0, 0)
        self.widget_119 = QWidget(self.widget_167)
        self.widget_119.setObjectName(u"widget_119")
        self.widget_119.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout_192 = QHBoxLayout(self.widget_119)
        self.horizontalLayout_192.setObjectName(u"horizontalLayout_192")
        self.horizontalLayout_192.setContentsMargins(2, 2, 2, 2)
        self.pressure_pv_displ = QDoubleSpinBox(self.widget_119)
        self.pressure_pv_displ.setObjectName(u"pressure_pv_displ")
        sizePolicy.setHeightForWidth(self.pressure_pv_displ.sizePolicy().hasHeightForWidth())
        self.pressure_pv_displ.setSizePolicy(sizePolicy)
        self.pressure_pv_displ.setFont(font2)
        self.pressure_pv_displ.setStyleSheet(u"")
        self.pressure_pv_displ.setAlignment(Qt.AlignCenter)
        self.pressure_pv_displ.setReadOnly(True)
        self.pressure_pv_displ.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_pv_displ.setDecimals(1)
        self.pressure_pv_displ.setMaximum(999.000000000000000)
        self.pressure_pv_displ.setValue(999.000000000000000)

        self.horizontalLayout_192.addWidget(self.pressure_pv_displ)

        self.label_30 = QLabel(self.widget_119)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(u"border: none;\n"
"")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_192.addWidget(self.label_30)

        self.pressure_sv_input = QDoubleSpinBox(self.widget_119)
        self.pressure_sv_input.setObjectName(u"pressure_sv_input")
        sizePolicy.setHeightForWidth(self.pressure_sv_input.sizePolicy().hasHeightForWidth())
        self.pressure_sv_input.setSizePolicy(sizePolicy)
        self.pressure_sv_input.setFont(font2)
        self.pressure_sv_input.setStyleSheet(u"")
        self.pressure_sv_input.setAlignment(Qt.AlignCenter)
        self.pressure_sv_input.setReadOnly(False)
        self.pressure_sv_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pressure_sv_input.setDecimals(1)
        self.pressure_sv_input.setMaximum(999.000000000000000)
        self.pressure_sv_input.setValue(999.000000000000000)

        self.horizontalLayout_192.addWidget(self.pressure_sv_input)


        self.horizontalLayout_41.addWidget(self.widget_119)


        self.verticalLayout_88.addWidget(self.widget_167)


        self.verticalLayout_87.addWidget(self.widget_116)


        self.horizontalLayout_163.addWidget(self.widget_114)


        self.horizontalLayout_95.addWidget(self.widget_55)

        self.horizontalLayout_95.setStretch(1, 1)
        self.horizontalLayout_95.setStretch(3, 2)
        self.widget_10 = QWidget(Form)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(450, 130, 791, 101))
        self.widget_10.setStyleSheet(u"border: none;")
        self.horizontalLayout_42 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_42.setSpacing(5)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.widget_90 = QWidget(self.widget_10)
        self.widget_90.setObjectName(u"widget_90")
        self.widget_90.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_94 = QHBoxLayout(self.widget_90)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(15, 0, 15, 0)
        self.label_112 = QLabel(self.widget_90)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setFont(font1)

        self.horizontalLayout_94.addWidget(self.label_112)


        self.horizontalLayout_42.addWidget(self.widget_90)

        self.widget_139 = QWidget(self.widget_10)
        self.widget_139.setObjectName(u"widget_139")
        self.widget_139.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_128 = QHBoxLayout(self.widget_139)
        self.horizontalLayout_128.setSpacing(10)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.horizontalLayout_128.setContentsMargins(18, 15, 10, 5)
        self.widget_56 = QWidget(self.widget_139)
        self.widget_56.setObjectName(u"widget_56")
        self.widget_56.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout_125 = QHBoxLayout(self.widget_56)
        self.horizontalLayout_125.setSpacing(0)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalLayout_125.setContentsMargins(2, 2, 2, 2)
        self.refuel_start_time_input = QDoubleSpinBox(self.widget_56)
        self.refuel_start_time_input.setObjectName(u"refuel_start_time_input")
        sizePolicy.setHeightForWidth(self.refuel_start_time_input.sizePolicy().hasHeightForWidth())
        self.refuel_start_time_input.setSizePolicy(sizePolicy)
        self.refuel_start_time_input.setFont(font2)
        self.refuel_start_time_input.setStyleSheet(u"")
        self.refuel_start_time_input.setAlignment(Qt.AlignCenter)
        self.refuel_start_time_input.setReadOnly(False)
        self.refuel_start_time_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.refuel_start_time_input.setDecimals(1)
        self.refuel_start_time_input.setMaximum(999.000000000000000)
        self.refuel_start_time_input.setValue(0.000000000000000)

        self.horizontalLayout_125.addWidget(self.refuel_start_time_input)

        self.label_25 = QLabel(self.widget_56)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"border: none;\n"
"")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_125.addWidget(self.label_25)

        self.refuel_end_time_input = QDoubleSpinBox(self.widget_56)
        self.refuel_end_time_input.setObjectName(u"refuel_end_time_input")
        sizePolicy.setHeightForWidth(self.refuel_end_time_input.sizePolicy().hasHeightForWidth())
        self.refuel_end_time_input.setSizePolicy(sizePolicy)
        self.refuel_end_time_input.setFont(font2)
        self.refuel_end_time_input.setStyleSheet(u"")
        self.refuel_end_time_input.setAlignment(Qt.AlignCenter)
        self.refuel_end_time_input.setReadOnly(False)
        self.refuel_end_time_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.refuel_end_time_input.setDecimals(1)
        self.refuel_end_time_input.setMaximum(999.000000000000000)
        self.refuel_end_time_input.setValue(999.000000000000000)

        self.horizontalLayout_125.addWidget(self.refuel_end_time_input)


        self.horizontalLayout_128.addWidget(self.widget_56)

        self.horizontalLayout_128.setStretch(0, 2)

        self.horizontalLayout_42.addWidget(self.widget_139)

        self.widget_17 = QWidget(Form)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setGeometry(QRect(50, 20, 367, 860))
        self.widget_17.setStyleSheet(u"border-left: None;")
        self.verticalLayout_27 = QVBoxLayout(self.widget_17)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 5)
        self.widget_66 = QWidget(self.widget_17)
        self.widget_66.setObjectName(u"widget_66")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_66)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_28 = QWidget(self.widget_66)
        self.widget_28.setObjectName(u"widget_28")
        self.horizontalLayout_359 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_359.setObjectName(u"horizontalLayout_359")
        self.horizontalLayout_359.setContentsMargins(5, 5, 5, 5)
        self.label_55 = QLabel(self.widget_28)
        self.label_55.setObjectName(u"label_55")
        sizePolicy1.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        self.label_55.setFont(font3)
        self.label_55.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_359.addWidget(self.label_55)

        self.label_272 = QLabel(self.widget_28)
        self.label_272.setObjectName(u"label_272")

        self.horizontalLayout_359.addWidget(self.label_272)

        self.horizontalLayout_359.setStretch(1, 1)

        self.horizontalLayout_17.addWidget(self.widget_28)


        self.verticalLayout_27.addWidget(self.widget_66)

        self.widget_41 = QWidget(self.widget_17)
        self.widget_41.setObjectName(u"widget_41")
        self.widget_41.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"}\n"
"QSpinBox\n"
"{\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"}")
        self.verticalLayout_36 = QVBoxLayout(self.widget_41)
        self.verticalLayout_36.setSpacing(10)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.widget_197 = QWidget(self.widget_41)
        self.widget_197.setObjectName(u"widget_197")
        self.horizontalLayout_186 = QHBoxLayout(self.widget_197)
        self.horizontalLayout_186.setObjectName(u"horizontalLayout_186")
        self.horizontalLayout_186.setContentsMargins(0, 0, 0, 0)
        self.sv_value_A_49 = QDoubleSpinBox(self.widget_197)
        self.sv_value_A_49.setObjectName(u"sv_value_A_49")
        sizePolicy.setHeightForWidth(self.sv_value_A_49.sizePolicy().hasHeightForWidth())
        self.sv_value_A_49.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(15)
        font4.setBold(True)
        font4.setItalic(False)
        self.sv_value_A_49.setFont(font4)
        self.sv_value_A_49.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.sv_value_A_49.setAlignment(Qt.AlignCenter)
        self.sv_value_A_49.setReadOnly(True)
        self.sv_value_A_49.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_A_49.setDecimals(0)
        self.sv_value_A_49.setMaximum(999.000000000000000)

        self.horizontalLayout_186.addWidget(self.sv_value_A_49)

        self.label_185 = QLabel(self.widget_197)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setFont(font4)
        self.label_185.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_186.addWidget(self.label_185)

        self.horizontalLayout_186.setStretch(0, 4)
        self.horizontalLayout_186.setStretch(1, 1)

        self.verticalLayout_36.addWidget(self.widget_197)

        self.widget_199 = QWidget(self.widget_41)
        self.widget_199.setObjectName(u"widget_199")
        self.horizontalLayout_188 = QHBoxLayout(self.widget_199)
        self.horizontalLayout_188.setObjectName(u"horizontalLayout_188")
        self.horizontalLayout_188.setContentsMargins(0, 0, 0, 0)
        self.sv_value_A_50 = QDoubleSpinBox(self.widget_199)
        self.sv_value_A_50.setObjectName(u"sv_value_A_50")
        sizePolicy.setHeightForWidth(self.sv_value_A_50.sizePolicy().hasHeightForWidth())
        self.sv_value_A_50.setSizePolicy(sizePolicy)
        self.sv_value_A_50.setFont(font)
        self.sv_value_A_50.setAlignment(Qt.AlignCenter)
        self.sv_value_A_50.setReadOnly(True)
        self.sv_value_A_50.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_A_50.setDecimals(1)
        self.sv_value_A_50.setMaximum(999.000000000000000)

        self.horizontalLayout_188.addWidget(self.sv_value_A_50)

        self.label_186 = QLabel(self.widget_199)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setFont(font4)
        self.label_186.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_188.addWidget(self.label_186)

        self.horizontalLayout_188.setStretch(0, 4)
        self.horizontalLayout_188.setStretch(1, 1)

        self.verticalLayout_36.addWidget(self.widget_199)

        self.widget_201 = QWidget(self.widget_41)
        self.widget_201.setObjectName(u"widget_201")
        self.horizontalLayout_191 = QHBoxLayout(self.widget_201)
        self.horizontalLayout_191.setObjectName(u"horizontalLayout_191")
        self.horizontalLayout_191.setContentsMargins(0, 0, 0, 0)
        self.sv_value_A_51 = QDoubleSpinBox(self.widget_201)
        self.sv_value_A_51.setObjectName(u"sv_value_A_51")
        sizePolicy.setHeightForWidth(self.sv_value_A_51.sizePolicy().hasHeightForWidth())
        self.sv_value_A_51.setSizePolicy(sizePolicy)
        self.sv_value_A_51.setFont(font)
        self.sv_value_A_51.setAlignment(Qt.AlignCenter)
        self.sv_value_A_51.setReadOnly(True)
        self.sv_value_A_51.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.horizontalLayout_191.addWidget(self.sv_value_A_51)

        self.label_187 = QLabel(self.widget_201)
        self.label_187.setObjectName(u"label_187")
        self.label_187.setFont(font4)
        self.label_187.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_191.addWidget(self.label_187)

        self.horizontalLayout_191.setStretch(0, 4)
        self.horizontalLayout_191.setStretch(1, 1)

        self.verticalLayout_36.addWidget(self.widget_201)

        self.widget_205 = QWidget(self.widget_41)
        self.widget_205.setObjectName(u"widget_205")
        self.horizontalLayout_194 = QHBoxLayout(self.widget_205)
        self.horizontalLayout_194.setObjectName(u"horizontalLayout_194")
        self.horizontalLayout_194.setContentsMargins(0, 0, 0, 0)
        self.sv_value_A_53 = QSpinBox(self.widget_205)
        self.sv_value_A_53.setObjectName(u"sv_value_A_53")
        sizePolicy.setHeightForWidth(self.sv_value_A_53.sizePolicy().hasHeightForWidth())
        self.sv_value_A_53.setSizePolicy(sizePolicy)
        self.sv_value_A_53.setFont(font)
        self.sv_value_A_53.setAlignment(Qt.AlignCenter)
        self.sv_value_A_53.setReadOnly(True)
        self.sv_value_A_53.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_A_53.setMaximum(999)

        self.horizontalLayout_194.addWidget(self.sv_value_A_53)

        self.label_188 = QLabel(self.widget_205)
        self.label_188.setObjectName(u"label_188")
        self.label_188.setFont(font4)
        self.label_188.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_194.addWidget(self.label_188)

        self.horizontalLayout_194.setStretch(0, 4)
        self.horizontalLayout_194.setStretch(1, 1)

        self.verticalLayout_36.addWidget(self.widget_205)

        self.widget_207 = QWidget(self.widget_41)
        self.widget_207.setObjectName(u"widget_207")
        self.horizontalLayout_196 = QHBoxLayout(self.widget_207)
        self.horizontalLayout_196.setObjectName(u"horizontalLayout_196")
        self.horizontalLayout_196.setContentsMargins(0, 0, 0, 0)
        self.sv_value_A_54 = QDoubleSpinBox(self.widget_207)
        self.sv_value_A_54.setObjectName(u"sv_value_A_54")
        sizePolicy.setHeightForWidth(self.sv_value_A_54.sizePolicy().hasHeightForWidth())
        self.sv_value_A_54.setSizePolicy(sizePolicy)
        self.sv_value_A_54.setFont(font)
        self.sv_value_A_54.setAlignment(Qt.AlignCenter)
        self.sv_value_A_54.setReadOnly(True)
        self.sv_value_A_54.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_A_54.setDecimals(1)
        self.sv_value_A_54.setMaximum(999.000000000000000)

        self.horizontalLayout_196.addWidget(self.sv_value_A_54)

        self.label_189 = QLabel(self.widget_207)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setFont(font4)
        self.label_189.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_196.addWidget(self.label_189)

        self.horizontalLayout_196.setStretch(0, 4)
        self.horizontalLayout_196.setStretch(1, 1)

        self.verticalLayout_36.addWidget(self.widget_207)

        self.widget_208 = QWidget(self.widget_41)
        self.widget_208.setObjectName(u"widget_208")
        self.horizontalLayout_197 = QHBoxLayout(self.widget_208)
        self.horizontalLayout_197.setObjectName(u"horizontalLayout_197")
        self.horizontalLayout_197.setContentsMargins(0, 0, 0, 0)
        self.sv_value_A_55 = QDoubleSpinBox(self.widget_208)
        self.sv_value_A_55.setObjectName(u"sv_value_A_55")
        sizePolicy.setHeightForWidth(self.sv_value_A_55.sizePolicy().hasHeightForWidth())
        self.sv_value_A_55.setSizePolicy(sizePolicy)
        self.sv_value_A_55.setFont(font)
        self.sv_value_A_55.setStyleSheet(u"")
        self.sv_value_A_55.setAlignment(Qt.AlignCenter)
        self.sv_value_A_55.setReadOnly(True)
        self.sv_value_A_55.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_A_55.setDecimals(1)

        self.horizontalLayout_197.addWidget(self.sv_value_A_55)

        self.label_190 = QLabel(self.widget_208)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setFont(font4)
        self.label_190.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_197.addWidget(self.label_190)

        self.horizontalLayout_197.setStretch(0, 4)
        self.horizontalLayout_197.setStretch(1, 1)

        self.verticalLayout_36.addWidget(self.widget_208)

        self.widget_213 = QWidget(self.widget_41)
        self.widget_213.setObjectName(u"widget_213")
        self.horizontalLayout_202 = QHBoxLayout(self.widget_213)
        self.horizontalLayout_202.setObjectName(u"horizontalLayout_202")
        self.horizontalLayout_202.setContentsMargins(0, 0, 0, 0)
        self.sv_value_A_58 = QSpinBox(self.widget_213)
        self.sv_value_A_58.setObjectName(u"sv_value_A_58")
        sizePolicy.setHeightForWidth(self.sv_value_A_58.sizePolicy().hasHeightForWidth())
        self.sv_value_A_58.setSizePolicy(sizePolicy)
        self.sv_value_A_58.setFont(font)
        self.sv_value_A_58.setAlignment(Qt.AlignCenter)
        self.sv_value_A_58.setReadOnly(True)
        self.sv_value_A_58.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_A_58.setMaximum(999)

        self.horizontalLayout_202.addWidget(self.sv_value_A_58)

        self.label_191 = QLabel(self.widget_213)
        self.label_191.setObjectName(u"label_191")
        self.label_191.setFont(font4)
        self.label_191.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_202.addWidget(self.label_191)

        self.horizontalLayout_202.setStretch(0, 4)
        self.horizontalLayout_202.setStretch(1, 1)

        self.verticalLayout_36.addWidget(self.widget_213)

        self.widget_215 = QWidget(self.widget_41)
        self.widget_215.setObjectName(u"widget_215")
        self.horizontalLayout_204 = QHBoxLayout(self.widget_215)
        self.horizontalLayout_204.setObjectName(u"horizontalLayout_204")
        self.horizontalLayout_204.setContentsMargins(0, 0, 0, 0)
        self.sv_value_A_60 = QDoubleSpinBox(self.widget_215)
        self.sv_value_A_60.setObjectName(u"sv_value_A_60")
        sizePolicy.setHeightForWidth(self.sv_value_A_60.sizePolicy().hasHeightForWidth())
        self.sv_value_A_60.setSizePolicy(sizePolicy)
        self.sv_value_A_60.setFont(font)
        self.sv_value_A_60.setAlignment(Qt.AlignCenter)
        self.sv_value_A_60.setReadOnly(True)
        self.sv_value_A_60.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_A_60.setDecimals(1)

        self.horizontalLayout_204.addWidget(self.sv_value_A_60)

        self.label_192 = QLabel(self.widget_215)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setFont(font4)
        self.label_192.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_204.addWidget(self.label_192)

        self.horizontalLayout_204.setStretch(0, 4)
        self.horizontalLayout_204.setStretch(1, 1)

        self.verticalLayout_36.addWidget(self.widget_215)

        self.widget_216 = QWidget(self.widget_41)
        self.widget_216.setObjectName(u"widget_216")
        self.horizontalLayout_205 = QHBoxLayout(self.widget_216)
        self.horizontalLayout_205.setObjectName(u"horizontalLayout_205")
        self.horizontalLayout_205.setContentsMargins(0, 0, 0, 0)
        self.sv_value_A_61 = QDoubleSpinBox(self.widget_216)
        self.sv_value_A_61.setObjectName(u"sv_value_A_61")
        sizePolicy.setHeightForWidth(self.sv_value_A_61.sizePolicy().hasHeightForWidth())
        self.sv_value_A_61.setSizePolicy(sizePolicy)
        self.sv_value_A_61.setFont(font)
        self.sv_value_A_61.setAlignment(Qt.AlignCenter)
        self.sv_value_A_61.setReadOnly(True)
        self.sv_value_A_61.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_A_61.setMaximum(999.000000000000000)

        self.horizontalLayout_205.addWidget(self.sv_value_A_61)

        self.label_193 = QLabel(self.widget_216)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setFont(font4)
        self.label_193.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_205.addWidget(self.label_193)

        self.horizontalLayout_205.setStretch(0, 4)
        self.horizontalLayout_205.setStretch(1, 1)

        self.verticalLayout_36.addWidget(self.widget_216)

        self.widget_217 = QWidget(self.widget_41)
        self.widget_217.setObjectName(u"widget_217")
        self.horizontalLayout_206 = QHBoxLayout(self.widget_217)
        self.horizontalLayout_206.setObjectName(u"horizontalLayout_206")
        self.horizontalLayout_206.setContentsMargins(0, 0, 0, 0)
        self.widget_218 = QWidget(self.widget_217)
        self.widget_218.setObjectName(u"widget_218")
        self.horizontalLayout_207 = QHBoxLayout(self.widget_218)
        self.horizontalLayout_207.setObjectName(u"horizontalLayout_207")
        self.horizontalLayout_207.setContentsMargins(0, 0, 0, 0)
        self.sv_value_A_62 = QSpinBox(self.widget_218)
        self.sv_value_A_62.setObjectName(u"sv_value_A_62")
        sizePolicy.setHeightForWidth(self.sv_value_A_62.sizePolicy().hasHeightForWidth())
        self.sv_value_A_62.setSizePolicy(sizePolicy)
        self.sv_value_A_62.setFont(font)
        self.sv_value_A_62.setAlignment(Qt.AlignCenter)
        self.sv_value_A_62.setReadOnly(True)
        self.sv_value_A_62.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_A_62.setMaximum(999)

        self.horizontalLayout_207.addWidget(self.sv_value_A_62)

        self.label_194 = QLabel(self.widget_218)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setFont(font4)
        self.label_194.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_207.addWidget(self.label_194)

        self.horizontalLayout_207.setStretch(0, 4)
        self.horizontalLayout_207.setStretch(1, 1)

        self.horizontalLayout_206.addWidget(self.widget_218)

        self.horizontalLayout_206.setStretch(0, 1)

        self.verticalLayout_36.addWidget(self.widget_217)

        self.widget_219 = QWidget(self.widget_41)
        self.widget_219.setObjectName(u"widget_219")
        self.horizontalLayout_208 = QHBoxLayout(self.widget_219)
        self.horizontalLayout_208.setObjectName(u"horizontalLayout_208")
        self.horizontalLayout_208.setContentsMargins(0, 0, 0, 0)
        self.widget_220 = QWidget(self.widget_219)
        self.widget_220.setObjectName(u"widget_220")
        self.horizontalLayout_209 = QHBoxLayout(self.widget_220)
        self.horizontalLayout_209.setObjectName(u"horizontalLayout_209")
        self.horizontalLayout_209.setContentsMargins(0, 0, 0, 0)
        self.sv_value_A_63 = QDoubleSpinBox(self.widget_220)
        self.sv_value_A_63.setObjectName(u"sv_value_A_63")
        sizePolicy.setHeightForWidth(self.sv_value_A_63.sizePolicy().hasHeightForWidth())
        self.sv_value_A_63.setSizePolicy(sizePolicy)
        self.sv_value_A_63.setFont(font)
        self.sv_value_A_63.setAlignment(Qt.AlignCenter)
        self.sv_value_A_63.setReadOnly(True)
        self.sv_value_A_63.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_A_63.setDecimals(1)
        self.sv_value_A_63.setMaximum(999.000000000000000)

        self.horizontalLayout_209.addWidget(self.sv_value_A_63)

        self.label_195 = QLabel(self.widget_220)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setFont(font4)
        self.label_195.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_209.addWidget(self.label_195)

        self.horizontalLayout_209.setStretch(0, 4)
        self.horizontalLayout_209.setStretch(1, 1)

        self.horizontalLayout_208.addWidget(self.widget_220)

        self.horizontalLayout_208.setStretch(0, 1)

        self.verticalLayout_36.addWidget(self.widget_219)

        self.widget_221 = QWidget(self.widget_41)
        self.widget_221.setObjectName(u"widget_221")
        self.horizontalLayout_210 = QHBoxLayout(self.widget_221)
        self.horizontalLayout_210.setObjectName(u"horizontalLayout_210")
        self.horizontalLayout_210.setContentsMargins(0, 0, 0, 0)
        self.widget_222 = QWidget(self.widget_221)
        self.widget_222.setObjectName(u"widget_222")
        self.horizontalLayout_211 = QHBoxLayout(self.widget_222)
        self.horizontalLayout_211.setObjectName(u"horizontalLayout_211")
        self.horizontalLayout_211.setContentsMargins(0, 0, 0, 0)
        self.sv_value_A_64 = QSpinBox(self.widget_222)
        self.sv_value_A_64.setObjectName(u"sv_value_A_64")
        sizePolicy.setHeightForWidth(self.sv_value_A_64.sizePolicy().hasHeightForWidth())
        self.sv_value_A_64.setSizePolicy(sizePolicy)
        self.sv_value_A_64.setFont(font)
        self.sv_value_A_64.setAlignment(Qt.AlignCenter)
        self.sv_value_A_64.setReadOnly(True)
        self.sv_value_A_64.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.horizontalLayout_211.addWidget(self.sv_value_A_64)

        self.label_196 = QLabel(self.widget_222)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setFont(font4)
        self.label_196.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_211.addWidget(self.label_196)

        self.horizontalLayout_211.setStretch(0, 4)
        self.horizontalLayout_211.setStretch(1, 1)

        self.horizontalLayout_210.addWidget(self.widget_222)

        self.horizontalLayout_210.setStretch(0, 1)

        self.verticalLayout_36.addWidget(self.widget_221)


        self.verticalLayout_27.addWidget(self.widget_41)

        self.verticalLayout_27.setStretch(0, 1)
        self.verticalLayout_27.setStretch(1, 21)
        self.widget_16 = QWidget(Form)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setGeometry(QRect(1290, 80, 1113, 709))
        self.widget_16.setStyleSheet(u"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #d1d3d3,\n"
"        stop:1 #c3c7cc);")
        self.verticalLayout_9 = QVBoxLayout(self.widget_16)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_75 = QWidget(self.widget_16)
        self.widget_75.setObjectName(u"widget_75")
        sizePolicy.setHeightForWidth(self.widget_75.sizePolicy().hasHeightForWidth())
        self.widget_75.setSizePolicy(sizePolicy)
        self.widget_75.setStyleSheet(u"QWidget {\n"
"    background-color: white;\n"
"    border-left: 4px solid #FB8C00;\n"
"    border-radius: 6px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.horizontalLayout_193 = QHBoxLayout(self.widget_75)
        self.horizontalLayout_193.setSpacing(5)
        self.horizontalLayout_193.setObjectName(u"horizontalLayout_193")
        self.horizontalLayout_193.setContentsMargins(0, 5, 15, 5)
        self.widget_76 = QWidget(self.widget_75)
        self.widget_76.setObjectName(u"widget_76")
        self.horizontalLayout_195 = QHBoxLayout(self.widget_76)
        self.horizontalLayout_195.setObjectName(u"horizontalLayout_195")
        self.horizontalLayout_195.setContentsMargins(-1, 0, -1, 0)
        self.label_143 = QLabel(self.widget_76)
        self.label_143.setObjectName(u"label_143")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(20)
        font5.setBold(True)
        font5.setItalic(False)
        self.label_143.setFont(font5)
        self.label_143.setStyleSheet(u"border: none;\n"
"padding: 20px;\n"
"border-left: none;")
        self.label_143.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_195.addWidget(self.label_143)

        self.line_13 = QFrame(self.widget_76)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.VLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_195.addWidget(self.line_13)


        self.horizontalLayout_193.addWidget(self.widget_76)

        self.widget_78 = QWidget(self.widget_75)
        self.widget_78.setObjectName(u"widget_78")
        self.widget_78.setStyleSheet(u"QWidget{\n"
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
        self.verticalLayout_55 = QVBoxLayout(self.widget_78)
        self.verticalLayout_55.setSpacing(10)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.widget_200 = QWidget(self.widget_78)
        self.widget_200.setObjectName(u"widget_200")
        self.widget_200.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_312 = QHBoxLayout(self.widget_200)
        self.horizontalLayout_312.setSpacing(10)
        self.horizontalLayout_312.setObjectName(u"horizontalLayout_312")
        self.horizontalLayout_312.setContentsMargins(0, 0, 0, 0)
        self.sys_state_stacked_wid_28 = QStackedWidget(self.widget_200)
        self.sys_state_stacked_wid_28.setObjectName(u"sys_state_stacked_wid_28")
        sizePolicy1.setHeightForWidth(self.sys_state_stacked_wid_28.sizePolicy().hasHeightForWidth())
        self.sys_state_stacked_wid_28.setSizePolicy(sizePolicy1)
        self.sys_state_stacked_wid_28.setStyleSheet(u"QLabel{\n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"padding-right: 3px;\n"
"}")
        self.running_light_31 = QWidget()
        self.running_light_31.setObjectName(u"running_light_31")
        self.horizontalLayout_325 = QHBoxLayout(self.running_light_31)
        self.horizontalLayout_325.setObjectName(u"horizontalLayout_325")
        self.horizontalLayout_325.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.running_light_31)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        self.pushButton_2.setFont(font6)
        self.pushButton_2.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #10B981; \n"
"padding-right: 3px;")
        icon = QIcon()
        icon.addFile(u":/newPrefix/record-button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_325.addWidget(self.pushButton_2)

        self.sys_state_stacked_wid_28.addWidget(self.running_light_31)
        self.wating_light_31 = QWidget()
        self.wating_light_31.setObjectName(u"wating_light_31")
        self.horizontalLayout_326 = QHBoxLayout(self.wating_light_31)
        self.horizontalLayout_326.setObjectName(u"horizontalLayout_326")
        self.horizontalLayout_326.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.wating_light_31)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setFont(font6)
        self.pushButton.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #FB8C00; \n"
"padding-right: 3px;")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/record-button (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_326.addWidget(self.pushButton)

        self.sys_state_stacked_wid_28.addWidget(self.wating_light_31)
        self.error_light_31 = QWidget()
        self.error_light_31.setObjectName(u"error_light_31")
        self.horizontalLayout_327 = QHBoxLayout(self.error_light_31)
        self.horizontalLayout_327.setObjectName(u"horizontalLayout_327")
        self.horizontalLayout_327.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.error_light_31)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setFont(font6)
        self.pushButton_3.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #F90A0A; \n"
"padding-right: 3px;")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/record-button (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(30, 30))

        self.horizontalLayout_327.addWidget(self.pushButton_3)

        self.sys_state_stacked_wid_28.addWidget(self.error_light_31)

        self.horizontalLayout_312.addWidget(self.sys_state_stacked_wid_28)

        self.widget_103 = QWidget(self.widget_200)
        self.widget_103.setObjectName(u"widget_103")
        self.widget_103.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout_316 = QHBoxLayout(self.widget_103)
        self.horizontalLayout_316.setSpacing(0)
        self.horizontalLayout_316.setObjectName(u"horizontalLayout_316")
        self.horizontalLayout_316.setContentsMargins(2, 2, 2, 2)
        self.high_temp_input_21 = QDoubleSpinBox(self.widget_103)
        self.high_temp_input_21.setObjectName(u"high_temp_input_21")
        sizePolicy.setHeightForWidth(self.high_temp_input_21.sizePolicy().hasHeightForWidth())
        self.high_temp_input_21.setSizePolicy(sizePolicy)
        self.high_temp_input_21.setFont(font4)
        self.high_temp_input_21.setStyleSheet(u"")
        self.high_temp_input_21.setAlignment(Qt.AlignCenter)
        self.high_temp_input_21.setReadOnly(False)
        self.high_temp_input_21.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.high_temp_input_21.setDecimals(1)
        self.high_temp_input_21.setMaximum(999.000000000000000)
        self.high_temp_input_21.setValue(0.000000000000000)

        self.horizontalLayout_316.addWidget(self.high_temp_input_21)

        self.label_160 = QLabel(self.widget_103)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setFont(font)
        self.label_160.setStyleSheet(u"border: none;\n"
"")
        self.label_160.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_316.addWidget(self.label_160)

        self.pv_value_displ_21 = QDoubleSpinBox(self.widget_103)
        self.pv_value_displ_21.setObjectName(u"pv_value_displ_21")
        sizePolicy.setHeightForWidth(self.pv_value_displ_21.sizePolicy().hasHeightForWidth())
        self.pv_value_displ_21.setSizePolicy(sizePolicy)
        self.pv_value_displ_21.setFont(font4)
        self.pv_value_displ_21.setStyleSheet(u"")
        self.pv_value_displ_21.setAlignment(Qt.AlignCenter)
        self.pv_value_displ_21.setReadOnly(True)
        self.pv_value_displ_21.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pv_value_displ_21.setDecimals(1)
        self.pv_value_displ_21.setMaximum(999.000000000000000)
        self.pv_value_displ_21.setValue(0.000000000000000)

        self.horizontalLayout_316.addWidget(self.pv_value_displ_21)

        self.label_161 = QLabel(self.widget_103)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setFont(font)
        self.label_161.setStyleSheet(u"border: none;\n"
"")
        self.label_161.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_316.addWidget(self.label_161)

        self.low_temp_input_21 = QDoubleSpinBox(self.widget_103)
        self.low_temp_input_21.setObjectName(u"low_temp_input_21")
        sizePolicy.setHeightForWidth(self.low_temp_input_21.sizePolicy().hasHeightForWidth())
        self.low_temp_input_21.setSizePolicy(sizePolicy)
        self.low_temp_input_21.setFont(font4)
        self.low_temp_input_21.setStyleSheet(u"")
        self.low_temp_input_21.setAlignment(Qt.AlignCenter)
        self.low_temp_input_21.setReadOnly(False)
        self.low_temp_input_21.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.low_temp_input_21.setDecimals(1)
        self.low_temp_input_21.setMaximum(999.000000000000000)
        self.low_temp_input_21.setValue(0.000000000000000)

        self.horizontalLayout_316.addWidget(self.low_temp_input_21)


        self.horizontalLayout_312.addWidget(self.widget_103)

        self.sv_value_input_21 = QDoubleSpinBox(self.widget_200)
        self.sv_value_input_21.setObjectName(u"sv_value_input_21")
        sizePolicy.setHeightForWidth(self.sv_value_input_21.sizePolicy().hasHeightForWidth())
        self.sv_value_input_21.setSizePolicy(sizePolicy)
        self.sv_value_input_21.setFont(font4)
        self.sv_value_input_21.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.sv_value_input_21.setAlignment(Qt.AlignCenter)
        self.sv_value_input_21.setReadOnly(False)
        self.sv_value_input_21.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_input_21.setDecimals(1)
        self.sv_value_input_21.setMinimum(-999.000000000000000)
        self.sv_value_input_21.setMaximum(999.000000000000000)

        self.horizontalLayout_312.addWidget(self.sv_value_input_21)

        self.offset_value_input_21 = QDoubleSpinBox(self.widget_200)
        self.offset_value_input_21.setObjectName(u"offset_value_input_21")
        sizePolicy.setHeightForWidth(self.offset_value_input_21.sizePolicy().hasHeightForWidth())
        self.offset_value_input_21.setSizePolicy(sizePolicy)
        self.offset_value_input_21.setFont(font4)
        self.offset_value_input_21.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.offset_value_input_21.setAlignment(Qt.AlignCenter)
        self.offset_value_input_21.setReadOnly(False)
        self.offset_value_input_21.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.offset_value_input_21.setDecimals(1)
        self.offset_value_input_21.setMinimum(-99.000000000000000)
        self.offset_value_input_21.setMaximum(99.000000000000000)

        self.horizontalLayout_312.addWidget(self.offset_value_input_21)

        self.stackedWidget_27 = QStackedWidget(self.widget_200)
        self.stackedWidget_27.setObjectName(u"stackedWidget_27")
        self.celsius_displ_21 = QWidget()
        self.celsius_displ_21.setObjectName(u"celsius_displ_21")
        self.horizontalLayout_317 = QHBoxLayout(self.celsius_displ_21)
        self.horizontalLayout_317.setObjectName(u"horizontalLayout_317")
        self.horizontalLayout_317.setContentsMargins(0, 0, 0, 0)
        self.label_245 = QLabel(self.celsius_displ_21)
        self.label_245.setObjectName(u"label_245")
        self.label_245.setFont(font4)
        self.label_245.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_245.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_317.addWidget(self.label_245)

        self.stackedWidget_27.addWidget(self.celsius_displ_21)
        self.fahrenheit_displ_21 = QWidget()
        self.fahrenheit_displ_21.setObjectName(u"fahrenheit_displ_21")
        self.horizontalLayout_318 = QHBoxLayout(self.fahrenheit_displ_21)
        self.horizontalLayout_318.setObjectName(u"horizontalLayout_318")
        self.horizontalLayout_318.setContentsMargins(0, 0, 0, 0)
        self.label_246 = QLabel(self.fahrenheit_displ_21)
        self.label_246.setObjectName(u"label_246")
        self.label_246.setFont(font4)
        self.label_246.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_246.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_318.addWidget(self.label_246)

        self.stackedWidget_27.addWidget(self.fahrenheit_displ_21)

        self.horizontalLayout_312.addWidget(self.stackedWidget_27)

        self.horizontalLayout_312.setStretch(0, 1)
        self.horizontalLayout_312.setStretch(1, 2)
        self.horizontalLayout_312.setStretch(2, 1)
        self.horizontalLayout_312.setStretch(3, 1)

        self.verticalLayout_55.addWidget(self.widget_200)


        self.horizontalLayout_193.addWidget(self.widget_78)

        self.horizontalLayout_193.setStretch(0, 1)
        self.horizontalLayout_193.setStretch(1, 4)

        self.verticalLayout_9.addWidget(self.widget_75)

        self.widget_123 = QWidget(self.widget_16)
        self.widget_123.setObjectName(u"widget_123")
        sizePolicy.setHeightForWidth(self.widget_123.sizePolicy().hasHeightForWidth())
        self.widget_123.setSizePolicy(sizePolicy)
        self.widget_123.setStyleSheet(u"QWidget {\n"
"    background-color: white;\n"
"    border-left: 4px solid #FB8C00;\n"
"    border-radius: 6px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.horizontalLayout_411 = QHBoxLayout(self.widget_123)
        self.horizontalLayout_411.setSpacing(5)
        self.horizontalLayout_411.setObjectName(u"horizontalLayout_411")
        self.horizontalLayout_411.setContentsMargins(0, 5, 15, 5)
        self.widget_124 = QWidget(self.widget_123)
        self.widget_124.setObjectName(u"widget_124")
        self.horizontalLayout_412 = QHBoxLayout(self.widget_124)
        self.horizontalLayout_412.setObjectName(u"horizontalLayout_412")
        self.horizontalLayout_412.setContentsMargins(-1, 0, -1, 0)
        self.label_273 = QLabel(self.widget_124)
        self.label_273.setObjectName(u"label_273")
        self.label_273.setFont(font5)
        self.label_273.setStyleSheet(u"border: none;\n"
"padding: 20px;\n"
"border-left: none;")

        self.horizontalLayout_412.addWidget(self.label_273)

        self.line_16 = QFrame(self.widget_124)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.Shape.VLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_412.addWidget(self.line_16)

        self.widget_125 = QWidget(self.widget_124)
        self.widget_125.setObjectName(u"widget_125")
        self.widget_125.setStyleSheet(u"border-left: none;")
        self.verticalLayout_70 = QVBoxLayout(self.widget_125)
        self.verticalLayout_70.setSpacing(10)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.widget_127 = QWidget(self.widget_125)
        self.widget_127.setObjectName(u"widget_127")
        self.widget_127.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_414 = QHBoxLayout(self.widget_127)
        self.horizontalLayout_414.setObjectName(u"horizontalLayout_414")
        self.horizontalLayout_414.setContentsMargins(0, 0, 5, 0)
        self.label_274 = QLabel(self.widget_127)
        self.label_274.setObjectName(u"label_274")
        self.label_274.setFont(font1)

        self.horizontalLayout_414.addWidget(self.label_274)


        self.verticalLayout_70.addWidget(self.widget_127)

        self.widget_128 = QWidget(self.widget_125)
        self.widget_128.setObjectName(u"widget_128")
        self.widget_128.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_415 = QHBoxLayout(self.widget_128)
        self.horizontalLayout_415.setObjectName(u"horizontalLayout_415")
        self.horizontalLayout_415.setContentsMargins(0, 0, 5, 0)
        self.label_275 = QLabel(self.widget_128)
        self.label_275.setObjectName(u"label_275")
        self.label_275.setFont(font1)

        self.horizontalLayout_415.addWidget(self.label_275)


        self.verticalLayout_70.addWidget(self.widget_128)

        self.widget_129 = QWidget(self.widget_125)
        self.widget_129.setObjectName(u"widget_129")
        self.widget_129.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_416 = QHBoxLayout(self.widget_129)
        self.horizontalLayout_416.setObjectName(u"horizontalLayout_416")
        self.horizontalLayout_416.setContentsMargins(0, 0, 5, 0)
        self.label_276 = QLabel(self.widget_129)
        self.label_276.setObjectName(u"label_276")
        self.label_276.setFont(font1)

        self.horizontalLayout_416.addWidget(self.label_276)


        self.verticalLayout_70.addWidget(self.widget_129)


        self.horizontalLayout_412.addWidget(self.widget_125)

        self.line_17 = QFrame(self.widget_124)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.Shape.VLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_412.addWidget(self.line_17)


        self.horizontalLayout_411.addWidget(self.widget_124)

        self.widget_130 = QWidget(self.widget_123)
        self.widget_130.setObjectName(u"widget_130")
        self.widget_130.setStyleSheet(u"QWidget{\n"
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
        self.verticalLayout_71 = QVBoxLayout(self.widget_130)
        self.verticalLayout_71.setSpacing(10)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.widget_230 = QWidget(self.widget_130)
        self.widget_230.setObjectName(u"widget_230")
        self.widget_230.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_424 = QHBoxLayout(self.widget_230)
        self.horizontalLayout_424.setSpacing(10)
        self.horizontalLayout_424.setObjectName(u"horizontalLayout_424")
        self.horizontalLayout_424.setContentsMargins(0, 0, 0, 0)
        self.sys_state_stacked_wid_29 = QStackedWidget(self.widget_230)
        self.sys_state_stacked_wid_29.setObjectName(u"sys_state_stacked_wid_29")
        sizePolicy1.setHeightForWidth(self.sys_state_stacked_wid_29.sizePolicy().hasHeightForWidth())
        self.sys_state_stacked_wid_29.setSizePolicy(sizePolicy1)
        self.sys_state_stacked_wid_29.setStyleSheet(u"QLabel{\n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"padding-right: 3px;\n"
"}")
        self.running_light_41 = QWidget()
        self.running_light_41.setObjectName(u"running_light_41")
        self.horizontalLayout_372 = QHBoxLayout(self.running_light_41)
        self.horizontalLayout_372.setObjectName(u"horizontalLayout_372")
        self.horizontalLayout_372.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.running_light_41)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)
        self.pushButton_6.setFont(font6)
        self.pushButton_6.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #10B981; \n"
"padding-right: 3px;")
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QSize(30, 30))

        self.horizontalLayout_372.addWidget(self.pushButton_6)

        self.sys_state_stacked_wid_29.addWidget(self.running_light_41)
        self.wating_light_41 = QWidget()
        self.wating_light_41.setObjectName(u"wating_light_41")
        self.horizontalLayout_373 = QHBoxLayout(self.wating_light_41)
        self.horizontalLayout_373.setObjectName(u"horizontalLayout_373")
        self.horizontalLayout_373.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.wating_light_41)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy1.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy1)
        self.pushButton_7.setFont(font6)
        self.pushButton_7.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #FB8C00; \n"
"padding-right: 3px;")
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QSize(30, 30))

        self.horizontalLayout_373.addWidget(self.pushButton_7)

        self.sys_state_stacked_wid_29.addWidget(self.wating_light_41)
        self.error_light_41 = QWidget()
        self.error_light_41.setObjectName(u"error_light_41")
        self.horizontalLayout_379 = QHBoxLayout(self.error_light_41)
        self.horizontalLayout_379.setObjectName(u"horizontalLayout_379")
        self.horizontalLayout_379.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.error_light_41)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy1.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy1)
        self.pushButton_8.setFont(font6)
        self.pushButton_8.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #F90A0A; \n"
"padding-right: 3px;")
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QSize(30, 30))

        self.horizontalLayout_379.addWidget(self.pushButton_8)

        self.sys_state_stacked_wid_29.addWidget(self.error_light_41)

        self.horizontalLayout_424.addWidget(self.sys_state_stacked_wid_29)

        self.widget_186 = QWidget(self.widget_230)
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
        self.horizontalLayout_428 = QHBoxLayout(self.widget_186)
        self.horizontalLayout_428.setSpacing(0)
        self.horizontalLayout_428.setObjectName(u"horizontalLayout_428")
        self.horizontalLayout_428.setContentsMargins(2, 2, 2, 2)
        self.high_temp_input_34 = QDoubleSpinBox(self.widget_186)
        self.high_temp_input_34.setObjectName(u"high_temp_input_34")
        sizePolicy.setHeightForWidth(self.high_temp_input_34.sizePolicy().hasHeightForWidth())
        self.high_temp_input_34.setSizePolicy(sizePolicy)
        self.high_temp_input_34.setFont(font4)
        self.high_temp_input_34.setStyleSheet(u"")
        self.high_temp_input_34.setAlignment(Qt.AlignCenter)
        self.high_temp_input_34.setReadOnly(False)
        self.high_temp_input_34.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.high_temp_input_34.setDecimals(1)
        self.high_temp_input_34.setMaximum(999.000000000000000)
        self.high_temp_input_34.setValue(0.000000000000000)

        self.horizontalLayout_428.addWidget(self.high_temp_input_34)

        self.label_281 = QLabel(self.widget_186)
        self.label_281.setObjectName(u"label_281")
        self.label_281.setFont(font)
        self.label_281.setStyleSheet(u"border: none;\n"
"")
        self.label_281.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_428.addWidget(self.label_281)

        self.pv_value_displ_34 = QDoubleSpinBox(self.widget_186)
        self.pv_value_displ_34.setObjectName(u"pv_value_displ_34")
        sizePolicy.setHeightForWidth(self.pv_value_displ_34.sizePolicy().hasHeightForWidth())
        self.pv_value_displ_34.setSizePolicy(sizePolicy)
        self.pv_value_displ_34.setFont(font4)
        self.pv_value_displ_34.setStyleSheet(u"")
        self.pv_value_displ_34.setAlignment(Qt.AlignCenter)
        self.pv_value_displ_34.setReadOnly(True)
        self.pv_value_displ_34.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pv_value_displ_34.setDecimals(1)
        self.pv_value_displ_34.setMaximum(999.000000000000000)
        self.pv_value_displ_34.setValue(0.000000000000000)

        self.horizontalLayout_428.addWidget(self.pv_value_displ_34)

        self.label_282 = QLabel(self.widget_186)
        self.label_282.setObjectName(u"label_282")
        self.label_282.setFont(font)
        self.label_282.setStyleSheet(u"border: none;\n"
"")
        self.label_282.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_428.addWidget(self.label_282)

        self.low_temp_input_34 = QDoubleSpinBox(self.widget_186)
        self.low_temp_input_34.setObjectName(u"low_temp_input_34")
        sizePolicy.setHeightForWidth(self.low_temp_input_34.sizePolicy().hasHeightForWidth())
        self.low_temp_input_34.setSizePolicy(sizePolicy)
        self.low_temp_input_34.setFont(font4)
        self.low_temp_input_34.setStyleSheet(u"")
        self.low_temp_input_34.setAlignment(Qt.AlignCenter)
        self.low_temp_input_34.setReadOnly(False)
        self.low_temp_input_34.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.low_temp_input_34.setDecimals(1)
        self.low_temp_input_34.setMaximum(999.000000000000000)
        self.low_temp_input_34.setValue(0.000000000000000)

        self.horizontalLayout_428.addWidget(self.low_temp_input_34)


        self.horizontalLayout_424.addWidget(self.widget_186)

        self.sv_value_input_34 = QDoubleSpinBox(self.widget_230)
        self.sv_value_input_34.setObjectName(u"sv_value_input_34")
        sizePolicy.setHeightForWidth(self.sv_value_input_34.sizePolicy().hasHeightForWidth())
        self.sv_value_input_34.setSizePolicy(sizePolicy)
        self.sv_value_input_34.setFont(font4)
        self.sv_value_input_34.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.sv_value_input_34.setAlignment(Qt.AlignCenter)
        self.sv_value_input_34.setReadOnly(False)
        self.sv_value_input_34.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_input_34.setDecimals(1)
        self.sv_value_input_34.setMinimum(-999.000000000000000)
        self.sv_value_input_34.setMaximum(999.000000000000000)

        self.horizontalLayout_424.addWidget(self.sv_value_input_34)

        self.offset_value_input_34 = QDoubleSpinBox(self.widget_230)
        self.offset_value_input_34.setObjectName(u"offset_value_input_34")
        sizePolicy.setHeightForWidth(self.offset_value_input_34.sizePolicy().hasHeightForWidth())
        self.offset_value_input_34.setSizePolicy(sizePolicy)
        self.offset_value_input_34.setFont(font4)
        self.offset_value_input_34.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.offset_value_input_34.setAlignment(Qt.AlignCenter)
        self.offset_value_input_34.setReadOnly(False)
        self.offset_value_input_34.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.offset_value_input_34.setDecimals(1)
        self.offset_value_input_34.setMinimum(-99.000000000000000)
        self.offset_value_input_34.setMaximum(99.000000000000000)

        self.horizontalLayout_424.addWidget(self.offset_value_input_34)

        self.stackedWidget_40 = QStackedWidget(self.widget_230)
        self.stackedWidget_40.setObjectName(u"stackedWidget_40")
        self.celsius_displ_34 = QWidget()
        self.celsius_displ_34.setObjectName(u"celsius_displ_34")
        self.horizontalLayout_429 = QHBoxLayout(self.celsius_displ_34)
        self.horizontalLayout_429.setObjectName(u"horizontalLayout_429")
        self.horizontalLayout_429.setContentsMargins(0, 0, 0, 0)
        self.label_283 = QLabel(self.celsius_displ_34)
        self.label_283.setObjectName(u"label_283")
        self.label_283.setFont(font4)
        self.label_283.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_283.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_429.addWidget(self.label_283)

        self.stackedWidget_40.addWidget(self.celsius_displ_34)
        self.fahrenheit_displ_34 = QWidget()
        self.fahrenheit_displ_34.setObjectName(u"fahrenheit_displ_34")
        self.horizontalLayout_430 = QHBoxLayout(self.fahrenheit_displ_34)
        self.horizontalLayout_430.setObjectName(u"horizontalLayout_430")
        self.horizontalLayout_430.setContentsMargins(0, 0, 0, 0)
        self.label_284 = QLabel(self.fahrenheit_displ_34)
        self.label_284.setObjectName(u"label_284")
        self.label_284.setFont(font4)
        self.label_284.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_284.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_430.addWidget(self.label_284)

        self.stackedWidget_40.addWidget(self.fahrenheit_displ_34)

        self.horizontalLayout_424.addWidget(self.stackedWidget_40)

        self.horizontalLayout_424.setStretch(0, 1)
        self.horizontalLayout_424.setStretch(1, 2)
        self.horizontalLayout_424.setStretch(2, 1)
        self.horizontalLayout_424.setStretch(3, 1)

        self.verticalLayout_71.addWidget(self.widget_230)

        self.widget_239 = QWidget(self.widget_130)
        self.widget_239.setObjectName(u"widget_239")
        self.widget_239.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_431 = QHBoxLayout(self.widget_239)
        self.horizontalLayout_431.setSpacing(10)
        self.horizontalLayout_431.setObjectName(u"horizontalLayout_431")
        self.horizontalLayout_431.setContentsMargins(0, 0, 0, 0)
        self.sys_state_stacked_wid_30 = QStackedWidget(self.widget_239)
        self.sys_state_stacked_wid_30.setObjectName(u"sys_state_stacked_wid_30")
        sizePolicy1.setHeightForWidth(self.sys_state_stacked_wid_30.sizePolicy().hasHeightForWidth())
        self.sys_state_stacked_wid_30.setSizePolicy(sizePolicy1)
        self.sys_state_stacked_wid_30.setStyleSheet(u"QLabel{\n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"padding-right: 3px;\n"
"}")
        self.running_light_42 = QWidget()
        self.running_light_42.setObjectName(u"running_light_42")
        self.horizontalLayout_383 = QHBoxLayout(self.running_light_42)
        self.horizontalLayout_383.setObjectName(u"horizontalLayout_383")
        self.horizontalLayout_383.setContentsMargins(0, 0, 0, 0)
        self.pushButton_9 = QPushButton(self.running_light_42)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy1.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy1)
        self.pushButton_9.setFont(font6)
        self.pushButton_9.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #10B981; \n"
"padding-right: 3px;")
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setIconSize(QSize(30, 30))

        self.horizontalLayout_383.addWidget(self.pushButton_9)

        self.sys_state_stacked_wid_30.addWidget(self.running_light_42)
        self.wating_light_42 = QWidget()
        self.wating_light_42.setObjectName(u"wating_light_42")
        self.horizontalLayout_384 = QHBoxLayout(self.wating_light_42)
        self.horizontalLayout_384.setObjectName(u"horizontalLayout_384")
        self.horizontalLayout_384.setContentsMargins(0, 0, 0, 0)
        self.pushButton_10 = QPushButton(self.wating_light_42)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy1.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy1)
        self.pushButton_10.setFont(font6)
        self.pushButton_10.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #FB8C00; \n"
"padding-right: 3px;")
        self.pushButton_10.setIcon(icon1)
        self.pushButton_10.setIconSize(QSize(30, 30))

        self.horizontalLayout_384.addWidget(self.pushButton_10)

        self.sys_state_stacked_wid_30.addWidget(self.wating_light_42)
        self.error_light_42 = QWidget()
        self.error_light_42.setObjectName(u"error_light_42")
        self.horizontalLayout_385 = QHBoxLayout(self.error_light_42)
        self.horizontalLayout_385.setObjectName(u"horizontalLayout_385")
        self.horizontalLayout_385.setContentsMargins(0, 0, 0, 0)
        self.pushButton_11 = QPushButton(self.error_light_42)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy1.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy1)
        self.pushButton_11.setFont(font6)
        self.pushButton_11.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #F90A0A; \n"
"padding-right: 3px;")
        self.pushButton_11.setIcon(icon2)
        self.pushButton_11.setIconSize(QSize(30, 30))

        self.horizontalLayout_385.addWidget(self.pushButton_11)

        self.sys_state_stacked_wid_30.addWidget(self.error_light_42)

        self.horizontalLayout_431.addWidget(self.sys_state_stacked_wid_30)

        self.widget_187 = QWidget(self.widget_239)
        self.widget_187.setObjectName(u"widget_187")
        self.widget_187.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout_435 = QHBoxLayout(self.widget_187)
        self.horizontalLayout_435.setSpacing(0)
        self.horizontalLayout_435.setObjectName(u"horizontalLayout_435")
        self.horizontalLayout_435.setContentsMargins(2, 2, 2, 2)
        self.high_temp_input_35 = QDoubleSpinBox(self.widget_187)
        self.high_temp_input_35.setObjectName(u"high_temp_input_35")
        sizePolicy.setHeightForWidth(self.high_temp_input_35.sizePolicy().hasHeightForWidth())
        self.high_temp_input_35.setSizePolicy(sizePolicy)
        self.high_temp_input_35.setFont(font4)
        self.high_temp_input_35.setStyleSheet(u"")
        self.high_temp_input_35.setAlignment(Qt.AlignCenter)
        self.high_temp_input_35.setReadOnly(False)
        self.high_temp_input_35.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.high_temp_input_35.setDecimals(1)
        self.high_temp_input_35.setMaximum(999.000000000000000)
        self.high_temp_input_35.setValue(0.000000000000000)

        self.horizontalLayout_435.addWidget(self.high_temp_input_35)

        self.label_285 = QLabel(self.widget_187)
        self.label_285.setObjectName(u"label_285")
        self.label_285.setFont(font)
        self.label_285.setStyleSheet(u"border: none;\n"
"")
        self.label_285.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_435.addWidget(self.label_285)

        self.pv_value_displ_35 = QDoubleSpinBox(self.widget_187)
        self.pv_value_displ_35.setObjectName(u"pv_value_displ_35")
        sizePolicy.setHeightForWidth(self.pv_value_displ_35.sizePolicy().hasHeightForWidth())
        self.pv_value_displ_35.setSizePolicy(sizePolicy)
        self.pv_value_displ_35.setFont(font4)
        self.pv_value_displ_35.setStyleSheet(u"")
        self.pv_value_displ_35.setAlignment(Qt.AlignCenter)
        self.pv_value_displ_35.setReadOnly(True)
        self.pv_value_displ_35.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pv_value_displ_35.setDecimals(1)
        self.pv_value_displ_35.setMaximum(999.000000000000000)
        self.pv_value_displ_35.setValue(0.000000000000000)

        self.horizontalLayout_435.addWidget(self.pv_value_displ_35)

        self.label_286 = QLabel(self.widget_187)
        self.label_286.setObjectName(u"label_286")
        self.label_286.setFont(font)
        self.label_286.setStyleSheet(u"border: none;\n"
"")
        self.label_286.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_435.addWidget(self.label_286)

        self.low_temp_input_35 = QDoubleSpinBox(self.widget_187)
        self.low_temp_input_35.setObjectName(u"low_temp_input_35")
        sizePolicy.setHeightForWidth(self.low_temp_input_35.sizePolicy().hasHeightForWidth())
        self.low_temp_input_35.setSizePolicy(sizePolicy)
        self.low_temp_input_35.setFont(font4)
        self.low_temp_input_35.setStyleSheet(u"")
        self.low_temp_input_35.setAlignment(Qt.AlignCenter)
        self.low_temp_input_35.setReadOnly(False)
        self.low_temp_input_35.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.low_temp_input_35.setDecimals(1)
        self.low_temp_input_35.setMaximum(999.000000000000000)
        self.low_temp_input_35.setValue(0.000000000000000)

        self.horizontalLayout_435.addWidget(self.low_temp_input_35)


        self.horizontalLayout_431.addWidget(self.widget_187)

        self.sv_value_input_35 = QDoubleSpinBox(self.widget_239)
        self.sv_value_input_35.setObjectName(u"sv_value_input_35")
        sizePolicy.setHeightForWidth(self.sv_value_input_35.sizePolicy().hasHeightForWidth())
        self.sv_value_input_35.setSizePolicy(sizePolicy)
        self.sv_value_input_35.setFont(font4)
        self.sv_value_input_35.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.sv_value_input_35.setAlignment(Qt.AlignCenter)
        self.sv_value_input_35.setReadOnly(False)
        self.sv_value_input_35.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_input_35.setDecimals(1)
        self.sv_value_input_35.setMinimum(-999.000000000000000)
        self.sv_value_input_35.setMaximum(999.000000000000000)

        self.horizontalLayout_431.addWidget(self.sv_value_input_35)

        self.offset_value_input_35 = QDoubleSpinBox(self.widget_239)
        self.offset_value_input_35.setObjectName(u"offset_value_input_35")
        sizePolicy.setHeightForWidth(self.offset_value_input_35.sizePolicy().hasHeightForWidth())
        self.offset_value_input_35.setSizePolicy(sizePolicy)
        self.offset_value_input_35.setFont(font4)
        self.offset_value_input_35.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.offset_value_input_35.setAlignment(Qt.AlignCenter)
        self.offset_value_input_35.setReadOnly(False)
        self.offset_value_input_35.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.offset_value_input_35.setDecimals(1)
        self.offset_value_input_35.setMinimum(-99.000000000000000)
        self.offset_value_input_35.setMaximum(99.000000000000000)

        self.horizontalLayout_431.addWidget(self.offset_value_input_35)

        self.stackedWidget_41 = QStackedWidget(self.widget_239)
        self.stackedWidget_41.setObjectName(u"stackedWidget_41")
        self.celsius_displ_35 = QWidget()
        self.celsius_displ_35.setObjectName(u"celsius_displ_35")
        self.horizontalLayout_436 = QHBoxLayout(self.celsius_displ_35)
        self.horizontalLayout_436.setObjectName(u"horizontalLayout_436")
        self.horizontalLayout_436.setContentsMargins(0, 0, 0, 0)
        self.label_287 = QLabel(self.celsius_displ_35)
        self.label_287.setObjectName(u"label_287")
        self.label_287.setFont(font4)
        self.label_287.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_287.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_436.addWidget(self.label_287)

        self.stackedWidget_41.addWidget(self.celsius_displ_35)
        self.fahrenheit_displ_35 = QWidget()
        self.fahrenheit_displ_35.setObjectName(u"fahrenheit_displ_35")
        self.horizontalLayout_437 = QHBoxLayout(self.fahrenheit_displ_35)
        self.horizontalLayout_437.setObjectName(u"horizontalLayout_437")
        self.horizontalLayout_437.setContentsMargins(0, 0, 0, 0)
        self.label_288 = QLabel(self.fahrenheit_displ_35)
        self.label_288.setObjectName(u"label_288")
        self.label_288.setFont(font4)
        self.label_288.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_288.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_437.addWidget(self.label_288)

        self.stackedWidget_41.addWidget(self.fahrenheit_displ_35)

        self.horizontalLayout_431.addWidget(self.stackedWidget_41)

        self.horizontalLayout_431.setStretch(0, 1)
        self.horizontalLayout_431.setStretch(1, 2)
        self.horizontalLayout_431.setStretch(2, 1)
        self.horizontalLayout_431.setStretch(3, 1)

        self.verticalLayout_71.addWidget(self.widget_239)

        self.widget_240 = QWidget(self.widget_130)
        self.widget_240.setObjectName(u"widget_240")
        self.widget_240.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_438 = QHBoxLayout(self.widget_240)
        self.horizontalLayout_438.setSpacing(10)
        self.horizontalLayout_438.setObjectName(u"horizontalLayout_438")
        self.horizontalLayout_438.setContentsMargins(0, 0, 0, 0)
        self.sys_state_stacked_wid_31 = QStackedWidget(self.widget_240)
        self.sys_state_stacked_wid_31.setObjectName(u"sys_state_stacked_wid_31")
        sizePolicy1.setHeightForWidth(self.sys_state_stacked_wid_31.sizePolicy().hasHeightForWidth())
        self.sys_state_stacked_wid_31.setSizePolicy(sizePolicy1)
        self.sys_state_stacked_wid_31.setStyleSheet(u"QLabel{\n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"padding-right: 3px;\n"
"}")
        self.running_light_43 = QWidget()
        self.running_light_43.setObjectName(u"running_light_43")
        self.horizontalLayout_386 = QHBoxLayout(self.running_light_43)
        self.horizontalLayout_386.setObjectName(u"horizontalLayout_386")
        self.horizontalLayout_386.setContentsMargins(0, 0, 0, 0)
        self.pushButton_12 = QPushButton(self.running_light_43)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy1.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy1)
        self.pushButton_12.setFont(font6)
        self.pushButton_12.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #10B981; \n"
"padding-right: 3px;")
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setIconSize(QSize(30, 30))

        self.horizontalLayout_386.addWidget(self.pushButton_12)

        self.sys_state_stacked_wid_31.addWidget(self.running_light_43)
        self.wating_light_43 = QWidget()
        self.wating_light_43.setObjectName(u"wating_light_43")
        self.horizontalLayout_387 = QHBoxLayout(self.wating_light_43)
        self.horizontalLayout_387.setObjectName(u"horizontalLayout_387")
        self.horizontalLayout_387.setContentsMargins(0, 0, 0, 0)
        self.pushButton_13 = QPushButton(self.wating_light_43)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy1.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy1)
        self.pushButton_13.setFont(font6)
        self.pushButton_13.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #FB8C00; \n"
"padding-right: 3px;")
        self.pushButton_13.setIcon(icon1)
        self.pushButton_13.setIconSize(QSize(30, 30))

        self.horizontalLayout_387.addWidget(self.pushButton_13)

        self.sys_state_stacked_wid_31.addWidget(self.wating_light_43)
        self.error_light_43 = QWidget()
        self.error_light_43.setObjectName(u"error_light_43")
        self.horizontalLayout_388 = QHBoxLayout(self.error_light_43)
        self.horizontalLayout_388.setObjectName(u"horizontalLayout_388")
        self.horizontalLayout_388.setContentsMargins(0, 0, 0, 0)
        self.pushButton_14 = QPushButton(self.error_light_43)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy1.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy1)
        self.pushButton_14.setFont(font6)
        self.pushButton_14.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #F90A0A; \n"
"padding-right: 3px;")
        self.pushButton_14.setIcon(icon2)
        self.pushButton_14.setIconSize(QSize(30, 30))

        self.horizontalLayout_388.addWidget(self.pushButton_14)

        self.sys_state_stacked_wid_31.addWidget(self.error_light_43)

        self.horizontalLayout_438.addWidget(self.sys_state_stacked_wid_31)

        self.widget_188 = QWidget(self.widget_240)
        self.widget_188.setObjectName(u"widget_188")
        self.widget_188.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout_442 = QHBoxLayout(self.widget_188)
        self.horizontalLayout_442.setSpacing(0)
        self.horizontalLayout_442.setObjectName(u"horizontalLayout_442")
        self.horizontalLayout_442.setContentsMargins(2, 2, 2, 2)
        self.high_temp_input_36 = QDoubleSpinBox(self.widget_188)
        self.high_temp_input_36.setObjectName(u"high_temp_input_36")
        sizePolicy.setHeightForWidth(self.high_temp_input_36.sizePolicy().hasHeightForWidth())
        self.high_temp_input_36.setSizePolicy(sizePolicy)
        self.high_temp_input_36.setFont(font4)
        self.high_temp_input_36.setStyleSheet(u"")
        self.high_temp_input_36.setAlignment(Qt.AlignCenter)
        self.high_temp_input_36.setReadOnly(False)
        self.high_temp_input_36.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.high_temp_input_36.setDecimals(1)
        self.high_temp_input_36.setMaximum(999.000000000000000)
        self.high_temp_input_36.setValue(0.000000000000000)

        self.horizontalLayout_442.addWidget(self.high_temp_input_36)

        self.label_289 = QLabel(self.widget_188)
        self.label_289.setObjectName(u"label_289")
        self.label_289.setFont(font)
        self.label_289.setStyleSheet(u"border: none;\n"
"")
        self.label_289.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_442.addWidget(self.label_289)

        self.pv_value_displ_36 = QDoubleSpinBox(self.widget_188)
        self.pv_value_displ_36.setObjectName(u"pv_value_displ_36")
        sizePolicy.setHeightForWidth(self.pv_value_displ_36.sizePolicy().hasHeightForWidth())
        self.pv_value_displ_36.setSizePolicy(sizePolicy)
        self.pv_value_displ_36.setFont(font4)
        self.pv_value_displ_36.setStyleSheet(u"")
        self.pv_value_displ_36.setAlignment(Qt.AlignCenter)
        self.pv_value_displ_36.setReadOnly(True)
        self.pv_value_displ_36.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pv_value_displ_36.setDecimals(1)
        self.pv_value_displ_36.setMaximum(999.000000000000000)
        self.pv_value_displ_36.setValue(0.000000000000000)

        self.horizontalLayout_442.addWidget(self.pv_value_displ_36)

        self.label_290 = QLabel(self.widget_188)
        self.label_290.setObjectName(u"label_290")
        self.label_290.setFont(font)
        self.label_290.setStyleSheet(u"border: none;\n"
"")
        self.label_290.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_442.addWidget(self.label_290)

        self.low_temp_input_36 = QDoubleSpinBox(self.widget_188)
        self.low_temp_input_36.setObjectName(u"low_temp_input_36")
        sizePolicy.setHeightForWidth(self.low_temp_input_36.sizePolicy().hasHeightForWidth())
        self.low_temp_input_36.setSizePolicy(sizePolicy)
        self.low_temp_input_36.setFont(font4)
        self.low_temp_input_36.setStyleSheet(u"")
        self.low_temp_input_36.setAlignment(Qt.AlignCenter)
        self.low_temp_input_36.setReadOnly(False)
        self.low_temp_input_36.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.low_temp_input_36.setDecimals(1)
        self.low_temp_input_36.setMaximum(999.000000000000000)
        self.low_temp_input_36.setValue(0.000000000000000)

        self.horizontalLayout_442.addWidget(self.low_temp_input_36)


        self.horizontalLayout_438.addWidget(self.widget_188)

        self.sv_value_input_36 = QDoubleSpinBox(self.widget_240)
        self.sv_value_input_36.setObjectName(u"sv_value_input_36")
        sizePolicy.setHeightForWidth(self.sv_value_input_36.sizePolicy().hasHeightForWidth())
        self.sv_value_input_36.setSizePolicy(sizePolicy)
        self.sv_value_input_36.setFont(font4)
        self.sv_value_input_36.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.sv_value_input_36.setAlignment(Qt.AlignCenter)
        self.sv_value_input_36.setReadOnly(False)
        self.sv_value_input_36.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_input_36.setDecimals(1)
        self.sv_value_input_36.setMinimum(-999.000000000000000)
        self.sv_value_input_36.setMaximum(999.000000000000000)

        self.horizontalLayout_438.addWidget(self.sv_value_input_36)

        self.offset_value_input_36 = QDoubleSpinBox(self.widget_240)
        self.offset_value_input_36.setObjectName(u"offset_value_input_36")
        sizePolicy.setHeightForWidth(self.offset_value_input_36.sizePolicy().hasHeightForWidth())
        self.offset_value_input_36.setSizePolicy(sizePolicy)
        self.offset_value_input_36.setFont(font4)
        self.offset_value_input_36.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.offset_value_input_36.setAlignment(Qt.AlignCenter)
        self.offset_value_input_36.setReadOnly(True)
        self.offset_value_input_36.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.offset_value_input_36.setDecimals(1)
        self.offset_value_input_36.setMinimum(-99.000000000000000)
        self.offset_value_input_36.setMaximum(99.000000000000000)

        self.horizontalLayout_438.addWidget(self.offset_value_input_36)

        self.stackedWidget_42 = QStackedWidget(self.widget_240)
        self.stackedWidget_42.setObjectName(u"stackedWidget_42")
        self.celsius_displ_36 = QWidget()
        self.celsius_displ_36.setObjectName(u"celsius_displ_36")
        self.horizontalLayout_443 = QHBoxLayout(self.celsius_displ_36)
        self.horizontalLayout_443.setObjectName(u"horizontalLayout_443")
        self.horizontalLayout_443.setContentsMargins(0, 0, 0, 0)
        self.label_291 = QLabel(self.celsius_displ_36)
        self.label_291.setObjectName(u"label_291")
        self.label_291.setFont(font4)
        self.label_291.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_291.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_443.addWidget(self.label_291)

        self.stackedWidget_42.addWidget(self.celsius_displ_36)
        self.fahrenheit_displ_36 = QWidget()
        self.fahrenheit_displ_36.setObjectName(u"fahrenheit_displ_36")
        self.horizontalLayout_444 = QHBoxLayout(self.fahrenheit_displ_36)
        self.horizontalLayout_444.setObjectName(u"horizontalLayout_444")
        self.horizontalLayout_444.setContentsMargins(0, 0, 0, 0)
        self.label_292 = QLabel(self.fahrenheit_displ_36)
        self.label_292.setObjectName(u"label_292")
        self.label_292.setFont(font4)
        self.label_292.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_292.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_444.addWidget(self.label_292)

        self.stackedWidget_42.addWidget(self.fahrenheit_displ_36)

        self.horizontalLayout_438.addWidget(self.stackedWidget_42)

        self.horizontalLayout_438.setStretch(0, 1)
        self.horizontalLayout_438.setStretch(1, 2)
        self.horizontalLayout_438.setStretch(2, 1)
        self.horizontalLayout_438.setStretch(3, 1)

        self.verticalLayout_71.addWidget(self.widget_240)


        self.horizontalLayout_411.addWidget(self.widget_130)

        self.horizontalLayout_411.setStretch(0, 1)
        self.horizontalLayout_411.setStretch(1, 4)

        self.verticalLayout_9.addWidget(self.widget_123)

        self.widget_94 = QWidget(self.widget_16)
        self.widget_94.setObjectName(u"widget_94")
        sizePolicy.setHeightForWidth(self.widget_94.sizePolicy().hasHeightForWidth())
        self.widget_94.setSizePolicy(sizePolicy)
        self.widget_94.setStyleSheet(u"QWidget {\n"
"    background-color: white;\n"
"    border-left: 4px solid #FB8C00;\n"
"    border-radius: 6px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.horizontalLayout_377 = QHBoxLayout(self.widget_94)
        self.horizontalLayout_377.setSpacing(5)
        self.horizontalLayout_377.setObjectName(u"horizontalLayout_377")
        self.horizontalLayout_377.setContentsMargins(0, 5, 15, 5)
        self.widget_95 = QWidget(self.widget_94)
        self.widget_95.setObjectName(u"widget_95")
        self.horizontalLayout_378 = QHBoxLayout(self.widget_95)
        self.horizontalLayout_378.setObjectName(u"horizontalLayout_378")
        self.horizontalLayout_378.setContentsMargins(-1, 0, -1, 0)
        self.label_180 = QLabel(self.widget_95)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setFont(font5)
        self.label_180.setStyleSheet(u"border: none;\n"
"padding: 20px;\n"
"border-left: none;")

        self.horizontalLayout_378.addWidget(self.label_180)

        self.line_12 = QFrame(self.widget_95)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.VLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_378.addWidget(self.line_12)

        self.widget_96 = QWidget(self.widget_95)
        self.widget_96.setObjectName(u"widget_96")
        self.widget_96.setStyleSheet(u"border-left: none;")
        self.verticalLayout_72 = QVBoxLayout(self.widget_96)
        self.verticalLayout_72.setSpacing(10)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.widget_117 = QWidget(self.widget_96)
        self.widget_117.setObjectName(u"widget_117")
        self.widget_117.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_380 = QHBoxLayout(self.widget_117)
        self.horizontalLayout_380.setObjectName(u"horizontalLayout_380")
        self.horizontalLayout_380.setContentsMargins(0, 0, 5, 0)
        self.label_197 = QLabel(self.widget_117)
        self.label_197.setObjectName(u"label_197")
        self.label_197.setFont(font1)

        self.horizontalLayout_380.addWidget(self.label_197)


        self.verticalLayout_72.addWidget(self.widget_117)

        self.widget_118 = QWidget(self.widget_96)
        self.widget_118.setObjectName(u"widget_118")
        self.widget_118.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_381 = QHBoxLayout(self.widget_118)
        self.horizontalLayout_381.setObjectName(u"horizontalLayout_381")
        self.horizontalLayout_381.setContentsMargins(0, 0, 5, 0)
        self.label_198 = QLabel(self.widget_118)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setFont(font1)

        self.horizontalLayout_381.addWidget(self.label_198)


        self.verticalLayout_72.addWidget(self.widget_118)

        self.widget_120 = QWidget(self.widget_96)
        self.widget_120.setObjectName(u"widget_120")
        self.widget_120.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_382 = QHBoxLayout(self.widget_120)
        self.horizontalLayout_382.setObjectName(u"horizontalLayout_382")
        self.horizontalLayout_382.setContentsMargins(0, 0, 5, 0)
        self.label_199 = QLabel(self.widget_120)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setFont(font1)

        self.horizontalLayout_382.addWidget(self.label_199)


        self.verticalLayout_72.addWidget(self.widget_120)


        self.horizontalLayout_378.addWidget(self.widget_96)

        self.line_15 = QFrame(self.widget_95)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.Shape.VLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_378.addWidget(self.line_15)


        self.horizontalLayout_377.addWidget(self.widget_95)

        self.widget_97 = QWidget(self.widget_94)
        self.widget_97.setObjectName(u"widget_97")
        self.widget_97.setStyleSheet(u"QWidget{\n"
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
        self.verticalLayout_73 = QVBoxLayout(self.widget_97)
        self.verticalLayout_73.setSpacing(10)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.widget_214 = QWidget(self.widget_97)
        self.widget_214.setObjectName(u"widget_214")
        self.widget_214.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_390 = QHBoxLayout(self.widget_214)
        self.horizontalLayout_390.setSpacing(10)
        self.horizontalLayout_390.setObjectName(u"horizontalLayout_390")
        self.horizontalLayout_390.setContentsMargins(0, 0, 0, 0)
        self.sys_state_stacked_wid_32 = QStackedWidget(self.widget_214)
        self.sys_state_stacked_wid_32.setObjectName(u"sys_state_stacked_wid_32")
        sizePolicy1.setHeightForWidth(self.sys_state_stacked_wid_32.sizePolicy().hasHeightForWidth())
        self.sys_state_stacked_wid_32.setSizePolicy(sizePolicy1)
        self.sys_state_stacked_wid_32.setStyleSheet(u"QLabel{\n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"padding-right: 3px;\n"
"}")
        self.running_light_44 = QWidget()
        self.running_light_44.setObjectName(u"running_light_44")
        self.horizontalLayout_389 = QHBoxLayout(self.running_light_44)
        self.horizontalLayout_389.setObjectName(u"horizontalLayout_389")
        self.horizontalLayout_389.setContentsMargins(0, 0, 0, 0)
        self.pushButton_15 = QPushButton(self.running_light_44)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy1.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy1)
        self.pushButton_15.setFont(font6)
        self.pushButton_15.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #10B981; \n"
"padding-right: 3px;")
        self.pushButton_15.setIcon(icon)
        self.pushButton_15.setIconSize(QSize(30, 30))

        self.horizontalLayout_389.addWidget(self.pushButton_15)

        self.sys_state_stacked_wid_32.addWidget(self.running_light_44)
        self.wating_light_44 = QWidget()
        self.wating_light_44.setObjectName(u"wating_light_44")
        self.horizontalLayout_391 = QHBoxLayout(self.wating_light_44)
        self.horizontalLayout_391.setObjectName(u"horizontalLayout_391")
        self.horizontalLayout_391.setContentsMargins(0, 0, 0, 0)
        self.pushButton_16 = QPushButton(self.wating_light_44)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy1.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy1)
        self.pushButton_16.setFont(font6)
        self.pushButton_16.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #FB8C00; \n"
"padding-right: 3px;")
        self.pushButton_16.setIcon(icon1)
        self.pushButton_16.setIconSize(QSize(30, 30))

        self.horizontalLayout_391.addWidget(self.pushButton_16)

        self.sys_state_stacked_wid_32.addWidget(self.wating_light_44)
        self.error_light_44 = QWidget()
        self.error_light_44.setObjectName(u"error_light_44")
        self.horizontalLayout_392 = QHBoxLayout(self.error_light_44)
        self.horizontalLayout_392.setObjectName(u"horizontalLayout_392")
        self.horizontalLayout_392.setContentsMargins(0, 0, 0, 0)
        self.pushButton_17 = QPushButton(self.error_light_44)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy1.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy1)
        self.pushButton_17.setFont(font6)
        self.pushButton_17.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #F90A0A; \n"
"padding-right: 3px;")
        self.pushButton_17.setIcon(icon2)
        self.pushButton_17.setIconSize(QSize(30, 30))

        self.horizontalLayout_392.addWidget(self.pushButton_17)

        self.sys_state_stacked_wid_32.addWidget(self.error_light_44)

        self.horizontalLayout_390.addWidget(self.sys_state_stacked_wid_32)

        self.widget_121 = QWidget(self.widget_214)
        self.widget_121.setObjectName(u"widget_121")
        self.widget_121.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout_394 = QHBoxLayout(self.widget_121)
        self.horizontalLayout_394.setSpacing(0)
        self.horizontalLayout_394.setObjectName(u"horizontalLayout_394")
        self.horizontalLayout_394.setContentsMargins(2, 2, 2, 2)
        self.high_temp_input_30 = QDoubleSpinBox(self.widget_121)
        self.high_temp_input_30.setObjectName(u"high_temp_input_30")
        sizePolicy.setHeightForWidth(self.high_temp_input_30.sizePolicy().hasHeightForWidth())
        self.high_temp_input_30.setSizePolicy(sizePolicy)
        self.high_temp_input_30.setFont(font4)
        self.high_temp_input_30.setStyleSheet(u"")
        self.high_temp_input_30.setAlignment(Qt.AlignCenter)
        self.high_temp_input_30.setReadOnly(False)
        self.high_temp_input_30.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.high_temp_input_30.setDecimals(1)
        self.high_temp_input_30.setMaximum(999.000000000000000)
        self.high_temp_input_30.setValue(0.000000000000000)

        self.horizontalLayout_394.addWidget(self.high_temp_input_30)

        self.label_233 = QLabel(self.widget_121)
        self.label_233.setObjectName(u"label_233")
        self.label_233.setFont(font)
        self.label_233.setStyleSheet(u"border: none;\n"
"")
        self.label_233.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_394.addWidget(self.label_233)

        self.pv_value_displ_30 = QDoubleSpinBox(self.widget_121)
        self.pv_value_displ_30.setObjectName(u"pv_value_displ_30")
        sizePolicy.setHeightForWidth(self.pv_value_displ_30.sizePolicy().hasHeightForWidth())
        self.pv_value_displ_30.setSizePolicy(sizePolicy)
        self.pv_value_displ_30.setFont(font4)
        self.pv_value_displ_30.setStyleSheet(u"")
        self.pv_value_displ_30.setAlignment(Qt.AlignCenter)
        self.pv_value_displ_30.setReadOnly(True)
        self.pv_value_displ_30.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pv_value_displ_30.setDecimals(1)
        self.pv_value_displ_30.setMaximum(999.000000000000000)
        self.pv_value_displ_30.setValue(0.000000000000000)

        self.horizontalLayout_394.addWidget(self.pv_value_displ_30)

        self.label_234 = QLabel(self.widget_121)
        self.label_234.setObjectName(u"label_234")
        self.label_234.setFont(font)
        self.label_234.setStyleSheet(u"border: none;\n"
"")
        self.label_234.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_394.addWidget(self.label_234)

        self.low_temp_input_30 = QDoubleSpinBox(self.widget_121)
        self.low_temp_input_30.setObjectName(u"low_temp_input_30")
        sizePolicy.setHeightForWidth(self.low_temp_input_30.sizePolicy().hasHeightForWidth())
        self.low_temp_input_30.setSizePolicy(sizePolicy)
        self.low_temp_input_30.setFont(font4)
        self.low_temp_input_30.setStyleSheet(u"")
        self.low_temp_input_30.setAlignment(Qt.AlignCenter)
        self.low_temp_input_30.setReadOnly(False)
        self.low_temp_input_30.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.low_temp_input_30.setDecimals(1)
        self.low_temp_input_30.setMaximum(999.000000000000000)
        self.low_temp_input_30.setValue(0.000000000000000)

        self.horizontalLayout_394.addWidget(self.low_temp_input_30)


        self.horizontalLayout_390.addWidget(self.widget_121)

        self.sv_value_input_30 = QDoubleSpinBox(self.widget_214)
        self.sv_value_input_30.setObjectName(u"sv_value_input_30")
        sizePolicy.setHeightForWidth(self.sv_value_input_30.sizePolicy().hasHeightForWidth())
        self.sv_value_input_30.setSizePolicy(sizePolicy)
        self.sv_value_input_30.setFont(font4)
        self.sv_value_input_30.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.sv_value_input_30.setAlignment(Qt.AlignCenter)
        self.sv_value_input_30.setReadOnly(False)
        self.sv_value_input_30.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_input_30.setDecimals(1)
        self.sv_value_input_30.setMinimum(-999.000000000000000)
        self.sv_value_input_30.setMaximum(999.000000000000000)

        self.horizontalLayout_390.addWidget(self.sv_value_input_30)

        self.offset_value_input_30 = QDoubleSpinBox(self.widget_214)
        self.offset_value_input_30.setObjectName(u"offset_value_input_30")
        sizePolicy.setHeightForWidth(self.offset_value_input_30.sizePolicy().hasHeightForWidth())
        self.offset_value_input_30.setSizePolicy(sizePolicy)
        self.offset_value_input_30.setFont(font4)
        self.offset_value_input_30.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.offset_value_input_30.setAlignment(Qt.AlignCenter)
        self.offset_value_input_30.setReadOnly(False)
        self.offset_value_input_30.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.offset_value_input_30.setDecimals(1)
        self.offset_value_input_30.setMinimum(-99.000000000000000)
        self.offset_value_input_30.setMaximum(99.000000000000000)

        self.horizontalLayout_390.addWidget(self.offset_value_input_30)

        self.stackedWidget_36 = QStackedWidget(self.widget_214)
        self.stackedWidget_36.setObjectName(u"stackedWidget_36")
        self.celsius_displ_30 = QWidget()
        self.celsius_displ_30.setObjectName(u"celsius_displ_30")
        self.horizontalLayout_395 = QHBoxLayout(self.celsius_displ_30)
        self.horizontalLayout_395.setObjectName(u"horizontalLayout_395")
        self.horizontalLayout_395.setContentsMargins(0, 0, 0, 0)
        self.label_263 = QLabel(self.celsius_displ_30)
        self.label_263.setObjectName(u"label_263")
        self.label_263.setFont(font4)
        self.label_263.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_263.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_395.addWidget(self.label_263)

        self.stackedWidget_36.addWidget(self.celsius_displ_30)
        self.fahrenheit_displ_30 = QWidget()
        self.fahrenheit_displ_30.setObjectName(u"fahrenheit_displ_30")
        self.horizontalLayout_396 = QHBoxLayout(self.fahrenheit_displ_30)
        self.horizontalLayout_396.setObjectName(u"horizontalLayout_396")
        self.horizontalLayout_396.setContentsMargins(0, 0, 0, 0)
        self.label_264 = QLabel(self.fahrenheit_displ_30)
        self.label_264.setObjectName(u"label_264")
        self.label_264.setFont(font4)
        self.label_264.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_264.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_396.addWidget(self.label_264)

        self.stackedWidget_36.addWidget(self.fahrenheit_displ_30)

        self.horizontalLayout_390.addWidget(self.stackedWidget_36)

        self.horizontalLayout_390.setStretch(0, 1)
        self.horizontalLayout_390.setStretch(1, 2)
        self.horizontalLayout_390.setStretch(2, 1)
        self.horizontalLayout_390.setStretch(3, 1)

        self.verticalLayout_73.addWidget(self.widget_214)

        self.widget_223 = QWidget(self.widget_97)
        self.widget_223.setObjectName(u"widget_223")
        self.widget_223.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_397 = QHBoxLayout(self.widget_223)
        self.horizontalLayout_397.setSpacing(10)
        self.horizontalLayout_397.setObjectName(u"horizontalLayout_397")
        self.horizontalLayout_397.setContentsMargins(0, 0, 0, 0)
        self.sys_state_stacked_wid_33 = QStackedWidget(self.widget_223)
        self.sys_state_stacked_wid_33.setObjectName(u"sys_state_stacked_wid_33")
        sizePolicy1.setHeightForWidth(self.sys_state_stacked_wid_33.sizePolicy().hasHeightForWidth())
        self.sys_state_stacked_wid_33.setSizePolicy(sizePolicy1)
        self.sys_state_stacked_wid_33.setStyleSheet(u"QLabel{\n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"padding-right: 3px;\n"
"}")
        self.running_light_45 = QWidget()
        self.running_light_45.setObjectName(u"running_light_45")
        self.horizontalLayout_393 = QHBoxLayout(self.running_light_45)
        self.horizontalLayout_393.setObjectName(u"horizontalLayout_393")
        self.horizontalLayout_393.setContentsMargins(0, 0, 0, 0)
        self.pushButton_18 = QPushButton(self.running_light_45)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy1.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy1)
        self.pushButton_18.setFont(font6)
        self.pushButton_18.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #10B981; \n"
"padding-right: 3px;")
        self.pushButton_18.setIcon(icon)
        self.pushButton_18.setIconSize(QSize(30, 30))

        self.horizontalLayout_393.addWidget(self.pushButton_18)

        self.sys_state_stacked_wid_33.addWidget(self.running_light_45)
        self.wating_light_45 = QWidget()
        self.wating_light_45.setObjectName(u"wating_light_45")
        self.horizontalLayout_398 = QHBoxLayout(self.wating_light_45)
        self.horizontalLayout_398.setObjectName(u"horizontalLayout_398")
        self.horizontalLayout_398.setContentsMargins(0, 0, 0, 0)
        self.pushButton_19 = QPushButton(self.wating_light_45)
        self.pushButton_19.setObjectName(u"pushButton_19")
        sizePolicy1.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy1)
        self.pushButton_19.setFont(font6)
        self.pushButton_19.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #FB8C00; \n"
"padding-right: 3px;")
        self.pushButton_19.setIcon(icon1)
        self.pushButton_19.setIconSize(QSize(30, 30))

        self.horizontalLayout_398.addWidget(self.pushButton_19)

        self.sys_state_stacked_wid_33.addWidget(self.wating_light_45)
        self.error_light_45 = QWidget()
        self.error_light_45.setObjectName(u"error_light_45")
        self.horizontalLayout_399 = QHBoxLayout(self.error_light_45)
        self.horizontalLayout_399.setObjectName(u"horizontalLayout_399")
        self.horizontalLayout_399.setContentsMargins(0, 0, 0, 0)
        self.pushButton_20 = QPushButton(self.error_light_45)
        self.pushButton_20.setObjectName(u"pushButton_20")
        sizePolicy1.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy1)
        self.pushButton_20.setFont(font6)
        self.pushButton_20.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #F90A0A; \n"
"padding-right: 3px;")
        self.pushButton_20.setIcon(icon2)
        self.pushButton_20.setIconSize(QSize(30, 30))

        self.horizontalLayout_399.addWidget(self.pushButton_20)

        self.sys_state_stacked_wid_33.addWidget(self.error_light_45)

        self.horizontalLayout_397.addWidget(self.sys_state_stacked_wid_33)

        self.widget_122 = QWidget(self.widget_223)
        self.widget_122.setObjectName(u"widget_122")
        self.widget_122.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout_401 = QHBoxLayout(self.widget_122)
        self.horizontalLayout_401.setSpacing(0)
        self.horizontalLayout_401.setObjectName(u"horizontalLayout_401")
        self.horizontalLayout_401.setContentsMargins(2, 2, 2, 2)
        self.high_temp_input_31 = QDoubleSpinBox(self.widget_122)
        self.high_temp_input_31.setObjectName(u"high_temp_input_31")
        sizePolicy.setHeightForWidth(self.high_temp_input_31.sizePolicy().hasHeightForWidth())
        self.high_temp_input_31.setSizePolicy(sizePolicy)
        self.high_temp_input_31.setFont(font4)
        self.high_temp_input_31.setStyleSheet(u"")
        self.high_temp_input_31.setAlignment(Qt.AlignCenter)
        self.high_temp_input_31.setReadOnly(False)
        self.high_temp_input_31.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.high_temp_input_31.setDecimals(1)
        self.high_temp_input_31.setMaximum(999.000000000000000)
        self.high_temp_input_31.setValue(0.000000000000000)

        self.horizontalLayout_401.addWidget(self.high_temp_input_31)

        self.label_235 = QLabel(self.widget_122)
        self.label_235.setObjectName(u"label_235")
        self.label_235.setFont(font)
        self.label_235.setStyleSheet(u"border: none;\n"
"")
        self.label_235.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_401.addWidget(self.label_235)

        self.pv_value_displ_31 = QDoubleSpinBox(self.widget_122)
        self.pv_value_displ_31.setObjectName(u"pv_value_displ_31")
        sizePolicy.setHeightForWidth(self.pv_value_displ_31.sizePolicy().hasHeightForWidth())
        self.pv_value_displ_31.setSizePolicy(sizePolicy)
        self.pv_value_displ_31.setFont(font4)
        self.pv_value_displ_31.setStyleSheet(u"")
        self.pv_value_displ_31.setAlignment(Qt.AlignCenter)
        self.pv_value_displ_31.setReadOnly(True)
        self.pv_value_displ_31.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pv_value_displ_31.setDecimals(1)
        self.pv_value_displ_31.setMaximum(999.000000000000000)
        self.pv_value_displ_31.setValue(0.000000000000000)

        self.horizontalLayout_401.addWidget(self.pv_value_displ_31)

        self.label_236 = QLabel(self.widget_122)
        self.label_236.setObjectName(u"label_236")
        self.label_236.setFont(font)
        self.label_236.setStyleSheet(u"border: none;\n"
"")
        self.label_236.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_401.addWidget(self.label_236)

        self.low_temp_input_31 = QDoubleSpinBox(self.widget_122)
        self.low_temp_input_31.setObjectName(u"low_temp_input_31")
        sizePolicy.setHeightForWidth(self.low_temp_input_31.sizePolicy().hasHeightForWidth())
        self.low_temp_input_31.setSizePolicy(sizePolicy)
        self.low_temp_input_31.setFont(font4)
        self.low_temp_input_31.setStyleSheet(u"")
        self.low_temp_input_31.setAlignment(Qt.AlignCenter)
        self.low_temp_input_31.setReadOnly(False)
        self.low_temp_input_31.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.low_temp_input_31.setDecimals(1)
        self.low_temp_input_31.setMaximum(999.000000000000000)
        self.low_temp_input_31.setValue(0.000000000000000)

        self.horizontalLayout_401.addWidget(self.low_temp_input_31)


        self.horizontalLayout_397.addWidget(self.widget_122)

        self.sv_value_input_31 = QDoubleSpinBox(self.widget_223)
        self.sv_value_input_31.setObjectName(u"sv_value_input_31")
        sizePolicy.setHeightForWidth(self.sv_value_input_31.sizePolicy().hasHeightForWidth())
        self.sv_value_input_31.setSizePolicy(sizePolicy)
        self.sv_value_input_31.setFont(font4)
        self.sv_value_input_31.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.sv_value_input_31.setAlignment(Qt.AlignCenter)
        self.sv_value_input_31.setReadOnly(False)
        self.sv_value_input_31.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_input_31.setDecimals(1)
        self.sv_value_input_31.setMinimum(-999.000000000000000)
        self.sv_value_input_31.setMaximum(999.000000000000000)

        self.horizontalLayout_397.addWidget(self.sv_value_input_31)

        self.offset_value_input_31 = QDoubleSpinBox(self.widget_223)
        self.offset_value_input_31.setObjectName(u"offset_value_input_31")
        sizePolicy.setHeightForWidth(self.offset_value_input_31.sizePolicy().hasHeightForWidth())
        self.offset_value_input_31.setSizePolicy(sizePolicy)
        self.offset_value_input_31.setFont(font4)
        self.offset_value_input_31.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.offset_value_input_31.setAlignment(Qt.AlignCenter)
        self.offset_value_input_31.setReadOnly(False)
        self.offset_value_input_31.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.offset_value_input_31.setDecimals(1)
        self.offset_value_input_31.setMinimum(-99.000000000000000)
        self.offset_value_input_31.setMaximum(99.000000000000000)

        self.horizontalLayout_397.addWidget(self.offset_value_input_31)

        self.stackedWidget_37 = QStackedWidget(self.widget_223)
        self.stackedWidget_37.setObjectName(u"stackedWidget_37")
        self.celsius_displ_31 = QWidget()
        self.celsius_displ_31.setObjectName(u"celsius_displ_31")
        self.horizontalLayout_402 = QHBoxLayout(self.celsius_displ_31)
        self.horizontalLayout_402.setObjectName(u"horizontalLayout_402")
        self.horizontalLayout_402.setContentsMargins(0, 0, 0, 0)
        self.label_265 = QLabel(self.celsius_displ_31)
        self.label_265.setObjectName(u"label_265")
        self.label_265.setFont(font4)
        self.label_265.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_265.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_402.addWidget(self.label_265)

        self.stackedWidget_37.addWidget(self.celsius_displ_31)
        self.fahrenheit_displ_31 = QWidget()
        self.fahrenheit_displ_31.setObjectName(u"fahrenheit_displ_31")
        self.horizontalLayout_403 = QHBoxLayout(self.fahrenheit_displ_31)
        self.horizontalLayout_403.setObjectName(u"horizontalLayout_403")
        self.horizontalLayout_403.setContentsMargins(0, 0, 0, 0)
        self.label_266 = QLabel(self.fahrenheit_displ_31)
        self.label_266.setObjectName(u"label_266")
        self.label_266.setFont(font4)
        self.label_266.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_266.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_403.addWidget(self.label_266)

        self.stackedWidget_37.addWidget(self.fahrenheit_displ_31)

        self.horizontalLayout_397.addWidget(self.stackedWidget_37)

        self.horizontalLayout_397.setStretch(0, 1)
        self.horizontalLayout_397.setStretch(1, 2)
        self.horizontalLayout_397.setStretch(2, 1)
        self.horizontalLayout_397.setStretch(3, 1)

        self.verticalLayout_73.addWidget(self.widget_223)

        self.widget_224 = QWidget(self.widget_97)
        self.widget_224.setObjectName(u"widget_224")
        self.widget_224.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_404 = QHBoxLayout(self.widget_224)
        self.horizontalLayout_404.setSpacing(10)
        self.horizontalLayout_404.setObjectName(u"horizontalLayout_404")
        self.horizontalLayout_404.setContentsMargins(0, 0, 0, 0)
        self.sys_state_stacked_wid_34 = QStackedWidget(self.widget_224)
        self.sys_state_stacked_wid_34.setObjectName(u"sys_state_stacked_wid_34")
        sizePolicy1.setHeightForWidth(self.sys_state_stacked_wid_34.sizePolicy().hasHeightForWidth())
        self.sys_state_stacked_wid_34.setSizePolicy(sizePolicy1)
        self.sys_state_stacked_wid_34.setStyleSheet(u"QLabel{\n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"padding-right: 3px;\n"
"}")
        self.running_light_47 = QWidget()
        self.running_light_47.setObjectName(u"running_light_47")
        self.horizontalLayout_407 = QHBoxLayout(self.running_light_47)
        self.horizontalLayout_407.setObjectName(u"horizontalLayout_407")
        self.horizontalLayout_407.setContentsMargins(0, 0, 0, 0)
        self.pushButton_24 = QPushButton(self.running_light_47)
        self.pushButton_24.setObjectName(u"pushButton_24")
        sizePolicy1.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy1)
        self.pushButton_24.setFont(font6)
        self.pushButton_24.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #10B981; \n"
"padding-right: 3px;")
        self.pushButton_24.setIcon(icon)
        self.pushButton_24.setIconSize(QSize(30, 30))

        self.horizontalLayout_407.addWidget(self.pushButton_24)

        self.sys_state_stacked_wid_34.addWidget(self.running_light_47)
        self.wating_light_47 = QWidget()
        self.wating_light_47.setObjectName(u"wating_light_47")
        self.horizontalLayout_413 = QHBoxLayout(self.wating_light_47)
        self.horizontalLayout_413.setObjectName(u"horizontalLayout_413")
        self.horizontalLayout_413.setContentsMargins(0, 0, 0, 0)
        self.pushButton_25 = QPushButton(self.wating_light_47)
        self.pushButton_25.setObjectName(u"pushButton_25")
        sizePolicy1.setHeightForWidth(self.pushButton_25.sizePolicy().hasHeightForWidth())
        self.pushButton_25.setSizePolicy(sizePolicy1)
        self.pushButton_25.setFont(font6)
        self.pushButton_25.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #FB8C00; \n"
"padding-right: 3px;")
        self.pushButton_25.setIcon(icon1)
        self.pushButton_25.setIconSize(QSize(30, 30))

        self.horizontalLayout_413.addWidget(self.pushButton_25)

        self.sys_state_stacked_wid_34.addWidget(self.wating_light_47)
        self.error_light_47 = QWidget()
        self.error_light_47.setObjectName(u"error_light_47")
        self.horizontalLayout_417 = QHBoxLayout(self.error_light_47)
        self.horizontalLayout_417.setObjectName(u"horizontalLayout_417")
        self.horizontalLayout_417.setContentsMargins(0, 0, 0, 0)
        self.pushButton_26 = QPushButton(self.error_light_47)
        self.pushButton_26.setObjectName(u"pushButton_26")
        sizePolicy1.setHeightForWidth(self.pushButton_26.sizePolicy().hasHeightForWidth())
        self.pushButton_26.setSizePolicy(sizePolicy1)
        self.pushButton_26.setFont(font6)
        self.pushButton_26.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #F90A0A; \n"
"padding-right: 3px;")
        self.pushButton_26.setIcon(icon2)
        self.pushButton_26.setIconSize(QSize(30, 30))

        self.horizontalLayout_417.addWidget(self.pushButton_26)

        self.sys_state_stacked_wid_34.addWidget(self.error_light_47)

        self.horizontalLayout_404.addWidget(self.sys_state_stacked_wid_34)

        self.widget_126 = QWidget(self.widget_224)
        self.widget_126.setObjectName(u"widget_126")
        self.widget_126.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout_408 = QHBoxLayout(self.widget_126)
        self.horizontalLayout_408.setSpacing(0)
        self.horizontalLayout_408.setObjectName(u"horizontalLayout_408")
        self.horizontalLayout_408.setContentsMargins(2, 2, 2, 2)
        self.high_temp_input_32 = QDoubleSpinBox(self.widget_126)
        self.high_temp_input_32.setObjectName(u"high_temp_input_32")
        sizePolicy.setHeightForWidth(self.high_temp_input_32.sizePolicy().hasHeightForWidth())
        self.high_temp_input_32.setSizePolicy(sizePolicy)
        self.high_temp_input_32.setFont(font4)
        self.high_temp_input_32.setStyleSheet(u"")
        self.high_temp_input_32.setAlignment(Qt.AlignCenter)
        self.high_temp_input_32.setReadOnly(False)
        self.high_temp_input_32.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.high_temp_input_32.setDecimals(1)
        self.high_temp_input_32.setMaximum(999.000000000000000)
        self.high_temp_input_32.setValue(0.000000000000000)

        self.horizontalLayout_408.addWidget(self.high_temp_input_32)

        self.label_267 = QLabel(self.widget_126)
        self.label_267.setObjectName(u"label_267")
        self.label_267.setFont(font)
        self.label_267.setStyleSheet(u"border: none;\n"
"")
        self.label_267.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_408.addWidget(self.label_267)

        self.pv_value_displ_32 = QDoubleSpinBox(self.widget_126)
        self.pv_value_displ_32.setObjectName(u"pv_value_displ_32")
        sizePolicy.setHeightForWidth(self.pv_value_displ_32.sizePolicy().hasHeightForWidth())
        self.pv_value_displ_32.setSizePolicy(sizePolicy)
        self.pv_value_displ_32.setFont(font4)
        self.pv_value_displ_32.setStyleSheet(u"")
        self.pv_value_displ_32.setAlignment(Qt.AlignCenter)
        self.pv_value_displ_32.setReadOnly(True)
        self.pv_value_displ_32.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pv_value_displ_32.setDecimals(1)
        self.pv_value_displ_32.setMaximum(999.000000000000000)
        self.pv_value_displ_32.setValue(0.000000000000000)

        self.horizontalLayout_408.addWidget(self.pv_value_displ_32)

        self.label_268 = QLabel(self.widget_126)
        self.label_268.setObjectName(u"label_268")
        self.label_268.setFont(font)
        self.label_268.setStyleSheet(u"border: none;\n"
"")
        self.label_268.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_408.addWidget(self.label_268)

        self.low_temp_input_32 = QDoubleSpinBox(self.widget_126)
        self.low_temp_input_32.setObjectName(u"low_temp_input_32")
        sizePolicy.setHeightForWidth(self.low_temp_input_32.sizePolicy().hasHeightForWidth())
        self.low_temp_input_32.setSizePolicy(sizePolicy)
        self.low_temp_input_32.setFont(font4)
        self.low_temp_input_32.setStyleSheet(u"")
        self.low_temp_input_32.setAlignment(Qt.AlignCenter)
        self.low_temp_input_32.setReadOnly(False)
        self.low_temp_input_32.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.low_temp_input_32.setDecimals(1)
        self.low_temp_input_32.setMaximum(999.000000000000000)
        self.low_temp_input_32.setValue(0.000000000000000)

        self.horizontalLayout_408.addWidget(self.low_temp_input_32)


        self.horizontalLayout_404.addWidget(self.widget_126)

        self.sv_value_input_32 = QDoubleSpinBox(self.widget_224)
        self.sv_value_input_32.setObjectName(u"sv_value_input_32")
        sizePolicy.setHeightForWidth(self.sv_value_input_32.sizePolicy().hasHeightForWidth())
        self.sv_value_input_32.setSizePolicy(sizePolicy)
        self.sv_value_input_32.setFont(font4)
        self.sv_value_input_32.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.sv_value_input_32.setAlignment(Qt.AlignCenter)
        self.sv_value_input_32.setReadOnly(False)
        self.sv_value_input_32.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_input_32.setDecimals(1)
        self.sv_value_input_32.setMinimum(-999.000000000000000)
        self.sv_value_input_32.setMaximum(999.000000000000000)

        self.horizontalLayout_404.addWidget(self.sv_value_input_32)

        self.offset_value_input_32 = QDoubleSpinBox(self.widget_224)
        self.offset_value_input_32.setObjectName(u"offset_value_input_32")
        sizePolicy.setHeightForWidth(self.offset_value_input_32.sizePolicy().hasHeightForWidth())
        self.offset_value_input_32.setSizePolicy(sizePolicy)
        self.offset_value_input_32.setFont(font4)
        self.offset_value_input_32.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.offset_value_input_32.setAlignment(Qt.AlignCenter)
        self.offset_value_input_32.setReadOnly(True)
        self.offset_value_input_32.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.offset_value_input_32.setDecimals(1)
        self.offset_value_input_32.setMinimum(-99.000000000000000)
        self.offset_value_input_32.setMaximum(99.000000000000000)

        self.horizontalLayout_404.addWidget(self.offset_value_input_32)

        self.stackedWidget_38 = QStackedWidget(self.widget_224)
        self.stackedWidget_38.setObjectName(u"stackedWidget_38")
        self.celsius_displ_32 = QWidget()
        self.celsius_displ_32.setObjectName(u"celsius_displ_32")
        self.horizontalLayout_409 = QHBoxLayout(self.celsius_displ_32)
        self.horizontalLayout_409.setObjectName(u"horizontalLayout_409")
        self.horizontalLayout_409.setContentsMargins(0, 0, 0, 0)
        self.label_269 = QLabel(self.celsius_displ_32)
        self.label_269.setObjectName(u"label_269")
        self.label_269.setFont(font4)
        self.label_269.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_269.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_409.addWidget(self.label_269)

        self.stackedWidget_38.addWidget(self.celsius_displ_32)
        self.fahrenheit_displ_32 = QWidget()
        self.fahrenheit_displ_32.setObjectName(u"fahrenheit_displ_32")
        self.horizontalLayout_410 = QHBoxLayout(self.fahrenheit_displ_32)
        self.horizontalLayout_410.setObjectName(u"horizontalLayout_410")
        self.horizontalLayout_410.setContentsMargins(0, 0, 0, 0)
        self.label_270 = QLabel(self.fahrenheit_displ_32)
        self.label_270.setObjectName(u"label_270")
        self.label_270.setFont(font4)
        self.label_270.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_270.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_410.addWidget(self.label_270)

        self.stackedWidget_38.addWidget(self.fahrenheit_displ_32)

        self.horizontalLayout_404.addWidget(self.stackedWidget_38)

        self.horizontalLayout_404.setStretch(0, 1)
        self.horizontalLayout_404.setStretch(1, 2)
        self.horizontalLayout_404.setStretch(2, 1)
        self.horizontalLayout_404.setStretch(3, 1)

        self.verticalLayout_73.addWidget(self.widget_224)


        self.horizontalLayout_377.addWidget(self.widget_97)

        self.horizontalLayout_377.setStretch(0, 1)
        self.horizontalLayout_377.setStretch(1, 4)

        self.verticalLayout_9.addWidget(self.widget_94)

        self.widget_98 = QWidget(self.widget_16)
        self.widget_98.setObjectName(u"widget_98")
        sizePolicy.setHeightForWidth(self.widget_98.sizePolicy().hasHeightForWidth())
        self.widget_98.setSizePolicy(sizePolicy)
        self.widget_98.setStyleSheet(u"QWidget {\n"
"    background-color: white;\n"
"    border-left: 4px solid #FB8C00;\n"
"    border-radius: 6px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(97, 97, 97)\n"
"}")
        self.horizontalLayout_340 = QHBoxLayout(self.widget_98)
        self.horizontalLayout_340.setSpacing(5)
        self.horizontalLayout_340.setObjectName(u"horizontalLayout_340")
        self.horizontalLayout_340.setContentsMargins(0, 5, 15, 5)
        self.widget_99 = QWidget(self.widget_98)
        self.widget_99.setObjectName(u"widget_99")
        self.horizontalLayout_341 = QHBoxLayout(self.widget_99)
        self.horizontalLayout_341.setObjectName(u"horizontalLayout_341")
        self.horizontalLayout_341.setContentsMargins(-1, 0, -1, 0)
        self.label_170 = QLabel(self.widget_99)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setFont(font5)
        self.label_170.setStyleSheet(u"border: none;\n"
"padding: 20px;\n"
"border-left: none;")

        self.horizontalLayout_341.addWidget(self.label_170)

        self.line_11 = QFrame(self.widget_99)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_341.addWidget(self.line_11)

        self.widget_100 = QWidget(self.widget_99)
        self.widget_100.setObjectName(u"widget_100")
        self.widget_100.setStyleSheet(u"border-left: none;")
        self.verticalLayout_64 = QVBoxLayout(self.widget_100)
        self.verticalLayout_64.setSpacing(10)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.widget_111 = QWidget(self.widget_100)
        self.widget_111.setObjectName(u"widget_111")
        self.widget_111.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_343 = QHBoxLayout(self.widget_111)
        self.horizontalLayout_343.setObjectName(u"horizontalLayout_343")
        self.horizontalLayout_343.setContentsMargins(0, 0, 5, 0)
        self.label_172 = QLabel(self.widget_111)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setFont(font1)

        self.horizontalLayout_343.addWidget(self.label_172)


        self.verticalLayout_64.addWidget(self.widget_111)

        self.widget_112 = QWidget(self.widget_100)
        self.widget_112.setObjectName(u"widget_112")
        self.widget_112.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_344 = QHBoxLayout(self.widget_112)
        self.horizontalLayout_344.setObjectName(u"horizontalLayout_344")
        self.horizontalLayout_344.setContentsMargins(0, 0, 5, 0)
        self.label_173 = QLabel(self.widget_112)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setFont(font1)

        self.horizontalLayout_344.addWidget(self.label_173)


        self.verticalLayout_64.addWidget(self.widget_112)

        self.widget_113 = QWidget(self.widget_100)
        self.widget_113.setObjectName(u"widget_113")
        self.widget_113.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_345 = QHBoxLayout(self.widget_113)
        self.horizontalLayout_345.setObjectName(u"horizontalLayout_345")
        self.horizontalLayout_345.setContentsMargins(0, 0, 5, 0)
        self.label_174 = QLabel(self.widget_113)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setFont(font1)

        self.horizontalLayout_345.addWidget(self.label_174)


        self.verticalLayout_64.addWidget(self.widget_113)


        self.horizontalLayout_341.addWidget(self.widget_100)

        self.line_18 = QFrame(self.widget_99)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.Shape.VLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_341.addWidget(self.line_18)


        self.horizontalLayout_340.addWidget(self.widget_99)

        self.widget_101 = QWidget(self.widget_98)
        self.widget_101.setObjectName(u"widget_101")
        self.widget_101.setStyleSheet(u"QWidget{\n"
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
        self.verticalLayout_74 = QVBoxLayout(self.widget_101)
        self.verticalLayout_74.setSpacing(10)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.widget_209 = QWidget(self.widget_101)
        self.widget_209.setObjectName(u"widget_209")
        self.widget_209.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_353 = QHBoxLayout(self.widget_209)
        self.horizontalLayout_353.setSpacing(10)
        self.horizontalLayout_353.setObjectName(u"horizontalLayout_353")
        self.horizontalLayout_353.setContentsMargins(0, 0, 0, 0)
        self.sys_state_stacked_wid_35 = QStackedWidget(self.widget_209)
        self.sys_state_stacked_wid_35.setObjectName(u"sys_state_stacked_wid_35")
        sizePolicy1.setHeightForWidth(self.sys_state_stacked_wid_35.sizePolicy().hasHeightForWidth())
        self.sys_state_stacked_wid_35.setSizePolicy(sizePolicy1)
        self.sys_state_stacked_wid_35.setStyleSheet(u"QLabel{\n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"padding-right: 3px;\n"
"}")
        self.running_light_48 = QWidget()
        self.running_light_48.setObjectName(u"running_light_48")
        self.horizontalLayout_418 = QHBoxLayout(self.running_light_48)
        self.horizontalLayout_418.setObjectName(u"horizontalLayout_418")
        self.horizontalLayout_418.setContentsMargins(0, 0, 0, 0)
        self.pushButton_27 = QPushButton(self.running_light_48)
        self.pushButton_27.setObjectName(u"pushButton_27")
        sizePolicy1.setHeightForWidth(self.pushButton_27.sizePolicy().hasHeightForWidth())
        self.pushButton_27.setSizePolicy(sizePolicy1)
        self.pushButton_27.setFont(font6)
        self.pushButton_27.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #10B981; \n"
"padding-right: 3px;")
        self.pushButton_27.setIcon(icon)
        self.pushButton_27.setIconSize(QSize(30, 30))

        self.horizontalLayout_418.addWidget(self.pushButton_27)

        self.sys_state_stacked_wid_35.addWidget(self.running_light_48)
        self.wating_light_48 = QWidget()
        self.wating_light_48.setObjectName(u"wating_light_48")
        self.horizontalLayout_419 = QHBoxLayout(self.wating_light_48)
        self.horizontalLayout_419.setObjectName(u"horizontalLayout_419")
        self.horizontalLayout_419.setContentsMargins(0, 0, 0, 0)
        self.pushButton_28 = QPushButton(self.wating_light_48)
        self.pushButton_28.setObjectName(u"pushButton_28")
        sizePolicy1.setHeightForWidth(self.pushButton_28.sizePolicy().hasHeightForWidth())
        self.pushButton_28.setSizePolicy(sizePolicy1)
        self.pushButton_28.setFont(font6)
        self.pushButton_28.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #FB8C00; \n"
"padding-right: 3px;")
        self.pushButton_28.setIcon(icon1)
        self.pushButton_28.setIconSize(QSize(30, 30))

        self.horizontalLayout_419.addWidget(self.pushButton_28)

        self.sys_state_stacked_wid_35.addWidget(self.wating_light_48)
        self.error_light_48 = QWidget()
        self.error_light_48.setObjectName(u"error_light_48")
        self.horizontalLayout_420 = QHBoxLayout(self.error_light_48)
        self.horizontalLayout_420.setObjectName(u"horizontalLayout_420")
        self.horizontalLayout_420.setContentsMargins(0, 0, 0, 0)
        self.pushButton_29 = QPushButton(self.error_light_48)
        self.pushButton_29.setObjectName(u"pushButton_29")
        sizePolicy1.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy1)
        self.pushButton_29.setFont(font6)
        self.pushButton_29.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #F90A0A; \n"
"padding-right: 3px;")
        self.pushButton_29.setIcon(icon2)
        self.pushButton_29.setIconSize(QSize(30, 30))

        self.horizontalLayout_420.addWidget(self.pushButton_29)

        self.sys_state_stacked_wid_35.addWidget(self.error_light_48)

        self.horizontalLayout_353.addWidget(self.sys_state_stacked_wid_35)

        self.widget_115 = QWidget(self.widget_209)
        self.widget_115.setObjectName(u"widget_115")
        self.widget_115.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout_357 = QHBoxLayout(self.widget_115)
        self.horizontalLayout_357.setSpacing(0)
        self.horizontalLayout_357.setObjectName(u"horizontalLayout_357")
        self.horizontalLayout_357.setContentsMargins(2, 2, 2, 2)
        self.high_temp_input_26 = QDoubleSpinBox(self.widget_115)
        self.high_temp_input_26.setObjectName(u"high_temp_input_26")
        sizePolicy.setHeightForWidth(self.high_temp_input_26.sizePolicy().hasHeightForWidth())
        self.high_temp_input_26.setSizePolicy(sizePolicy)
        self.high_temp_input_26.setFont(font4)
        self.high_temp_input_26.setStyleSheet(u"")
        self.high_temp_input_26.setAlignment(Qt.AlignCenter)
        self.high_temp_input_26.setReadOnly(False)
        self.high_temp_input_26.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.high_temp_input_26.setDecimals(1)
        self.high_temp_input_26.setMaximum(999.000000000000000)
        self.high_temp_input_26.setValue(0.000000000000000)

        self.horizontalLayout_357.addWidget(self.high_temp_input_26)

        self.label_177 = QLabel(self.widget_115)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setFont(font)
        self.label_177.setStyleSheet(u"border: none;\n"
"")
        self.label_177.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_357.addWidget(self.label_177)

        self.pv_value_displ_26 = QDoubleSpinBox(self.widget_115)
        self.pv_value_displ_26.setObjectName(u"pv_value_displ_26")
        sizePolicy.setHeightForWidth(self.pv_value_displ_26.sizePolicy().hasHeightForWidth())
        self.pv_value_displ_26.setSizePolicy(sizePolicy)
        self.pv_value_displ_26.setFont(font4)
        self.pv_value_displ_26.setStyleSheet(u"")
        self.pv_value_displ_26.setAlignment(Qt.AlignCenter)
        self.pv_value_displ_26.setReadOnly(True)
        self.pv_value_displ_26.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pv_value_displ_26.setDecimals(1)
        self.pv_value_displ_26.setMaximum(999.000000000000000)
        self.pv_value_displ_26.setValue(0.000000000000000)

        self.horizontalLayout_357.addWidget(self.pv_value_displ_26)

        self.label_178 = QLabel(self.widget_115)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setFont(font)
        self.label_178.setStyleSheet(u"border: none;\n"
"")
        self.label_178.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_357.addWidget(self.label_178)

        self.low_temp_input_26 = QDoubleSpinBox(self.widget_115)
        self.low_temp_input_26.setObjectName(u"low_temp_input_26")
        sizePolicy.setHeightForWidth(self.low_temp_input_26.sizePolicy().hasHeightForWidth())
        self.low_temp_input_26.setSizePolicy(sizePolicy)
        self.low_temp_input_26.setFont(font4)
        self.low_temp_input_26.setStyleSheet(u"")
        self.low_temp_input_26.setAlignment(Qt.AlignCenter)
        self.low_temp_input_26.setReadOnly(False)
        self.low_temp_input_26.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.low_temp_input_26.setDecimals(1)
        self.low_temp_input_26.setMaximum(999.000000000000000)
        self.low_temp_input_26.setValue(0.000000000000000)

        self.horizontalLayout_357.addWidget(self.low_temp_input_26)


        self.horizontalLayout_353.addWidget(self.widget_115)

        self.sv_value_input_26 = QDoubleSpinBox(self.widget_209)
        self.sv_value_input_26.setObjectName(u"sv_value_input_26")
        sizePolicy.setHeightForWidth(self.sv_value_input_26.sizePolicy().hasHeightForWidth())
        self.sv_value_input_26.setSizePolicy(sizePolicy)
        self.sv_value_input_26.setFont(font4)
        self.sv_value_input_26.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.sv_value_input_26.setAlignment(Qt.AlignCenter)
        self.sv_value_input_26.setReadOnly(False)
        self.sv_value_input_26.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_input_26.setDecimals(1)
        self.sv_value_input_26.setMinimum(-999.000000000000000)
        self.sv_value_input_26.setMaximum(999.000000000000000)

        self.horizontalLayout_353.addWidget(self.sv_value_input_26)

        self.offset_value_input_26 = QDoubleSpinBox(self.widget_209)
        self.offset_value_input_26.setObjectName(u"offset_value_input_26")
        sizePolicy.setHeightForWidth(self.offset_value_input_26.sizePolicy().hasHeightForWidth())
        self.offset_value_input_26.setSizePolicy(sizePolicy)
        self.offset_value_input_26.setFont(font4)
        self.offset_value_input_26.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.offset_value_input_26.setAlignment(Qt.AlignCenter)
        self.offset_value_input_26.setReadOnly(False)
        self.offset_value_input_26.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.offset_value_input_26.setDecimals(1)
        self.offset_value_input_26.setMinimum(-99.000000000000000)
        self.offset_value_input_26.setMaximum(99.000000000000000)

        self.horizontalLayout_353.addWidget(self.offset_value_input_26)

        self.stackedWidget_32 = QStackedWidget(self.widget_209)
        self.stackedWidget_32.setObjectName(u"stackedWidget_32")
        self.celsius_displ_26 = QWidget()
        self.celsius_displ_26.setObjectName(u"celsius_displ_26")
        self.horizontalLayout_358 = QHBoxLayout(self.celsius_displ_26)
        self.horizontalLayout_358.setObjectName(u"horizontalLayout_358")
        self.horizontalLayout_358.setContentsMargins(0, 0, 0, 0)
        self.label_255 = QLabel(self.celsius_displ_26)
        self.label_255.setObjectName(u"label_255")
        self.label_255.setFont(font4)
        self.label_255.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_255.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_358.addWidget(self.label_255)

        self.stackedWidget_32.addWidget(self.celsius_displ_26)
        self.fahrenheit_displ_26 = QWidget()
        self.fahrenheit_displ_26.setObjectName(u"fahrenheit_displ_26")
        self.horizontalLayout_360 = QHBoxLayout(self.fahrenheit_displ_26)
        self.horizontalLayout_360.setObjectName(u"horizontalLayout_360")
        self.horizontalLayout_360.setContentsMargins(0, 0, 0, 0)
        self.label_256 = QLabel(self.fahrenheit_displ_26)
        self.label_256.setObjectName(u"label_256")
        self.label_256.setFont(font4)
        self.label_256.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_256.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_360.addWidget(self.label_256)

        self.stackedWidget_32.addWidget(self.fahrenheit_displ_26)

        self.horizontalLayout_353.addWidget(self.stackedWidget_32)

        self.horizontalLayout_353.setStretch(0, 1)
        self.horizontalLayout_353.setStretch(1, 2)
        self.horizontalLayout_353.setStretch(2, 1)
        self.horizontalLayout_353.setStretch(3, 1)

        self.verticalLayout_74.addWidget(self.widget_209)

        self.widget_210 = QWidget(self.widget_101)
        self.widget_210.setObjectName(u"widget_210")
        self.widget_210.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_361 = QHBoxLayout(self.widget_210)
        self.horizontalLayout_361.setSpacing(10)
        self.horizontalLayout_361.setObjectName(u"horizontalLayout_361")
        self.horizontalLayout_361.setContentsMargins(0, 0, 0, 0)
        self.sys_state_stacked_wid_36 = QStackedWidget(self.widget_210)
        self.sys_state_stacked_wid_36.setObjectName(u"sys_state_stacked_wid_36")
        sizePolicy1.setHeightForWidth(self.sys_state_stacked_wid_36.sizePolicy().hasHeightForWidth())
        self.sys_state_stacked_wid_36.setSizePolicy(sizePolicy1)
        self.sys_state_stacked_wid_36.setStyleSheet(u"QLabel{\n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"padding-right: 3px;\n"
"}")
        self.running_light_49 = QWidget()
        self.running_light_49.setObjectName(u"running_light_49")
        self.horizontalLayout_421 = QHBoxLayout(self.running_light_49)
        self.horizontalLayout_421.setObjectName(u"horizontalLayout_421")
        self.horizontalLayout_421.setContentsMargins(0, 0, 0, 0)
        self.pushButton_30 = QPushButton(self.running_light_49)
        self.pushButton_30.setObjectName(u"pushButton_30")
        sizePolicy1.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy1)
        self.pushButton_30.setFont(font6)
        self.pushButton_30.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #10B981; \n"
"padding-right: 3px;")
        self.pushButton_30.setIcon(icon)
        self.pushButton_30.setIconSize(QSize(30, 30))

        self.horizontalLayout_421.addWidget(self.pushButton_30)

        self.sys_state_stacked_wid_36.addWidget(self.running_light_49)
        self.wating_light_49 = QWidget()
        self.wating_light_49.setObjectName(u"wating_light_49")
        self.horizontalLayout_422 = QHBoxLayout(self.wating_light_49)
        self.horizontalLayout_422.setObjectName(u"horizontalLayout_422")
        self.horizontalLayout_422.setContentsMargins(0, 0, 0, 0)
        self.pushButton_31 = QPushButton(self.wating_light_49)
        self.pushButton_31.setObjectName(u"pushButton_31")
        sizePolicy1.setHeightForWidth(self.pushButton_31.sizePolicy().hasHeightForWidth())
        self.pushButton_31.setSizePolicy(sizePolicy1)
        self.pushButton_31.setFont(font6)
        self.pushButton_31.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #FB8C00; \n"
"padding-right: 3px;")
        self.pushButton_31.setIcon(icon1)
        self.pushButton_31.setIconSize(QSize(30, 30))

        self.horizontalLayout_422.addWidget(self.pushButton_31)

        self.sys_state_stacked_wid_36.addWidget(self.wating_light_49)
        self.error_light_49 = QWidget()
        self.error_light_49.setObjectName(u"error_light_49")
        self.horizontalLayout_423 = QHBoxLayout(self.error_light_49)
        self.horizontalLayout_423.setObjectName(u"horizontalLayout_423")
        self.horizontalLayout_423.setContentsMargins(0, 0, 0, 0)
        self.pushButton_32 = QPushButton(self.error_light_49)
        self.pushButton_32.setObjectName(u"pushButton_32")
        sizePolicy1.setHeightForWidth(self.pushButton_32.sizePolicy().hasHeightForWidth())
        self.pushButton_32.setSizePolicy(sizePolicy1)
        self.pushButton_32.setFont(font6)
        self.pushButton_32.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #F90A0A; \n"
"padding-right: 3px;")
        self.pushButton_32.setIcon(icon2)
        self.pushButton_32.setIconSize(QSize(30, 30))

        self.horizontalLayout_423.addWidget(self.pushButton_32)

        self.sys_state_stacked_wid_36.addWidget(self.error_light_49)

        self.horizontalLayout_361.addWidget(self.sys_state_stacked_wid_36)

        self.widget_131 = QWidget(self.widget_210)
        self.widget_131.setObjectName(u"widget_131")
        self.widget_131.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout_367 = QHBoxLayout(self.widget_131)
        self.horizontalLayout_367.setSpacing(0)
        self.horizontalLayout_367.setObjectName(u"horizontalLayout_367")
        self.horizontalLayout_367.setContentsMargins(2, 2, 2, 2)
        self.high_temp_input_27 = QDoubleSpinBox(self.widget_131)
        self.high_temp_input_27.setObjectName(u"high_temp_input_27")
        sizePolicy.setHeightForWidth(self.high_temp_input_27.sizePolicy().hasHeightForWidth())
        self.high_temp_input_27.setSizePolicy(sizePolicy)
        self.high_temp_input_27.setFont(font4)
        self.high_temp_input_27.setStyleSheet(u"")
        self.high_temp_input_27.setAlignment(Qt.AlignCenter)
        self.high_temp_input_27.setReadOnly(False)
        self.high_temp_input_27.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.high_temp_input_27.setDecimals(1)
        self.high_temp_input_27.setMaximum(999.000000000000000)
        self.high_temp_input_27.setValue(0.000000000000000)

        self.horizontalLayout_367.addWidget(self.high_temp_input_27)

        self.label_179 = QLabel(self.widget_131)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setFont(font)
        self.label_179.setStyleSheet(u"border: none;\n"
"")
        self.label_179.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_367.addWidget(self.label_179)

        self.pv_value_displ_27 = QDoubleSpinBox(self.widget_131)
        self.pv_value_displ_27.setObjectName(u"pv_value_displ_27")
        sizePolicy.setHeightForWidth(self.pv_value_displ_27.sizePolicy().hasHeightForWidth())
        self.pv_value_displ_27.setSizePolicy(sizePolicy)
        self.pv_value_displ_27.setFont(font4)
        self.pv_value_displ_27.setStyleSheet(u"")
        self.pv_value_displ_27.setAlignment(Qt.AlignCenter)
        self.pv_value_displ_27.setReadOnly(True)
        self.pv_value_displ_27.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pv_value_displ_27.setDecimals(1)
        self.pv_value_displ_27.setMaximum(999.000000000000000)
        self.pv_value_displ_27.setValue(0.000000000000000)

        self.horizontalLayout_367.addWidget(self.pv_value_displ_27)

        self.label_229 = QLabel(self.widget_131)
        self.label_229.setObjectName(u"label_229")
        self.label_229.setFont(font)
        self.label_229.setStyleSheet(u"border: none;\n"
"")
        self.label_229.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_367.addWidget(self.label_229)

        self.low_temp_input_27 = QDoubleSpinBox(self.widget_131)
        self.low_temp_input_27.setObjectName(u"low_temp_input_27")
        sizePolicy.setHeightForWidth(self.low_temp_input_27.sizePolicy().hasHeightForWidth())
        self.low_temp_input_27.setSizePolicy(sizePolicy)
        self.low_temp_input_27.setFont(font4)
        self.low_temp_input_27.setStyleSheet(u"")
        self.low_temp_input_27.setAlignment(Qt.AlignCenter)
        self.low_temp_input_27.setReadOnly(False)
        self.low_temp_input_27.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.low_temp_input_27.setDecimals(1)
        self.low_temp_input_27.setMaximum(999.000000000000000)
        self.low_temp_input_27.setValue(0.000000000000000)

        self.horizontalLayout_367.addWidget(self.low_temp_input_27)


        self.horizontalLayout_361.addWidget(self.widget_131)

        self.sv_value_input_27 = QDoubleSpinBox(self.widget_210)
        self.sv_value_input_27.setObjectName(u"sv_value_input_27")
        sizePolicy.setHeightForWidth(self.sv_value_input_27.sizePolicy().hasHeightForWidth())
        self.sv_value_input_27.setSizePolicy(sizePolicy)
        self.sv_value_input_27.setFont(font4)
        self.sv_value_input_27.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.sv_value_input_27.setAlignment(Qt.AlignCenter)
        self.sv_value_input_27.setReadOnly(False)
        self.sv_value_input_27.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_input_27.setDecimals(1)
        self.sv_value_input_27.setMinimum(-999.000000000000000)
        self.sv_value_input_27.setMaximum(999.000000000000000)

        self.horizontalLayout_361.addWidget(self.sv_value_input_27)

        self.offset_value_input_27 = QDoubleSpinBox(self.widget_210)
        self.offset_value_input_27.setObjectName(u"offset_value_input_27")
        sizePolicy.setHeightForWidth(self.offset_value_input_27.sizePolicy().hasHeightForWidth())
        self.offset_value_input_27.setSizePolicy(sizePolicy)
        self.offset_value_input_27.setFont(font4)
        self.offset_value_input_27.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.offset_value_input_27.setAlignment(Qt.AlignCenter)
        self.offset_value_input_27.setReadOnly(False)
        self.offset_value_input_27.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.offset_value_input_27.setDecimals(1)
        self.offset_value_input_27.setMinimum(-99.000000000000000)
        self.offset_value_input_27.setMaximum(99.000000000000000)

        self.horizontalLayout_361.addWidget(self.offset_value_input_27)

        self.stackedWidget_33 = QStackedWidget(self.widget_210)
        self.stackedWidget_33.setObjectName(u"stackedWidget_33")
        self.celsius_displ_27 = QWidget()
        self.celsius_displ_27.setObjectName(u"celsius_displ_27")
        self.horizontalLayout_368 = QHBoxLayout(self.celsius_displ_27)
        self.horizontalLayout_368.setObjectName(u"horizontalLayout_368")
        self.horizontalLayout_368.setContentsMargins(0, 0, 0, 0)
        self.label_257 = QLabel(self.celsius_displ_27)
        self.label_257.setObjectName(u"label_257")
        self.label_257.setFont(font4)
        self.label_257.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_257.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_368.addWidget(self.label_257)

        self.stackedWidget_33.addWidget(self.celsius_displ_27)
        self.fahrenheit_displ_27 = QWidget()
        self.fahrenheit_displ_27.setObjectName(u"fahrenheit_displ_27")
        self.horizontalLayout_369 = QHBoxLayout(self.fahrenheit_displ_27)
        self.horizontalLayout_369.setObjectName(u"horizontalLayout_369")
        self.horizontalLayout_369.setContentsMargins(0, 0, 0, 0)
        self.label_258 = QLabel(self.fahrenheit_displ_27)
        self.label_258.setObjectName(u"label_258")
        self.label_258.setFont(font4)
        self.label_258.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_258.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_369.addWidget(self.label_258)

        self.stackedWidget_33.addWidget(self.fahrenheit_displ_27)

        self.horizontalLayout_361.addWidget(self.stackedWidget_33)

        self.horizontalLayout_361.setStretch(0, 1)
        self.horizontalLayout_361.setStretch(1, 2)
        self.horizontalLayout_361.setStretch(2, 1)
        self.horizontalLayout_361.setStretch(3, 1)

        self.verticalLayout_74.addWidget(self.widget_210)

        self.widget_211 = QWidget(self.widget_101)
        self.widget_211.setObjectName(u"widget_211")
        self.widget_211.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_370 = QHBoxLayout(self.widget_211)
        self.horizontalLayout_370.setSpacing(10)
        self.horizontalLayout_370.setObjectName(u"horizontalLayout_370")
        self.horizontalLayout_370.setContentsMargins(0, 0, 0, 0)
        self.sys_state_stacked_wid_37 = QStackedWidget(self.widget_211)
        self.sys_state_stacked_wid_37.setObjectName(u"sys_state_stacked_wid_37")
        sizePolicy1.setHeightForWidth(self.sys_state_stacked_wid_37.sizePolicy().hasHeightForWidth())
        self.sys_state_stacked_wid_37.setSizePolicy(sizePolicy1)
        self.sys_state_stacked_wid_37.setStyleSheet(u"QLabel{\n"
"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"padding-right: 3px;\n"
"}")
        self.running_light_50 = QWidget()
        self.running_light_50.setObjectName(u"running_light_50")
        self.horizontalLayout_425 = QHBoxLayout(self.running_light_50)
        self.horizontalLayout_425.setObjectName(u"horizontalLayout_425")
        self.horizontalLayout_425.setContentsMargins(0, 0, 0, 0)
        self.pushButton_33 = QPushButton(self.running_light_50)
        self.pushButton_33.setObjectName(u"pushButton_33")
        sizePolicy1.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy1)
        self.pushButton_33.setFont(font6)
        self.pushButton_33.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #10B981; \n"
"padding-right: 3px;")
        self.pushButton_33.setIcon(icon)
        self.pushButton_33.setIconSize(QSize(30, 30))

        self.horizontalLayout_425.addWidget(self.pushButton_33)

        self.sys_state_stacked_wid_37.addWidget(self.running_light_50)
        self.wating_light_50 = QWidget()
        self.wating_light_50.setObjectName(u"wating_light_50")
        self.horizontalLayout_426 = QHBoxLayout(self.wating_light_50)
        self.horizontalLayout_426.setObjectName(u"horizontalLayout_426")
        self.horizontalLayout_426.setContentsMargins(0, 0, 0, 0)
        self.pushButton_34 = QPushButton(self.wating_light_50)
        self.pushButton_34.setObjectName(u"pushButton_34")
        sizePolicy1.setHeightForWidth(self.pushButton_34.sizePolicy().hasHeightForWidth())
        self.pushButton_34.setSizePolicy(sizePolicy1)
        self.pushButton_34.setFont(font6)
        self.pushButton_34.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #FB8C00; \n"
"padding-right: 3px;")
        self.pushButton_34.setIcon(icon1)
        self.pushButton_34.setIconSize(QSize(30, 30))

        self.horizontalLayout_426.addWidget(self.pushButton_34)

        self.sys_state_stacked_wid_37.addWidget(self.wating_light_50)
        self.error_light_50 = QWidget()
        self.error_light_50.setObjectName(u"error_light_50")
        self.horizontalLayout_427 = QHBoxLayout(self.error_light_50)
        self.horizontalLayout_427.setObjectName(u"horizontalLayout_427")
        self.horizontalLayout_427.setContentsMargins(0, 0, 0, 0)
        self.pushButton_35 = QPushButton(self.error_light_50)
        self.pushButton_35.setObjectName(u"pushButton_35")
        sizePolicy1.setHeightForWidth(self.pushButton_35.sizePolicy().hasHeightForWidth())
        self.pushButton_35.setSizePolicy(sizePolicy1)
        self.pushButton_35.setFont(font6)
        self.pushButton_35.setStyleSheet(u"border: 2px solid #E5E5E5; \n"
"border-radius: 10px;\n"
"color: #F90A0A; \n"
"padding-right: 3px;")
        self.pushButton_35.setIcon(icon2)
        self.pushButton_35.setIconSize(QSize(30, 30))

        self.horizontalLayout_427.addWidget(self.pushButton_35)

        self.sys_state_stacked_wid_37.addWidget(self.error_light_50)

        self.horizontalLayout_370.addWidget(self.sys_state_stacked_wid_37)

        self.widget_132 = QWidget(self.widget_211)
        self.widget_132.setObjectName(u"widget_132")
        self.widget_132.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout_374 = QHBoxLayout(self.widget_132)
        self.horizontalLayout_374.setSpacing(0)
        self.horizontalLayout_374.setObjectName(u"horizontalLayout_374")
        self.horizontalLayout_374.setContentsMargins(2, 2, 2, 2)
        self.high_temp_input_28 = QDoubleSpinBox(self.widget_132)
        self.high_temp_input_28.setObjectName(u"high_temp_input_28")
        sizePolicy.setHeightForWidth(self.high_temp_input_28.sizePolicy().hasHeightForWidth())
        self.high_temp_input_28.setSizePolicy(sizePolicy)
        self.high_temp_input_28.setFont(font4)
        self.high_temp_input_28.setStyleSheet(u"")
        self.high_temp_input_28.setAlignment(Qt.AlignCenter)
        self.high_temp_input_28.setReadOnly(False)
        self.high_temp_input_28.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.high_temp_input_28.setDecimals(1)
        self.high_temp_input_28.setMaximum(999.000000000000000)
        self.high_temp_input_28.setValue(0.000000000000000)

        self.horizontalLayout_374.addWidget(self.high_temp_input_28)

        self.label_230 = QLabel(self.widget_132)
        self.label_230.setObjectName(u"label_230")
        self.label_230.setFont(font)
        self.label_230.setStyleSheet(u"border: none;\n"
"")
        self.label_230.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_374.addWidget(self.label_230)

        self.pv_value_displ_28 = QDoubleSpinBox(self.widget_132)
        self.pv_value_displ_28.setObjectName(u"pv_value_displ_28")
        sizePolicy.setHeightForWidth(self.pv_value_displ_28.sizePolicy().hasHeightForWidth())
        self.pv_value_displ_28.setSizePolicy(sizePolicy)
        self.pv_value_displ_28.setFont(font4)
        self.pv_value_displ_28.setStyleSheet(u"")
        self.pv_value_displ_28.setAlignment(Qt.AlignCenter)
        self.pv_value_displ_28.setReadOnly(True)
        self.pv_value_displ_28.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pv_value_displ_28.setDecimals(1)
        self.pv_value_displ_28.setMaximum(999.000000000000000)
        self.pv_value_displ_28.setValue(0.000000000000000)

        self.horizontalLayout_374.addWidget(self.pv_value_displ_28)

        self.label_231 = QLabel(self.widget_132)
        self.label_231.setObjectName(u"label_231")
        self.label_231.setFont(font)
        self.label_231.setStyleSheet(u"border: none;\n"
"")
        self.label_231.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_374.addWidget(self.label_231)

        self.low_temp_input_28 = QDoubleSpinBox(self.widget_132)
        self.low_temp_input_28.setObjectName(u"low_temp_input_28")
        sizePolicy.setHeightForWidth(self.low_temp_input_28.sizePolicy().hasHeightForWidth())
        self.low_temp_input_28.setSizePolicy(sizePolicy)
        self.low_temp_input_28.setFont(font4)
        self.low_temp_input_28.setStyleSheet(u"")
        self.low_temp_input_28.setAlignment(Qt.AlignCenter)
        self.low_temp_input_28.setReadOnly(False)
        self.low_temp_input_28.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.low_temp_input_28.setDecimals(1)
        self.low_temp_input_28.setMaximum(999.000000000000000)
        self.low_temp_input_28.setValue(0.000000000000000)

        self.horizontalLayout_374.addWidget(self.low_temp_input_28)


        self.horizontalLayout_370.addWidget(self.widget_132)

        self.sv_value_input_28 = QDoubleSpinBox(self.widget_211)
        self.sv_value_input_28.setObjectName(u"sv_value_input_28")
        sizePolicy.setHeightForWidth(self.sv_value_input_28.sizePolicy().hasHeightForWidth())
        self.sv_value_input_28.setSizePolicy(sizePolicy)
        self.sv_value_input_28.setFont(font4)
        self.sv_value_input_28.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.sv_value_input_28.setAlignment(Qt.AlignCenter)
        self.sv_value_input_28.setReadOnly(False)
        self.sv_value_input_28.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sv_value_input_28.setDecimals(1)
        self.sv_value_input_28.setMinimum(-999.000000000000000)
        self.sv_value_input_28.setMaximum(999.000000000000000)

        self.horizontalLayout_370.addWidget(self.sv_value_input_28)

        self.offset_value_input_28 = QDoubleSpinBox(self.widget_211)
        self.offset_value_input_28.setObjectName(u"offset_value_input_28")
        sizePolicy.setHeightForWidth(self.offset_value_input_28.sizePolicy().hasHeightForWidth())
        self.offset_value_input_28.setSizePolicy(sizePolicy)
        self.offset_value_input_28.setFont(font4)
        self.offset_value_input_28.setStyleSheet(u"QSpinBox:hover {\n"
"    background-color: rgb(222, 0, 0)\n"
"}")
        self.offset_value_input_28.setAlignment(Qt.AlignCenter)
        self.offset_value_input_28.setReadOnly(True)
        self.offset_value_input_28.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.offset_value_input_28.setDecimals(1)
        self.offset_value_input_28.setMinimum(-99.000000000000000)
        self.offset_value_input_28.setMaximum(99.000000000000000)

        self.horizontalLayout_370.addWidget(self.offset_value_input_28)

        self.stackedWidget_34 = QStackedWidget(self.widget_211)
        self.stackedWidget_34.setObjectName(u"stackedWidget_34")
        self.celsius_displ_28 = QWidget()
        self.celsius_displ_28.setObjectName(u"celsius_displ_28")
        self.horizontalLayout_375 = QHBoxLayout(self.celsius_displ_28)
        self.horizontalLayout_375.setObjectName(u"horizontalLayout_375")
        self.horizontalLayout_375.setContentsMargins(0, 0, 0, 0)
        self.label_259 = QLabel(self.celsius_displ_28)
        self.label_259.setObjectName(u"label_259")
        self.label_259.setFont(font4)
        self.label_259.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_259.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_375.addWidget(self.label_259)

        self.stackedWidget_34.addWidget(self.celsius_displ_28)
        self.fahrenheit_displ_28 = QWidget()
        self.fahrenheit_displ_28.setObjectName(u"fahrenheit_displ_28")
        self.horizontalLayout_376 = QHBoxLayout(self.fahrenheit_displ_28)
        self.horizontalLayout_376.setObjectName(u"horizontalLayout_376")
        self.horizontalLayout_376.setContentsMargins(0, 0, 0, 0)
        self.label_260 = QLabel(self.fahrenheit_displ_28)
        self.label_260.setObjectName(u"label_260")
        self.label_260.setFont(font4)
        self.label_260.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_260.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_376.addWidget(self.label_260)

        self.stackedWidget_34.addWidget(self.fahrenheit_displ_28)

        self.horizontalLayout_370.addWidget(self.stackedWidget_34)

        self.horizontalLayout_370.setStretch(0, 1)
        self.horizontalLayout_370.setStretch(1, 2)
        self.horizontalLayout_370.setStretch(2, 1)
        self.horizontalLayout_370.setStretch(3, 1)

        self.verticalLayout_74.addWidget(self.widget_211)


        self.horizontalLayout_340.addWidget(self.widget_101)

        self.horizontalLayout_340.setStretch(0, 1)
        self.horizontalLayout_340.setStretch(1, 4)

        self.verticalLayout_9.addWidget(self.widget_98)

        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 3)
        self.verticalLayout_9.setStretch(2, 3)
        self.verticalLayout_9.setStretch(3, 3)

        self.retranslateUi(Form)

        self.sys_state_stacked_wid_28.setCurrentIndex(1)
        self.stackedWidget_27.setCurrentIndex(0)
        self.sys_state_stacked_wid_29.setCurrentIndex(1)
        self.stackedWidget_40.setCurrentIndex(0)
        self.sys_state_stacked_wid_30.setCurrentIndex(1)
        self.stackedWidget_41.setCurrentIndex(0)
        self.sys_state_stacked_wid_31.setCurrentIndex(1)
        self.stackedWidget_42.setCurrentIndex(0)
        self.sys_state_stacked_wid_32.setCurrentIndex(1)
        self.stackedWidget_36.setCurrentIndex(0)
        self.sys_state_stacked_wid_33.setCurrentIndex(1)
        self.stackedWidget_37.setCurrentIndex(0)
        self.sys_state_stacked_wid_34.setCurrentIndex(1)
        self.stackedWidget_38.setCurrentIndex(0)
        self.sys_state_stacked_wid_35.setCurrentIndex(1)
        self.stackedWidget_32.setCurrentIndex(0)
        self.sys_state_stacked_wid_36.setCurrentIndex(1)
        self.stackedWidget_33.setCurrentIndex(0)
        self.sys_state_stacked_wid_37.setCurrentIndex(1)
        self.stackedWidget_34.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_113.setText(QCoreApplication.translate("Form", u"Filling:", None))
        self.label_114.setText(QCoreApplication.translate("Form", u"G.Holding:", None))
        self.label_115.setText(QCoreApplication.translate("Form", u"Bleeding:", None))
        self.filling_time_input.setPrefix("")
        self.filling_time_input.setSuffix(QCoreApplication.translate("Form", u" s", None))
        self.g_holding_time_input.setPrefix("")
        self.g_holding_time_input.setSuffix(QCoreApplication.translate("Form", u" s", None))
        self.bleeding_time_input.setPrefix("")
        self.bleeding_time_input.setSuffix(QCoreApplication.translate("Form", u" s", None))
        self.label_128.setText(QCoreApplication.translate("Form", u"Pressure:", None))
        self.pressure_pv_displ.setPrefix(QCoreApplication.translate("Form", u"PV: ", None))
        self.pressure_pv_displ.setSuffix(QCoreApplication.translate("Form", u" Bar", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"-", None))
        self.pressure_sv_input.setPrefix(QCoreApplication.translate("Form", u"SV: ", None))
        self.pressure_sv_input.setSuffix(QCoreApplication.translate("Form", u" Bar", None))
        self.label_112.setText(QCoreApplication.translate("Form", u"Refueling:", None))
        self.refuel_start_time_input.setPrefix(QCoreApplication.translate("Form", u"Start: ", None))
        self.refuel_start_time_input.setSuffix(QCoreApplication.translate("Form", u" s", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"-", None))
        self.refuel_end_time_input.setPrefix(QCoreApplication.translate("Form", u"End: ", None))
        self.refuel_end_time_input.setSuffix(QCoreApplication.translate("Form", u" s", None))
        self.label_55.setText(QCoreApplication.translate("Form", u"PV / SV Value A", None))
        self.label_272.setText("")
        self.sv_value_A_49.setPrefix(QCoreApplication.translate("Form", u"0 / ", None))
        self.sv_value_A_49.setSuffix("")
        self.label_185.setText(QCoreApplication.translate("Form", u"%", None))
        self.sv_value_A_50.setPrefix(QCoreApplication.translate("Form", u"0.0 / ", None))
        self.label_186.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.sv_value_A_51.setPrefix(QCoreApplication.translate("Form", u"0.00 / ", None))
        self.label_187.setText(QCoreApplication.translate("Form", u"s", None))
        self.sv_value_A_53.setPrefix(QCoreApplication.translate("Form", u"0 / ", None))
        self.label_188.setText(QCoreApplication.translate("Form", u"%", None))
        self.sv_value_A_54.setPrefix(QCoreApplication.translate("Form", u"0.0 / ", None))
        self.label_189.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.sv_value_A_55.setPrefix(QCoreApplication.translate("Form", u"0.0 / ", None))
        self.label_190.setText(QCoreApplication.translate("Form", u"s", None))
        self.sv_value_A_58.setPrefix(QCoreApplication.translate("Form", u"0 / ", None))
        self.label_191.setText(QCoreApplication.translate("Form", u"s", None))
        self.sv_value_A_60.setPrefix(QCoreApplication.translate("Form", u"0.0 / ", None))
        self.label_192.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.sv_value_A_61.setPrefix(QCoreApplication.translate("Form", u"0.00 / ", None))
        self.label_193.setText(QCoreApplication.translate("Form", u"s", None))
        self.sv_value_A_62.setPrefix(QCoreApplication.translate("Form", u"0 / ", None))
        self.label_194.setText(QCoreApplication.translate("Form", u"%", None))
        self.sv_value_A_63.setPrefix(QCoreApplication.translate("Form", u"0.0 / ", None))
        self.label_195.setText(QCoreApplication.translate("Form", u"s", None))
        self.sv_value_A_64.setSuffix("")
        self.sv_value_A_64.setPrefix(QCoreApplication.translate("Form", u"0 / ", None))
        self.label_196.setText(QCoreApplication.translate("Form", u"s", None))
        self.label_143.setText(QCoreApplication.translate("Form", u"T0", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Stable", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Heating", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.high_temp_input_21.setPrefix("")
        self.high_temp_input_21.setSuffix("")
        self.label_160.setText(QCoreApplication.translate("Form", u"-", None))
        self.pv_value_displ_21.setPrefix("")
        self.pv_value_displ_21.setSuffix("")
        self.label_161.setText(QCoreApplication.translate("Form", u"-", None))
        self.low_temp_input_21.setPrefix("")
        self.low_temp_input_21.setSuffix("")
        self.sv_value_input_21.setPrefix("")
        self.sv_value_input_21.setSuffix("")
        self.offset_value_input_21.setPrefix("")
        self.offset_value_input_21.setSuffix("")
        self.label_245.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.label_246.setText(QCoreApplication.translate("Form", u"\u00b0F", None))
        self.label_273.setText(QCoreApplication.translate("Form", u"A", None))
        self.label_274.setText(QCoreApplication.translate("Form", u"Front:", None))
        self.label_275.setText(QCoreApplication.translate("Form", u"Middle:", None))
        self.label_276.setText(QCoreApplication.translate("Form", u"End:", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"Stable", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"Heating", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.high_temp_input_34.setPrefix("")
        self.high_temp_input_34.setSuffix("")
        self.label_281.setText(QCoreApplication.translate("Form", u"-", None))
        self.pv_value_displ_34.setPrefix("")
        self.pv_value_displ_34.setSuffix("")
        self.label_282.setText(QCoreApplication.translate("Form", u"-", None))
        self.low_temp_input_34.setPrefix("")
        self.low_temp_input_34.setSuffix("")
        self.sv_value_input_34.setPrefix("")
        self.sv_value_input_34.setSuffix("")
        self.offset_value_input_34.setPrefix("")
        self.offset_value_input_34.setSuffix("")
        self.label_283.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.label_284.setText(QCoreApplication.translate("Form", u"\u00b0F", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"Stable", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"Heating", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.high_temp_input_35.setPrefix("")
        self.high_temp_input_35.setSuffix("")
        self.label_285.setText(QCoreApplication.translate("Form", u"-", None))
        self.pv_value_displ_35.setPrefix("")
        self.pv_value_displ_35.setSuffix("")
        self.label_286.setText(QCoreApplication.translate("Form", u"-", None))
        self.low_temp_input_35.setPrefix("")
        self.low_temp_input_35.setSuffix("")
        self.sv_value_input_35.setPrefix("")
        self.sv_value_input_35.setSuffix("")
        self.offset_value_input_35.setPrefix("")
        self.offset_value_input_35.setSuffix("")
        self.label_287.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.label_288.setText(QCoreApplication.translate("Form", u"\u00b0F", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"Stable", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"Heating", None))
        self.pushButton_14.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.high_temp_input_36.setPrefix("")
        self.high_temp_input_36.setSuffix("")
        self.label_289.setText(QCoreApplication.translate("Form", u"-", None))
        self.pv_value_displ_36.setPrefix("")
        self.pv_value_displ_36.setSuffix("")
        self.label_290.setText(QCoreApplication.translate("Form", u"-", None))
        self.low_temp_input_36.setPrefix("")
        self.low_temp_input_36.setSuffix("")
        self.sv_value_input_36.setPrefix("")
        self.sv_value_input_36.setSuffix("")
        self.offset_value_input_36.setPrefix("")
        self.offset_value_input_36.setSuffix("")
        self.label_291.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.label_292.setText(QCoreApplication.translate("Form", u"\u00b0F", None))
        self.label_180.setText(QCoreApplication.translate("Form", u"B", None))
        self.label_197.setText(QCoreApplication.translate("Form", u"Front:", None))
        self.label_198.setText(QCoreApplication.translate("Form", u"Middle:", None))
        self.label_199.setText(QCoreApplication.translate("Form", u"End:", None))
        self.pushButton_15.setText(QCoreApplication.translate("Form", u"Stable", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u"Heating", None))
        self.pushButton_17.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.high_temp_input_30.setPrefix("")
        self.high_temp_input_30.setSuffix("")
        self.label_233.setText(QCoreApplication.translate("Form", u"-", None))
        self.pv_value_displ_30.setPrefix("")
        self.pv_value_displ_30.setSuffix("")
        self.label_234.setText(QCoreApplication.translate("Form", u"-", None))
        self.low_temp_input_30.setPrefix("")
        self.low_temp_input_30.setSuffix("")
        self.sv_value_input_30.setPrefix("")
        self.sv_value_input_30.setSuffix("")
        self.offset_value_input_30.setPrefix("")
        self.offset_value_input_30.setSuffix("")
        self.label_263.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.label_264.setText(QCoreApplication.translate("Form", u"\u00b0F", None))
        self.pushButton_18.setText(QCoreApplication.translate("Form", u"Stable", None))
        self.pushButton_19.setText(QCoreApplication.translate("Form", u"Heating", None))
        self.pushButton_20.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.high_temp_input_31.setPrefix("")
        self.high_temp_input_31.setSuffix("")
        self.label_235.setText(QCoreApplication.translate("Form", u"-", None))
        self.pv_value_displ_31.setPrefix("")
        self.pv_value_displ_31.setSuffix("")
        self.label_236.setText(QCoreApplication.translate("Form", u"-", None))
        self.low_temp_input_31.setPrefix("")
        self.low_temp_input_31.setSuffix("")
        self.sv_value_input_31.setPrefix("")
        self.sv_value_input_31.setSuffix("")
        self.offset_value_input_31.setPrefix("")
        self.offset_value_input_31.setSuffix("")
        self.label_265.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.label_266.setText(QCoreApplication.translate("Form", u"\u00b0F", None))
        self.pushButton_24.setText(QCoreApplication.translate("Form", u"Stable", None))
        self.pushButton_25.setText(QCoreApplication.translate("Form", u"Heating", None))
        self.pushButton_26.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.high_temp_input_32.setPrefix("")
        self.high_temp_input_32.setSuffix("")
        self.label_267.setText(QCoreApplication.translate("Form", u"-", None))
        self.pv_value_displ_32.setPrefix("")
        self.pv_value_displ_32.setSuffix("")
        self.label_268.setText(QCoreApplication.translate("Form", u"-", None))
        self.low_temp_input_32.setPrefix("")
        self.low_temp_input_32.setSuffix("")
        self.sv_value_input_32.setPrefix("")
        self.sv_value_input_32.setSuffix("")
        self.offset_value_input_32.setPrefix("")
        self.offset_value_input_32.setSuffix("")
        self.label_269.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.label_270.setText(QCoreApplication.translate("Form", u"\u00b0F", None))
        self.label_170.setText(QCoreApplication.translate("Form", u"C", None))
        self.label_172.setText(QCoreApplication.translate("Form", u"Front:", None))
        self.label_173.setText(QCoreApplication.translate("Form", u"Middle:", None))
        self.label_174.setText(QCoreApplication.translate("Form", u"End:", None))
        self.pushButton_27.setText(QCoreApplication.translate("Form", u"Stable", None))
        self.pushButton_28.setText(QCoreApplication.translate("Form", u"Heating", None))
        self.pushButton_29.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.high_temp_input_26.setPrefix("")
        self.high_temp_input_26.setSuffix("")
        self.label_177.setText(QCoreApplication.translate("Form", u"-", None))
        self.pv_value_displ_26.setPrefix("")
        self.pv_value_displ_26.setSuffix("")
        self.label_178.setText(QCoreApplication.translate("Form", u"-", None))
        self.low_temp_input_26.setPrefix("")
        self.low_temp_input_26.setSuffix("")
        self.sv_value_input_26.setPrefix("")
        self.sv_value_input_26.setSuffix("")
        self.offset_value_input_26.setPrefix("")
        self.offset_value_input_26.setSuffix("")
        self.label_255.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.label_256.setText(QCoreApplication.translate("Form", u"\u00b0F", None))
        self.pushButton_30.setText(QCoreApplication.translate("Form", u"Stable", None))
        self.pushButton_31.setText(QCoreApplication.translate("Form", u"Heating", None))
        self.pushButton_32.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.high_temp_input_27.setPrefix("")
        self.high_temp_input_27.setSuffix("")
        self.label_179.setText(QCoreApplication.translate("Form", u"-", None))
        self.pv_value_displ_27.setPrefix("")
        self.pv_value_displ_27.setSuffix("")
        self.label_229.setText(QCoreApplication.translate("Form", u"-", None))
        self.low_temp_input_27.setPrefix("")
        self.low_temp_input_27.setSuffix("")
        self.sv_value_input_27.setPrefix("")
        self.sv_value_input_27.setSuffix("")
        self.offset_value_input_27.setPrefix("")
        self.offset_value_input_27.setSuffix("")
        self.label_257.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.label_258.setText(QCoreApplication.translate("Form", u"\u00b0F", None))
        self.pushButton_33.setText(QCoreApplication.translate("Form", u"Stable", None))
        self.pushButton_34.setText(QCoreApplication.translate("Form", u"Heating", None))
        self.pushButton_35.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.high_temp_input_28.setPrefix("")
        self.high_temp_input_28.setSuffix("")
        self.label_230.setText(QCoreApplication.translate("Form", u"-", None))
        self.pv_value_displ_28.setPrefix("")
        self.pv_value_displ_28.setSuffix("")
        self.label_231.setText(QCoreApplication.translate("Form", u"-", None))
        self.low_temp_input_28.setPrefix("")
        self.low_temp_input_28.setSuffix("")
        self.sv_value_input_28.setPrefix("")
        self.sv_value_input_28.setSuffix("")
        self.offset_value_input_28.setPrefix("")
        self.offset_value_input_28.setSuffix("")
        self.label_259.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.label_260.setText(QCoreApplication.translate("Form", u"\u00b0F", None))
    # retranslateUi


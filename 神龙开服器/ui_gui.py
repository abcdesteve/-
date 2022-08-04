# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_gui(object):
    def setupUi(self, gui):
        if not gui.objectName():
            gui.setObjectName(u"gui")
        gui.resize(400, 250)
        gui.setMinimumSize(QSize(400, 250))
        gui.setMaximumSize(QSize(400, 250))
        font = QFont()
        font.setFamilies([u"HarmonyOS Sans SC"])
        gui.setFont(font)
        self.centralwidget = QWidget(gui)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_java = QLabel(self.centralwidget)
        self.label_java.setObjectName(u"label_java")
        self.label_java.setGeometry(QRect(10, 13, 91, 31))
        font1 = QFont()
        font1.setFamilies([u"HarmonyOS Sans SC"])
        font1.setPointSize(10)
        self.label_java.setFont(font1)
        self.label_java.setAlignment(Qt.AlignCenter)
        self.combo_java = QComboBox(self.centralwidget)
        self.combo_java.setObjectName(u"combo_java")
        self.combo_java.setGeometry(QRect(100, 13, 291, 28))
        self.combo_java.setFont(font)
        self.combo_version = QComboBox(self.centralwidget)
        self.combo_version.setObjectName(u"combo_version")
        self.combo_version.setGeometry(QRect(100, 60, 291, 28))
        self.combo_version.setFont(font)
        self.label_version = QLabel(self.centralwidget)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setGeometry(QRect(10, 60, 91, 31))
        self.label_version.setFont(font1)
        self.label_version.setAlignment(Qt.AlignCenter)
        self.combo_map = QComboBox(self.centralwidget)
        self.combo_map.setObjectName(u"combo_map")
        self.combo_map.setGeometry(QRect(100, 130, 291, 28))
        self.combo_map.setFont(font)
        self.label_map = QLabel(self.centralwidget)
        self.label_map.setObjectName(u"label_map")
        self.label_map.setGeometry(QRect(10, 130, 91, 31))
        self.label_map.setFont(font1)
        self.label_map.setAlignment(Qt.AlignCenter)
        self.check_mod = QCheckBox(self.centralwidget)
        self.check_mod.setObjectName(u"check_mod")
        self.check_mod.setGeometry(QRect(280, 90, 111, 26))
        self.check_mod.setFont(font)
        self.check_mod.setCheckable(False)
        self.button_launch = QPushButton(self.centralwidget)
        self.button_launch.setObjectName(u"button_launch")
        self.button_launch.setGeometry(QRect(230, 210, 92, 29))
        self.button_launch.setFont(font1)
        self.button_tunnel = QPushButton(self.centralwidget)
        self.button_tunnel.setObjectName(u"button_tunnel")
        self.button_tunnel.setGeometry(QRect(80, 210, 92, 29))
        self.button_tunnel.setFont(font1)
        self.ram = QDoubleSpinBox(self.centralwidget)
        self.ram.setObjectName(u"ram")
        self.ram.setGeometry(QRect(100, 170, 81, 28))
        self.ram.setFont(font)
        self.ram.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ram.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.ram.setDecimals(1)
        self.ram.setMinimum(0.100000000000000)
        self.ram.setMaximum(16.000000000000000)
        self.ram.setSingleStep(0.100000000000000)
        self.ram.setStepType(QAbstractSpinBox.DefaultStepType)
        self.ram.setValue(0.500000000000000)
        self.label_ram = QLabel(self.centralwidget)
        self.label_ram.setObjectName(u"label_ram")
        self.label_ram.setGeometry(QRect(10, 170, 91, 31))
        self.label_ram.setFont(font1)
        self.label_ram.setAlignment(Qt.AlignCenter)
        self.button_flash = QPushButton(self.centralwidget)
        self.button_flash.setObjectName(u"button_flash")
        self.button_flash.setGeometry(QRect(350, 170, 41, 29))
        self.button_flash.setFont(font1)
        gui.setCentralWidget(self.centralwidget)

        self.retranslateUi(gui)

        QMetaObject.connectSlotsByName(gui)
    # setupUi

    def retranslateUi(self, gui):
        gui.setWindowTitle(QCoreApplication.translate("gui", u"\u795e\u9f99\u5f00\u670d\u5668", None))
        self.label_java.setText(QCoreApplication.translate("gui", u"java\u7248\u672c\uff1a", None))
        self.label_version.setText(QCoreApplication.translate("gui", u"\u6e38\u620f\u7248\u672c\uff1a", None))
        self.label_map.setText(QCoreApplication.translate("gui", u"\u6e38\u620f\u5730\u56fe\uff1a", None))
        self.check_mod.setText(QCoreApplication.translate("gui", u"\u542f\u7528\u6a21\u7ec4(\u00d7)", None))
        self.button_launch.setText(QCoreApplication.translate("gui", u"\u542f\u52a8\u670d\u52a1\u5668", None))
        self.button_tunnel.setText(QCoreApplication.translate("gui", u"\u5f00\u542f\u96a7\u9053", None))
        self.ram.setPrefix("")
        self.ram.setSuffix(QCoreApplication.translate("gui", u"GB", None))
        self.label_ram.setText(QCoreApplication.translate("gui", u"\u6700\u5927\u5185\u5b58\uff1a", None))
        self.button_flash.setText(QCoreApplication.translate("gui", u"\u5237\u65b0", None))
    # retranslateUi


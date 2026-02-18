# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dados.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QSizePolicy, QSlider, QWidget)

class Ui_Dados(object):
    def setupUi(self, Dados):
        if not Dados.objectName():
            Dados.setObjectName(u"Dados")
        Dados.resize(371, 240)
        Dados.setStyleSheet(u"background-color: #E0FFFF;")
        self.centralwidget = QWidget(Dados)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 40, 241, 129))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: #AFEEEE;\n"
"color: rgb(0, 0, 0);")
        self.label.setFrameShape(QFrame.Box)
        self.label.setLineWidth(2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: #AFEEEE;\n"
"color: rgb(0, 0, 0);")
        self.label_2.setFrameShape(QFrame.Box)
        self.label_2.setLineWidth(2)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: #AFEEEE;\n"
"color: rgb(0, 0, 0);")
        self.label_3.setFrameShape(QFrame.Box)
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_3.setLineWidth(2)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)

        self.Slider_dados = QSlider(self.layoutWidget)
        self.Slider_dados.setObjectName(u"Slider_dados")
        self.Slider_dados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Slider_dados.setStyleSheet(u"background-color: #AFEEEE;")
        self.Slider_dados.setMaximum(1)
        self.Slider_dados.setOrientation(Qt.Horizontal)
        self.Slider_dados.setTickPosition(QSlider.TicksBothSides)
        self.Slider_dados.setTickInterval(0)

        self.gridLayout.addWidget(self.Slider_dados, 2, 0, 1, 2)

        Dados.setCentralWidget(self.centralwidget)

        self.retranslateUi(Dados)

        QMetaObject.connectSlotsByName(Dados)
    # setupUi

    def retranslateUi(self, Dados):
        Dados.setWindowTitle(QCoreApplication.translate("Dados", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Dados", u"Coleta de Dados", None))
        self.label_2.setText(QCoreApplication.translate("Dados", u"Parar", None))
        self.label_3.setText(QCoreApplication.translate("Dados", u"Iniciar", None))
    # retranslateUi


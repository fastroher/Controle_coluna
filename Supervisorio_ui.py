# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Supervisorio.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QDial, QGraphicsView, QGridLayout,
    QHBoxLayout, QHeaderView, QLCDNumber, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QToolBox, QVBoxLayout,
    QWidget)
import Imagens_rc
import sys

class Ui_Superv_geral(object):
    def setupUi(self, Superv_geral):
        if not Superv_geral.objectName():
            Superv_geral.setObjectName(u"Superv_geral")
        Superv_geral.resize(1389, 839)
        Superv_geral.setStyleSheet(u"background-color: #E0FFFF;")
        self.layout_principal = QWidget(Superv_geral)
        self.layout_principal.setObjectName(u"layout_principal")
        self.horizontalLayout_5 = QHBoxLayout(self.layout_principal)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.layout_graph = QVBoxLayout()
        self.layout_graph.setObjectName(u"layout_graph")
        self.graph_xD = QGraphicsView(self.layout_principal)
        self.graph_xD.setObjectName(u"graph_xD")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_xD.sizePolicy().hasHeightForWidth())
        self.graph_xD.setSizePolicy(sizePolicy)
        self.graph_xD.setStyleSheet(u"background-color: white;")

        self.layout_graph.addWidget(self.graph_xD)

        self.graph_T = QGraphicsView(self.layout_principal)
        self.graph_T.setObjectName(u"graph_T")
        self.graph_T.setStyleSheet(u"background-color: white;")

        self.layout_graph.addWidget(self.graph_T)

        self.table_T = QTableWidget(self.layout_principal)
        self.table_T.setObjectName(u"table_T")
        self.table_T.setStyleSheet(u"background-color: white;")

        self.layout_graph.addWidget(self.table_T)


        self.horizontalLayout_5.addLayout(self.layout_graph)

        self.layout_col = QGridLayout()
        self.layout_col.setObjectName(u"layout_col")
        self.layout_col.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.layout_col.setHorizontalSpacing(7)
        self.label_col = QLabel(self.layout_principal)
        self.label_col.setObjectName(u"label_col")

        self.layout_col.addWidget(self.label_col, 0, 0, 1, 1)


        self.horizontalLayout_5.addLayout(self.layout_col)

        self.layout_ctr_see = QVBoxLayout()
        self.layout_ctr_see.setObjectName(u"layout_ctr_see")
        self.toolBox = QToolBox(self.layout_principal)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy1)
        self.toolBox.setStyleSheet(u"background-color: #AFEEEE;\n"
"font-weight: bold;\n"
"")
        self.layout_tool_manual = QWidget()
        self.layout_tool_manual.setObjectName(u"layout_tool_manual")
        self.layout_tool_manual.setGeometry(QRect(0, 0, 342, 212))
        self.gridLayout_2 = QGridLayout(self.layout_tool_manual)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.layout_ctr_VL = QVBoxLayout()
        self.layout_ctr_VL.setObjectName(u"layout_ctr_VL")
        self.label_VL = QLabel(self.layout_tool_manual)
        self.label_VL.setObjectName(u"label_VL")

        self.layout_ctr_VL.addWidget(self.label_VL)

        self.lcd_VL = QLCDNumber(self.layout_tool_manual)
        self.lcd_VL.setObjectName(u"lcd_VL")
        self.lcd_VL.setStyleSheet(u"background-color: white;")

        self.layout_ctr_VL.addWidget(self.lcd_VL)

        self.dial_ctr_VL = QDial(self.layout_tool_manual)
        self.dial_ctr_VL.setObjectName(u"dial_ctr_VL")
        self.dial_ctr_VL.setStyleSheet(u"background-color: #B0E0E6;")

        self.layout_ctr_VL.addWidget(self.dial_ctr_VL)


        self.gridLayout_2.addLayout(self.layout_ctr_VL, 0, 1, 1, 1)

        self.layout_ctr_VD = QVBoxLayout()
        self.layout_ctr_VD.setObjectName(u"layout_ctr_VD")
        self.label_VD = QLabel(self.layout_tool_manual)
        self.label_VD.setObjectName(u"label_VD")

        self.layout_ctr_VD.addWidget(self.label_VD)

        self.lcd_VD = QLCDNumber(self.layout_tool_manual)
        self.lcd_VD.setObjectName(u"lcd_VD")
        self.lcd_VD.setStyleSheet(u"background-color: white;")

        self.layout_ctr_VD.addWidget(self.lcd_VD)

        self.dial_ctr_VD = QDial(self.layout_tool_manual)
        self.dial_ctr_VD.setObjectName(u"dial_ctr_VD")
        self.dial_ctr_VD.setStyleSheet(u"background-color: #B0E0E6;")

        self.layout_ctr_VD.addWidget(self.dial_ctr_VD)


        self.gridLayout_2.addLayout(self.layout_ctr_VD, 0, 0, 1, 1)

        self.layout_ctr_RB = QVBoxLayout()
        self.layout_ctr_RB.setObjectName(u"layout_ctr_RB")
        self.label_RB = QLabel(self.layout_tool_manual)
        self.label_RB.setObjectName(u"label_RB")

        self.layout_ctr_RB.addWidget(self.label_RB)

        self.lcd_RB = QLCDNumber(self.layout_tool_manual)
        self.lcd_RB.setObjectName(u"lcd_RB")
        self.lcd_RB.setStyleSheet(u"background-color: white;")

        self.layout_ctr_RB.addWidget(self.lcd_RB)

        self.dial_RB = QDial(self.layout_tool_manual)
        self.dial_RB.setObjectName(u"dial_RB")
        self.dial_RB.setStyleSheet(u"background-color: #B0E0E6;")

        self.layout_ctr_RB.addWidget(self.dial_RB)


        self.gridLayout_2.addLayout(self.layout_ctr_RB, 0, 2, 1, 1)

        self.pushButton = QPushButton(self.layout_tool_manual)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #DC3545 ;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #28a745;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border: 1px solid #218838;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d0d0d0;\n"
"}")
        self.pushButton.setCheckable(True)

        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.layout_tool_manual)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #DC3545 ;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #28a745;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border: 1px solid #218838;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d0d0d0;\n"
"}")

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 2, 1, 1)

        self.toolBox.addItem(self.layout_tool_manual, u"Controle Manual")
        self.layout_tool_auto = QWidget()
        self.layout_tool_auto.setObjectName(u"layout_tool_auto")
        self.layout_tool_auto.setGeometry(QRect(0, 0, 142, 85))
        self.horizontalLayout = QHBoxLayout(self.layout_tool_auto)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_3 = QPushButton(self.layout_tool_auto)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.toolBox.addItem(self.layout_tool_auto, u"Controle Autom\u00e1tico")

        self.layout_ctr_see.addWidget(self.toolBox)

        self.layout_see_xD = QHBoxLayout()
        self.layout_see_xD.setObjectName(u"layout_see_xD")
        self.label_xD = QLabel(self.layout_principal)
        self.label_xD.setObjectName(u"label_xD")
        self.label_xD.setStyleSheet(u"background-color: #B0E0E6;\n"
"color: black;\n"
"font-weight: bold;\n"
"font-size:20px;\n"
"border: 1px solid #cccccc;\n"
"padding: 5px;\n"
"border-radius: 3px;\n"
"text-align: center;\n"
"padding: center;\n"
"")

        self.layout_see_xD.addWidget(self.label_xD)

        self.lcd_xD = QLCDNumber(self.layout_principal)
        self.lcd_xD.setObjectName(u"lcd_xD")
        self.lcd_xD.setStyleSheet(u"background-color: white;")

        self.layout_see_xD.addWidget(self.lcd_xD)


        self.layout_ctr_see.addLayout(self.layout_see_xD)

        self.layout_see_xB = QHBoxLayout()
        self.layout_see_xB.setObjectName(u"layout_see_xB")
        self.label_xB = QLabel(self.layout_principal)
        self.label_xB.setObjectName(u"label_xB")
        self.label_xB.setStyleSheet(u"background-color: #B0E0E6;\n"
"color: black;\n"
"font-weight: bold;\n"
"font-size:20px;\n"
"border: 1px solid #cccccc;\n"
"padding: 5px;\n"
"border-radius: 3px;\n"
"text-align: center;\n"
"padding: center;\n"
"")

        self.layout_see_xB.addWidget(self.label_xB)

        self.lcd_xB = QLCDNumber(self.layout_principal)
        self.lcd_xB.setObjectName(u"lcd_xB")
        self.lcd_xB.setStyleSheet(u"background-color: white;")

        self.layout_see_xB.addWidget(self.lcd_xB)


        self.layout_ctr_see.addLayout(self.layout_see_xB)

        self.layout_see_MD = QHBoxLayout()
        self.layout_see_MD.setObjectName(u"layout_see_MD")
        self.label_MD = QLabel(self.layout_principal)
        self.label_MD.setObjectName(u"label_MD")
        self.label_MD.setStyleSheet(u"background-color: #B0E0E6;\n"
"color: black;\n"
"font-weight: bold;\n"
"font-size:20px;\n"
"border: 1px solid #cccccc;\n"
"padding: 5px;\n"
"border-radius: 3px;\n"
"text-align: center;\n"
"padding: center;")

        self.layout_see_MD.addWidget(self.label_MD)

        self.lcd_MD = QLCDNumber(self.layout_principal)
        self.lcd_MD.setObjectName(u"lcd_MD")
        self.lcd_MD.setStyleSheet(u"background-color: white;")

        self.layout_see_MD.addWidget(self.lcd_MD)


        self.layout_ctr_see.addLayout(self.layout_see_MD)

        self.layout_see_MB = QHBoxLayout()
        self.layout_see_MB.setObjectName(u"layout_see_MB")
        self.label_MB = QLabel(self.layout_principal)
        self.label_MB.setObjectName(u"label_MB")
        self.label_MB.setStyleSheet(u"background-color: #B0E0E6;\n"
"color: black;\n"
"font-weight: bold;\n"
"font-size:20px;\n"
"border: 1px solid #cccccc;\n"
"padding: 5px;\n"
"border-radius: 3px;\n"
"text-align: center;\n"
"padding: center;")

        self.layout_see_MB.addWidget(self.label_MB)

        self.lcd_MB = QLCDNumber(self.layout_principal)
        self.lcd_MB.setObjectName(u"lcd_MB")
        self.lcd_MB.setStyleSheet(u"background-color: white;")

        self.layout_see_MB.addWidget(self.lcd_MB)


        self.layout_ctr_see.addLayout(self.layout_see_MB)


        self.horizontalLayout_5.addLayout(self.layout_ctr_see)

        Superv_geral.setCentralWidget(self.layout_principal)

        self.retranslateUi(Superv_geral)
        self.dial_ctr_VD.valueChanged.connect(self.lcd_VD.display)
        self.dial_ctr_VL.valueChanged.connect(self.lcd_VL.display)
        self.dial_RB.valueChanged.connect(self.lcd_RB.display)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Superv_geral)
    # setupUi

    def retranslateUi(self, Superv_geral):
        Superv_geral.setWindowTitle(QCoreApplication.translate("Superv_geral", u"MainWindow", None))
        self.label_col.setText(QCoreApplication.translate("Superv_geral", u"<html><head/><body><p align=\"center\"><img src=\":/Imagens/Imagens/Coluna destila\u00e7\u00e3o v5.png\"/></p></body></html>", None))
        self.label_VL.setText(QCoreApplication.translate("Superv_geral", u"VL", None))
        self.label_VD.setText(QCoreApplication.translate("Superv_geral", u"VD", None))
        self.label_RB.setText(QCoreApplication.translate("Superv_geral", u"RB", None))
        self.pushButton.setText(QCoreApplication.translate("Superv_geral", u"Resist\u00eancia 1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Superv_geral", u"Resis\u00eancia 2", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.layout_tool_manual), QCoreApplication.translate("Superv_geral", u"Controle Manual", None))
        self.pushButton_3.setText(QCoreApplication.translate("Superv_geral", u"PushButton", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.layout_tool_auto), QCoreApplication.translate("Superv_geral", u"Controle Autom\u00e1tico", None))
        self.label_xD.setText(QCoreApplication.translate("Superv_geral", u"xD", None))
        self.label_xB.setText(QCoreApplication.translate("Superv_geral", u"xB", None))
        self.label_MD.setText(QCoreApplication.translate("Superv_geral", u"MD", None))
        self.label_MB.setText(QCoreApplication.translate("Superv_geral", u"MB", None))

class SupervisaoGeralApp:
    def __init__(self):
        # Inicializa a aplicação Qt
        self.app = QApplication.instance() or QApplication(sys.argv)
        # Cria a janela principal
        self.window = QMainWindow()
        # Cria a instância da UI
        self.ui = Ui_Superv_geral()
        # Configura a UI na janela
        self.ui.setupUi(self.window)
    
    def show(self):
        """Mostra a janela"""
        self.window.show()
        return self.app.exec()
    
    def get_ui_instance(self):
          return self.ui
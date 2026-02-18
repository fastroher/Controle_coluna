# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Supervisorio.ui'
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
from PySide6.QtWidgets import (QApplication, QDial, QGraphicsView, QGridLayout,
    QGroupBox, QHBoxLayout, QLCDNumber, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QToolBox,
    QVBoxLayout, QWidget)
import UIs.Imagens_rc as Imagens_rc

class Ui_Superv_geral(object):
    def setupUi(self, Superv_geral):
        if not Superv_geral.objectName():
            Superv_geral.setObjectName(u"Superv_geral")
        Superv_geral.resize(1375, 817)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Superv_geral.sizePolicy().hasHeightForWidth())
        Superv_geral.setSizePolicy(sizePolicy)
        Superv_geral.setMinimumSize(QSize(1375, 817))
        Superv_geral.setStyleSheet(u"background-color: #E0FFFF;")
        self.layout_principal = QWidget(Superv_geral)
        self.layout_principal.setObjectName(u"layout_principal")
        self.horizontalLayout = QHBoxLayout(self.layout_principal)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.graph_xD = QGraphicsView(self.layout_principal)
        self.graph_xD.setObjectName(u"graph_xD")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.graph_xD.sizePolicy().hasHeightForWidth())
        self.graph_xD.setSizePolicy(sizePolicy1)
        self.graph_xD.setStyleSheet(u"background-color: white;")

        self.verticalLayout_7.addWidget(self.graph_xD)

        self.graph_T = QGraphicsView(self.layout_principal)
        self.graph_T.setObjectName(u"graph_T")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.graph_T.sizePolicy().hasHeightForWidth())
        self.graph_T.setSizePolicy(sizePolicy2)
        self.graph_T.setStyleSheet(u"background-color: white;")

        self.verticalLayout_7.addWidget(self.graph_T)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.label_col = QLabel(self.layout_principal)
        self.label_col.setObjectName(u"label_col")

        self.horizontalLayout.addWidget(self.label_col)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.toolBox = QToolBox(self.layout_principal)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy3)
        self.toolBox.setMinimumSize(QSize(240, 480))
        self.toolBox.setMaximumSize(QSize(250, 500))
        self.toolBox.setStyleSheet(u"background-color: #AFEEEE;\n"
"font-weight: bold;\n"
"color: black;\n"
"")
        self.layout_tool_manual = QWidget()
        self.layout_tool_manual.setObjectName(u"layout_tool_manual")
        self.layout_tool_manual.setGeometry(QRect(0, 0, 240, 418))
        self.gridLayout = QGridLayout(self.layout_tool_manual)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(self.layout_tool_manual)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"background-color: #B0E0E6;")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lcd_VL = QLCDNumber(self.groupBox_2)
        self.lcd_VL.setObjectName(u"lcd_VL")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lcd_VL.sizePolicy().hasHeightForWidth())
        self.lcd_VL.setSizePolicy(sizePolicy4)
        self.lcd_VL.setStyleSheet(u"background-color: white;")

        self.verticalLayout.addWidget(self.lcd_VL)

        self.dial_ctr_VL = QDial(self.groupBox_2)
        self.dial_ctr_VL.setObjectName(u"dial_ctr_VL")
        sizePolicy.setHeightForWidth(self.dial_ctr_VL.sizePolicy().hasHeightForWidth())
        self.dial_ctr_VL.setSizePolicy(sizePolicy)
        self.dial_ctr_VL.setMinimumSize(QSize(50, 50))
        self.dial_ctr_VL.setMaximumSize(QSize(70, 70))
        self.dial_ctr_VL.setStyleSheet(u"background-color: #9ECACF;")

        self.verticalLayout.addWidget(self.dial_ctr_VL)


        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.layout_tool_manual)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"background-color: #B0E0E6;")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lcd_VD = QLCDNumber(self.groupBox_3)
        self.lcd_VD.setObjectName(u"lcd_VD")
        sizePolicy4.setHeightForWidth(self.lcd_VD.sizePolicy().hasHeightForWidth())
        self.lcd_VD.setSizePolicy(sizePolicy4)
        self.lcd_VD.setStyleSheet(u"background-color: white;")

        self.verticalLayout_2.addWidget(self.lcd_VD)

        self.dial_ctr_VD = QDial(self.groupBox_3)
        self.dial_ctr_VD.setObjectName(u"dial_ctr_VD")
        self.dial_ctr_VD.setMinimumSize(QSize(50, 50))
        self.dial_ctr_VD.setMaximumSize(QSize(70, 70))
        self.dial_ctr_VD.setStyleSheet(u"background-color: #9ECACF;")

        self.verticalLayout_2.addWidget(self.dial_ctr_VD)


        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.layout_tool_manual)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"background-color: #B0E0E6;")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lcd_VF = QLCDNumber(self.groupBox_4)
        self.lcd_VF.setObjectName(u"lcd_VF")
        sizePolicy4.setHeightForWidth(self.lcd_VF.sizePolicy().hasHeightForWidth())
        self.lcd_VF.setSizePolicy(sizePolicy4)
        self.lcd_VF.setStyleSheet(u"background-color: white;")

        self.verticalLayout_4.addWidget(self.lcd_VF)

        self.dial_ctr_VF = QDial(self.groupBox_4)
        self.dial_ctr_VF.setObjectName(u"dial_ctr_VF")
        self.dial_ctr_VF.setMinimumSize(QSize(50, 50))
        self.dial_ctr_VF.setMaximumSize(QSize(70, 70))
        self.dial_ctr_VF.setStyleSheet(u"background-color: #9ECACF;")

        self.verticalLayout_4.addWidget(self.dial_ctr_VF)


        self.gridLayout.addWidget(self.groupBox_4, 1, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.layout_tool_manual)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"background-color: #B0E0E6;")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lcd_VB = QLCDNumber(self.groupBox_5)
        self.lcd_VB.setObjectName(u"lcd_VB")
        self.lcd_VB.setStyleSheet(u"background-color: white;")

        self.verticalLayout_8.addWidget(self.lcd_VB)

        self.dial_ctr_VB = QDial(self.groupBox_5)
        self.dial_ctr_VB.setObjectName(u"dial_ctr_VB")
        self.dial_ctr_VB.setMinimumSize(QSize(50, 50))
        self.dial_ctr_VB.setMaximumSize(QSize(70, 70))
        self.dial_ctr_VB.setStyleSheet(u"background-color: #9ECACF;")

        self.verticalLayout_8.addWidget(self.dial_ctr_VB)


        self.gridLayout.addWidget(self.groupBox_5, 1, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.layout_tool_manual)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setStyleSheet(u"background-color: #B0E0E6;")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lcd_RB = QLCDNumber(self.groupBox_6)
        self.lcd_RB.setObjectName(u"lcd_RB")
        self.lcd_RB.setStyleSheet(u"background-color: white;")

        self.verticalLayout_9.addWidget(self.lcd_RB)

        self.dial_RB = QDial(self.groupBox_6)
        self.dial_RB.setObjectName(u"dial_RB")
        self.dial_RB.setMinimumSize(QSize(50, 50))
        self.dial_RB.setMaximumSize(QSize(70, 70))
        self.dial_RB.setStyleSheet(u"background-color: #9ECACF;")

        self.verticalLayout_9.addWidget(self.dial_RB)


        self.gridLayout.addWidget(self.groupBox_6, 2, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.button_R1 = QPushButton(self.layout_tool_manual)
        self.button_R1.setObjectName(u"button_R1")
        self.button_R1.setStyleSheet(u"QPushButton {\n"
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
        self.button_R1.setCheckable(True)

        self.verticalLayout_6.addWidget(self.button_R1)

        self.button_R2 = QPushButton(self.layout_tool_manual)
        self.button_R2.setObjectName(u"button_R2")
        self.button_R2.setStyleSheet(u"QPushButton {\n"
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
        self.button_R2.setCheckable(True)

        self.verticalLayout_6.addWidget(self.button_R2)


        self.gridLayout.addLayout(self.verticalLayout_6, 2, 1, 1, 1)

        self.toolBox.addItem(self.layout_tool_manual, u"Controle Manual")
        self.layout_tool_auto = QWidget()
        self.layout_tool_auto.setObjectName(u"layout_tool_auto")
        self.layout_tool_auto.setGeometry(QRect(0, 0, 240, 418))
        self.verticalLayout_5 = QVBoxLayout(self.layout_tool_auto)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.button_Dados = QPushButton(self.layout_tool_auto)
        self.button_Dados.setObjectName(u"button_Dados")
        self.button_Dados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_Dados.setStyleSheet(u"background-color: #B0E0E6;")

        self.verticalLayout_5.addWidget(self.button_Dados)

        self.button_ID = QPushButton(self.layout_tool_auto)
        self.button_ID.setObjectName(u"button_ID")
        self.button_ID.setStyleSheet(u"background-color: #B0E0E6;")

        self.verticalLayout_5.addWidget(self.button_ID)

        self.button_RNA = QPushButton(self.layout_tool_auto)
        self.button_RNA.setObjectName(u"button_RNA")
        self.button_RNA.setStyleSheet(u"background-color: #B0E0E6;")

        self.verticalLayout_5.addWidget(self.button_RNA)

        self.button_pred = QPushButton(self.layout_tool_auto)
        self.button_pred.setObjectName(u"button_pred")
        self.button_pred.setStyleSheet(u"background-color: #B0E0E6;")

        self.verticalLayout_5.addWidget(self.button_pred)

        self.toolBox.addItem(self.layout_tool_auto, u"Controle Autom\u00e1tico")

        self.verticalLayout_10.addWidget(self.toolBox)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_xD = QLabel(self.layout_principal)
        self.label_xD.setObjectName(u"label_xD")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.label_xD.sizePolicy().hasHeightForWidth())
        self.label_xD.setSizePolicy(sizePolicy5)
        self.label_xD.setMinimumSize(QSize(0, 37))
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

        self.horizontalLayout_6.addWidget(self.label_xD)

        self.lcd_xD = QLCDNumber(self.layout_principal)
        self.lcd_xD.setObjectName(u"lcd_xD")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lcd_xD.sizePolicy().hasHeightForWidth())
        self.lcd_xD.setSizePolicy(sizePolicy6)
        self.lcd_xD.setStyleSheet(u"background-color: white;")

        self.horizontalLayout_6.addWidget(self.lcd_xD)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_xB = QLabel(self.layout_principal)
        self.label_xB.setObjectName(u"label_xB")
        sizePolicy5.setHeightForWidth(self.label_xB.sizePolicy().hasHeightForWidth())
        self.label_xB.setSizePolicy(sizePolicy5)
        self.label_xB.setMinimumSize(QSize(0, 37))
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

        self.horizontalLayout_5.addWidget(self.label_xB)

        self.lcd_xB = QLCDNumber(self.layout_principal)
        self.lcd_xB.setObjectName(u"lcd_xB")
        sizePolicy6.setHeightForWidth(self.lcd_xB.sizePolicy().hasHeightForWidth())
        self.lcd_xB.setSizePolicy(sizePolicy6)
        self.lcd_xB.setStyleSheet(u"background-color: white;")

        self.horizontalLayout_5.addWidget(self.lcd_xB)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_MD = QLabel(self.layout_principal)
        self.label_MD.setObjectName(u"label_MD")
        sizePolicy5.setHeightForWidth(self.label_MD.sizePolicy().hasHeightForWidth())
        self.label_MD.setSizePolicy(sizePolicy5)
        self.label_MD.setMinimumSize(QSize(0, 37))
        self.label_MD.setStyleSheet(u"background-color: #B0E0E6;\n"
"color: black;\n"
"font-weight: bold;\n"
"font-size:20px;\n"
"border: 1px solid #cccccc;\n"
"padding: 5px;\n"
"border-radius: 3px;\n"
"text-align: center;\n"
"padding: center;")

        self.horizontalLayout_4.addWidget(self.label_MD)

        self.lcd_MD = QLCDNumber(self.layout_principal)
        self.lcd_MD.setObjectName(u"lcd_MD")
        sizePolicy6.setHeightForWidth(self.lcd_MD.sizePolicy().hasHeightForWidth())
        self.lcd_MD.setSizePolicy(sizePolicy6)
        self.lcd_MD.setStyleSheet(u"background-color: white;")

        self.horizontalLayout_4.addWidget(self.lcd_MD)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_MB = QLabel(self.layout_principal)
        self.label_MB.setObjectName(u"label_MB")
        sizePolicy5.setHeightForWidth(self.label_MB.sizePolicy().hasHeightForWidth())
        self.label_MB.setSizePolicy(sizePolicy5)
        self.label_MB.setMinimumSize(QSize(0, 36))
        self.label_MB.setStyleSheet(u"background-color: #B0E0E6;\n"
"color: black;\n"
"font-weight: bold;\n"
"font-size:20px;\n"
"border: 1px solid #cccccc;\n"
"padding: 5px;\n"
"border-radius: 3px;\n"
"text-align: center;\n"
"padding: center;")

        self.horizontalLayout_3.addWidget(self.label_MB)

        self.lcd_MB = QLCDNumber(self.layout_principal)
        self.lcd_MB.setObjectName(u"lcd_MB")
        sizePolicy6.setHeightForWidth(self.lcd_MB.sizePolicy().hasHeightForWidth())
        self.lcd_MB.setSizePolicy(sizePolicy6)
        self.lcd_MB.setStyleSheet(u"background-color: white;")

        self.horizontalLayout_3.addWidget(self.lcd_MB)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_10.addLayout(self.verticalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout_10)

        Superv_geral.setCentralWidget(self.layout_principal)

        self.retranslateUi(Superv_geral)
        self.dial_ctr_VD.valueChanged.connect(self.lcd_VD.display)
        self.dial_RB.valueChanged.connect(self.lcd_RB.display)
        self.dial_ctr_VF.valueChanged.connect(self.lcd_VF.display)
        self.dial_ctr_VL.valueChanged.connect(self.lcd_VL.display)
        self.dial_ctr_VB.valueChanged.connect(self.lcd_VB.display)

        self.toolBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Superv_geral)
    # setupUi

    def retranslateUi(self, Superv_geral):
        Superv_geral.setWindowTitle(QCoreApplication.translate("Superv_geral", u"MainWindow", None))
        self.label_col.setText(QCoreApplication.translate("Superv_geral", u"<html><head/><body><p align=\"center\"><img src=\":/Imagens/Imagens/Coluna destila\u00e7\u00e3o v5.png\"/></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Superv_geral", u"VL", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Superv_geral", u"VD", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Superv_geral", u"VF", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Superv_geral", u"VB", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Superv_geral", u"RB", None))
        self.button_R1.setText(QCoreApplication.translate("Superv_geral", u"Resist\u00eancia 1", None))
        self.button_R2.setText(QCoreApplication.translate("Superv_geral", u"Resis\u00eancia 2", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.layout_tool_manual), QCoreApplication.translate("Superv_geral", u"Controle Manual", None))
        self.button_Dados.setText(QCoreApplication.translate("Superv_geral", u"Dados", None))
        self.button_ID.setText(QCoreApplication.translate("Superv_geral", u"Identifica\u00e7\u00e3o", None))
        self.button_RNA.setText(QCoreApplication.translate("Superv_geral", u"Redes Neurais", None))
        self.button_pred.setText(QCoreApplication.translate("Superv_geral", u"Control Preditivo", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.layout_tool_auto), QCoreApplication.translate("Superv_geral", u"Controle Autom\u00e1tico", None))
        self.label_xD.setText(QCoreApplication.translate("Superv_geral", u"xD", None))
        self.label_xB.setText(QCoreApplication.translate("Superv_geral", u"xB", None))
        self.label_MD.setText(QCoreApplication.translate("Superv_geral", u"MD", None))
        self.label_MB.setText(QCoreApplication.translate("Superv_geral", u"MB", None))
    # retranslateUi


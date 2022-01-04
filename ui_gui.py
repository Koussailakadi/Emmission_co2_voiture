# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_guisQckft.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1291, 816)
        MainWindow.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Titre_frame = QFrame(self.centralwidget)
        self.Titre_frame.setObjectName(u"Titre_frame")
        self.Titre_frame.setMinimumSize(QSize(0, 101))
        self.Titre_frame.setMaximumSize(QSize(16777215, 101))
        self.Titre_frame.setFrameShape(QFrame.StyledPanel)
        self.Titre_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Titre_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Title = QLabel(self.Titre_frame)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setPointSize(12)
        self.Title.setFont(font)
        self.Title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Title)

        self.Titre_bouton = QFrame(self.Titre_frame)
        self.Titre_bouton.setObjectName(u"Titre_bouton")
        self.Titre_bouton.setMinimumSize(QSize(121, 41))
        self.Titre_bouton.setMaximumSize(QSize(121, 41))
        self.Titre_bouton.setFrameShape(QFrame.StyledPanel)
        self.Titre_bouton.setFrameShadow(QFrame.Raised)
        self.minimizeButton = QPushButton(self.Titre_bouton)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setGeometry(QRect(10, 10, 25, 24))
        self.minimizeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizeButton.setStyleSheet(u"background-color: rgb(84, 84, 126);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon)
        self.minimizeButton.setIconSize(QSize(24, 24))
        self.closeButton = QPushButton(self.Titre_bouton)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(84, 10, 24, 24))
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.setStyleSheet(u"background-repeat: none;\n"
"background-position: center left;\n"
"background-image: url(:/icons/icons/cil-x.png);\n"
"background-color: rgb(84, 84, 126);\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon1)
        self.closeButton.setIconSize(QSize(24, 24))
        self.restoreButton = QPushButton(self.Titre_bouton)
        self.restoreButton.setObjectName(u"restoreButton")
        self.restoreButton.setGeometry(QRect(47, 10, 25, 24))
        self.restoreButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.restoreButton.setStyleSheet(u"background-image: url(:/icons/icons/cil-window-maximize.png);\n"
"background-repeat: none;\n"
"background-position: center left;\n"
"background-color: rgb(84, 84, 126);\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreButton.setIcon(icon2)
        self.restoreButton.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.Titre_bouton)


        self.verticalLayout_3.addWidget(self.Titre_frame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.Database_config = QWidget()
        self.Database_config.setObjectName(u"Database_config")
        self.verticalLayout = QVBoxLayout(self.Database_config)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.Database_config)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.Database_config)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 600))
        self.frame_4.setMaximumSize(QSize(16777215, 600))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 550))
        self.frame_7.setMaximumSize(QSize(16777215, 550))
        self.frame_7.setStyleSheet(u"background-color: none;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(680, 550))
        self.frame_6.setMaximumSize(QSize(680, 550))
        self.frame_6.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(218, 218, 218);\n"
"}\n"
"QPushButton{\n"
"	padding: 20px 10px;\n"
"	border: none;\n"
"	border-left: 2px solid transparent;\n"
"	border-bottom: 2px solid transparent;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(68, 68, 102);\n"
"	color: rgb(140, 140, 140);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 92, 157);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:  rgb(0, 92, 157);\n"
"	border-bottom: 2px solid rgb(255, 165, 24);\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 34, 653, 157))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.frame_14 = QFrame(self.frame_6)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(340, 360, 323, 157))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.valid_config = QPushButton(self.frame_14)
        self.valid_config.setObjectName(u"valid_config")
        self.valid_config.setGeometry(QRect(150, 30, 111, 31))
        self.cancel_config = QPushButton(self.frame_14)
        self.cancel_config.setObjectName(u"cancel_config")
        self.cancel_config.setGeometry(QRect(20, 30, 111, 31))
        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(340, 197, 323, 157))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.Database_name = QLineEdit(self.frame_13)
        self.Database_name.setObjectName(u"Database_name")
        self.Database_name.setGeometry(QRect(20, 60, 211, 31))
        self.Database_name.setStyleSheet(u"background-color: rgb(207, 219, 255);\n"
"color: rgb(182, 60, 182);\n"
"font: 12pt \"Century Gothic\";")
        self.frame_15 = QFrame(self.frame_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(10, 197, 324, 157))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.label_117 = QLabel(self.frame_15)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setGeometry(QRect(40, 60, 231, 31))
        self.label_117.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 16pt \"Century Gothic\";")
        self.frame_16 = QFrame(self.frame_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(10, 360, 324, 157))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 550))
        self.frame_8.setMaximumSize(QSize(16777215, 550))
        self.frame_8.setStyleSheet(u"background-color: none;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_8)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.Database_config)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.Database_config)
        self.database = QWidget()
        self.database.setObjectName(u"database")
        self.horizontalLayout_4 = QHBoxLayout(self.database)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_2 = QFrame(self.database)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_26 = QFrame(self.frame_2)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(0, 80))
        self.frame_26.setMaximumSize(QSize(16777215, 80))
        self.frame_26.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(218, 218, 218);\n"
"}\n"
"QPushButton{\n"
"	padding: 10px 10px;\n"
"	font: 10pt;\n"
"	border: none;\n"
"	border-left: 2px solid transparent;\n"
"	border-bottom: 2px solid transparent;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(68, 68, 102);\n"
"	color: rgb(140, 140, 140);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 92, 157);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:  rgb(0, 92, 157);\n"
"	border-bottom: 2px solid rgb(255, 165, 24);\n"
"}")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.frame_26)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.label_126 = QLabel(self.frame_26)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMinimumSize(QSize(200, 30))
        self.label_126.setMaximumSize(QSize(200, 30))
        self.label_126.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 16pt \"Century Gothic\";")

        self.horizontalLayout_6.addWidget(self.label_126)

        self.cnit = QLineEdit(self.frame_26)
        self.cnit.setObjectName(u"cnit")
        self.cnit.setMinimumSize(QSize(290, 40))
        self.cnit.setMaximumSize(QSize(290, 40))
        self.cnit.setStyleSheet(u"background-color: rgb(207, 219, 255);\n"
"color: rgb(182, 60, 182);\n"
"font: 10pt \"Century Gothic\";")

        self.horizontalLayout_6.addWidget(self.cnit)

        self.search_cnit = QPushButton(self.frame_26)
        self.search_cnit.setObjectName(u"search_cnit")
        self.search_cnit.setMinimumSize(QSize(160, 40))
        self.search_cnit.setMaximumSize(QSize(160, 40))

        self.horizontalLayout_6.addWidget(self.search_cnit)


        self.verticalLayout_4.addWidget(self.frame_26)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_17 = QFrame(self.frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(680, 0))
        self.frame_17.setMaximumSize(QSize(680, 16777215))
        self.frame_17.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(218, 218, 218);\n"
"}\n"
"QPushButton{\n"
"	padding: 10px 10px;\n"
"	font: 10pt;\n"
"	border: none;\n"
"	border-left: 2px solid transparent;\n"
"	border-bottom: 2px solid transparent;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(68, 68, 102);\n"
"	color: rgb(140, 140, 140);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 92, 157);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:  rgb(0, 92, 157);\n"
"	border-bottom: 2px solid rgb(255, 165, 24);\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.comb_designation_com = QComboBox(self.frame_17)
        self.comb_designation_com.setObjectName(u"comb_designation_com")
        self.comb_designation_com.setGeometry(QRect(380, 190, 291, 41))
        self.comb_designation_com.setStyleSheet(u"background-color: rgb(207, 219, 255);\n"
"color: rgb(182, 60, 182);\n"
"font: 10pt \"Century Gothic\";")
        self.label_125 = QLabel(self.frame_17)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setGeometry(QRect(20, 190, 351, 31))
        self.label_125.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 16pt \"Century Gothic\";")
        self.comb_modele_com = QComboBox(self.frame_17)
        self.comb_modele_com.setObjectName(u"comb_modele_com")
        self.comb_modele_com.setGeometry(QRect(380, 120, 291, 41))
        self.comb_modele_com.setStyleSheet(u"background-color: rgb(207, 219, 255);\n"
"color: rgb(182, 60, 182);\n"
"font: 10pt \"Century Gothic\";")
        self.label_127 = QLabel(self.frame_17)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setGeometry(QRect(20, 110, 301, 31))
        self.label_127.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 16pt \"Century Gothic\";")
        self.comb_marque = QComboBox(self.frame_17)
        self.comb_marque.setObjectName(u"comb_marque")
        self.comb_marque.setGeometry(QRect(380, 40, 291, 41))
        self.comb_marque.setStyleSheet(u"background-color: rgb(207, 219, 255);\n"
"color: rgb(182, 60, 182);\n"
"font: 10pt \"Century Gothic\";")
        self.label_128 = QLabel(self.frame_17)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setGeometry(QRect(20, 40, 201, 31))
        self.label_128.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 16pt \"Century Gothic\";")
        self.search_marque = QPushButton(self.frame_17)
        self.search_marque.setObjectName(u"search_marque")
        self.search_marque.setGeometry(QRect(500, 280, 160, 40))
        self.search_marque.setMinimumSize(QSize(160, 40))
        self.search_marque.setMaximumSize(QSize(160, 40))

        self.horizontalLayout_5.addWidget(self.frame_17)

        self.tableWidget = QTableWidget(self.frame)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_5.addWidget(self.tableWidget)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_29 = QFrame(self.frame_2)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 60))
        self.frame_29.setMaximumSize(QSize(16777215, 60))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_29)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.database)
        self.Connect_server = QWidget()
        self.Connect_server.setObjectName(u"Connect_server")
        self.verticalLayout_2 = QVBoxLayout(self.Connect_server)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_28 = QFrame(self.Connect_server)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_28)

        self.frame_18 = QFrame(self.Connect_server)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 600))
        self.frame_18.setMaximumSize(QSize(16777215, 600))
        self.frame_18.setStyleSheet(u"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 550))
        self.frame_19.setMaximumSize(QSize(16777215, 550))
        self.frame_19.setStyleSheet(u"background-color: none;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(680, 550))
        self.frame_20.setMaximumSize(QSize(680, 550))
        self.frame_20.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(218, 218, 218);\n"
"}\n"
"QPushButton{\n"
"	padding: 20px 10px;\n"
"	border: none;\n"
"	border-left: 2px solid transparent;\n"
"	border-bottom: 2px solid transparent;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(68, 68, 102);\n"
"	color: rgb(140, 140, 140);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 92, 157);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:  rgb(0, 92, 157);\n"
"	border-bottom: 2px solid rgb(255, 165, 24);\n"
"}")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_20)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 34, 653, 157))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(340, 360, 323, 157))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.connect_server = QPushButton(self.frame_21)
        self.connect_server.setObjectName(u"connect_server")
        self.connect_server.setGeometry(QRect(150, 30, 111, 29))
        self.cancel_server = QPushButton(self.frame_21)
        self.cancel_server.setObjectName(u"cancel_server")
        self.cancel_server.setGeometry(QRect(20, 30, 111, 31))
        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(340, 197, 323, 157))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.User = QLineEdit(self.frame_22)
        self.User.setObjectName(u"User")
        self.User.setGeometry(QRect(20, 60, 211, 31))
        self.User.setStyleSheet(u"background-color: rgb(207, 219, 255);\n"
"color: rgb(182, 60, 182);\n"
"font: 12pt \"Century Gothic\";")
        self.Host = QLineEdit(self.frame_22)
        self.Host.setObjectName(u"Host")
        self.Host.setGeometry(QRect(20, 10, 211, 31))
        self.Host.setStyleSheet(u"background-color: rgb(207, 219, 255);\n"
"color: rgb(182, 60, 182);\n"
"font: 12pt \"Century Gothic\";")
        self.Password = QLineEdit(self.frame_22)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(20, 110, 211, 31))
        self.Password.setStyleSheet(u"background-color: rgb(207, 219, 255);\n"
"color: rgb(182, 60, 182);\n"
"font: 12pt \"Century Gothic\";")
        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(10, 197, 324, 157))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.label_118 = QLabel(self.frame_23)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setGeometry(QRect(40, 100, 171, 31))
        self.label_118.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 16pt \"Century Gothic\";")
        self.label_121 = QLabel(self.frame_23)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setGeometry(QRect(40, 10, 171, 31))
        self.label_121.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 16pt \"Century Gothic\";")
        self.label_122 = QLabel(self.frame_23)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setGeometry(QRect(40, 60, 171, 31))
        self.label_122.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 16pt \"Century Gothic\";")
        self.frame_24 = QFrame(self.frame_20)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(10, 360, 324, 157))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_20)

        self.frame_25 = QFrame(self.frame_18)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 550))
        self.frame_25.setMaximumSize(QSize(16777215, 550))
        font1 = QFont()
        font1.setFamily(u"Microsoft Yi Baiti")
        self.frame_25.setFont(font1)
        self.frame_25.setStyleSheet(u"background-color: none;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_25)


        self.verticalLayout_2.addWidget(self.frame_18)

        self.frame_27 = QFrame(self.Connect_server)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_27)

        self.stackedWidget.addWidget(self.Connect_server)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"                       Bienvenu sur la base de donn\u00e9es \u00e9mmisions CO2 Voiture immatr\u00e9cul\u00e9es en france ", None))
#if QT_CONFIG(whatsthis)
        self.minimizeButton.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.minimizeButton.setText("")
        self.closeButton.setText("")
        self.restoreButton.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Database Configuration", None))
        self.valid_config.setText(QCoreApplication.translate("MainWindow", u"Validation", None))
        self.cancel_config.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Database name", None))
        self.label.setText("")
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"CNIT", None))
        self.cnit.setText("")
        self.search_cnit.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"Designation Commerciale", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"Modele Commercial", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"Marque", None))
        self.search_marque.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Connect to MySQL server", None))
        self.connect_server.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.cancel_server.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.Host.setText("")
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Host", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"User", None))
    # retranslateUi


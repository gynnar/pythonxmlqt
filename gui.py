# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'xml.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from channelList import channelList


class Ui_Dialog(object):

    def __init__(self):

        self.cl = channelList()

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(548, 443)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 40, 481, 381))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.urlLineEdit = QLineEdit(self.widget)
        self.urlLineEdit.setObjectName(u"urlLineEdit")
        self.urlLineEdit.setText("http://api.sr.se/api/v2/channels/")

        self.verticalLayout.addWidget(self.urlLineEdit)

        self.loadButton = QPushButton(self.widget)
        self.loadButton.setObjectName(u"loadButton")

        self.verticalLayout.addWidget(self.loadButton)

        self.loadButton.clicked.connect(lambda: self.buttonClicked())

        self.listWidget = QListWidget(self.widget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)
        self.listWidget.itemClicked.connect(lambda: self.itemSelected())

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Url", None))
        self.loadButton.setText(QCoreApplication.translate("Dialog", u"Ladda XML", None))
    # retranslateUi

    def buttonClicked(self):
        print('Klickade knapp!')
    #    cl = channelList()
        self.cl.fetchXmlData()

        for channel in self.cl.ch_list:
#            print(channel.name)
            self.listWidget.addItem(channel.name)

    def itemSelected(self):
        index = self.listWidget.currentIndex().row()
        print(index)
        print(self.cl.ch_list[index].name)

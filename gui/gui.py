# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'USBtest.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_USBtest(object):
    def setupUi(self, USBtest):
        if not USBtest.objectName():
            USBtest.setObjectName(u"USBtest")
        USBtest.resize(746, 584)
        self.label3 = QLabel(USBtest)
        self.label3.setObjectName(u"label3")
        self.label3.setGeometry(QRect(480, 100, 54, 12))
        self.label_2 = QLabel(USBtest)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 40, 101, 16))
        self.label_3 = QLabel(USBtest)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(450, 40, 81, 20))
        self.filename = QTextEdit(USBtest)
        self.filename.setObjectName(u"filename")
        self.filename.setGeometry(QRect(150, 150, 251, 31))
        self.user = QTextEdit(USBtest)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(150, 90, 111, 31))
        self.passwd = QTextEdit(USBtest)
        self.passwd.setObjectName(u"passwd")
        self.passwd.setGeometry(QRect(540, 90, 111, 31))
        self.run = QPushButton(USBtest)
        self.run.setObjectName(u"run")
        self.run.setGeometry(QRect(230, 460, 75, 23))
        self.label_5 = QLabel(USBtest)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(400, 160, 291, 16))
        self.label = QLabel(USBtest)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 150, 71, 16))
        self.remotopath = QTextEdit(USBtest)
        self.remotopath.setObjectName(u"remotopath")
        self.remotopath.setGeometry(QRect(150, 200, 251, 31))
        self.ftpip = QTextEdit(USBtest)
        self.ftpip.setObjectName(u"ftpip")
        self.ftpip.setGeometry(QRect(150, 270, 251, 31))
        self.label2 = QLabel(USBtest)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(60, 100, 61, 16))
        self.label_4 = QLabel(USBtest)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 210, 91, 16))
        self.lable1 = QLabel(USBtest)
        self.lable1.setObjectName(u"lable1")
        self.lable1.setGeometry(QRect(60, 280, 91, 16))
        self.serType = QComboBox(USBtest)
        self.serType.addItem("")
        self.serType.addItem("")
        self.serType.setObjectName(u"serType")
        self.serType.setGeometry(QRect(150, 40, 111, 22))
        self.direction = QComboBox(USBtest)
        self.direction.addItem("")
        self.direction.addItem("")
        self.direction.setObjectName(u"direction")
        self.direction.setGeometry(QRect(540, 40, 91, 22))
        self.label_6 = QLabel(USBtest)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(480, 280, 54, 12))
        self.times = QTextEdit(USBtest)
        self.times.setObjectName(u"times")
        self.times.setGeometry(QRect(550, 270, 104, 31))
        self.label_7 = QLabel(USBtest)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 360, 54, 12))
        self.status = QTextEdit(USBtest)
        self.status.setObjectName(u"status")
        self.status.setGeometry(QRect(130, 350, 521, 41))
        self.stop = QPushButton(USBtest)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(450, 460, 75, 23))
        self.label_8 = QLabel(USBtest)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(400, 210, 251, 16))

        self.retranslateUi(USBtest)

        QMetaObject.connectSlotsByName(USBtest)
    # setupUi

    def retranslateUi(self, USBtest):
        USBtest.setWindowTitle(QCoreApplication.translate("USBtest", u"USB\u7a33\u5b9a\u6027\u6d4b\u8bd5", None))
        self.label3.setText(QCoreApplication.translate("USBtest", u"\u5bc6\u7801\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("USBtest", u"USB\u670d\u52a1\u5668\u7c7b\u578b:", None))
        self.label_3.setText(QCoreApplication.translate("USBtest", u"\u6587\u4ef6\u4f20\u8f93\u65b9\u5411\uff1a", None))
        self.user.setHtml(QCoreApplication.translate("USBtest", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">admin</p></body></html>", None))
        self.passwd.setHtml(QCoreApplication.translate("USBtest", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">admin</p></body></html>", None))
        self.run.setText(QCoreApplication.translate("USBtest", u"\u8fd0\u884c", None))
        self.label_5.setText(QCoreApplication.translate("USBtest", u"\uff08\u9700\u8981\u52a0\u6587\u4ef6\u7684\u7edd\u5bf9\u8def\u5f84/\u5f53\u524d\u76ee\u5f55\u76f4\u63a5\u5199\u6587\u4ef6\u540d\uff09", None))
        self.label.setText(QCoreApplication.translate("USBtest", u"\u62f7\u8d1d\u6587\u4ef6\u540d\uff1a", None))
        self.ftpip.setHtml(QCoreApplication.translate("USBtest", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">192.168.0.1</p></body></html>", None))
        self.label2.setText(QCoreApplication.translate("USBtest", u"\u8d26\u53f7\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("USBtest", u"\u670d\u52a1\u5668\u6587\u4ef6\u76ee\u5f55\uff1a", None))
        self.lable1.setText(QCoreApplication.translate("USBtest", u"\u670d\u52a1\u5668\u5730\u5740:", None))
        self.serType.setItemText(0, QCoreApplication.translate("USBtest", u"FTPSer", None))
        self.serType.setItemText(1, QCoreApplication.translate("USBtest", u"SambaSer", None))

        self.direction.setItemText(0, QCoreApplication.translate("USBtest", u"\u4e0a\u4f20", None))
        self.direction.setItemText(1, QCoreApplication.translate("USBtest", u"\u4e0b\u8f7d", None))

        self.label_6.setText(QCoreApplication.translate("USBtest", u"\u62f7\u8d1d\u6b21\u6570\uff1a", None))
        self.times.setHtml(QCoreApplication.translate("USBtest", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">100</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("USBtest", u"\u8fd0\u884c\u72b6\u6001\uff1a", None))
        self.status.setHtml(QCoreApplication.translate("USBtest", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u672a\u5f00\u59cb\u8fd0\u884c\uff01</p></body></html>", None))
        self.stop.setText(QCoreApplication.translate("USBtest", u"\u505c\u6b62", None))
        self.label_8.setText(QCoreApplication.translate("USBtest", u"\uff08USB\u670d\u52a1\u5668\u7684\u5171\u4eab\u7a7a\u95f4\u76ee\u5f55\u7684\u7edd\u5bf9\u8def\u5f84\uff09", None))
    # retranslateUi


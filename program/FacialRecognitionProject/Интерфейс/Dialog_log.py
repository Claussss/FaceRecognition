# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_Dialog_log.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(292, 522)
        Form.setMinimumSize(QtCore.QSize(292, 522))
        Form.setMaximumSize(QtCore.QSize(292, 522))
        Form.setStyleSheet("\n"
"QPushButton{\n"
"border-style:solid;\n"
"color:#fff;\n"
"border-radius:10px;\n"
"background-color:#3d3d3d;\n"
"font: 11pt \"Century Gothic\";\n"
"}\n"
"\n"
"QLabel{\n"
"color:#2d89ef;\n"
"qproperty-alignment: AlignLeft;\n"
"}\n"
"QDialogButtonBox{\n"
"color:#2d89ef;\n"
"}\n"
"\n"
"QWidget{\n"
"background-color:#3d3d3d;\n"
"}\n"
"QTextBrowser{\n"
"color:#fff;\n"
"background-color:#1d1d1d;\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.txtB_log = QtWidgets.QTextBrowser(Form)
        self.txtB_log.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txtB_log.setAutoFillBackground(False)
        self.txtB_log.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.txtB_log.setFrameShadow(QtWidgets.QFrame.Plain)
        self.txtB_log.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtB_log.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtB_log.setObjectName("txtB_log")
        self.verticalLayout.addWidget(self.txtB_log)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Face Recognize"))
        self.label.setText(_translate("Form", "Журнал статистик"))
        self.txtB_log.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


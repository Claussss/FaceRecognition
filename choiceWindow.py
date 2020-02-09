# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choiceWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_main(object):
    def setupUi(self, Form_main):
        Form_main.setObjectName("Form_main")
        Form_main.resize(271, 212)
        Form_main.setMinimumSize(QtCore.QSize(271, 212))
        Form_main.setMaximumSize(QtCore.QSize(271, 212))
        Form_main.setStyleSheet("\n"
"\n"
"QTabWidget::tab{\n"
"background-color:#3d3d3d;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius:7;\n"
"}\n"
"\n"
"\n"
"QMessageBox{\n"
"background-color:#1d1d1d;\n"
"color:#fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"color:#2d89ef;\n"
"qproperty-alignment: AlignLeft;\n"
"\n"
"\n"
"}\n"
"\n"
"QDialogButtonBox{\n"
"color:#2d89ef;\n"
"}\n"
"QTextBrowser{\n"
"color:#2d89ef;\n"
"background-color:#1d1d1d;\n"
"}\n"
"\n"
"\n"
"QWidget{\n"
"background-color:#1d1d1d;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"border-style:solid;\n"
"color:#fff;\n"
"border-radius:10px;\n"
"background-color:#3d3d3d;\n"
"font: 11pt \"Century Gothic\";\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color:#ccc;\n"
"    background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.517, y2:1, stop:0 rgba(45, 45, 45, 255), stop:0.505682 rgba(45, 45, 45, 255), stop:1 rgba(29, 29, 29, 255));\n"
"    border-color:#2d89ef;\n"
"border-width:2px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.517, y2:1, stop:0 rgba(29, 29, 29, 255), stop:0.505682 rgba(45, 45, 45, 255), stop:1 rgba(29, 29, 29, 255));\n"
"}\n"
"\n"
"QInputDialog{\n"
"background-color:#1d1d1d;\n"
"color:#fff;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius:7;\n"
"background-color:#fff;\n"
"}\n"
"")
        self.pb_open = QtWidgets.QPushButton(Form_main)
        self.pb_open.setGeometry(QtCore.QRect(10, 10, 121, 91))
        self.pb_open.setToolTipDuration(-1)
        self.pb_open.setText("")
        icon = QtGui.QIcon.fromTheme("C:\\\\Users\\\\1\\\\FacialRecognitionProject\\\\Интерфейс\\\\иконки\\\\лицо_иконка.png")
        self.pb_open.setIcon(icon)
        self.pb_open.setIconSize(QtCore.QSize(50, 50))
        self.pb_open.setAutoRepeat(False)
        self.pb_open.setFlat(False)
        self.pb_open.setObjectName("pb_open")
        self.pb_add = QtWidgets.QPushButton(Form_main)
        self.pb_add.setGeometry(QtCore.QRect(10, 110, 121, 91))
        self.pb_add.setText("")
        self.pb_add.setObjectName("pb_add")
        self.pb_rename = QtWidgets.QPushButton(Form_main)
        self.pb_rename.setGeometry(QtCore.QRect(140, 110, 121, 91))
        self.pb_rename.setText("")
        self.pb_rename.setObjectName("pb_rename")
        self.pb_delete = QtWidgets.QPushButton(Form_main)
        self.pb_delete.setGeometry(QtCore.QRect(140, 10, 121, 91))
        self.pb_delete.setText("")
        self.pb_delete.setObjectName("pb_delete")

        self.retranslateUi(Form_main)
        QtCore.QMetaObject.connectSlotsByName(Form_main)

    def retranslateUi(self, Form_main):
        _translate = QtCore.QCoreApplication.translate
        Form_main.setWindowTitle(_translate("Form_main", "Form"))
        self.pb_open.setToolTip(_translate("Form_main", "Відкрити навчальну базу"))
        self.pb_add.setToolTip(_translate("Form_main", "Додати людину в  навчальну базу"))
        self.pb_rename.setToolTip(_translate("Form_main", "Змінити ім\'я людини в  навчальній базі"))
        self.pb_delete.setToolTip(_translate("Form_main", "Видалити людину з  навчальної бази"))


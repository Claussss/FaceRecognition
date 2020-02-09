# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'last_Main_window_after.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(292, 321)
        MainWindow.setMinimumSize(QtCore.QSize(292, 321))
        MainWindow.setMaximumSize(QtCore.QSize(292, 321))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-color:#1d1d1d;\n"
"color:#fff;\n"
"}\n"
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
"\n"
"QTabWidget::tab{\n"
"background-color:#3d3d3d;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius:7;\n"
"}\n"
"\n"
"QProgressBar{\n"
"border-radius:0;\n"
"text-align:center;\n"
"color:#fff;\n"
"background-color:transparent;\n"
"border: 2px solid #2d89ef;\n"
"border-radius:7px;\n"
"    font: 75 12pt \"Open Sans\";\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"background-color:#2d89ef;\n"
"width:20px;\n"
"}\n"
"QMessageBox{\n"
"background-color:#1d1d1d;\n"
"color:#fff;\n"
"\n"
"}\n"
"QInputDialog{\n"
"background-color:#1d1d1d;\n"
"color:#fff;\n"
"}\n"
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
"")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PB_start = QtWidgets.QPushButton(self.centralwidget)
        self.PB_start.setGeometry(QtCore.QRect(10, 10, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PB_start.setFont(font)
        self.PB_start.setAutoFillBackground(False)
        self.PB_start.setStyleSheet("")
        self.PB_start.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        icon = QtGui.QIcon.fromTheme("ff")
        self.PB_start.setIcon(icon)
        self.PB_start.setAutoDefault(False)
        self.PB_start.setDefault(False)
        self.PB_start.setFlat(False)
        self.PB_start.setObjectName("PB_start")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 70, 271, 20))
        self.line.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.PB_all_bd = QtWidgets.QPushButton(self.centralwidget)
        self.PB_all_bd.setGeometry(QtCore.QRect(10, 90, 271, 61))
        self.PB_all_bd.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.PB_all_bd.setObjectName("PB_all_bd")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 230, 271, 20))
        self.line_2.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.PB_exit = QtWidgets.QPushButton(self.centralwidget)
        self.PB_exit.setGeometry(QtCore.QRect(10, 250, 271, 61))
        self.PB_exit.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.PB_exit.setObjectName("PB_exit")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 150, 271, 20))
        self.line_3.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.PB_log = QtWidgets.QPushButton(self.centralwidget)
        self.PB_log.setGeometry(QtCore.QRect(10, 170, 271, 61))
        self.PB_log.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PB_log.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.PB_log.setObjectName("PB_log")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.PB_start, self.PB_all_bd)
        MainWindow.setTabOrder(self.PB_all_bd, self.PB_log)
        MainWindow.setTabOrder(self.PB_log, self.PB_exit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Face Recognition"))
        self.PB_start.setText(_translate("MainWindow", "Розпізнати обличчя"))
        self.PB_all_bd.setText(_translate("MainWindow", "Навчальна база"))
        self.PB_exit.setText(_translate("MainWindow", "Вихід"))
        self.PB_log.setText(_translate("MainWindow", "Журнал"))


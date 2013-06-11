"""
Author : tharindra galahena (inf0_warri0r)
Project: fsm simulater
Blog   : http://www.inf0warri0r.blogspot.com
Date   : 03/06/2013
License:

     Copyright 2013 Tharindra Galahena

This is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. This is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

* You should have received a copy of the GNU General Public License along with
this. If not, see http://www.gnu.org/licenses/.

"""

# Form implementation generated from reading ui file 'fsm_ui.ui'
#
# Created: Sun Jun  2 18:20:43 2013
#      by: pyside-uic 0.2.8 running on PySide 1.0.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(771, 643)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 241))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 67, 31))
        self.definitions = QtGui.QTextEdit(self.centralwidget)
        self.definitions.setGeometry(QtCore.QRect(120, 40, 261, 211))
        self.definitions.setObjectName("definitions")
        self.state_view = QtGui.QGraphicsView(self.centralwidget)
        self.state_view.setGeometry(QtCore.QRect(30, 300, 711, 281))
        self.state_view.setObjectName("state_view")
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(420, 10, 331, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 81, 31))
        self.label_3.setObjectName("label_3")
        self.test = QtGui.QPushButton(self.groupBox_2)
        self.test.setGeometry(QtCore.QRect(0, 60, 321, 27))
        self.test.setObjectName("test")
        self.test_string = QtGui.QLineEdit(self.groupBox_2)
        self.test_string.setGeometry(QtCore.QRect(120, 30, 201, 25))
        self.test_string.setObjectName("test_string")
        self.generate = QtGui.QPushButton(self.centralwidget)
        self.generate.setGeometry(QtCore.QRect(30, 260, 351, 27))
        self.generate.setObjectName("generate")
        self.reset = QtGui.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(420, 260, 321, 27))
        self.reset.setObjectName("reset")
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(420, 100, 331, 151))
        self.groupBox_3.setObjectName("groupBox_3")
        self.test_char = QtGui.QLineEdit(self.groupBox_3)
        self.test_char.setGeometry(QtCore.QRect(120, 30, 121, 31))
        self.test_char.setObjectName("test_char")
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 67, 17))
        self.label_4.setObjectName("label_4")
        self.current_st = QtGui.QLineEdit(self.groupBox_3)
        self.current_st.setGeometry(QtCore.QRect(120, 70, 201, 31))
        self.current_st.setObjectName("current_st")
        self.current_str = QtGui.QLineEdit(self.groupBox_3)
        self.current_str.setGeometry(QtCore.QRect(120, 110, 201, 31))
        self.current_str.setObjectName("current_str")
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 111, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 111, 41))
        self.label_6.setObjectName("label_6")
        self.go = QtGui.QPushButton(self.groupBox_3)
        self.go.setGeometry(QtCore.QRect(250, 30, 71, 31))
        self.go.setObjectName("go")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 771, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "FSM - Simulater", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Input:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Definitions", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Testing - Compleate String ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Test String", None, QtGui.QApplication.UnicodeUTF8))
        self.test.setText(QtGui.QApplication.translate("MainWindow", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.generate.setText(QtGui.QApplication.translate("MainWindow", "Generate", None, QtGui.QApplication.UnicodeUTF8))
        self.reset.setText(QtGui.QApplication.translate("MainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Testing - Character by Character", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Char", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Current State", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Current String", None, QtGui.QApplication.UnicodeUTF8))
        self.go.setText(QtGui.QApplication.translate("MainWindow", "Go", None, QtGui.QApplication.UnicodeUTF8))


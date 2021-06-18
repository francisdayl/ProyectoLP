# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Proyecto_LP2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 350)
        MainWindow.setMinimumSize(QtCore.QSize(450, 350))
        MainWindow.setMaximumSize(QtCore.QSize(1050, 950))
        MainWindow.setStyleSheet("background-color:rgb(28, 105, 157);\n"
"color:white;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Label_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Label_title.setFont(font)
        self.Label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_title.setObjectName("Label_title")
        self.gridLayout.addWidget(self.Label_title, 0, 0, 1, 2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color:white;\n"
"color: black;")
        self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 2, 1)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.ListWidget = QtWidgets.QListWidget(self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.ListWidget.setFont(font)
        self.ListWidget.setStyleSheet("background-color:rgb(221, 221, 221);\n"
"color: black;")
        self.ListWidget.setObjectName("ListWidget")
        self.gridLayout.addWidget(self.ListWidget, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.analiza)

        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Proyecto - Samira Suárez|David Yánez"))
        self.Label_title.setText(_translate("MainWindow", "Analizador Sintáctico"))
        self.pushButton.setText(_translate("MainWindow", "Analizar"))

    def analiza(self):
        self.ListWidget.clear()
        self.ListWidget.setStyleSheet("background-color:rgb(221, 221, 221);color: red;")
        self.ListWidget.addItems(["Error de Compilacion","Se esperaba un ; al final de la línea 4"])


        #4

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
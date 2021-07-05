from PyQt5 import QtCore, QtGui, QtWidgets
import funciones_sintact as pr
import time
import random as rd

class Sintactico(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(634, 208)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(400, 175))
        self.setMaximumSize(QtCore.QSize(800, 373))
        self.setStyleSheet("background-color:rgb(28, 105, 157);\n"
"color:white;\n"
"")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Label_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Label_title.setFont(font)
        self.Label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_title.setObjectName("Label_title")
        self.verticalLayout.addWidget(self.Label_title)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Text_Sem = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Text_Sem.sizePolicy().hasHeightForWidth())
        self.Text_Sem.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Text_Sem.setFont(font)
        self.Text_Sem.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Text_Sem.setStyleSheet("background-color:white;\n"
"color: black;")
        self.Text_Sem.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Text_Sem.setObjectName("Text_Sem")
        self.horizontalLayout.addWidget(self.Text_Sem)
        self.Button_Analizar = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Analizar.sizePolicy().hasHeightForWidth())
        self.Button_Analizar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_Analizar.setFont(font)
        self.Button_Analizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_Analizar.setObjectName("Button_Analizar")
        self.horizontalLayout.addWidget(self.Button_Analizar)
        self.Button_Demo = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Demo.sizePolicy().hasHeightForWidth())
        self.Button_Demo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_Demo.setFont(font)
        self.Button_Demo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_Demo.setObjectName("Button_Demo")
        self.horizontalLayout.addWidget(self.Button_Demo)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.ListWidget = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ListWidget.setFont(font)
        self.ListWidget.setStyleSheet("background-color:rgb(221, 221, 221);\n"
"color: black;")
        self.ListWidget.setObjectName("ListWidget")
        self.verticalLayout.addWidget(self.ListWidget)
        self.Button_Regresar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Button_Regresar.setFont(font)
        self.Button_Regresar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_Regresar.setObjectName("Button_Regresar")
        self.verticalLayout.addWidget(self.Button_Regresar)
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        #self.Button_Regresar.clicked.connect(lambda: self.close())
        self.Button_Regresar.clicked.connect(self.close)
        self.Button_Analizar.clicked.connect(self.analizar)
        self.Button_Demo.clicked.connect(self.demostrar)

        self.ejemplos = ["a = 32","int _num = 32;","bool comp = 32>12;","if(a==b){a++;}","while(cont>0){if(cont==0){--cont;}}",
        "for(int i=0;i<n;i++){suma++;}"]

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Proyecto - Samira Suárez|David Yánez"))
        self.Label_title.setText(_translate("self", "Analizador Sintáctico"))
        self.Text_Sem.setPlaceholderText(_translate("self", "Ingrese Sentencia"))
        self.Button_Analizar.setText(_translate("self", "Analizar"))
        self.Button_Analizar.setShortcut(_translate("self", "Return"))
        self.Button_Demo.setText(_translate("self", "Ejecutar Demo"))
        self.Button_Regresar.setText(_translate("self", "Regresar"))

    def analizar(self):
        self.ListWidget.clear()
        if len(self.Text_Sem.toPlainText().strip())>0:
            result = pr.parser.parse(self.Text_Sem.toPlainText())
            if result is not None:
                if type(result) == list:
                    self.ListWidget.addItem(result[0])
                else:
                    self.ListWidget.addItem(result)
            else:
                self.ListWidget.addItem("Sintaxis invalida e irreconocible")

    def demostrar(self):
        if len(self.ejemplos)>0:
            ejemplo = rd.choice(self.ejemplos)
            self.ejemplos.remove(ejemplo)
            self.Text_Sem.setPlainText(ejemplo)
            self.Button_Analizar.click()

    def closeEvent(self,event):
        self.Text_Sem.clear()
        self.ListWidget.clear()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window=Sintactico()
    window.show()
    app.exec_()



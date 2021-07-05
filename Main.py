from PyQt5 import QtCore, QtGui, QtWidgets
import Sintactico as st
import Lexico as lx
import Semantico as smt

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400, 115)
        self.setMinimumSize(QtCore.QSize(400, 115))
        self.setMaximumSize(QtCore.QSize(1050, 950))
        self.setStyleSheet("background-color:rgb(28, 105, 157);\n"
"color:white;\n"
"")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 54, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Button_Lex = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_Lex.setFont(font)
        self.Button_Lex.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_Lex.setObjectName("Button_Lex")
        self.horizontalLayout.addWidget(self.Button_Lex)
        self.Button_Sint = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_Sint.setFont(font)
        self.Button_Sint.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_Sint.setObjectName("Button_Sint")
        self.horizontalLayout.addWidget(self.Button_Sint)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.Button_semant = QtWidgets.QPushButton()
        self.Button_semant.setFont(font)
        self.Button_semant.setText("Analizador Semántico")
        self.Button_semant.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verticalLayout.addWidget(self.Button_semant)

        
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        
        self.Button_Lex.clicked.connect(self.show_lex)
        self.Button_Sint.clicked.connect(self.show_sint)
        self.Button_semant.clicked.connect(self.show_sem)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Proyecto - Samira Suárez|David Yánez"))
        self.label.setText(_translate("self", "Proyecto Lenguajes de Programación: C#"))
        self.Button_Lex.setText(_translate("self", "Analizador Léxico"))
        self.Button_Sint.setText(_translate("self", "Analizador Sintáctico"))

    def show_sem(self):
        Semant.show()

    def show_lex(self):
        if not Sintact.isHidden():
            Sintact.close()
        if not Semant.isHidden():
            Semant.close()
        Lexi.show()

    def show_sint(self):
        if not Lexi.isHidden():
            Lexi.close()
        if not Semant.isHidden():
            Semant.close()
        Sintact.show()

    def closeEvent(self,event):
        if not Lexi.isHidden():
            Lexi.close()
        if not Sintact.isHidden():
            Sintact.close()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = Main()
    Lexi = lx.Lexico()
    Sintact = st.Sintactico()
    Semant = smt.Semantico()

    Principal.show()
    sys.exit(app.exec_())

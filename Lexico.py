

from PyQt5 import QtCore, QtGui, QtWidgets
import ply.lex as lex
import funciones as fc



class Lexico(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(450, 350)
        self.setMinimumSize(QtCore.QSize(450, 350))
        self.setMaximumSize(QtCore.QSize(1050, 950))
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
        self.Text_ent = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Text_ent.setStyleSheet("background-color:white;\n"
"color: black;")
        self.Text_ent.setObjectName("Text_ent")
        font.setPointSize(12)
        font.setBold(False)
        self.Text_ent.setFont(font)
        self.horizontalLayout.addWidget(self.Text_ent)
        self.Boton_analizar = QtWidgets.QPushButton(self.centralwidget)
        self.Boton_analizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Boton_analizar.setObjectName("Boton_analizar")
        self.horizontalLayout.addWidget(self.Boton_analizar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.ListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.ListWidget.setStyleSheet("background-color:white;\n"
"color: black;")
        self.ListWidget.setObjectName("ListWidget")
        self.verticalLayout.addWidget(self.ListWidget)

        self.Button_Regresar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Button_Regresar.setFont(font)
        self.Button_Regresar.setText("Regresar")
        self.Button_Regresar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_Regresar.setObjectName("Button_Regresar")
        self.verticalLayout.addWidget(self.Button_Regresar)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName(self)

        self.verticalLayout.setStretch(0,1)
        self.verticalLayout.setStretch(1,1)
        self.verticalLayout.setStretch(2,10)
        self.Boton_analizar.clicked.connect(self.analizar)
        self.Button_Regresar.clicked.connect(self.close)
        self.exit = 45


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Proyecto - Samira Suárez|David Yánez"))
        self.Label_title.setText(_translate("self", "Analizador Léxico"))
        self.Boton_analizar.setText(_translate("self", "Analizar"))

    def analizar(self):
        texto = self.Text_ent.toPlainText()
        self.ListWidget.clear()
        lexer = fc.lexer
        lexer.input(texto)
        results = fc.getTokens(lexer)
        self.ListWidget.addItem("Total de tokens: "+str(len(results)))
        for toquen in results:
            desc_token = "Token N°: "+str(toquen[-1]+1)+" | "
            desc_token+= "Token identificado: "+str(toquen[1])+" | "
            desc_token += "Tipo Token: "
            if toquen[0] in fc.reserved:
                desc_token += "Palabra Reservada "
            else:
                desc_token += toquen[0] 
            
            self.ListWidget.addItem(desc_token)
    
    def closeEvent(self,event):
        self.Text_ent.clear()
        self.ListWidget.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = Lexico()
    ventana.show()
    sys.exit(app.exec_())

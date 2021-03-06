from PyQt5 import QtCore, QtGui, QtWidgets
import funciones as fc
import funciones_sint as pr
import random as rd

class Semantico(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(525, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.ejemplos = ["i++;","if(a==b){a++;}","while(5>0){if(2==0){--cont;}}",
        "short var_s= 165165132;","int num=-2.65;",'string cade="Hola Mundo";',"a+3","a>3","3==3"]

        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(500, 250))
        self.setMaximumSize(QtCore.QSize(800, 1000))
        self.setStyleSheet("background-color:rgb(28, 105, 157);\n"
"color:white;\n"
"")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Label_title = QtWidgets.QLabel(self.centralwidget)
        self.Label_title.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Label_title.setFont(font)
        self.Label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_title.setObjectName("Label_title")
        self.verticalLayout.addWidget(self.Label_title)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Text_Sem = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Text_Sem.sizePolicy().hasHeightForWidth())
        self.Text_Sem.setSizePolicy(sizePolicy)
        self.Text_Sem.setMaximumSize(QtCore.QSize(16777215, 130))
        self.Text_Sem.setSizeIncrement(QtCore.QSize(1, 1))
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
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(28, 105, 157))
        gradient.setColorAt(0.0738636, QtGui.QColor(232, 232, 232))
        gradient.setColorAt(0.920455, QtGui.QColor(232, 232, 232))
        gradient.setColorAt(0.977273, QtGui.QColor(28, 105, 157))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(28, 105, 157))
        gradient.setColorAt(0.0738636, QtGui.QColor(232, 232, 232))
        gradient.setColorAt(0.920455, QtGui.QColor(232, 232, 232))
        gradient.setColorAt(0.977273, QtGui.QColor(28, 105, 157))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(28, 105, 157))
        gradient.setColorAt(0.0738636, QtGui.QColor(232, 232, 232))
        gradient.setColorAt(0.920455, QtGui.QColor(232, 232, 232))
        gradient.setColorAt(0.977273, QtGui.QColor(28, 105, 157))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(28, 105, 157))
        gradient.setColorAt(0.0738636, QtGui.QColor(232, 232, 232))
        gradient.setColorAt(0.920455, QtGui.QColor(232, 232, 232))
        gradient.setColorAt(0.977273, QtGui.QColor(28, 105, 157))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(28, 105, 157))
        gradient.setColorAt(0.0738636, QtGui.QColor(232, 232, 232))
        gradient.setColorAt(0.920455, QtGui.QColor(232, 232, 232))
        gradient.setColorAt(0.977273, QtGui.QColor(28, 105, 157))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(28, 105, 157))
        gradient.setColorAt(0.0738636, QtGui.QColor(232, 232, 232))
        gradient.setColorAt(0.920455, QtGui.QColor(232, 232, 232))
        gradient.setColorAt(0.977273, QtGui.QColor(28, 105, 157))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(28, 105, 157))
        gradient.setColorAt(0.0738636, QtGui.QColor(232, 232, 232))
        gradient.setColorAt(0.920455, QtGui.QColor(232, 232, 232))
        gradient.setColorAt(0.977273, QtGui.QColor(28, 105, 157))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(28, 105, 157))
        gradient.setColorAt(0.0738636, QtGui.QColor(232, 232, 232))
        gradient.setColorAt(0.920455, QtGui.QColor(232, 232, 232))
        gradient.setColorAt(0.977273, QtGui.QColor(28, 105, 157))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(28, 105, 157))
        gradient.setColorAt(0.0738636, QtGui.QColor(232, 232, 232))
        gradient.setColorAt(0.920455, QtGui.QColor(232, 232, 232))
        gradient.setColorAt(0.977273, QtGui.QColor(28, 105, 157))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.scrollArea.setPalette(palette)
        self.scrollArea.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(28, 105, 157, 255), stop:0.0738636 rgba(232, 232, 232, 255), stop:0.920455 rgba(232, 232, 232, 255), stop:0.977273 rgba(28, 105, 157, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: black;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 505, 138))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.Form_elementos = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.Form_elementos.setObjectName("Form_elementos")
        self.Grid = QtWidgets.QGridLayout()
        self.Form_elementos.addLayout(self.Grid, 0, 0, 1, 1)

        """self.label_4 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.Grid.addWidget(self.label_4,0,0)
        self.label_3 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.Grid.addWidget(self.label_3,0,1)  """     
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.ListWidget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListWidget.sizePolicy().hasHeightForWidth())
        self.ListWidget.setSizePolicy(sizePolicy)
        self.ListWidget.setMaximumSize(QtCore.QSize(10000, 40))
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
        self.verticalLayout.setStretch(3, 3)
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()

        self.Button_Regresar.clicked.connect(self.close)
        self.Button_Analizar.clicked.connect(self.analizar)
        self.Button_Demo.clicked.connect(self.demo)

        

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Proyecto - Samira Su??rez|David Y??nez"))
        self.Label_title.setText(_translate("self", "Analizador Sem??ntico"))
        self.Text_Sem.setPlaceholderText(_translate("self", "Ingrese Sentencia"))
        self.Button_Analizar.setText(_translate("self", "Analizar"))
        self.Button_Analizar.setShortcut(_translate("self", "Return"))
        self.Button_Demo.setText(_translate("self", "Ejecutar Demo"))
        self.Button_Regresar.setText(_translate("self", "Regresar"))
    
    def cleargrid(self):
        pr.list_sintax.clear()
        self.ListWidget.clear()
        while self.Grid.count():
            child = self.Grid.takeAt(0)                        
            if child.widget():
                child.widget().deleteLater()
        label_4 = QtWidgets.QLabel("Token")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        label_4.setFont(font)
        label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.Grid.addWidget(label_4,0,0)
        label_3 = QtWidgets.QLabel("Sintaxis")
        label_3.setFont(font)
        label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Grid.addWidget(label_3,0,1)

    def analizar(self):
        self.cleargrid()
        texto = self.Text_Sem.toPlainText()
        if len(texto)>0:
            lexer = fc.lexer
            lexer.input(texto)
            results = fc.getTokens(lexer)
            for i in range(len(results)):
                toquen = results[i]
                desc_token = "Token identificado: "+str(toquen[1])+" | "
                desc_token += "Tipo Token: "
                if toquen[0] in fc.reserved:
                    desc_token += "Palabra Reservada "
                else:
                    desc_token += toquen[0] 
                self.Grid.addWidget(QtWidgets.QLabel(desc_token),i+1,0)
            result = pr.parser.parse(self.Text_Sem.toPlainText())
            for i in range(len(pr.list_sintax)):
                self.Grid.addWidget(QtWidgets.QLabel(pr.list_sintax[len(pr.list_sintax)-i-1]),i+1,1)
            if result is not None:
                self.ListWidget.addItem(result)
            else:
                self.ListWidget.addItem("Sintaxis invalida e irreconocible")

    def demo(self):
        if len(self.ejemplos)>0:
            ejemplo = rd.choice(self.ejemplos)
            self.Text_Sem.setPlainText(ejemplo)
            self.ejemplos.remove(ejemplo)
            self.Button_Analizar.click()

    

    def closeEvent(self,event):
        pr.list_sintax.clear()
        self.Text_Sem.clear()
        self.ListWidget.clear()
        self.cleargrid()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Semant = Semantico()
    Semant.show()
    sys.exit(app.exec_())

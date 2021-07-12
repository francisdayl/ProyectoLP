from funciones import tokens, OperandosInvalidosException, CondicionInvalidaException, SemiColonException, TipoDatoException
import ply.yacc as yacc
from PyQt5 import QtWidgets

list_tok = []
list_sintax = []
flag=0

def msj_error(msj):
    boton = QtWidgets.QMessageBox()
    boton.setWindowTitle("Error")
    boton.setIcon(QtWidgets.QMessageBox.Critical)
    boton.setText(msj)
    x = boton.exec_() 

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_expression_aritme(p):
    '''expression : term opmat term
    | term opmat term expression'''
    if (type(p[1])==int or type(p[1])==float) and (type(p[3])==int or type(p[3])==float):
        p[0] = "Expresion aritmética válida"
        list_sintax.append("Expresion aritmética")
    else:
        try:
            raise OperandosInvalidosException
        except OperandosInvalidosException as ex:
            msj_error(ex.mensaje)


#Validacion de  expresiones logicas
def p_expression_logic(p):
    '''expression : expresionlogic
    | expresionlogic connectlog expresionlogic'''
    p[0]= "Operacion Logica Valida"
    list_sintax.append("Operacion Logica")

#Validar que los operandos de expresiones logicas sean del mismo tipo
def p_expresionlogic_rel(p):
    'expresionlogic : term oplog term'
    if (type(p[1])!=type(p[3])):
        try:
            raise CondicionInvalidaException
        except CondicionInvalidaException as ex:
            p[0] = "Operación Lógica inválida"
            msj_error(ex.mensaje)
    else:
        p[0] = "Operación Lógica Válida"



def p_expresionlogic_bool(p):
    'expresionlogic : booleano connectlog booleano'
    p[0] = "Expresion Logica Valida"
    list_sintax.append("Expresion Logica Valida")


def p_booleano_val(p):
    '''booleano : TRUE
    | FALSE'''
    p[0] = p[1]


def p_connectlog(p):
    '''connectlog : AND
    | OR'''
    p[0] = p[1]

def p_oplog(p):
    '''oplog : EQUAL
    | NOTEQUAL
    | GREATERTHAN
    | GREATERTHANEQUAL
    | LESSERTHAN
    | LESSERTHANEQUAL'''
    p[0] = p[1]

def p_opmat(p):
    '''opmat : PLUS
    | MINUS
    | TIMES
    | DIVIDE
    | MOD'''
    p[0] = p[1]

def p_assignacion(p):
    '''assignacion : INCREMENT
    | DECREMENT
    | COMPASSIGPLUS
    | COMPASSIGMINUS
    | COMPASSIGTIMES
    | COMPASSIGDIVIDE'''
    p[0] = p[1]

def p_term(p):
    '''term : NUMBER
    | VARIABLE
    | TEXT
    | NUMDEC'''
    p[0] = p[1]


def p_expression_preop(p):
    'expression : VARIABLE assignacion SEMICOLON'
    p[0] = "Operacion de post-incremento/decremento valida"
    list_sintax.append("Operacion de post-incremento/decremento")

def p_expression_postop(p):
    'expression : assignacion VARIABLE SEMICOLON'
    p[0] = "Operacion de pre-incremento/decremento valida"
    list_sintax.append("Operacion de pre-incremento/decremento")

def p_expression_while(p):
    'expression : WHILE LPAREN expresionlogic RPAREN LBRACKET expression RBRACKET'
    p[0] = "Bucle while valido"
    list_sintax.append("Bucle While")

def p_expression_for(p):
    'expression : FOR LPAREN datos declaracion expresionlogic SEMICOLON oper RPAREN LBRACKET expression RBRACKET'
    p[0] = "Bucle for valido"
    list_sintax.append("Bucle FOR")

def p_expression_if(p):
    '''expression : IF LPAREN expresionlogic RPAREN LBRACKET expression RBRACKET
    | IF LPAREN expresionlogic RPAREN LBRACKET expression RBRACKET ELSE LBRACKET expression RBRACKET'''
    p[0] = "Estructura if valida"
    list_sintax.append("Sentencia IF")

def p_preop(p):
    'oper : VARIABLE assignacion'

def p_postop(p):
    'oper : assignacion VARIABLE'


def p_datos(p):
    '''datos : BOOL
    | BYTE
    | CHAR
    | DECIMAL
    | DOUBLE
    | FLOAT
    | INT
    | LONG
    | SBYTE
    | SHORT
    | UINT
    | ULONG
    | USHORT
    | STRING'''
    p[0] = p[1]


#Asignacion de valor a variable creada
def p_expression_declsimp(p):
    'declaracion : VARIABLE ASSIGNMENT expression SEMICOLON'
    p[0] = "Asignacion de dato valida"

#DECLAracion de valor a variable 
def p_expression_decldato(p):
    '''expression : datos VARIABLE ASSIGNMENT term SEMICOLON'''
    if p[1].upper() in  ["INT", "LONG", "BYTE", "SHORT","SBYTE", "BYTE","UINT","ULONG","USHORT"]:
        if type(p[4])!=int:
            try:
                raise TipoDatoException
            except TipoDatoException as ex:
                msj_error(ex.mensaje)
        elif p[4]<0 and p[1].upper() in ["BYTE","UINT","ULONG","USHORT"]:
            try:
                raise TipoDatoException
            except TipoDatoException as ex:
                msj_error(ex.mensaje) 
        else:
            dic_rang = {"BYTE": [0,255], "SHORT":[-32768 , 32767],"SBYTE": [-128 , 127],
             "BYTE": [0 , 255],"USHORT":[ 0, 65535]}
            if p[1].upper() not in dic_rang:
                p[0] = "Declaracion de " + p[1].upper()+" Valida"
                list_sintax.append("Declaracion de " + p[1].upper()+" Valida")
            else:
                if p[4]>=dic_rang[p[1].upper()][0] and p[4]<=dic_rang[p[1].upper()][1]:
                    p[0] = "Declaracion de " + p[1].upper()+" Valida"
                    list_sintax.append("Declaracion de " + p[1].upper()+" Valida")
                else:
                    try:
                        raise TipoDatoException
                    except TipoDatoException as ex:
                        msj_error(ex.mensaje) 
    elif p[1].upper() in ["DECIMAL","DOUBLE","FLOAT"]:
        if type(p[4])!=float:
            try:
                raise TipoDatoException
            except TipoDatoException as ex:
                msj_error(ex.mensaje)
        else:
            p[0] = "Declaracion de " + p[1].upper()+" Valida"
            list_sintax.append("Declaracion de " + p[1].upper()+" Valida")
    elif p[1].upper() in ["STRING","CHAR"]:
        if type(p[4])!=str:
            try:
                raise TipoDatoException
            except TipoDatoException as ex:
                msj_error(ex.mensaje)
        elif len(p[4])>1 and p[1].upper() == "CHAR":
            try:
                raise TipoDatoException
            except TipoDatoException as ex:
                msj_error(ex.mensaje)
        else:
            p[0] = "Declaracion de " + p[1].upper()+" Valida"
            list_sintax.append("Declaracion de " + p[1].upper()+" Valida")
    elif p[1].upper() == "BOOL":
        if type(p[4])!=str:
            try:
                raise TipoDatoException
            except TipoDatoException as ex:
                msj_error(ex.mensaje)
        elif p[4].lower() in ["true","false"]:
            p[0] = "Declaracion de " + p[1].upper()+" Valida"
            list_sintax.append("Declaracion de " + p[1].upper()+" Valida")
        else:
            try:
                raise TipoDatoException
            except TipoDatoException as ex:
                msj_error(ex.mensaje)
    

def p_while(p):
    'expression : WHILE LPAREN expression RPAREN LBRACKET expression RBRACKET'
    p[0] = "Bucle WHILE valido"
    list_sintax.append("Bucle WHILE valido")


def p_for(p):
    'expression : FOR LPAREN declaracion expression SEMICOLON RPAREN LBRACKET expression RBRACKET'
    p[0] = "Bucle FOR valido"
    list_sintax.append("Bucle FOR valido")


def p_listas(p):
    'expression : LIST LESSERTHAN datos GREATERTHAN term ASSIGNMENT NEW LIST LESSERTHAN datos GREATERTHAN LPAREN RPAREN LBRACKET expression RBRACKET SEMICOLON'
    p[0] = "Declaracion de lista valida"
    list_sintax.append("Declaracion de lista valida")


def p_listas_add(p):
    'expression : term POINT ADD LPAREN term RPAREN SEMICOLON'


def p_listas_remove(p):
    'expression : term POINT REMOVE LPAREN term RPAREN SEMICOLON'


def p_listas_removeAt(p):
    'expression : term POINT REMOVEAT LPAREN term RPAREN SEMICOLON'


def p_tuplas(p):
    'expression : TUPLE LESSERTHAN LPAREN datos COMMA datos RPAREN GREATERTHAN term ASSIGNMENT NEW TUPLE LPAREN datos COMMA datos RPAREN LPAREN term COMMA term RPAREN SEMICOLON'
    p[0] = "Declaracion de tupla valida"
    list_sintax.append("Declaracion de tupla valida")


def p_tuplas_equals(p):
    'expression : term POINT EQUALS LPAREN expression RPAREN SEMICOLON'


def p_tuplas_compareTo(p):
    'expression : term POINT COMPARETO LPAREN expression RPAREN SEMICOLON'


def p_tuplas_item(p):
    'expression : term POINT ITEM SEMICOLON'

def p_error(p):
    if p:
        print("Syntax error at token", p.type)
    else:
        print("Syntax error at EOF")


parser = yacc.yacc()




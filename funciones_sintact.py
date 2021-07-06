
#tkinter calculator
from funciones import tokens
import ply.yacc as yacc

list_tok = []
list_sintax = []

def p_expression_term(p):
    'expression : term'

def p_expression_decl(p):
    '''expression : datos declaracion 
    | declaracion'''
    p[0] = ["Declaracion valida"]
    list_sintax.append("Declaracion de variable")

def p_expression_opermat(p):
    'expression : expression opmat term'
    p[0] = "Operacion Matematica Valida"
    list_sintax.append("Operacion Matematica")

def p_expression_condicion(p):
    'expression : condicional'
    p[0] = "Condicion Valida"
    list_sintax.append("Condicion")

def p_expression_logic(p):
    '''expression : expresionlogic
    | expresionlogic connectlog expresionlogic'''
    p[0] = "Operacion logica Valida"
    list_sintax.append("Operacion Logica")

def p_expresionlogic_rel(p):
    '''expresionlogic : term oplog term'''

def p_expresionlogic_bool(p):
    '''expresionlogic : TRUE
    | FALSE'''

def p_expression_preop(p):
    'expression : VARIABLE assignacion SEMICOLON'
    p[0] = "Operacion de post-incremento/decremento valida"
    list_sintax.append("Operacion de post-incremento/decremento")

def p_expression_postop(p):
    'expression : assignacion VARIABLE SEMICOLON'
    p[0] = "Operacion de pre-incremento/decremento valida"
    list_sintax.append("Operacion de pre-incremento/decremento")

def p_preop(p):
    'oper : VARIABLE assignacion'

def p_postop(p):
    'oper : assignacion VARIABLE'


def p_expression_while(p):
    'expression : WHILE condicional LBRACKET expression RBRACKET'
    p[0] = "BUCLE VALIDO"
    list_sintax.append("Bucle While")

def p_expression_for(p):
    'expression : FOR LPAREN datos declaracion expresionlogic SEMICOLON oper RPAREN LBRACKET expression RBRACKET'
    p[0] = "FOR Valido"
    list_sintax.append("Bucle FOR")

def p_expression_if(p):
    'expression : IF condicional LBRACKET expression RBRACKET'
    p[0] = "IF VALIDO"
    list_sintax.append("Sentencia IF")


def p_condicional(p):
    'condicional : LPAREN expresionlogic RPAREN'

def p_declaracion(p):
    'declaracion : VARIABLE ASSIGNMENT expression SEMICOLON'

def p_connectlog(p):
    '''connectlog : AND
    | OR'''
    list_tok.append(p[1])

def p_oplog(p):
    '''oplog : EQUAL
    | NOTEQUAL
    | GREATERTHAN
    | GREATERTHANEQUAL
    | LESSERTHAN
    | LESSERTHANEQUAL'''
    list_tok.append(p[1])

def p_opmat(p):
    '''opmat : PLUS
    | MINUS
    | TIMES
    | DIVIDE
    | MOD'''
    list_tok.append(p[1])

def p_assignacion(p):
    '''assignacion : INCREMENT
    | DECREMENT
    | COMPASSIGPLUS
    | COMPASSIGMINUS
    | COMPASSIGTIMES
    | COMPASSIGDIVIDE'''
    list_tok.append(p[1])

def p_term_factor(p):
    'term : factor'

def p_factor_var(p):
    'factor : VARIABLE'
    list_tok.append(p[1])

def p_term_numero(p):
    'term : NUMBER'
    list_tok.append(p[1])


#def p_while(p):
##    'while : WHILE LPAREN NUMBER RPAREN'
#    p[0] = "Sentencia WHile valida"


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
    | USHORT'''
    list_tok.append(p[1])

def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
    else:
        print("Syntax error at EOF")


# Build the parser
parser = yacc.yacc()
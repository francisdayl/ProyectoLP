
#tkinter calculator
from funciones import tokens
import ply.yacc as yacc

list_tok = []

<<<<<<< HEAD
def p_expression_term(p):
    'expression : term'
=======
L = [["IF",["(",["a"],")"],[]]]
>>>>>>> eacaffd849e1f91eb408bf734a03ca9c7adac7bb

def p_expression_decl(p):
    '''expression : datos declaracion 
    | declaracion'''
    p[0] = ["Declaracion valida"]

def p_expression_opermat(p):
    'expression : expression opmat term'
    p[0] = "Operacion Matematica Valida"

def p_expression_condicion(p):
    'expression : condicional'
    p[0] = "Condicion Valida"

def p_expression_logic(p):
    '''expression : expresionlogic
    | expresionlogic connectlog expresionlogic'''
    p[0] = "Operacion logica Valida"

def p_expresionlogic_rel(p):
    '''expresionlogic : term oplog term'''

def p_expresionlogic_bool(p):
    '''expresionlogic : TRUE
    | FALSE'''

def p_expression_preop(p):
    'expression : VARIABLE assignacion SEMICOLON'
    p[0] = "Operacion de post-incremento/decremento valida"

def p_expression_postop(p):
    'expression : assignacion VARIABLE SEMICOLON'
    p[0] = "Operacion de pre-incremento/decremento valida"

def p_preop(p):
    'oper : VARIABLE assignacion'

def p_postop(p):
    'oper : assignacion VARIABLE'


def p_expression_while(p):
    'expression : WHILE condicional LBRACKET expression RBRACKET'
    p[0] = "BUCLE VALIDO"

def p_expression_for(p):
    'expression : FOR LPAREN datos declaracion expresionlogic SEMICOLON oper RPAREN LBRACKET expression RBRACKET'
    p[0] = "FOR Valido"

def p_expression_if(p):
    'expression : IF condicional LBRACKET expression RBRACKET'
    p[0] = "IF VALIDO"


def p_condicional(p):
    'condicional : LPAREN expresionlogic RPAREN'

def p_declaracion(p):
    'declaracion : VARIABLE ASSIGNMENT expression SEMICOLON'

def p_connectlog(p):
    '''connectlog : AND
    | OR'''

def p_oplog(p):
    '''oplog : EQUAL
    | NOTEQUAL
    | GREATERTHAN
    | GREATERTHANEQUAL
    | LESSERTHAN
    | LESSERTHANEQUAL'''
    list_tok.append(p[1])
    #p[0] = p[1]
    #print("XDDD")

def p_opmat(p):
    '''opmat : PLUS
    | MINUS
    | TIMES
    | DIVIDE
    | MOD'''

def p_assignacion(p):
    '''assignacion : INCREMENT
    | DECREMENT
    | COMPASSIGPLUS
    | COMPASSIGMINUS
    | COMPASSIGTIMES
    | COMPASSIGDIVIDE'''

def p_term_factor(p):
    'term : factor'

def p_factor_var(p):
    'factor : VARIABLE'

def p_term_numero(p):
    'term : NUMBER'


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

def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
    else:
        print("Syntax error at EOF")


# Build the parser
parser = yacc.yacc()

while True:
    list_tok.clear()
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(list_tok)
    print(result)
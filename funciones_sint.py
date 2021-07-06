from funciones import tokens
import ply.yacc as yacc

list_tok = []
list_sintax = []
flag=0
def p_expression_term(p):
    'expression : term'

def p_expression_opermat(p):
    '''expression : expresionmate
    | LPAREN expresionmate RPAREN
    | expression opmat expresionmate
    | expresionmate opmat expression
    | expression opmat LPAREN expresionmate RPAREN
    | LPAREN expresionmate RPAREN opmat expression'''
    if (len(p)>2):
        if (p[1]!="Semantic error in input!" and p[3]!="Semantic error in input!" ):
            if p[2] == '+':
                p[0] = (p[1] + p[3])
            elif p[2] == '-':
                p[0] = (p[1] - p[3])
            elif p[2] == '*':
                p[0] = (p[1] * p[3])
            elif p[2] == '/':
                p[0] = (p[1] / p[3])
            elif p[2] == '%':
                p[0] = (p[1] % p[3])
        else:
            p[0] = "Semantic error in input!"
    else:
        if (p[1] == "Semantic error in input!"):
            p[0] = "Semantic error in input!"
        else:
            print(p[1])
            p[0] = "Operacion Matematica Valida"

    list_sintax.append("Operacion Matematica")

def p_expresionmate_rel(p):
    'expresionmate : term opmat term'
    if (str(p[1]).isdigit() and str(p[3]).isdigit()):
        if p[2] == '+':
            p[0] = (p[1] + p[3])
        elif p[2] == '-':
            p[0] = (p[1] - p[3])
        elif p[2] == '*':
            p[0] = (p[1] * p[3])
        elif p[2] == '/':
            p[0] = (p[1] / p[3])
        elif p[2] == '%':
            p[0] = (p[1] % p[3])
    else:
        p[0] = "Semantic error in input!"

def p_expression_logic(p):
    '''expression : expresionlogic
    | LPAREN expresionlogic RPAREN
    | expression oplog expresionlogic
    | expresionlogic oplog expression
    | expression connectlog expresionlogic
    | expresionlogic connectlog expression
    | expression oplog LPAREN expresionlogic RPAREN
    | LPAREN expresionlogic RPAREN oplog expression
    | expression connectlog LPAREN expresionlogic RPAREN
    | LPAREN expresionlogic RPAREN connectlog expression'''

    if (len(p)>2):
        if (p[1]!="Semantic error in input!" and p[3]!="Semantic error in input!" ):
            if p[2] == '==':
                p[0] = bool(p[1] == p[3])
            elif p[2] == '!=':
                p[0] = bool(p[1] != p[3])
            elif p[2] == '>':
                p[0] = bool(p[1] > p[3])
            elif p[2] == '>=':
                p[0] = bool(p[1] >= p[3])
            elif p[2] == '<':
                p[0] = bool(p[1] < p[3])
            elif p[2] == '<=':
                p[0] = bool(p[1] <= p[3])
            elif p[2] == '\&':
                p[0] = bool(p[1] and p[3])
            elif p[2] == '\^':
                p[0] = bool(p[1] or p[3])

        else:
            p[0] = "Semantic error in input!"

    else:
        if (p[1] == "Semantic error in input!"):
            p[0] = "Semantic error in input!"
        else:
            print(p[1])
            p[0]= "Operacion Logica Valida"
    list_sintax.append("Operacion Logica")


def p_expresionlogic_rel(p):
    'expresionlogic : term oplog term'
    if (type(p[1])==type(p[3])):
        if p[2] == '==':
            p[0] = bool(p[1] == p[3])
        elif p[2] == '!=':
            p[0] = bool(p[1] != p[3])
        elif p[2] == '>':
            p[0] = bool(p[1] > p[3])
        elif p[2] == '>=':
            p[0] = bool(p[1] >= p[3])
        elif p[2] == '<':
            p[0] = bool(p[1] < p[3])
        elif p[2] == '<=':
            p[0] = bool(p[1] <= p[3])
    else:
        p[0] = "Semantic error in input!"



def p_expresionlogic_bool(p):
    'expresionlogic : boolean connectlog boolean'
    if p[2] == '\&':
        p[0] = bool(p[1] and p[3])

    elif p[2] == '\^':
        p[0] = bool (p[1] or p[3])

def p_bool_true(p):
    '''boolean : TRUE
    | FALSE'''
    list_tok.append(p[1])
    p[0]=bool(p[1]=='true')


def p_connectlog(p):
    '''connectlog : AND
    | OR'''
    list_tok.append(p[1])
    p[0]=p[1]

def p_oplog(p):
    '''oplog : EQUAL
    | NOTEQUAL
    | GREATERTHAN
    | GREATERTHANEQUAL
    | LESSERTHAN
    | LESSERTHANEQUAL'''
    list_tok.append(p[1])
    p[0] = p[1]

def p_opmat(p):
    '''opmat : PLUS
    | MINUS
    | TIMES
    | DIVIDE
    | MOD'''
    list_tok.append(p[1])
    p[0] = p[1]

def p_assignacion(p):
    '''assignacion : INCREMENT
    | DECREMENT
    | COMPASSIGPLUS
    | COMPASSIGMINUS
    | COMPASSIGTIMES
    | COMPASSIGDIVIDE'''
    list_tok.append(p[1])
    p[0] = p[1]

def p_term(p):
    '''term : NUMBER
    | VARIABLE'''
    p[0] = p[1]


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


def p_declaracion(p):
    'declaracion : VARIABLE ASSIGNMENT expression SEMICOLON'

def p_expression_decl(p):
    '''expression : datos declaracion
    | declaracion'''
    p[0] = "Declaracion valida"
    list_sintax.append("Declaracion de variable")

def p_if(p):
    '''expression : IF LPAREN expression RPAREN LBRACKET expression RBRACKET
    | IF LPAREN expression RPAREN LBRACKET expression RBRACKET ELSE LBRACKET expression RBRACKET'''
    list_tok.append(p[1])
    p[0] = "Bucle IF valido"
    list_sintax.append("Bucle IF valido")


def p_while(p):
    'expression : WHILE LPAREN expression RPAREN LBRACKET expression RBRACKET'
    list_tok.append(p[1])
    p[0] = "Bucle WHILE valido"
    list_sintax.append("Bucle WHILE valido")


def p_for(p):
    'expression : FOR LPAREN declaracion expression SEMICOLON RPAREN LBRACKET expression RBRACKET'
    list_tok.append(p[1])
    p[0] = "Bucle FOR valido"
    list_sintax.append("Bucle FOR valido")


def p_listas(p):
    'expression : LIST LESSERTHAN datos GREATERTHAN term ASSIGNMENT NEW LIST LESSERTHAN datos GREATERTHAN LPAREN RPAREN LBRACKET expression RBRACKET SEMICOLON'
    list_tok.append(p[1])
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
    list_tok.append(p[1])
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
        # Just discard the token and tell the parser it's okay.
    else:
        print("Syntax error at EOF")


# Build the parser
parser = yacc.yacc()
# while True:
#     list_tok.clear()
#     try:
#         s = input('calc > ')
#     except EOFError:
#         break
#     if not s: continue
#     result = parser.parse(s)
#     print(list_tok)
#     print(result)

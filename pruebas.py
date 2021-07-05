from funciones import tokens
import ply.yacc as yacc

list_tok = []

def p_expression_term(p):
    'expression : term'

def p_expression_decl(p):
    '''expression : datos declaracion
    | declaracion'''
    p[0] = ["Declaracion valida"]

def p_expression_opermat(p):
    'expression : term opmat expression'
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

def p_logcon(p):
    'expression : LPAREN condicional connectlog expression RPAREN'

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

def p_true(p):
    'term : TRUE'
    p[0]= True

def p_false(p):
    'term : FALSE'
    p[0]= False

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

def p_semant_MatOper(p):
    '''factor : NUMBER PLUS NUMBER
    | NUMBER MINUS NUMBER
    | NUMBER TIMES NUMBER
    | NUMBER DIVIDE NUMBER
    | NUMBER MOD NUMBER'''

    if p[2] == 'PLUS' :
        p[0] = p[1] + p[3]

    elif p[2] == 'MINUS' :
        p[0] = p[1] - p[3]

    elif p[2] == 'TIMES' :
        p[0] = p[1] * p[3]

    elif p[2] == 'DIVIDE' :
        p[0] = p[1] / p[3]

    elif p[2] == 'MOD':
        p[0] = p[1] % p[3]


    if not isinstance(p[1], int) and not isinstance(p[2], int):
        print("Semantic error in input!")




def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
    else:
        print("Syntax error at EOF")

def p_boolean_operations(p):
    '''expression : NUMBER EQUAL NUMBER
    | NUMBER NOTEQUAL NUMBER
    | NUMBER GREATERTHAN NUMBER
    | NUMBER GREATERTHANEQUAL NUMBER
    | NUMBER LESSERTHAN NUMBER
    | NUMBER LESSERTHANEQUAL NUMBER
    | TRUE AND TRUE
    | TRUE OR TRUE
    | TRUE AND FALSE
    | TRUE OR FALSE
    | FALSE AND FALSE
    | FALSE OR FALSE
    | TRUE EQUAL TRUE
    | TRUE EQUAL FALSE
    | FALSE EQUAL FALSE
    | FALSE EQUAL TRUE
    | TRUE NOTEQUAL TRUE
    | TRUE NOTEQUAL FALSE
    | FALSE NOTEQUAL FALSE
    | FALSE NOTEQUAL TRUE'''
    # Semantic (prueba semantica)

    if p[1]=='true' or p[3]=='true' or p[1]=='false' or p[3]=='false':
        p[1]= bool(p[1]=='true')
        p[3]= bool(p[3]=='true')


    if p[2] == 'AND':
        p[0] = p[1] and p[3]

    elif p[2] == 'OR':
        p[0] = p[1] or p[3]
    elif p[2] == 'EQUAL':
        if p[1] == p[3]:
            p[0] = True
        else:
            p[0] = False
    elif p[2] == 'NOTEQUAL':
        if p[1] != p[3]:
            p[0] = True
        else:
            p[0] = False
    elif p[2] == 'GREATERTHAN':
        if p[1] > p[3]:
            p[0] = True
        else:
            p[0] = False
    elif p[2] == 'GREATERTHANEQUAL':
        if p[1] >= p[3]:
            p[0] = True
        else:
            p[0] = False
    elif p[2] == 'LESSERTHAN':
        if p[1] < p[3]:
            p[0] = True
        else:
            p[0] = False
    elif p[2] == 'LESSERTHANEQUAL':
        if p[1] <= p[3]:
            p[0] = True
        else:
            p[0] = False

    if (not isinstance(p[1], bool) and not isinstance(p[3], bool)) or (not isinstance(p[1], int) and not isinstance(p[3], int)) :
        print("Semantic error in input!")



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
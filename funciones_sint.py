from funciones import tokens
import ply.yacc as yacc



#EXPRESIONES MATEMATICAS

def p_factor_var(p):
    'factor : ID'


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_term_plus(p):
    'term : term PLUS factor'


def p_term_minus(p):
    'term : term MINUS factor'


def p_term_times(p):
    'term : term TIMES factor'


def p_term_div(p):
    'term : term DIVIDE factor'


def p_term_mod(p):
    'term : term MOD factor'


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_expression_plus(p):
    'expression : expression PLUS term'


def p_expression_minus(p):
    'expression : expression MINUS term'


def p_expression_times(p):
    'expression : expression TIMES term'


def p_expression_divide(p):
    'expression : expression DIVIDE term'


def p_expression_mod(p):
    'expression : expression MOD term'

#EXPRESIONES LOGICAS

def p_term_equal(p):
    'term : term EQUAL factor'


def p_term_notequal(p):
    'term : term NOTEQUAL factor'


def p_term_greaterthan(p):
    'term : term GREATERTHAN factor'


def p_term_greaterthanequal(p):
    'term : term GREATERTHANEQUAL factor'


def p_term_lesserthan(p):
    'term : term LESSERTHAN factor'


def p_term_lesserthanequal(p):
    'term : term LESSERTHANEQUAL factor'


def p_expression_equal(p):
    'expression : expression EQUAL term'


def p_expression_notequal(p):
    'expression : expression NOTEQUAL term'


def p_expression_greaterthan(p):
    'expression : expression GREATERTHAN term'


def p_expression_greaterthanequal(p):
    'expression : expression GREATERTHANEQUAL term'


def p_expression_lesserthan(p):
    'expression : expression LESSERTHAN term'


def p_expression_lesserthanequal(p):
    'expression : expression LESSERTHANEQUAL term'

#OPERACIONES DE INCREMENTO
def p_term_increment(p):
    'term : factor INCREMENT'


def p_term_decrement(p):
    'term : factor DECREMENT'


def p_term_compassigplus(p):
    'term : term COMPASSIGPLUS factor'


def p_term_compassigminus(p):
    'term : term COMPASSIGMINUS factor'


def p_term_compassigtimes(p):
    'term : term COMPASSIGTIMES factor'


def p_term_compassigdivide(p):
    'term : term COMPASSIGDIVIDE factor'


def p_expression_increment(p):
    'expression : term INCREMENT'


def p_expression_decrement(p):
    'expression : term DECREMENT'


def p_expression_compassigplus(p):
    'expression : expression COMPASSIGPLUS term'


def p_expression_compassigminus(p):
    'expression : expression COMPASSIGMINUS term'


def p_expression_compassigtimes(p):
    'expression : expression COMPASSIGTIMES term'


def p_expression_compassigdivide(p):
    'expression : expression COMPASSIGDIVIDE term'


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

def p_factor_num(p):
    '''factor : datos VARIABLE SEMICOLON
    | datos VARIABLE ASSIGNMENT VARIABLE SEMICOLON
    | VARIABLE ASSIGNMENT VARIABLE SEMICOLON
    | NUMBER'''


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'


def p_if(p):
    'expression : IF LPAREN expression RPAREN LBRACKET expression RBRACKET'


def p_else(p):
    'expression : ELSE LBRACKET expression RBRACKET'


def p_while(p):
    'expression : WHILE LPAREN expression RPAREN LBRACKET expression RBRACKET'


def p_for(p):
    'expression : FOR LPAREN expression SEMICOLON expression SEMICOLON RPAREN LBRACKET expression RBRACKET'


def p_listas(p):
    'expression: LIST LESSERTHAN datos BIGGERTHAN term ASSIGMENT NEW LIST LESSERTHAN datos BIGGERTHAN LPAREN RPAREN LBRACKET expression RBRACKET SEMICOLON'

def p_listas_add(p):
    'expression: term POINT ADD LPAREN factor RPAREN SEMICOLON'

def p_listas_remove(p):
    'expression: term POINT REMOVE LPAREN factor RPAREN SEMICOLON'

def p_listas_removeAt(p):
    'expression: term POINT REMOVEAT LPAREN NUMBER RPAREN SEMICOLON'

def p_tuplas(p):
    'expression: TUPLE LESSERTHAN LPAREN datos COMMA datos RPAREN BIGGERTHAN term ASSIGMENT NEW TUPLE LPAREN datos COMMA datos RPAREN LPAREN factor COMMA factor RPAREN SEMICOLON'

def p_tuplas_equals(p):
    'expression: term POINT EQUALS LPAREN expression RPAREN SEMICOLON'

def p_tuplas_compareTo(p):
    'expression: term POINT COMPARETO LPAREN expression RPAREN SEMICOLON'

def p_tuplas_item(p):
    'expression: term POINT ITEM SEMICOLON'

def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
    else:
        print("Syntax error at EOF")



# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
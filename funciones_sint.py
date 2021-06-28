from funciones import tokens
import ply.yacc as yacc


def p_expression_mate(p):
    'expression : expression opermat factor'
    p[0] = "Expresion matemática válida"

def p_expression_logic(p):
    'expression : expression operlog factor'
    p[0] = "Expresion lógica válida"

def p_expression_term(p):
    'expression : term'

def p_opermat_mate(p):
    '''opermat : PLUS 
    | MINUS
    | TIMES
    | DIVIDE
    | MOD'''

def p_operlog_logico(p):
    '''operlog : EQUAL
    | NOTEQUAL
    | GREATERTHAN
    | GREATERTHANEQUAL
    | LESSERTHAN
    | LESSERTHANEQUAL'''

def p_term_factor(p):
    'term : factor'

def p_factor_num(p):
    '''factor : NUMBER
    | VARIABLE'''

def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if s=="": 
       break
   result = parser.parse(s)
   print(result)



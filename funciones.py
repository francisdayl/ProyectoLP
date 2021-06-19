import ply.lex as lex
# List of token names.   This is always required
reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
}
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'MOD',
    'VARIABLE'
) + tuple(reserved.values())
# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MOD = r'%'
def t_VARIABLE(t):
    r'[a-zA-Z_]\w+'
    t.type = reserved.get(t.value, 'VARIABLE')  # Check for reserved words
    return t
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def getTokens(lexer):
    list_token = []
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        list_token.append([tok.type, tok.value, tok.lineno, tok.lexpos])
    return list_token
    
# Build the lexer
lexer = lex.lex()
"""
while linea!="":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)
# Tokenize
print("Succesfull")"""

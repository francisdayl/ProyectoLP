import ply.lex as lex
# List of token names.   This is always required
reserved = {
    'bool': 'BOOL',
    'byte': 'BYTE',
    'char': 'CHAR',
    'decimal': 'DECIMAL',
    'double': 'DOUBLE',
    'else': 'ELSE',
    'enum': 'ENUM',
    'event': 'EVENT',
    'float': 'FLOAT',
    'for': 'FOR',
    'foreach': 'FOREACH',
    'if': 'IF',
    'in': 'IN',
    'int': 'INT',
    'long': 'LONG',
    'new': 'NEW',
    'null': 'NULL',
    'sbyte': 'SBYTE',
    'short': 'SHORT',
    'sizeof': 'SIZEOF',
    'string': 'STRING',
    'typeof': 'TYPEOF',
    'uint': 'UINT',
    'ulong': 'ULONG',
    'ushort': 'USHORT',
    'while': 'WHILE',
    'false': 'FALSE',
    'true': 'TRUE',
    'console': 'CONSOLE',
    'writeline': 'WRITELINE',
    'write': 'WRITE',
    'list': 'LIST',
    'Tuple': 'TUPLE',
    'new': 'NEW',
    'add': 'ADD',
    'remove': 'REMOVE',
    'removeAt': 'REMOVEAT',
    'Equals': 'EQUALS',
    'CompareTo': 'COMPARETO',
    'Item': 'ITEM'
}
tokens = (
             'SEMICOLON',
             'COMMA',
             'POINT',
             'ASSIGNMENT',
             'NUMBER',
             'PLUS',
             'MINUS',
             'TIMES',
             'DIVIDE',
             'LPAREN',
             'RPAREN',
             'LBRACKET',
             'RBRACKET',
             'MOD',
             'VARIABLE',
             'EQUAL',
             'NOTEQUAL',
             'GREATERTHAN',
             'GREATERTHANEQUAL',
             'LESSERTHAN',
             'LESSERTHANEQUAL',
             'INCREMENT',
             'DECREMENT',
             'COMPASSIGPLUS',
             'COMPASSIGMINUS',
             'COMPASSIGTIMES',
             'COMPASSIGDIVIDE'
         ) + tuple(reserved.values())
# Regular expression rules for simple tokens
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_POINT = r'\.'
t_ASSIGNMENT = r'\='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MOD = r'\%'
t_EQUAL = r'\=\='
t_NOTEQUAL = r'\!\='
t_GREATERTHAN = r'\>'
t_GREATERTHANEQUAL = r'\>\='
t_LESSERTHAN = r'\<'
t_LESSERTHANEQUAL = r'\<\='
t_INCREMENT = r'\+\+'
t_DECREMENT = r'\-\-'
t_COMPASSIGPLUS = r'\+\='
t_COMPASSIGMINUS = r'\-\='
t_COMPASSIGTIMES = r'\*\='
t_COMPASSIGDIVIDE= r'\/\='
t_LBRACKET= r'\{'
t_RBRACKET= r'\}'



def t_VARIABLE(t):
    r'([a-zA-Z]|\_)([a-zA-Z0-9]|\_)*'
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


def t_comment(t):
    r'/\*.*\*/'
    pass

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
linea = " a"
"""while linea!="":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)
# Tokenize
print("Succesfull")"""

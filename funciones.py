import ply.lex as lex

class OperandosInvalidosException(Exception):
    def __init__(self):
        self.mensaje = "Operadores incompatibles para realizar operación artimética"

class CondicionInvalidaException(Exception):
    def __init__(self):
        self.mensaje = "Operadores incompatibles para realizar operación lógica"

class TipoDatoException(Exception):
    def __init__(self):
        self.mensaje = "Valor de dato incompatible con el tipo de dato asignado"

# List of token names.   This is always required
reserved = {
    'bool': 'BOOL',
    'byte': 'BYTE',
    'char': 'CHAR',
    'decimal': 'DECIMAL',
    'double': 'DOUBLE',
    'else': 'ELSE',
    'float': 'FLOAT',
    'for': 'FOR',
    'if': 'IF',
    'int': 'INT',
    'long': 'LONG',
    'new': 'NEW',
    'sbyte': 'SBYTE',
    'short': 'SHORT',
    'uint': 'UINT',
    'ulong': 'ULONG',
    'ushort': 'USHORT',
    'while': 'WHILE',
    'false': 'FALSE',
    'true': 'TRUE',
    'List': 'LIST',
    'Tuple': 'TUPLE',
    'add': 'ADD',
    'remove': 'REMOVE',
    'removeAt': 'REMOVEAT',
    'Equals': 'EQUALS',
    'CompareTo': 'COMPARETO',
    'Item': 'ITEM',
    'string' : 'STRING'
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
             'COMPASSIGDIVIDE',
             'LBRACKET',
             'RBRACKET',
             'AND',
             'OR',
             'TEXT',
             'NUMDEC',
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
t_AND=r'\&\&'
t_OR=r'\|\|'
t_TEXT=r'\".*\"'

def t_VARIABLE(t):
    r'([a-zA-Z]|\_)([a-zA-Z0-9]|\_)*'
    t.type = reserved.get(t.value, 'VARIABLE')  # Check for reserved words
    return t

def t_NUMDEC(t):
    r'-{0,1}[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\-{0,1}[0-9]+'
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


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

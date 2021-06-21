import ply.lex as lex

# List of token names.   This is always required
reserved = {
    'abstract': 'ABSTRACT',
    'as': 'AS',
    'base': 'BASE',
    'bool': 'BOOL',
    'break': 'BREAK',
    'byte': 'BYTE',
    'case': 'CASE',
    'catch': 'CATCH',
    'char': 'CHAR',
    'checked': 'CHECKED',
    'class': 'CLASS',
    'const': 'CONST',
    'continue': 'CONTINUE',
    'decimal': 'DECIMAL',
    'default': 'DEFAULT',
    'delegate': 'DELEGATE',
    'do': 'DO',
    'double': 'DOUBLE',
    'else': 'ELSE',
    'enum': 'ENUM',
    'event': 'EVENT',
    'explicit': 'EXPLICIT',
    'extern': 'EXTERN',
    'finally': 'FINALLY',
    'fixed': 'FIXED',
    'float': 'FLOAT',
    'for': 'FOR',
    'foreach': 'FOREACH',
    'goto': 'GOTO',
    'if': 'IF',
    'implicit': 'IMPLICIT',
    'in': 'IN',
    'int': 'INT',
    'interface': 'INTERFACE',
    'internal': 'INTERNAL',
    'is': 'IS',
    'lock': 'LOCK',
    'long': 'LONG',
    'namespace': 'NAMESPACE',
    'new': 'NEW',
    'null': 'NULL',
    'object': 'OBJECT',
    'operator': 'OPERATOR',
    'out': 'OUT',
    'override': 'OVERRIDE',
    'params': 'PARAMS',
    'private': 'PRIVATE',
    'protected': 'PROTECTED',
    'public': 'PUBLIC',
    'readonly': 'READONLY',
    'ref': 'REF',
    'return': 'RETURN',
    'sbyte': 'SBYTE',
    'sealed': 'SEALED',
    'short': 'SHORT',
    'sizeof': 'SIZEOF',
    'stackalloc': 'STACKALLOC',
    'static': 'STATIC',
    'string': 'STRING',
    'struct': 'STRUCT',
    'switch': 'SWITCH',
    'this': 'THIS',
    'throw': 'THROW',
    'try': 'TRY',
    'typeof': 'TYPEOF',
    'uint': 'UINT',
    'ulong': 'ULONG',
    'unchecked': 'UNCHECKED',
    'unsafe': 'UNSAFE',
    'ushort': 'USHORT',
    'using': 'USING',
    'virtual': 'VIRTUAL',
    'void': 'VOID',
    'volatile': 'VOLATILE',
    'while': 'WHILE',
    'false': 'FALSE',
    'true': 'TRUE',
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


def t_VARIABLE(t):
    r'^([a-zA-Z]|\_)([a-zA-Z0-9]|\_)*'
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

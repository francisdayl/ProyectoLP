
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD AND ASSIGNMENT BOOL BYTE CHAR COMMA COMPARETO COMPASSIGDIVIDE COMPASSIGMINUS COMPASSIGPLUS COMPASSIGTIMES DECIMAL DECREMENT DIVIDE DOUBLE ELSE EQUAL EQUALS FALSE FLOAT FOR GREATERTHAN GREATERTHANEQUAL IF INCREMENT INT ITEM LBRACKET LESSERTHAN LESSERTHANEQUAL LIST LONG LPAREN MINUS MOD NEW NOTEQUAL NULL NUMBER OR PLUS POINT RBRACKET REMOVE REMOVEAT RPAREN SBYTE SEMICOLON SHORT TIMES TRUE TUPLE UINT ULONG USHORT VARIABLE WHILEexpression : termexpression : expresionmate\n    | LPAREN expresionmate RPAREN\n    | expression opmat expresionmate\n    | expresionmate opmat expression\n    | expression opmat LPAREN expresionmate RPAREN\n    | LPAREN expresionmate RPAREN opmat expressionexpresionmate : term opmat termexpression : expresionlogic\n    | LPAREN expresionlogic RPAREN\n    | expression oplog expresionlogic\n    | expresionlogic oplog expression\n    | expression connectlog expresionlogic\n    | expresionlogic connectlog expression\n    | expression oplog LPAREN expresionlogic RPAREN\n    | LPAREN expresionlogic RPAREN oplog expression\n    | expression connectlog LPAREN expresionlogic RPAREN\n    | LPAREN expresionlogic RPAREN connectlog expressionexpresionlogic : term oplog termexpresionlogic : boolean connectlog booleanboolean : TRUE\n    | FALSEconnectlog : AND\n    | ORoplog : EQUAL\n    | NOTEQUAL\n    | GREATERTHAN\n    | GREATERTHANEQUAL\n    | LESSERTHAN\n    | LESSERTHANEQUALopmat : PLUS\n    | MINUS\n    | TIMES\n    | DIVIDE\n    | MODassignacion : INCREMENT\n    | DECREMENT\n    | COMPASSIGPLUS\n    | COMPASSIGMINUS\n    | COMPASSIGTIMES\n    | COMPASSIGDIVIDEterm : NUMBER\n    | VARIABLEexpression : VARIABLE assignacion SEMICOLONexpression : assignacion VARIABLE SEMICOLONoper : VARIABLE assignacionoper : assignacion VARIABLEexpression : WHILE LPAREN expresionlogic RPAREN LBRACKET expression RBRACKETexpression : FOR LPAREN datos declaracion expresionlogic SEMICOLON oper RPAREN LBRACKET expression RBRACKETexpression : IF LPAREN expresionlogic RPAREN LBRACKET expression RBRACKET\n    | IF LPAREN expresionlogic RPAREN LBRACKET expression RBRACKET ELSE LBRACKET expression RBRACKETdatos : BOOL\n    | BYTE\n    | CHAR\n    | DECIMAL\n    | DOUBLE\n    | FLOAT\n    | INT\n    | LONG\n    | SBYTE\n    | SHORT\n    | UINT\n    | ULONG\n    | USHORTdeclaracion : VARIABLE ASSIGNMENT expression SEMICOLONexpression : datos declaracion\n    | declaracionexpression : IF LPAREN expression RPAREN LBRACKET expression RBRACKET\n    | IF LPAREN expression RPAREN LBRACKET expression RBRACKET ELSE LBRACKET expression RBRACKETexpression : WHILE LPAREN expression RPAREN LBRACKET expression RBRACKETexpression : FOR LPAREN declaracion expression SEMICOLON RPAREN LBRACKET expression RBRACKETexpression : LIST LESSERTHAN datos GREATERTHAN term ASSIGNMENT NEW LIST LESSERTHAN datos GREATERTHAN LPAREN RPAREN LBRACKET expression RBRACKET SEMICOLONexpression : term POINT ADD LPAREN term RPAREN SEMICOLONexpression : term POINT REMOVE LPAREN term RPAREN SEMICOLONexpression : term POINT REMOVEAT LPAREN term RPAREN SEMICOLONexpression : TUPLE LESSERTHAN LPAREN datos COMMA datos RPAREN GREATERTHAN term ASSIGNMENT NEW TUPLE LPAREN datos COMMA datos RPAREN LPAREN term COMMA term RPAREN SEMICOLONexpression : term POINT EQUALS LPAREN expression RPAREN SEMICOLONexpression : term POINT COMPARETO LPAREN expression RPAREN SEMICOLONexpression : term POINT ITEM SEMICOLON'
    
_lr_action_items = {'LPAREN':([0,8,9,12,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,71,73,83,84,85,86,87,103,115,116,118,119,120,121,141,142,145,146,172,185,187,188,199,202,205,212,],[4,67,68,71,76,79,82,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,4,4,4,4,4,4,107,112,113,114,115,116,4,4,4,4,4,4,-65,4,4,4,4,4,4,4,4,201,204,4,213,]),'VARIABLE':([0,4,7,10,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,62,63,65,67,68,71,76,79,82,102,103,112,113,114,115,116,118,119,120,121,124,128,141,142,145,146,156,171,172,184,185,187,188,205,213,215,],[6,61,66,70,-36,-37,-38,-39,-40,-41,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,61,61,61,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,61,61,6,6,6,6,6,70,6,61,61,61,70,6,61,61,61,6,6,6,6,6,-65,61,61,6,6,6,6,170,179,6,61,6,6,6,6,61,61,]),'WHILE':([0,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,71,103,115,116,118,119,120,121,141,142,145,146,172,185,187,188,205,],[8,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,8,8,8,8,8,8,8,8,8,8,8,8,-65,8,8,8,8,8,8,8,8,8,]),'FOR':([0,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,71,103,115,116,118,119,120,121,141,142,145,146,172,185,187,188,205,],[9,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,9,9,9,9,9,9,9,9,9,9,9,9,-65,9,9,9,9,9,9,9,9,9,]),'IF':([0,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,71,103,115,116,118,119,120,121,141,142,145,146,172,185,187,188,205,],[12,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,12,12,12,12,12,12,12,12,12,12,12,12,-65,12,12,12,12,12,12,12,12,12,]),'LIST':([0,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,71,103,115,116,118,119,120,121,141,142,145,146,172,175,185,187,188,205,],[13,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,13,13,13,13,13,13,13,13,13,13,13,13,-65,13,13,13,13,13,183,13,13,13,13,]),'TUPLE':([0,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,71,103,115,116,118,119,120,121,141,142,145,146,172,185,187,188,200,205,],[14,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,14,14,14,14,14,14,14,14,14,14,14,14,-65,14,14,14,14,14,14,14,14,202,14,]),'NUMBER':([0,4,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,62,63,65,67,71,76,79,82,103,112,113,114,115,116,118,119,120,121,124,128,141,142,145,146,172,184,185,187,188,205,213,215,],[15,15,15,15,15,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-65,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'INCREMENT':([0,6,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,71,103,115,116,118,119,120,121,141,142,145,146,156,170,172,185,187,188,205,],[17,17,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,17,17,17,17,17,17,17,17,17,17,17,17,-65,17,17,17,17,17,17,17,17,17,17,17,]),'DECREMENT':([0,6,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,71,103,115,116,118,119,120,121,141,142,145,146,156,170,172,185,187,188,205,],[18,18,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,18,18,18,18,18,18,18,18,18,18,18,18,-65,18,18,18,18,18,18,18,18,18,18,18,]),'COMPASSIGPLUS':([0,6,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,71,103,115,116,118,119,120,121,141,142,145,146,156,170,172,185,187,188,205,],[19,19,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,19,19,19,19,19,19,19,19,19,19,19,19,-65,19,19,19,19,19,19,19,19,19,19,19,]),'COMPASSIGMINUS':([0,6,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,71,103,115,116,118,119,120,121,141,142,145,146,156,170,172,185,187,188,205,],[20,20,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,20,20,20,20,20,20,20,20,20,20,20,20,-65,20,20,20,20,20,20,20,20,20,20,20,]),'COMPASSIGTIMES':([0,6,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,71,103,115,116,118,119,120,121,141,142,145,146,156,170,172,185,187,188,205,],[21,21,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,21,21,21,21,21,21,21,21,21,21,21,21,-65,21,21,21,21,21,21,21,21,21,21,21,]),'COMPASSIGDIVIDE':([0,6,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,71,103,115,116,118,119,120,121,141,142,145,146,156,170,172,185,187,188,205,],[22,22,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,22,22,22,22,22,22,22,22,22,22,22,22,-65,22,22,22,22,22,22,22,22,22,22,22,]),'BOOL':([0,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,68,71,72,103,107,115,116,118,119,120,121,141,142,145,146,148,172,185,187,188,189,204,205,208,],[23,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-65,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'BYTE':([0,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,68,71,72,103,107,115,116,118,119,120,121,141,142,145,146,148,172,185,187,188,189,204,205,208,],[24,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-65,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'CHAR':([0,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,68,71,72,103,107,115,116,118,119,120,121,141,142,145,146,148,172,185,187,188,189,204,205,208,],[25,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-65,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'DECIMAL':([0,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,68,71,72,103,107,115,116,118,119,120,121,141,142,145,146,148,172,185,187,188,189,204,205,208,],[26,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-65,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'DOUBLE':([0,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,68,71,72,103,107,115,116,118,119,120,121,141,142,145,146,148,172,185,187,188,189,204,205,208,],[27,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-65,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'FLOAT':([0,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,68,71,72,103,107,115,116,118,119,120,121,141,142,145,146,148,172,185,187,188,189,204,205,208,],[28,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-65,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'INT':([0,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,68,71,72,103,107,115,116,118,119,120,121,141,142,145,146,148,172,185,187,188,189,204,205,208,],[29,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-65,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'LONG':([0,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,68,71,72,103,107,115,116,118,119,120,121,141,142,145,146,148,172,185,187,188,189,204,205,208,],[30,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-65,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'SBYTE':([0,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,68,71,72,103,107,115,116,118,119,120,121,141,142,145,146,148,172,185,187,188,189,204,205,208,],[31,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-65,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'SHORT':([0,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,68,71,72,103,107,115,116,118,119,120,121,141,142,145,146,148,172,185,187,188,189,204,205,208,],[32,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-65,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'UINT':([0,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,68,71,72,103,107,115,116,118,119,120,121,141,142,145,146,148,172,185,187,188,189,204,205,208,],[33,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-65,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'ULONG':([0,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,68,71,72,103,107,115,116,118,119,120,121,141,142,145,146,148,172,185,187,188,189,204,205,208,],[34,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-65,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'USHORT':([0,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,68,71,72,103,107,115,116,118,119,120,121,141,142,145,146,148,172,185,187,188,189,204,205,208,],[35,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-65,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'TRUE':([0,4,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,71,74,79,82,103,115,116,118,119,120,121,124,141,142,145,146,172,185,187,188,205,],[36,36,36,36,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-65,36,36,36,36,36,36,36,36,36,36,]),'FALSE':([0,4,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,57,62,63,65,67,71,74,79,82,103,115,116,118,119,120,121,124,141,142,145,146,172,185,187,188,205,],[37,37,37,37,-31,-32,-33,-34,-35,-25,-26,-27,-28,-29,-30,-23,-24,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-65,37,37,37,37,37,37,37,37,37,37,]),'$end':([1,2,3,5,6,11,15,36,37,61,69,75,78,81,89,90,91,92,93,94,95,96,98,108,117,121,130,131,132,138,139,140,162,163,164,165,166,167,168,173,174,186,196,197,198,211,218,],[0,-1,-2,-9,-43,-67,-42,-21,-22,-43,-66,-4,-11,-13,-8,-19,-5,-3,-10,-12,-14,-44,-45,-20,-79,-65,-6,-15,-17,-7,-16,-18,-73,-74,-75,-77,-78,-48,-70,-50,-68,-71,-49,-51,-69,-72,-76,]),'PLUS':([1,2,3,5,6,11,15,36,37,60,61,69,75,77,78,81,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,108,117,121,125,130,131,132,136,137,138,139,140,154,155,158,159,162,163,164,165,166,167,168,173,174,180,186,191,192,193,196,197,198,207,211,218,],[41,41,41,-9,-43,-67,-42,-21,-22,41,-43,-66,-4,41,-11,-13,-8,-19,41,41,-10,41,41,-44,41,-45,-9,41,41,-9,41,-20,-79,-65,41,-6,-15,-17,41,41,41,41,41,41,41,41,41,-73,-74,-75,-77,-78,-48,-70,-50,-68,41,-71,41,41,41,-49,-51,-69,41,-72,-76,]),'MINUS':([1,2,3,5,6,11,15,36,37,60,61,69,75,77,78,81,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,108,117,121,125,130,131,132,136,137,138,139,140,154,155,158,159,162,163,164,165,166,167,168,173,174,180,186,191,192,193,196,197,198,207,211,218,],[42,42,42,-9,-43,-67,-42,-21,-22,42,-43,-66,-4,42,-11,-13,-8,-19,42,42,-10,42,42,-44,42,-45,-9,42,42,-9,42,-20,-79,-65,42,-6,-15,-17,42,42,42,42,42,42,42,42,42,-73,-74,-75,-77,-78,-48,-70,-50,-68,42,-71,42,42,42,-49,-51,-69,42,-72,-76,]),'TIMES':([1,2,3,5,6,11,15,36,37,60,61,69,75,77,78,81,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,108,117,121,125,130,131,132,136,137,138,139,140,154,155,158,159,162,163,164,165,166,167,168,173,174,180,186,191,192,193,196,197,198,207,211,218,],[43,43,43,-9,-43,-67,-42,-21,-22,43,-43,-66,-4,43,-11,-13,-8,-19,43,43,-10,43,43,-44,43,-45,-9,43,43,-9,43,-20,-79,-65,43,-6,-15,-17,43,43,43,43,43,43,43,43,43,-73,-74,-75,-77,-78,-48,-70,-50,-68,43,-71,43,43,43,-49,-51,-69,43,-72,-76,]),'DIVIDE':([1,2,3,5,6,11,15,36,37,60,61,69,75,77,78,81,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,108,117,121,125,130,131,132,136,137,138,139,140,154,155,158,159,162,163,164,165,166,167,168,173,174,180,186,191,192,193,196,197,198,207,211,218,],[44,44,44,-9,-43,-67,-42,-21,-22,44,-43,-66,-4,44,-11,-13,-8,-19,44,44,-10,44,44,-44,44,-45,-9,44,44,-9,44,-20,-79,-65,44,-6,-15,-17,44,44,44,44,44,44,44,44,44,-73,-74,-75,-77,-78,-48,-70,-50,-68,44,-71,44,44,44,-49,-51,-69,44,-72,-76,]),'MOD':([1,2,3,5,6,11,15,36,37,60,61,69,75,77,78,81,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,108,117,121,125,130,131,132,136,137,138,139,140,154,155,158,159,162,163,164,165,166,167,168,173,174,180,186,191,192,193,196,197,198,207,211,218,],[45,45,45,-9,-43,-67,-42,-21,-22,45,-43,-66,-4,45,-11,-13,-8,-19,45,45,-10,45,45,-44,45,-45,-9,45,45,-9,45,-20,-79,-65,45,-6,-15,-17,45,45,45,45,45,45,45,45,45,-73,-74,-75,-77,-78,-48,-70,-50,-68,45,-71,45,45,45,-49,-51,-69,45,-72,-76,]),'EQUAL':([1,2,3,5,6,11,15,36,37,60,61,69,75,78,80,81,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,108,117,121,125,130,131,132,136,137,138,139,140,154,155,158,159,162,163,164,165,166,167,168,173,174,180,186,191,192,193,196,197,198,207,211,218,],[46,46,-2,46,-43,-67,-42,-21,-22,46,-43,-66,-4,-11,46,-13,-8,-19,46,-3,46,46,46,-44,46,-45,46,46,46,46,46,-20,-79,-65,46,-6,-15,-17,46,46,46,46,46,46,46,46,46,-73,-74,-75,-77,-78,-48,-70,-50,-68,46,-71,46,46,46,-49,-51,-69,46,-72,-76,]),'NOTEQUAL':([1,2,3,5,6,11,15,36,37,60,61,69,75,78,80,81,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,108,117,121,125,130,131,132,136,137,138,139,140,154,155,158,159,162,163,164,165,166,167,168,173,174,180,186,191,192,193,196,197,198,207,211,218,],[47,47,-2,47,-43,-67,-42,-21,-22,47,-43,-66,-4,-11,47,-13,-8,-19,47,-3,47,47,47,-44,47,-45,47,47,47,47,47,-20,-79,-65,47,-6,-15,-17,47,47,47,47,47,47,47,47,47,-73,-74,-75,-77,-78,-48,-70,-50,-68,47,-71,47,47,47,-49,-51,-69,47,-72,-76,]),'GREATERTHAN':([1,2,3,5,6,11,15,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,60,61,69,75,78,80,81,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,106,108,117,121,125,130,131,132,136,137,138,139,140,154,155,158,159,162,163,164,165,166,167,168,173,174,176,180,186,191,192,193,194,196,197,198,207,211,218,],[48,48,-2,48,-43,-67,-42,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-21,-22,48,-43,-66,-4,-11,48,-13,-8,-19,48,-3,48,48,48,-44,48,-45,48,48,48,48,48,128,-20,-79,-65,48,-6,-15,-17,48,48,48,48,48,48,48,48,48,-73,-74,-75,-77,-78,-48,-70,-50,-68,184,48,-71,48,48,48,199,-49,-51,-69,48,-72,-76,]),'GREATERTHANEQUAL':([1,2,3,5,6,11,15,36,37,60,61,69,75,78,80,81,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,108,117,121,125,130,131,132,136,137,138,139,140,154,155,158,159,162,163,164,165,166,167,168,173,174,180,186,191,192,193,196,197,198,207,211,218,],[49,49,-2,49,-43,-67,-42,-21,-22,49,-43,-66,-4,-11,49,-13,-8,-19,49,-3,49,49,49,-44,49,-45,49,49,49,49,49,-20,-79,-65,49,-6,-15,-17,49,49,49,49,49,49,49,49,49,-73,-74,-75,-77,-78,-48,-70,-50,-68,49,-71,49,49,49,-49,-51,-69,49,-72,-76,]),'LESSERTHAN':([1,2,3,5,6,11,13,14,15,36,37,60,61,69,75,78,80,81,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,108,117,121,125,130,131,132,136,137,138,139,140,154,155,158,159,162,163,164,165,166,167,168,173,174,180,183,186,191,192,193,196,197,198,207,211,218,],[50,50,-2,50,-43,-67,72,73,-42,-21,-22,50,-43,-66,-4,-11,50,-13,-8,-19,50,-3,50,50,50,-44,50,-45,50,50,50,50,50,-20,-79,-65,50,-6,-15,-17,50,50,50,50,50,50,50,50,50,-73,-74,-75,-77,-78,-48,-70,-50,-68,50,189,-71,50,50,50,-49,-51,-69,50,-72,-76,]),'LESSERTHANEQUAL':([1,2,3,5,6,11,15,36,37,60,61,69,75,78,80,81,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,108,117,121,125,130,131,132,136,137,138,139,140,154,155,158,159,162,163,164,165,166,167,168,173,174,180,186,191,192,193,196,197,198,207,211,218,],[51,51,-2,51,-43,-67,-42,-21,-22,51,-43,-66,-4,-11,51,-13,-8,-19,51,-3,51,51,51,-44,51,-45,51,51,51,51,51,-20,-79,-65,51,-6,-15,-17,51,51,51,51,51,51,51,51,51,-73,-74,-75,-77,-78,-48,-70,-50,-68,51,-71,51,51,51,-49,-51,-69,51,-72,-76,]),'AND':([1,2,3,5,6,11,15,16,36,37,61,69,75,78,81,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,108,117,121,125,130,131,132,136,137,138,139,140,154,155,158,159,162,163,164,165,166,167,168,173,174,180,186,191,192,193,196,197,198,207,211,218,],[52,-1,-2,52,-43,-67,-42,52,-21,-22,-43,-66,-4,-11,-13,-8,-19,52,-3,52,52,52,-44,52,-45,52,52,-1,52,52,-20,-79,-65,52,-6,-15,-17,52,52,52,52,52,52,52,52,52,-73,-74,-75,-77,-78,-48,-70,-50,-68,52,-71,52,52,52,-49,-51,-69,52,-72,-76,]),'OR':([1,2,3,5,6,11,15,16,36,37,61,69,75,78,81,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,108,117,121,125,130,131,132,136,137,138,139,140,154,155,158,159,162,163,164,165,166,167,168,173,174,180,186,191,192,193,196,197,198,207,211,218,],[53,-1,-2,53,-43,-67,-42,53,-21,-22,-43,-66,-4,-11,-13,-8,-19,53,-3,53,53,53,-44,53,-45,53,53,-1,53,53,-20,-79,-65,53,-6,-15,-17,53,53,53,53,53,53,53,53,53,-73,-74,-75,-77,-78,-48,-70,-50,-68,53,-71,53,53,53,-49,-51,-69,53,-72,-76,]),'SEMICOLON':([2,3,5,6,11,15,17,18,19,20,21,22,36,37,61,64,66,69,75,78,81,88,89,90,91,92,93,94,95,96,97,98,108,117,121,125,130,131,132,138,139,140,143,149,150,151,152,153,162,163,164,165,166,167,168,173,174,186,196,197,198,209,211,217,218,],[-1,-2,-9,-43,-67,-42,-36,-37,-38,-39,-40,-41,-21,-22,-43,96,98,-66,-4,-11,-13,117,-8,-19,-5,-3,-10,-12,-14,-44,121,-45,-20,-79,-65,144,-6,-15,-17,-7,-16,-18,156,162,163,164,165,166,-73,-74,-75,-77,-78,-48,-70,-50,-68,-71,-49,-51,-69,211,-72,218,-76,]),'RPAREN':([2,3,5,6,11,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,58,59,61,69,75,78,81,89,90,91,92,93,94,95,96,98,99,100,101,104,105,108,109,110,111,117,121,130,131,132,133,134,135,136,137,138,139,140,144,161,162,163,164,165,166,167,168,169,173,174,178,179,186,196,197,198,201,210,211,216,218,],[-1,-2,-9,-43,-67,-42,-36,-37,-38,-39,-40,-41,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-21,-22,92,93,-43,-66,-4,-11,-13,-8,-19,-5,-3,-10,-12,-14,-44,-45,122,123,-1,126,127,-20,130,131,132,-79,-65,-6,-15,-17,149,150,151,152,153,-7,-16,-18,157,176,-73,-74,-75,-77,-78,-48,-70,177,-50,-68,-46,-47,-71,-49,-51,-69,203,212,-72,217,-76,]),'RBRACKET':([2,3,5,6,11,15,36,37,61,69,75,78,81,89,90,91,92,93,94,95,96,98,108,117,121,130,131,132,138,139,140,154,155,158,159,162,163,164,165,166,167,168,173,174,180,186,191,192,193,196,197,198,207,211,218,],[-1,-2,-9,-43,-67,-42,-21,-22,-43,-66,-4,-11,-13,-8,-19,-5,-3,-10,-12,-14,-44,-45,-20,-79,-65,-6,-15,-17,-7,-16,-18,167,168,173,174,-73,-74,-75,-77,-78,-48,-70,-50,-68,186,-71,196,197,198,-49,-51,-69,209,-72,-76,]),'POINT':([2,6,15,101,],[54,-43,-42,54,]),'ASSIGNMENT':([6,15,61,70,147,190,],[65,-42,-43,65,160,195,]),'COMMA':([15,23,24,25,26,27,28,29,30,31,32,33,34,35,61,129,206,214,],[-42,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-43,148,208,215,]),'ADD':([54,],[83,]),'REMOVE':([54,],[84,]),'REMOVEAT':([54,],[85,]),'EQUALS':([54,],[86,]),'COMPARETO':([54,],[87,]),'ITEM':([54,],[88,]),'LBRACKET':([122,123,126,127,157,177,181,182,203,],[141,142,145,146,172,185,187,188,205,]),'NEW':([160,195,],[175,200,]),'ELSE':([173,174,],[181,182,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,57,62,63,65,67,71,103,115,116,118,119,120,141,142,145,146,172,185,187,188,205,],[1,91,94,95,97,100,105,125,136,137,138,139,140,154,155,158,159,180,191,192,193,207,]),'term':([0,4,38,39,40,55,56,57,62,63,65,67,71,76,79,82,103,112,113,114,115,116,118,119,120,124,128,141,142,145,146,172,184,185,187,188,205,213,215,],[2,60,77,80,80,89,90,2,2,2,2,101,101,77,80,80,2,133,134,135,2,2,2,2,2,80,147,2,2,2,2,2,190,2,2,2,2,214,216,]),'expresionmate':([0,4,38,57,62,63,65,67,71,76,103,115,116,118,119,120,141,142,145,146,172,185,187,188,205,],[3,58,75,3,3,3,3,3,3,109,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'expresionlogic':([0,4,39,40,57,62,63,65,67,71,79,82,103,115,116,118,119,120,124,141,142,145,146,172,185,187,188,205,],[5,59,78,81,5,5,5,5,99,104,110,111,5,5,5,5,5,5,143,5,5,5,5,5,5,5,5,5,]),'assignacion':([0,6,57,62,63,65,67,71,103,115,116,118,119,120,141,142,145,146,156,170,172,185,187,188,205,],[7,64,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,171,178,7,7,7,7,7,]),'datos':([0,57,62,63,65,67,68,71,72,103,107,115,116,118,119,120,141,142,145,146,148,172,185,187,188,189,204,205,208,],[10,10,10,10,10,10,102,10,106,10,129,10,10,10,10,10,10,10,10,10,161,10,10,10,10,194,206,10,210,]),'declaracion':([0,10,57,62,63,65,67,68,71,102,103,115,116,118,119,120,141,142,145,146,172,185,187,188,205,],[11,69,11,11,11,11,11,103,11,124,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'boolean':([0,4,39,40,57,62,63,65,67,71,74,79,82,103,115,116,118,119,120,124,141,142,145,146,172,185,187,188,205,],[16,16,16,16,16,16,16,16,16,16,108,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'opmat':([1,2,3,60,77,91,92,94,95,97,100,101,105,125,136,137,138,139,140,154,155,158,159,180,191,192,193,207,],[38,55,57,55,55,38,118,38,38,38,38,55,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'oplog':([1,2,5,60,80,91,93,94,95,97,99,100,101,104,105,125,136,137,138,139,140,154,155,158,159,180,191,192,193,207,],[39,56,62,56,56,39,119,39,39,39,62,39,56,62,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'connectlog':([1,5,16,91,93,94,95,97,99,100,104,105,125,136,137,138,139,140,154,155,158,159,180,191,192,193,207,],[40,63,74,40,120,40,40,40,63,40,63,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'oper':([156,],[169,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> term','expression',1,'p_expression_term','funciones_sint.py',8),
  ('expression -> expresionmate','expression',1,'p_expression_opermat','funciones_sint.py',11),
  ('expression -> LPAREN expresionmate RPAREN','expression',3,'p_expression_opermat','funciones_sint.py',12),
  ('expression -> expression opmat expresionmate','expression',3,'p_expression_opermat','funciones_sint.py',13),
  ('expression -> expresionmate opmat expression','expression',3,'p_expression_opermat','funciones_sint.py',14),
  ('expression -> expression opmat LPAREN expresionmate RPAREN','expression',5,'p_expression_opermat','funciones_sint.py',15),
  ('expression -> LPAREN expresionmate RPAREN opmat expression','expression',5,'p_expression_opermat','funciones_sint.py',16),
  ('expresionmate -> term opmat term','expresionmate',3,'p_expresionmate_rel','funciones_sint.py',41),
  ('expression -> expresionlogic','expression',1,'p_expression_logic','funciones_sint.py',57),
  ('expression -> LPAREN expresionlogic RPAREN','expression',3,'p_expression_logic','funciones_sint.py',58),
  ('expression -> expression oplog expresionlogic','expression',3,'p_expression_logic','funciones_sint.py',59),
  ('expression -> expresionlogic oplog expression','expression',3,'p_expression_logic','funciones_sint.py',60),
  ('expression -> expression connectlog expresionlogic','expression',3,'p_expression_logic','funciones_sint.py',61),
  ('expression -> expresionlogic connectlog expression','expression',3,'p_expression_logic','funciones_sint.py',62),
  ('expression -> expression oplog LPAREN expresionlogic RPAREN','expression',5,'p_expression_logic','funciones_sint.py',63),
  ('expression -> LPAREN expresionlogic RPAREN oplog expression','expression',5,'p_expression_logic','funciones_sint.py',64),
  ('expression -> expression connectlog LPAREN expresionlogic RPAREN','expression',5,'p_expression_logic','funciones_sint.py',65),
  ('expression -> LPAREN expresionlogic RPAREN connectlog expression','expression',5,'p_expression_logic','funciones_sint.py',66),
  ('expresionlogic -> term oplog term','expresionlogic',3,'p_expresionlogic_rel','funciones_sint.py',100),
  ('expresionlogic -> boolean connectlog boolean','expresionlogic',3,'p_expresionlogic_bool','funciones_sint.py',120),
  ('boolean -> TRUE','boolean',1,'p_bool_true','funciones_sint.py',128),
  ('boolean -> FALSE','boolean',1,'p_bool_true','funciones_sint.py',129),
  ('connectlog -> AND','connectlog',1,'p_connectlog','funciones_sint.py',135),
  ('connectlog -> OR','connectlog',1,'p_connectlog','funciones_sint.py',136),
  ('oplog -> EQUAL','oplog',1,'p_oplog','funciones_sint.py',141),
  ('oplog -> NOTEQUAL','oplog',1,'p_oplog','funciones_sint.py',142),
  ('oplog -> GREATERTHAN','oplog',1,'p_oplog','funciones_sint.py',143),
  ('oplog -> GREATERTHANEQUAL','oplog',1,'p_oplog','funciones_sint.py',144),
  ('oplog -> LESSERTHAN','oplog',1,'p_oplog','funciones_sint.py',145),
  ('oplog -> LESSERTHANEQUAL','oplog',1,'p_oplog','funciones_sint.py',146),
  ('opmat -> PLUS','opmat',1,'p_opmat','funciones_sint.py',151),
  ('opmat -> MINUS','opmat',1,'p_opmat','funciones_sint.py',152),
  ('opmat -> TIMES','opmat',1,'p_opmat','funciones_sint.py',153),
  ('opmat -> DIVIDE','opmat',1,'p_opmat','funciones_sint.py',154),
  ('opmat -> MOD','opmat',1,'p_opmat','funciones_sint.py',155),
  ('assignacion -> INCREMENT','assignacion',1,'p_assignacion','funciones_sint.py',160),
  ('assignacion -> DECREMENT','assignacion',1,'p_assignacion','funciones_sint.py',161),
  ('assignacion -> COMPASSIGPLUS','assignacion',1,'p_assignacion','funciones_sint.py',162),
  ('assignacion -> COMPASSIGMINUS','assignacion',1,'p_assignacion','funciones_sint.py',163),
  ('assignacion -> COMPASSIGTIMES','assignacion',1,'p_assignacion','funciones_sint.py',164),
  ('assignacion -> COMPASSIGDIVIDE','assignacion',1,'p_assignacion','funciones_sint.py',165),
  ('term -> NUMBER','term',1,'p_term','funciones_sint.py',170),
  ('term -> VARIABLE','term',1,'p_term','funciones_sint.py',171),
  ('expression -> VARIABLE assignacion SEMICOLON','expression',3,'p_expression_preop','funciones_sint.py',177),
  ('expression -> assignacion VARIABLE SEMICOLON','expression',3,'p_expression_postop','funciones_sint.py',182),
  ('oper -> VARIABLE assignacion','oper',2,'p_preop','funciones_sint.py',187),
  ('oper -> assignacion VARIABLE','oper',2,'p_postop','funciones_sint.py',190),
  ('expression -> WHILE LPAREN expresionlogic RPAREN LBRACKET expression RBRACKET','expression',7,'p_expression_while','funciones_sint.py',194),
  ('expression -> FOR LPAREN datos declaracion expresionlogic SEMICOLON oper RPAREN LBRACKET expression RBRACKET','expression',11,'p_expression_for','funciones_sint.py',199),
  ('expression -> IF LPAREN expresionlogic RPAREN LBRACKET expression RBRACKET','expression',7,'p_expression_if','funciones_sint.py',204),
  ('expression -> IF LPAREN expresionlogic RPAREN LBRACKET expression RBRACKET ELSE LBRACKET expression RBRACKET','expression',11,'p_expression_if','funciones_sint.py',205),
  ('datos -> BOOL','datos',1,'p_datos','funciones_sint.py',211),
  ('datos -> BYTE','datos',1,'p_datos','funciones_sint.py',212),
  ('datos -> CHAR','datos',1,'p_datos','funciones_sint.py',213),
  ('datos -> DECIMAL','datos',1,'p_datos','funciones_sint.py',214),
  ('datos -> DOUBLE','datos',1,'p_datos','funciones_sint.py',215),
  ('datos -> FLOAT','datos',1,'p_datos','funciones_sint.py',216),
  ('datos -> INT','datos',1,'p_datos','funciones_sint.py',217),
  ('datos -> LONG','datos',1,'p_datos','funciones_sint.py',218),
  ('datos -> SBYTE','datos',1,'p_datos','funciones_sint.py',219),
  ('datos -> SHORT','datos',1,'p_datos','funciones_sint.py',220),
  ('datos -> UINT','datos',1,'p_datos','funciones_sint.py',221),
  ('datos -> ULONG','datos',1,'p_datos','funciones_sint.py',222),
  ('datos -> USHORT','datos',1,'p_datos','funciones_sint.py',223),
  ('declaracion -> VARIABLE ASSIGNMENT expression SEMICOLON','declaracion',4,'p_declaracion','funciones_sint.py',228),
  ('expression -> datos declaracion','expression',2,'p_expression_decl','funciones_sint.py',231),
  ('expression -> declaracion','expression',1,'p_expression_decl','funciones_sint.py',232),
  ('expression -> IF LPAREN expression RPAREN LBRACKET expression RBRACKET','expression',7,'p_if','funciones_sint.py',237),
  ('expression -> IF LPAREN expression RPAREN LBRACKET expression RBRACKET ELSE LBRACKET expression RBRACKET','expression',11,'p_if','funciones_sint.py',238),
  ('expression -> WHILE LPAREN expression RPAREN LBRACKET expression RBRACKET','expression',7,'p_while','funciones_sint.py',245),
  ('expression -> FOR LPAREN declaracion expression SEMICOLON RPAREN LBRACKET expression RBRACKET','expression',9,'p_for','funciones_sint.py',252),
  ('expression -> LIST LESSERTHAN datos GREATERTHAN term ASSIGNMENT NEW LIST LESSERTHAN datos GREATERTHAN LPAREN RPAREN LBRACKET expression RBRACKET SEMICOLON','expression',17,'p_listas','funciones_sint.py',259),
  ('expression -> term POINT ADD LPAREN term RPAREN SEMICOLON','expression',7,'p_listas_add','funciones_sint.py',266),
  ('expression -> term POINT REMOVE LPAREN term RPAREN SEMICOLON','expression',7,'p_listas_remove','funciones_sint.py',270),
  ('expression -> term POINT REMOVEAT LPAREN term RPAREN SEMICOLON','expression',7,'p_listas_removeAt','funciones_sint.py',274),
  ('expression -> TUPLE LESSERTHAN LPAREN datos COMMA datos RPAREN GREATERTHAN term ASSIGNMENT NEW TUPLE LPAREN datos COMMA datos RPAREN LPAREN term COMMA term RPAREN SEMICOLON','expression',23,'p_tuplas','funciones_sint.py',278),
  ('expression -> term POINT EQUALS LPAREN expression RPAREN SEMICOLON','expression',7,'p_tuplas_equals','funciones_sint.py',285),
  ('expression -> term POINT COMPARETO LPAREN expression RPAREN SEMICOLON','expression',7,'p_tuplas_compareTo','funciones_sint.py',289),
  ('expression -> term POINT ITEM SEMICOLON','expression',4,'p_tuplas_item','funciones_sint.py',293),
]
